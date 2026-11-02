import pandas as pd
a=pd.read_pickle('/home/claude/w/apt_all.pkl'); a['ym']=a['계약년월'].astype(int)
s=a[a.ym>=202601]
def show(dong,lo,hi,n=12):
    x=s[(s['읍면동']==dong)&(s.a.between(lo,hi))]
    g=x.groupby(['시군','단지명','건축년도']).p.agg(['median','count']).sort_values('median',ascending=False)
    print('==',dong,lo,hi); print(g.head(n).to_string())
