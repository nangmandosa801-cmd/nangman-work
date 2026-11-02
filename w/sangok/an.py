# 산곡역 자이 힐스테이트 앤 하늘채 — 부평구 실거래 계산 (2026.10.8) · 자료: PC C:\블로그\실거래\아파트매매_인천_2025.csv · _202601-202608.csv (국토교통부 실거래가 공개시스템 · 계약일 기준)
import pandas as pd, io
def rd(p):
    t=open(p,'rb').read().decode('cp949'); i=t.index('"NO","시군구"')
    d=pd.read_csv(io.StringIO(t[i:]),dtype=str)
    d['p']=d['거래금액(만원)'].str.replace(',','').astype(float)/1e4; d['a']=d['전용면적(㎡)'].astype(float); d['ym']=d['계약년월'].astype(int); d['y']=d['건축년도'].astype(int)
    return d
U='/mnt/user-data/uploads/블로그/실거래/'
d=pd.concat([rd(U+'아파트매매_인천_2025.csv'),rd(U+'아파트매매_인천_202601-202608.csv')])
print('전체',len(d),'해제',(d['해제사유발생일']!='-').sum())
d=d[d['해제사유발생일']=='-']
b=d[d['시군구'].str.contains('부평구')].copy(); b['dong']=b['시군구'].str.split().str[-1]
b.to_pickle('bp.pkl')
r=b[(b.ym>=202601)&(b.ym<=202608)]
print('부평구 2026.1~8',len(r),'건 · 동별',r['dong'].value_counts().to_dict())
for lo,hi,nm in ((58.5,60.5,'59'),(83.5,85.5,'84'),(73.0,77.0,'75'),(48,52.5,'50')):
    x=r[(r.a>=lo)&(r.a<hi)]
    print('====',nm,'㎡ 부평구',len(x),'건 · 가장 비싼',x.p.max(), x.loc[x.p.idxmax(),['단지명','dong','y','ym','층']].tolist())
    print('  7억 넘는',(x.p>7).sum(),'· 6.64억 넘는',(x.p>6.64).sum(),'· 9.11억 넘는',(x.p>9.11).sum())
    g=x.groupby(['dong','단지명','y']).p.agg(['count','median','min','max']).reset_index()
    print(g[(g['count']>=3)].sort_values('median',ascending=False).head(14).to_string())
    s=x[x.dong.isin(['산곡동','청천동'])]
    print('  산곡·청천',len(s),'건 최고',s.p.max(), s.loc[s.p.idxmax(),['단지명','y','ym']].tolist() if len(s) else '')
