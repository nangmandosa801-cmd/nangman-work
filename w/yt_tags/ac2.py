"""자동완성 확인(짧은 출력). 사용: python3 ac2.py <질문파일>
줄마다 「번호|검색어1|검색어2|…」. 검색어 앞에 * 를 붙이면 추천어 3개씩 늘 보여 준다(단지 이름 · 지역 확인용).
출력: 번호 검색어 [N][Y]  E=그대로 있음 · P=이 말로 시작하는 추천어만 있음 · -=없음"""
import json, subprocess, sys, urllib.parse
from concurrent.futures import ThreadPoolExecutor
def get(url):
    return subprocess.run(['curl','-s','--max-time','8','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
norm = lambda s: s.replace(' ','').lower()
def flag(q, L):
    if any(norm(x) == norm(q) for x in L): return 'E'
    if any(norm(x).startswith(norm(q)) for x in L): return 'P'
    return '-'
def one(item):
    lab, q = item
    show = q.startswith('*'); q = q.lstrip('*')
    e = urllib.parse.quote(q)
    nv = get(f'https://ac.search.naver.com/nx/ac?q={e}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    yt = get(f'https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=ko&q={e}')
    try: n = [x[0] for x in json.loads(nv)['items'][0]]
    except Exception: n = []
    try: y = json.loads(yt)[1]
    except Exception: y = []
    fn, fy = flag(q, n), flag(q, y)
    s = f"{lab} {q} [{fn}{fy}]"
    if show or (fn != 'E' and fy != 'E'):
        s += ' → N: ' + ' / '.join(n[:3]) + ' | Y: ' + ' / '.join(y[:3])
    return s[:230]
items = []
for line in open(sys.argv[1], encoding='utf-8'):
    p = [x.strip() for x in line.strip().split('|') if x.strip()]
    if len(p) > 1: items += [(p[0], q) for q in p[1:]]
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(one, items): print(r)
