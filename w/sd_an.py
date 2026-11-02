import pandas as pd, json, numpy as np
s=pd.read_pickle('songdo.pkl')
s=s[s['해제사유발생일'].isna()|(s['해제사유발생일'].astype(str).str.strip().isin(['','-','nan']))].copy()
s['a']=pd.to_numeric(s['전용면적(㎡)'],errors='coerce').round(2); s['p']=pd.to_numeric(s['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
g=json.load(open('sdgeo.json')); H={k:v['hd'] for k,v in g.items()}
over={'송도더샵센트럴시티':'송도3동','힐스테이트레이크송도2차':'송도4동','힐스테이트레이크송도3차':'송도4동','더샵송도프라임뷰20BL':'송도4동','더샵송도프라임뷰25BL':'송도4동','더샵송도아크베이':'송도4동','송도자이더스타':'송도5동','송도자이크리스탈오션':'송도5동','인천송도힐스테이트4단지':'송도2동','송도푸르지오월드마크1단지':'송도2동','송도푸르지오월드마크8단지':'송도2동','송도센트럴파크리버리치':'송도2동','송도아리스타프라임아파트':'송도2동'}
H.update(over); s['hd']=s.단지명.map(H)
print('unmapped',s[s.hd.isna()|(s.hd=='')].단지명.unique())
s.to_pickle('songdo2.pkl')
# ranking 2026 84
x=s[(s.y==2026)&s.a.between(83,86)]
r=x.groupby(['단지명','hd','건축년도']).p.agg(['mean','size']).reset_index(); r=r[r['size']>=5].sort_values('mean',ascending=False)
print(r.head(12).to_string()); print(r.tail(5).to_string()); print('n complexes',len(r))
def pairs(d,y0,y1,mn=2):
    q=d[d.y.isin([y0,y1])].groupby(['단지명','a','y']).p.agg(['mean','size']).unstack('y').dropna()
    q=q[(q[('size',y0)]>=mn)&(q[('size',y1)]>=mn)]
    w=q[('size',y1)]; rr=q[('mean',y1)]/q[('mean',y0)]-1
    return round((rr*w).sum()/w.sum()*100,1), len(q)
print('all 25-26',pairs(s,2025,2026),'21-26',pairs(s,2021,2026,1))
for h in ['송도1동','송도2동','송도3동','송도4동','송도5동']:
    d=s[s.hd==h]; print(h, 'n cplx',d.단지명.nunique(),'25->26',pairs(d,2025,2026),'21->26',pairs(d,2021,2026,1), 'by median',int(pd.to_numeric(d.건축년도).median()))
