import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.965,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.93,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
df=pd.read_pickle('/home/claude/w/seoul_engine.pkl').set_index('구')

# fig1 구축 vs 신축 1년 변동 (dumbbell) 25구
order=['성동구','광진구','강동구','마포구','동작구','송파구','중구','동대문구','영등포구','양천구','성북구','강서구','종로구','서초구','서대문구','용산구','노원구','관악구','구로구','강남구','강북구','은평구','도봉구','중랑구','금천구']
fig=plt.figure(figsize=(11.2,14)); ax=fig.add_axes([0.14,0.05,0.82,0.84])
head(fig,'1년 변동 (2025.3~8 → 2026.3~8) · 주황 = 1995년 이전 구축 · 파랑 = 가장 새 연식(2021~ 또는 2011~2020)','서울 구축 아파트 시세, 25개 구 중 17곳은 30년 넘은 집이 더 올랐습니다')
n=len(order)
for i,gu in enumerate(order):
    r=df.loc[gu]; y=n-1-i
    old=r['~1995']; new=r['2021~'] if pd.notna(r['2021~']) else r['2011~2020']
    if pd.notna(old) and pd.notna(new):
        ax.plot([min(old,new),max(old,new)],[y,y],color=LINE,lw=3,zorder=1)
    if pd.notna(old):
        ax.plot(old,y,'o',ms=11,color=WARN,zorder=3); ax.text(old+(0.8 if old>=new else -0.8),y,f'{old:.1f}',ha='left' if old>=new else 'right',va='center',fontsize=11.5,color=WARN,fontweight='bold')
    if pd.notna(new):
        ax.plot(new,y,'o',ms=11,color=NAVY,zorder=3); ax.text(new+(0.8 if new>old else -0.8),y,f'{new:.1f}',ha='left' if new>old else 'right',va='center',fontsize=11.5,color=NAVY,fontweight='bold')
    ax.text(-2.5,y,gu,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(0,color=LINE,lw=1)
ax.plot([24],[2.2],'o',ms=10,color=WARN); ax.text(25,2.2,'1995년 이전 구축',fontsize=12.5,color=WARN,va='center',fontweight='bold')
ax.plot([24],[1.2],'o',ms=10,color=NAVY); ax.text(25,1.2,'가장 새 연식 (2021~ 또는 2011~2020)',fontsize=12.5,color=NAVY,va='center',fontweight='bold')
ax.set_xlim(-3,38); ax.set_ylim(-0.7,n+0.2); clean(ax)
finish(fig,O+'seoulengine_fig1.png','같은 단지·같은 전용면적 중앙값 · 묶음별 쌍 8개 이상 · 2021년 이후 쌍이 부족한 구는 2011~2020년으로 대신',allow_outside=True,strict=False)

# fig2 구축/신축 평당가 배율
R=[('성북구',2.65),('은평구',2.07),('중구',1.84),('서대문구',1.78),('서초구',1.75),('동대문구',1.73),('중랑구',1.62),('금천구',1.61),('마포구',1.52),('강북구',1.50),('구로구',1.42),('강동구',1.32),('노원구',1.32),('관악구',1.24),('영등포구',1.20),('동작구',1.19),('종로구',1.11),('도봉구',1.08),('강남구',1.07),('강서구',1.07),('성동구',1.05),('용산구',0.92),('송파구',0.84),('광진구',0.79),('양천구',0.56)]
fig=plt.figure(figsize=(11.2,13.5)); ax=fig.add_axes([0.14,0.05,0.82,0.84])
head(fig,'2026년 3~8월 평당 중앙값 · 가장 새 연식 ÷ 1995년 이전 구축','서울 재건축 아파트 기대, 양천·광진·송파·용산은 구축이 신축보다 비쌉니다')
n=len(R)
for i,(gu,v) in enumerate(R):
    y=n-1-i; c=WARN if v<1 else (NAVY if v>=1.7 else MID)
    ax.barh(y,v,0.62,color=c)
    ax.text(v+0.03,y,f'{v:.2f}배',va='center',fontsize=13,color=c,fontweight='bold')
    ax.text(-0.04,y,gu,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(1,color=LINE,lw=1.5,ls='--'); ax.text(1.02,n-0.2,'1배 = 구축과 신축이 같은 값',fontsize=12,color=MID,va='bottom')
ax.set_xlim(0,3.1); ax.set_ylim(-0.7,n+0.3); clean(ax)
finish(fig,O+'seoulengine_fig2.png','주황 = 구축이 더 비싼 구(재건축 기대) · 진한 파랑 = 신축이 1.7배 넘는 구(재개발 입주) · 거래 5건 이상 연식만',allow_outside=True,strict=False)

render('서울 구축 아파트 시세',['25개 구 중 17곳','30년 넘은 집이 신축보다 더 올랐다'],'성동 구축 +32% · 양천은 구축이 신축의 1.8배 · 강남은 전 연식 멈춤',O+'seoulengine_thumb.png')
print('ok')
