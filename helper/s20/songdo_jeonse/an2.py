import pandas as pd
n=pd.read_pickle('n.pkl'); mm=pd.read_pickle('mm.pkl'); t=pd.read_pickle('t.pkl')
G={'6·8공구':['e편한세상송도','더샵송도마리나베이','랜드마크시티센트럴더샵','송도SKVIEW','송도오션파크베르디움','호반써밋송도']}
th=['퍼스트파크','파크애비뉴','마스터뷰','프라임뷰','센터니얼','아트윈']
import json; g=json.load(open('/home/claude/w/sdgeo.json')); H={k:v['hd'] for k,v in g.items()}
def grp(x):
    if x in G['6·8공구']: return '6·8공구'
    if any(k in x for k in th): return '3공구'
    h=H.get(x,'')
    if h=='송도2동': return '1공구'
    if h=='송도3동': return '7공구'
    if h=='송도1동' and any(k in x for k in ['풍림아이원','웰카운티','금호어울림','한진해모로','성지리벨루스']): return '2·4공구'
    return None
for d in (n,mm): d['g']=d['단지명'].map(grp)
print('unassigned 신규', n[n.g.isna()]['단지명'].value_counts().head(20).to_dict())
for k in ['1공구','3공구','7공구','2·4공구','6·8공구']:
    a=n[n.g==k]; b=mm[mm.g==k]
    print(k, '전세', a.dep.median(), len(a), a['단지명'].nunique(), '매매', b.p.median(), len(b), round(a.dep.median()/b.p.median()*100,1))
# 국제도시 (build>=2003)
n['by']=pd.to_numeric(n['건축년도']); mm['by']=pd.to_numeric(mm['건축년도'])
a=n[n.by>=2003]; b=mm[mm.by>=2003]
print('국제도시(2003+) 신규',a.dep.median(),len(a),'매매',b.p.median(),len(b), round(a.dep.median()/b.p.median()*100,1))
print('old',n[n.by<2003].dep.median(),len(n[n.by<2003]))
# monthly 신규 median
print(n.groupby('계약년월').dep.agg(['median','size']).to_string())
# 4억 이하 share
print('<=4억 share', (n.dep<=40000).mean(), '4억대', ((n.dep>=40000)&(n.dep<50000)).mean())
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); r=r[r['시군구'].str.contains('연수구 송도동')]
r['a']=r['전용면적(㎡)'].astype(float); r84=r[r.a.between(83,86)]
print('84 월세 share', (r84['전월세구분']=='월세').mean(), len(r84))
