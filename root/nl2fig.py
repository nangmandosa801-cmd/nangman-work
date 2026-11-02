import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1 땅값
R=[('하남 감북동',536,'14건'),('과천',454,'32건'),('구리',205,'21건'),('광명',181,'20건'),('고양 덕양구',112,'237건'),('김포 고촌',92,'56건'),('남양주 와부 (1차 발표)',83,'93건')]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.30,0.10,0.64,0.70])
head(fig,'거론되는 신규택지 후보지 · 그린벨트 밭·논 · 2025년 1월~2026년 8월 통째 거래 평당 중간값','신규택지 후보지 땅값, 감북동 536만원부터 고촌 92만원까지')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; col=NAVY if i<2 else (MID if i<4 else (GREY if i==6 else '#7E97B8'))
    ax.barh(y,v,0.62,color=col); ax.text(v+8,y,f'{v}만원',va='center',fontsize=16.5,color=NAVY,fontweight='bold'); ax.text(v+8,y-0.3,c,va='center',fontsize=12,color=MID)
    ax.text(-10,y,nm,ha='right',va='center',fontsize=15.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,640); ax.set_ylim(-0.7,n-0.4); clean(ax)
finish(fig,O+'newland2_fig1.png','국토교통부 토지 실거래 · 개발제한구역 전·답 · 지분·해제 거래 제외 · 감북동은 14건이라 한두 건에 흔들릴 수 있습니다',allow_outside=True,strict=False)
# fig2 거래량
R=[('고양 덕양구',95,338),('남양주 와부',70,162),('김포 고촌',38,51),('과천',59,58),('광명',11,70),('하남 감북동',63,28),('구리',96,17)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.26,0.12,0.68,0.68])
head(fig,'신규택지 후보지 · 그린벨트 토지 거래 건수 · 1~8월','그린벨트 토지 거래, 고양은 3.6배 늘고 감북·구리는 줄었습니다')
n=len(R)
for i,(nm,a,b) in enumerate(R):
    y=n-1-i
    ax.barh(y+0.17,a,0.3,color=GREY); ax.barh(y-0.17,b,0.3,color=NAVY if b>a else WARN)
    ax.text(a+5,y+0.17,f'{a}건',va='center',fontsize=12.5,color=MID); ax.text(b+5,y-0.17,f'{b}건',va='center',fontsize=14.5,color=NAVY if b>a else WARN,fontweight='bold')
    ax.text(-8,y,nm,ha='right',va='center',fontsize=15.5,color=NAVY,fontweight='bold',clip_on=False)
ax.barh([-5],[0],color=GREY,label='2024년 1~8월'); ax.barh([-5],[0],color=NAVY,label='2026년 1~8월')
lg=ax.legend(loc='lower right',frameon=False,fontsize=13)
ax.set_xlim(0,390); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'newland2_fig2.png','구리는 2026년 7월 규제지역 지정, 하남은 8월 18일 토지거래허가구역 지정 · 해제 거래 제외',allow_outside=True,strict=False)
# fig3 발표 뒤 1년
R=[('하남 교산 (2018.12)',2.0,1.1),('남양주 왕숙 (2018.12)',0.3,1.1),('고양 창릉 (2019.5)',1.5,5.0),('부천 대장 (2019.5)',6.5,5.0),('광명시흥 (2021.2)',21.9,37.0),('의왕·군포·안산 (2021.8)',0.5,11.0),('화성 진안 (2021.8)',16.5,11.0)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.30,0.12,0.64,0.68])
head(fig,'신규택지 발표 전 6개월 → 발표 뒤 7~12개월 · 같은 단지·같은 면적 중간값 변화','신규택지 발표 뒤 1년, 옆 아파트가 경기보다 더 오른 곳은 3곳')
n=len(R)
for i,(nm,a,b) in enumerate(R):
    y=n-1-i; win=a>b
    ax.barh(y+0.17,a,0.3,color=NAVY if win else WARN); ax.barh(y-0.17,b,0.3,color=GREY)
    ax.text(a+0.6,y+0.17,f'{a:+.1f}%',va='center',fontsize=14.5,color=NAVY if win else WARN,fontweight='bold'); ax.text(b+0.6,y-0.17,f'경기 {b:+.1f}%',va='center',fontsize=12.5,color=MID)
    ax.text(-1,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,44); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'newland2_fig3.png','파란색은 경기 평균보다 더 오른 곳, 붉은색은 덜 오른 곳 · 국토교통부 아파트 실거래',allow_outside=True,strict=False)
render('신규택지 후보지',['신규택지 후보지 6곳','그린벨트 땅값 536만 vs 92만'],'발표는 11월 초까지 밀렸고 서울 그린벨트는 빠집니다',O+'newland2_thumb.png')
print('ok')
