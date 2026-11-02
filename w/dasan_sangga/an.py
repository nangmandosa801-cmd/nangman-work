import pandas as pd,io
pd.set_option('display.width',220)
def L(f):
    t=open(f,encoding='cp949',errors='ignore').read().splitlines()
    h=[i for i,l in enumerate(t) if l.startswith('"NO"')][0]
    d=pd.read_csv(io.StringIO('\n'.join(t[h:])))
    d=d[d['해제사유발생일'].astype(str).str.strip()=='-'].copy()
    d['p']=d['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
    d['a']=pd.to_numeric(d['전용/연면적(㎡)'].astype(str).str.replace(',',''),errors='coerce')
    d['층']=pd.to_numeric(d['층'],errors='coerce'); d['py']=d.p/d.a*3.3058
    return d
R='/home/claude/watch/rt/'
A=L(R+'biz_41000_2025-10_2026-10.csv'); Bp=L(R+'biz_41000_2024-10_2025-10.csv')
def sel(d,dong): return d[d['시군구'].str.contains(dong)&(d['유형']=='집합')]
for nm,d in [('최근1년',A),('그전1년',Bp)]:
    for dong in ['남양주시 다산동','남양주시 별내동','구리시 갈매동']:
        x=sel(d,dong); x=x.assign(fl=pd.cut(x['층'],[-5,0,1,2,99],labels=['지하','1층','2층','3층+']))
        print(nm,dong,len(x)); print(x.groupby('fl',observed=True).agg(n=('p','count'),pmed=('p','median'),amed=('a','median'),py=('py','median')).round(0))
x=A[A['시군구'].str.contains('다산동')&(A['지번'].astype(str)=='668-3')]
print('668-3',len(x),x['계약년월'].value_counts().to_dict(),x['매수'].value_counts().to_dict(),x['거래유형'].value_counts().to_dict(),x['건축물주용도'].value_counts().to_dict(),x['층'].describe().round(0).to_dict())
print(A[A['시군구'].str.contains('다산동')&(A['유형']=='집합')]['계약년월'].max(), A['계약일'].max())
print('---')
for nm,d in [('최근1년',A),('그전1년',Bp)]:
    x=sel(d,'남양주시 다산동'); vc=x.groupby('지번').size().sort_values(ascending=False)
    print(nm,'지번 top',vc.head(6).to_dict())
    big=vc[vc>=10].index; y=x[~x['지번'].isin(big)]
    y=y.assign(fl=pd.cut(y['층'],[-5,0,1,2,99],labels=['지하','1층','2층','3층+']))
    print(nm,'한 건물 10건 넘는 곳 뺌',len(y)); print(y.groupby('fl',observed=True).agg(n=('p','count'),pmed=('p','median'),amed=('a','median'),py=('py','median'),pyq1=('py',lambda s:s.quantile(.25)),pyq3=('py',lambda s:s.quantile(.75))).round(0))
    print(y['용도지역'].value_counts().to_dict(), y['건축년도'].median())
    z=y[y['층']==1]; print(z[['지번','a','p','py','건축년도','계약년월','용도지역']].sort_values('py').to_string())
