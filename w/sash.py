import re, urllib.parse, urllib.request, pickle, json, os
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
CACHE='saccache.pkl'
C = pickle.load(open(CACHE,'rb')) if os.path.exists(CACHE) else {}

def ac(q):
    if q in C: return C[q]
    try:
        u=AC % urllib.parse.quote(q)
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        items=[i[0] for i in d.get('items',[[]])[0]]
    except Exception:
        items=None
    C[q]=items
    return items

def blogads(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=14) as x:
            h=x.read().decode('utf-8','ignore')
    except Exception: return None,None
    b=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in b: b.append(m.group(1))
    ads=len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
    return b,ads

SPELL=['샷시','새시','샤시','창호','창']
CORE=['샷시 교체','샷시 가격','샷시 비용','샷시 견적','샷시 브랜드','샷시 등급','샷시 시공',
 '샷시 종류','샷시 단열','샷시 결로','샷시 방음','샷시 하자','샷시 as','샷시 실측','샷시 색상',
 '아파트 샷시','발코니 샷시','베란다 샷시','거실 샷시','안방 샷시','확장 샷시','내창','외창',
 '이중창','단창','로이유리','복층유리','시스템창호','발코니 확장','샷시 철거','샷시 리모델링',
 '창호 교체','창호 등급','창호 브랜드','새시 교체','새시 가격','샤시 교체',
 'kcc창호','lx하우시스','이건창호','윈체','대신시스템창호','영림 창호','현대l&c',
 '24평 샷시','32평 샷시','34평 샷시','25평 샷시','샷시 교체 비용','아파트 샷시 교체 비용',
 '샷시 곰팡이','샷시 물맺힘','샷시 방충망','샷시 손잡이','샷시 잠금장치','샷시 롤러',
 '샷시 코킹','샷시 실리콘','샷시 청소','샷시 수리','샷시 문틀','샷시 틈새']

def job(q):
    a=ac(q); b,ad=blogads(q)
    return q,(len(a) if a is not None else -1), (len(b) if b else -1), (ad if ad is not None else -1)

Q=SPELL+CORE
with ThreadPoolExecutor(6) as ex: R=list(ex.map(job,Q))
pickle.dump(C,open(CACHE,'wb'))
pickle.dump(R,open('sash.pkl','wb'))
print('%-24s %4s %4s %4s' % ('검색어','제안','블로그','광고'))
for q,a,b,ad in sorted(R,key=lambda r:(-r[3],-r[1])):
    print('%-24s %4d %4d %4d' % (q,a,b,ad))
