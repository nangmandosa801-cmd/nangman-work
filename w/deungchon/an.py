# 힐스테이트 등촌역 분양가 글(gs/deungchon.py)의 계산 — 2026.10.7
# 자료: w/apt_all.pkl → 서울 강서구 · 양천구만 뽑은 gs.pkl(아파트 매매 · 2026년 8월 계약분까지) · 해제 거래 제외
# 방법: 같은 단지 · 같은 전용면적(㎡ 반올림)을 한 묶음 → 건수와 중앙값 → 두 기간을 비교할 때는 두 기간 모두 2건 이상 팔린 묶음만 → 묶음별 변화율의 중앙값
# 분양가: 청약홈 입주자모집공고(주택관리번호 2024000688 · 2024.11.25) 공급금액 표의 층별 가구 수 × 공급금액(만원) · 무순위 공고(2025910001 · 2025.1.8)의 남은 79가구
import pandas as pd, numpy as np
pd.set_option('display.max_rows',800,'display.width',260)
W='/home/claude/w/deungchon/'
try: b=pd.read_pickle(W+'gs.pkl')
except Exception:
    d=pd.read_pickle('/home/claude/w/apt_all.pkl'); b=d[(d['광역']=='서울특별시')&(d['시군구'].str.contains('강서구|양천구'))].copy(); b.to_pickle(W+'gs.pkl')
n0=len(b)
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float); b['ar']=b['a'].round(0)
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
b['dong']=b['읍면동']; b['nm']=b['단지명']; b['gu']=b['시군구'].str.split().str[1]
g=b[b.gu=='강서구']
NOW=(202603,202608); PRE=(202408,202410); PRE6=(202405,202410); YA=(202503,202508); PK=(202107,202206)
def win(lo,hi,x=None):
    x=g if x is None else x
    return x[(x.ym>=lo)&(x.ym<=hi)]
def band(lo,hi,x=None):
    x=g if x is None else x
    return x[(x.a>=lo)&(x.a<hi)]
def per(lo,hi,minn=2,x=None):
    q=win(lo,hi,x).groupby(['dong','nm','y','ar'])['p'].agg(['median','size'])
    return q[q['size']>=minn]
def cmp(A,B,minn=2,x=None):
    m=per(*A,minn,x).join(per(*B,minn,x),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100
    return m.reset_index()
def summ(m,by):
    return m.groupby(by).agg(med=('c','median'),k=('c','size'),dan=('nm','nunique'),up=('c',lambda s:(s>0).sum()),nA=('size_A','sum'),nB=('size_B','sum')).round(1)
def age(y): return np.where(y>=2015,'2015후',np.where(y>=2000,'2000~2014','1999전'))
# 일반분양 공급금액(만원 · 가구 수) — 공고문 7~8쪽. 층: 1 · 2 · 3 · 4 · 5 · 6~10 · 11층 이상
S={'59A':[(103800,1),(106100,6),(108400,16),(110600,15),(111700,8),(112900,21),(114000,22)],
   '59B':[(103400,2),(105700,2),(107900,2),(110200,2),(111300,2),(112400,4),(0,0)],
   '84A':[(132200,20),(135000,23),(137900,23),(140800,22),(142200,1),(0,0),(0,0)],
   '84B':[(132400,1),(135300,2),(138200,2),(141000,2),(142500,2),(143900,10),(145400,10)],
   '84C':[(131600,4),(134500,5),(137300,5),(140200,5),(141600,5),(143000,17),(144500,12)]}
# 무순위(2025.1.8 공고) 남은 집 — 층별 가구 수
R={'59A':[0,0,0,0,0,0,0],'59B':[1,0,0,0,1,0,0],'84A':[11,12,13,11,1,0,0],'84B':[1,1,0,0,2,5,5],'84C':[2,2,1,1,2,4,3]}
def wmed(keys):
    w=np.concatenate([np.repeat([p for p,_ in S[k]],[c for _,c in S[k]]) for k in keys]); w=w[w>0]; return len(w),float(np.median(w)),w.min(),w.max()
if __name__=='__main__':
    print('강서 · 양천',n0,'→ 해제 뺀',len(b),'| 강서구',len(g),'| 등촌동',len(g[g.dong=='등촌동']))
    for nm,ks in [('59',['59A','59B']),('84',['84A','84B','84C']),('전체',list(S))]:
        n_,m_,lo,hi=wmed(ks); f=np.sum([[c for _,c in S[k]] for k in ks],axis=0); r=np.sum([R[k] for k in ks],axis=0)
        print('분양가',nm,'가구',n_,'중앙값',m_,'범위',lo,hi,'| 층별(1·2·3·4·5·6~10·11위)',f.tolist(),'5층 아래',int(f[:5].sum()),round(f[:5].sum()/n_*100,1),'4층 아래',int(f[:4].sum()),'| 무순위',int(r.sum()),round(r.sum()/n_*100,1),'무순위 층별',r.tolist(),'5층 아래',int(r[:5].sum()))
    for k in S: print('  ',k,wmed([k]),'무순위',sum(R[k]))
    P59=wmed(['59A','59B'])[1]; P84=wmed(['84A','84B','84C'])[1]; print('P59',P59,'P84',P84)
    # 잔금 30% · 확장비
    print('잔금 30%: 59',P59*0.3,'84',P84*0.3)
    # a. 공고 직전 석 달(2024.8~10) → 2026.3~8 — 비교 단지
    C=[('등촌동','등촌동아이파크'),('가양동','강서한강자이'),('염창동','e편한세상염창'),('염창동','강변힐스테이트'),('염창동','염창1차한화꿈에그린'),('화곡동','강서힐스테이트'),('화곡동','우장산숲아이파크'),('화곡동','우장산아이파크,이편한세상'),('내발산동','우장산힐스테이트'),('마곡동','마곡13단지힐스테이트마스터'),('마곡동','마곡힐스테이트'),('마곡동','마곡엠밸리9단지'),('마곡동','마곡엠밸리8단지'),('등촌동','가양역두산위브'),('등촌동','등촌지와인아파트,비지니스센터')]
    for ar,pr in [(60,P59),(85,P84)]:
        print(f'\n== a. 비교 단지 {ar}㎡ 묶음: 2024.8~10 | 2024.5~10 | 2025.3~8 | 2026.3~8 (중앙값 · 건) · 분양가 중앙값 {pr}')
        for dg,nm_ in C:
            x=g[(g.dong==dg)&(g.nm==nm_)&(g.ar==ar)]
            for yy,xx in x.groupby('y'):
                r=[]
                for (lo,hi) in [PRE,PRE6,YA,NOW]:
                    w=win(lo,hi,xx); r.append((None if not len(w) else int(w.p.median()),len(w)))
                ch=None if not(r[0][0] and r[3][0]) else round((r[3][0]/r[0][0]-1)*100,1)
                print(f'  {dg} {nm_}({yy})',r,'변화%',ch,'| 분양가−그때',None if not r[0][0] else int(pr-r[0][0]),'분양가−지금',None if not r[3][0] else int(pr-r[3][0]))
    for nm_ in ['등촌동아이파크','강서힐스테이트','강서한강자이','마곡13단지힐스테이트마스터','e편한세상염창','우장산숲아이파크']:
        x=g[(g.nm==nm_)&(g.ar.isin([60,85]))&(g.ym>=202408)]
        print(nm_,x.groupby(['y','ar']).agg(n=('p','size')).T.to_dict(), '| 2024.8~10 낱건',win(*PRE,x).sort_values(['ar','ym'])[['y','ar','p','ym']].values.tolist())
    # b. 강서구 전체 — 분양가 중앙값보다 비싸게 팔린 거래
    for nm,lo,hi,pr in [('59',58.5,60.5,P59),('84',83.5,85.5,P84)]:
        for tag,(l2,h2) in [('2024.8~10',PRE),('2026.3~8',NOW)]:
            w=win(l2,h2,band(lo,hi)); w=w.assign(gp=age(w.y)); nw=w[w.y>=2015]
            print(f'\nb. 강서구 {nm}㎡대 {tag} 전체',len(w),'분양가 중앙값보다 비싼',int((w.p>pr).sum()),'| 2015후',len(nw),'비싼',int((nw.p>pr).sum()),'싼',int((nw.p<pr).sum()),'| 동별(전체 · 비싼)',w.assign(hi=w.p>pr).groupby('dong').hi.agg(['size','sum']).T.to_dict())
            print('   2015후 단지별',nw.groupby(['dong','nm','y']).p.agg(['median','size']).round(0).to_dict('index'))
            dd=w[w.dong=='등촌동']; print('   등촌동',len(dd),'비싼',int((dd.p>pr).sum()),'가장 비싼',dd.sort_values('p').tail(3)[['nm','y','a','p','ym']].values.tolist(),'| 지은 해별',dd.assign(gp=age(dd.y)).groupby('gp').size().to_dict())
    # c. 등촌동 안의 새 아파트
    n=win(*NOW,g[g.dong=='등촌동']); print('\nc. 등촌동 2026.3~8',len(n),'지은 해별',pd.Series(age(n.y)).value_counts().to_dict(),'| 2015후 전용 40㎡ 넘는',int(((n.y>=2015)&(n.a>40)).sum()))
    print(n[n.y>=2015].groupby(['nm','y','ar']).p.agg(['median','size']).to_string())
    nn=win(*NOW); print('강서구 2026.3~8',len(nn),'2015후',int((nn.y>=2015).sum()),'동별 전체',nn.groupby('dong').size().to_dict(),'동별 2015후',nn[nn.y>=2015].groupby('dong').size().to_dict())
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        x=band(lo,hi,nn); print(nm,'㎡대 강서구',len(x),'2015후',len(x[x.y>=2015]),'동별 2015후',x[x.y>=2015].groupby('dong').size().to_dict())
    # d. 묶음별 변화율
    for tag,(A,B) in [('2024.8~10 → 2026.3~8',(PRE,NOW)),('2024.5~10 → 2026.3~8',(PRE6,NOW)),('2025.3~8 → 2026.3~8',(YA,NOW)),('2021.7~2022.6 → 2026.3~8',(PK,NOW))]:
        m=cmp(A,B); m['gp']=age(m.y)
        print('\n== d.',tag,'강서구 전체',round(m.c.median(),1),len(m),'오른',int((m.c>0).sum())); print(summ(m,'dong').to_string()); print(summ(m,'gp').to_string())
        if A in (PRE,PRE6): print(m[m.dong=='등촌동'].sort_values('c').round(1).to_string())
    # e. 양천구(목동 쪽) 새 아파트 — 참고
    q=b[b.gu=='양천구']
    for nm_ in ['목동센트럴아이파크위브1단지','목동센트럴아이파크위브2단지','목동센트럴아이파크위브4단지','목동힐스테이트','목동롯데캐슬마에스트로']:
        for ar in (60,85):
            x=q[(q.nm==nm_)&(q.ar==ar)]; r=[(None if not len(w) else int(w.p.median()),len(w)) for w in [win(*PRE,x),win(*NOW,x)]]; print('e.',nm_,ar,r)
    # f. 달마다 강서구 84㎡대 건수
    x=band(83.5,85.5,g[g.ym>=202401]); print(x.groupby('ym').p.agg(['size']).T.to_string())
