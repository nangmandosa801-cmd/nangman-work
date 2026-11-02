# -*- coding: utf-8 -*-
# 구리 토평2지구 글(topyeong2b) 계산 — 2026.10.7
# 자료: /home/claude/w/apt_all.pkl (국토교통부 아파트 매매 실거래 · 2026년 8월 계약분까지 · 해제 거래는 이미 빠져 있음)
# 규칙: 같은 단지 · 같은 전용면적(㎡ 소수점 버림)끼리만 비교. 두 기간 모두 2건 이상 팔린 묶음만. 여러 단지를 섞은 중앙값은 내지 않음.
#       묶음마다 「기간별 중앙값의 오른 폭」을 내고, 동별로는 그 오른 폭의 중앙값과 묶음 수 · 건수만 말함.
import pandas as pd, numpy as np, sys
d=pd.read_pickle('/home/claude/w/apt_all.pkl')
g=d[d['시군구'].str.contains('구리시')].copy()
g['ym']=g['계약년월'].astype(int); g['amt']=g['p']*10000   # p = 억원
g['a0']=np.floor(g['a']).astype(int)
g['dong']=g['읍면동']
def cmp(p1,p2,dongs=None,minn=2):
    """p1,p2 = (시작,끝) 계약년월. 돌려줌: 묶음별 표"""
    x=g if dongs is None else g[g['dong'].isin(dongs)]
    a=x[(x.ym>=p1[0])&(x.ym<=p1[1])].groupby(['dong','단지명','건축년도','a0'])['amt'].agg(['median','count'])
    b=x[(x.ym>=p2[0])&(x.ym<=p2[1])].groupby(['dong','단지명','건축년도','a0'])['amt'].agg(['median','count'])
    m=a.join(b,lsuffix='1',rsuffix='2',how='inner'); m=m[(m.count1>=minn)&(m.count2>=minn)].copy()
    m['chg']=(m.median2/m.median1-1)*100; m['diff']=m.median2-m.median1
    return m.reset_index()
def summ(m,label):
    print('\n==',label)
    for dg,s in m.groupby('dong'):
        print('  %s 묶음 %d · 건수 %d→%d · 오른 폭 중앙값 %.1f%% (%.1f ~ %.1f) · 오른 묶음 %d'%(dg,len(s),s.count1.sum(),s.count2.sum(),s.chg.median(),s.chg.min(),s.chg.max(),(s.chg>0).sum()))
    print('  구리 전체 묶음 %d · 오른 폭 중앙값 %.1f%%'%(len(m),m.chg.median()))
W={'A 후보지 발표 앞 1년(2022.11~2023.10) → 발표 뒤 1년(2023.11~2024.10)':((202211,202310),(202311,202410)),
   'B 지구 지정 앞 1년(2025.1~2025.12) → 2026.1~8':((202501,202512),(202601,202608)),
   'C 후보지 발표 앞 1년(2022.11~2023.10) → 최근 1년(2025.9~2026.8)':((202211,202310),(202509,202608)),
   'D 지구 지정 앞 6달(2025.7~12) → 뒤 6달(2026.1~6 · 규제 앞)':((202507,202512),(202601,202606)),
   'E 최근 1년 전(2024.9~2025.8) → 최근 1년(2025.9~2026.8)':((202409,202508),(202509,202608))}
R={}
for k,(p1,p2) in W.items():
    m=cmp(p1,p2); R[k]=m; summ(m,k)
if __name__=='__main__':
    pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
    for k in ['C 후보지 발표 앞 1년(2022.11~2023.10) → 최근 1년(2025.9~2026.8)','B 지구 지정 앞 1년(2025.1~2025.12) → 2026.1~8']:
        m=R[k]; s=m[m.dong.isin(['토평동','교문동','수택동'])].sort_values(['dong','단지명','a0'])
        print('\n##',k); print(s[['dong','단지명','건축년도','a0','median1','count1','median2','count2','chg','diff']].to_string(index=False))
    # 달마다 거래 건수 (지구가 걸친 세 동)
    x=g[g.dong.isin(['토평동','교문동','수택동'])&(g.ym>=202301)]
    print(x.groupby(['ym','dong']).size().unstack(fill_value=0).to_string())

# ── 토지 (부동산DB.parquet · 자료=토지) : 구리시 토평 · 교문 · 수택 · 아천동 · 지분과 해제 거래 제외 · 같은 지목 · 같은 용도지역끼리만
def land():
    import pyarrow.parquet as pq, pyarrow.compute as pc, pyarrow as pa
    t=pq.read_table('/mnt/attach/outputs/부동산DB.parquet',columns=['시군구','자료','유형','용도지역','도로조건','거래금액(만원)','계약년월','지분구분','해제사유발생일','지목','계약면적','읍면동','시군'],filters=[('시군','=','구리시')]).to_pandas()
    return t
if __name__=='__main__':
    t=land(); print(t['자료'].value_counts())
    L=t[t['자료'].astype(str).str.contains('토지')].copy()
    print(len(L)); print(L[['지분구분','해제사유발생일']].astype(str).apply(lambda s:s.value_counts().head(4).to_dict()))
    L['ym']=L['계약년월'].astype(int); L['amt']=pd.to_numeric(L['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce'); L['ar']=pd.to_numeric(L['계약면적'],errors='coerce')
    L=L[L['읍면동'].isin(['토평동','교문동','수택동','아천동'])&(L.ym>=202111)]
    whole=L[~L['지분구분'].astype(str).str.contains('지분')&~L['해제사유발생일'].astype(str).str.match(r'^\d')]
    whole=whole[whole.ar>=100]
    whole['per']=np.where(whole.ym<202311,'발표 앞 2년(2021.11~2023.10)',np.where(whole.ym<202601,'발표 뒤~지정(2023.11~2025.12)','지정 뒤(2026.1~8)'))
    print(whole.ym.max()); print(whole.groupby(['읍면동','지목','용도지역','per']).size().unstack(fill_value=0).to_string())
    # 토평동 · 밭(전) · 개발제한구역 : 기간별 건수 (통째 / 지분 · 넓이 구간)
    T=t[t['자료'].astype(str).str.contains('토지')].copy()
    T['ym']=T['계약년월'].astype(int); T['ar']=pd.to_numeric(T['계약면적'],errors='coerce'); T['amt']=pd.to_numeric(T['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
    T=T[~T['해제사유발생일'].astype(str).str.match(r'^\d')]
    T['jb']=T['지분구분'].astype(str).str.contains('지분')
    for dg in ['토평동','교문동','아천동','수택동']:
        x=T[(T['읍면동']==dg)&(T['용도지역']=='개발제한구역')&(T.ym>=202111)]
        x=x.assign(per=np.where(x.ym<202311,'1 앞 2년(2021.11~2023.10)',np.where(x.ym<202511,'2 뒤 2년(2023.11~2025.10)','3 그 뒤(2025.11~2026.7)')))
        print(dg,'개발제한구역 전체 지목'); print(x.groupby(['per','jb']).size().unstack(fill_value=0).to_string())
        y=x[x['지목']=='전']; print(dg,'밭'); print(y.groupby(['per','jb']).agg(n=('ar','size'),ar_med=('ar','median')).to_string())
    x=T[(T['읍면동']=='토평동')&(T['용도지역']=='개발제한구역')&(T['지목']=='전')&(T.ym>=202111)].sort_values('ym')
    print(x[['ym','지목','ar','amt','jb','도로조건']].to_string(index=False))
