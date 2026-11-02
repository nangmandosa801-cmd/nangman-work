import pandas as pd, numpy as np, re
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
w=pd.read_pickle('w.pkl')
print(w['시군구'].head(3).tolist())
def um(s):
    p=s.split()
    for x in p[2:]:
        if re.search('[읍면]$',x): return x
    return p[2] if len(p)>2 else ''
w['um']=w['시군구'].map(um)
print(w['um'].value_counts().head(30))
u=w[(w.amt<=10000)&(w.py>=100)]
print(u.groupby('um').agg(n=('pp','size'),pp=('pp','median'),py=('py','median')).sort_values('n',ascending=False).round(1))
f=w[w['지목'].isin(['전','답'])&(w.py>=100)&(w.py<1000)&(w['용도지역']=='개발제한구역')]
print('GB 밭논 100~1천',len(f)); print(f.groupby('um').agg(n=('pp','size'),pp=('pp','median')).sort_values('pp',ascending=False).round(0))
f2=w[w['지목'].isin(['전','답'])&(w.py>=100)&(w.py<1000)&(w['용도지역']=='계획관리지역')]
print('계획관리 밭논',len(f2)); print(f2.groupby('um').agg(n=('pp','size'),pp=('pp','median')).sort_values('pp',ascending=False).round(0))
m=w[(w['지목']=='임야')&(w.py>=100)]
print('임야 100평↑',len(m)); print(m.groupby('um').agg(n=('pp','size'),pp=('pp','median'),py=('py','median')).sort_values('n',ascending=False).round(1))
print('1~3억 지목별'); x=w[(w.amt>10000)&(w.amt<=30000)]; print(len(x)); print(x.groupby('지목').agg(n=('pp','size'),py=('py','median'),amt=('amt','median'),pp=('pp','median')).sort_values('n',ascending=False).head(6).round(1))
# 가평
g=pd.read_parquet('/mnt/user-data/outputs/부동산DB.parquet',filters=[('자료','==','토지'),('시군','==','가평군')])
g=g[(g['계약년월']>='202501')&(g['계약년월']<='202608')&(g['해제사유발생일'].isin(['-']))&(g['지분구분']!='지분')].copy()
g['amt']=pd.to_numeric(g['거래금액(만원)'],errors='coerce'); g['py']=pd.to_numeric(g['계약면적'],errors='coerce')/3.3058; g['pp']=g.amt/g.py
print('가평 통째',len(g))
for lo,hi,nm in [(0,10000,'1억 이하'),(10000,30000,'1~3억')]:
    for jm in ['임야','전']:
        for dd,name in [(w,'남양주'),(g,'가평')]:
            z=dd[(dd.amt>lo)&(dd.amt<=hi)&(dd['지목']==jm)&(dd.py>=100)]
            print(nm,jm,name,len(z),'평',round(z.py.median(),0),'금액',z.amt.median(),'평당',round(z.pp.median(),1))
print('---- 큰 임야')
for dd,name in [(w,'남양주'),(g,'가평')]:
    for lo,hi in [(1000,3000),(3000,10000),(10000,1e9),(3000,1e9)]:
        z=dd[(dd['지목']=='임야')&(dd.py>=lo)&(dd.py<hi)]
        print(name,lo,hi,len(z),'평당',round(z.pp.median(),1),'금액',z.amt.median(), dict(z['용도지역'].value_counts().head(4)))
z=w[(w['지목']=='임야')&(w.py>=3000)]; print(z.groupby('용도지역').agg(n=('pp','size'),pp=('pp','median'),amt=('amt','median')).round(1))
z=g[(g['지목']=='임야')&(g.py>=3000)]; print(z.groupby('용도지역').agg(n=('pp','size'),pp=('pp','median'),amt=('amt','median')).round(1))
print('남양주 통째 지목별 전체'); print(w.groupby('지목').agg(n=('pp','size')).sort_values('n',ascending=False).head(8).T)
print('GB 비중 통째',(w['용도지역']=='개발제한구역').mean().round(3), (w[w.py>=100]['용도지역']=='개발제한구역').mean().round(3), len(w[w.py>=100]))
print(w[w.py>=100]['용도지역'].value_counts().head(8))
