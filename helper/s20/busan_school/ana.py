import pandas as pd, json
R='/home/claude/rtn/'
m=pd.read_pickle(R+'MB_busan_2021_2026.pkl'); r=pd.read_pickle(R+'RB_busan_2024_2026.pkl')
m=m[(m['면']>=83)&(m['면']<=86)]; r84=r[(r['면']>=83)&(r['면']<=86)]
m['준']=m['건축년도'].astype(int); r84=r84.copy(); r84['준']=pd.to_numeric(r84['건축년도'],errors='coerce')
# 묶음: (동, 단지 목록 또는 None=준공 범위)
G={
 '사직롯데캐슬더클래식':('사직동',['사직롯데캐슬더클래식'],None),
 '쌍용더플래티넘사직아시아드':('사직동',['쌍용더플래티넘사직아시아드아파트','쌍용더플래티넘사직아시아드'],None),
 '사직쌍용예가':('사직동',['사직쌍용예가'],None),
 '사직역삼정그린코아더베스트1차':('사직동',['사직역삼정그린코아더베스트1차'],None),
 '좌동신시가지':('좌동',None,(1996,1999)),
 '건영2':('좌동',['건영2'],None),
 '엘지':('좌동',['엘지'],None),
 '벽산1':('좌동',['벽산1'],None),
 '대우마리나1·2':('우동',['대우마리나1','대우마리나2'],None),
 '마린시티자이':('우동',['마린시티자이'],None),
 '해운대자이2차1단지':('우동',['해운대자이2차1단지'],None),
 '해운대자이1단지':('우동',['해운대자이1단지'],None),
 '더샵센텀파크1차':('재송동',['더샵센텀파크1차'],None),
 '더샵센텀파크2차':('재송동',['더샵센텀파크2차'],None),
 '대우트럼프월드센텀':('우동',['대우트럼프월드센텀'],None),
 '센텀이편한세상':('재송동',['센텀이편한세상'],None),
}
def sel(df,k):
    d,names,rng=G[k]; x=df[df['동']==d]
    if names: x=x[x['단'].isin(names)]
    else: x=x[(x['준']>=rng[0])&(x['준']<=rng[1])]
    return x
def med(s): return float(s.median()) if len(s) else None
out={}
Y=['2021','2022','2023','2024','2025','2026']
for k in G:
    x=sel(m,k); o={'names':sorted(x['단'].unique().tolist())[:40],'build':sorted(x['건축년도'].unique().tolist())}
    for y in Y:
        z=x[x['년']==y]; o[y]={'n':int(len(z)),'med':med(z['금']),'max':int(z['금'].max()) if len(z) else None}
    y_=sel(r84,k); j=y_[y_['월세']==0]
    for y in ['2024','2025','2026']:
        jj=j[j['년']==y]; o['j'+y]={'all':int(len(jj)),'m12':int((jj['월']<=2).sum()),'new':int((jj['계약구분']=='신규').sum()),'renew':int((jj['계약구분']=='갱신').sum()),'new_med':med(jj[jj['계약구분']=='신규']['보']),'renew_med':med(jj[jj['계약구분']=='갱신']['보']),'med':med(jj['보'])}
        aa=y_[y_['년']==y]; o['w'+y]={'all':int(len(aa)),'wol':int((aa['월세']>0).sum())}
    out[k]=o
# 동 전체 전세(모든 넓이) 1~2월 · 갱신
def ratio(df):
    j=df[df['월세']==0]; a=j[j['년'].isin(['2024','2025'])]; b=j[j['년']=='2026']
    return {'all':int(len(a)),'m12':int((a['월']<=2).sum()),'renew':int((a['계약구분']=='갱신').sum()),'26all':int(len(b)),'26_12':int((b['월']<=2).sum()),'26renew':int((b['계약구분']=='갱신').sum())}
out['_사직동']=ratio(r[r['동']=='사직동']); out['_좌동']=ratio(r[r['동']=='좌동']); out['_우동']=ratio(r[r['동']=='우동']); out['_재송동']=ratio(r[r['동']=='재송동'])
out['_동래구']=ratio(r[r['시군구'].str.contains('동래구')]); out['_해운대구']=ratio(r[r['시군구'].str.contains('해운대구')])
out['_동래구_사직밖']=ratio(r[r['시군구'].str.contains('동래구')&(r['동']!='사직동')]); out['_해운대구_좌동밖']=ratio(r[r['시군구'].str.contains('해운대구')&(r['동']!='좌동')])
# 동 84 전체 중앙값
for d in ['사직동','좌동','우동','재송동']:
    x=m[m['동']==d]; out['_m_'+d]={y:{'n':int((x['년']==y).sum()),'med':med(x[x['년']==y]['금'])} for y in Y}
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items():
    if k.startswith('_'): print(k,v); continue
    print('\n',k,v['build'],len(v['names']))
    print('  매매',{y:(v[y]['med'],v[y]['n']) for y in Y},'max26',v['2026']['max'])
    for y in ['2024','2025','2026']: print('  전세',y,v['j'+y],v['w'+y])
