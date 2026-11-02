import pandas as pd, numpy as np
a=pd.read_pickle('/home/claude/w/apt_all.pkl'); a['ym']=a['계약년월'].astype(int); a['y']=a.ym//100
a['by']=a['건축년도'].astype(int); a['ar']=a['전용면적(㎡)'].astype(str)
def sub(sigun,gu_or_dong=None):
    x=a[a['시군']==sigun]
    return x
def pair(x,y0,y1,m1=8,minn=1):
    x0=x[(x.y==y0)&(x.ym%100<=m1)] if m1<12 else x[x.y==y0]
    x0=x[x.y==y0]; x1=x[(x.y==y1)]
    g0=x0.groupby(['읍면동','단지명','ar']).p.agg(['median','count']); g1=x1.groupby(['읍면동','단지명','ar']).p.agg(['median','count'])
    j=g0.join(g1,lsuffix='0',rsuffix='1',how='inner'); j=j[(j.count0>=minn)&(j.count1>=minn)]
    j['r']=j.median1/j.median0-1; return j
