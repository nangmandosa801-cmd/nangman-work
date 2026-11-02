import pandas as pd, numpy as np
g=pd.read_parquet('/mnt/user-data/outputs/부동산DB.parquet',filters=[('자료','==','토지'),('시군','==','가평군')])
for a,b in [('202501','202608'),('202301','202608')]:
    x=g[(g['계약년월']>=a)&(g['계약년월']<=b)&(g['해제사유발생일'].isin(['-']))&(g['지분구분']!='지분')].copy()
    x['amt']=pd.to_numeric(x['거래금액(만원)'],errors='coerce'); x['py']=pd.to_numeric(x['계약면적'],errors='coerce')/3.3058; x['pp']=x.amt/x.py
    x['road']=np.where(x['도로조건']=='-','없음','붙음')
    z=x[(x['지목']=='임야')&(x.py>=1000)]
    print(a,b,len(z)); print(z.groupby(['용도지역','road']).agg(n=('pp','size'),pp=('pp','median')).round(1).unstack())
    z=x[(x['지목']=='임야')&(x.py>=3000)]; print('3천↑',z.groupby('road').agg(n=('pp','size'),pp=('pp','median')).round(1).T)
w=pd.read_pickle('w.pkl'); w['road']=np.where(w['도로조건']=='-','없음','붙음')
z=w[(w['지목']=='임야')&(w.py>=3000)]; print('남양주 3천↑',z.groupby('road').agg(n=('pp','size'),pp=('pp','median')).round(1).T)
print(w[(w.amt<=10000)&(w.py>=100)]['road'].value_counts())
