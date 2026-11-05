import pandas as pd, numpy as np
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
M=[]
for y in ['M2025','M2026']:
    m=pd.read_pickle(f'/home/claude/rtn/{y}.pkl'); m=m[m['시군구'].str.contains('경기도 하남시')]
    M.append(m)
m=pd.concat(M); m=m[m['해제사유발생일'].astype(str).str.strip().isin(['-',''])|m['해제사유발생일'].isna()]
m['p']=num(m['거래금액(만원)']); m['a']=num(m['전용면적(㎡)']); m['ym']=m['계약년월'].astype(int)
m.to_pickle('m.pkl')
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); r=r[r['시군구'].str.contains('경기도 하남시')].copy()
r['dep']=num(r['보증금(만원)']); r['mon']=num(r['월세금(만원)']); r['a']=num(r['전용면적(㎡)']); r['ym']=r['계약년월'].astype(int)
r['old']=num(r['종전계약 보증금(만원)']); r['oldm']=num(r['종전계약 월세(만원)'])
r.to_pickle('r.pkl'); print(len(m),len(r), m.ym.max(), r.ym.max())
