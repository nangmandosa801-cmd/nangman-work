import json,math,pandas as pd,numpy as np
exec(open('dong_scan.py').read().split('res=[]')[0])
P=json.load(open('picked.json')); P.pop('마포그랑자이'); P.pop('래미안힐스테이트고덕')
gaps={'래미안힐스테이트고덕':[105,109],'마포프레스티지자이':[103],'태릉해링턴플레이스':[113],'DMC롯데캐슬더퍼스트':[106,107],'북한산푸르지오':[309,319],'강동리버스트4단지':[405]}
gu={'래미안힐스테이트고덕':'강동구','마포프레스티지자이':'마포구','태릉해링턴플레이스':'노원구','DMC롯데캐슬더퍼스트':'은평구','북한산푸르지오':'은평구','강동리버스트4단지':'강동구'}
def dist(x,y): return math.hypot((x[0]-y[0])*111000,(x[1]-y[1])*88000)
rows=[];allb=[]
for n,pk in P.items():
    pk={int(k):v for k,v in pk.items()}
    g=t[(t.시군==gu[n])&(t.단지명==n)].copy()
    g['lp']=np.log(g.p); g['k']=g.a.astype(str)+'_'+g.h.astype(str)
    g['r']=g.lp-g.groupby('k').lp.transform('mean'); g=g[g.groupby('k').lp.transform('size')>=2]
    b=np.polyfit(g.f,g.r,1)[0]; g['r2']=g.r-b*(g.f-g.f.mean())
    nd={d:min(dist(pk[d],pk[x]) for x in gaps[n] if x in pk) for d in pk if d not in gaps[n]}
    g['nd']=g.d.map(nd); g=g.dropna(subset=['nd'])
    near=sorted(nd,key=nd.get)[:2*len(gaps[n])]
    numadj=[d for d in nd if any(abs(d-x)==1 for x in gaps[n])]
    ni=g[g.d.isin(near)]; ot=g[~g.d.isin(near)]
    na=g[g.d.isin(numadj)]; oa=g[~g.d.isin(numadj)]
    rows.append((n,gaps[n],[(d,round(nd[d])) for d in near],len(ni),round((ni.r2.mean()-ot.r2.mean())*100,2),numadj,round((na.r2.mean()-oa.r2.mean())*100,2),round(b*100,2)))
    g['n']=n; allb.append(g[['n','d','nd','r2']])
for r in rows: print(r)
d=np.array([r[4] for r in rows]); print('spatial mean',d.mean().round(2),'neg',(d<0).sum())
A=pd.concat(allb)
A['band']=pd.cut(A.nd,[0,80,160,260,2000],labels=['~80m','80~160m','160~260m','260m~'])
A['r3']=A.r2-A.groupby('n').r2.transform('mean')
print(A.groupby('band',observed=True).r3.agg(['mean','size']).assign(mean=lambda x:(x['mean']*100).round(2)))
print(A.groupby(['n','band'],observed=True).r3.agg(['mean','size']).assign(mean=lambda x:(x['mean']*100).round(2)))
