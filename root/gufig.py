import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gucuk_interior_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 구축 아파트',['구축 아파트','인테리어 순서'],'샷시·중문·결로부터 정해야 돈이 두 번 안 듭니다',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1 stacked horizontal bars
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.13,0.2,0.83,0.58])
head(fig,'구축 아파트 · 2026년 1~8월 아파트 매매, 지은 지 몇 년 된 집인가','서울은 열 채 중 여덟 채가 15년 넘은 구축입니다')
R=[('서울',[7.9,100-7.9-78.4,78.4]),('경기',[12.6,100-12.6-59.5,59.5]),('서울·경기',[11.2,100-11.2-65.2,65.2])]
C=[OK,GREY,WARN]; N=['5년 안 됨','6~14년','15년 넘음']
for i,(n,v) in enumerate(R[::-1]):
    x=0
    for j,(w,c) in enumerate(zip(v,C)):
        ax.barh(i,w,0.5,left=x,color=c)
        ax.text(x+w/2,i+0.36,f'{w:.1f}%',ha='center',va='bottom',fontsize=18,color=c if j!=1 else SAND,fontweight='bold')
        x+=w
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in R[::-1]],fontsize=19,color=NAVY,fontweight='bold')
ax.set_xlim(0,100); ax.set_xticks([]); ax.set_ylim(-0.5,2.8)
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
for j,(n,c) in enumerate(zip(N,C)):
    fig.text(0.13+j*0.2,0.12,'■ '+n,fontsize=16,color=c if j!=1 else SAND,fontweight='bold')
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 서울 4만 8,820건 · 경기 11만 4,862건 · 해제 거래 제외',allow_outside=True,strict=False)
# fig2 steps
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,80); ax.axis('off')
head(fig,'구축 아파트 인테리어 순서','뜯는 것 먼저, 보이는 마감은 뒤')
S=[('0','지원금 신청','공사 전에 넣어야 받습니다',WARN),('1','철거','바닥 · 벽지 · 낡은 문',GREY),('2','샷시 · 배관 · 전기','벽을 건드리는 공사',WARN),
   ('3','목공 · 타일','벽 · 천장 · 욕실',GREY),('4','도배 · 바닥','보이는 마감',GREY),('5','주방 · 붙박이장 · 조명','바닥 높이에 맞춰',GREY),('6','중문','바닥 깐 뒤 실측',WARN)]
for i,(n,t,d,c) in enumerate(S):
    y=72-i*10.4
    fc='#FBEFEA' if c==WARN else '#F4F6F9'
    ax.add_patch(mp.FancyBboxPatch((14,y-8),90,8.2,boxstyle='round,pad=0.2,rounding_size=1.5',fc=fc,ec=c if c==WARN else LINE,lw=2.5 if c==WARN else 1.2))
    ax.add_patch(mp.Circle((8,y-3.9),3.6,fc=c if c==WARN else MID,ec='none'))
    ax.text(8,y-3.9,n,ha='center',va='center',fontsize=19,color='white',fontweight='bold')
    ax.text(18,y-3.9,t,va='center',fontsize=21,color=NAVY,fontweight='bold')
    ax.text(101,y-3.9,d,va='center',ha='right',fontsize=17,color=WARN if c==WARN else TXT)
finish(fig,O+'fig2.png','업체와 현장에 따라 조금씩 다를 수 있습니다 · 주황 = 순서를 틀리면 두 번 손대는 곳',allow_outside=True,strict=False)
