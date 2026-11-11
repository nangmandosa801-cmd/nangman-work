import pandas as pd
m=pd.read_pickle('/home/claude/rtn/MD_daegu_2021_2026.pkl')
m=m[m['해제사유발생일'].astype(str).str.strip()=='-']; m=m[m['거래유형'].astype(str).str.strip()!='직거래']
m['면']=m['전용면적(㎡)'].astype(float); m['금']=m['거래금액(만원)'].str.replace(',','').astype(int)
m['년']=m['계약년월'].str[:4]; m['단']=m['단지명'].str.replace(' ',''); m['구']=m['시군구'].str.split().str[1]; m['동']=m['시군구'].str.split().str[2]
x=m[(m['면']>=83)&(m['면']<=86)]
pd.set_option('display.width',250); pd.set_option('display.max_rows',500)
import sys
for g,dn in [('수성구',None),('달서구',None),('동구',None)]:
    z=x[x['구']==g]
    t=z.pivot_table(index=['동','단','건축년도'],columns='년',values='금',aggfunc=['median','count'])
    t=t[(t[('count','2026')]>=8)]
    if g!='수성구': t=t[t.index.get_level_values('건축년도').astype(int)>=2015]
    print(g); print(t.to_string())
