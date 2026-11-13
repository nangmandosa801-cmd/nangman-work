#!/usr/bin/env python3
# 낭만 작업 저장소 동기화 (11/13 고침 · sync.sh · restore.sh 가 이 파일을 부른다)
#
# 왜 바꿨나: 예전 sync.sh 는 「이 창의 /home/claude 파일을 통째로 저장소에 덮어쓰기」였다. 오래 열어 둔 창이
#   git pull → restore(있는 파일은 안 바꿈) → sync 를 하면, 다른 창이 고친 새 파일을 이 창의 옛 파일로 되돌렸다.
#   (11/13 09:47 한 번에 381개 · gas.py 는 11/3부터 40번 왔다 갔다 · 링크 3개 · 인테리어 링크 금지 같은 규칙이 계속 되살아남)
#
# 이제는 파일마다 따진다. 기준 = /home/claude/.sync_base.json (이 창이 저장소와 마지막으로 같았던 때의 파일 해시)
#   · 이 창만 고친 파일        → 저장소로 올림
#   · 저장소만 바뀐 파일        → 이 창 파일을 새것으로 바꿈(옛 파일은 /home/claude/.stale_bak/<시각>/ 에 남김)
#   · 둘 다 고친 파일           → 합침(CLAUDE.md 는 양쪽 줄을 모두 남김). 못 합치면 「나중에 만들어진 내용」이 이기고 목록을 찍음
#   · 기준이 없는 파일(처음)    → 저장소 기록에 있는 옛 내용이면 이 창이 낡은 것 → 새것으로 바꿈. 기록에 없는 내용이면 이 창이 새로 쓴 것
#
# 쓰기:  python3 sync.py sync [--dry]     고친 것 올리기(끝낼 때)
#        python3 sync.py restore [--dry]  저장소 → 이 창(시작할 때 · git pull 뒤)
# 커밋 글 끝에 붙일 줄이 있으면 환경 변수 SYNC_TRAILER 에.
import os, sys, subprocess, hashlib, json, time, shutil, tempfile

R = os.environ.get('SYNC_REPO', '/home/claude/nangman-work'); H = os.environ.get('SYNC_HOME', '/home/claude')   # 시험할 때만 바꿈
DIRS = 'tools ipjuhub watch int/mp4_1015 w helper gcontacts kit spread gas coffee 텍스트 jisan jisan_move'.split()
BASE = H + '/.sync_base.json'
BAK = H + '/.stale_bak/' + time.strftime('%m%d_%H%M%S')
EXT = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mp3', '.wav', '.pkl', '.pdf', '.zip')
NEVER = {'gas/conf.json', 'gas/key.txt', 'gas/setup.html', 'helper/Code.gs'}   # 열쇠 · 로그인 — 저장소에 안 담음
MAXB = 1048576           # 예전 find -size -2M 과 같은 뜻(1MiB 이하만)
ID = ['-c', 'user.name=nangman', '-c', 'user.email=nangmandosa801@users.noreply.github.com']


def git(*a, check=False):
    r = subprocess.run(['git', '-C', R, '-c', 'core.quotepath=false', *a], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit('git %s 실패: %s' % (a[0], (r.stderr or r.stdout or '')[-400:]))
    return r


def keep(rel):
    """저장소에 올려도 되는 파일인가(그림 · 영상 · 데이터 덩어리 · 열쇠 · 백업은 뺌)"""
    parts = rel.split('/'); b = parts[-1]
    if rel in NEVER or b in ('token.json', 'client.json'): return False
    if b.lower().endswith(EXT) or '.bak' in b or '__pycache__' in parts: return False
    if any(p.startswith('bak') for p in parts[:-1]): return False
    return True


def bh(path):
    """git blob 해시(없으면 None)"""
    try:
        if os.path.islink(path) or not os.path.isfile(path): return None
        d = open(path, 'rb').read()
    except OSError:
        return None
    return hashlib.sha1(b'blob %d\0' % len(d) + d).hexdigest()


def pairs():
    """(rel, 이 창 경로, 저장소 경로) — 양쪽 어느 한 곳에라도 있는 파일"""
    seen = {}
    for d in DIRS:
        for top, side in ((os.path.join(H, d), 'l'), (os.path.join(R, d), 'r')):
            if not os.path.isdir(top): continue
            for root, dirs, files in os.walk(top):
                dirs[:] = [x for x in dirs if x != '.git']
                for f in files:
                    inner = os.path.relpath(os.path.join(root, f), top)
                    if inner.startswith('kin'): continue
                    rel = d + '/' + inner
                    seen.setdefault(rel, (os.path.join(H, rel), os.path.join(R, rel)))
    for f in os.listdir(H):                       # /home/claude 바로 아래 py · sh · md ↔ root/
        p = os.path.join(H, f)
        if os.path.isfile(p) and f.endswith(('.py', '.sh', '.md')):
            seen.setdefault('root/' + f, (p, os.path.join(R, 'root', f)))
    rr = os.path.join(R, 'root')
    if os.path.isdir(rr):
        for f in os.listdir(rr):
            if os.path.isfile(os.path.join(rr, f)):
                seen.setdefault('root/' + f, (os.path.join(H, f), os.path.join(rr, f)))
    return [(k, v[0], v[1]) for k, v in sorted(seen.items())]


def history():
    """(경로, blob) → 그 내용이 저장소에 처음 나타난 시각"""
    first = {}
    ct = 0
    out = git('log', '--raw', '--no-abbrev', '--no-renames', '--format=C %ct').stdout
    for ln in out.split('\n'):
        if ln.startswith('C '):
            ct = int(ln[2:]); continue
        if ln.startswith(':') and '\t' in ln:
            meta, path = ln.split('\t', 1); k = (path, meta.split()[3])
            if k not in first or ct < first[k]: first[k] = ct
    return first


def merge3(rel, lp, rp, hb):
    """둘 다 고친 파일 합치기. 깨끗하게 합쳐지면 bytes, 아니면 None"""
    r = subprocess.run(['git', '-C', R, 'cat-file', 'blob', hb], capture_output=True)
    if r.returncode: return None
    with tempfile.NamedTemporaryFile(delete=False) as t:
        t.write(r.stdout); bp = t.name
    try:
        a = ['git', 'merge-file', '-p'] + (['--union'] if os.path.basename(rel) == 'CLAUDE.md' else []) + [lp, bp, rp]
        m = subprocess.run(a, capture_output=True)
        return m.stdout if m.returncode == 0 else None
    finally:
        os.unlink(bp)


def put(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def backup(rel, lp):
    if os.path.isfile(lp):
        b = os.path.join(BAK, rel); os.makedirs(os.path.dirname(b), exist_ok=True); shutil.copy2(lp, b)


def run(mode, dry):
    base = {}
    if os.path.isfile(BASE):
        try: base = json.load(open(BASE, encoding='utf8'))
        except Exception: base = {}
    if not dry:
        if mode == 'sync' and git('status', '--porcelain').stdout.strip():      # 저장소 폴더에서 바로 고친 것(CLAUDE.md 등)
            git('add', '-A'); git(*ID, 'commit', '-qm', '저장소에서 바로 고친 것 ' + time.strftime('%m%d_%H%M') + ('\n\n' + os.environ['SYNC_TRAILER'] if os.environ.get('SYNC_TRAILER') else ''))
        p = git('pull', '-q', '--rebase', '--autostash', '-X', 'theirs', 'origin', 'main')
        if p.returncode:
            git('rebase', '--abort')
            msg = (p.stderr or p.stdout or '').strip().split('\n')[-1][:200]
            if mode == 'sync':
                print(json.dumps({'ok': False, 'why': 'pull 실패 — 올리지 않음(이 창 파일은 그대로)', 'git': msg}, ensure_ascii=False)); return 2
            print('pull 실패(지금 있는 저장소 사본으로 진행): ' + msg)
    first = None
    n = dict(push=0, pull=0, merged=0, same=0); notes = []; touched = []
    for rel, lp, rp in pairs():
        hl, hr, hb = bh(lp), bh(rp), base.get(rel)
        if hl == hr:
            if hl: base[rel] = hl; n['same'] += 1
            continue
        act = None; data = None
        if hl is None:
            act = 'pull' if rel not in NEVER else None
        elif hr is None:
            if hb == hl: act = None                                   # 저장소에서 지워진 파일 — 되살리지 않음
            elif keep(rel) and os.path.getsize(lp) <= MAXB: act = 'push'
        elif hb == hl: act = 'pull'
        elif hb == hr: act = 'push' if keep(rel) and os.path.getsize(lp) <= MAXB else None
        else:
            if hb: data = merge3(rel, lp, rp, hb)
            if data is not None: act = 'merged'
            else:
                if first is None: first = history()
                tl = first.get((rel, hl)) or os.path.getmtime(lp)
                tr = first.get((rel, hr)) or 0
                act = 'push' if tl > tr else 'pull'
                if act == 'push' and not (keep(rel) and os.path.getsize(lp) <= MAXB): act = None
                if (rel, hl) not in first and act == 'pull':
                    notes.append('이 창에서 고친 내용이 저장소 새 내용에 밀림(옛 파일은 .stale_bak 에): ' + rel)
                elif hb:
                    notes.append('둘 다 고쳐 못 합침 → %s 쪽을 씀: %s' % ('이 창' if act == 'push' else '저장소', rel))
        if act is None: continue
        if mode == 'restore' and act in ('push', 'merged'): continue    # 시작할 때는 이 창 파일만 새것으로
        n[act] += 1; touched.append((act, rel))
        if dry: continue
        if act == 'push': put(lp, rp)
        elif act == 'pull': backup(rel, lp); put(rp, lp)
        else:
            backup(rel, lp)
            open(lp, 'wb').write(data); put(lp, rp)
        base[rel] = bh(rp)
    res = dict(mode=mode, dry=dry, **n)
    if mode == 'sync' and not dry:
        git('add', '-A')
        if git('status', '--porcelain').stdout.strip():
            msg = '작업 파일 동기화 ' + time.strftime('%m%d_%H%M')
            if os.environ.get('SYNC_TRAILER'): msg += '\n\n' + os.environ['SYNC_TRAILER']
            git(*ID, 'commit', '-qm', msg, check=True)
        ahead = git('rev-list', '--count', 'origin/main..HEAD').stdout.strip()
        res['pushed'] = False
        if ahead and ahead != '0':
            for _ in range(3):
                if git('push', '-q', 'origin', 'HEAD:main').returncode == 0:
                    res['pushed'] = True; break
                if git('pull', '-q', '--rebase', '-X', 'theirs', 'origin', 'main').returncode: git('rebase', '--abort'); time.sleep(3)
            if not res['pushed']: res['why'] = 'push 실패 — 다음 sync 때 다시 올라감'
        else:
            res['nochange'] = True
    if not dry:
        json.dump(base, open(BASE, 'w', encoding='utf8'), ensure_ascii=False)
        if n['pull'] or n['merged']: res['옛파일'] = BAK
    if notes: res['notes'] = notes[:30]
    if dry or '-v' in sys.argv: res['files'] = touched[:200]
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    os.environ.setdefault('TZ', 'Asia/Seoul'); time.tzset()
    mode = sys.argv[1] if len(sys.argv) > 1 else 'sync'
    if mode not in ('sync', 'restore'): raise SystemExit('쓰기: sync.py sync|restore [--dry]')
    sys.exit(run(mode, '--dry' in sys.argv))
