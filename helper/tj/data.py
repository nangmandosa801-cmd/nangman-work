import pandas as pd
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); m=pd.read_pickle('/home/claude/rtn/M2026.pkl')
num=lambda s: pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
for d in (m,r):
    d['a']=num(d['전용면적(㎡)']); d['y']=num(d['건축년도'])
m['p']=num(m['거래금액(만원)']); r['bo']=num(r['보증금(만원)']); r['wo']=num(r['월세금(만원)'])
m=m[m['해제사유발생일'].astype(str).str.strip().isin(['-','','nan'])]
reg='아산시 (?:탕정|배방)'
mm=m[m['시군구'].str.contains(reg)&(m.y>=2021)]; rr=r[r['시군구'].str.contains(reg)&(r.y>=2021)]
sale=set(mm['단지명']); rr=rr[rr['단지명'].isin(sale)]
print('complexes',sorted(sale))
for lab,lo,hi in [('84',80,86),('70',69,76)]:
    j=rr[rr.a.between(lo,hi)&(rr.wo==0)]; w=rr[rr.a.between(lo,hi)&(rr.wo>0)]; s=mm[mm.a.between(lo,hi)]
    print(lab,'전세',len(j),j.bo.median(),j.bo.quantile([.25,.75]).tolist(),'월세',len(w),w.bo.median(),w.wo.median(),'매매',len(s),s.p.median())
    print(j.groupby('단지명').bo.agg(['size','median']).join(s.groupby('단지명').p.agg(['size','median']),rsuffix='_m',how='outer').to_string())
    if lab=='84': print(j.groupby('계약년월').bo.agg(['size','median']).to_string())
# asan all 2019+ 84
ma=m[m['시군구'].str.contains('아산')&(m.y>=2019)&m.a.between(80,86)]; ra=r[r['시군구'].str.contains('아산')&(r.y>=2019)&r.a.between(80,86)&(r.wo==0)]
print('아산 2019+ 84 매매',len(ma),ma.p.median(),'전세',len(ra),ra.bo.median())
tot=rr; print('임대 전체',len(tot),'월세',(tot.wo>0).sum())
