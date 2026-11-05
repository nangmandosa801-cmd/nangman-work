# 학군지 6화 · 분당 수내 · 서현 소형 평당가 역전 — 실거래 집계 → ana.json
import pandas as pd, numpy as np, json
R='/home/claude/rtn/'
m=pd.read_pickle(R+'MB_2021_2026.pkl')            # 분당구 2021~2026.10 매매 · 해제 뺌 · 직거래 뺌
m['nm']=m['단지명'].str.replace(' ',''); m['py']=m['p']/(m['a']/3.3058); m['mo']=m['계약년월'].str[4:].astype(int)
r=pd.read_pickle(R+'RB_2024_2026.pkl')            # 분당구 2024~2026.10 전세
def binA(a):
    if a<50: return 'S'
    if a<62: return '59'
    if 83<=a<=86: return '84'
    if 99<=a<=103: return '101'
    if 127<=a<=136: return '131'
    if a>=160: return '164'
    return None
m['bin']=m['a'].apply(binA); r['bin']=r['a'].apply(binA)
G={'sunae':['양지마을(금호1)','양지마을(2단지)(청구)','양지마을(3단지)(금호)','양지마을(5단지)(한양501-514)','양지마을(5단지)(한양515-529)','양지마을(6단지)(금호,청구)','양지마을(6단지)(한양603동)','파크타운(대림)','파크타운(롯데)','파크타운(삼익)','파크타운(서안)'],
   'seohyeon':['시범삼성','시범한신','시범우성','시범현대','시범한양'],
   'yatap':['탑마을(주공)','매화마을(주공3)','매화마을(주공4)','장미마을(현대)','탑마을(선경)1','장미마을(동부)','장미마을(코오롱)1','탑마을(경남)1','탑마을(벽산)','탑마을(대우)'],
   'gumi':['하얀마을(5단지)(주공)','무지개(12단지)(주공)','까치마을(2단지)(주공)','까치마을(1단지)(대우롯데선경)','무지개(2단지)(엘지)','까치마을(3단지)(신원)','까치마을(4단지)(롯데)','까치마을(4단지)(선경)','무지개(1단지)(대림)','무지개(5단지)(청구)']}
G['hak']=G['sunae']+G['seohyeon']; G['pair']=G['yatap']+G['gumi']
BINS=['S','59','84','101','131','164']; YS=['2021','2022','2023','2024','2025','2026']
def st(g):
    return dict(n=int(len(g)),med=float(g.p.median()) if len(g) else None,max=int(g.p.max()) if len(g) else None,py=float(g.py.median()) if len(g) else None,a=float(g.a.median()) if len(g) else None)
J={'grp':{},'dan':{},'rent':{},'meta':{}}
for k,v in G.items():
    x=m[m.nm.isin(v)]
    J['grp'][k]={b:{y:st(x[(x.bin==b)&(x.y==y)]) for y in YS} for b in BINS}
    J['grp'][k]['total']={y:int((x.y==y).sum()) for y in YS}
# 단지별 · 면적별 (2021 · 2023 · 2025 · 2026)
D=[('양지마을(5단지)(한양501-514)',28,29,'h5_28'),('양지마을(5단지)(한양501-514)',35,36,'h5_35'),('양지마을(5단지)(한양501-514)',42,44,'h5_43'),('양지마을(5단지)(한양501-514)',48,50,'h5_49'),
   ('시범한양',28,30,'sh_29'),('시범한양',35,36,'sh_35'),('시범우성',45,47,'su_46'),('시범현대',48,50,'sc_49'),
   ('양지마을(금호1)',84,85,'k1_84'),('양지마을(금호1)',133,135,'k1_134'),('양지마을(금호1)',163,165,'k1_164'),('양지마을(금호1)',190,200,'k1_196'),
   ('양지마을(2단지)(청구)',84,85,'c2_84'),('양지마을(2단지)(청구)',134,136,'c2_135'),('양지마을(5단지)(한양515-529)',134,136,'h5b_135'),('양지마을(5단지)(한양515-529)',163,165,'h5b_164'),
   ('시범한양',59,60,'sh_59'),('시범한양',84,85,'sh_84'),('시범한양',134,136,'sh_135'),('시범한양',164,165,'sh_164'),
   ('시범우성',84,85,'su_84'),('시범우성',128,135,'su_131'),('시범현대',84,85,'sc_84'),('시범현대',128,131,'sc_130'),('시범현대',185,195,'sc_190'),
   ('시범삼성',84,85,'ss_84'),('시범삼성',190,195,'ss_192'),('시범한신',84,85,'sn_84'),('시범한신',132,134,'sn_133'),
   ('파크타운(서안)',59,60,'ps_59'),('파크타운(서안)',84,85,'ps_84'),('파크타운(롯데)',101,103,'pl_102'),('파크타운(대림)',130,136,'pd_134'),('파크타운(서안)',184,187,'ps_185'),
   ('탑마을(주공)',35,36,'tj_35'),('탑마을(주공)',42,43,'tj_42'),('하얀마을(5단지)(주공)',35,39,'hy_36'),('장미마을(현대)',84,85,'jh_84'),('장미마을(현대)',133,134,'jh_133'),('까치마을(1단지)(대우롯데선경)',84,85,'kk_84'),('까치마을(3단지)(신원)',130,132,'k3_131')]
for nm,lo,hi,key in D:
    x=m[(m.nm==nm)&(m.a>=lo)&(m.a<=hi)]
    J['dan'][key]={'nm':nm,'built':x['건축년도'].iloc[0] if len(x) else None,**{y:st(x[x.y==y]) for y in ['2021','2023','2025','2026']}}
# 보고서가 든 거래 확인
x=m[(m.nm=='양지마을(5단지)(한양501-514)')&(m.a>48)&(m.a<49)&(m.y=='2026')].sort_values('p',ascending=False).head(3)
J['meta']['h5_49_top']=x[['계약년월','계약일','p','층']].astype(str).values.tolist()
x=m[(m.nm=='양지마을(5단지)(한양501-514)')&(m.a>42)&(m.a<43)&(m.y=='2026')].sort_values('p',ascending=False).head(2)
J['meta']['h5_43_top']=x[['계약년월','계약일','p','층']].astype(str).values.tolist()
x=m[(m.nm=='시범한양')&(m.a>35)&(m.a<36)&(m.y=='2026')].sort_values('p',ascending=False).head(4)
J['meta']['sh_35_top']=x[['계약년월','계약일','p','층']].astype(str).values.tolist()
x=m[(m.nm=='양지마을(금호1)')&(m.a>=190)&(m.y=='2026')].sort_values('p',ascending=False)
J['meta']['k1_196_2026']=x[['전용면적(㎡)','계약년월','p','층']].astype(str).values.tolist()
# 전세
for k,v in G.items():
    x=r[r.nm.isin(v)]
    o={}
    for y in ['2024','2025','2026']:
        g=x[x.y==y]; n=len(g)
        o[y]=dict(n=int(n),jan2=float((g.mo<=2).mean()*100) if n else None,renew=float((g['계약구분']=='갱신').mean()*100) if n else None)
    for y in ['2025','2026']:
        g=x[(x.y==y)&(x['계약구분']=='신규')]
        o['new'+y]={b:dict(n=int(len(gg)),med=float(gg.dep.median())) for b,gg in g.groupby('bin')}
        g=x[(x.y==y)&(x['계약구분']=='갱신')]
        o['ren'+y]={b:dict(n=int(len(gg)),med=float(gg.dep.median())) for b,gg in g.groupby('bin')}
    J['rent'][k]=o
g=r; J['rent']['bundang']={y:dict(n=int((g.y==y).sum()),jan2=float((g[g.y==y].mo<=2).mean()*100),renew=float((g[g.y==y]['계약구분']=='갱신').mean()*100)) for y in ['2024','2025','2026']}
rg=pd.read_pickle(R+'R2026.pkl'); rg=rg[(rg['전월세구분']=='전세')&(rg['시군구'].str.startswith('경기도'))]
mo=rg['계약년월'].str[4:].astype(int)
J['rent']['gyeonggi2026']=dict(n=int(len(rg)),jan2=float((mo<=2).mean()*100),renew=float((rg['계약구분']=='갱신').mean()*100))
# 분당구 2026 매매 월별 (10.15 뒤)
x=m[m.nm.isin(G['hak'])]
J['meta']['hak_monthly_2026']={k:int(v) for k,v in x[x.y=='2026'].groupby('계약년월').size().to_dict().items()}
J['meta']['hak_monthly_2025']={k:int(v) for k,v in x[x.y=='2025'].groupby('계약년월').size().to_dict().items()}
json.dump(J,open('ana.json','w'),ensure_ascii=False,indent=1)
print('ok')
