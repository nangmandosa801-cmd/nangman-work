import sys,io; sys.path.insert(0,'/home/claude/watch')
import pandas as pd, rt_fetch
pd.set_option('display.width',220)
f='/home/claude/watch/rt/bun_41000_2025-10_2026-10.csv'
t=open(f,encoding='cp949',errors='ignore').read().splitlines()
h=[i for i,l in enumerate(t) if '단지명' in l][0]
b=pd.read_csv(io.StringIO('\n'.join(t[h:])))
b=b[b['단지명'].str.contains('센트라인',na=False)&b['시군구'].str.contains('의왕',na=False)].copy()
b=b[b['해제사유발생일'].astype(str).str.strip()=='-']
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(int); b['ym']=b['계약년월'].astype(int); b['층']=b['층'].astype(int)
TY={37.81:'37A',37.91:'37B',59.88:'59A',59.52:'59B',84.43:'84A',84.63:'84B',98.06:'98'}
b['ty']=b['전용면적(㎡)'].round(2).map(TY)
P={'37A':[(9,9,37600),(10,15,38400),(16,25,38700),(26,99,39100)],'37B':[(10,15,39100),(16,25,39500),(26,99,39900)],
 '59B':[(1,1,62500),(2,2,63100),(3,3,63800),(4,4,65100),(5,9,65800),(10,15,67200),(16,25,67800),(26,99,68500)],
 '84A':[(1,1,85400),(2,2,86300),(3,3,87200),(4,4,89100),(5,9,90000),(10,15,91800),(16,25,92700),(26,99,93700)],
 '84B':[(1,1,85200),(2,2,86100),(3,3,87000),(4,4,88800),(5,9,89800),(10,15,91600),(16,19,92500)],
 '98':[(3,3,100600),(4,4,102700),(5,9,103800),(10,15,105900),(16,24,106900)]}
def bp(ty,fl):
  for a,c,v in P.get(ty,[]):
    if a<=fl<=c: return v
b['bp']=[bp(a,c) for a,c in zip(b['ty'],b['층'])]; b['d']=b['p']-b['bp']
r=b[(b['ym']>=202604)&(b['분/입주권']=='분양권')]
print('분양권 4~10월(10/1까지)', len(r))
print(r.groupby('ty').agg(n=('p','count'),med=('p','median'),mn=('p','min'),mx=('p','max'),dmed=('d','median'),dmin=('d','min'),dmax=('d','max'),flmin=('층','min'),flmax=('층','max')))
r7=b[(b['ym']>=202607)&(b['분/입주권']=='분양권')]
print('7~10월'); print(r7.groupby('ty').agg(n=('p','count'),med=('p','median'),dmed=('d','median'),flmin=('층','min'),flmax=('층','max')))
print(r[r.ty=='84A'].sort_values('d')[['ym','계약일','층','p','bp','d','거래유형']].to_string())
print(r[r.ty=='59B'].sort_values('d')[['ym','계약일','층','p','bp','d']].to_string())
print('입주권',b[b['분/입주권']=='입주권'][['ym','층','ty','p']].to_string())
print('max date', b['ym'].max(), b[b.ym==b.ym.max()]['계약일'].max())
# neighbors
d=rt_fetch.load(sidos=['41000'])
d=d[d['해제사유발생일'].astype(str).str.strip().isin(['-','','nan'])] if '해제사유발생일' in d else d
x=d[d['시군구'].str.contains('의왕',na=False)].copy(); x['면']=x['전용면적(㎡)'].astype(float)
print('sale ym',x['ym'].min(),x['ym'].max(), x[x.ym==x.ym.max()]['계약일'].max())
for nm in ['의왕더샵캐슬','의왕서해그랑블','의왕역푸르지오라포레','한진해모로','대명솔채','의왕백운 해링턴 플레이스 1단지']:
  y=x[x['단지명'].str.contains(nm,regex=False)]
  for lo,hi,lab in [(58,61,'59'),(82,86,'84')]:
    z=y[(y['면']>=lo)&(y['면']<=hi)]
    if len(z): print(nm,lab,len(z),int(z['p'].median()),sorted(z['층'].astype(int).tolist()),z['건축년도'].iloc[0], sorted(z['p'].tolist()))
# 만원 정밀
for nm in ['의왕더샵캐슬','의왕서해그랑블','의왕역푸르지오라포레']:
  y=x[x['단지명'].str.contains(nm,regex=False)&(x['면']>=82)&(x['면']<=86)]
  print(nm,'84 만원 med',y['거래금액(만원)'].astype(str).str.replace(',','').astype(int).median(), y['ym'].min(),y['ym'].max())
# rent
import glob
rs=[]
for ym in ['202607','202608','202609','202610']:
  fn=f'/home/claude/watch/rt/rent_41000_{ym}.csv'
  try:
    tt=open(fn,encoding='cp949',errors='ignore').read().splitlines()
    hh=[i for i,l in enumerate(tt) if '단지명' in l][0]
    rs.append(pd.read_csv(io.StringIO('\n'.join(tt[hh:]))))
  except Exception as e: print('no',fn)
R=pd.concat(rs); R=R[R['시군구'].str.contains('의왕',na=False)]
print(R.columns.tolist())
R=R[R['전월세구분'].astype(str).str.contains('전세')]
R['bo']=R['보증금(만원)'].astype(str).str.replace(',','').astype(int); R['면']=R['전용면적(㎡)'].astype(float)
for nm in ['센트라인','의왕더샵캐슬','의왕서해그랑블','의왕역푸르지오라포레']:
  for lo,hi,lab in [(37,38,'37'),(58,61,'59'),(82,86,'84')]:
    z=R[R['단지명'].str.contains(nm,regex=False)&(R['면']>=lo)&(R['면']<=hi)]
    if len(z): print('전세',nm,lab,len(z),z['bo'].median(),z['계약년월'].min(),z['계약년월'].max(),sorted(z['bo'].tolist()))
print('rent max', R['계약년월'].max())
