import pandas as pd, sys
sys.path.insert(0,'/home/claude/watch'); import rt_fetch
d=pd.read_pickle('/home/claude/w/apt_all.pkl')
d=d[(d['읍면동']=='흑석동')&(d['시군']=='동작구')&(d['자료']=='아파트매매')&(d['해제사유발생일']=='-')].copy(); d['ym']=d['계약년월'].astype(int)
d['y']=pd.to_numeric(d['건축년도'],errors='coerce'); d['A']=d.a.round()
r=rt_fetch.load(['202604','202605','202606','202607','202608','202609','202610'])
r=r[(r['읍면동']=='흑석동')&(r['시군']=='동작구')].copy(); r['A']=r.a.round(); r['층']=r['층'].astype(int)
print('rt rows',len(r), r.ym.value_counts().sort_index().to_dict())
print('pkl 2026.4-6',len(d[(d.ym>=202604)&(d.ym<=202606)]))
A=d[(d.ym>=202504)&(d.ym<=202509)]
B=r[(r.ym>=202604)&(r.ym<=202609)]
print('A',len(A),'B',len(B), 'last 계약', B.sort_values(['ym','계약일']).tail(1)[['ym','계약일']].values)
ga=A.groupby(['단지명','A']).p.agg(['median','count']); gb=B.groupby(['단지명','A']).p.agg(['median','count'])
j=ga.join(gb,lsuffix='_A',rsuffix='_B',how='inner'); j['chg%']=(j['median_B']/j['median_A']-1)*100
print(j.round(2).to_string())
jj=j[(j.count_A>=2)&(j.count_B>=2)]; print('pairs>=2',len(jj),'median chg',jj['chg%'].median().round(1), 'down',(jj['chg%']<0).sum())
print('all pairs',len(j),'median',j['chg%'].median().round(1))
for n,a in [('흑석리버파크자이',85),('흑석한강센트레빌',85),('흑석한강푸르지오',85),('흑석한강센트레빌Ⅱ',85),('흑석동양아파트',85),('흑석리버파크자이',60),('아크로리버하임',60),('롯데캐슬에듀포레',60),('흑석동양아파트',60),('청호',60),('우리유앤미',84)]:
    z=B[(B.단지명==n)&(B.A==a)].sort_values('p')
    print(n,a,len(z),'med',z.p.median(),'floors',z[['p','층','ym','계약일']].values.tolist())
print(B.groupby(['단지명']).y.first())
# 2025 H1 vs and annual counts
print('counts by year', d[d.ym>=202301].groupby(d.ym//100).size().to_dict())
