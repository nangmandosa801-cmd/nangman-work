import pandas as pd
D=[]
for y in (2025,2026):
    m=pd.read_pickle(f'/home/claude/rtn/M{y}.pkl'); m=m[m['시군구'].str.contains('하남시 감이동|하남시 감일동')&(m['해제사유발생일']=='-')].copy(); D.append(m)
m=pd.concat(D); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int); m['a']=m['전용면적(㎡)'].astype(float)
m['ym']=m['계약년월'].astype(int); m['y']=m.ym//100; m['f']=pd.to_numeric(m['층'])
print(m['거래유형'].value_counts())
m=m[m['거래유형']!='직거래']
pd.set_option('display.width',250)
h=m[m['단지명']=='감일한라비발디']
for ar,g in h.groupby(h.a.round()):
    print('AREA',ar); print(g.groupby('y').p.agg(['median','size','min','max']))
    g2=g[g.y==2026]; print(g2.groupby('ym').p.agg(['median','size']).to_string())
h84=h[h.a.between(83,86)]
print('last 84', h84.sort_values(['ym','계약일']).tail(8)[['ym','계약일','층','p']].to_string())
print('h84 2025 by half', h84[h84.y==2025].groupby(h84.ym%100>6).p.median())
# floor
x=h84[h84.y==2026]; print('floor', x.groupby(pd.cut(x.f,[0,5,10,30])).p.agg(['median','size']))
# 1~10 same period 2025
print('2025 1-10', h84[(h84.y==2025)&(h84.ym%100<=10)].p.agg(['median','size']))
x=m[m.a.between(83,86)]
t=x.groupby(['단지명','건축년도','y']).p.agg(['median','size']).unstack('y'); print(t.to_string())
t=x[x.ym%100<=10].groupby(['단지명','y']).p.agg(['median','size']).unstack('y'); print('1-10',t.to_string())
y74=m[m.a.between(74,76)]; print(y74.groupby(['단지명','y']).p.agg(['median','size']).unstack('y'))
