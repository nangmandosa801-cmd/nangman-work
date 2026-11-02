import pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
s=pd.read_pickle('/home/claude/w/suwon.pkl')
s=s[s['해제사유발생일'].isin(['-','',None])|s['해제사유발생일'].isna()].copy()
s['ym']=s['계약년월'].astype(str)
def per(a,b): return s[(s.ym>=a)&(s.ym<=b)]
A=per('202501','202508'); B=per('202601','202608'); P21=per('202101','202112')
print('전체 건수 2025',len(A),'2026',len(B),'2021',len(P21))
print(pd.concat([A.groupby('구').size().rename('25'),B.groupby('구').size().rename('26')],axis=1))
def f84(x): return x[(x.a>=84)&(x.a<85.5)]
for nm,x in [('25',A),('26',B),('21',P21)]:
    y=f84(x); print(nm,'84㎡',len(y),'중앙',y.p.median()); print(y.groupby('구').p.agg(['size','median']).T)
key=['구','읍면동','단지명']
def comp(x,n=3):
    g=f84(x).groupby(key).agg(n=('p','size'),med=('p','median'),yr=('건축년도','first')).reset_index(); return g[g.n>=n]
ca,cb,c21=comp(A),comp(B),comp(P21)
m=ca.merge(cb,on=key,suffixes=('_25','_26')); m['chg']=(m.med_26/m.med_25-1)*100
print('두 해 모두 3건↑ 단지',len(m),'변화 중앙값',round(m.chg.median(),1),'오른 곳',(m.chg>0).sum(),'내린 곳',(m.chg<0).sum())
print(m.groupby('구').agg(n=('chg','size'),chg=('chg','median'),m25=('med_25','median'),m26=('med_26','median')).round(2))
m2=c21.merge(cb,on=key,suffixes=('_21','_26')); m2['chg']=(m2.med_26/m2.med_21-1)*100
print('2021 대비',len(m2),round(m2.chg.median(),1),'넘은 곳',(m2.chg>0).sum()); print(m2.groupby('구').agg(n=('chg','size'),chg=('chg','median'),over=('chg',lambda v:(v>0).sum())).round(1))
print('--- 올해 84㎡ 상위 12'); t=cb.sort_values('med',ascending=False).head(12).merge(ca[key+['med']],on=key,how='left',suffixes=('','_25')); t['chg']=((t.med/t.med_25-1)*100).round(1); print(t.to_string())
print('--- 동별 84㎡ 올해 (10건↑)'); d=f84(B).groupby(['구','읍면동']).p.agg(['size','median']); d=d[d['size']>=10].sort_values('median',ascending=False); 
da=f84(A).groupby(['구','읍면동']).p.agg(['size','median']); d=d.join(da,rsuffix='_25'); d['chg']=((d['median']/d['median_25']-1)*100).round(1); print(d.to_string())
print('--- 59㎡'); 
def f59(x): return x[(x.a>=59)&(x.a<60)]
for nm,x in [('25',A),('26',B)]:
    y=f59(x); print(nm,len(y),y.p.median()); print(y.groupby('구').p.agg(['size','median']).T)
print('--- 많이 오른/내린 단지 84'); print(m.sort_values('chg',ascending=False).head(8)[key+['n_25','med_25','n_26','med_26','chg','yr_26']].round(2).to_string()); print(m.sort_values('chg').head(6)[key+['n_25','med_25','n_26','med_26','chg','yr_26']].round(2).to_string())
print('월별 건수 2026'); print(B.groupby('ym').size().to_dict()); print('2025',A.groupby('ym').size().to_dict())
print('=== 동별 같은 단지 변화')
x=m.groupby(['구','읍면동']).agg(n=('chg','size'),chg=('chg','median'),up=('chg',lambda v:(v>0).sum()),m25=('med_25','median'),m26=('med_26','median')).round(2)
print(x[x.n>=3].sort_values('chg',ascending=False).to_string())
gg=m[m['읍면동'].isin(['이의동','원천동','하동'])]; print('광교 3동',len(gg),round(gg.chg.median(),1),(gg.chg>=20).sum(), gg.med_26.median())
print('20% 넘게 오른 곳',(m.chg>=20).sum(), m[m.chg>=20].groupby('구').size().to_dict(), '10% 넘게',(m.chg>=10).sum(),'5% 미만',((m.chg<5)).sum())
print('2021 못 넘은 곳',(m2.chg<=0).sum(),'/',len(m2)); print(m2.groupby('구').agg(n=('chg','size'),under=('chg',lambda v:(v<0).sum())))
top=cb.sort_values('med',ascending=False).head(10).merge(c21[key+['med']],on=key,how='left',suffixes=('','_21')); print(top[key+['med','med_21']].to_string())
print('10억 넘는 84 단지',(cb.med>=10).sum(), cb[cb.med>=10].groupby('구').size().to_dict(),'전체 단지',len(cb),'5억 아래',(cb.med<5).sum())
