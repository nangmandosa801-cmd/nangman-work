import re, urllib.parse, urllib.request, pickle, json, os
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
def ac(q):
    try:
        u=AC % urllib.parse.quote(q)
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        return [i[0] for i in d.get('items',[[]])[0]]
    except Exception: return None
def blogads(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=14) as x:
            h=x.read().decode('utf-8','ignore')
    except Exception: return None,None
    b=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in b: b.append(m.group(1))
    return b,len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
Q=['lx하우시스','kcc창호','이건창호','현대l&c','윈체','영림','lx지인','kcc글라스',
 '창호 브랜드','창호 비교','샷시 브랜드 비교','창호 브랜드 순위','샷시 브랜드 순위',
 'lx하우시스 창호','kcc 창호 가격','이건창호 가격','lx하우시스 가격','창호 브랜드 추천',
 '수퍼세이브','발코니 샷시','샷시 회사','국산 샷시','시스템창호 브랜드','창호 1등급',
 '창호 열관류율','샷시 열관류율','창호 에너지등급','샷시 1등급']
def job(q):
    a=ac(q); b,ad=blogads(q)
    return q,a,(len(b) if b else -1),(ad if ad is not None else -1)
with ThreadPoolExecutor(6) as ex: R=list(ex.map(job,Q))
pickle.dump(R,open('brand.pkl','wb'))
print('%-22s %4s %4s %4s   제안어' % ('검색어','제안','블로그','광고'))
for q,a,b,ad in R:
    print('%-22s %4d %4d %4d   %s' % (q,len(a) if a else 0,b,ad,' | '.join(a[:6]) if a else ''))
