import pandas as pd,sys
r=pd.read_pickle('/home/claude/rtn/R2026.pkl')
r=r[r['시군구'].str.contains(sys.argv[1])].copy()
r['dep']=r['보증금(만원)'].astype(str).str.replace(',','').astype(int); r['mo']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['a']=r['전용면적(㎡)'].astype(float)
j=r[(r.mo==0)&r.a.between(float(sys.argv[2]),float(sys.argv[3]))]
pd.set_option('display.width',250)
print(j.groupby(['단지명','계약구분']).dep.agg(['median','size']).unstack('계약구분').to_string())
print(j.groupby('계약구분').dep.agg(['median','size']))
print(j['계약구분'].value_counts(dropna=False))
