import pandas as pd, json, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
R='/home/claude/rtn/'
m=pd.concat([pd.read_pickle(R+f) for f in ['M2021_2024_seoul.pkl','M2025.pkl','M2026.pkl']],ignore_index=True)
m=m[m['시군구'].str.startswith('서울특별시 광진구')]
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']
m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].astype(str).str.replace(',','').astype(int)
m['년']=m['계약년월'].astype(str).str[:4]; m['동']=m['시군구'].str.split().str[-1]; m['단']=m['단지명'].str.replace(' ','')
r=pd.concat([load(R+'rawK/RK2024_11215.csv'),load(R+'rawK/RK2025_11215.csv'),pd.read_pickle(R+'R2026.pkl')],ignore_index=True)
r=r[r['시군구'].str.startswith('서울특별시 광진구')]
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].astype(str).str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['년']=r['계약년월'].astype(str).str[:4]; r['월']=r['계약년월'].astype(str).str[4:].astype(int); r['동']=r['시군구'].str.split().str[-1]; r['단']=r['단지명'].str.replace(' ','')
m84=m[(m['면']>=83)&(m['면']<=86)]; r84=r[(r['면']>=83)&(r['면']<=86)]
out={}
for (d,n),x in m84.groupby(['동','단']):
    if len(x)<20: continue
    o={'build':int(x['건축년도'].iloc[0]),'n':int(len(x)),'areas':sorted(set(round(a,2) for a in x['면']))}
    for y in ['2021','2022','2023','2024','2025','2026']:
        z=x[x['년']==y]; o[y]=[float(z['금'].median()) if len(z) else None,int(len(z)),int(z['금'].max()) if len(z) else None]
    y=r84[(r84['동']==d)&(r84['단']==n)]; j=y[y['전월세구분']=='전세']
    for yy in ['2025','2026']:
        a=j[(j['년']==yy)&(j['계약구분']=='신규')]; b=j[(j['년']==yy)&(j['계약구분']=='갱신')]
        o['jn'+yy]=[float(a['보'].median()) if len(a) else None,int(len(a))]; o['jg'+yy]=[float(b['보'].median()) if len(b) else None,int(len(b))]
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425']=[int(len(jj)),int(len(jj[jj['월']<=2])),int(len(jj[jj['계약구분']=='갱신']))]
    y25=y[y['년'].isin(['2025','2026'])]; o['wol']=[int(len(y25)),int(len(y25[y25['전월세구분']=='월세']))]
    out[d+' '+n]=o
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
def e(v): return '-' if v is None else f'{v/10000:.2f}'
for k,v in sorted(out.items(),key=lambda t:(t[0].split()[0],t[1]['build'])):
    ra=(v['jn2026'][0]/v['2026'][0]*100) if v['jn2026'][0] and v['2026'][0] else None
    up=(v['2026'][0]/v['2021'][0]-1)*100 if v['2026'][0] and v['2021'][0] else None
    print(k,v['build'],' '.join(f"{e(v[y][0])}({v[y][1]})" for y in ['2021','2022','2023','2024','2025','2026']),'| jn26',e(v['jn2026'][0]),v['jn2026'][1],'jg26',e(v['jg2026'][0]),v['jg2026'][1],'jn25',e(v['jn2025'][0]),v['jn2025'][1],'| 율',f'{ra:.0f}' if ra else '-','| 21대비',f'{up:+.1f}' if up is not None else '-',v['areas'][:4])
