import pandas as pd
D=[]
for y in (2025,2026):
    m=pd.read_pickle(f'/home/claude/rtn/M{y}.pkl')
    m=m[m['시군구'].str.contains('수정구 창곡동|송파구 장지동|하남시 학암동|송파구 거여동')&(m['해제사유발생일']=='-')].copy(); m['y']=y; D.append(m)
m=pd.concat(D); m['p']=m['거래금액(만원)'].str.replace(',','').astype(int); m['a']=m['전용면적(㎡)'].astype(float); m['by']=pd.to_numeric(m['건축년도'])
m=m[m.by>=2013]
m['시']=m['시군구'].str.split().str[1]
print(m['계약년월'].max())
x=m[m.a.between(83,86)]
t=x.groupby(['시군구','단지명','by','y']).p.agg(['median','size']).unstack('y')
pd.set_option('display.width',250); print(t.to_string())
x.to_pickle('x.pkl'); m.to_pickle('m.pkl')
for s,d in x.groupby('시군구'):
    print(s, d[d.y==2026].p.median(), len(d[d.y==2026]), d[d.y==2025].p.median(), len(d[d.y==2025]))
