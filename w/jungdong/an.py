import pandas as pd, numpy as np
pd.set_option('display.max_rows',500,'display.width',250)
b=pd.read_pickle('bc.pkl')
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float); b['ar']=b['a'].round(0)
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
b['pp']=b['p']/(b['a']/3.3058)
eun={'은하마을(주공1)','은하마을(주공2)','은하마을(대우)','은하마을(동부)','은하마을(효성)','은하마을(쌍용)'}
ban={'반달마을(삼익)','반달마을(동아)','반달마을(선경)','반달마을(건영)'}
big=b.groupby('단지명').size()
def gg(r):
    n=r['단지명']
    if n in eun: return '은하'
    if n in ban: return '반달A'
    if r.y>=2005: return '2005후'
    if 1992<=r.y<=1997 and big[n]>=150: return '구축'   # 1기 신도시 때 지은 단지
    return None
b['g']=b.apply(gg,axis=1)
b.to_pickle('bc2.pkl')
