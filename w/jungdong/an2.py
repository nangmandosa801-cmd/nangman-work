# 중동 재건축 글(gs/jungdong_re.py)의 실거래 계산 — 2026.10.7
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
def gg(r):
    n=r['단지명']
    if n in eun: return '은하'
    if n in ban: return '반달A'
    if r.y>=2005: return '2005후'
    if 1992<=r.y<=1997: return '구축'
    return None
b['g']=b.apply(gg,axis=1); b=b[b.g.notna()]
MIN=2
def per(lo,hi,minn=MIN):
    x=b[(b.ym>=lo)&(b.ym<=hi)].groupby(['g','단지명','ar'])['p'].agg(['median','size'])
    return x[x['size']>=minn]
def cmp(a,bb,minn=MIN):
    m=per(*a,minn).join(per(*bb,minn),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100
    return m
def summ(m):
    return m.groupby('g').agg(mean=('c','mean'),med=('c','median'),k=('c','size'),up=('c',lambda s:(s>0).sum()),nA=('size_A','sum'),nB=('size_B','sum'),lo=('c','min'),hi=('c','max'),dan=('c',lambda s:s.index.get_level_values('단지명').nunique())).round(1)
if __name__=='__main__':
    A=(202401,202410); B=(202603,202608); P=(202107,202206)
    print('전체 건수 B',len(b[(b.ym>=B[0])&(b.ym<=B[1])]), b[(b.ym>=B[0])&(b.ym<=B[1])].groupby('g').size().to_dict())
    print('전체 건수 A', b[(b.ym>=A[0])&(b.ym<=A[1])].groupby('g').size().to_dict())
    print('전체 건수 P', b[(b.ym>=P[0])&(b.ym<=P[1])].groupby('g').size().to_dict())
    for nm,a,bb in [('발표 전→2026.3~8',A,B),('발표 전→2025.3~8',A,(202503,202508)),('2025.3~8→2026.3~8',(202503,202508),B),('2021.7~2022.6→2026.3~8',P,B),('2026.1~5→2026.6~8',(202601,202605),(202606,202608))]:
        m=cmp(a,bb); print('==',nm); print(summ(m).T.to_string())
    for mn in (1,3):
        print('== MIN',mn,'main'); print(summ(cmp(A,B,mn)).T.to_string()); print('peak'); print(summ(cmp(P,B,mn)).T.to_string())
    m=cmp(A,B).reset_index(); x=m[m.g.isin(['은하','반달A'])]
    print(x.groupby(['g','단지명']).agg(c=('c','mean'),k=('c','size'),nA=('size_A','sum'),nB=('size_B','sum')).round(1))
    print(x.round(1).to_string())
    print(cmp(P,B).reset_index().query("g in ['은하','반달A']").round(1).to_string())
    # 세 기간 값
    q=per(*A).join(per(*P),rsuffix='_P',how='outer').join(per(*B),rsuffix='_B',how='outer').reset_index()
    print(q[q.g.isin(['은하','반달A'])].to_string())
    # 월별 은하·반달 건수 (2026)
    print(b[(b.ym>=202601)&b.g.isin(['은하','반달A'])].groupby(['ym','g']).size().unstack().to_string())
