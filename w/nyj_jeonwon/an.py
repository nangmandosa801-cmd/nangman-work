import pandas as pd, numpy as np
d=pd.read_parquet('/mnt/user-data/outputs/부동산DB.parquet')
t=d[(d['자료']=='토지')&(d['시군']=='남양주시')].copy()
t['ym']=t['계약년월'].astype(int)
t=t[(t.ym>=202501)&(t.ym<=202608)]
t=t[t['해제사유발생일'].isna()|(t['해제사유발생일'].astype(str).str.strip().isin(['','-','nan']))]
print('지분',t['지분구분'].value_counts(dropna=False).to_dict())
t=t[t['지분구분'].astype(str).str.contains('지분')==False]
t['a']=pd.to_numeric(t['계약면적'],errors='coerce'); t['p']=pd.to_numeric(t['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
t['py']=t.a/3.3058; t['pp']=t.p/t.py
print(t['지목'].value_counts().head(10).to_dict())
u=t[t['지목']=='대']
print('대',len(u)); print(u['용도지역'].value_counts().to_dict())
u['읍면']=u['읍면동']
print(u['읍면'].value_counts().to_dict())
v=u[(u.a>=330)&(u.a<=1000)]
print('100~300평 대지',len(v))
g=v.groupby(['읍면']).agg(n=('pp','size'),med_pp=('pp','median'),med_p=('p','median'),med_py=('py','median'))
print(g.sort_values('n',ascending=False).round(0))
g2=v.groupby(['용도지역']).agg(n=('pp','size'),med_pp=('pp','median'),med_p=('p','median'))
print(g2.sort_values('n',ascending=False).round(0))
print(v['도로조건'].value_counts().to_dict())
g3=v.groupby(['도로조건']).agg(n=('pp','size'),med_pp=('pp','median'))
print(g3.round(0))
v.to_pickle('v.pkl'); u.to_pickle('u.pkl')
