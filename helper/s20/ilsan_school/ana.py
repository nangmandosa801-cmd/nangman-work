from base import get
import pandas as pd, json
m,r=get()
G={'후곡':('일산동','후곡마을'),'백마':('마두동','백마마을'),'강촌':('마두동','강촌마을'),'문촌':('주엽동','문촌마을'),'강선':('주엽동','강선마을'),'백송':('백석동','백송마을'),'흰돌':('백석동','흰돌마을'),'성저장성':('대화동','성저마을|장성마을'),'호수':('장항동','호수마을')}
def sel(df,k,a84=True):
    d,p=G[k]; x=df[(df['동']==d)&(df['단'].str.contains(p))&(df['건'].between(1992,1997))]
    if a84: x=x[(x['면']>=83)&(x['면']<=86)]
    return x
out={}
for k in G:
    x=sel(m,k); o={'단지수':int(x['단'].nunique())}
    for y in ['2021','2022','2023','2024','2025','2026']:
        z=x[x['년']==y]; o[y]={'n':int(len(z)),'med':float(z['금'].median()) if len(z) else None,'max':int(z['금'].max()) if len(z) else None}
    # 같은 단지 짝: 단지별 중앙값 비율의 중앙값 (2021, 2026 각 3건 이상)
    pr=[];pr23=[]
    for dn,z in x.groupby(['단','건']):
        a=z[z['년']=='2021']['금']; b=z[z['년']=='2026']['금']; c=z[z['년']=='2023']['금']
        if len(a)>=3 and len(b)>=3: pr.append(b.median()/a.median()-1)
        if len(a)>=3 and len(c)>=3: pr23.append(c.median()/a.median()-1)
    o['pair26']=[len(pr),float(pd.Series(pr).median()) if pr else None]; o['pair23']=[len(pr23),float(pd.Series(pr23).median()) if pr23 else None]
    y=sel(r,k); j=y[y['전월세구분']=='전세']
    for yy in ['2024','2025','2026']:
        jn=j[(j['년']==yy)&(j['계약구분']=='신규')]; jg=j[(j['년']==yy)&(j['계약구분']=='갱신')]
        o['jn'+yy]={'n':int(len(jn)),'med':float(jn['보'].median()) if len(jn) else None}; o['jg'+yy]={'n':int(len(jg)),'med':float(jg['보'].median()) if len(jg) else None}
    # 비율은 모든 평형
    ya=sel(r,k,False); ja=ya[ya['전월세구분']=='전세']
    jj=ja[ja['년'].isin(['2024','2025'])]
    o['j2425_all']=int(len(jj)); o['j2425_12']=int(len(jj[jj['월']<=2])); o['j2425_renew']=int(len(jj[jj['계약구분']=='갱신']))
    j26=ja[ja['년']=='2026']; o['j26_all']=int(len(j26)); o['j26_12']=int(len(j26[j26['월']<=2])); o['j26_renew']=int(len(j26[j26['계약구분']=='갱신']))
    a3=ja; o['j3_all']=int(len(a3)); o['j3_renew']=int(len(a3[a3['계약구분']=='갱신']))
    y25=ya[ya['년'].isin(['2025','2026'])]; o['r_all']=int(len(y25)); o['r_wol']=int(len(y25[y25['전월세구분']=='월세']))
    g=ja[(ja['년'].isin(['2025','2026']))&(ja['계약구분']=='갱신')].copy()
    g['전']=g['종전계약 보증금(만원)'].astype(str).str.replace(',',''); g=g[g['전'].str.isdigit()]; g['전']=g['전'].astype(int); g=g[g['전']>0]
    o['renew_up']=[int(len(g)),float((g['보']/g['전']-1).median()) if len(g) else None]
    out[k]=o
# 일산 전체(두 구 · 모든 아파트) 전세
ja=r[r['전월세구분']=='전세']; jj=ja[ja['년'].isin(['2024','2025'])]
out['_all']={'all':int(len(jj)),'12':int(len(jj[jj['월']<=2])),'renew':int(len(jj[jj['계약구분']=='갱신'])),'3all':int(len(ja)),'3renew':int(len(ja[ja['계약구분']=='갱신']))}
# 단지별
out['_dan']={}
for k in ['후곡','백마','강촌','백송','성저장성','문촌','강선']:
    for (dn,by),z in sel(m,k).groupby(['단','건']):
        o={y:[float(z[z['년']==y]['금'].median()) if len(z[z['년']==y]) else None,int(len(z[z['년']==y]))] for y in ['2021','2023','2025','2026']}
        o['max26']=int(z[z['년']=='2026']['금'].max()) if len(z[z['년']=='2026']) else None
        out['_dan'][f'{k}|{dn}|{by}']=o
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
for k,v in out.items():
    if k=='_dan': continue
    if k.startswith('_'): print(k,v); continue
    print(k,v['단지수'],{y:(v[y]['med'],v[y]['n']) for y in ['2021','2022','2023','2024','2025','2026']})
    a,b,c=v['2021']['med'],v['2023']['med'],v['2026']['med']
    print('   23/21 %.1f 26/21 %.1f 26/23 %.1f'%((b/a-1)*100,(c/a-1)*100,(c/b-1)*100),'pair26',v['pair26'],'pair23',v['pair23'])
    print('   jn26',v['jn2026'],'jg26',v['jg2026'],'jn25',v['jn2025'],'전세가율 %.1f'%(v['jn2026']['med']/c*100),'1~2월 %d/%d=%.1f'%(v['j2425_12'],v['j2425_all'],v['j2425_12']/v['j2425_all']*100),'갱신2425 %.1f'%(v['j2425_renew']/v['j2425_all']*100),'26: 12월 %.1f 갱신 %.1f'%(v['j26_12']/v['j26_all']*100,v['j26_renew']/v['j26_all']*100),'월세 %.1f'%(v['r_wol']/v['r_all']*100),'인상',v['renew_up'])
# 단지 섞임을 뺀 지수: 거래값 ÷ 그 단지 84㎡ 전체 기간 중앙값 → 해마다 중앙값 → 2021=100
print('--- 지수')
ix={}
for k in G:
    x=sel(m,k).copy(); x['key']=x['단']+x['건'].astype(str)
    c=x.groupby('key')['금'].transform('median'); cnt=x.groupby('key')['금'].transform('size')
    x=x[cnt>=10]; x['지']=x['금']/c[cnt>=10]
    s=x.groupby('년')['지'].median(); o={y:round(float(s[y]/s['2021']*100),1) for y in ['2021','2022','2023','2024','2025','2026']}
    ix[k]=o; print(k,x['key'].nunique(),o,'26/23 %.1f'%((s['2026']/s['2023']-1)*100))
out['_ix']=ix
# 후곡 안에서: 학원가 붙은 9·10·15·16단지(럭키 롯데 건영15 동아16 코오롱) 대 나머지
A=['후곡마을(럭키)','후곡마을(롯데)','후곡마을(건영15)','후곡마을(동아16)','후곡마을(코오롱)']
x=sel(m,'후곡'); 
for nm,z in [('후곡 9·15·16',x[x['단'].isin(A)]),('후곡 나머지',x[~x['단'].isin(A)])]:
    o={y:[float(z[z['년']==y]['금'].median()),int(len(z[z['년']==y]))] for y in ['2021','2023','2025','2026']}; out['_'+nm]=o; print(nm,o)
y=sel(r,'후곡'); j=y[(y['전월세구분']=='전세')&(y['년']=='2026')&(y['계약구분']=='신규')]
for nm,z in [('후곡 9·15·16',j[j['단'].isin(A)]),('후곡 나머지',j[~j['단'].isin(A)])]: print(nm,'jn26',z['보'].median(),len(z)); out['_jn_'+nm]=[float(z['보'].median()),int(len(z))]
# 2026 달별 후곡 · 백송
for k in ['후곡','백마','강촌','백송','성저장성']:
    z=sel(m,k); z=z[z['년']=='2026']; print(k,'max26',z['금'].max(),'min',z['금'].min(), z.groupby('계약년월')['금'].agg(['median','count']).T.to_dict())
    z=sel(m,k); z=z[z['년']=='2021']; print(k,'max21',z['금'].max())
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=0)
