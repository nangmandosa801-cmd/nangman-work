import pandas as pd, json, numpy as np
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m=pd.read_pickle('/home/claude/rtn/MK_2021_2026.pkl'); m=m[m['해제사유발생일']=='-'].copy()
m['a']=m['전용면적(㎡)'].astype(float); m['p']=num(m['거래금액(만원)']); m['y']=m['계약년월'].str[:4]; m['dong']=m['시군구'].str.split().str[2]
r=pd.read_pickle('/home/claude/rtn/RK_2024_2026.pkl').copy()
r['a']=r['전용면적(㎡)'].astype(float); r['dep']=num(r['보증금(만원)']); r['rent']=num(r['월세금(만원)']); r['y']=r['계약년월'].str[:4]; r['mo']=r['계약년월'].str[4:].astype(int); r['dong']=r['시군구'].str.split().str[2]
r=r[r['주택유형']=='아파트'] if '주택유형' in r else r
PAIRS=[('강남구','대치동',['세곡동','자곡동','율현동'],'세곡 · 자곡 · 율현'),('양천구','목동',['신월동'],'신월동'),('노원구','중계동',['하계동'],'하계동'),('서초구','반포동',['방배동'],'방배동')]
def f84(d): return d[(d.a>=83)&(d.a<=86)]
out={}
def jstat(q):
    """새 세입자 전세(월세 0) 84: 연도별 1~2월 몫, 월별 건수"""
    q=f84(q); q=q[(q.rent==0)&(q['계약구분']=='신규')]
    o={}
    for y in ['2024','2025','2026']:
        qq=q[q.y==y]; n=len(qq); j=int(qq.mo.isin([1,2]).sum())
        o[y]={'n':int(n),'jf':j,'share':round(j/n*100,1) if n else None,'month':{int(k):int(v) for k,v in qq.groupby('mo').size().items()},'med':float(qq.dep.median()) if n else None,
              'med_jf':float(qq[qq.mo.isin([1,2])].dep.median()) if j else None,'med_rest':float(qq[~qq.mo.isin([1,2])].dep.median()) if n-j else None}
    return o
def mstat(d):
    d=f84(d); o={}
    for y in ['2021','2022','2023','2024','2025','2026']:
        dd=d[d.y==y]; o[y]={'n':int(len(dd)),'med':float(dd.p.median()) if len(dd) else None}
    # 반기
    d2=d.copy(); d2['h']=d2['계약년월'].apply(lambda s:s[:4]+('H1' if int(s[4:])<=6 else 'H2'))
    o['half']={h:[int(len(g)),float(g.p.median())] for h,g in d2.groupby('h')}
    return o
for gu,hk,nh,nhlab in PAIRS:
    gm=m[m['시군구'].str.contains(gu)]; gr=r[r['시군구'].str.contains(gu)]
    for lab,dongs in [(hk,[hk]),(nhlab,nh)]:
        dm=gm[gm.dong.isin(dongs)]; dr=gr[gr.dong.isin(dongs)]
        out[f'{gu}|{lab}']={'je':jstat(dr),'m':mstat(dm)}
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=1)
for k,v in out.items():
    print('==',k)
    for y in ['2024','2025','2026']: print('  je',y,v['je'][y]['n'],v['je'][y]['jf'],v['je'][y]['share'],'med',v['je'][y]['med'],'jf',v['je'][y]['med_jf'],'rest',v['je'][y]['med_rest'])
    print('  je2026 month',v['je']['2026']['month']); print('  je2025 month',v['je']['2025']['month'])
    print('  m',{y:(v['m'][y]['n'],v['m'][y]['med']) for y in ['2021','2022','2023','2024','2025','2026']})
    print('  half',v['m']['half'])
