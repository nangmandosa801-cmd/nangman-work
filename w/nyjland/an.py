import pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
d=pd.read_pickle('nyj.pkl')
d=d[(d['계약년월']>='202501')&(d['계약년월']<='202608')]
print('전체',len(d))
d=d[d['해제사유발생일'].isin(['-','',None])|d['해제사유발생일'].isna()]
print('해제 뺌',len(d),'지분',(d['지분구분']=='지분').sum())
w=d[d['지분구분']!='지분'].copy()
w['amt']=pd.to_numeric(w['거래금액(만원)'],errors='coerce'); w['m2']=pd.to_numeric(w['계약면적'],errors='coerce'); w['py']=w['m2']/3.3058; w['pp']=w['amt']/w['py']
w=w[(w.amt>0)&(w.m2>0)]
print('통째',len(w))
bins=[0,5000,10000,20000,30000,50000,100000,1e12]; lab=['~5천','5천~1억','1~2억','2~3억','3~5억','5~10억','10억~']
w['b']=pd.cut(w.amt,bins,labels=lab,right=True)
g=w.groupby('b',observed=True).agg(n=('amt','size'),py=('py','median'),amt=('amt','median')); g['share']=(g.n/len(w)*100).round(1); print(g)
u=w[w.amt<=10000]; print('1억 이하',len(u),round(len(u)/len(w)*100,1),'면적 중앙',round(u.py.median(),1),'평', round(u.m2.median(),1))
print(u.groupby('지목').agg(n=('amt','size'),py=('py','median')).sort_values('n',ascending=False).head(8))
b=u[u.py>=100]; print('1억 이하 100평 이상',len(b))
print(b.groupby('지목').agg(n=('amt','size'),py=('py','median'),amt=('amt','median'),pp=('pp','median')).sort_values('n',ascending=False).head(6).round(1))
print(b.groupby('용도지역').agg(n=('amt','size'),py=('py','median'),pp=('pp','median')).sort_values('n',ascending=False).head(8).round(1))
print(b['도로조건'].value_counts())
print('임야&(GB|농림)',((b['지목']=='임야')&b['용도지역'].isin(['개발제한구역','농림지역'])).sum(), '(GB|농림)',b['용도지역'].isin(['개발제한구역','농림지역']).sum())
print(b.groupby('읍면동').agg(n=('amt','size'),pp=('pp','median')).sort_values('n',ascending=False).head(10).round(1))
# 같은 조건끼리: 밭·논 100~1천 평, 용도지역×도로
w['road']=np.where(w['도로조건']=='-','없음','붙음')
f=w[w['지목'].isin(['전','답'])&(w.py>=100)&(w.py<1000)]
print('밭논 100~1천',len(f)); t=f.groupby(['용도지역','road']).agg(n=('pp','size'),pp=('pp','median')).round(0).unstack(); print(t[t[('n','붙음')].fillna(0)+t[('n','없음')].fillna(0)>=15])
# 임야 넓이×용도지역
m=w[w['지목']=='임야'].copy(); m['sz']=pd.cut(m.py,[0,100,1000,3000,10000,1e9],labels=['~100','100~1천','1천~3천','3천~1만','1만~'])
print('임야',len(m)); print(m.groupby(['sz','용도지역'],observed=True).agg(n=('pp','size'),pp=('pp','median')).round(1).unstack(0).dropna(how='all').to_string())
print(m[m.py>=100].groupby('road').agg(n=('pp','size'),pp=('pp','median')).round(1))
print(m[(m.py>=100)].groupby(['용도지역','road']).agg(n=('pp','size'),pp=('pp','median')).round(1).unstack())
# 대지
dj=w[(w['지목']=='대')&(w.py>=30)&(w.py<300)]; print('대지 30~300평',len(dj)); print(dj.groupby(['용도지역','road']).agg(n=('pp','size'),pp=('pp','median')).round(0).unstack())
w.to_pickle('w.pkl')
