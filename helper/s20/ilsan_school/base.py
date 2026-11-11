import pandas as pd, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
R='/home/claude/rtn/'
def get():
    ms=[load(R+f'rawG/MG{y}_{g}.csv') for y in [2021,2022,2023,2024] for g in ['41287','41285']]
    ms+=[pd.read_pickle(R+'M2025.pkl'),pd.read_pickle(R+'M2026.pkl')]
    m=pd.concat(ms,ignore_index=True)
    m=m[m['시군구'].str.contains('고양시 일산서구|고양시 일산동구')]
    m=m[m['해제사유발생일'].astype(str).str.strip()=='-']
    m=m[m['거래유형'].astype(str).str.strip()!='직거래']
    m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
    m['년']=m['계약년월'].str[:4]; m['월']=m['계약년월'].str[4:].astype(int)
    m['단']=m['단지명'].str.replace(' ',''); m['동']=m['시군구'].str.split().str[-1]; m['건']=m['건축년도'].astype(int)
    rs=[load(R+f'rawG/RG{y}_{g}.csv') for y in [2024,2025] for g in ['41287','41285']]+[pd.read_pickle(R+'R2026.pkl')]
    r=pd.concat(rs,ignore_index=True)
    r=r[r['시군구'].str.contains('고양시 일산서구|고양시 일산동구')]
    r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
    r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int)
    r['단']=r['단지명'].str.replace(' ',''); r['동']=r['시군구'].str.split().str[-1]; r['건']=pd.to_numeric(r['건축년도'],errors='coerce')
    return m,r
