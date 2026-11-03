#!/usr/bin/env python3
"""발행 뒤 후속 한 번에 (사용자 11/3 「발행 뒤 후속을 프로그램 하나로 묶기」)
사용: python3 post_followup.py [logNo ...]      인자 없으면 champion_chart 최근 글 중 아직 안 한 글 전부
하는 일(글마다):
  1) 네이버 글 목록(PostTitleListAsync)에서 제목 · 번호 확인
  2) /home/claude/ipjuhub/posts.json 추가 · /home/claude/watch/mix_schedule_1017c.json 상태 published
  3) 꼬리 링크 도우미 linkhelp.py 한 번(새 글 여러 편을 같이)
  4) 같은 제목의 발행 도우미 html(/home/claude/w/**)을 찾아 소제목 · 사진으로 세로 클립 자동 생성(vert.py)
     + _info.txt (캡션 100자 안 · 해시태그 5개)
  5) 상태 /home/claude/tools/followup/state.json (done) 저장
출력: JSON 한 줄. SNS 자동 배포는 정기 작업 「네이버 발행 → 전 채널」이 맡는다(여기서 안 함).
"""
import sys, os, re, json, glob, base64, html, subprocess, urllib.request, urllib.parse
D = os.path.dirname(os.path.abspath(__file__)); ST = f'{D}/state.json'
POSTS = '/home/claude/ipjuhub/posts.json'; SCHED = '/home/claude/watch/mix_schedule_1017c.json'
OUT = '/mnt/user-data/outputs/int/clip_sigong'; MP4 = '/home/claude/int/mp4_1015'
BLOG = 'champion_chart'; PHONE = '010-2882-8165'
def jload(p, d):
    try: return json.load(open(p))
    except Exception: return d
def recent(n=30):
    u = f'https://blog.naver.com/PostTitleListAsync.naver?blogId={BLOG}&currentPage=1&countPerPage={n}'
    s = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read().decode('utf8', 'ignore')
    return [(no, urllib.parse.unquote_plus(t)) for no, t in re.findall(r'"logNo":"(\d+)","title":"(.*?)"', s)]
def norm(t): return re.sub(r'[^가-힣A-Za-z0-9]', '', html.unescape(t))
_HELP = None
def helpers():
    global _HELP
    if _HELP is None:
        _HELP = {}
        for f in glob.glob('/home/claude/w/**/*.html', recursive=True):
            try: s = open(f, encoding='utf8', errors='ignore').read()
            except Exception: continue
            for m in re.finditer(r'<div class="t" id="(t\d+)">(.*?)</div>', s):
                _HELP.setdefault(norm(m.group(2))[:30], (f, m.group(1).replace('t', 'h')))
    return _HELP
def find_helper(title):
    k = norm(title)[:30]; H = helpers()
    if k in H: return H[k]
    for kk, v in H.items():
        if kk[:18] == k[:18]: return v
    # 이 창에 파일이 없으면 구글 드라이브 「블로그/도우미」에서 받아 온다(11/3)
    try:
        r = subprocess.run(['python3', f'{D}/helper_cloud.py', 'get', title[:14]], capture_output=True, text=True, timeout=120).stdout.strip()
        if r.endswith('.html') and os.path.exists(r):
            s = open(r, encoding='utf8', errors='ignore').read()
            m = re.search(r'<div class="t" id="(t\d+)">', s)
            if m: return (r, m.group(1).replace('t', 'h'))
    except Exception: pass
    return None
def body_of(f, hid):
    s = open(f, encoding='utf8', errors='ignore').read()
    i = s.find(f'id="{hid}"'); j = s.find('</details>', i)
    return s[i:j if j > 0 else None]
def short(t, n=13):
    t = re.sub(r'[?？!.]', '', html.unescape(re.sub('<[^>]+>', '', t))).strip()
    w = t.split(); lines = ['']
    for x in w:
        if len(lines[-1]) + len(x) + 1 > n and lines[-1]: lines.append(x)
        else: lines[-1] = (lines[-1] + ' ' + x).strip()
    return '\n'.join(lines[:2])
def make_clip(no, title, slug):
    h = find_helper(title)
    if not h: return 'helper_not_found'
    f, hid = h; b = body_of(f, hid)
    tmp = f'{MP4}/auto_{slug}'; os.makedirs(tmp, exist_ok=True)
    # 소제목과 사진을 문서 순서대로
    items = []
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>|<img[^>]*src="data:image/(jpeg|png);base64,([^"]+)"', b):
        if m.group(1): items.append(('h', m.group(1)))
        else: items.append(('i', (m.group(2), m.group(3))))
    heads = [x for k, x in items if k == 'h']
    slides = []; cur = heads[0] if heads else title
    k = 0
    for kind, x in items:
        if kind == 'h': cur = x; continue
        ext, data = x; k += 1
        p = f'{tmp}/{k:02d}.{"jpg" if ext == "jpeg" else "png"}'
        open(p, 'wb').write(base64.b64decode(data))
        slides.append({'src': p, 'line': short(cur), 'sub': '낭만 인테리어 · 제휴 시공 사례'})
    # 겹치는 소제목은 한 장만, 최대 5장
    seen = set(); pick = []
    for s_ in slides:
        if s_['line'] in seen: continue
        seen.add(s_['line']); pick.append(s_)
    pick = pick[:5]
    if len(pick) < 3: return 'too_few_photos'
    head, _, rest = title.partition(',')
    spec = {'head': [head.strip(), short(rest or title, 16).replace('\n', ' ')], 'what': head.strip(),
            'vintro': [{'kicker': head.strip(), 'line': short(rest or title), 'sub': f'문의 {PHONE}'}],
            'slides': pick}
    sp = f'{MP4}/spec_auto_{slug}.json'; json.dump(spec, open(sp, 'w'), ensure_ascii=False, indent=1)
    mp4 = f'{OUT}/nangman_interior_{slug}_clip.mp4'
    r = subprocess.run(['python3', 'vert.py', sp, slug, mp4, '11'], cwd=MP4, capture_output=True, text=True, timeout=900)
    if not os.path.exists(mp4): return 'vert_fail:' + r.stderr[-200:]
    tags = re.findall(r'#[가-힣A-Za-z0-9]+', re.sub('<[^>]+>', ' ', b))
    tags = [t for t in dict.fromkeys(tags) if t != '#낭만인테리어'][:4] + ['#낭만인테리어']
    lead = head.strip() + ', ' + (rest.strip() if rest else '')
    cap = lead
    while len(cap + ' ' + ' '.join(tags)) > 100: cap = cap[:-1]
    cap = cap.rstrip(' ,·') + ' ' + ' '.join(tags)
    info = (f'블로그 원제목\n{title}\n\n파일: nangman_interior_{slug}_clip.mp4\n\n[ 네이버 클립 ]\n\n캡션 ({len(cap)}자)\n{cap}\n\n'
            f'대표 이미지\nnangman_interior_{slug}_clip_cover.jpg\n\n연결할 글\n{title}\nhttps://blog.naver.com/{BLOG}/{no}\n\n'
            f'고정 댓글\n전화 · 문자 {PHONE} · 사진 한 장 보내 주시면 무료로 봐 드립니다\n\n[ 장면 ]\n' +
            '\n'.join(f'{i+1}  {x["line"].replace(chr(10), " ")}' for i, x in enumerate(spec['vintro'] + pick)) +
            f'\n\n[ 자료 ]\n시공 사진은 제휴 업체 사례(NI 번호)\n')
    open(f'{OUT}/nangman_interior_{slug}_clip_info.txt', 'w').write(info)
    up = drive_put(slug)
    return 'ok' + (' · drive' if up else '')
def drive_put(slug):
    """PC 대신 구글 드라이브 「블로그/shorts」에 저장 + info.txt 맨 아래에 다운로드 링크 넣기(11/3 사용자 「다운 받게 만들어야지」)."""
    if not os.path.exists('/home/claude/gas/conf.json'): return False
    sys.path.insert(0, '/home/claude/helper'); from gas import call
    links = {}
    for ext in ('_clip.mp4', '_clip_cover.jpg'):
        f = f'{OUT}/nangman_interior_{slug}{ext}'
        if os.path.exists(f):
            r = call('fput', path='블로그/shorts', name=os.path.basename(f), b64=base64.b64encode(open(f, 'rb').read()).decode())
            try: links[ext] = call('flink', id=r['id'])['url']
            except Exception: pass
    fi = f'{OUT}/nangman_interior_{slug}_clip_info.txt'
    if os.path.exists(fi):
        t = open(fi, encoding='utf8').read().split('\n[ 다운로드 ]')[0].rstrip('\n')
        t += '\n\n[ 다운로드 ]\n영상: ' + links.get('_clip.mp4', '') + '\n커버: ' + links.get('_clip_cover.jpg', '') + '\n'
        open(fi, 'w', encoding='utf8').write(t)
        call('fput', path='블로그/shorts', name=os.path.basename(fi), b64=base64.b64encode(t.encode('utf8')).decode())
    return True
def slug_of(f):
    b = os.path.basename(f).replace('.html', '')
    return re.sub(r'[^a-z0-9_]', '', b.lower()) or 'post'
def main():
    st = jload(ST, {'done': []}); done = set(st['done'])
    R = recent(); want = set(sys.argv[1:])
    todo = [(no, t) for no, t in R if (no in want) or (not want and no not in done)]
    if not want: todo = todo[:12]
    P = jload(POSTS, []); S = jload(SCHED, []); res = []
    for no, t in todo:
        u = f'https://blog.naver.com/{BLOG}/{no}'
        if not any(p.get('u') == u for p in P): P.insert(0, {'b': '낭만 인테리어', 'u': u, 't': t})
        for s in S:
            if norm(s.get('title', ''))[:18] == norm(t)[:18]: s['logNo'] = no; s['state'] = 'published'
        h = find_helper(t); slug = slug_of(h[0]) if h else f'post{no}'
        clip = 'skip_exists' if os.path.exists(f'{OUT}/nangman_interior_{slug}_clip.mp4') else make_clip(no, t, slug)
        res.append({'no': no, 'title': t[:30], 'helper': bool(h), 'clip': clip}); done.add(no)
    json.dump(P, open(POSTS, 'w'), ensure_ascii=False, indent=1); json.dump(S, open(SCHED, 'w'), ensure_ascii=False, indent=1)
    lh = ''
    if todo:
        r = subprocess.run(['python3', '/home/claude/ipjuhub/linkhelp.py'] + [n for n, _ in todo], capture_output=True, text=True, timeout=300)
        lh = r.stdout.strip().splitlines()[-1:] if r.stdout else r.stderr[-120:]
    st['done'] = sorted(done); json.dump(st, open(ST, 'w'))
    print(json.dumps({'posts': res, 'linkhelp': lh}, ensure_ascii=False))
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--seed':   # 이미 처리한 글을 done으로만 표시
        st = jload(ST, {'done': []}); st['done'] = sorted(set(st['done']) | set(sys.argv[2:])); json.dump(st, open(ST, 'w')); print('seeded')
    else: main()
