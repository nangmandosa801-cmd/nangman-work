import pandas as pd, json, numpy as np
R='/home/claude/rtn/'
M=pd.concat([pd.read_pickle(R+'MG_2021_2024_anyang.pkl'),pd.read_pickle(R+'M2025.pkl'),pd.read_pickle(R+'M2026.pkl')],ignore_index=True)
M=M[M['시군구'].str.contains('안양시 동안구')].copy()
M=M[(M['해제사유발생일']=='-')&(M['거래유형']!='직거래')]
M['a']=M['전용면적(㎡)'].astype(float); M['p']=M['거래금액(만원)'].str.replace(',','').astype(int); M['y']=M['계약년월'].str[:4]; M['nm']=M['단지명'].str.replace(' ','')
Rt=pd.concat([pd.read_pickle(R+'RG_2024_2025_anyang.pkl'),pd.read_pickle(R+'R2026.pkl')],ignore_index=True)
Rt=Rt[Rt['시군구'].str.contains('안양시 동안구')].copy()
Rt['a']=Rt['전용면적(㎡)'].astype(float); Rt['d']=Rt['보증금(만원)'].str.replace(',','').astype(int); Rt['w']=Rt['월세금(만원)'].str.replace(',','').astype(int); Rt['y']=Rt['계약년월'].str[:4]; Rt['m']=Rt['계약년월'].str[4:].astype(int); Rt['nm']=Rt['단지명'].str.replace(' ','')
Rt['start']=Rt['계약기간'].str[:6]
Rt=Rt[(Rt['전월세구분']=='전세')&(Rt['w']==0)]
G={
 '귀인현대홈타운80':(['귀인마을현대홈타운'],(79,82)),
 '향촌롯데85':(['향촌롯데'],(83,86)),
 '향촌현대4차85':(['향촌마을현대4차'],(83,86)),
 '향촌현대5차85':(['향촌마을현대5차'],(83,86)),
 '향촌3단지85':(['향촌롯데','향촌마을현대4차','향촌마을현대5차'],(83,86)),
 '호계1차현대홈타운85':(['호계1차현대홈타운'],(83,86)),
 '호계2차현대홈타운85':(['호계2차현대홈타운'],(83,86)),
 '호계현대홈타운85':(['호계1차현대홈타운','호계2차현대홈타운'],(83,86)),
 '비산삼성래미안85':(['삼성래미안'],(83,86)),
 '비산더포레스트힐85':(['더포레스트힐'],(83,86)),
 '무궁화85':(['무궁화태영','무궁화건영캐스빌','무궁화경남','무궁화금호','무궁화코오롱','무궁화진흥','무궁화효성','무궁화한양'],(83,86)),
 '관악85':(['관악','관악부영4'],(83,86)),
 '은하수85':(['은하수벽산','은하수청구','은하수신성'],(83,86)),
 '한가람85':(['한가람(삼성)','한가람(두산)','한가람(한양)'],(83,86)),
 '초원85':(['초원마을대림','초원한양','초원LG','초원마을대원','초원성원'],(83,86)),
 '귀인현대홈타운56':(['귀인마을현대홈타운'],(55,58)),
 '향촌3단지60':(['향촌롯데','향촌마을현대4차','향촌마을현대5차'],(58,61)),
 '호계2차현대홈타운60':(['호계2차현대홈타운'],(58,61)),
 '비산삼성래미안60':(['삼성래미안'],(58,61)),
 '무궁화60':(['무궁화태영','무궁화경남','무궁화금호','무궁화효성','무궁화한양','무궁화코오롱'],(58,61)),
 '관악59':(['관악','관악부영4'],(58,61)),
 '공작60':(['공작아파트','공작성일'],(58,61)),
}
def med(s): return int(s.median()) if len(s) else None
out={}
for k,(nms,(lo,hi)) in G.items():
    m=M[M['nm'].isin(nms)&(M['a']>=lo)&(M['a']<=hi)]
    r=Rt[Rt['nm'].isin(nms)&(Rt['a']>=lo)&(Rt['a']<=hi)]
    d={'sale':{},'rent':{}}
    for y in ['2021','2022','2023','2024','2025','2026']:
        s=m[m['y']==y]['p']; d['sale'][y]={'med':med(s),'n':len(s)}
    # 2021 H2
    s=m[(m['계약년월']>='202107')&(m['계약년월']<='202112')]['p']; d['sale']['2021H2']={'med':med(s),'n':len(s)}
    # monthly max median in 2021
    for y in ['2024','2025','2026']:
        rr=r[r['y']==y]; new=rr[rr['계약구분']=='신규']; ren=rr[rr['계약구분']=='갱신']
        d['rent'][y]={'new_med':med(new['d']),'new_n':len(new),'ren_med':med(ren['d']),'ren_n':len(ren),'all_n':len(rr)}
    # 2024~2025 new: 1~2월 계약 몫, 2월 입주 몫
    nn=r[(r['y'].isin(['2024','2025']))&(r['계약구분']=='신규')]
    d['jan_feb']={'n':len(nn),'jf':int(((nn['m']==1)|(nn['m']==2)).sum()),'feb_in':int((nn['start'].str[4:]=='02').sum()),'feb_mar_in':int(nn['start'].str[4:].isin(['02','03']).sum())}
    # 갱신 비율 2025
    r25=r[r['y']=='2025']; d['renew_share_2025']={'n':len(r25),'ren':int((r25['계약구분']=='갱신').sum())}
    d['n_all']=len(m)
    out[k]=d
json.dump(out,open('ana.json','w'),ensure_ascii=False,indent=1)
for k,d in out.items():
    print(k,{y:(v['med'],v['n']) for y,v in d['sale'].items()})
    print('   rent',{y:(v['new_med'],v['new_n'],v['ren_med'],v['ren_n']) for y,v in d['rent'].items()},'jf',d['jan_feb'],'ren25',d['renew_share_2025'])
