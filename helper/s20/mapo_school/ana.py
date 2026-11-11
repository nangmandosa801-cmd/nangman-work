import pandas as pd, json, sys
sys.path.insert(0,'/home/claude/rtn')
from load import load
R='/home/claude/rtn/'
m=pd.concat([pd.read_pickle(R+'M2021_2024_seoul.pkl'),pd.read_pickle(R+'M2025.pkl'),pd.read_pickle(R+'M2026.pkl')],ignore_index=True)
m=m[m['시군구'].str.startswith('서울특별시 마포구')]
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']; m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
m['년']=m['계약년월'].str[:4]; m['월']=m['계약년월'].str[4:].astype(int); m['단']=m['단지명'].str.replace(' ',''); m['동']=m['시군구'].str.split().str[-1]
m=m[(m['면']>=83)&(m['면']<=86)]
r=pd.concat([load(R+'rawS/R2024_11440.csv'),load(R+'rawS/R2025_11440.csv'),pd.read_pickle(R+'R2026.pkl')],ignore_index=True)
r=r[r['시군구'].str.startswith('서울특별시 마포구')]
r['면']=r['전용면적(㎡)'].astype(float); r['보']=r['보증금(만원)'].str.replace(',','').astype(int); r['월세']=r['월세금(만원)'].astype(str).str.replace(',','').astype(int)
r['년']=r['계약년월'].str[:4]; r['월']=r['계약년월'].str[4:].astype(int); r['단']=r['단지명'].str.replace(' ',''); r['동']=r['시군구'].str.split().str[-1]
r84=r[(r['면']>=83)&(r['면']<=86)]
A=['염리동','대흥동','용강동']
def med(z): return float(z['금'].median()) if len(z) else None
def one(dong,dan):
    x=m[(m['동']==dong)&(m['단']==dan)]; o={'build':str(x['건축년도'].iloc[0]) if len(x) else None}
    for y in ['2021','2022','2023','2024','2025','2026']:
        z=x[x['년']==y]; o[y]=[med(z),int(len(z))]
    z=x[(x['계약년월']>='202507')]; o['2507_2610']=[med(z),int(len(z))]
    z=x[x['년']=='2026']; o['max26']=int(z['금'].max()) if len(z) else None
    y=r84[(r84['동']==dong)&(r84['단']==dan)]; j=y[y['전월세구분']=='전세']
    for tag,yy in [('26',['2026']),('25',['2025']),('2526',['2025','2026'])]:
        a=j[j['년'].isin(yy)&(j['계약구분']=='신규')]; b=j[j['년'].isin(yy)&(j['계약구분']=='갱신')]
        o['jn'+tag]=[float(a['보'].median()) if len(a) else None,int(len(a))]; o['jg'+tag]=[float(b['보'].median()) if len(b) else None,int(len(b))]
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425']=[int(len(jj)),int((jj['월']<=2).sum()),int((jj['계약구분']=='갱신').sum())]
    j26=j[j['년']=='2026']; o['j26']=[int(len(j26)),int((j26['월']<=2).sum()),int((j26['계약구분']=='갱신').sum())]
    y25=y[y['년'].isin(['2025','2026'])]; o['wol2526']=[int(len(y25)),int((y25['전월세구분']=='월세').sum())]
    return o
L=[('염리동','마포프레스티지자이'),('염리동','마포자이더센트리지(102동~112동)'),('염리동','마포자이'),('염리동','염리삼성래미안'),('대흥동','마포그랑자이'),('대흥동','마포자이2차'),('대흥동','대흥동태영아파트'),('용강동','래미안마포리버웰'),('용강동','마포용강삼성래미안'),('용강동','이편한세상마포리버파크'),
   ('아현동','마포래미안푸르지오1단지'),('아현동','마포래미안푸르지오2단지'),('아현동','마포래미안푸르지오3단지'),('아현동','마포래미안푸르지오4단지'),('아현동','더클래시'),('아현동','공덕자이'),('아현동','마포센트럴아이파크'),('공덕동','공덕파크자이'),('공덕동','공덕1삼성래미안'),('공덕동','공덕2삼성래미안'),('공덕동','래미안공덕5차'),('공덕동','공덕SK리더스뷰'),('신수동','마포아이파크포레'),('신공덕동','신공덕1차삼성래미안1아파트'),('상암동','상암월드컵파크4단지'),('상암동','상암월드컵파크7단지'),('상암동','상암월드컵파크3단지'),('성산동','성산월드타운대림'),('현석동','래미안웰스트림'),('상수동','래미안밤섬리베뉴Ⅱ')]
out={d+' '+n:one(d,n) for d,n in L}
# 마포래미안푸르지오 1~4 합침
x=m[(m['동']=='아현동')&(m['단'].str.startswith('마포래미안푸르지오'))]; o={}
for y in ['2021','2023','2025','2026']: z=x[x['년']==y]; o[y]=[med(z),int(len(z))]
y=r84[(r84['동']=='아현동')&(r84['단'].str.startswith('마포래미안푸르지오'))]; j=y[y['전월세구분']=='전세']
a=j[(j['년']=='2026')&(j['계약구분']=='신규')]; b=j[(j['년']=='2026')&(j['계약구분']=='갱신')]
o['jn26']=[float(a['보'].median()),len(a)]; o['jg26']=[float(b['보'].median()),len(b)]
jj=j[j['년'].isin(['2024','2025'])]; o['j2425']=[int(len(jj)),int((jj['월']<=2).sum()),int((jj['계약구분']=='갱신').sum())]
j26=j[j['년']=='2026']; o['j26']=[int(len(j26)),int((j26['월']<=2).sum()),int((j26['계약구분']=='갱신').sum())]
out['_mrp']=o
# 묶음: 2021년에 거래가 있던 단지만(2020년까지 준공), 동 묶음
def grp(name,dongs):
    x=m[m['동'].isin(dongs)&(m['건축년도'].astype(int)<=2020)]; o={}
    for y in ['2021','2022','2023','2024','2025','2026']: z=x[x['년']==y]; o[y]=[med(z),int(len(z))]
    xa=m[m['동'].isin(dongs)]
    for y in ['2021','2025','2026']: z=xa[xa['년']==y]; o['all'+y]=[med(z),int(len(z))]
    j=r[r['동'].isin(dongs)&(r['전월세구분']=='전세')]   # 모든 평형 전세
    jj=j[j['년'].isin(['2024','2025'])]; o['j2425']=[int(len(jj)),int((jj['월']<=2).sum()),int((jj['계약구분']=='갱신').sum())]
    j26=j[j['년']=='2026']; o['j26']=[int(len(j26)),int((j26['월']<=2).sum()),int((j26['계약구분']=='갱신').sum())]
    j8=r84[r84['동'].isin(dongs)&(r84['전월세구분']=='전세')]
    a=j8[(j8['년']=='2026')&(j8['계약구분']=='신규')]; b=j8[(j8['년']=='2026')&(j8['계약구분']=='갱신')]
    o['jn26']=[float(a['보'].median()),len(a)]; o['jg26']=[float(b['보'].median()),len(b)]
    a=j8[(j8['년']=='2026')&(j8['계약구분']=='신규')&(j8['건축년도'].astype(int)<=2020)]; o['jn26_old']=[float(a['보'].median()),len(a)]
    y=r[r['동'].isin(dongs)&r['년'].isin(['2025','2026'])]; o['wol2526']=[int(len(y)),int((y['전월세구분']=='월세').sum())]
    g=j[(j['년'].isin(['2025','2026']))&(j['계약구분']=='갱신')].copy(); g['전']=g['종전계약 보증금(만원)'].astype(str).str.replace(',',''); g=g[g['전'].str.isdigit()]; g['전']=g['전'].astype(int); g=g[g['전']>0]
    o['renew_up']=[float((g['보']/g['전']-1).median()),len(g)]
    out[name]=o
grp('_A',A); grp('_gongdeok',['공덕동','신공덕동']); grp('_ahyeon',['아현동']); grp('_sangam',['상암동']); grp('_seongsan',['성산동','중동']); grp('_etc',[d for d in m['동'].unique() if d not in A]); grp('_mapo',list(m['동'].unique()))
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items(): print(k,v)
