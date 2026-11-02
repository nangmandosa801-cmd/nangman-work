import pandas as pd
b=pd.read_pickle('ilsan.pkl')
b=b[b['해제사유발생일'].isna()|(b['해제사유발생일']=='-')].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float).round(0); b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
first={'백송마을(삼부)','백송마을(대림)','백송마을(한신)','백송마을(풍림)','백송마을(삼호)',
'후곡마을(현대3)','후곡마을(금호)','후곡마을(한양)','후곡마을(동아10)','후곡마을(서안)','후곡마을(임광)','후곡마을(건영15)',
'강촌마을(라이프)','강촌마을(선경)','강촌마을(코오롱)','강촌마을(우방)'}
def gg(r):
    if r.y>=2005: return '2005년 이후 준공'
    if r.y>1996: return None
    return '1차 선정' if r['단지명'] in first else '미선정 구축'
b['g']=b.apply(gg,axis=1); b=b[b.g.notna()]
print(b[b.g=='1차 선정']['단지명'].nunique(), b[b.g=='미선정 구축']['단지명'].nunique())
def per(lo,hi): return b[(b.ym>=lo)&(b.ym<=hi)].groupby(['g','단지명','a'])['p'].agg(['mean','size'])
A=per(202401,202410)
for nm,lo,hi in [('2024.12~2025.3',202412,202503),('2025.4~2025.9',202504,202509),('2025.10~2026.2',202510,202602),('2026.3~2026.8',202603,202608)]:
    m=A.join(per(lo,hi),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=m.mean_B/m.mean_A-1
    print(nm, m.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
m.to_pickle('il_pairs.pkl')
pk=per(202107,202112); m2=pk.join(per(202603,202608),lsuffix='_A',rsuffix='_B',how='inner'); m2['c']=m2.mean_B/m2.mean_A-1
print('vs2021H2', m2.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
x=m.reset_index(); print(x[x.g=='1차 선정'].groupby('단지명').agg(c=('c','mean'),k=('c','size')).round(3))
x['bk']=pd.cut(x.a,[0,50,70,90,300]); print(x[x.g!='2005년 이후 준공'].groupby('bk')['c'].agg(['mean','size']).round(3))
