#!/usr/bin/env python3
"""발행 도우미 html 을 구글 드라이브 「블로그/도우미」에 올리고 목록(JSON)을 「블로그/장부」에 둔다.
사용: python3 helper_cloud.py up      모든 도우미 올리기(이미 같은 크기로 있으면 건너뜀) + 목록 갱신
      python3 helper_cloud.py get <제목 일부>  드라이브에서 받아 /home/claude/w/_cloud/ 에 저장, 경로 출력
목록: /home/claude/w/helper_index.json  {title, name, size, drive_id, local}
"""
import sys, os, re, json, glob, base64
sys.path.insert(0, '/home/claude/helper'); from gas import call
IDX = '/home/claude/w/helper_index.json'; FOLDER = '블로그/도우미'
def scan():
    out = []
    for f in glob.glob('/home/claude/w/**/*.html', recursive=True):
        if '/_cloud/' in f: continue
        try: s = open(f, encoding='utf8', errors='ignore').read()
        except Exception: continue
        m = re.search(r'<div class="t" id="t0">(.*?)</div>', s)
        if m: out.append({'title': re.sub('<[^>]+>', '', m.group(1)).strip(), 'local': f, 'size': os.path.getsize(f)})
    return out
def up():
    have = {x['name']: x for x in (call('ls', path=FOLDER) if True else [])} if _exists() else {}
    idx = []; fail = []
    for h in scan():
        name = os.path.relpath(h['local'], '/home/claude/w').replace('/', '__')
        h['name'] = name; ex = have.get(name)
        if ex and ex.get('size') == h['size']: h['drive_id'] = ex['id']
        else:
            try:
                r = call('fput', path=FOLDER, name=name, b64=base64.b64encode(open(h['local'], 'rb').read()).decode())
                h['drive_id'] = r.get('id') if isinstance(r, dict) else None
            except Exception as e: fail.append((name, str(e)[:80])); h['drive_id'] = None
        idx.append(h)
    json.dump(idx, open(IDX, 'w'), ensure_ascii=False, indent=1)
    call('fput', path='블로그/장부', name='도우미_목록.json', b64=base64.b64encode(open(IDX, 'rb').read()).decode())
    print(json.dumps({'helpers': len(idx), 'uploaded_ok': sum(1 for h in idx if h['drive_id']), 'fail': fail}, ensure_ascii=False))
def _exists():
    try: call('ls', path=FOLDER); return True
    except Exception: return False
def get(q):
    idx = json.load(open(IDX)) if os.path.exists(IDX) else json.loads(base64.b64decode(call('fget', path='블로그/장부', name='도우미_목록.json')['b64']))
    for h in idx:
        if q in h['title'] or q in h['name']:
            p = h['local'] if os.path.exists(h['local']) else None
            if not p:
                os.makedirs('/home/claude/w/_cloud', exist_ok=True); p = '/home/claude/w/_cloud/' + h['name']
                open(p, 'wb').write(base64.b64decode(call('fget', path=FOLDER, name=h['name'])['b64']))
            print(p); return
    print('not_found')
if __name__ == '__main__':
    up() if sys.argv[1] == 'up' else get(sys.argv[2])
