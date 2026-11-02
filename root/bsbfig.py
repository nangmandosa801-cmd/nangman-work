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

# fig1 땅 종류별 배율 + 권역
fig=plt.figure(figsize=(11.2,8.4))
head(fig,'KDI 2021 · 2017~2020 실제 보상 62.9만 건 ÷ 개별공시지가 · 중앙값','토지보상 공시지가 몇배, 경기 2.18배인데 임야 3.5배 상업지 1.6배입니다')
ax=fig.add_axes([0.22,0.10,0.34,0.72])
R=[('임야',3.50,WARN),('공공·기타',3.18,MID),('전·답',2.12,NAVY),('경기 전체',2.18,'#1F3864'),('주거·공업용',1.85,NAVY),('상업·주상용',1.62,NAVY)]
R=[('임야',3.50,WARN),('공공·기타',3.18,LB),('경기 전체',2.18,'#1F3864'),('전·답',2.12,NAVY),('주거·공업용',1.85,NAVY),('상업·주상용',1.62,NAVY)]
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+0.06,y,f'{v:.2f}배',va='center',fontsize=14.5,color=c,fontweight='bold')
    ax.text(-0.08,y,nm,ha='right',va='center',fontsize=14,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,4.4); ax.set_ylim(-0.6,n-0.4); clean(ax)
ax.text(0,n-0.3,'땅 종류별',fontsize=14,color=MID,fontweight='bold',va='bottom')
ax2=fig.add_axes([0.72,0.10,0.24,0.72])
K=[('화성·평택·오산·안성',2.36),('하남·광주·이천',2.33),('고양·구리·남양주·파주',2.14),('부천·광명·시흥·김포',1.99),('수원·성남·과천·용인',1.83),('서울',1.59)]
m=len(K)
for i,(nm,v) in enumerate(K):
    y=m-1-i; c=NAVY if i<5 else GREY
    ax2.barh(y,v,0.6,color=c)
    ax2.text(v+0.06,y,f'{v:.2f}',va='center',fontsize=13.5,color=c if i<5 else MID,fontweight='bold')
    ax2.text(-0.08,y,nm,ha='right',va='center',fontsize=12.5,color=NAVY,clip_on=False)
ax2.set_xlim(0,3.2); ax2.set_ylim(-0.6,m-0.4); clean(ax2)
ax2.text(0,m-0.3,'경기 권역별',fontsize=14,color=MID,fontweight='bold',va='bottom')
finish(fig,O+'bosangbae_fig1.png','예타 보상비 추정용 통계 · 특정 지구 배율 아님 · 임야 배율이 높은 건 공시지가 현실화율 62.7%로 제일 낮아서',allow_outside=True,strict=False)

# fig2 3인 구조 + 110% 규칙
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.03,0.08,0.94,0.74])
head(fig,'토지보상법 68조 · 시행령 28조 · 시행규칙 16·17조','감정평가사 3명 중 1명은 땅 주인이 고르고, 차이 10% 넘으면 재평가입니다')
boxes=[(0.03,'사업시행자 추천 1인','LH·GH 등 · 수수료 부담',NAVY),(0.35,'시·도지사 추천 1인','추첨 등 객관적 절차',MID),(0.67,'토지소유자 추천 1인','열람 끝난 날부터 30일 안\n면적 1/2 + 사람 과반 동의',WARN)]
for x,a,b,c in boxes:
    ax.add_patch(plt.Rectangle((x,0.62),0.30,0.30,color=c))
    ax.text(x+0.15,0.85,a,ha='center',va='center',fontsize=16,color='white',fontweight='bold')
    ax.text(x+0.15,0.71,b,ha='center',va='center',fontsize=12.5,color='white')
    ax.annotate('',xy=(x+0.15,0.47),xytext=(x+0.15,0.61),arrowprops=dict(arrowstyle='-|>',color=LINE,lw=2))
ax.add_patch(plt.Rectangle((0.03,0.30),0.94,0.16,fill=False,ec=NAVY,lw=2.5))
ax.text(0.50,0.41,'보상액 = 3인 평가액의 산술평균',ha='center',va='center',fontsize=18,color=NAVY,fontweight='bold')
ax.text(0.50,0.34,'예: 10억 · 10억 3천 · 10억 9천 → 10억 4천  (추천 없이 2인이면 10억 1,500만)',ha='center',va='center',fontsize=13.5,color=MID)
ax.add_patch(plt.Rectangle((0.03,0.02),0.94,0.20,fill=False,ec=WARN,lw=2,ls='--'))
ax.text(0.06,0.16,'단, 가장 높은 평가액이 가장 낮은 값의 110%를 넘으면',fontsize=15,color=WARN,fontweight='bold',va='center')
ax.text(0.06,0.07,'→ 다른 평가사 2인 이상이 다시 평가 (시행규칙 17조) · 추천 평가사 혼자 높게 쓰면 평균이 아니라 재평가로 갑니다',fontsize=13,color=NAVY,va='center')
ax.set_xlim(0,1); ax.set_ylim(0,1); clean(ax)
finish(fig,O+'bosangbae_fig2.png','둘 다 추천 안 하면 시행자 선정 2인 · 한쪽만 추천하면 2인 · 예시는 감정평가사 기고의 가상 계산',allow_outside=True,strict=False)

render('토지보상 공시지가 몇배',['경기 실제 보상 중앙값 2.18배','임야 3.5배 · 상업지 1.6배'],'비싼 땅일수록 배율 낮음 · 감정평가사 추천은 30일 안',O+'bosangbae_thumb.png')
print('ok')
