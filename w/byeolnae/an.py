# 별내역 아파트 글(gs/byeolnae_yeok.py)의 실거래 계산 — 2026.10.7
# 자료: w/apt_all.pkl → 경기도 남양주시 별내동만 뽑은 bn.pkl(7,900건 · 아파트 매매 · 2012.3~2026.8 계약 · 해제 거래 없음)
# 셈법: 같은 단지 · 같은 전용면적(㎡ 반올림)을 한 묶음 → 건수와 중앙값 → 두 기간을 견줄 때는 두 기간 모두 2건 이상 팔린 묶음만 → 묶음별 변화율의 중앙값
import pandas as pd, numpy as np, sys
pd.set_option('display.max_rows',900,'display.width',260)
try: d=pd.read_pickle('/home/claude/w/byeolnae/bn.pkl')
except Exception:
    a=pd.read_pickle('/home/claude/w/apt_all.pkl'); d=a[a['시군구'].astype(str).str.contains('남양주시 별내')].copy(); d.to_pickle('/home/claude/w/byeolnae/bn.pkl')
b=d[d['읍면동']=='별내동'].copy()
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float); b['ar']=b['a'].round(0)
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
b['nm']=b['단지명']
NOW=(202603,202608); PRE=(202308,202407); POST=(202408,202507); PK=(202107,202206); LOW=(202210,202309); YA=(202503,202508)
def win(w,x=None):
    x=b if x is None else x
    return x[(x.ym>=w[0])&(x.ym<=w[1])]
def per(w,minn=2):
    g=win(w).groupby(['nm','y','ar'])['p'].agg(['median','size'])
    return g[g['size']>=minn]
def cmp(A,B,minn=2):
    m=per(A,minn).join(per(B,minn),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100
    return m.reset_index()
def band84(x): return x[(x.a>=83.5)&(x.a<85.5)]
if __name__=='__main__':
    n=win(NOW); print('별내동 전체',len(b),'2026.3~8',len(n),'단지',n.nm.nunique())
    # 1. 면적대별 거래
    cut=pd.cut(n.a,[0,60,70,80,86,110,200],labels=['60미만','60~70','70~80','80~86','86~110','110이상']); print(n.groupby(cut,observed=False).agg(k=('p','size'),med=('p','median'),lo=('p','min'),hi=('p','max'),dan=('nm','nunique')).to_string())
    print('전 기간 60㎡ 미만 단지',b[b.a<60].groupby(['nm','ar']).size().to_dict(),'/ 58.5~60.5㎡ 거래',len(b[(b.a>=58.5)&(b.a<60.5)]))
    # 2. 84㎡대 단지별
    x=band84(n); print('84㎡대',len(x),'중앙값',x.p.median(),'단지',x.nm.nunique())
    g=x.groupby(['nm','y']).p.agg(['median','size','min','max']).reset_index().sort_values('median',ascending=False); print(g.to_string())
    print('가격대', pd.cut(x.p,[0,50000,60000,70000,80000,90000,100000,200000],right=False).value_counts().sort_index().to_string())
    print('자이더스타 뺀 84㎡대',len(x[x.nm!='별내자이더스타']),x[x.nm!='별내자이더스타'].p.median(), x[x.nm!='별내자이더스타'].p.min(), x[x.nm!='별내자이더스타'].p.max())
    # 묶음(㎡ 반올림)으로
    g2=n.groupby(['nm','y','ar']).p.agg(['median','size','min','max']).reset_index(); print(g2.to_string())
    # 3. 가장 싸게 · 비싸게 팔린 거래
    print(n.sort_values('p').head(12)[['nm','y','a','p','ym']].to_string()); print(n.sort_values('p').tail(8)[['nm','y','a','p','ym']].to_string())
    print('전체 중앙값',n.p.median(),' 6억 미만',int((n.p<60000).sum()),' 5억 미만',int((n.p<50000).sum()))
    # 4. 별내선 개통(2024.8.10) 앞뒤
    for nmx,A,B in [('개통 전 1년(2023.8~2024.7)→2026.3~8',PRE,NOW),('개통 전 1년→개통 뒤 1년(2024.8~2025.7)',PRE,POST),('2025.3~8→2026.3~8',YA,NOW),('2021.7~2022.6→2026.3~8',PK,NOW),('2022.10~2023.9→2026.3~8',LOW,NOW),('2021.7~2022.6→개통 전 1년',PK,PRE)]:
        m=cmp(A,B); print('==',nmx,'묶음',len(m),'단지',m.nm.nunique(),'건',int(m.size_A.sum()),'→',int(m.size_B.sum()),'변화 중앙값',round(m.c.median(),1),'오른 묶음',int((m.c>0).sum()),'내린',int((m.c<0).sum()),'범위',round(m.c.min(),1),round(m.c.max(),1))
        print(m.sort_values('c').round(1).to_string())
        m3=cmp(A,B,3); print('   3건 이상',len(m3),round(m3.c.median(),1),int((m3.c>0).sum()))
        m84=m[(m.ar>=84)&(m.ar<=85)]; print('   84㎡대만',len(m84),round(m84.c.median(),1),int((m84.c>0).sum())); mL=m[m.ar>=100]; print('   100㎡ 이상',len(mL),round(mL.c.median(),1),int((mL.c>0).sum()))
    # 5. 월별 건수
    print(b[b.ym>=202401].groupby('ym').size().to_string())
    # 6. 해마다 84㎡대
    b['yr']=b.ym//100; print(band84(b).groupby('yr').p.agg(['median','size']).to_string())
    # ── 7. 역까지 직선거리(오픈스트리트맵 좌표 · 2026.6.1 기준 자료 · overpass 10/7 · 단지 테두리의 가운데 → 역 점 · m) ──
    #   (별내역, 별내별가람역). 맞춰 본 것: 쌍용예가 884m ↔ 리치고 「별내역 867m」 · 별내자이더스타 473m ↔ 리치고 「440m」 · 별내아이파크2차 별가람역 406m ↔ 리치고 「별가람역 도보 5분」
    D={'별내자이더스타':(473,2723),'별내역우미린더퍼스트':(839,2643),'쌍용예가':(884,2339),'동익미라벨(1058)':(940,2114),'동익미라벨(1060)':(940,2114),'포스코더샵':(1007,2010),
       '신일유토빌':(1202,2096),'포레나별내':(1249,2607),'신안인스빌':(1495,2182),'KCC스위첸':(1820,1291),'남양주별내리슈빌':(1883,1122),'대원칸타빌':(2188,1000),'모아미래도아파트':(2221,1162),
       '현대아이파크':(2357,653),'유승한내들':(2466,1100),'별내우미린스타포레':(2559,1376),'별내아이파크2차':(2618,406),'별내유승한내들이노스타':(2777,1428),'별내퍼스트포레':(2800,480),
       '별내푸르지오':(2858,1240),'별내별가람역 한라비발디':(3085,279),'남광하우스토리':(3115,1459)}
    assert set(D)==set(b.nm.unique()), set(b.nm.unique())-set(D)
    b['d1']=b.nm.map(lambda k:D[k][0]); b['d2']=b.nm.map(lambda k:D[k][1])
    b['side']=np.where(b.d1<=1500,'별내역 1.5km 안','그 밖(별내별가람역 쪽)')
    n=win(NOW)
    t=n.groupby(['nm','y','d1','d2']).agg(k=('p','size'),amin=('ar','min'),amax=('ar','max'),k84=('a',lambda s:int(((s>=83.5)&(s<85.5)).sum()))).reset_index().sort_values('d1')
    m84=band84(n).groupby('nm').p.median(); t['m84']=t.nm.map(m84); print(t.to_string())
    print(n.groupby('side').agg(k=('p','size'),dan=('nm','nunique'),med=('p','median')).to_string())
    x=band84(n); print(x.groupby('side').agg(k=('p','size'),dan=('nm','nunique'),med=('p','median')).to_string())
    print('84㎡대 1km 안',x[x.d1<=1000].groupby('nm').size().to_dict(),' 1~1.5km',x[(x.d1>1000)&(x.d1<=1500)].groupby('nm').size().to_dict())
    x6=x[(x.p>=60000)&(x.p<70000)]; print('84㎡ 6억대',len(x6),x6.groupby(['nm','d1']).size().sort_values(ascending=False).to_string()); print(' 6억대 가운데 1.5km 안',int((x6.d1<=1500).sum()),' 별가람역이 더 가까운 단지',int((x6.d2<x6.d1).sum()))
    x7=x[(x.p>=70000)&(x.p<80000)]; print('84㎡ 7억대',len(x7),x7.groupby(['nm','d1']).size().sort_values(ascending=False).to_string())
    x5=x[(x.p<60000)]; print('84㎡ 6억 미만',len(x5),x5.groupby(['nm','d1']).size().sort_values(ascending=False).to_string())
    x8=x[(x.p>=80000)&(x.p<100000)]; print('84㎡ 8~9억대',len(x8),x8.groupby(['nm','d1']).size().to_string())
    a6=n[(n.p>=60000)&(n.p<70000)]; print('모든 면적 6억대',len(a6),a6.groupby(['nm','d1','ar']).size().to_string())
    s=n[n.d1<=1500]; print('별내역 1.5km 안 거래',len(s),'가장 싼',s.sort_values('p').head(8)[['nm','a','p','ym']].values.tolist(),' 7억 미만',int((s.p<70000).sum()),' 84㎡대',int(((s.a>=83.5)&(s.a<85.5)).sum()),' 100㎡ 이상',int((s.a>=100).sum()))
    s1=n[n.d1<=1000]; print('1km 안 거래',len(s1),s1.groupby(['nm','ar']).p.agg(['median','size']).to_string(),' 가장 싼',s1.p.min(), s1.sort_values('p').head(4)[['nm','a','p','ym']].values.tolist())
    for nmx,A,B in [('개통 전 1년→2026.3~8',PRE,NOW),('2021.7~2022.6→2026.3~8',PK,NOW),('개통 전 1년→개통 뒤 1년',PRE,POST),('2025.3~8→2026.3~8',YA,NOW)]:
        m=cmp(A,B); m['d1']=m.nm.map(lambda k:D[k][0]); m['d2']=m.nm.map(lambda k:D[k][1]); m['side']=np.where(m.d1<=1500,'별내역 1.5km 안','그 밖')
        print('==',nmx); print(m.groupby('side').agg(med=('c','median'),k=('c','size'),dan=('nm','nunique'),up=('c',lambda s:int((s>0).sum())),nA=('size_A','sum'),nB=('size_B','sum'),lo=('c','min'),hi=('c','max')).round(1).to_string())
        m['s2']=np.where(m.d1<=1000,'1km 안',np.where(m.d1<=1500,'1~1.5km',np.where(m.d2<=700,'별가람역 700m 안','그 밖'))); print(m.groupby('s2').agg(med=('c','median'),k=('c','size'),up=('c',lambda s:int((s>0).sum()))).round(1).to_string())
    # 별내자이더스타 해마다 · 반기마다
    z=b[b.nm=='별내자이더스타']; z=z.assign(h=z.ym.map(lambda v:f'{v//100}{"상" if v%100<=6 else "하"}')); print(z.groupby(['h','ar']).p.agg(['median','size','min','max']).to_string())
    # 84㎡대 1억 500만원 · 6억 900만원과 나란히 둘 숫자
    print('가장 싼 묶음(2건 이상)',n.groupby(['nm','ar']).p.agg(['median','size']).query('size>=2').sort_values('median').head(6).to_string())
    print('전체 570건 최저 5건',n.sort_values('p').head(5)[['nm','a','p','ym']].values.tolist())
    # ── 8. 별내역 1km 안팎(단지 가운데까지 1,010m 안 · 포스코더샵 1,007m 포함) 여섯 단지 ──
    s=n[n.d1<=1010]; print('1km 안팎',len(s),'단지',s.nm.nunique(),sorted(s.nm.unique()),'84㎡대',int(((s.a>=83.5)&(s.a<85.5)).sum()),'99㎡ 넘는',int((s.a>=99).sum()),'7억 미만',int((s.p<70000).sum()),'8억 미만',int((s.p<80000).sum()),'중앙값',s.p.median(),'최저 3',s.sort_values('p').head(3)[['nm','a','p','ym']].values.tolist())
    print(' 자이더스타 뺀 1km 안팎',len(s[s.nm!='별내자이더스타']),s[s.nm!='별내자이더스타'].p.median(),s[s.nm!='별내자이더스타'].a.min())
    print('면적 구성 570:', {'60미만':int((n.a<60).sum()),'70~80':int(((n.a>=70)&(n.a<80)).sum()),'84대':int(((n.a>=83.5)&(n.a<85.5)).sum()),'99넘는':int((n.a>=99).sum())})
    print('70~80㎡',n[(n.a>=70)&(n.a<80)].groupby(['nm','ar','d1']).p.agg(['median','size']).to_string())
    print('전 기간 60㎡ 미만',len(b[b.a<60]),b[b.a<60].groupby('nm').size().to_dict(),'전 기간 60~70',len(b[(b.a>=60)&(b.a<70)]),'자료 기간',b.ym.min(),b.ym.max())
    both=n[(n.d1>1010)&(n.d2>1010)&((n.a>=83.5)&(n.a<85.5))]; print('두 역 모두 1km 넘는 84㎡ 단지',both.groupby('nm').p.agg(['median','size']).to_string())
    print('84㎡ 6억대 비율',round(117/317*100,1),' 60미만 비율',round(16/570*100,1),round(49/570*100,1),round(317/570*100,1),round(188/570*100,1))
    # 별가람역 700m 안 단지 묶음(개통 전 1년 → 2026.3~8)
    m=cmp(PRE,NOW); m['d1']=m.nm.map(lambda k:D[k][0]); m['d2']=m.nm.map(lambda k:D[k][1])
    print(m[m.d2<=700][['nm','ar','median_A','size_A','median_B','size_B','c']].round(1).to_string()); print(m[m.d1<=1010][['nm','ar','median_A','size_A','median_B','size_B','c']].round(1).to_string())
    print('별가람 700m 안',round(m[m.d2<=700].c.median(),1),len(m[m.d2<=700]),int(m[m.d2<=700].size_A.sum()),int(m[m.d2<=700].size_B.sum()),' 별내역 1km 안팎',round(m[m.d1<=1010].c.median(),1),len(m[m.d1<=1010]),int((m[m.d1<=1010].c>0).sum()),int(m[m.d1<=1010].size_A.sum()),int(m[m.d1<=1010].size_B.sum()))
