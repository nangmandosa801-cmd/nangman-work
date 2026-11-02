import pandas as pd
d=pd.read_pickle('/home/claude/w/apt_all.pkl')
s=d[(d['광역'].astype(str).str.contains('서울'))&(d['해제사유발생일'].astype(str).str.strip().isin(['-','','nan']))].copy()
s['ym']=s['계약년월'].astype(int); s['y']=s.ym//100; s['m']=s.ym%100; s['p']=s.p.astype(float); s['a']=s.a.astype(float); s['건축년도']=s['건축년도'].astype(int)
s=s[s['m']<=8]
s['gu']=s['시군구'].str.split().str[1]
print('max ym',d['계약년월'].max())
for y in [2025,2026]:
    t=s[s.y==y]; n=len(t); k=((t.p>=7)&(t.p<8)).sum(); k6=((t.p>=6)&(t.p<7)).sum()
    print(y,n,'7억대',k,round(k/n*100,1),'6억대',k6, '84대', ((t.p>=7)&(t.p<8)&(t.a>=84)&(t.a<=85.5)).sum())
# per complex 84
s84=s[(s.a>=84)&(s.a<=85.5)]
key=['gu','읍면동','단지명','건축년도']
g=s84.groupby(key+['y']).p.agg(['median','count']).reset_index()
g=g[g['count']>=3]
a=g[g.y==2025].set_index(key); b=g[g.y==2026].set_index(key)
c=a.join(b,lsuffix='25',rsuffix='26',how='inner')
w=c[(c.median25>=7)&(c.median25<8)]
print('작년 7억대 단지(3건+)',len(a[(a['median']>=7)&(a['median']<8)]),'올해도',len(w))
print('8억 넘음',(w.median26>=8).sum(),'7억대',((w.median26>=7)&(w.median26<8)).sum(),'7억 아래',(w.median26<7).sum())
w=w.assign(r=(w.median26/w.median25-1)*100)
print('오른폭 중앙값',round(w.r.median(),1))
print(w[w.median26>=8].reset_index().gu.value_counts().head(8).to_dict())
print('올해 8억 넘은 곳 중앙값의 중앙값',w[w.median26>=8].median26.median())
print(w.sort_values('r',ascending=False).head(8)[['median25','median26','count26','r']])
nb=b[(b['median']>=7)&(b['median']<8)]
print('올해 84 7억대 단지',len(nb),'of',len(b)); print(nb.reset_index().gu.value_counts().to_dict())
print('지은해 중앙값',nb.reset_index()['건축년도'].median(), '2010후',(nb.reset_index()['건축년도']>=2010).sum())
print(nb.sort_values('count',ascending=False).head(10))
# 6억대 -> 7억대 inflow: last year <7 this year 7억대
cc=c[(c.median26>=7)&(c.median26<8)]
print('올해 7억대 & 작년도 3건+',len(cc),'작년 7억 아래',(cc.median25<7).sum())
# same 7.4 contrast
for nm in ['에스케이북한산시티','상계주공6(고층)','상계주공6']:
    t=s[(s.y==2026)&(s['단지명'].str.contains(nm.split('(')[0],regex=False))]
    if len(t): print(nm, t.groupby(t.a.round()).p.agg(['median','count']).to_string())
# 서울 전체 7억대 by gu 2026
t=s[(s.y==2026)&(s.p>=7)&(s.p<8)]
vc=t.gu.value_counts(); tot=s[s.y==2026].gu.value_counts()
print(pd.DataFrame({'n':vc,'tot':tot,'pct':(vc/tot*100).round(1)}).sort_values('n',ascending=False).head(10))
print('---')
for nm,lo,hi in [('에스케이북한산시티',84,85.5),('상계주공6',58,59.99),('삼각산아이원',84,85.5),('관악산휴먼시아2단지',84,85.5)]:
    t=s[s['단지명'].str.contains(nm,regex=False)&(s.a>=lo)&(s.a<=hi)]
    print(nm,t.groupby('y').p.agg(['median','count']).to_dict())
