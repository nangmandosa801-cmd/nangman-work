import pandas as pd
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
a=pd.read_pickle('/home/claude/rtn/M2025.pkl'); a=a[a['시군구'].str.contains('경기도 하남시')]
b=pd.read_pickle('/tmp/fresh/M_hanam26.pkl'); b=b[b['시군구'].str.contains('경기도 하남시')]
m=pd.concat([a,b]); m=m[m['해제사유발생일'].astype(str).str.strip().isin(['-',''])]
m=m[m['거래유형']!='직거래']
m['p']=num(m['거래금액(만원)']); m['a']=num(m['전용면적(㎡)']); m['ym']=m['계약년월'].astype(int); m['y']=m.ym//100
m.to_pickle('m2.pkl')
mm=m[m.ym%100<=10]
N=['미사강변스타힐스아파트','미사강변푸르지오','미사강변 센텀팰리스','미사강변 하우스디 더 레이크','미사강변 파크뷰','미사강변트래지안','미사강변루나리움','미사강변파밀리에','미사강변한신휴플러스']
for n in N:
  x=mm[mm['단지명']==n].copy(); x['a1']=x.a.round(0)
  t=x.groupby(['a1','y']).agg(n=('p','size'),med=('p','median')).unstack()
  t['up%']=((t[('med',2026)]/t[('med',2025)]-1)*100).round(1)
  print('##',n); print(t.to_string())
x=m[(m['단지명']=='미사강변스타힐스아파트')].copy(); x['a1']=x.a.round(0)
print(x[x.ym>=202607].sort_values(['ym','계약일'])[['ym','계약일','a1','p','층']].to_string())
