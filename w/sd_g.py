import pandas as pd
s=pd.read_pickle('songdo2.pkl'); s['by']=pd.to_numeric(s['건축년도'],errors='coerce')
def grp(n,hd):
    if any(k in n for k in ['레이크송도']): return None
    if n in ['e편한세상송도','더샵송도마리나베이','랜드마크시티센트럴더샵','송도SKVIEW','송도오션파크베르디움']: return '6·8공구'
    if any(k in n for k in ['퍼스트파크','파크애비뉴','마스터뷰','프라임뷰','센터니얼','아트윈']): return '3공구'
    if hd=='송도3동': return '7공구'
    if hd=='송도2동': return '1공구'
    if hd=='송도1동': return '2·4공구'
    return None
s['g']=[grp(n,h) for n,h in zip(s.단지명,s.hd)]
s.to_pickle('songdo3.pkl')
def pairs(d,y0,y1,mn=2):
    q=d[d.y.isin([y0,y1])].groupby(['단지명','a','y']).p.agg(['mean','size']).unstack('y').dropna()
    q=q[(q[('size',y0)]>=mn)&(q[('size',y1)]>=mn)]
    w=q[('size',y1)]; rr=q[('mean',y1)]/q[('mean',y0)]-1
    return round((rr*w).sum()/w.sum()*100,1), len(q)
old=s[s.by<=2022]
print('ALL(<=2022)',pairs(old,2025,2026),pairs(old,2021,2026,1))
for g in ['1공구','2·4공구','3공구','7공구','6·8공구']:
    d=old[old.g==g]; dd=s[s.g==g]
    x=dd[(dd.y==2026)&dd.a.between(83,86)]
    print(g,'cplx',dd.단지명.nunique(),'by',int(dd.drop_duplicates('단지명').by.median()),'25-26',pairs(d,2025,2026),'21-26',pairs(d,2021,2026,1),'84avg26',round(x.p.mean()/1e4,2),len(x))
print(s[s.g.isna()].단지명.unique())
