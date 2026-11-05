import pandas as pd, json, numpy as np
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m=pd.read_pickle('/home/claude/rtn/MK_2021_2026.pkl'); m=m[m['해제사유발생일']=='-'].copy()
m=m[m['거래유형']!='직거래'] if '거래유형' in m else m
m['a']=m['전용면적(㎡)'].astype(float); m['p']=num(m['거래금액(만원)']); m['y']=m['계약년월'].str[:4]; m['dong']=m['시군구'].str.split().str[2]
m['ym']=m['계약년월'].astype(int)
r=pd.read_pickle('/home/claude/rtn/RK_2024_2026.pkl').copy()
r=r[r['주택유형']=='아파트'] if '주택유형' in r else r
r['a']=r['전용면적(㎡)'].astype(float); r['dep']=num(r['보증금(만원)']); r['rent']=num(r['월세금(만원)']); r['y']=r['계약년월'].str[:4]; r['mo']=r['계약년월'].str[4:].astype(int); r['dong']=r['시군구'].str.split().str[2]
r['ym']=r['계약년월'].astype(int)
NW=m[m['시군구'].str.contains('노원구')]; NR=r[r['시군구'].str.contains('노원구')]
# 단지 정의: (표시이름, 동, 단지명, 면적 lo, hi, 묶음)
D=[('주공10단지','중계동','주공10',56,60,'을지초'),
   ('건영3차','중계동','건영3',83,86,'을지초'),
   ('청구3차','중계동','청구3',83,86,'을지초'),
   ('롯데우성 101㎡','중계동','롯데우성',100,103,'을지초'),
   ('롯데우성 115㎡','중계동','롯데우성',114,116,'을지초'),
   ('주공8단지','중계동','주공8',48,51,'을지초'),
   ('성원1','중계동','성원1',83,86,'을지초'),
   ('신안','중계동','신안',83,86,'을지초'),
   ('양지대림1','중계동','양지마을(대림)1',83,86,'을지초'),
   # 짝
   ('중계그린1단지 59㎡','중계동','중계그린1단지',58,60,'짝'),
   ('중계무지개 59㎡','중계동','중계무지개',58,60,'짝'),
   ('학여울청구 59㎡','하계동','학여울청구',58,60,'짝'),
   ('하계1청구','하계동','하계1청구',83,86,'짝'),
   ('하계2현대','하계동','하계2현대',83,86,'짝'),
   ('한신4차(상계)','상계동','한신4차',83,86,'짝'),
   ('노원현대(상계)','상계동','노원현대',83,86,'짝'),
   ('금호타운(상계)','상계동','금호타운',83,86,'짝'),
   ('상계신동아','상계동','상계신동아',83,86,'짝'),
   ('라이프 101㎡','중계동','라이프',100,103,'짝'),
   ('신동아 101㎡','중계동','신동아(366)',100,103,'짝'),
   ('청구(366) 101㎡','중계동','청구(366)',100,103,'짝'),
   ('동진신안 101㎡','중계동','동진신안',100,103,'짝'),
   ('라이프 115㎡','중계동','라이프',114,116,'짝'),
   ('신동아 115㎡','중계동','신동아(366)',114,116,'짝'),
   ('청구(366) 115㎡','중계동','청구(366)',114,116,'짝'),
   ('대림벽산 114㎡','중계동','대림벽산(363)',113,116,'짝'),
  ]
out={}
for nm,dong,dj,lo,hi,grp in D:
    x=NW[(NW.dong==dong)&(NW['단지명']==dj)&(NW.a>=lo)&(NW.a<=hi)]
    q=NR[(NR.dong==dong)&(NR['단지명']==dj)&(NR.a>=lo)&(NR.a<=hi)]
    row={'grp':grp,'b':x['건축년도'].iloc[0] if len(x) else None,'areas':sorted(x.a.round(1).unique().tolist())}
    for y in ['2021','2022','2023','2024','2025','2026']:
        xx=x[x.y==y]; row[y]={'n':int(len(xx)),'med':float(xx.p.median()) if len(xx) else None,'max':int(xx.p.max()) if len(xx) else None}
    # 2021 하반기 중앙값 · 최고
    h=x[(x.ym>=202107)&(x.ym<=202112)]; row['2021H2']={'n':int(len(h)),'med':float(h.p.median()) if len(h) else None}
    # 2026 마지막 거래 · 2026 최고
    if row['2026']['n']:
        last=x[x.y=='2026'].sort_values(['계약년월','계약일']).iloc[-1]; row['last26']=[last['계약년월'],int(last['계약일']),int(last.p),last['층']]
    # 반기
    x2=x.copy(); x2['h']=x2['계약년월'].apply(lambda s:s[:4]+('H1' if int(s[4:])<=6 else 'H2'))
    row['half']={h:[int(len(g)),float(g.p.median())] for h,g in x2.groupby('h')}
    # 전세 (월세 0) 2026 · 2025 · 신규/갱신
    for y in ['2025','2026']:
        je=q[(q.y==y)&(q.rent==0)]; new=je[je['계약구분']=='신규']; ren=je[je['계약구분']=='갱신']
        row[f'je{y}']={'all':int(len(je)),'new_n':int(len(new)),'new_med':float(new.dep.median()) if len(new) else None,'ren_n':int(len(ren)),'ren_med':float(ren.dep.median()) if len(ren) else None,
                       'lease_n':int(len(q[q.y==y])),'rent_n':int(((q.y==y)&(q.rent>0)).sum())}
        jf=je[je.mo.isin([1,2])]; row[f'je{y}']['jf']=int(len(jf)); row[f'je{y}']['jf_share']=round(len(jf)/len(je)*100,1) if len(je) else None
    if row['2026']['med'] and row['je2026']['new_med']: row['ratio26']=round(row['je2026']['new_med']/row['2026']['med']*100,1)
    if row['2021']['med'] and row['2026']['med']: row['rec_med']=round(row['2026']['med']/row['2021']['med']*100,1)
    if row['2021']['max'] and row['2026']['max']: row['rec_max']=round(row['2026']['max']/row['2021']['max']*100,1)
    out[nm]=row
# 동별 전세 1~2월 비율 (아파트 전세 전체 · 월세 0)
def jf(q,y):
    je=q[(q.y==y)&(q.rent==0)]; k=int(je.mo.isin([1,2]).sum()); n=len(je)
    g=je[je['계약구분']=='갱신']; new=je[je['계약구분']=='신규']
    return {'n':int(n),'jf':k,'share':round(k/n*100,1) if n else None,'ren_share':round(len(g)/(len(g)+len(new))*100,1) if (len(g)+len(new)) else None,'month':{int(a):int(b) for a,b in je.groupby('mo').size().items()}}
dongs={}
for dong in ['중계동','하계동','상계동','월계동','공릉동']:
    q=NR[NR.dong==dong]; dongs[dong]={y:jf(q,y) for y in ['2024','2025','2026']}
dongs['노원구']={y:jf(NR,y) for y in ['2024','2025','2026']}
# 을지초 네 단지 묶음 전세 1~2월
sel=NR[(NR.dong=='중계동')&(NR['단지명'].isin(['주공10','건영3','청구3','롯데우성']))]
dongs['을지초4']={y:jf(sel,y) for y in ['2024','2025','2026']}
sel2=NR[(NR.dong=='중계동')&(NR['단지명'].isin(['주공10','건영3','청구3','롯데우성','주공8','성원1','신안','양지마을(대림)1']))]
dongs['을지초8']={y:jf(sel2,y) for y in ['2024','2025','2026']}
# 서울 전체 2026 (R2026)
try:
    S=pd.read_pickle('/home/claude/rtn/R2026.pkl'); S=S[S['시군구'].str.startswith('서울')]
    S=S[S['주택유형']=='아파트'] if '주택유형' in S else S
    S['rent']=num(S['월세금(만원)']); S['mo']=S['계약년월'].str[4:].astype(int); S['y']=S['계약년월'].str[:4]
    dongs['서울']={'2026':jf(S,'2026')}
except Exception as e: dongs['서울']={'err':str(e)}
out['_dong']=dongs
# 중계동 84 전체 · 하계동 84 전체 연도별
for lab,dong in [('중계동84','중계동'),('하계동84','하계동')]:
    x=NW[(NW.dong==dong)&(NW.a>=83)&(NW.a<=86)]
    out['_'+lab]={y:{'n':int((x.y==y).sum()),'med':float(x[x.y==y].p.median()) if (x.y==y).sum() else None} for y in ['2021','2022','2023','2024','2025','2026']}
# 2026 노원구 거래금액 상위 10
top=NW[NW.y=='2026'].sort_values('p',ascending=False).head(12)[['단지명','a','p','계약년월','dong']]
out['_top26']=[[a,b,int(c),d,e] for a,b,c,d,e in top.values.tolist()]
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=1,default=str)
for k,v in out.items():
    if k.startswith('_'): continue
    print('==',k,v['grp'],v['b'],v['areas'])
    print('   ',{y:(v[y]['n'],v[y]['med'],v[y]['max']) for y in ['2021','2022','2023','2024','2025','2026']})
    print('    21H2',v['2021H2'],'last26',v.get('last26'),'rec_med',v.get('rec_med'),'rec_max',v.get('rec_max'))
    print('    je26',v['je2026'],'ratio',v.get('ratio26'))
    print('    je25',v['je2025'])
print(json.dumps(out['_dong'],ensure_ascii=False))
print(out['_중계동84'],out['_하계동84'])
print(out['_top26'])
