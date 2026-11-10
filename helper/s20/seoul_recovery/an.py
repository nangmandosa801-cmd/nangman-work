import pandas as pd
D=[]
m=pd.read_pickle('/home/claude/rtn/M2021_2024_seoul.pkl'); D.append(m)
for y in (2025,2026):
    m=pd.read_pickle(f'/home/claude/rtn/M{y}.pkl'); D.append(m[m['시군구'].str.startswith('서울특별시')])
m=pd.concat(D)
m=m[(m['해제사유발생일']=='-')&(m['거래유형']!='직거래')].copy()
m['p']=m['거래금액(만원)'].str.replace(',','').astype(int); m['a']=m['전용면적(㎡)'].astype(float)
m['y']=m['계약년월'].str[:4].astype(int)
m['gu']=m['시군구'].str.split().str[1]
print(m.groupby('y')['거래유형'].value_counts())
x=m[m.a.between(83,86)].copy()
x.to_pickle('x.pkl')
t=x.groupby(['gu','y']).p.agg(['median','size']).unstack('y')
pd.set_option('display.width',250); pd.set_option('display.max_rows',100)
print(t.to_string())
# recovery
r=pd.DataFrame({'m21':t[('median',2021)],'n21':t[('size',2021)],'m23':t[('median',2023)],'n23':t[('size',2023)],'m26':t[('median',2026)],'n26':t[('size',2026)],'m25':t[('median',2025)],'n25':t[('size',2025)]})
r['rec']=(r.m26/r.m21*100).round(1); r['up23']=((r.m26/r.m23-1)*100).round(1)
r['rank_price']=r.m26.rank(ascending=False).astype(int); r['rank_rec']=r.rec.rank(ascending=False).astype(int)
r=r.sort_values('rec',ascending=False)
print(r.to_string())
r.to_pickle('r.pkl')
# seoul total
for y in range(2021,2027):
    d=x[x.y==y]; print(y, d.p.median(), len(d))
