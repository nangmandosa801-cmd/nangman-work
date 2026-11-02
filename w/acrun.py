import pickle, re, json, urllib.parse, urllib.request, os, sys
from concurrent.futures import ThreadPoolExecutor
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
CACHE='accache.pkl'
cache = pickle.load(open(CACHE,'rb')) if os.path.exists(CACHE) else {}
def _ac(w):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(w)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0'
       '&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=8) as r:
            j=json.loads(r.read().decode('utf-8'))
        return [i[0] for i in j.get('items',[[]])[0]]
    except Exception: return None

d=pickle.load(open('pubac.pkl','rb'))
pub,heads,res=d['pub'],d['heads'],d['res']
dead=[(i,pub[i],heads[i]) for i in range(len(pub)) if res[i]==[]]

TAIL={'낭만':['시세','아파트 시세','땅값','호재','재건축','기출','전세'],
      '지산':['시세','아파트 시세','땅값','호재','매매','임대','분양가','오피스텔'],
      '도사':['사주','뜻','보는 법']}
cands={}
for i,r,h in dead:
    toks=h.split(); c=set()
    for n in range(1,min(len(toks),4)+1):
        pre=' '.join(toks[:n])
        if len(pre)<2: continue
        c.add(pre)
        for t in TAIL.get(r['블로그'],[]):
            if t not in pre: c.add(pre+' '+t)
    cands[i]=sorted(c)

allw=[w for v in cands.values() for w in v]
todo=[w for w in dict.fromkeys(allw) if w not in cache]
print('후보',len(set(allw)),'| 조회할 것',len(todo),flush=True)
with ThreadPoolExecutor(32) as ex:
    for k,(w,r) in enumerate(zip(todo, ex.map(_ac,todo))):
        if r is not None: cache[w]=r
        if k%300==0: print(k,flush=True); pickle.dump(cache,open(CACHE,'wb'))
pickle.dump(cache,open(CACHE,'wb'))
pickle.dump(cands,open('cands.pkl','wb'))
print('끝, 캐시',len(cache),flush=True)
