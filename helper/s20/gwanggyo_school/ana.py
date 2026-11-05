import pandas as pd, json, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
R='/home/claude/rtn/'
# 매매 2021~2026 (영통구)
ms=[load(R+f'rawG/MG{y}_41117.csv') for y in [2021,2022,2023,2024]]
ms+= [pd.read_pickle(R+'M2025.pkl'), pd.read_pickle(R+'M2026.pkl')]
m=pd.concat(ms,ignore_index=True)
m=m[m['시군구'].str.startswith('경기도 수원시 영통구')]
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']
m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
m['년']=m['계약년월'].str[:4]; m['월']=m['계약년월'].str[4:].astype(int)
m['단']=m['단지명'].str.replace(' ','')
# 전월세 2024~2026
rs=[load(R+f'rawG/RG{y}_41117.csv') for y in [2024,2025]]+[pd.read_pickle(R+'R2026.pkl')]
r=pd.concat(rs,ignore_index=True)
r=r[r['시군구'].str.startswith('경기도 수원시 영통구')]
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int)
r['단']=r['단지명'].str.replace(' ','')
D={'매탄위브하늘채':'매탄위브하늘채','힐스테이트영통':'힐스테이트영통','자연앤힐스테이트':'자연앤힐스테이트','광교2차e편한세상':'광교2차e편한세상','광교호반베르디움(이의)':'광교호반베르디움','광교센트럴뷰':'광교센트럴뷰','광교더리브':'광교더리브','광교더포레스트':'광교더포레스트','광교호수마을호반써밋':'광교호수마을호반써밋','광교해모로':'광교해모로아파트','광교한양수자인':'광교한양수자인','광교중흥에스클래스':'광교중흥에스클래스','광교더샵':'광교더샵','광교아이파크':'광교아이파크','광교에듀포레':'광교에듀포레'}
DONG={'매탄위브하늘채':'매탄동','힐스테이트영통':'망포동','자연앤힐스테이트':'이의동','광교2차e편한세상':'이의동','광교호반베르디움(이의)':'이의동','광교센트럴뷰':'이의동','광교더리브':'하동','광교더포레스트':'하동','광교호수마을호반써밋':'하동','광교해모로':'이의동','광교한양수자인':'이의동','광교중흥에스클래스':'원천동','광교더샵':'원천동','광교아이파크':'원천동','광교에듀포레':'이의동'}
def sel(df,k):
    x=df[(df['단']==D[k])&(df['시군구'].str.endswith(DONG[k]))&(df['면']>=83)&(df['면']<=86)]
    return x
out={}
for k in D:
    x=sel(m,k); o={}
    for y in ['2021','2022','2023','2024','2025','2026']:
        z=x[x['년']==y]; o[y]={'n':int(len(z)),'med':float(z['금'].median()) if len(z) else None,'max':int(z['금'].max()) if len(z) else None}
    # 2021~2022 월별 중앙값 고점
    z=x[x['년'].isin(['2021','2022'])]
    mm=z.groupby('계약년월')['금'].agg(['median','count'])
    mm=mm[mm['count']>=3]
    o['peak']={'ym':str(mm['median'].idxmax()),'med':float(mm['median'].max()),'n':int(mm.loc[mm['median'].idxmax(),'count'])} if len(mm) else None
    # 2026 월별
    z=x[x['년']=='2026']; o['m2026']={str(a):[float(b['median']),int(b['count'])] for a,b in z.groupby('계약년월')['금'].agg(['median','count']).iterrows()}
    o['build']=str(x['건축년도'].iloc[0]) if len(x) else None
    o['areas']=[float(x['면'].min()),float(x['면'].max())] if len(x) else None
    # 전세
    y=sel(r,k); j=y[(y['전월세구분']=='전세')]
    jn26=j[(j['년']=='2026')&(j['계약구분']=='신규')]; jg26=j[(j['년']=='2026')&(j['계약구분']=='갱신')]
    jn25=j[(j['년']=='2025')&(j['계약구분']=='신규')]
    o['jn26']={'n':int(len(jn26)),'med':float(jn26['보'].median()) if len(jn26) else None}
    o['jg26']={'n':int(len(jg26)),'med':float(jg26['보'].median()) if len(jg26) else None}
    o['jn25']={'n':int(len(jn25)),'med':float(jn25['보'].median()) if len(jn25) else None}
    j25=j[j['년']=='2025']; o['j25_all']=int(len(j25)); o['j25_12']=int(len(j25[j25['월']<=2]))
    j24=j[j['년']=='2024']; o['j24_all']=int(len(j24)); o['j24_12']=int(len(j24[j24['월']<=2]))
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425_all']=int(len(jj)); o['j2425_12']=int(len(jj[jj['월']<=2]))
    j26=j[j['년']=='2026']; o['j26_all']=int(len(j26)); o['j26_12']=int(len(j26[j26['월']<=2]))
    o['j2425_renew']=int(len(jj[jj['계약구분']=='갱신'])); o['j2425_new']=int(len(jj[jj['계약구분']=='신규']))
    # 월세 비율 2025
    y25=y[y['년']=='2025']; o['r25_all']=int(len(y25)); o['r25_wol']=int(len(y25[y25['전월세구분']=='월세']))
    # 갱신 인상률 2025~2026 (전세→전세, 종전 보증금 있는 것)
    g=j[(j['년'].isin(['2025','2026']))&(j['계약구분']=='갱신')].copy()
    g['전']=g['종전계약 보증금(만원)'].astype(str).str.replace(',','')
    g=g[g['전'].str.isdigit()]; g['전']=g['전'].astype(int); g=g[g['전']>0]
    g['증']=g['보']/g['전']-1
    o['renew_up']={'n':int(len(g)),'med':float(g['증'].median()) if len(g) else None}
    out[k]=o
# 광교 전체 (이의동 · 하동 · 원천동 2011~2014 준공 단지) 전세 1~2월 비율 · 영통구 전체
def ratio(df):
    a=df[df['년'].isin(['2024','2025'])]; b=df[df['년']=='2026']; return {'all':int(len(a)),'12':int(len(a[a['월']<=2])),'renew':int(len(a[a['계약구분']=='갱신'])),'26all':int(len(b)),'26_12':int(len(b[b['월']<=2]))}
jall=r[r['전월세구분']=='전세']
out['_yt']=ratio(jall)
gk=jall[jall['시군구'].str.contains('이의동|하동|원천동')]
out['_gwanggyo']=ratio(gk)
out['_yt_other']=ratio(jall[~jall['시군구'].str.contains('이의동|하동|원천동')])
# 영통구 다른 동(영통동 · 망포동) 2011~2014 준공 84 매매 비교: 짝 후보
o2=m[(m['면']>=83)&(m['면']<=86)&(m['시군구'].str.contains('영통동|망포동'))&(m['건축년도'].astype(int).between(2009,2015))]
out['_yt_pair']={}
for (d,n),z in o2.groupby([m['시군구'].str.split().str[-1],'단']):
    if len(z)<60: continue
    oo={}
    for y in ['2021','2023','2025','2026']:
        zz=z[z['년']==y]; oo[y]=[float(zz['금'].median()) if len(zz) else None,int(len(zz))]
    oo['build']=str(z['건축년도'].iloc[0]); out['_yt_pair'][d+' '+n]=oo
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items():
    if k.startswith('_'): print(k,v); continue
    print(k,v['build'],{y:(v[y]['med'],v[y]['n']) for y in ['2021','2022','2023','2024','2025','2026']},'peak',v['peak'],'jn26',v['jn26'],'jg26',v['jg26'],'12월비율',v['j2425_12'],'/',v['j2425_all'],'갱신',v['j2425_renew'],'인상',v['renew_up'])
