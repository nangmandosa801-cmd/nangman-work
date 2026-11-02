import sys; sys.path.insert(0,'/home/claude/watch')
import rt_fetch, pandas as pd, numpy as np, json
a=pd.read_pickle('/home/claude/w/apt_all.pkl'); a=a[a['시군구'].astype(str).str.contains('마포구')].copy()
a['ym']=a['계약년월'].astype(int); a['층']=np.nan
r=rt_fetch.load(); r=r[r['시군구'].str.contains('마포구')].copy(); r['ym']=r['ym'].astype(int)
r['p']=r['거래금액(만원)'].astype(str).str.replace(',','').astype(float)/1e4; r['a']=r['전용면적(㎡)'].astype(float)
r['읍면동']=r['시군구'].str.split().str[-1]; r['층']=pd.to_numeric(r['층'],errors='coerce')
keep=['단지명','a','p','ym','건축년도','읍면동','층','해제사유발생일']
a=a[keep] if '층' in a else a.assign(층=np.nan)[keep]
A=a[(a.ym>=202504)&(a.ym<=202509)]
B=pd.concat([a[(a.ym>=202604)&(a.ym<=202606)], r[(r.ym>=202607)&(r.ym<=202609)][keep]])
for X in (A,B): X.drop(X[X['해제사유발생일'].astype(str).str.strip().ne('-')].index,inplace=True)
for X in (A,B): X['ar']=X['a'].round(); X['k']=X['단지명']+'|'+X['ar'].astype(int).astype(str)
print('건수 A',len(A),'B',len(B), 'B월',B.ym.value_counts().sort_index().to_dict())
ga=A.groupby('k').agg(pa=('p','median'),na=('p','size'),y=('건축년도','first'),dong=('읍면동','first'))
gb=B.groupby('k').agg(pb=('p','median'),nb=('p','size'))
g=ga.join(gb,how='inner'); g['ch']=g.pb/g.pa-1
print('비교 곳',len(g),'변화 중앙',round(g.ch.median()*100,1),'내린 곳',(g.ch<0).sum())
g2=g[(g.na>=2)&(g.nb>=2)]; print('2건씩 곳',len(g2),'중앙',round(g2.ch.median()*100,1))
bins=[0,8,12,16,999]; lab=['8억 이하','8~12억','12~16억','16억 넘음']
g['b']=pd.cut(g.pa,bins,labels=lab)
for l,x in g.groupby('b',observed=True): print(l,len(x),'변화중앙',round(x.ch.median()*100,1),'지은해중앙',int(x.y.astype(int).median()),'지금15억넘',(x.pb>15).sum(),'작년15억이하→넘',((x.pa<=15)&(x.pb>15)).sum())
x=g[g.pa>20]; print('20억 넘던',len(x),round(x.ch.median()*100,1))
# 84 complexes
A84=A[(A.ar>=84)&(A.ar<=85)]; B84=B[(B.ar>=84)&(B.ar<=85)]
c=A84.groupby('단지명').agg(pa=('p','median'),na=('p','size'),y=('건축년도','first'),dong=('읍면동','first')).join(B84.groupby('단지명').agg(pb=('p','median'),nb=('p','size'),fl=('층',lambda s: f"{int(s.min())}~{int(s.max())}" if s.notna().any() else '')),how='inner')
c=c[(c.na>=3)&(c.nb>=3)]; c['ch']=c.pb/c.pa-1
print(c.sort_values('pb',ascending=False).round(3).to_string())
print('84 B건수',len(B84),'중앙',B84.p.median(),'최고',B84.sort_values('p').tail(1)[['단지명','p','ym','층']].values)
g.to_pickle('/home/claude/w/mapo2/g.pkl')
