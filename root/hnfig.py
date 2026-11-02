import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# ── 하남 집값 fig1 : 가격대별 상승률
j=pd.read_pickle('/tmp/j.pkl')
j['pb']=pd.cut(j.m0,[0,5,8,11,99],labels=['5억 이하','5억~8억','8억~11억','11억 넘음'])
g=j.groupby('pb',observed=True).r.agg(['median','size'])
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.08,0.17,0.86,0.60])
head(fig,'하남 아파트 · 2025년 가격대별 · 같은 단지·같은 면적 2025년 → 2026년','비싼 집일수록 더 올랐습니다, 5억 이하는 6.9%')
for i,(lab,row) in enumerate(g.iterrows()):
    v=row['median']*100; c=NAVY if i>=2 else (MID if i==1 else GREY)
    ax.bar(i,v,0.62,color=c); ax.text(i,v+0.6,f'{v:.1f}%',ha='center',fontsize=20,color=NAVY,fontweight='bold')
    ax.text(i,-1.6,lab,ha='center',va='top',fontsize=17,color=NAVY,fontweight='bold'); ax.text(i,-3.6,f'{int(row["size"])}곳',ha='center',va='top',fontsize=13.5,color=MID)
ax.axhline(17.0,color=WARN,lw=2,ls='--'); ax.text(-0.3,17.6,'하남 전체 17.0%',ha='left',fontsize=14,color=WARN,fontweight='bold')
ax.set_xlim(-0.6,3.6); ax.set_ylim(-6,24); clean(ax)
finish(fig,O+'hnjipgap_fig1.png','5억 이하 28곳은 대부분 덕풍·신장 구축 · 싼 집과 비싼 집 차이가 1년 새 더 벌어졌습니다',allow_outside=True,strict=False)

# ── 하남 집값 fig2 : 많이 오른 단지
R=[('미사강변효성해링턴플레이스 52㎡','망월동',7.00,9.58,36.9),('미사강변트래지안 52㎡','망월동',6.87,9.03,31.4),
   ('감일센트레빌 60㎡','감이동',8.95,11.70,30.7),('더샵포웰시티 91㎡','감이동',12.43,16.24,30.7),
   ('미사강변 골든센트로 60㎡','망월동',8.95,11.60,29.6),('포웰시티푸르지오라포레 99㎡','감이동',12.30,15.75,28.0)]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.40,0.10,0.50,0.70])
head(fig,'하남 아파트 · 같은 단지·같은 면적 · 2025년 → 2026년','하남 집값 17% 오를 때 미사·감일은 30% 안팎')
n=len(R)
for i,(nm,dong,a0,b0,v) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.62,color=NAVY)
    ax.text(v+0.8,y+0.12,f'{v:.1f}%',va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(v+0.8,y-0.24,f'{a0:.2f}억 → {b0:.2f}억',va='center',fontsize=12.5,color=MID)
    fig.text(0.39,0.10+0.70*(y+0.5)/n+0.012,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
    fig.text(0.39,0.10+0.70*(y+0.5)/n-0.018,dong,ha='right',va='center',fontsize=12.5,color=MID)
ax.axvline(17.0,color=WARN,lw=2.2,ls='--'); ax.text(17.0,n-0.35,'하남 중간값 17.0%',ha='center',fontsize=13.5,color=WARN,fontweight='bold')
ax.set_xlim(0,50); ax.set_ylim(-0.6,n-0.1); clean(ax)
finish(fig,O+'hnjipgap_fig2.png','미사는 52·60㎡ 작은 평수, 감일은 90㎡대 큰 평수까지 30% 가까이 올랐습니다',allow_outside=True,strict=False)

# ── 하남 집값 fig3 : 3.3㎡당 가격, 동네별 점
p=pd.read_pickle('/tmp/pp.pkl'); order=['위례','감일','미사','원도심']
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.17,0.14,0.77,0.64])
head(fig,'하남 아파트 · 2026년 거래 10건 이상 79개 단지 · 3.3㎡당 가격 중간값','같은 하남인데 3.3㎡당 1,784만원부터 6,601만원까지')
rng=np.random.default_rng(3)
for i,z in enumerate(order):
    s=p[p.z==z]; y=len(order)-1-i
    ax.scatter(s.pp,y+rng.uniform(-0.18,0.18,len(s)),s=110,color=WARN if z=='원도심' else NAVY,alpha=0.75,edgecolor='white',linewidth=1)
    md=s.pp.median(); ax.plot([md,md],[y-0.32,y+0.32],color=SAND,lw=3.5)
    ax.text(md,y+0.42,f'{md:,.0f}만원',ha='center',fontsize=14,color=NAVY,fontweight='bold')
    fig.text(0.155,0.14+0.64*(y+0.5)/len(order)+0.012,z,ha='right',va='center',fontsize=19,color=NAVY,fontweight='bold')
    fig.text(0.155,0.14+0.64*(y+0.5)/len(order)-0.025,f'{len(s)}개 단지',ha='right',va='center',fontsize=13,color=MID)
for v in [2000,3000,4000,5000,6000,7000]:
    ax.axvline(v,color=LINE,lw=1,zorder=0); ax.text(v,-0.72,f'{v:,}만원',ha='center',fontsize=13,color=MID)
t=p[p.단지명=='더샵하남에디피스']
if len(t): ax.annotate('더샵하남에디피스 (2024)\n원도심 새 아파트',(t.pp.iloc[0],0),(6500,0.42),fontsize=13,color=WARN,fontweight='bold',ha='center',arrowprops=dict(arrowstyle='-',color=WARN,lw=1.5))
ax.set_xlim(1500,7000); ax.set_ylim(-0.9,len(order)-0.35); clean(ax)
finish(fig,O+'hnjipgap_fig3.png','세로 막대는 동네별 중간값 · 원도심은 넓게 퍼져 있고 위례·감일은 5천만원대에 모여 있습니다',allow_outside=True,strict=False)

# ── 하남 부동산 전망 fig1 : 월별 거래
import sys as _s; exec(open('/tmp/hn.py').read())
m=a[a.y>=2024].groupby('ym').size()
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.07,0.18,0.89,0.58])
head(fig,'하남 아파트 매매 · 월별 거래 건수 · 2024년 1월 → 2026년 8월','규제 직전 두 달 600건대, 규제 뒤에는 한 달 300건 안팎')
xs=list(range(len(m)))
for i,(ym,v) in enumerate(m.items()):
    c=WARN if ym in (202509,202510) else (NAVY if ym>=202511 else GREY)
    ax.bar(i,v,0.72,color=c)
    if ym in (202406,202407,202506,202509,202510,202511): ax.text(i,v+12,f'{v}',ha='center',fontsize=13.5,color=c if c!=GREY else MID,fontweight='bold')
    if ym%100 in (1,7): ax.text(i,-28,f'{ym//100}.{ym%100}',ha='center',fontsize=13,color=MID)
i1=list(m.index).index(202510); ax.axvline(i1+0.5,color=WARN,lw=2,ls='--'); ax.text(i1+0.7,540,'10·15 대책\n투기과열·조정·토허',fontsize=13.5,color=WARN,fontweight='bold',va='top')
i2=list(m.index).index(202601); ax.plot([i2-0.4,len(m)-0.6],[300,300],color=NAVY,lw=2,ls=':'); ax.text(len(m)-0.6,395,'월 300건 선',ha='right',fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_xlim(-0.8,len(m)-0.2); ax.set_ylim(-45,700); clean(ax)
finish(fig,O+'hnjeonmang_fig1.png','규제 전 서둘러 산 거래가 9·10월에 몰렸습니다 · 2026년 8월은 신고가 덜 들어온 숫자입니다',allow_outside=True,strict=False)

# ── 하남 부동산 전망 fig2 : 동네별 2021 대비
j=pd.read_pickle('/tmp/j.pkl'); k=pd.read_pickle('/tmp/k.pkl')
Zs=['감일','위례','미사','원도심']
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.08,0.20,0.86,0.56])
head(fig,'하남 아파트 · 같은 단지·같은 면적 · 동네별 상승률 중간값','2021년 가격 아래 38곳 중 34곳이 원도심입니다')
for i,z in enumerate(Zs):
    a1=j[j.z==z].r.median()*100; a2=k[k.z==z].r.median()*100; nb=(k[k.z==z].r<0).sum(); nn=len(k[k.z==z])
    ax.bar(i-0.19,a1,0.36,color=MID); ax.bar(i+0.19,a2,0.36,color=WARN if z=='원도심' else NAVY)
    ax.text(i-0.19,a1+1.2,f'{a1:.1f}%',ha='center',fontsize=15,color=MID,fontweight='bold')
    ax.text(i+0.19,a2+1.2,f'{a2:.1f}%',ha='center',fontsize=15,color=WARN if z=='원도심' else NAVY,fontweight='bold')
    ax.text(i,-4,z,ha='center',va='top',fontsize=19,color=NAVY,fontweight='bold')
    ax.text(i,-10.5,f'2021년 아래 {nb}곳 / {nn}곳',ha='center',va='top',fontsize=13.5,color=WARN if nb>10 else MID,fontweight='bold' if nb>10 else 'normal')
fig.text(0.50,0.835,'■ 작년 대비 (2025→2026)',fontsize=15,color=MID,fontweight='bold')
fig.text(0.74,0.835,'■ 2021년 대비',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(-0.6,3.6); ax.set_ylim(-16,70); ax.axhline(0,color=LINE,lw=1.5); clean(ax)
finish(fig,O+'hnjeonmang_fig2.png','감일은 2021년 입주 초기 가격이 기준이라 폭이 큽니다 · 원도심은 덕풍·신장·창우, 미사는 망월·풍산·선동',allow_outside=True,strict=False)

# ── 하남 부동산 전망 fig3 : 일정
E=[('2026.10 초','신규택지 7.3만호 발표','하남 후보지 포함 여부',WARN),
   ('2026.12.31','녹지 토지거래허가 만료','연장 여부',WARN),
   ('2028','9호선 4단계 개통 목표','고덕강일 쪽',NAVY),
   ('2029.6','교산 A2 첫 입주','1,115가구',NAVY),
   ('2031','강동하남남양주선 목표','강일~미사',NAVY),
   ('2032','송파하남선(3호선) 목표','감일·교산·하남시청',NAVY)]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.04,0.08,0.92,0.74]); ax.axis('off')
head(fig,'하남 부동산 전망에 걸린 날짜 · 2026년 10월 → 2032년','가장 가까운 변수는 10월 신규택지 발표입니다')
n=len(E); ax.set_xlim(0,10); ax.set_ylim(-0.6,n-0.4)
ax.plot([2.6,2.6],[-0.3,n-0.7],color=LINE,lw=3,zorder=1)
for i,(d,t,s,c) in enumerate(E):
    y=n-1-i; ax.scatter(2.6,y,s=260,color=c,zorder=3,edgecolor='white',linewidth=2.5)
    ax.text(2.25,y,d,ha='right',va='center',fontsize=17,color=c,fontweight='bold')
    ax.text(3.0,y+0.13,t,va='center',fontsize=18,color=NAVY,fontweight='bold'); ax.text(3.0,y-0.24,s,va='center',fontsize=14,color=MID)
finish(fig,O+'hnjeonmang_fig3.png','붉은 두 개는 올해 안 일정 · 철도 개통 시기는 목표이며 바뀔 수 있습니다',allow_outside=True,strict=False)
