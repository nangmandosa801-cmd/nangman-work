import pandas as pd, json, numpy as np
def num(s): return pd.to_numeric(s.astype(str).str.replace(',',''),errors='coerce')
m=pd.concat([pd.read_pickle('/home/claude/rtn/M2025.pkl'),pd.read_pickle('/home/claude/rtn/M2026.pkl')],ignore_index=True)
m=m[m['해제사유발생일']=='-'].copy(); m['a']=m['전용면적(㎡)'].astype(float); m['p']=num(m['거래금액(만원)']); m['y']=m['계약년월'].str[:4]
d=m[m['시군구']=='서울특별시 강남구 대치동']
r=pd.read_pickle('/home/claude/rtn/R2026.pkl'); r=r[r['시군구']=='서울특별시 강남구 대치동'].copy()
r['a']=r['전용면적(㎡)'].astype(float); r['dep']=num(r['보증금(만원)']); r['rent']=num(r['월세금(만원)'])
D={'래미안대치팰리스':'래미안대치팰리스','대치아이파크':'대치아이파크','대치SKVIEW':'대치SKVIEW','은마':'은마','선경1차(1동-7동)':'선경1차','선경2차(8동-12동)':'선경2차','대치우성아파트1동,2동,3동,5동,6동,7동':'대치우성1차','한보미도맨션1':'한보미도맨션1','한보미도맨션2':'한보미도맨션2','대치삼성':'대치삼성','대치현대':'대치현대','쌍용대치아파트1동,2동,3동,5동,6동':'쌍용대치1차','쌍용대치2':'쌍용대치2차','대치르엘':'대치르엘','현대1':'현대1차','동부센트레빌':'동부센트레빌','개포우성1':'개포우성1차','개포우성2':'개포우성2차','대치푸르지오써밋':'대치푸르지오써밋'}
out={}
def rng(lo,hi): return lambda a:(a>=lo)&(a<=hi)
for k,nm in D.items():
    dd=d[d['단지명']==k]; rr=r[r['단지명']==k]
    for lab,f in [('84',rng(83,86)),('76',rng(76,77))]:
        if lab=='76' and k!='은마': continue
        x=dd[f(dd.a)]; q=rr[f(rr.a)]
        row={'건축':dd['건축년도'].iloc[0] if len(dd) else None}
        for y in ['2025','2026']:
            xx=x[x.y==y]; row[f'm{y}_n']=int(len(xx)); row[f'm{y}_med']=float(xx.p.median()) if len(xx) else None
            if len(xx): row[f'm{y}_last']=xx.sort_values(['계약년월','계약일']).iloc[-1][['계약년월','계약일','p','층']].tolist()
        je=q[(q.rent==0)]; new=je[je['계약구분']=='신규']; ren=je[je['계약구분']=='갱신']
        row['je_all']=int(len(je)); row['je_new_n']=int(len(new)); row['je_new_med']=float(new.dep.median()) if len(new) else None; row['je_ren_med']=float(ren.dep.median()) if len(ren) else None
        ws=q[q.rent>0]; row['rent_n']=int(len(ws)); row['lease_n']=int(len(q)); row['rent_share']=round(len(ws)/len(q)*100,1) if len(q) else None
        wn=ws[ws['계약구분']=='신규']; row['rent_new_n']=int(len(wn)); row['rent_new_dep_med']=float(wn.dep.median()) if len(wn) else None; row['rent_new_rent_med']=float(wn.rent.median()) if len(wn) else None
        row['rent_dep_med']=float(ws.dep.median()) if len(ws) else None; row['rent_rent_med']=float(ws.rent.median()) if len(ws) else None
        if row['m2026_med'] and row['je_new_med']: row['ratio']=round(row['je_new_med']/row['m2026_med']*100,1)
        out[f'{nm}_{lab}']=row
# 대치동 전체 84
x=d[rng(83,86)(d.a)]; q=r[rng(83,86)(r.a)]
tot={}
for y in ['2025','2026']:
    xx=x[x.y==y]; tot[f'm{y}_n']=int(len(xx)); tot[f'm{y}_med']=float(xx.p.median())
tot['lease_n']=int(len(q)); tot['rent_n']=int((q.rent>0).sum()); tot['rent_share']=round((q.rent>0).mean()*100,1)
je=q[q.rent==0]; tot['je_new_med']=float(je[je['계약구분']=='신규'].dep.median())
ws=q[(q.rent>0)&(q['계약구분']=='신규')]; tot['rent_new_dep_med']=float(ws.dep.median()); tot['rent_new_rent_med']=float(ws.rent.median()); tot['rent_new_n']=int(len(ws))
# 월세 보증금 구간
tot['rent_dep_bins']={str(b):int(c) for b,c in pd.cut(ws.dep,[0,30000,50000,100000,200000,1e9]).value_counts().sort_index().items()}
tot['rent_rent_bins']={str(b):int(c) for b,c in pd.cut(ws.rent,[0,100,200,300,400,500,1e9]).value_counts().sort_index().items()}
out['_대치동84']=tot
# 월별 매매 건수 2026
out['_m2026_month']=x[x.y=='2026'].groupby('계약년월').size().to_dict()
out['_m2025_month']=x[x.y=='2025'].groupby('계약년월').size().to_dict()
# 반기별 중앙값
x2=x.copy(); x2['h']=x2['계약년월'].apply(lambda s: s[:4]+('H1' if int(s[4:])<=6 else 'H2'))
out['_half']={h:[int(len(g)),float(g.p.median())] for h,g in x2.groupby('h')}
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=1,default=str)
for k,v in out.items(): print(k,v)
