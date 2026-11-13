"""자동완성 확인. 사용: python3 ac.py <질문파일>  (줄마다 「번호|검색어1|검색어2|…」)
네이버 · 유튜브 자동완성 위쪽 5개를 한 줄씩 찍는다. 태그는 여기 나온 말만 쓴다."""
import json, subprocess, sys, urllib.parse
from concurrent.futures import ThreadPoolExecutor
def get(url):
    return subprocess.run(['curl','-s','--max-time','8','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
def one(item):
    lab, q = item
    e = urllib.parse.quote(q)
    nv = get(f'https://ac.search.naver.com/nx/ac?q={e}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    yt = get(f'https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=ko&q={e}')
    try: n = [x[0] for x in json.loads(nv)['items'][0]][:5]
    except Exception: n = ['ERR']
    try: y = json.loads(yt)[1][:5]
    except Exception: y = ['ERR']
    return f"{lab}:{q} | N: {' / '.join(n)} | Y: {' / '.join(y)}"
items = []
for line in open(sys.argv[1], encoding='utf-8'):
    p = [x.strip() for x in line.strip().split('|') if x.strip()]
    if len(p) > 1: items += [(p[0], q) for q in p[1:]]
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(one, items): print(r[:300])
