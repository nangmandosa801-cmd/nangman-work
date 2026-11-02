import pandas as pd, numpy as np
d=pd.read_pickle('apt_all.pkl')
b=d[d['시군구'].str.contains('분당구')&(d['해제사유발생일']=='-')].copy()
b['ym']=b['계약년월'].astype(int); b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float); b['a']=b['전용면적(㎡)'].astype(float)
b['py']=b['p']/b['a']*3.3058
g1=['샛별마을(삼부)','샛별마을(동성)','샛별마을(라이프)','샛별마을(우방)','시범현대','시범우성']+[n for n in b['단지명'].unique() if n.startswith('양지마을')]+[n for n in b['단지명'].unique() if n.startswith('목련마을')]
g2=['시범삼성','시범한신','시범한양','이매촌(삼성)','이매촌(삼환)','파크타운(대림)','파크타운(서안)','파크타운(삼익)','파크타운(롯데)','푸른마을(신성)','푸른마을(쌍용)','푸른마을(벽산)','한솔마을(1단지)(청구)','한솔마을(2단지)(LG)','한솔마을(3단지)(한일)']
b['grp']=np.where(b['단지명'].isin(g1),'1차',np.where(b['단지명'].isin(g2),'2차','나머지'))
def pairs(df,w1,w2):
    a=df[(df.ym>=w1[0])&(df.ym<=w1[1])].groupby(['단지명','a'])['py'].median()
    c=df[(df.ym>=w2[0])&(df.ym<=w2[1])].groupby(['단지명','a'])['py'].median()
    j=pd.concat([a,c],axis=1,keys=['x','y']).dropna()
    if len(j)==0: return 0,float('nan')
    return len(j),(j.y/j.x-1).median()*100
if __name__=='__main__':
  for g in ['1차','2차','나머지']:
    s=b[b.grp==g]
    n1,r1=pairs(s,(202503,202508),(202603,202608))
    n2,r2=pairs(s,(202405,202410),(202603,202608))
    print(g,'1년',n1,round(r1,1),'| 선정전(24.5~10)→지금',n2,round(r2,1), '| 2026.3~8 평당중앙',round(s[(s.ym>=202603)].py.median()), '건수', len(s[s.ym>=202603]))
  m=b[b.ym>=202501].groupby(['ym','grp']).size().unstack(fill_value=0); print(m.to_string())
  print('--- 2차 단지별')
  for n in g2:
    s=b[b['단지명']==n]; k,r=pairs(s,(202503,202508),(202603,202608))
    rec=s[s.ym>=202606].sort_values('ym').tail(1)
    print(n,k,round(r,1) if k else None, rec[['a','p','ym']].values.tolist())
  print('--- 1차 단지별')
  for n in ['샛별마을(삼부)','샛별마을(우방)','양지마을(금호1)','양지마을(2단지)(청구)','시범현대','시범우성','목련마을(영남)']:
    s=b[b['단지명']==n]; k,r=pairs(s,(202503,202508),(202603,202608)); k2,r2=pairs(s,(202405,202410),(202603,202608))
    print(n,k,round(r,1) if k else None,'| 선정전→',k2,round(r2,1) if k2 else None)
