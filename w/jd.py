import pandas as pd
b=pd.read_pickle('jungdong.pkl')
b=b[b['해제사유발생일'].isna()|(b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan']))].copy()
b=b[b['단지명'].notna()]
b=b[b['건축년도'].notna()&b['유형'].isna()] if False else b[b['건축년도'].notna()]; b['y']=pd.to_numeric(b['건축년도']).astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float).round(0); b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
eun={'은하마을(주공1)','은하마을(주공2)','은하마을(대우)','은하마을(동부)','은하마을(효성)','은하마을(쌍용)'}
ban={'반달마을(삼익)','반달마을(동아)','반달마을(선경)','반달마을(건영)'}
big=b.groupby('단지명').size()
def gg(r):
    n=r['단지명']
    if n in eun: return '은하마을'
    if n in ban: return '반달마을A'
    if r.y>=2005: return '2005년 이후 준공'
    if r.y>1996 or big[n]<150: return None
    return '나머지 구축'
b['g']=b.apply(gg,axis=1); b=b[b.g.notna()]
print(b.groupby('g')['단지명'].nunique().to_dict())
def per(lo,hi): return b[(b.ym>=lo)&(b.ym<=hi)].groupby(['g','단지명','a'])['p'].agg(['mean','size'])
A=per(202401,202410)
for nm,lo,hi in [('2024.12~2025.3',202412,202503),('2025.4~2025.9',202504,202509),('2025.10~2026.2',202510,202602),('2026.3~2026.8',202603,202608)]:
    m=A.join(per(lo,hi),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=m.mean_B/m.mean_A-1
    print(nm, m.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
m.to_pickle('jd_pairs.pkl')
m2=per(202107,202112).join(per(202603,202608),lsuffix='_A',rsuffix='_B',how='inner'); m2['c']=m2.mean_B/m2.mean_A-1
print('vs2021H2', m2.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
m3=per(202506,202608)
x=m.reset_index(); print(x[x.g.isin(['은하마을','반달마을A'])].groupby(['g','단지명']).agg(c=('c','mean'),k=('c','size'),n=('size_B','sum')).round(3))
print(x[x.g.isin(['은하마을','반달마을A'])][['단지명','a','mean_A','mean_B','size_A','size_B','c']].round(3).to_string())
# 은하 지정 전후 (2026.6.15)
e1=per(202601,202605); e2=per(202606,202608); m4=e1.join(e2,lsuffix='_A',rsuffix='_B',how='inner'); m4['c']=m4.mean_B/m4.mean_A-1
print('지정전후 2026.1-5→6-8', m4.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
