import pandas as pd, numpy as np
t=pd.read_pickle('seoul8.pkl')
t=t[t['해제사유발생일'].isna()|(t['해제사유발생일'].astype(str).str.strip().isin(['','-','nan']))]
t=t[t['동']!='-'].copy()
t['d']=pd.to_numeric(t['동'].str.extract(r'^(\d{3,4})$')[0],errors='coerce')
t=t.dropna(subset=['d']); t['d']=t.d.astype(int)
t['a']=pd.to_numeric(t['전용면적(㎡)'],errors='coerce').round(2)
t['p']=pd.to_numeric(t['거래금액(만원)'].astype(str).str.replace(',',''),errors='coerce')
t['f']=pd.to_numeric(t['층'],errors='coerce'); t['y']=t['연'].astype(int); t['m']=t['월'].astype(int)
t['h']=t.y*2+(t.m>6)
t['by']=pd.to_numeric(t['건축년도'],errors='coerce')
t=t[t.by>=2005]
res=[]
for (gu,n),g in t.groupby(['시군','단지명']):
    if len(g)<120: continue
    ds=set(g.d.unique())
    gaps=[]
    for blk in sorted(set(d//100 for d in ds)):
        b=sorted(d for d in ds if d//100==blk)
        if len(b)<4: continue
        miss=[x for x in range(b[0],b[-1]+1) if x not in ds]
        gaps+=miss
    if not gaps: continue
    per=len(g)/len(ds)
    res.append((gu,n,int(g.by.iloc[0]),len(g),len(ds),round(per,1),gaps))
for r in sorted(res,key=lambda r:-r[3]): print(r)
