import pandas as pd
pd.set_option('display.width',250)
m=pd.read_pickle('/home/claude/rtn/M_hanam_2014_2026.pkl'); m=m[m.ym<=202610]
x=m[m.dong.isin(['망월동','풍산동','선동'])&m.a.between(83,86)&(pd.to_numeric(m['건축년도'])>=2014)]
t=x.groupby('y').p.agg(['median','size','min','max']); print(t.to_string())
# 월별 고점 · 바닥 (3건 이상 달)
mm=x.groupby('ym').p.agg(['median','size']); mm=mm[mm['size']>=5]
print('2021 max month', mm.loc[202101:202112].sort_values('median').tail(3).to_string())
print('2023 min month', mm.loc[202201:202312].sort_values('median').head(3).to_string())
print('2026 months', mm.loc[202601:202610].to_string())
# 푸르지오
pj=x[x['단지명']=='미사강변푸르지오']; print(pj.groupby('y').p.agg(['median','size']).to_string())
# 2015 12건 단지
print(x[x.y==2015].groupby('단지명').p.agg(['median','size']))
print(x[x.y==2016].groupby('단지명').p.agg(['median','size']))
# 입주 연도별 단지 수
print(x.groupby('건축년도').단지명.nunique())
# 하남 전체 84 for context
h=m[m.a.between(83,86)]; print(h.groupby('y').p.median().to_string())
