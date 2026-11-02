import json,math,statistics as st,pandas as pd
g=json.load(open('geo2.json'))
t=pd.read_pickle('seoul8.pkl'); t=t[t['동']!='-']
t['d']=pd.to_numeric(t['동'].str.extract(r'^(\d{3,4})$')[0],errors='coerce')
gaps={'래미안힐스테이트고덕':[105,109],'마포프레스티지자이':[103],'태릉해링턴플레이스':[113],'DMC롯데캐슬더퍼스트':[106,107],'마포그랑자이':[103],'북한산푸르지오':[306,309,319],'강동리버스트4단지':[405]}
kw={'래미안힐스테이트고덕':'힐스테이트','마포프레스티지자이':'프레스티지','태릉해링턴플레이스':'해링턴','DMC롯데캐슬더퍼스트':'롯데캐슬','마포그랑자이':'그랑자이','북한산푸르지오':'북한산','강동리버스트4단지':'리버스트'}
def dist(a,b): return math.hypot((a[0]-b[0])*111000,(a[1]-b[1])*88000)
R={}
for n,v in g.items():
    real=set(t[t.단지명==n].d.dropna().astype(int))|set(gaps[n])
    cand={int(k):c for k,c in v['cand'].items() if int(k) in real and c}
    ctr=tuple(v['center']); pick={}
    for it in range(3):
        for d,cs in cand.items():
            named=[c for c in cs if kw[n] in c[2]]
            pool=named if named else cs
            pick[d]=min(pool,key=lambda c:dist(c[:2],ctr))
        ctr=(st.median(p[0] for p in pick.values()),st.median(p[1] for p in pick.values()))
    dd={d:round(dist(p[:2],ctr)) for d,p in pick.items()}
    R[n]={d:(p[0],p[1]) for d,p in pick.items()}
    print(n,'real',len(real),'picked',len(pick),'missing',sorted(real-set(pick)),'maxdist',max(dd.values()), 'named',sum(kw[n] in p[2] for p in pick.values()))
json.dump({n:{str(k):v for k,v in r.items()} for n,r in R.items()},open('picked.json','w'))
