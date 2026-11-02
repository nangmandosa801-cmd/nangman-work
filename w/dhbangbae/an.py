# 디에이치 방배 분양가 글(gs/dhbangbae2.py)의 계산 — 2026.10.7
# 자료: w/apt_all.pkl → 서울 서초구만 뽑은 sc.pkl(52,671건 · 아파트 매매 · 2010.1~2026.8 계약) · 해제 거래 제외
# 셈법: 같은 단지 · 같은 전용면적(㎡ 반올림)을 한 묶음 → 건수와 중앙값 → 두 기간을 견줄 때는 두 기간 모두 2건 이상 팔린 묶음만 → 묶음별 변화율의 중앙값
# 분양가: 청약홈 입주자모집공고(주택관리번호 2024000412 · 2024.8.16) 공급금액 표의 층별 가구 수 × 공급금액(만원)
import pandas as pd, numpy as np
pd.set_option('display.max_rows',800,'display.width',260)
try: b=pd.read_pickle('/home/claude/w/dhbangbae/sc.pkl')
except Exception:
    d=pd.read_pickle('/home/claude/w/apt_all.pkl'); b=d[(d['광역']=='서울특별시')&(d['시군구'].str.contains('서초구'))].copy(); b.to_pickle('/home/claude/w/dhbangbae/sc.pkl')
n0=len(b)
b=b[b['해제사유발생일'].astype(str).str.strip().isin(['','-','nan','None'])].copy()
b['y']=b['건축년도'].astype(int); b['ym']=b['계약년월'].astype(int)
b['a']=b['전용면적(㎡)'].astype(float); b['ar']=b['a'].round(0)
b['p']=b['거래금액(만원)'].astype(str).str.replace(',','').astype(float)
b['dong']=b['읍면동']; b['nm']=b['단지명']
NOW=(202603,202608); PRE=(202405,202407); PK=(202107,202206); YA=(202503,202508)
def win(lo,hi,x=None):
    x=b if x is None else x
    return x[(x.ym>=lo)&(x.ym<=hi)]
def band(lo,hi,x=None):
    x=b if x is None else x
    return x[(x.a>=lo)&(x.a<hi)]
def per(lo,hi,minn=2,x=None):
    g=win(lo,hi,x).groupby(['dong','nm','y','ar'])['p'].agg(['median','size'])
    return g[g['size']>=minn]
def cmp(A,B,minn=2,x=None):
    m=per(*A,minn,x).join(per(*B,minn,x),lsuffix='_A',rsuffix='_B',how='inner'); m['c']=(m.median_B/m.median_A-1)*100
    return m.reset_index()
def summ(m,by):
    return m.groupby(by).agg(med=('c','median'),k=('c','size'),dan=('nm','nunique'),up=('c',lambda s:(s>0).sum()),nA=('size_A','sum'),nB=('size_B','sum'),lo=('c','min'),hi=('c','max')).round(1)
def age(y): return np.where(y>=2015,'2015후',np.where(y>=2000,'2000~2014','1999전'))
# 일반분양 공급금액(만원 · 가구 수) — 공고문 6~8쪽
S={'59A':[(155330,3),(160510,18),(162230,12),(165680,33)],
   '59B':[(151440,3),(156480,6),(158170,4),(161530,11),(164900,26),(168260,60),(170790,14)],
   '59C':[(160500,2),(162230,2),(165680,5),(169130,6),(172580,10)],
   '84A':[(199020,24),(205660,38),(207870,37),(212290,77),(216710,156),(221130,265),(224450,62)],
   '84B':[(196030,5),(202560,5),(204740,6),(209100,12),(213450,24),(217810,60),(221080,60),(224350,14)],
   '84C':[(193950,2),(200410,5),(202570,5),(206880,10),(211190,20),(215500,45),(218730,23),(221960,1)],
   '101A':[(235800,18),(243660,19),(246280,9)],
   '101B':[(229980,2),(237640,2),(240190,1),(245250,4),(250360,3)],
   '114A':[(276250,6)],
   '114B':[(260870,4),(263670,2),(269280,3)]}
# 층별 가구 수(1층 · 2층 · 3층 · 4~5층 · 6~9층 · 10~19층 · 20~29층 · 30층 이상)
FL={'59A':[3,18,12,33,0,0,0,0],'59B':[3,6,4,11,26,60,14,0],'59C':[0,2,2,5,6,10,0,0],
    '84A':[24,38,37,77,156,265,62,0],'84B':[5,5,6,12,24,60,60,14],'84C':[2,5,5,10,20,45,23,1],
    '101A':[18,19,9,0,0,0,0,0],'101B':[2,2,1,4,3,0,0,0],'114A':[0,0,0,6,0,0,0,0],'114B':[0,4,2,3,0,0,0,0]}
def wmed(keys):
    w=np.concatenate([np.repeat([p for p,_ in S[k]],[c for _,c in S[k]]) for k in keys]); return len(w),np.median(w),w.min(),w.max()
if __name__=='__main__':
    print('서초구',n0,'→ 해제 뺀',len(b),'방배동',len(b[b.dong=='방배동']))
    for g,ks in [('59',['59A','59B','59C']),('84',['84A','84B','84C']),('101',['101A','101B']),('114',['114A','114B'])]:
        n_,m_,lo,hi=wmed(ks); f=np.sum([FL[k] for k in ks],axis=0)
        print('분양가',g,'가구',n_,'중앙값',m_,'범위',lo,hi,'층별',f.tolist(),'5층 아래',int(f[:4].sum()),round(f[:4].sum()/n_*100,1),'10층 위',int(f[5:].sum()),round(f[5:].sum()/n_*100,1),'20층 위',int(f[6:].sum()))
    for k in S: print('  ',k,wmed([k]))
    allf=np.sum(list(FL.values()),axis=0); print('일반분양 전체 층별',allf.tolist(),allf.sum(),'5층 아래',allf[:4].sum(),'20층 위',allf[6:].sum())
    P59=wmed(['59A','59B','59C'])[1]; P84=wmed(['84A','84B','84C'])[1]
    bb=b[b.dong=='방배동']; n=win(*NOW,bb)
    print('\n== 방배동 2015년 뒤 지은 단지(자료의 건축년도) 전체 건수'); print(bb[bb.y>=2015].groupby(['nm','y']).agg(n=('p','size'),amin=('a','min'),amax=('a','max'),first=('ym','min')).to_string())
    # a. 분양 직전 석 달(2024.5~7)과 2026.3~8 — 방배동 단지별 59㎡ · 84㎡
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        x=band(lo,hi,bb)
        A=win(*PRE,x).groupby(['nm','y']).p.agg(['median','size']); B=win(*NOW,x).groupby(['nm','y']).p.agg(['median','size'])
        m=A.join(B,lsuffix='_A',rsuffix='_B',how='outer'); m['c']=(m.median_B/m.median_A-1)*100
        print(f'\n== a. 방배동 {nm}㎡대 단지별 2024.5~7 → 2026.3~8'); print(m.sort_values('median_B',ascending=False).round(1).to_string())
        for tag,(l2,h2) in [('2024.5~7',PRE),('2026.3~8',NOW)]:
            w=win(l2,h2,x); w=w.assign(g=age(w.y)); print('  ',tag,'전체',len(w),w.p.median(),'| 지은 해별',w.groupby('g').p.agg(['median','size']).to_dict('index'))
            pr=P59 if nm=='59' else P84
            print('     분양가 중앙값',pr,'보다 비싼 거래',int((w.p>pr).sum()),'/',len(w),'| 가장 비싼',w.sort_values('p').tail(3)[['nm','y','a','p','ym']].values.tolist())
    # 2024.2~7(여섯 달)로 넓혀도 같은지
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        x=win(202402,202407,band(lo,hi,bb)); print('  2024.2~7',nm,x.groupby(['nm','y']).p.agg(['median','size']).query('size>=2').round(0).to_dict('index'))
    # b. 방배동 안의 새 아파트와 구축
    print('\n== b. 방배동 2026.3~8 전체',len(n),'| 2015후',int((n.y>=2015).sum()),'| 2015후 전용 40㎡ 넘는',int(((n.y>=2015)&(n.a>40)).sum()),'| 지은 해별',n.assign(g=age(n.y)).groupby('g').size().to_dict())
    print(n[n.y>=2015].groupby(['nm','y','ar']).p.agg(['median','size']).to_string())
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        x=band(lo,hi,n); x=x.assign(g=age(x.y)); print(nm,'㎡대',len(x),x.groupby('g').p.agg(['median','size','min','max']).to_string())
        print(x.groupby(['nm','y']).p.agg(['median','size']).sort_values('median',ascending=False).to_string())
    print('방배동 해마다 건수',bb.groupby(bb.ym//100).size().tail(8).to_dict(),'| 2015후',bb[bb.y>=2015].groupby(bb.ym//100).size().tail(8).to_dict())
    # c. 방배 · 반포 · 서초 · 잠원 새 아파트
    D4=['방배동','반포동','서초동','잠원동']; n4=win(*NOW,b[b.dong.isin(D4)])
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        x=band(lo,hi,n4); x=x.assign(g=age(x.y))
        print(f'\n== c. {nm}㎡대 2026.3~8 동 × 지은 해'); print(x.groupby(['dong','g']).p.agg(['median','size']).unstack(0).to_string())
        print(x[x.y>=2015].groupby(['dong','nm','y']).p.agg(['median','size']).sort_values('median',ascending=False).to_string())
        pr=P59 if nm=='59' else P84
        print('   서초구 네 동 2015후 거래 가운데 분양가 중앙값보다 싼 거래',int((x[x.y>=2015].p<pr).sum()),'/',len(x[x.y>=2015]),'| 동별',x[x.y>=2015].assign(lo=lambda t:t.p<pr).groupby('dong').lo.agg(['sum','size']).to_dict('index'))
    for tag,(A,B) in [('2021.7~2022.6 → 2026.3~8',(PK,NOW)),('2025.3~8 → 2026.3~8',(YA,NOW)),('2024.5~7 → 2026.3~8',(PRE,NOW))]:
        m=cmp(A,B,x=b[b.dong.isin(D4)]); m['g']=age(m.y)
        print('\n==',tag); print(summ(m,'dong').to_string()); print(summ(m,'g').to_string()); print(summ(m,['dong','g']).to_string()); print('네 동 전체',round(m.c.median(),1),len(m),int((m.c>0).sum()))
        if A==PK: print(m[m.dong=='방배동'].sort_values('c').round(1).to_string())
        if A==PRE: print(m[(m.dong=='방배동')].sort_values('c').round(1).to_string())
    # 서초구 전체 2021.7~2022.6 → 2026.3~8
    m=cmp(PK,NOW); print('\n서초구 전체 2021.7~22.6 → 2026.3~8',round(m.c.median(),1),len(m),int((m.c>0).sum()),summ(m,'dong').to_string())
    # 방배동 달마다 건수 · 84㎡대 중앙값
    print(bb[bb.ym>=202401].groupby('ym').agg(n=('p','size')).T.to_string())
    x=band(83.5,85.5,bb[bb.ym>=202401]); print(x.groupby('ym').p.agg(['median','size']).T.to_string())
    # ── 덧붙임: 서초구 전체(여덟 동) 2015년 뒤 지은 집과 분양가 중앙값 · 방배동 새 아파트의 세 기간 ──
    nn=win(*NOW)
    for nm,lo,hi,pr in [('59',58.5,60.5,P59),('84',83.5,85.5,P84)]:
        x=band(lo,hi,nn[nn.y>=2015]); print(f'\n서초구 전체 2015후 {nm}㎡대 2026.3~8',len(x),'중앙값',x.p.median(),'| 분양가 중앙값',pr,'보다 싼',int((x.p<pr).sum()),x[x.p<pr][['dong','nm','y','a','p','ym']].values.tolist(),'| 동별 건수',x.groupby('dong').size().to_dict())
        hi_=max(p for k in S if k.startswith(nm) for p,_ in S[k]); print('   가장 비싼 분양가',hi_,'보다 싼',int((x.p<hi_).sum()))
        x=band(lo,hi,nn); print(f'   서초구 전체 {nm}㎡대(지은 해 무관)',len(x),'분양가 중앙값보다 싼',int((x.p<pr).sum()))
        x=band(lo,hi,win(*PRE)); x2=x[x.y>=2015]; print(f'   2024.5~7 서초구 전체 {nm}㎡대',len(x),'2015후',len(x2),x2.p.median(),'분양가 중앙값보다 싼 2015후',int((x2.p<pr).sum()),'| 네 동 2015후',len(x2[x2.dong.isin(D4)]),int((x2[x2.dong.isin(D4)].p<pr).sum()), x2[x2.dong.isin(D4)].groupby('dong').p.agg(['median','size']).to_dict('index'))
    for nm_ in ['방배그랑자이','방배아트자이','서리풀e편한세상','롯데캐슬아르떼','방배 서리풀 그랑블','방배1차현대홈타운','임광']:
        for ar in (60,85):
            x=bb[(bb.nm==nm_)&(bb.ar==ar)]
            r=[(t,int(len(w)),(None if not len(w) else int(w.p.median()))) for t,w in [('24.5~7',win(*PRE,x)),('24.8~25.2',win(202408,202502,x)),('25.3~8',win(*YA,x)),('25.9~26.2',win(202509,202602,x)),('26.3~8',win(*NOW,x))]]
            print(nm_,ar,r)
    x=band(83.5,85.5,bb[(bb.nm=='방배그랑자이')&(bb.ym>=202401)]).sort_values('ym'); print(x[['a','p','ym']].values.tolist())
    x=band(83.5,85.5,bb[(bb.nm=='방배아트자이')&(bb.ym>=202401)]).sort_values('ym'); print(x[['a','p','ym']].values.tolist())
    x=band(58.5,60.5,bb[(bb.nm=='방배아트자이')&(bb.ym>=202401)]).sort_values('ym'); print(x[['a','p','ym']].values.tolist())
    # 방배동 84㎡대 전체 · 2015후: 세 기간
    for nm,lo,hi in [('59',58.5,60.5),('84',83.5,85.5)]:
        for t,(a_,b_) in [('24.5~7',PRE),('25.3~8',YA),('26.3~8',NOW)]:
            w=win(a_,b_,band(lo,hi,bb)); print(nm,t,'방배 전체',len(w),w.p.median(),'2015후',len(w[w.y>=2015]),w[w.y>=2015].p.median())
    # 2015후 묶음만 따로: 2024.5~7 → 2026.3~8 네 동
    m=cmp(PRE,NOW,x=b[b.dong.isin(D4)&(b.y>=2015)&(b.a>=58.5)&(b.a<85.5)]); print(m.sort_values(['dong','c']).round(1).to_string())
    # 방배그랑자이 · 방배아트자이 84㎡ 최근 1년(2025.9~2026.8)
    for nm_ in ['방배그랑자이','방배아트자이']:
        x=win(202509,202608,bb[(bb.nm==nm_)&(bb.ar==85)]); print(nm_,'84㎡ 2025.9~2026.8',len(x),x.p.median())
    x=band(83.5,85.5,win(*PRE,bb)); print('2024.5~7 방배동 84㎡대',len(x),'중앙값',x.p.median(),'분양가 중앙값보다 싼',int((x.p<P84).sum()),'| 2015후',len(x[x.y>=2015]),'가운데 싼',int((x[x.y>=2015].p<P84).sum()))
    x=band(58.5,60.5,win(*PRE,bb)); print('2024.5~7 방배동 59㎡대',len(x),'중앙값',x.p.median(),'분양가 중앙값보다 싼',int((x.p<P59).sum()))
