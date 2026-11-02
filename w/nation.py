import re, urllib.parse, urllib.request, pickle, json
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
REG=['서울','강남','송파','노원','인천','부산','대구','광주','대전','울산','세종',
     '수원','용인','화성','성남','분당','고양','일산','파주','김포','안양','평택',
     '천안','청주','전주','창원','제주','포항','김해','원주']
def scan(r):
    q=r+' 중문'
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=14) as x:
            h=x.read().decode('utf-8','ignore')
    except Exception: return r,None,None
    b=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in b: b.append(m.group(1))
    ads=len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
    return r,b,ads
with ThreadPoolExecutor(5) as ex: R=list(ex.map(scan,REG))
D={r:(b,a) for r,b,a in R}
pickle.dump(D,open('nation.pkl','wb'))
allb=sorted({x for b,a in D.values() if b for x in b})
print('지역 %d · 블로그 %d개' % (len(D), len(allb)))
for r in REG:
    b,a=D.get(r,(None,None))
    print('  %-5s 블로그 %-4s 광고 %-4s' % (r, len(b) if b else '?', a))
