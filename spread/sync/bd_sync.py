#!/usr/bin/env python3
"""낭만 부동산 채널 동기화 장부 (11/10 사용자 「부동산 관련 모든 채널 동기화 · 같은 주제 다른 내용 · 링크 서로 연계 · 네이버 밖으로 나가는 건 소수화 · 클립을 본문에」)
규칙 전문: /home/claude/spread/sync/SYNC.md

  python3 bd_sync.py scan                 네이버 dong_jin_kim 1~2쪽 → 새 글을 topics.json 에 더함(JSON 한 줄)
  python3 bd_sync.py todo [N]             할 일 N개(기본 2편) · 채널 순서대로 빈 칸
  python3 bd_sync.py set <logNo> <ch> <값>  채널 결과 적기(주소 · 드라이브 id · '예약 …' · 'skip:이유')
  python3 bd_sync.py links <logNo> <ch> [k] 그 채널 글 끝에 붙일 「같이 보면 좋은 글」 k개(기본 5) JSON
  python3 bd_sync.py block <logNo> <ch>   위 링크를 그 채널용 html 조각으로(<!--BDREL--> … <!--/BDREL-->)
  python3 bd_sync.py relink [N]           새 주소가 생겨 꼬리 링크가 바뀌어야 할 구글 블로그 글 N개를 gas.py patch 로 고침
  python3 bd_sync.py show <logNo>
채널: clip(세로 영상 · 드라이브 id) · naverclip(어사이드 지시 · 본문 삽입) · blogger · tistory · threads · insta · youtube
"""
import json, os, re, sys, time, subprocess
D = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.join(D, 'topics.json')
sys.path.insert(0, '/home/claude/spread'); sys.path.insert(0, '/home/claude/helper')
NAV = 'https://blog.naver.com/dong_jin_kim/'
ORDER = ['clip', 'naverclip', 'blogger', 'tistory', 'threads', 'insta', 'youtube']
BUNYANG = re.compile(r'분양가|청약|줍줍|무순위|모집공고')
STOP = set('아파트 매매 전세 시세 분양가 청약 입주 이주 일정 위치 개발 84㎡ 59㎡ 새 옆 단지 서울 경기 수도권 올해 1년 2년'.split())

def load():
    return json.load(open(TOP)) if os.path.exists(TOP) else {'topics': {}, 'since': '224462880000'}
def save(s): json.dump(s, open(TOP, 'w'), ensure_ascii=False, indent=1)
def head(t): return t.split(',')[0].strip()
def words(t, full=False):
    h = t if full else head(t)
    return {re.sub(r'(동|역|시|구)$','',w) or w for w in re.findall(r'[가-힣A-Za-z0-9]{2,}', h) if w not in STOP and not re.fullmatch(r'[0-9,]+[가-힣]*', w)}

def scan():
    from fetch import page
    s = load(); T = s['topics']; new = []
    for n in (1, 2):
        for p in page(n):
            k = str(p['logNo'])
            if k in T or k < s['since']: continue
            T[k] = dict(title=p['title'], naver=NAV + k, found=time.strftime('%Y-%m-%d %H:%M', time.gmtime(time.time()+9*3600)),
                        bunyang=bool(BUNYANG.search(p['title'])), ch={})
            new.append(k)
    save(s); print(json.dumps({'new': len(new), 'logNos': new, 'total': len(T)}, ensure_ascii=False))

def todo(n=2):
    s = load(); out = []
    for k in sorted(s['topics'], reverse=True):          # 새 글 먼저
        t = s['topics'][k]; miss = []
        for c in ORDER:
            if c in t['ch']: continue
            if c == 'tistory' and t['bunyang']: continue   # 티스토리 개편: 분양가 · 청약 글 안 씀
            miss.append(c)
        if miss: out.append(dict(logNo=k, title=t['title'], missing=miss))
        if len(out) >= n: break
    print(json.dumps(out, ensure_ascii=False, indent=0))

def setv(k, c, v):
    s = load(); s['topics'][k]['ch'][c] = v; s['topics'][k]['ch'][c + '_at'] = time.strftime('%m-%d %H:%M', time.gmtime(time.time()+9*3600)); save(s)
    print(json.dumps({'ok': True, 'logNo': k, c: v}, ensure_ascii=False))

def url_of(t, c):
    v = t['ch'].get(c, '')
    return v if isinstance(v, str) and v.startswith('http') else ''

def related(k, c, kk=5):
    s = load(); T = s['topics']; me = T[k]; w = words(me['title'])
    allp = json.load(open('/home/claude/spread/all_posts.json'))
    pool = {**{p['logNo']: p['title'] for p in allp}, **{x: T[x]['title'] for x in T}}
    sc = []
    for x, ti in pool.items():
        if x == k: continue
        o = 2 * len(w & words(ti, True)) + len(words(me['title'], True) & words(ti, True))
        if o >= 2: sc.append((o, x, ti))
    sc.sort(key=lambda z: (-z[0], -int(z[1])))
    res = []
    for o, x, ti in sc[:kk * 2]:
        t = T.get(x)
        u = (url_of(t, c) if t else '') or NAV + x      # 같은 채널 주소가 있으면 그쪽, 없으면 네이버 원문
        res.append(dict(logNo=x, title=ti, url=u, same=bool(t and url_of(t, c))))
    if len(res) < kk:                                     # 모자라면 같은 채널에 이미 올라간 최근 글로 채움
        for x in sorted(T, reverse=True):
            if x == k or any(r['logNo'] == x for r in res): continue
            u = url_of(T[x], c)
            if u: res.append(dict(logNo=x, title=T[x]['title'], url=u, same=True))
            if len(res) >= kk: break
    res.sort(key=lambda r: not r['same'])                 # 같은 채널 글 먼저(채널 안에서 돌게)
    return res[:kk]

def block(k, c):
    rs = related(k, c)
    li = ''.join(f'<li><a href="{r["url"]}">{r["title"]}</a></li>' for r in rs)
    me = load()['topics'][k]
    return (f'<!--BDREL--><h3>같이 보면 좋은 글</h3><ul>{li}</ul>'
            f'<p>원문 분석 · 표 전체: <a href="{me["naver"]}">{me["title"]}</a></p><!--/BDREL-->')

def relink(n=5):
    """구글 블로그 글 꼬리를 최신 주소로. 바뀐 글만 patch."""
    from gas import call, BLOG
    s = load(); done = 0; log = []
    for k, t in s['topics'].items():
        u = url_of(t, 'blogger')
        if not u or done >= n: continue
        want = block(k, 'blogger')
        if t['ch'].get('blogger_rel') == want: continue
        try:
            path = '/' + u.split('.com/', 1)[1]
            post = call('get', blogId=BLOG['budongsan'], path=path)
            html = post.get('html') or post.get('content', '')
            new = re.sub(r'<!--BDREL-->.*?<!--/BDREL-->', want, html, flags=re.S) if '<!--BDREL-->' in html else html + want
            if new != html:
                call('patch', blogId=BLOG['budongsan'], postId=post['id'], html=new)
            t['ch']['blogger_rel'] = want; done += 1; log.append(k)
        except Exception as e:
            log.append(f'{k}:err {e}')
    save(s); print(json.dumps({'relinked': log}, ensure_ascii=False))

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    if a[0] == 'scan': scan()
    elif a[0] == 'pool':      # 네이버 발행 글 목록 새로 고침(링크 고를 때 씀)
        from fetch import page
        L = []
        for n in range(1, int(a[1]) if len(a) > 1 else 12):
            try: P = page(n)
            except Exception: break
            if not P: break
            L += P
        json.dump(L, open('/home/claude/spread/all_posts.json', 'w'), ensure_ascii=False); print(json.dumps({'pool': len(L)}))
    elif a[0] == 'todo': todo(int(a[1]) if len(a) > 1 else 2)
    elif a[0] == 'set': setv(a[1], a[2], ' '.join(a[3:]))
    elif a[0] == 'links': print(json.dumps(related(a[1], a[2], int(a[3]) if len(a) > 3 else 5), ensure_ascii=False, indent=0))
    elif a[0] == 'block': print(block(a[1], a[2]))
    elif a[0] == 'relink': relink(int(a[1]) if len(a) > 1 else 5)
    elif a[0] == 'show': print(json.dumps(load()['topics'][a[1]], ensure_ascii=False, indent=1))
