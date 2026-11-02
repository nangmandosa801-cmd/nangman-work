import sys; sys.path.insert(0,'/home/claude/watch')
import rt_fetch, pandas as pd, numpy as np
a=pd.read_pickle('/home/claude/w/apt_all.pkl'); a=a[a['시군구'].astype(str).str.contains('남양주시')].copy(); a['ym']=a['계약년월'].astype(int); a['읍면동']=a['시군구'].astype(str).str.split().str[2]
r=rt_fetch.load(); r=r[r['시군구'].str.contains('남양주시')].copy(); r['ym']=r['ym'].astype(int)
r['p']=r['거래금액(만원)'].astype(str).str.replace(',','').astype(float)/1e4; r['a']=r['전용면적(㎡)'].astype(float); r['읍면동']=r['시군구'].str.split().str[2]
k=['단지명','a','p','ym','건축년도','읍면동','해제사유발생일']
A=a[(a.ym>=202504)&(a.ym<=202509)][k]; B=pd.concat([a[(a.ym>=202604)&(a.ym<=202606)][k],r[(r.ym>=202607)&(r.ym<=202609)][k]])
for X in (A,B): X.drop(X[X['해제사유발생일'].astype(str).str.strip().ne('-')].index,inplace=True); X['ar']=X.a.round()
for dong in ['진접읍','별내동','다산동','진건읍','퇴계원읍','오남읍']:
    a8=A[(A.읍면동==dong)&(A.ar.between(84,85))]; b8=B[(B.읍면동==dong)&(B.ar.between(84,85))]
    g=a8.groupby('단지명').agg(pa=('p','median'),na=('p','size'),y=('건축년도','first')).join(b8.groupby('단지명').agg(pb=('p','median'),nb=('p','size')),how='inner')
    g=g[(g.na>=3)&(g.nb>=3)]; g['ch']=g.pb/g.pa-1
    print('==',dong,'84건 A',len(a8),'B',len(b8),'단지',len(g),'변화중앙',round(g.ch.median()*100,1) if len(g) else None)
    if dong in('진접읍','진건읍'): print(g.sort_values('pb',ascending=False).round(3).head(12).to_string())
