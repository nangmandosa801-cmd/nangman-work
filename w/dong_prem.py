import pandas as pd, numpy as np
exec(open('dong_scan.py').read().split('res=[]')[0])
C={('강동구','래미안힐스테이트고덕'):[105,109],('성동구','센트라스'):[123,124,125,126],('마포구','마포프레스티지자이'):[103],
 ('강남구','래미안블레스티지'):[207,208],('마포구','마포래미안푸르지오4단지'):[405],('노원구','태릉해링턴플레이스'):[113],
 ('은평구','DMC롯데캐슬더퍼스트'):[106,107],('마포구','마포그랑자이'):[103],('송파구','e편한세상송파파크센트럴'):[207,208],
 ('노원구','노원센트럴푸르지오'):[104],('은평구','북한산푸르지오'):[306,309,319],('강남구','디에이치아너힐즈'):[319],
 ('마포구','마포래미안푸르지오3단지'):[306],('강동구','강동리버스트4단지'):[405]}
out=[]
for (gu,n),gap in C.items():
    g=t[(t.시군==gu)&(t.단지명==n)].copy()
    g['lp']=np.log(g.p); g['k']=g.a.astype(str)+'_'+g.h.astype(str)
    # demean by area-halfyear cell, then floor slope
    g['r']=g.lp-g.groupby('k').lp.transform('mean')
    g=g[g.groupby('k').lp.transform('size')>=2]
    b=np.polyfit(g.f,g.r,1)[0]; g['r2']=g.r-b*(g.f-g.f.mean())
    ds=sorted(g.d.unique())
    nb=set()
    for x in gap:
        for dd in (x-1,x+1):
            if dd in ds: nb.add(dd)
    if not nb: continue
    e=g.groupby('d').r2.agg(['mean','size'])
    ni=g[g.d.isin(nb)]; ot=g[~g.d.isin(nb)]
    diff=(ni.r2.mean()-ot.r2.mean())*100
    out.append((gu,n,gap,sorted(nb),len(ni),len(ot),round(diff,2),round(b*100,2)))
for o in out: print(o)
d=np.array([o[6] for o in out]); w=np.array([o[4] for o in out])
print('simple mean',d.mean().round(2),'median',np.median(d).round(2),'neg count',(d<0).sum(),'/',len(d),'weighted',(d*w).sum()/w.sum())
print('---spread')
sp=[]
for (gu,n),gap in C.items():
    g=t[(t.시군==gu)&(t.단지명==n)].copy()
    g['lp']=np.log(g.p); g['k']=g.a.astype(str)+'_'+g.h.astype(str)
    g['r']=g.lp-g.groupby('k').lp.transform('mean'); g=g[g.groupby('k').lp.transform('size')>=2]
    b=np.polyfit(g.f,g.r,1)[0]; g['r2']=g.r-b*(g.f-g.f.mean())
    e=g.groupby('d').r2.agg(['mean','size']); e=e[e['size']>=8]
    sp.append((n,round((e['mean'].max()-e['mean'].min())*100,1),round(e['mean'].std()*100,2),len(e)))
    if n=='센트라스': print((e['mean']*100).round(2).sort_values().to_dict()); print(g[g.a.between(83,86)&(g.y==2025)].groupby('d').p.agg(['mean','size']).round(0).to_dict())
for s in sp: print(s)
