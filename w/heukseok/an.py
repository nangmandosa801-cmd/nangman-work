import pandas as pd, sys
sys.path.insert(0,'/home/claude/watch'); import rt_fetch
d=pd.read_pickle('/home/claude/w/apt_all.pkl')
d=d[(d['읍면동']=='흑석동')&(d['시군']=='동작구')&(d['자료']=='아파트매매')]
d=d[d['해제사유발생일']=='-'].copy(); d['ym']=d['계약년월'].astype(int)
r=rt_fetch.load(['202607','202608','202609','202610'])
r=r[(r['읍면동']=='흑석동')&(r['시군']=='동작구')]
print('pkl ym range',d.ym.min(),d.ym.max(),len(d)); print('rt',r.ym.min(),r.ym.max(),len(r))
# combine: pkl up to 202606, rt from 202607
d=d[d.ym<=202606]
cols=['단지명','a','p','ym','건축년도','층'] 
r2=r.copy()
print(r.columns.tolist())
d['y']=pd.to_numeric(d['건축년도'],errors='coerce')
all_=pd.concat([d[['단지명','a','p','ym','y']].assign(층=None,일=None),r[['단지명','a','p','ym','y','층','계약일']].rename(columns={'계약일':'일'})])
all_['A']=all_['a'].round()
print(all_.groupby('ym').size().loc[202401:].to_string())
x=all_[all_.ym>=202501]
print(x.groupby(['단지명','y']).size().sort_values(ascending=False).head(25))
print(r[['단지명','a','p','ym','계약일','층','y']].sort_values('ym').to_string())
print('=====')
def per(lo,hi): 
    z=all_[(all_.ym>=lo)&(all_.ym<=hi)]; return z
for lo,hi,nm in [(202504,202509,'A'),(202604,202609,'B'),(202501,202506,'H1_25'),(202510,202510,'Oct25')]:
    z=per(lo,hi); print(nm,len(z))
A=per(202504,202509); B=per(202604,202609)
ga=A.groupby(['단지명','A']).p.agg(['median','count']); gb=B.groupby(['단지명','A']).p.agg(['median','count'])
j=ga.join(gb,lsuffix='_A',rsuffix='_B',how='outer'); j['chg%']=(j['median_B']/j['median_A']-1)*100
print(j.round(2).to_string())
