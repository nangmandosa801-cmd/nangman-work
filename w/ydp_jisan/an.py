import pandas as pd,io
rows=[]
for f in ['/home/claude/watch/rt/fac_11000_2024-10_2025-10.csv','/home/claude/watch/rt/fac_11000_2025-10_2026-10.csv']:
    t=open(f,encoding='cp949',errors='ignore').read().splitlines()
    print([l for l in t[:14] if '기간' in l or ':' in l][:6])
    h=[i for i,l in enumerate(t) if 'NO' in l and '시군구' in l][0]
    rows.append(pd.read_csv(io.StringIO('\n'.join(t[h:]))))
d=pd.concat(rows).drop_duplicates(subset=['시군구','지번','전용/연면적(㎡)','거래금액(만원)','층','계약년월','계약일'])
d=d[d['시군구'].str.contains('영등포')&(d['유형']=='집합')]
d=d[d['해제사유발생일'].astype(str).str.strip()=='-']
d['p']=d['거래금액(만원)'].astype(str).str.replace(',','').astype(int)
d['a']=d['전용/연면적(㎡)'].astype(float); d['py']=d.p/(d.a/3.3058)
d['dong']=d['시군구'].str.split().str[-1].str.replace(r'\d+가','',regex=True)
d['ym']=d['계약년월'].astype(int); d['y']=d['건축년도']
print('n',len(d), d.ym.min(), d.ym.max(), d[d.ym==d.ym.max()]['계약일'].max())
print(d['건축물주용도'].value_counts().to_dict(), d['용도지역'].value_counts().to_dict())
print(d.groupby('dong').agg(n=('p','size'),py=('py','median'),area=('a','median'),yr=('y','median')).sort_values('n',ascending=False).round(0))
d['age']=pd.cut(d.y,[0,2009,2019,2030],labels=['2009년 이전','2010~2019년','2020년 이후'])
print(d.groupby('age').agg(n=('p','size'),py=('py','median'),p=('p','median'),a=('a','median')).round(0))
d['half']=(d.ym>=202510).map({True:'B 2025.10~',False:'A ~2025.9'})
print(d.groupby(['half','age']).agg(n=('p','size'),py=('py','median')).round(0))
g=d.groupby(['시군구','지번','y']).agg(n=('p','size'),py=('py','median'),a=('a','median')).reset_index().sort_values('n',ascending=False)
print(g.head(15).round(0).to_string())
print(d['매수'].value_counts().to_dict(), d['매도'].value_counts().to_dict())
d.to_pickle('/home/claude/w/ydp_jisan/d.pkl')
