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
    blogs=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
        if m.group(1) not in blogs: blogs.append(m.group(1))
    ads=len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
    return blogs, ads
REG=['구리','남양주','별내','다산','갈매','토평','인창','수택','퇴계원','와부','진접','호평','평내','덕소']
Q=[r+' 인테리어' for r in REG]
with ThreadPoolExecutor(16) as ex: acs=dict(zip(Q, ex.map(ac,Q)))
with ThreadPoolExecutor(6) as ex: cps=dict(zip(Q, ex.map(comp,Q)))
pickle.dump((acs,cps),open('gnh.pkl','wb'))
print('%-16s %-4s %-4s %s' % ('검색어','제안','광고','블로그 수 / 상위'))
rows=[]
for q in Q:
    a=acs.get(q) or []; b,ads=cps.get(q,(None,None))
    rows.append((len(b) if b else 99, q, len(a), ads, b))
rows.sort()
for n,q,na,ads,b in rows:
    print('%-16s %-4d %-4s %2s개  %s' % (q, na, ads if ads is not None else '-',
          len(b) if b else '?', ', '.join(b[:5]) if b else '못읽음'))
    if a:=acs.get(q): print('%18s%s' % ('', ' / '.join(a[:5])))
