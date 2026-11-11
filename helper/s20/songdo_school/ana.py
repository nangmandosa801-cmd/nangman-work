import pandas as pd, json
R='/home/claude/rtn/'
m=pd.read_pickle(R+'MI_yeonsu_2021_2026.pkl'); r=pd.read_pickle(R+'RI_yeonsu_2024_2026.pkl')
m=m[m['시군구'].str.endswith('송도동')&(m['해제사유발생일'].astype(str).str.strip()=='-')&(m['거래유형'].astype(str).str.strip()!='직거래')].copy()
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int); m['년']=m['계약년월'].str[:4]; m['단']=m['단지명'].str.replace(' ','')
r=r[r['시군구'].str.endswith('송도동')].copy()
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int)
r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int); r['단']=r['단지명'].str.replace(' ','')
G={'1공구':['더샵그린워크1차','더샵그린워크2차','송도더샵그린워크3차(17-1블럭)','송도더샵그린워크3차(18-1블럭)','더샵엑스포9단지','더샵엑스포10단지','송도더샵그린애비뉴7단지','송도더샵그린애비뉴8단지','송도더샵하버뷰(D13)','송도더샵하버뷰(D14)','송도더샵하버뷰(D15)','송도자이하버뷰2단지','더샵퍼스트월드'],
 '2공구':['송도풍림아이원1단지','송도풍림아이원2단지','송도풍림아이원3단지','송도풍림아이원4단지','송도금호어울림','송도한진해모로','성지리벨루스','아이파크송도'],
 '웰카운티':['송도웰카운티1단지','송도웰카운티2단지','송도웰카운티3단지','송도웰카운티4단지'],
 '8공구':['e편한세상송도','더샵송도마리나베이','랜드마크시티센트럴더샵','송도SKVIEW','송도오션파크베르디움','호반써밋송도'],
 '6공구':['힐스테이트레이크송도1차','힐스테이트레이크송도2차','힐스테이트레이크송도3차','힐스테이트레이크송도4차','송도자이더스타','송도자이크리스탈오션','송도LuxeOceanSKVIEW']}
g={d:k for k,v in G.items() for d in v}
m['g']=m['단'].map(g); r['g']=r['단'].map(g)
m84=m[m['면'].between(83,86)]; r84=r[r['면'].between(83,86)]
j=r[r['전월세구분']=='전세']; j84=j[j['면'].between(83,86)]
out={}
def yr(x): return {y:[float(z['금'].median()) if len(z) else None,int(len(z))] for y in ['2021','2022','2023','2024','2025','2026'] for z in [x[x['년']==y]]}
def jeon(x,xa,ra):
    n26=x[(x['년']=='2026')&(x['계약구분']=='신규')]; g26=x[(x['년']=='2026')&(x['계약구분']=='갱신')]
    a=xa[xa['년'].isin(['2024','2025'])]; b=xa[xa['년']=='2026']
    gg=xa[(xa['계약구분']=='갱신')].copy(); gg['전']=pd.to_numeric(gg['종전계약 보증금(만원)'].astype(str).str.replace(',',''),errors='coerce'); gg=gg[gg['전']>0]
    r25=ra[ra['년'].isin(['2025','2026'])]
    return {'new26':[float(n26['보'].median()) if len(n26) else None,int(len(n26))],'ren26':[float(g26['보'].median()) if len(g26) else None,int(len(g26))],
      'all2425':int(len(a)),'jf2425':int((a['월']<=2).sum()),'ren2425':int((a['계약구분']=='갱신').sum()),'new2425':int((a['계약구분']=='신규').sum()),
      'all26':int(len(b)),'jf26':int((b['월']<=2).sum()),'ren26n':int((b['계약구분']=='갱신').sum()),
      'up':[float((gg['보']/gg['전']-1).median()) if len(gg) else None,int(len(gg))],'wol':[int((r25['전월세구분']=='월세').sum()),int(len(r25))]}
for k in G:
    o={'m':yr(m84[m84.g==k]),'j84':jeon(j84[j84.g==k],j84[j84.g==k],r84[r84.g==k]),'jall':jeon(j[j.g==k],j[j.g==k],r[r.g==k])}
    # 2021에도 거래 있던 단지만(같은 단지)
    s=m84[m84.g==k]; keep=[d for d in G[k] if len(s[(s['단']==d)&(s['년']=='2021')])>0]; o['m_same']=yr(s[s['단'].isin(keep)]); o['same']=keep
    out[k]=o
for d in g:
    out[d]={'g':g[d],'build':str(m[m['단']==d]['건축년도'].iloc[0]) if len(m[m['단']==d]) else None,'m':yr(m84[m84['단']==d]),'j84':jeon(j84[j84['단']==d],j84[j84['단']==d],r84[r84['단']==d]),'jall':jeon(j[j['단']==d],j[j['단']==d],r[r['단']==d]),
     'max26':int(m84[(m84['단']==d)&(m84['년']=='2026')]['금'].max()) if len(m84[(m84['단']==d)&(m84['년']=='2026')]) else None}
out['_songdo_all']={'j84':jeon(j84,j84,r84),'jall':jeon(j,j,r)}
# 1공구 면적 구성: 2025~2026 매매 중 84 비중
for k in G:
    s=m[(m.g==k)&m['년'].isin(['2025','2026'])]; out[k]['area']={'all':int(len(s)),'u85':int((s['면']<=86).sum()),'84':int(s['면'].between(83,86).sum()),'o100':int((s['면']>100).sum())}
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
def pr(k):
    v=out[k]; print(k,v.get('build',''),{y:tuple(a) for y,a in v['m'].items()}); 
    for t in ('j84','jall'):
        x=v[t]; print('   ',t,'new26',x['new26'],'ren26',x['ren26'],'1~2월 24-25 %.1f%% (%d/%d)'%(x['jf2425']/max(x['all2425'],1)*100,x['jf2425'],x['all2425']),'26 %.1f%% (%d/%d)'%(x['jf26']/max(x['all26'],1)*100,x['jf26'],x['all26']),'갱신 24-25 %.1f%%'%(x['ren2425']/max(x['all2425'],1)*100),'갱신26 %.1f%%'%(x['ren26n']/max(x['all26'],1)*100),'up',x['up'],'월세 %.0f%%'%(x['wol'][0]/max(x['wol'][1],1)*100),x['wol'])
for k in list(G)+['_songdo_all']:
    if k in G: print('same',out[k]['same'],{y:tuple(a) for y,a in out[k]['m_same'].items()},out[k]['area'])
    if k in G: pr(k)
    else: print(k,out[k])
print('-----')
for d in g: pr(d); print('   max26',out[d]['max26'])
