import pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
def money(s): return s.astype(str).str.replace(',','').str.strip().replace('-','0').astype(float)
def prep_m(m):
    m=m[m['시군구'].str.startswith('서울')&(m['해제사유발생일']=='-')&(m['거래유형']!='직거래')].copy()
    m['p']=money(m['거래금액(만원)']); m['a']=m['전용면적(㎡)'].astype(float); m['gu']=m['시군구'].str.split().str[1]
    return m[m.a.between(83,86)]
def prep_r(r):
    r=r[r['시군구'].str.startswith('서울')].copy()
    r['dep']=money(r['보증금(만원)']); r['rent']=money(r['월세금(만원)']); r['a']=r['전용면적(㎡)'].astype(float); r['gu']=r['시군구'].str.split().str[1]
    r=r[(r['전월세구분']=='전세')&(r.rent==0)&(r['계약구분']=='신규')&r.a.between(83,86)]
    return r
M26=prep_m(pd.read_pickle('/home/claude/rtn/M2026.pkl')); M25=prep_m(pd.read_pickle('/home/claude/rtn/M2025.pkl'))
MS=pd.read_pickle('/home/claude/rtn/M2021_2024_seoul.pkl'); MS['계약년월']=MS['계약년월'].astype(int); M24=prep_m(MS[MS['계약년월']//100==2024])
R26=prep_r(pd.read_pickle('/home/claude/rtn/R2026.pkl'))
RK=pd.read_pickle('/home/claude/rtn/RK_2024_2026.pkl'); RK['계약년월']=RK['계약년월'].astype(int); RK=prep_r(RK)
print('M26',len(M26),'M25',len(M25),'M24',len(M24),'R26',len(R26),'RK',len(RK), RK.gu.unique())
g=pd.DataFrame({'m26':M26.groupby('gu').p.median(),'m26n':M26.groupby('gu').size(),'m25':M25.groupby('gu').p.median(),'m25n':M25.groupby('gu').size(),
                'm24':M24.groupby('gu').p.median(),'m24n':M24.groupby('gu').size(),
                'r26':R26.groupby('gu').dep.median(),'r26n':R26.groupby('gu').size()})
g['ratio']=g.r26/g.m26*100; g['gap']=g.m26-g.r26
g['m_rank']=g.m26.rank(ascending=False).astype(int); g['ratio_rank']=g.ratio.rank(ascending=False).astype(int)
g['m25_26']=(g.m26/g.m25-1)*100; g['m24_26']=(g.m26/g.m24-1)*100
g=g.sort_values('m26',ascending=False)
print(g.round(1).to_string())
# 단지 짝 맞춤 검증: 같은 단지 매매 · 전세 둘 다 있는 단지의 전세가율 중앙값
mm=M26.groupby(['gu','단지명']).p.agg(['median','size']).rename(columns={'median':'mp','size':'mn'})
rr=R26.groupby(['gu','단지명']).dep.agg(['median','size']).rename(columns={'median':'rp','size':'rn'})
j=mm.join(rr,how='inner'); j=j[(j.mn>=2)&(j.rn>=2)]; j['ratio']=j.rp/j.mp*100
g2=j.groupby('gu').agg(pair_ratio=('ratio','median'),pairs=('ratio','size'))
g=g.join(g2); print(g[['m26','ratio','pair_ratio','pairs']].round(1).to_string())
from scipy.stats import spearmanr
print('spearman m26 vs ratio', spearmanr(g.m26,g.ratio)); print('spearman m26 vs pair_ratio', spearmanr(g.m26,g.pair_ratio))
# 5개씩 묶음
g['grp']=pd.cut(g.m_rank,[0,5,10,15,20,25],labels=['1~5','6~10','11~15','16~20','21~25'])
print(g.groupby('grp').agg(m=('m26','median'),r=('r26','median'),ratio=('ratio','median'),rmin=('ratio','min'),rmax=('ratio','max')).round(1))
# 4개 구 2024 → 2026
RKg=RK.copy(); RKg['y']=RKg['계약년월']//100
k=RKg.groupby(['gu','y']).dep.agg(['median','size']).unstack('y'); print(k)
for gu in ['강남구','서초구','양천구','노원구']:
    print(gu,'매매 24/25/26',g.loc[gu,['m24','m25','m26']].tolist(),'전세 24/25/26',[k.loc[gu,('median',y)] for y in (2024,2025,2026)],[k.loc[gu,('size',y)] for y in (2024,2025,2026)])
g.to_pickle('g.pkl'); k.to_pickle('k.pkl')
print('월:',M26['계약년월'].max(),R26['계약년월'].max())
