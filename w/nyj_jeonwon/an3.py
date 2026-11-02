exec(open('an2.py').read().split("for name,t in")[0])
v=n[(n['지목']=='대')&(n.a>=330)&(n.a<=1000)].copy()
k=v[v['용도지역']=='계획관리지역']
print('계획관리',len(k),k.pp.quantile([.25,.5,.75]).round().tolist(),k.p.quantile([.25,.5,.75]).round().tolist(),k.py.median())
print(k.groupby('읍면').agg(n=('pp','size'),pp=('pp','median'),p=('p','median')).round())
print(k.groupby('도로조건').agg(n=('pp','size'),pp=('pp','median')).round())
for e in ['수동면','화도읍','진접읍','조안면']:
    x=v[v['읍면']==e]; print(e, x.groupby('용도지역').agg(n=('pp','size'),pp=('pp','median'),p=('p','median')).round().to_dict('index'))
gb=v[v['용도지역']=='개발제한구역']; print('GB',gb[['읍면','py','p','pp']].round().values.tolist())
v['y']=v.ym//100; print(v.groupby('y').agg(n=('pp','size'),pp=('pp','median')).round())
gk=g[(g['지목']=='대')&(g.a>=330)&(g.a<=1000)&(g['용도지역']=='계획관리지역')]
print('가평 계획관리 대',len(gk),gk.pp.median().round(),gk.p.median().round(),gk.groupby('읍면').agg(n=('pp','size'),pp=('pp','median')).round().to_dict('index'))
w=n[(n['지목'].isin(['전','답']))&(n.a>=330)&(n.a<=1000)&(n['용도지역']=='계획관리지역')]
print('남양주 계획관리 전답',len(w),w.pp.median().round(),w.p.median().round())
