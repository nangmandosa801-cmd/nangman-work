import pandas as pd, numpy as np, math
p=pd.read_pickle('paju.pkl'); geo=pd.read_pickle('unjeong_geo2.pkl')
p=p[p['해제사유발생일'].isna()|(p['해제사유발생일']=='-')].copy()
p=p[p['단지명'].isin([k for k,v in geo.items() if v])]
S=(37.71615,126.72829)
def dist(n):
    la,lo,_=geo[n]; return math.hypot((la-S[0])*111.0,(lo-S[1])*88.2)
p['d']=p['단지명'].map(dist); p['ym']=p['계약년월'].astype(int); p['y']=p['건축년도'].astype(int)
p['a']=p['전용면적(㎡)'].astype(float).round(0); p['p']=p['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
p['bk']=pd.cut(p.d,[0,1,2,10],labels=['1km 안','1~2km','2km 밖'])
def per(lo,hi): return p[(p.ym>=lo)&(p.ym<=hi)].groupby(['bk','단지명','a'],observed=True)['p'].agg(['mean','size'])
def cmp(A,B,name):
    m=A.join(B,lsuffix='A',rsuffix='B',how='inner'); m['c']=m.meanB/m.meanA-1
    print(name, m.groupby('bk',observed=True)['c'].agg(['mean','size']).round(3).to_dict()); return m
pk=per(202107,202112); pre=per(202401,202411)
for nm,lo,hi in [('개통~2025.3',202412,202503),('2025.4~9',202504,202509),('2025.10~2026.2',202510,202602),('2026.3~8',202603,202608)]:
    cmp(pre,per(lo,hi),'vs개통전 '+nm)
m=cmp(pk,per(202603,202608),'vs2021하반기 고점')
m2=cmp(pk,pre,'2021고점→개통전')
print(p.groupby('bk',observed=True)['단지명'].nunique())
cx=p.groupby('단지명').agg(d=('d','first'),y=('y','first'),n=('p','size'))
cx.to_pickle('uj_cx.pkl')
m.to_pickle('uj_peak.pkl'); cmp(pre,per(202603,202608),'x').to_pickle('uj_pre.pkl')
