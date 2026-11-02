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
    fig.text(0.04,0.965,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.925,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
df=pd.read_pickle('/home/claude/w/seoul_recovery.pkl')

# fig1 25구 고점 대비
fig=plt.figure(figsize=(11.2,13.5)); ax=fig.add_axes([0.16,0.06,0.80,0.82])
head(fig,'같은 단지·같은 전용면적 중앙값 · 2021.7~2022.1 → 2026.3~8 · 국토교통부 실거래가','서울 아파트 시세 순위, 2021년 고점을 넘은 구는 25곳 중 12곳입니다')
n=len(df)
for i,(_,r) in enumerate(df.iterrows()):
    y=n-1-i; v=r['고점대비']; c=NAVY if v>=0 else WARN
    ax.barh(y,v,0.64,color=c)
    ax.text(v+(0.6 if v>=0 else -0.6),y,f'{v:+.1f}%',ha='left' if v>=0 else 'right',va='center',fontsize=13.5,color=c,fontweight='bold')
    ax.text(-21.5,y,r['구'],ha='right',va='center',fontsize=14,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(0,color=LINE,lw=1.5)
ax.axvline(4.7,color=MID,lw=1.5,ls='--'); ax.text(5.2,n-0.3,'서울 전체 +4.7%',fontsize=12.5,color=MID,va='bottom')
ax.set_xlim(-21.5,38); ax.set_ylim(-0.7,n+0.3); clean(ax)
finish(fig,O+'seoul25_fig1.png','구별 48~416쌍 · 서울 전체 5,149쌍 · 2026년 8월은 신고 진행 중 · 성동 +30.2%와 도봉 -16.0%는 46포인트 차이',allow_outside=True,strict=False)

# fig2 고점 대비 vs 1년
fig=plt.figure(figsize=(11.2,9.2)); ax=fig.add_axes([0.10,0.10,0.86,0.72])
head(fig,'가로: 2021년 고점 대비 · 세로: 최근 1년 변동 (2025.3~8 → 2026.3~8)','강남·서초는 고점은 넘었는데 올해는 멈췄고, 성동·동작·송파는 둘 다 앞입니다')
for _,r in df.iterrows():
    x,y=r['고점대비'],r['1년']
    c=WARN if r['구'] in ('강남구','서초구') else (NAVY if x>=0 else MID)
    ax.plot(x,y,'o',ms=11,color=c)
    off={'마포구':(1.0,-1.2),'동작구':(1.0,1.2),'송파구':(1.0,-1.2),'영등포구':(1.0,1.0),'성북구':(-1.0,0.0,'right'),'동대문구':(1.0,0.5),'서대문구':(1.0,1.0),'양천구':(1.0,0.0),'강서구':(1.0,-1.0),'관악구':(1.0,-1.0),'구로구':(1.0,0.9),'강북구':(-1.0,0.0,'right'),'중랑구':(-1.0,-0.9,'right'),'은평구':(1.0,-0.6)}
    o=off.get(r['구'],(1.0,0.0)); dx,dy=o[0],o[1]; ha=o[2] if len(o)>2 else 'left'
    ax.text(x+dx,y+dy,r['구'][:-1],fontsize=12.5,color=c,va='center',ha=ha,fontweight='bold')
ax.axvline(0,color=LINE,lw=1.2); ax.axhline(13.7,color=LINE,lw=1.2,ls='--')
ax.text(37,14.2,'서울 1년 +13.7%',ha='right',fontsize=12,color=MID)
ax.text(1,1.0,'고점 ↑',fontsize=12,color=MID); ax.text(-17.5,1.0,'← 고점 아래',fontsize=12,color=MID)
ax.set_xlim(-18,38); ax.set_ylim(0,29); clean(ax)
finish(fig,O+'seoul25_fig2.png','주황은 강남·서초 (고점 +20.6%·+19.4% / 1년 +5.1%·+9.5%) · 15억 초과 대출 4억 한도가 만든 차이로 보임',allow_outside=True,strict=False)

render('서울 아파트 시세 순위',['2021년 고점 넘은 구 12 / 25','성동 +30% · 도봉 -16%'],'강남은 올해 +5%로 멈추고 성동·동작·송파가 +25%',O+'seoul25_thumb.png')
print('ok')
