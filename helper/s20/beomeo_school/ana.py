import pandas as pd, json
R='/home/claude/rtn/'
m=pd.read_pickle(R+'MD_daegu_2021_2026.pkl')
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']; m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
m['년']=m['계약년월'].str[:4]; m['월']=m['계약년월'].str[4:].astype(int); m['단']=m['단지명'].str.replace(' ','')
m['구']=m['시군구'].str.split().str[1]; m['동']=m['시군구'].str.split().str[2]
r=pd.read_pickle(R+'RD_daegu_2024_2026.pkl')
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int); r['단']=r['단지명'].str.replace(' ','')
r['구']=r['시군구'].str.split().str[1]; r['동']=r['시군구'].str.split().str[2]
L=[('범어동','힐스테이트범어'),('범어동','빌리브범어'),('범어동','범어에스케이뷰'),('범어동','범어에일린의뜰'),('범어동','범어센트럴푸르지오'),('범어동','e편한세상범어'),('만촌동','만촌삼정그린코아에듀파크'),('만촌동','만촌자이르네'),('만촌동','만촌3차화성파크드림'),
 ('시지동','수성알파시티동화아이위시'),('사월동','시지3차서한이다음'),('범물동','수성하늘채르레브'),('지산동','더샵수성라크에르'),('중동','수성효성해링턴플레이스'),('황금동','힐스테이트황금동'),
 ('유천동','대구월배2차아이파크'),('월성동','월성삼정그린코아에듀파크'),('대천동','월배삼정그린코아포레스트'),('신암동','이안동대구'),('신암동','동대구이안센트럴D'),('신천동','동대구반도유보라')]
out={}
for d,k in L:
    x=m[(m['단']==k)&(m['동']==d)&(m['면']>=83)&(m['면']<=86)]; o={'구':x['구'].iloc[0],'동':d,'build':str(x['건축년도'].iloc[0]),'areas':sorted(set(x['면'].round(2)))[:6]}
    for y in ['2021','2022','2023','2024','2025','2026']:
        z=x[x['년']==y]; o[y]={'n':int(len(z)),'med':float(z['금'].median()) if len(z) else None,'max':int(z['금'].max()) if len(z) else None}
    z=x[x['년']=='2026']; o['m2026']={str(a):[float(b['median']),int(b['count'])] for a,b in z.groupby('계약년월')['금'].agg(['median','count']).iterrows()}
    y=r[(r['단']==k)&(r['동']==d)&(r['면']>=83)&(r['면']<=86)]; j=y[y['전월세구분']=='전세']
    for nm,q in [('jn26',(j['년']=='2026')&(j['계약구분']=='신규')),('jg26',(j['년']=='2026')&(j['계약구분']=='갱신')),('ja26',(j['년']=='2026'))]:
        z=j[q]; o[nm]={'n':int(len(z)),'med':float(z['보'].median()) if len(z) else None}
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425']=[int(len(jj)),int((jj['월']<=2).sum()),int((jj['계약구분']=='갱신').sum())]
    j26=j[j['년']=='2026']; o['j26']=[int(len(j26)),int((j26['월']<=2).sum()),int((j26['계약구분']=='갱신').sum())]
    y26=y[y['년']=='2026']; o['r26']=[int(len(y26)),int((y26['전월세구분']=='월세').sum())]
    out[k]=o
# 지역 묶음 (전 평형 아파트 전세)
ja=r[r['전월세구분']=='전세']
def ratio(df):
    a=df[df['년'].isin(['2024','2025'])]; b=df[df['년']=='2026']
    return {'all':int(len(a)),'12':int((a['월']<=2).sum()),'renew':int((a['계약구분']=='갱신').sum()),'26all':int(len(b)),'26_12':int((b['월']<=2).sum()),'26renew':int((b['계약구분']=='갱신').sum())}
out['_범어만촌']=ratio(ja[(ja['구']=='수성구')&ja['동'].isin(['범어동','만촌동'])])
out['_수성다른']=ratio(ja[(ja['구']=='수성구')&~ja['동'].isin(['범어동','만촌동'])])
out['_달서']=ratio(ja[ja['구']=='달서구']); out['_동구']=ratio(ja[ja['구']=='동구'])
# 월세 비율
for nm,q in [('_범어만촌',(r['구']=='수성구')&r['동'].isin(['범어동','만촌동'])),('_수성다른',(r['구']=='수성구')&~r['동'].isin(['범어동','만촌동'])),('_달서',r['구']=='달서구'),('_동구',r['구']=='동구')]:
    z=r[q&(r['년']=='2026')]; out[nm]['r26']=[int(len(z)),int((z['전월세구분']=='월세').sum())]
# 동별 84 전체 (2015년 이후 준공) 중앙값
x=m[(m['면']>=83)&(m['면']<=86)]
def grp(q):
    z=x[q]; return {y:[float(z[z['년']==y]['금'].median()),int((z['년']==y).sum())] for y in ['2021','2022','2023','2024','2025','2026']}
out['_g범어만촌84']=grp((x['구']=='수성구')&x['동'].isin(['범어동','만촌동']))
out['_g수성다른84']=grp((x['구']=='수성구')&~x['동'].isin(['범어동','만촌동']))
out['_g달서84']=grp(x['구']=='달서구'); out['_g동구84']=grp(x['구']=='동구')
# 거래량 전체
out['_cnt']={g:{y:int(((m['구']==g)&(m['년']==y)).sum()) for y in ['2021','2022','2023','2024','2025','2026']} for g in ['수성구','달서구','동구']}
out['_last']=str(m[m['계약년월']=='202610']['계약일'].astype(int).max())
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items():
    if k.startswith('_'): print(k,v); continue
    f=lambda a,b:(f"{(v[b]['med']/v[a]['med']-1)*100:+.1f}" if v[a]['med'] and v[b]['med'] else None)
    jn=v['jn26']['med']; 
    print(k,v['동'],v['build'],v['areas'],{y:(v[y]['med'],v[y]['n']) for y in ['2021','2023','2025','2026']},'21→23',f('2021','2023'),'23→26',f('2023','2026'),'21→26',f('2021','2026'),'| jn26',v['jn26'],'jg26',v['jg26'],'전세가율',round(jn/v['2026']['med']*100,1) if jn else None,'j2425',v['j2425'],'j26',v['j26'],'r26',v['r26'],'max26',v['2026']['max'])
