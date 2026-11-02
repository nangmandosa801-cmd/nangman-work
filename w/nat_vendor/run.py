# 전국 업체 후보 (10/18 17:02 사용자 「업체까지 가고 전국적으로 다 확보」)
import sys,json,re,pickle
sys.path.insert(0,'/home/claude/w/expand')
from scan import get,ranks,rss
from concurrent.futures import ThreadPoolExecutor
REG={'부산':['부산'],'경남':['창원','김해','양산'],'울산':['울산'],'대구':['대구'],'경북':['구미','포항','경산'],'광주':['광주'],'전남':['순천','광양','여수'],'전북':['전주','군산','익산'],'대전':['대전'],'세종':['세종'],'충북':['청주','충주'],'충남':['천안','아산','서산','당진'],'강원':['원주','강릉','춘천'],'제주':['제주']}
CAT={'중문':(['{} 중문 시공','{} 중문'],'중문|도어'),'입주청소':(['{} 입주청소','{} 입주청소 업체'],'청소|클린|크린|홈케어'),'줄눈':(['{} 줄눈 시공','{} 줄눈 탄성코트'],'줄눈|탄성|케어|코트'),'이사':(['{} 포장이사','{} 포장이사 업체'],'이사|익스프레스|통운|물류')}
qs=[(rg,c,q.format(city)) for rg,cs in REG.items() for city in cs for c,(qq,_) in CAT.items() for q in qq]
with ThreadPoolExecutor(8) as ex: res=list(ex.map(lambda t:(t,ranks(t[2])),qs))
hits={}
for (rg,c,q),r in res:
    for b,rk in r.items():
        k=(rg,c,b); hits.setdefault(k,[]).append(rk)
blogs=sorted({b for (_,_,b) in hits})
print(len(qs),'queries',len(blogs),'blogs',flush=True)
with ThreadPoolExecutor(12) as ex: P=dict(zip(blogs,ex.map(rss,blogs)))
pickle.dump((hits,P),open('raw.pkl','wb'))
out=[]
BAD='부동산|공인중개|맛집|여행|육아|리뷰|일상|분양|대출'
for (rg,c,b),rks in hits.items():
    p=P[b]; txt=p['name']+' '+p['desc']+' '+' '.join(p['titles'][:20])
    if not p['ph'] or re.search(BAD,p['name']): continue
    if not re.search(CAT[c][1],txt): continue
    if p['n30']>25: continue
    score=len(rks)*10-min(rks)
    out.append(dict(region=rg,cat=c,blog=b,name=p['name'],ph=p['ph'],n30=p['n30'],hits=len(rks),best=min(rks),score=score,titles=p['titles'][:5]))
out.sort(key=lambda x:(x['region'],x['cat'],-x['score']))
json.dump(out,open('cand.json','w'),ensure_ascii=False,indent=1)
print(len(out),'cand')
