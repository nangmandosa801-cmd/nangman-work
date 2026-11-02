import pandas as pd, io, glob, sys
sys.path.insert(0,'/home/claude/watch')
f='/home/claude/watch/rt/bun_41000_2025-10_2026-10.csv'
t=open(f,encoding='cp949',errors='ignore').read().splitlines()
h=[i for i,l in enumerate(t) if '단지명' in l][0]
b=pd.read_csv(io.StringIO('\n'.join(t[h:])))
b=b[b['단지명'].str.contains('신곡 시그니처뷰',na=False)]
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(int)
b['ym']=b['계약년월'].astype(int)
b=b[b['해제사유발생일'].astype(str).str.strip()=='-']
def ty(a):
  return {52.5195:'52A',52.4767:'52B',59.9166:'59A',59.9329:'59B',59.9548:'59C',74.9257:'74',84.6432:'84A',84.8729:'84B'}[round(a,4)]
b['ty']=b['전용면적(㎡)'].apply(ty)
print('total',len(b), b['ym'].min(), b['ym'].max(), b['분/입주권'].value_counts().to_dict(), b['거래유형'].value_counts().to_dict())
r=b[(b['ym']>=202604)]
print(r.groupby(['ty','분/입주권'])['p'].agg(['count','median','min','max']))
# 분양가 band
P={'59A':[(1,1,43600),(2,2,45540),(3,3,46510),(4,9,47480),(10,19,48450),(20,29,48930),(30,99,49420)],
   '59B':[(1,1,43610),(2,2,45550),(3,3,46520),(4,9,47490),(10,19,48460),(20,99,48940)],  # 104동4호 group lower? use max group
   '59C':[(1,1,42580),(2,2,44480),(3,3,45420),(4,9,46370),(10,19,47310),(20,29,47790),(30,99,48260)],
   '74':[(1,1,51680),(2,2,53980),(3,3,55130),(4,9,56270),(10,19,57420),(20,29,58000),(30,99,58570)],
   '84A':[(1,1,60710),(2,2,62030),(3,3,64010),(4,4,64670)],
   '84B':[(1,1,60220),(2,2,62890),(3,3,64230),(4,9,65570),(10,19,66910),(20,29,67580),(30,99,68240)],
   '52A':[(2,2,41390),(3,3,42270),(4,9,43150),(10,19,44030),(20,99,44480)],
   '52B':[(2,2,41400),(3,3,42280),(4,9,43160),(10,19,44040),(20,99,44480)]}
def bp(ty,fl):
  for a,c,v in P[ty]:
    if a<=fl<=c: return v
r=r[r['분/입주권']=='분양권'].copy()
r['층']=r['층'].astype(int); r['bp']=[bp(a,c) for a,c in zip(r['ty'],r['층'])]; r['d']=r['p']-r['bp']
pd.set_option('display.width',200)
print(r.sort_values(['ty','ym','계약일'])[['ty','ym','계약일','층','p','bp','d','거래유형']].to_string())
print(r.groupby('ty')['d'].agg(['count','median','min','max']))
r.to_pickle('/home/claude/w/singok/bun.pkl')
