import pandas as pd, json
R='/home/claude/rtn/'
m=pd.read_pickle(R+'MGJ_2021_2026.pkl')
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']
m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
m['년']=m['계약년월'].str[:4]; m['월']=m['계약년월'].str[4:].astype(int); m['단']=m['단지명'].str.replace(' ','')
m['동']=m['시군구'].str.split().str[-1]
r=pd.read_pickle(R+'RGJ_2024_2026.pkl')
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int); r['단']=r['단지명'].str.replace(' ','')
r['동']=r['시군구'].str.split().str[-1]
# 이름: (단지명 정확히, 동)
D={'제일풍경채엘리트파크':('봉선동제일풍경채엘리트파크','봉선동'),'봉선3차한국아델리움':('봉선3차한국아델리움','봉선동'),'포스코더샵':('포스코더샵','봉선동'),'금호2':('금호2','봉선동'),'봉선로광명메이루즈':('봉선로광명메이루즈','봉선동'),
 '힐스테이트리버파크':('힐스테이트리버파크','쌍암동'),'수완호반베르디움1차':('수완지구호반베르디움1차','신가동'),'효천시티프라디움':('효천시티프라디움','임암동'),'효천1중흥에코시티':('효천1중흥에스-클래스에코시티','임암동'),'상무엘리체':('상무엘리체','쌍촌동'),'상무양우내안애':('상무양우내안애','마륵동'),'해솔대방2차':('해솔마을대방노블랜드2차','수완동'),'우미린2차':('우미린2차','수완동'),'수완모아엘가':('모아엘가','수완동')}
def sel(df,k):
    n,d=D[k]; return df[(df['단']==n)&(df['동']==d)&(df['면']>=83)&(df['면']<=86)]
Y=['2021','2022','2023','2024','2025','2026']
def stat(x,y):
    o={}
    for yy in Y:
        z=x[x['년']==yy]; o[yy]={'n':int(len(z)),'med':float(z['금'].median()) if len(z) else None,'max':int(z['금'].max()) if len(z) else None}
    j=y[y['월세']==0]
    for t,c in [('jn','신규'),('jg','갱신')]:
        for yy in ['2025','2026']:
            z=j[(j['년']==yy)&(j['계약구분']==c)]; o[t+yy[2:]]={'n':int(len(z)),'med':float(z['보'].median()) if len(z) else None}
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425']={'all':int(len(jj)),'12':int(len(jj[jj['월']<=2])),'renew':int(len(jj[jj['계약구분']=='갱신']))}
    j26=j[j['년']=='2026']; o['j26']={'all':int(len(j26)),'12':int(len(j26[j26['월']<=2])),'renew':int(len(j26[j26['계약구분']=='갱신']))}
    ja=j[j['년'].isin(['2024','2025','2026'])]; o['j3']={'all':int(len(ja)),'12':int(len(ja[ja['월']<=2])),'renew':int(len(ja[ja['계약구분']=='갱신']))}
    y25=y[y['년'].isin(['2025','2026'])]; o['wol']={'all':int(len(y25)),'wol':int(len(y25[y25['월세']>0]))}
    return o
out={}
for k in D:
    x=sel(m,k); o=stat(x,sel(r,k)); o['build']=str(x['건축년도'].iloc[0]) if len(x) else None
    o['areas']=sorted(set(round(a,2) for a in x['면']))
    z=x[x['년'].isin(['2021','2022'])]; o['max2122']=[int(z['금'].max()),str(z.loc[z['금'].idxmax(),'계약년월'])] if len(z) else None
    z=x[x['년']=='2026']; o['m2026']={str(a):[float(b['median']),int(b['count'])] for a,b in z.groupby('계약년월')['금'].agg(['median','count']).iterrows()}
    out[k]=o
# 동네 묶음: 84㎡ 전체
G={'_봉선동':['봉선동'],'_수완':['수완동','신가동','장덕동'],'_첨단':['쌍암동','월계동','산월동'],'_효천':['임암동','행암동'],'_상무':['치평동','쌍촌동','마륵동']}
m84=m[(m['면']>=83)&(m['면']<=86)]; r84=r[(r['면']>=83)&(r['면']<=86)]
for g,ds in G.items():
    o=stat(m84[m84['동'].isin(ds)],r84[r84['동'].isin(ds)])
    # 같은 단지 2021·2026 둘 다 5건 넘는 단지의 변화율 중앙값
    x=m84[m84['동'].isin(ds)]; ch=[]
    for (d,n),z in x.groupby(['동','단']):
        a=z[z['년']=='2021']['금']; b=z[z['년']=='2026']['금']; c=z[z['년']=='2023']['금']
        if len(a)>=5 and len(b)>=5: ch.append((n,float(b.median()/a.median()-1),float(c.median()/a.median()-1) if len(c)>=3 else None,int(len(a)),int(len(b)),str(z['건축년도'].iloc[0])))
    o['pairs']=ch; o['pair_med']=float(pd.Series([c[1] for c in ch]).median()) if ch else None; o['pair_n']=len(ch); o['pair_up']=sum(1 for c in ch if c[1]>=0)
    out[g]=o
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items():
    print(k,v.get('build'),{y:(v[y]['med'],v[y]['n']) for y in Y},'max2122',v.get('max2122'),'jn26',v['jn26'],'jg26',v['jg26'],'jn25',v['jn25'],'j2425',v['j2425'],'j26',v['j26'],'wol',v['wol'])
    if k.startswith('_'): print('  pairs',v['pair_n'],v['pair_up'],v['pair_med'],sorted(v['pairs'],key=lambda c:-c[1])[:6],sorted(v['pairs'],key=lambda c:c[1])[:3])
    else: print('  ',v['areas'],v['m2026'])
print('max m date',m['계약년월'].max(),m[m['계약년월']=='202610']['계약일'].astype(int).max())
print(sorted(set(m[(m['동']=='봉선동')]['단'])))
