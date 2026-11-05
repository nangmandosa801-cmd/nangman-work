import pandas as pd, numpy as np, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
def prep(d):
    d=d[d['시군구'].str.contains('경기도 하남시')].copy()
    d=d[d['해제사유발생일'].astype(str).str.strip().isin(['-',''])|d['해제사유발생일'].isna()]
    d['p']=num(d['거래금액(만원)']); d['a']=num(d['전용면적(㎡)']); d['ym']=d['계약년월'].astype(int); d['dd']=d['계약일'].astype(int)
    d['dong']=d['시군구'].str.split().str[2]
    d['ar']=d['a'].round().astype(int)
    d['key']=d['dong']+'|'+d['단지명']+'|'+d['ar'].astype(str)
    d['yr']=d['ym']//100; d['mo']=d['ym']%100
    return d
m26=prep(load('/home/claude/rtn/rawN/M2026_41000.csv'))
m25=prep(pd.read_pickle('/home/claude/rtn/M2025.pkl'))
m21=prep(load('/home/claude/rtn/rawN/M2021_41000.csv'))
m=pd.concat([m21,m25,m26],ignore_index=True)
m.to_pickle('h.pkl')
print(len(m21),len(m25),len(m26))
print(m26.groupby('mo').size().to_dict())
print(m25.groupby('mo').size().to_dict())
