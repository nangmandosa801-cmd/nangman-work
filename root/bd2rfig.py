import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_bd2result_'
render('낭만 부동산 분석 플랫폼 · 분당 재건축 2차 발표',
       ['분당 재건축 2차 5곳 선정,','가장 많이 오른 효자촌은 빠졌습니다'],
       '이매촌1 · 시범단지1 · 파크타운 · 푸른마을 · 한솔마을2', O+'thumb.png')

# fig1 : 선정 vs 탈락 후보 발표 전 상승률
R=[('서현 효자촌',53.0,0),('이매촌 삼성·삼환',47.6,1),('상록마을 우성',45.4,0),('파크타운 4개 단지',42.5,1),
   ('한솔마을 청구·LG',42.0,1),('야탑 탑마을',40.5,0),('시범 삼성·한신·한양',39.9,1),('푸른마을 쌍용·신성',39.5,1),
   ('아름마을 풍림·선경·효성',35.7,0)]
fig=plt.figure(figsize=(11.2,9.2)); ax=fig.add_axes([0.30,0.10,0.64,0.70])
fig.text(0.04,0.955,'분당 2차 후보 · 2024년 1~10월 → 2026년 3~8월 같은 단지·같은 면적',fontsize=16,color=MID,va='center')
fig.text(0.04,0.905,'선정 5곳은 발표 전 덜 오른 쪽이었습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
n=len(R)
for i,(nm,v,s) in enumerate(R):
    y=n-1-i; c=NAVY if s else '#C9C3B6'
    ax.barh(y,v,0.66,color=c)
    ax.text(v+0.8,y,f'{v:.1f}%',va='center',fontsize=15,color=NAVY if s else SAND,fontweight='bold')
    fig.text(0.29,0.10+0.70*(y+0.5)/n,nm,ha='right',va='center',fontsize=15,color=NAVY if s else '#555555',fontweight='bold' if s else 'normal')
ax.set_xlim(0,62); ax.set_ylim(-0.5,n-0.5); ax.set_xticks([]); ax.set_yticks([])
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
fig.text(0.60,0.845,'■ 선정  평균 42.1%',fontsize=15,color=NAVY,fontweight='bold')
fig.text(0.80,0.845,'■ 탈락  평균 45.0%',fontsize=15,color='#A8A194',fontweight='bold')
finish(fig,O+'fig1.png','국토교통부 실거래 · 해제 거래 제외 · 2026년 8월 계약분까지 · 탈락 평균은 비교 면적 수로 가중',allow_outside=True,strict=False)

# fig2 : 1차 발표 뒤 흐름
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.08,0.16,0.86,0.60])
fig.text(0.04,0.955,'분당 1차 선도지구 발표(2024년 11월) 뒤 · 발표 전 대비 상승률',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'반년은 선정 단지가 앞섰고, 1년 반 뒤 따라잡혔습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x=[0,1,2,3]; lab=['넉 달 뒤','반년 뒤','1년 뒤','1년 반 뒤']
s=[9.9,23.6,42.8,46.3]; o=[5.3,13.7,36.5,47.0]
ax.plot(x,s,color=NAVY,lw=3.4,marker='o',ms=9); ax.plot(x,o,color=WARN,lw=3.4,marker='o',ms=9)
for i in x:
    ax.text(i+(0 if i<3 else -0.1),s[i]+2.2 if i<3 else s[i]-6.5,f'{s[i]}%',ha='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(i,o[i]-5.2 if i<3 else o[i]+2.4,f'{o[i]}%',ha='center',fontsize=15,color=WARN,fontweight='bold')
    ax.text(i,-7.5,lab[i],ha='center',fontsize=14,color=NAVY)
fig.text(0.60,0.835,'● 1차 선정 단지',fontsize=15,color=NAVY,fontweight='bold')
fig.text(0.80,0.835,'● 못 든 구축',fontsize=15,color=WARN,fontweight='bold')
ax.set_xlim(-0.4,3.5); ax.set_ylim(-10,56); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
finish(fig,O+'fig2.png','2차 선정 단지도 같은 흐름일지 석 달 뒤 같은 방식으로 다시 확인합니다',allow_outside=True,strict=False)
