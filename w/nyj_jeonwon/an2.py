import pandas as pd, numpy as np
d=pd.read_parquet('/mnt/user-data/outputs/부동산DB.parquet')
def prep(city):
    t=d[(d['자료']=='토지')&(d['시군']==city)].copy()
    t['ym']=t['계약년월'].astype(int); t=t[(t.ym>=202501)&(t.ym<=202608)]
    t=t[t['해제사유발생일'].isna()|(t['해제사유발생일'].astype(str).str.strip().isin(['','-','nan']))]
    t=t[t['지분구분'].astype(str).str.contains('지분')==False]
    t['a']=pd.to_numeric(t['계약면적'],errors='coerce'); t['p']=pd.to_numeric(t['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
    t['py']=t.a/3.3058; t['pp']=t.p/t.py
    t['읍면']=t['시군구'].str.split().str[2]
    return t
n=prep('남양주시'); g=prep('가평군')
for name,t in [('남양주',n),('가평',g)]:
    v=t[(t['지목']=='대')&(t.a>=330)&(t.a<=1000)]
    print('==',name,'대 100~300평',len(v), 'pp med',round(v.pp.median()),'p med',round(v.p.median()))
    print(v.groupby('읍면').agg(n=('pp','size'),pp=('pp','median'),p=('p','median'),py=('py','median')).sort_values('n',ascending=False).round(0))
    print(v.groupby('용도지역').agg(n=('pp','size'),pp=('pp','median'),p=('p','median')).sort_values('n',ascending=False).round(0))
    print('도로',v.groupby('도로조건').agg(n=('pp','size'),pp=('pp','median')).round(0).to_dict())
    w=t[(t['지목'].isin(['전','답']))&(t.a>=330)&(t.a<=1000)&(t['용도지역']=='계획관리지역')]
    print('계획관리 전답 100~300평',len(w),round(w.pp.median()) if len(w) else '')
print(n[(n['지목']=='대')&(n.a>=330)&(n.a<=1000)]['ym'].agg(['min','max']))
