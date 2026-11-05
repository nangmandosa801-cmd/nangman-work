import pandas as pd, json, numpy as np
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m=pd.read_pickle('/home/claude/rtn/MK_2021_2026.pkl'); m=m[m['해제사유발생일']=='-'].copy()
m['a']=m['전용면적(㎡)'].astype(float); m['p']=num(m['거래금액(만원)']); m['y']=m['계약년월'].str[:4]; m['dong']=m['시군구'].str.split().str[2]; m['b']=pd.to_numeric(m['건축년도'],errors='coerce')
r=pd.read_pickle('/home/claude/rtn/RK_2024_2026.pkl').copy()
r['a']=r['전용면적(㎡)'].astype(float); r['dep']=num(r['보증금(만원)']); r['rent']=num(r['월세금(만원)']); r['ym']=r['계약년월'].astype(int); r['mo']=r['계약년월'].str[4:].astype(int); r['dong']=r['시군구'].str.split().str[2]
r['start']=r['계약기간'].str[:6]; r['smo']=pd.to_numeric(r['start'].str[4:],errors='coerce')
PAIRS=[('강남구','대치동',['세곡동','자곡동','율현동'],'세곡 · 자곡 · 율현'),('양천구','목동',['신월동'],'신월동'),('노원구','중계동',['하계동'],'하계동'),('서초구','반포동',['방배동'],'방배동')]
def f84(d): return d[(d.a>=83)&(d.a<=86)]
out={}
for gu,hk,nh,nhlab in PAIRS:
    for lab,dongs in [(hk,[hk]),(nhlab,nh)]:
        dr=f84(r[r.dong.isin(dongs)&r['시군구'].str.contains(gu)]); dr=dr[(dr.rent==0)&(dr['계약구분']=='신규')]
        o={}
        # 창 W1 2024-11~2025-10, W2 2025-11~2026-10 ; 11~1월 몫
        for wn,(a,b) in {'W1':(202411,202510),'W2':(202511,202610)}.items():
            w=dr[(dr.ym>=a)&(dr.ym<=b)]; n=len(w); k=int(w.mo.isin([11,12,1]).sum())
            o[wn]={'n':int(n),'ndj':k,'share':round(k/n*100,1) if n else None,'month':{int(x):int(v) for x,v in w.groupby('ym').size().items()}}
        # 2025년 계약 중 입주(계약 시작) 2~3월 몫
        for y in ['2024','2025']:
            w=dr[dr['계약년월'].str[:4]==y]; n=len(w); k=int(w.smo.isin([2,3]).sum()); o[f'start23_{y}']={'n':int(n),'k':k,'share':round(k/n*100,1) if n else None,'smo':{int(x):int(v) for x,v in w.groupby('smo').size().items()}}
        # 같은 단지 비율 (매매 84)
        dm=f84(m[m.dong.isin(dongs)&m['시군구'].str.contains(gu)])
        g=dm.groupby(['단지명','y']).agg(n=('p','size'),med=('p','median')).reset_index()
        piv=g.pivot(index='단지명',columns='y',values='med'); cnt=g.pivot(index='단지명',columns='y',values='n').fillna(0)
        ok=piv[(cnt.get('2021',0)>=3)&(cnt.get('2023',0)>=2)&(cnt.get('2026',0)>=2)]
        o['same']={'n_danji':int(len(ok)),'r2321':round(float(((ok['2023']/ok['2021'])).median()*100-100),1) if len(ok) else None,'r2621':round(float(((ok['2026']/ok['2021'])).median()*100-100),1) if len(ok) else None,
                   'list':{i:[int(cnt.loc[i,'2021']),float(row['2021']),float(row['2023']),float(row['2026'])] for i,row in ok.iterrows()}}
        # 전세가율 2026 (동 중앙값) · 같은 단지 중앙값
        je26=dr[dr.ym>=202601]; m26=dm[dm.y=='2026']
        o['ratio26']=round(float(je26.dep.median())/float(m26.p.median())*100,1)
        jg=je26.groupby('단지명').agg(jn=('dep','size'),jmed=('dep','median')); mg=m26.groupby('단지명').agg(mn=('p','size'),mmed=('p','median'))
        jj=jg.join(mg,how='inner'); jj=jj[(jj.jn>=3)&(jj.mn>=2)]; jj['ratio']=jj.jmed/jj.mmed*100
        o['ratio26_same']={'n':int(len(jj)),'med':round(float(jj.ratio.median()),1) if len(jj) else None,'list':{i:[int(x.jn),float(x.jmed),int(x.mn),float(x.mmed),round(float(x.ratio),1)] for i,x in jj.iterrows()}}
        out[f'{gu}|{lab}']=o
json.dump(out,open('ana2.json','w'),ensure_ascii=False,indent=1)
for k,v in out.items():
    print('==',k)
    for wn in ['W1','W2']: print('  ',wn,v[wn]['n'],v[wn]['ndj'],v[wn]['share'])
    for y in ['2024','2025']: print('   start23',y,v[f'start23_{y}']['n'],v[f'start23_{y}']['k'],v[f'start23_{y}']['share'],v[f'start23_{y}']['smo'])
    print('   same',v['same']['n_danji'],v['same']['r2321'],v['same']['r2621'])
    for i,x in v['same']['list'].items(): print('      ',i,x)
    print('   ratio26',v['ratio26'],'same',v['ratio26_same']['n'],v['ratio26_same']['med'])
    for i,x in v['ratio26_same']['list'].items(): print('      ',i,x)
