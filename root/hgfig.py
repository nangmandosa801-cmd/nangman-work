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
    fig.text(0.04,0.96,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.92,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 한강 쪽 vs 안쪽 84 중앙값
R=[('강남','압구정',58.5,'자곡',17.5),('서초','반포',51.5,'양재',15.5),('송파','잠실',32.72,'마천',12.4),('강동','둔촌',27.0,'길동',8.5),('용산','이촌',26.08,'문배',15.7),('마포','용강',26.0,'망원',9.3),('성동','옥수',23.8,'사근',8.6),('동작','흑석',23.0,'신대방',12.64),('광진','광장',21.35,'중곡',6.79),('영등포','당산5가',19.6,'대림',8.68),('양천','목동',14.8,'신월',8.4),('강서','가양',12.55,'방화',7.85)]
fig=plt.figure(figsize=(11.2,12.5)); ax=fig.add_axes([0.12,0.05,0.84,0.82])
head(fig,'전용 84㎡ 실거래 중앙값 · 2026년 3~8월 · 동별 거래 5건 이상','서울 한강뷰 아파트 시세, 같은 구 안에서 한강 쪽 동과 안쪽 동은 최대 3.3배입니다')
n=len(R)
for i,(gu,a,va,b,vb) in enumerate(R):
    y=n-1-i
    ax.plot([vb,va],[y,y],color=LINE,lw=3,zorder=1)
    ax.plot(va,y,'o',ms=12,color=WARN,zorder=3); ax.text(va+1,y,f'{a} {va:.1f}억',va='center',fontsize=12.5,color=WARN,fontweight='bold')
    ax.plot(vb,y,'o',ms=12,color=NAVY,zorder=3); ax.text(vb-1,y,f'{b} {vb:.1f}억',ha='right',va='center',fontsize=12.5,color=NAVY,fontweight='bold')
    ax.text(-13,y,gu,ha='right',va='center',fontsize=14,color=NAVY,fontweight='bold',clip_on=False)
    ax.text(68,y,f'{va/vb:.1f}배',ha='right',va='center',fontsize=13,color=MID,fontweight='bold')
ax.set_xlim(-13,69); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'hangang_fig1.png','주황 = 한강 쪽 동 · 파랑 = 안쪽 동 · 국토교통부 실거래가 · 둔촌은 올림픽파크포레온 신축 효과 포함',allow_outside=True,strict=False)

# fig2 고점 대비 vs 1년, 한강 동
G=['압구정','반포','잠실','둔촌','이촌','옥수','광장','당산5가','가양']
peak=[44.1,34.7,36.5,13.2,31.6,27.7,27.7,28.3,5.2]; yr=[-3.9,5.3,11.5,25.8,14.0,18.7,28.2,24.7,24.5]; price=[58.5,51.5,32.7,27.0,26.1,23.8,21.4,19.6,12.6]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.06,0.14,0.90,0.66])
head(fig,'한강 쪽 동 9곳 · 왼쪽부터 84㎡ 값이 비싼 순서','30억 넘는 압구정·반포·잠실은 멈췄고 20억대 광장·둔촌·당산은 아직 뜁니다')
x=np.arange(len(G)); w=0.36
ax.bar(x-w/2,peak,w,color=LB); ax.bar(x+w/2,yr,w,color=[WARN if v<15 else NAVY for v in yr])
for i in range(len(G)):
    ax.text(x[i]-w/2,peak[i]+1,f'{peak[i]:+.0f}',ha='center',va='bottom',fontsize=12,color='#5F7FA6',fontweight='bold')
    ax.text(x[i]+w/2,(yr[i]+1 if yr[i]>=0 else yr[i]-1),f'{yr[i]:+.1f}',ha='center',va='bottom' if yr[i]>=0 else 'top',fontsize=12,color=WARN if yr[i]<15 else NAVY,fontweight='bold')
    ax.text(x[i],-8,G[i],ha='center',va='top',fontsize=13.5,color=NAVY,fontweight='bold'); ax.text(x[i],-13,f'{price[i]:.0f}억',ha='center',va='top',fontsize=11.5,color=MID)
ax.axhline(0,color=LINE,lw=1)
ax.bar([0],[0],color=LB,label='2021 고점 대비 (4년)'); ax.bar([0],[0],color=NAVY,label='최근 1년'); ax.legend(loc='upper right',fontsize=13,frameon=False)
ax.set_xlim(-0.6,len(G)-0.4); ax.set_ylim(-20,55); clean(ax)
finish(fig,O+'hangang_fig2.png','주황 = 1년 변동 15% 미만 · 15억 초과 대출 4억 한도 뒤 30억대는 현금 26억 이상이 필요 · 단위 %',allow_outside=True,strict=False)

render('서울 한강뷰 아파트',['같은 구 안에서 3배 차이','올해는 안쪽 동이 따라붙었다'],'압구정 -3.9% · 자곡 +23.5% · 15억 대출 벽이 만든 역전',O+'hangang_thumb.png')
print('ok')
