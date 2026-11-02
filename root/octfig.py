import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 지역별 가구
R=[('경기 (23개 단지)',16043,NAVY),('인천 (7개 단지)',6921,MID),('서울 (5개 단지)',1654,WARN),('지방 (15개 단지)',13414,GREY)]
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.20,0.12,0.76,0.66])
head(fig,'2026년 10월 분양 예정 · 전국 50개 단지 3만 8,032가구 · 직방 9월 28일 조사','10월 분양 아파트, 경기 1만 6천 가구인데 서울은 1,654가구입니다')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+200,y,f'{v:,}가구 · {v/38032*100:.0f}%',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(-200,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,21500); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'oct_bunyang_fig1.png','작년 10월 2만 3,667가구보다 61% 많음 · 수도권 2만 4,618가구(65%) · 서울 신규 청약은 고덕강일 3단지 215가구가 중심',allow_outside=True,strict=False)

# fig2 경기 4곳 주변 신축 시세
R=[('안산 아르무제 자이\n(고잔동 · 984가구)',9.85,'레이크타운푸르지오 2016'),('경기광주역 롯데캐슬 2단지\n(쌍령동 · 1,249가구)',8.5,'광주역자연앤자이 2021'),('지제역 한화포레나\n(지제동 · 1,098가구)',8.0,'지제역더샵센트럴시티 2022'),('향남 롯데캐슬 시그니처\n(향남읍 · 1,542가구)',4.93,'한양수자인디에스티지 2024')]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.30,0.10,0.66,0.72])
head(fig,'경기 10월 분양 1천 가구 이상 4곳 · 주변 신축 전용 84㎡ 실거래 중앙값 (2026년 3~8월)','경기 10월 분양, 분양가가 이 선 아래인지가 기준입니다')
n=len(R)
for i,(nm,v,ref) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=NAVY if v>=8 else MID)
    ax.text(v+0.12,y+0.1,f'{v:.2f}억',va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(v+0.12,y-0.22,ref,va='center',fontsize=12.5,color=MID)
    ax.text(-0.15,y,nm,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False,linespacing=1.4)
ax.set_xlim(0,13.5); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'oct_bunyang_fig2.png','국토교통부 실거래가 · 해제 거래 제외 · 네 곳 모두 10·15 규제지역 밖 (전매 6개월 · LTV 70%) · 분양가는 모집공고로 확정',allow_outside=True,strict=False)

# fig3 규제 vs 비규제
fig=plt.figure(figsize=(11.2,7.4)); ax=fig.add_axes([0.04,0.08,0.92,0.70])
head(fig,'같은 10월 청약인데 지역에 따라 조건이 다릅니다','규제지역과 비규제, 전매 3년 vs 6개월 · LTV 40% vs 70%')
rows=[('전매제한','3년','6개월'),('재당첨 제한','10년','없음'),('대출 LTV','40%','70%'),('1순위 통장','2년 · 세대주','1년'),('분양가상한제','공공택지 · 강남3구·용산','없음')]
ax.text(0.38,1.0,'규제지역\n서울 전역 · 경기 12곳',ha='center',va='bottom',fontsize=15,color=WARN,fontweight='bold',linespacing=1.4)
ax.text(0.78,1.0,'비규제\n향남·광주·평택·안산·인천',ha='center',va='bottom',fontsize=15,color=NAVY,fontweight='bold',linespacing=1.4)
for i,(a,b,c) in enumerate(rows):
    y=0.85-i*0.19
    ax.plot([0.02,0.98],[y-0.095,y-0.095],color=LINE,lw=1)
    ax.text(0.02,y,a,ha='left',va='center',fontsize=15,color=MID,fontweight='bold')
    ax.text(0.38,y,b,ha='center',va='center',fontsize=16,color=WARN,fontweight='bold')
    ax.text(0.78,y,c,ha='center',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,1); ax.set_ylim(-0.12,1.2); clean(ax)
finish(fig,O+'oct_bunyang_fig3.png','주택공급에 관한 규칙 · 10·15 대책 기준 · 고덕강일 3단지는 공공택지라 분양가상한제·실거주 의무까지 붙음',allow_outside=True,strict=False)

render('10월 분양',['전국 3만 8천 가구 · 경기 1만 6천','서울은 고덕강일 3억대 215가구'],'향남·광주역·지제역·안산 1천 가구 4곳은 비규제',O+'oct_bunyang_thumb.png')
print('ok')
