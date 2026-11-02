import re, json, urllib.parse, urllib.request, pickle
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
def ac(w):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(w)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0'
       '&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=8) as r:
            return [i[0] for i in json.loads(r.read().decode('utf-8')).get('items',[[]])[0]]
    except Exception: return None
def comp(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=12) as r:
            h=r.read().decode('utf-8','ignore')
    except Exception: return None,None
    b=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in b: b.append(m.group(1))
    return b, len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))

GONG=['샷시','도배','화장실 리모델링','욕실 리모델링','올수리','중문','싱크대','장판','필름']
REG=['구리','남양주','다산','별내','갈매']
DANJI=['갈매역아이파크','구리갈매푸르지오','다산자이','다산신도시자연앤이편한세상',
       '별내아이파크','인창주공','토평마을','덕소두산위브','평내호평 KCC스위첸','e편한세상인창']
Q1=[r+' '+g for r in REG[:2] for g in GONG]
Q2=[d+' 인테리어' for d in DANJI]
Q=Q1+Q2
with ThreadPoolExecutor(16) as ex: acs=dict(zip(Q, ex.map(ac,Q)))
with ThreadPoolExecutor(6) as ex: cps=dict(zip(Q, ex.map(comp,Q)))
pickle.dump((acs,cps),open('deep.pkl','wb'))
def show(title, qs):
    print('\n===== %s =====' % title)
    rows=[]
    for q in qs:
        a=acs.get(q) or []; b,ads=cps.get(q,(None,None))
        rows.append((len(b) if b is not None else 99, q, a, ads, b))
    rows.sort()
    for n,q,a,ads,b in rows:
        mark='★' if (b is not None and len(b)<=12) else ' '
        print('%s %-26s 제안 %-2d 광고 %-3s 블로그 %2s개' % (mark,q,len(a),
              ads if ads is not None else '-', len(b) if b is not None else '?'))
        if a: print('%30s%s' % ('', ' / '.join(a[:4])))
show('지역 + 공정', Q1)
show('단지명 + 인테리어', Q2)
