import pandas as pd
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); m=pd.read_pickle('/home/claude/rtn/M2026.pkl')
r=r[r['시군구'].str.contains('연수구 송도동')&(r['주택유형']=='아파트' if '주택유형' in r else True)].copy()
print(r['전월세구분'].value_counts().to_dict(), r['계약구분'].value_counts(dropna=False).to_dict(), r['계약년월'].min(), r['계약년월'].max())
r['a']=r['전용면적(㎡)'].astype(float); r['dep']=r['보증금(만원)'].str.replace(',','').astype(int); r['mw']=pd.to_numeric(r['월세금(만원)'].astype(str).str.replace(',',''),errors='coerce').fillna(0)
j=r[(r['전월세구분']=='전세')&(r.mw==0)&r.a.between(83,86)]
print('84 전세',len(j), j['계약구분'].value_counts(dropna=False).to_dict())
n=j[j['계약구분']=='신규']; g=j[j['계약구분']=='갱신']
print('신규 median',n.dep.median(),len(n),'q',n.dep.quantile([.25,.75]).tolist(),'갱신',g.dep.median(),len(g))
m=m[m['시군구'].str.contains('연수구 송도동')&(m['해제사유발생일']=='-')].copy(); m['a']=m['전용면적(㎡)'].astype(float); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int)
mm=m[m.a.between(83,86)]
print('매매 84 median',mm.p.median(),len(mm), m['계약년월'].max())
a=n.groupby(['단지명']).dep.agg(['median','size']); b=mm.groupby('단지명').p.agg(['median','size'])
by=r.groupby('단지명')['건축년도'].first()
t=a.join(b,lsuffix='_j',rsuffix='_m',how='left').join(by); t['ratio']=(t.median_j/t.median_m*100).round(1)
t=t[t.size_j>=5].sort_values('median_j',ascending=False)
pd.set_option('display.width',200); print(t.to_string())
t.to_pickle('t.pkl'); n.to_pickle('n.pkl'); mm.to_pickle('mm.pkl')
