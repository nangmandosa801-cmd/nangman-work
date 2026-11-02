# 위례선 트램 글(gs/wirye_tram.py)의 실거래 계산 — 2026.10.7
# 자료: w/apt_all.pkl → 송파구 장지 · 거여 · 마천동, 성남 수정구 창곡 · 복정동, 하남 학암 · 감이동만 뽑은 wr.pkl(아파트 매매 · 2026.8 계약분까지) · 해제 거래 제외
# 셈법: 같은 단지 · 같은 전용면적(㎡ 반올림)을 한 묶음 → 기간별 건수와 중앙값 → 두 기간 모두 MIN건(2건) 이상 팔린 묶음만 → 묶음별 변화율의 중앙값. 단지가 섞인 중앙값은 쓰지 않는다.
# 단지와 정거장 거리: geo.py(구글 지도 장소 좌표 · 단지 가운데 점에서 정거장 점까지 직선거리). 좌표를 못 찾은 단지(위례신도시송파푸르지오 · 위례역푸르지오6단지 · 위례자이더시티 · 송파레이크힐 · 포레나송파 · 힐트리움송파)는 뺐다.
# 기간: 착공식(2023.4.13)을 한 해의 3~8월 → 2026.3~8(3년) · 2025.3~8 → 2026.3~8(1년) · 바꿔 본 기간 2023.9~2024.8 → 2025.9~2026.8
import pandas as pd, numpy as np, os
from geo import APT,TRAM,SUB,near
pd.set_option('display.max_rows',600,'display.width',260)
W='/home/claude/w/wirye_tram/wr.pkl'
if not os.path.exists(W):
    d=pd.read_pickle('/home/claude/w/apt_all.pkl')
    m=((d['시군구'].str.contains('송파구'))&(d['읍면동'].isin(['장지동','거여동','마천동'])))|((d['시군구'].str.contains('수정구'))&(d['읍면동'].isin(['창곡동','복정동'])))|((d['시군구'].str.contains('하남'))&(d['읍면동'].isin(['학암동','감이동'])))
    d[m].to_pickle(W)
b=pd.read_pickle(W)
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['ym']=b['계약년월'].astype(int); b['ar']=b['전용면적(㎡)'].astype(float).round(0)
b['pm']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float); b['nm']=b['단지명']; b['dong']=b['읍면동']
G=pd.DataFrame([dict(nm=nm,si=si,tram=near((la,lo),TRAM)[0],dtr=near((la,lo),TRAM)[1],sub=near((la,lo),SUB)[0],ds=near((la,lo),SUB)[1]) for nm,si,la,lo,ad in APT])
G['near']=np.where(G.dtr<=350,'정거장 350m 안','350m 밖'); G['near3']=np.where(G.dtr<=350,'350m 안',np.where(G.dtr>500,'500m 밖','사이'))
def band(a): return '60㎡ 아래' if a<61 else ('74~86㎡' if 74<=a<=86 else ('95~117㎡' if 95<=a<=117 else '그 밖'))
def per(lo,hi,minn):
    g=b[(b.ym>=lo)&(b.ym<=hi)].groupby(['dong','nm','ar'])['pm'].agg(['median','size'])
    return g[g['size']>=minn]
def cmp(A,B,minn=2):
    m=per(*A,minn).join(per(*B,minn),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100; m['d']=m.median_B-m.median_A
    m=m.reset_index().merge(G,on='nm',how='inner'); m['band']=m.ar.map(band); return m
def summ(m,by):
    return m.groupby(by).agg(med=('c','median'),k=('c','size'),dan=('nm','nunique'),up=('c',lambda s:(s>0).sum()),nA=('size_A','sum'),nB=('size_B','sum'),lo=('c','min'),hi=('c','max'),dmed=('d','median')).round(1)
P=[('① 3년: 착공식을 한 2023.3~8 → 2026.3~8',(202303,202308),(202603,202608)),
   ('② 1년: 2025.3~8 → 2026.3~8',(202503,202508),(202603,202608)),
   ('③ 바꿔 본 기간: 2023.9~2024.8 → 2025.9~2026.8',(202309,202408),(202509,202608)),
   ('④ 비쌌던 때: 2021.7~2022.6 → 2026.3~8',(202107,202206),(202603,202608))]
if __name__=='__main__':
    print(G.sort_values(['si','dtr']).to_string())
    for nm,A,B in P:
        for mn in (2,1):
            m=cmp(A,B,mn); w=m[m.si!='거여마천']; o=m[m.si=='거여마천']
            print('\n=====',nm,'· 묶음 조건',mn,'건 =====')
            print('위례 전체 %.1f%% · 묶음 %d · 단지 %d · 오른 묶음 %d · 건수 %d → %d · 오른 금액 중앙 %d만원'%(w.c.median(),len(w),w.nm.nunique(),(w.c>0).sum(),w.size_A.sum(),w.size_B.sum(),w.d.median()))
            print('-- 정거장 거리(위례)'); print(summ(w,'near').to_string()); print(summ(w,'near3').to_string())
            for th in (250,300,400):
                x=w.assign(n2=np.where(w.dtr<=th,'안','밖')); print('   거리 %dm로 바꾸면'%th,x.groupby('n2').c.agg(['median','size']).round(1).to_dict())
            print('-- 면적대(위례)'); print(summ(w,'band').to_string())
            print('-- 면적대 × 정거장 거리'); print(summ(w,['band','near']).to_string()); print(summ(w,['band','near3']).to_string())
            print('-- 시(위례)'); print(summ(w,'si').to_string()); print(summ(w,['band','si']).to_string())
            print('-- 옛 동네(5호선 거여역 · 마천역 둘레 · 거여동 · 마천동)  전체 %.1f%% · 묶음 %d · 단지 %d'%(o.c.median(),len(o),o.nm.nunique())); print(summ(o,'band').to_string())
            if mn==2: print(m.sort_values(['band','ar','c']).round(1)[['si','nm','ar','median_A','size_A','median_B','size_B','c','d','tram','dtr','sub','ds']].to_string())
    # 2026.3~8 위례 거래(좌표를 확인한 단지) — 시 · 면적대별 건수
    n=b.merge(G,on='nm'); n=n[(n.ym>=202603)&(n.ym<=202608)&(n.si!='거여마천')].copy(); n['band']=n.ar.map(band)
    print('\n2026.3~8 위례 거래',len(n)); print(n.groupby(['si','band']).size().unstack().fillna(0).astype(int).to_string())
    # 정거장이 선 곳: 송파 7 · 성남 5 · 하남 0 / 하남 단지 가운데 정거장 350m 안
    print(G[G.si=='하남'].sort_values('dtr')[['nm','tram','dtr']].to_string())
