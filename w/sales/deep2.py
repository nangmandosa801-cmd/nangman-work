import re, subprocess, json, urllib.parse, html
from concurrent.futures import ThreadPoolExecutor
def get(u, ua='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'):
    return subprocess.run(['curl','-sL','--max-time','20','-A',ua,u],capture_output=True,text=True).stdout
# 1) 글 안 연락 수단
rows = json.load(open('rss.json'))
for no in [rows[0][1], rows[27][1]]:
    h = get(f'https://m.blog.naver.com/PostView.naver?blogId=champion_chart&logNo={no}')
    for k in ['open.kakao', 'tel:']:
        for m in list(re.finditer(re.escape(k), h))[:2]:
            s = re.sub(r'\s+', ' ', h[max(0, m.start()-160): m.start()+120])
            print('POST', no, k, '…', s[:260])
    body = h[h.find('se-main-container'):] if 'se-main-container' in h else ''
    print('POST', no, 'body len', len(body), 'body links:', len(re.findall(r'<a [^>]*href="http', body)), 'kakao in body:', 'open.kakao' in body, '| 댓글 수 표기:', re.findall(r'"commentCount":(\d+)', h)[:1])
h = get('https://m.blog.naver.com/champion_chart')
for m in list(re.finditer('tel:', h))[:1]:
    print('HOME tel …', re.sub(r'\s+',' ', h[max(0,m.start()-200): m.start()+80])[:260])
# 2) 지역 x 종목 자동완성(네이버) — 수요 신호
grid = {
 '곰팡이제거': ['대구','창원','부산','울산','인천','수원','성남','하남'],
 '단열시공': ['대구','창원','부산','울산','인천','수원'],
 '결로': ['대구','창원','부산','인천'],
 '누수탐지': ['하남','성남','송파','강동','구리','남양주','부산','울산','청주','인천','수원','대구'],
 '보일러 교체': ['하남','강동','구리','남양주','성남'],
 '보일러 수리': ['하남','강동','구리','남양주'],
 '중문': ['동탄','화성','인천','시흥','부산','대전','수원','평택','김포','남양주','하남','대구'],
 '무타공 중문': ['부산','인천','대구','수원','김포'],
 '창틀 코킹': ['서울','인천','수원','동탄','부산','대구'],
 '새집증후군': ['평택','인천','수원','고양','부산','대구','포항'],
 '입주청소': ['평택','인천','수원','시흥','부산','울산','전주','포항'],
 '도어락': ['의정부','노원','양주'],
 '욕실문 교체': ['파주','고양','하남'],
}
def ac(q):
    e = urllib.parse.quote(q)
    r = get(f'https://ac.search.naver.com/nx/ac?q={e}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    try: L = [x[0] for x in json.loads(r)['items'][0]]
    except Exception: L = []
    n = lambda s: s.replace(' ','')
    ex = any(n(x) == n(q) for x in L); buy = [x for x in L if re.search(r'가격|비용|업체|견적|추천|잘하는', x)]
    return q, len(L), ex, len(buy)
qs = [f'{r} {t}' for t, R in grid.items() for r in R]
with ThreadPoolExecutor(8) as ex: res = list(ex.map(ac, qs))
json.dump(res, open('grid.json','w'), ensure_ascii=False)
i = 0
for t, R in grid.items():
    line = []
    for r in R:
        q, n, e, b = res[i]; i += 1
        line.append(f"{r}{n}{'★' if e else ''}{'/살'+str(b) if b else ''}")
    print(f'{t}: ' + ' · '.join(line))
