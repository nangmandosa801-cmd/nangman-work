import pandas as pd, json
pd.set_option('display.width',250)
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m=pd.read_pickle('/home/claude/rtn/M_hanam_2014_2026.pkl')
m=m[m.ym<=202610]
MISA=['망월동','풍산동','선동']; GAM=['감일동','감이동']
x=m[m.a.between(83,86)]
x['area']=x.dong.map(lambda d:'미사' if d in MISA else('감일' if d in GAM else '기타'))
cur=x[x.y==2026]; prev=x[(x.y==2025)&(x.ym%100<=10)]
print('== 지역 84 중앙값 2026 / 2025(1~10)')
for a in ['미사','감일']:
    print(a, cur[cur.area==a].p.agg(['median','size']).to_dict(), prev[prev.area==a].p.agg(['median','size']).to_dict())
print('== 12억 안팎(11.5~12.5억) 2026')
b=cur[cur.p.between(115000,125000)]
print(b.groupby('area').agg(n=('p','size'),cx=('단지명','nunique')))
print(b[b.area=='미사'].groupby(['단지명','건축년도']).p.size().sort_values(ascending=False).head(8))
print(b[b.area=='감일'][['단지명','건축년도','ym','계약일','층','p']].sort_values('ym').to_string())
print('== 감일 단지별 2026 중앙값·최저')
print(cur[cur.area=='감일'].groupby(['단지명','건축년도']).p.agg(['size','median','min']).to_string())
print('== 두 단지')
for n in ['미사강변 센텀팰리스','감일센트레빌']:
    c=cur[cur['단지명']==n]; p=prev[prev['단지명']==n]
    print(n,'2026',c.p.agg(['size','median','min','max']).to_dict(),'2025(1-10)',p.p.agg(['size','median']).to_dict(), 'up%',round((c.p.median()/p.p.median()-1)*100,1))
    print(c[['ym','계약일','층','p']].sort_values(['ym','계약일']).to_string())
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); r=r[r['시군구'].str.contains('경기도 하남시')].copy()
r['dep']=num(r['보증금(만원)']); r['mo']=num(r['월세금(만원)']); r['a']=num(r['전용면적(㎡)']); r['ym']=r['계약년월'].astype(int); r['dong']=r['시군구'].str.split().str[-1]
j=r[(r.mo==0)&r.a.between(83,86)&(r['전월세구분']=='전세')&(r.ym<=202610)]
j['area']=j.dong.map(lambda d:'미사' if d in MISA else('감일' if d in GAM else '기타'))
print('== 신규 전세 84 2026 1~10')
print(j[j['계약구분']=='신규'].groupby('area').dep.agg(['median','size']))
for n in ['미사강변 센텀팰리스','감일센트레빌']:
    t=j[j['단지명']==n]; print(n, t.groupby('계약구분').dep.agg(['median','size','min','max']).to_dict('index'))
