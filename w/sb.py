import pandas as pd
b=pd.read_pickle('gunpo.pkl')
b=b[(b['해제사유발생일'].isna()|(b['해제사유발생일']=='-'))&b['읍면동'].isin(['산본동','금정동'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float).round(0); b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
first={'백합','삼성장미','주공11','백두(동성)','한양백두','백두(극동)'}
second={'목화','무궁화(화성)','충무주공(872)','퇴계주공(351~359동)','퇴계주공(360~368동)','율곡','세종','한일을지','삼익가든을지','솔거대림','신안모란','한양목련','우방,한국공영목련','동백(우성)'}
big=b.groupby('단지명').size(); 
def gg(r):
    if r.y>=2005: return '2005년 이후 준공'
    if r.y>1996: return None
    if big[r['단지명']]<150: return None
    n=r['단지명']
    return '1차 선정' if n in first else '2차 제안' if n in second else '나머지 구축'
b['g']=b.apply(gg,axis=1); b=b[b.g.notna()]
print(b.groupby('g')['단지명'].nunique())
def per(lo,hi): return b[(b.ym>=lo)&(b.ym<=hi)].groupby(['g','단지명','a'])['p'].agg(['mean','size'])
A=per(202401,202410)
for nm,lo,hi in [('2024.12~2025.3',202412,202503),('2025.4~2025.9',202504,202509),('2025.10~2026.2',202510,202602),('2026.3~2026.8',202603,202608)]:
    m=A.join(per(lo,hi),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=m.mean_B/m.mean_A-1
    print(nm, m.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
m.to_pickle('sb_pairs.pkl')
pk=per(202107,202112); m2=pk.join(per(202603,202608),lsuffix='_A',rsuffix='_B',how='inner'); m2['c']=m2.mean_B/m2.mean_A-1
print('vs2021H2', m2.groupby('g')['c'].agg(['mean','size']).round(3).to_dict())
x=m.reset_index(); print(x[x.g.isin(['1차 선정','2차 제안'])].groupby(['g','단지명']).agg(c=('c','mean'),k=('c','size'),n=('size_B','sum')).round(3))
x['bk']=pd.cut(x.a,[0,50,70,90,300]); print(x[x.g!='2005년 이후 준공'].groupby('bk',observed=True)['c'].agg(['mean','size']).round(3))
