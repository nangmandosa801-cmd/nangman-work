# 힐스테이트 메디알레 글(gs/medialle.py)의 실거래 계산 — 2026.10.7
# 자료: w/apt_all.pkl → 서울 은평구만 뽑은 ep.pkl(40,676건 · 아파트 매매 · 2010.1~2026.8 계약 · 해제 거래 제외)
# 셈법: 같은 단지 · 같은 전용면적(㎡ 반올림)을 한 묶음 → 건수와 중앙값 → 두 기간을 견줄 때는 두 기간 모두 2건 이상 팔린 묶음만 → 묶음별 변화율의 중앙값
import pandas as pd, numpy as np, re, sys
pd.set_option('display.max_rows',600,'display.width',260)
try: b=pd.read_pickle('/home/claude/w/medialle/ep.pkl')
except Exception:
    d=pd.read_pickle('/home/claude/w/apt_all.pkl'); b=d[(d['광역']=='서울특별시')&(d['시군구'].str.contains('은평구'))].copy(); b.to_pickle('/home/claude/w/medialle/ep.pkl')
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float); b['ar']=b['a'].round(0)
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
b['dong']=b['읍면동']
# 같은 단지가 동 번호로 나뉘어 적힌 것은 하나로(DMC센트럴자이 1~4단지는 그대로 둠 — 단지가 다름)
b['nm']=b['단지명'].str.replace(r'10[12]동$','',regex=True)
NOW=(202603,202608); PRE=(202312,202411); PRE2=(202401,202411); YA=(202503,202508); PK=(202107,202206)
def band(lo,hi,x=None):
    x=b if x is None else x
    return x[(x.a>=lo)&(x.a<hi)]
def per(lo,hi,minn=2,x=None):
    x=b if x is None else x
    g=x[(x.ym>=lo)&(x.ym<=hi)].groupby(['dong','nm','y','ar'])['p'].agg(['median','size'])
    return g[g['size']>=minn]
def cmp(A,B,minn=2,x=None):
    m=per(*A,minn,x).join(per(*B,minn,x),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100
    return m.reset_index()
def summ(m,by):
    return m.groupby(by).agg(med=('c','median'),k=('c','size'),dan=('nm','nunique'),up=('c',lambda s:(s>0).sum()),nA=('size_A','sum'),nB=('size_B','sum'),lo=('c','min'),hi=('c','max')).round(1)
STN={'대조동','불광동','갈현동'}   # 연신내역(3 · 6호선 · GTX-A) · 불광역(3 · 6호선)을 낀 세 동
if __name__=='__main__':
    n=b[(b.ym>=NOW[0])&(b.ym<=NOW[1])]
    print('은평구 2026.3~8 전체',len(n),'동별',n.groupby('dong').size().to_dict())
    # a. 2015년 이후 지은 단지의 59㎡대(58.5~60.5) · 74㎡대(73.5~76) · 84㎡대(83.5~85.5) 2026.3~8
    for nm,lo,hi in [('59',58.5,60.5),('74',73.5,76.0),('84',83.5,85.5)]:
        x=band(lo,hi,n[n.y>=2015]).groupby(['dong','nm','y'])['p'].agg(['median','size','min','max']).reset_index().sort_values('median',ascending=False)
        print('== 2015후',nm,'㎡대 2026.3~8  거래',int(x['size'].sum()),'단지',len(x)); print(x.to_string())
        y=x[x['size']>=5]; print('   5건 이상 단지',len(y),'중앙값의 중앙값',y['median'].median())
        # 엄격한 묶음(㎡ 반올림)
        z=band(lo,hi,n[n.y>=2015]).groupby(['dong','nm','y','ar'])['p'].agg(['median','size']).reset_index(); print(z[z['size']>=2].sort_values('median',ascending=False).to_string())
    # 은평구 59㎡대 전체(지은 해 무관) 2026.3~8
    x=band(58.5,60.5,n); print('은평 59㎡대 전체',len(x),'중앙값',x.p.median(),'/ 2015후',len(x[x.y>=2015]),x[x.y>=2015].p.median(),'/ 2014전',len(x[x.y<2015]),x[x.y<2015].p.median())
    x=band(83.5,85.5,n); print('은평 84㎡대 전체',len(x),'중앙값',x.p.median(),'/ 2015후',len(x[x.y>=2015]),x[x.y>=2015].p.median())
    for lim in (99830,103430,114140,115060,125650,137820):
        x=band(58.5,60.5,n[n.y>=2015]); print('  59㎡대 2015후 거래 가운데',lim,'이상',int((x.p>=lim).sum()),'/',len(x))
    # 올해 은평구에서 가장 비싸게 팔린 59㎡대 · 84㎡대
    for lo,hi in [(58.5,60.5),(73.5,76.0),(83.5,85.5)]:
        x=band(lo,hi,b[b.ym>=202601]).sort_values('p',ascending=False).head(6); print(x[['dong','nm','y','a','p','ym']].to_string())
    # b. GTX-A 연신내역 개통(2024.12.28) 앞뒤
    b['g']=np.where(b.dong.isin(STN),'역 둘레 세 동',np.where(b.dong=='진관동','진관동','은평 나머지'))
    for nm,A in [('개통 전 1년(2023.12~2024.11)→2026.3~8',PRE),('2024.1~11→2026.3~8',PRE2),('2025.3~8→2026.3~8',YA),('개통 전 1년→2025.3~8',PRE)]:
        B=YA if nm.endswith('2025.3~8') else NOW
        m=cmp(A,B); print('==',nm); print(summ(m,'g' if 'g' in m else m.dong.map(lambda d:'역 둘레 세 동' if d in STN else ('진관동' if d=='진관동' else '은평 나머지'))).to_string())
        print(summ(m,'dong').to_string()); print('은평 전체',round(m.c.median(),1),len(m),int(m.size_A.sum()),int(m.size_B.sum()),int((m.c>0).sum()))
        m['new']=np.where(m.y>=2015,'2015후',np.where(m.y>=2000,'2000~2014','1999전'))
        print(summ(m,'new').to_string())
        m['gg']=m.dong.map(lambda d:'역' if d in STN else '밖')+m.new; print(summ(m,'gg').to_string())
        if A==PRE and B==NOW:
            print(m[m.dong.isin(STN)].sort_values('size_B',ascending=False).round(1).to_string())
            print(m[(m.y>=2015)].sort_values('c').round(1).to_string())
    # MIN 3으로 올렸을 때
    m=cmp(PRE,NOW,3); m['s']=m.dong.isin(STN); print('MIN3',m.groupby('s').c.agg(['median','size']).round(1).to_dict(),round(m.c.median(),1))
    # c. 2021.7~2022.6 값을 넘었는가
    m=cmp(PK,NOW); m['new']=np.where(m.y>=2015,'2015후',np.where(m.y>=2000,'2000~2014','1999전')); m['s']=np.where(m.dong.isin(STN),'역 둘레 세 동','밖')
    print('== 2021.7~2022.6 → 2026.3~8'); print(summ(m,'new').to_string()); print(summ(m,'s').to_string()); print(summ(m,'dong').to_string()); print('은평 전체',round(m.c.median(),1),len(m),int((m.c>0).sum()))
    print(m[m.y>=2015].sort_values('c').round(1).to_string())
    print(m[m.dong.isin(STN)].sort_values('c').round(1).to_string())
    # 대조동 · 불광동 구축과 새 아파트의 값 차이(59㎡대 · 84㎡대 · 2026.3~8)
    for lo,hi in [(58.5,60.5),(83.5,85.5)]:
        x=band(lo,hi,n[n.dong.isin(STN)]); x=x.assign(new=np.where(x.y>=2015,'2015후',np.where(x.y>=2000,'2000~2014','1999전')))
        print(x.groupby('new').p.agg(['median','size']).to_string())
        print(x.groupby(['dong','nm','y']).p.agg(['median','size']).reset_index().sort_values('median',ascending=False).to_string())
    # 월별 건수(역 둘레 세 동 · 은평 전체)
    print(b[b.ym>=202401].groupby(['ym',b.dong.isin(STN)]).size().unstack().to_string())
    # ── 분양(공고 2025.5.9) 직전 석 달과 지금 · 옆 단지 59㎡ · 84㎡ ──
    T=['녹번역e편한세상캐슬','힐스테이트녹번','래미안베라힐즈','힐스테이트녹번역','북한산푸르지오','불광롯데캐슬','북한산힐스테이트7차','백련산에스케이뷰아이파크']
    for ar in (60,85):
        x=b[b.nm.isin(T)&(b.ar==ar)]
        for nm,lo,hi in [('2025.2~4',202502,202504),('2026.3~8',202603,202608)]:
            g=x[(x.ym>=lo)&(x.ym<=hi)].groupby('nm').p.agg(['median','size']); print(ar,nm,{k:(int(v['median']),int(v['size'])) for k,v in g.iterrows()})
    y=b[b.nm.isin(T[:3])&(b.ar==60)]
    for nm,lo,hi in [('2025.2~4',202502,202504),('2026.3~8',202603,202608)]:
        z=y[(y.ym>=lo)&(y.ym<=hi)]; print('녹번역 세 곳 59 합침',nm,len(z),z.p.median())
    # 일반분양 공급금액을 가구 수대로 세운 한가운데(입주자모집공고 공급금액 표 · 만원)
    S={'59':[(103430,3),(106800,11),(109050,15),(110180,15),(112430,48),(105010,5),(108430,15),(110710,15),(111850,15),(114140,48),(100650,1),(103930,1),(106120,1),(107210,1),(109400,5),(111150,1),(99830,4),(103080,5),(105250,5),(106340,5),(108510,20),(101350,1),(104650,1),(106860,1),(107960,1),(110160,4),(104270,7),(107670,10),(109930,10),(111070,10),(113330,32),(105850,1),(109310,1),(111610,1),(112760,1),(115060,3)],
       '74':[(127320,6),(131480,8),(134240,9),(129260,11),(133480,13),(136290,6),(125650,2),(129750,2),(132480,3),(127570,1),(131730,3),(134500,3),(130930,3),(133690,3),(135750,1),(137820,2)],
       '51':[(86770,3),(89590,4),(91480,4),(92420,4),(94310,20),(95820,11),(88090,2),(90960,2),(92870,2),(93830,2),(95750,10),(97280,6),(86270,1),(89080,1),(90960,1),(91890,1),(93770,5),(95270,5)]}
    for k,v in S.items():
        w=np.repeat([p for p,_ in v],[c for _,c in v]); print('분양가',k,'가구',len(w),'한가운데',np.median(w),'범위',w.min(),w.max())
    n=b[(b.ym>=NOW[0])&(b.ym<=NOW[1])]; x=band(58.5,60.5,n[n.y>=2015]); print('은평 2015후 59㎡대',len(x),'가운데 110710 넘는 거래',int((x.p>110710).sum()),'115060 넘는',int((x.p>115060).sum()))
    x=band(58.5,60.5,n[n.dong.isin(STN)]); print('세 동 59㎡대',len(x),'2015후',int((x.y>=2015).sum()),'110710 넘는',int((x.p>110710).sum()),'가장 비싼',x.p.max(), x.sort_values('p').tail(3)[['nm','p','ym']].values.tolist())
    x=band(83.5,85.5,n[n.dong.isin(STN)]); print('세 동 84㎡대',len(x),'2015후',int((x.y>=2015).sum()),'가장 비싼', x.sort_values('p').tail(3)[['nm','p','ym']].values.tolist())
    print('세 동 2026.3~8 전체',len(n[n.dong.isin(STN)]),'2015후',len(n[n.dong.isin(STN)&(n.y>=2015)]),'그 가운데 전용 40㎡ 넘는',len(n[n.dong.isin(STN)&(n.y>=2015)&(n.a>40)]))
    print(n[n.dong.isin(STN)&(n.y>=2015)].groupby(['nm','ar']).size().to_string())
