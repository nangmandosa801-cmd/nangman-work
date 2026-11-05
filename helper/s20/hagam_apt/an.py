import pandas as pd
D=[]
for y in (2025,2026):
    m=pd.read_pickle(f'/home/claude/rtn/M{y}.pkl'); m=m[m['시군구'].str.contains('하남시 학암동')&(m['해제사유발생일']=='-')].copy(); D.append(m)
m=pd.concat(D); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int); m['a']=m['전용면적(㎡)'].astype(float)
m['ym']=m['계약년월'].astype(int); m['y']=m.ym//100
print(m['거래유형'].value_counts()); m=m[m['거래유형']!='직거래']
m['pp']=m.p/(m.a/3.3058)
pd.set_option('display.width',250)
print(m.groupby(['단지명','건축년도','도로명']).size())
t=m.groupby(['단지명','건축년도','y']).agg(n=('p','size'),pp=('pp','median')).unstack('y'); print(t.round(0).to_string())
m['g']=m['건축년도'].astype(int).map(lambda b:'2015-17' if b<=2017 else '2021-22')
big=m[m.a.between(95,105)]
print(big.groupby(['g','y']).agg(n=('p','size'),p=('p','median'),pp=('pp','median')).round(0))
print(m.groupby(['g','y']).agg(n=('p','size'),pp=('pp','median')).round(0))
print(m[m.y==2026].groupby('ym').size())
print('all 2026',m[m.y==2026].p.median(),len(m[m.y==2026]),'2025',m[m.y==2025].p.median(),len(m[m.y==2025]))
print(m[(m.y==2026)&(m.ym>=202610)][['단지명','a','ym','계약일','p']])
print(big.groupby(['단지명','y']).p.agg(['median','size']).unstack('y'))
print('2025 1-10 n', len(m[(m.y==2025)&(m.ym%100<=10)]))
l=m[(m['단지명']=='위례롯데캐슬')&m.a.between(83,86)]
print(l.groupby('y').p.agg(['median','size','max'])); print(l[l.y==2026].groupby('ym').p.agg(['median','size']).to_string())
print(l[(l.y==2025)&(l.ym%100<=10)].p.agg(['median','size']))
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); r=r[r['시군구'].str.contains('하남시 학암동')].copy()
r['dep']=r['보증금(만원)'].astype(str).str.replace(',','').astype(int); r['mo']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int); r['a']=r['전용면적(㎡)'].astype(float)
r['g']=r['건축년도'].astype(int).map(lambda b:'2015-17' if b<=2017 else '2021-22')
j=r[(r.mo==0)]
print(j[j.a.between(95,105)].groupby(['g','계약구분']).dep.agg(['median','size']))
print(j[j.a.between(95,105)].groupby(['단지명','계약구분']).dep.agg(['median','size']).unstack())
print(j[(r['단지명']=='위례롯데캐슬')&j.a.between(83,86)].groupby('계약구분').dep.agg(['median','size']))
