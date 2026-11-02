import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_choi_loc_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 경기 하남',['초이IC,','역보다 도로가 먼저'],'9호선 4단계 · 송파하남선 · 서하남로 · 황산~초이 도로',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def canvas(h=6.4,yl=5.2):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,yl); ax.axis('off'); return fig,ax

# fig1 목표 시점
fig,ax=canvas(6.8,5.6)
head(fig,'하남 초이동 교통 계획 · 목표 시점','이미 열린 것은 초이IC 하나, 나머지는 2028~2032년 목표입니다')
yrs=list(range(2025,2033)); X0,DX=3.7,0.95
for k,yv in enumerate(yrs):
    x=X0+k*DX; ax.text(x,5.05,str(yv),ha='center',fontsize=12.5,color=SAND,fontweight='bold'); ax.plot([x,x],[0.35,4.85],color='#EFECE6',lw=1)
rows=[('초이IC','초이동 안',2025,OK,'개통'),('9호선 4단계','939정거장이 가까움',2028,NAVY,'공사 중'),
      ('서하남로 8차로 확장','감북·초이 서울 접근',2030,NAVY,'계획 입안'),('강동하남남양주선','강일~미사, 간접',2031,SAND,'설계'),
      ('서하남IC 교차로 확장','초이동 남쪽 출입구',2031,NAVY,'계획'),('황산~초이 도로','초이동과 원도심 연결',2032,NAVY,'추진 중'),
      ('송파하남선','감일·교산, 간접',2032,SAND,'설계 전')]
for i,(n,d,yv,c,st) in enumerate(rows):
    y=4.45-i*0.64
    ax.text(0.3,y+0.1,n,fontsize=14,color=NAVY,fontweight='bold',va='center')
    ax.text(0.3,y-0.2,d,fontsize=10.8,color=TXT,va='center')
    x=X0+(yv-2025)*DX
    ax.plot([X0,x],[y,y],color=c if c!=SAND else GREY,lw=3,alpha=0.35)
    ax.add_patch(mp.Circle((x,y),0.17,fc=c,ec='white',lw=1.5,zorder=3))
    ax.text(x+0.25 if yv<2031 else x-0.25,y,st,fontsize=11.5,color=c,fontweight='bold',va='center',ha='left' if yv<2031 else 'right')
finish(fig,O+'fig1.png','초록은 이미 개통 · 남색은 초이동을 지나는 사업 · 회색은 간접 효과',allow_outside=True,strict=False)

# fig2 철도 vs 도로
fig,ax=canvas(6.2,5.0)
head(fig,'하남 초이동 교통 · 철도와 도로','철도는 초이동을 비켜 가고, 도로는 초이동을 지나갑니다')
cols=[(0.4,'철도',MID,[('9호선 4단계','△','939정거장이 북서쪽 경계와 가까움'),('강동하남남양주선','X','강일~미사를 지남'),('송파하남선','X','감일~교산을 지남')]),
      (5.8,'도로',WARN,[('초이IC','O','초이동 안, 2025년 개통'),('서하남로 8차로','O','감북·초이 서울 접근'),('황산~초이 도로','O','초이동과 원도심 연결')])]
for x,t,c,items in cols:
    ax.add_patch(mp.FancyBboxPatch((x,0.4),5.0,3.95,boxstyle='round,pad=0.02,rounding_size=0.12',fc='#F7F5F0',ec=c,lw=2))
    ax.add_patch(mp.Rectangle((x+0.02,3.65),4.96,0.68,fc=c,ec='none'))
    ax.text(x+2.5,3.99,t,ha='center',va='center',fontsize=17,color='white',fontweight='bold')
    for i,(n,m,d) in enumerate(items):
        y=3.0-i*1.0
        col={'O':OK,'△':'#C08A2E','X':GREY}[m]
        ax.text(x+0.45,y,m,ha='center',va='center',fontsize=24,color=col,fontweight='bold')
        ax.text(x+0.95,y+0.16,n,fontsize=14.5,color=NAVY,fontweight='bold',va='center')
        ax.text(x+0.95,y-0.24,d,fontsize=11.5,color=TXT,va='center')
finish(fig,O+'fig3.png','초이동을 직접 지나는 것 O · 가까운 것 △ · 지나지 않는 것 X',allow_outside=True,strict=False)

# fig3 송파하남선 일정
fig,ax=canvas(5.4,4.2)
head(fig,'송파하남선 · 일정이 한 번 밀렸습니다','개통 목표가 2028년에서 2032년으로 4년 늦어졌습니다')
yrs=list(range(2025,2033)); X0,DX=2.6,1.08
for k,yv in enumerate(yrs):
    x=X0+k*DX; ax.text(x,3.65,str(yv),ha='center',fontsize=12.5,color=SAND,fontweight='bold'); ax.plot([x,x],[0.5,3.45],color='#EFECE6',lw=1)
for y,lab,a,b,c in [(2.6,'처음 목표',2025,2028,SAND),(1.3,'지금 목표',2027,2032,WARN)]:
    xa,xb=X0+(a-2025)*DX,X0+(b-2025)*DX
    ax.text(0.35,y,lab,fontsize=15,color=c,fontweight='bold',va='center')
    ax.add_patch(mp.FancyBboxPatch((xa,y-0.25),xb-xa,0.5,boxstyle='round,pad=0.01,rounding_size=0.1',fc=c,ec='none',alpha=0.85))
    ax.text(xa+0.1,y,'착공',fontsize=12,color='white',fontweight='bold',va='center')
    ax.text(xb-0.1,y,'개통',fontsize=12,color='white',fontweight='bold',va='center',ha='right')
finish(fig,O+'fig2.png','2025년 7월 기본계획 승인 · 총사업비 1조 8,356억원',allow_outside=True,strict=False)

# fig4 생활권
fig,ax=canvas(6.6,5.4)
head(fig,'하남 초이동 입지 · 생활은 이웃 동네에','역과 생활시설은 옆 동네, 트럭과 헬기는 초이동에 있습니다')
ax.add_patch(mp.Circle((5.6,2.55),0.95,fc=NAVY,ec='none'))
ax.text(5.6,2.55,'초이동',ha='center',va='center',fontsize=19,color='white',fontweight='bold')
out=[(1.7,4.1,'강동 고덕·상일','장보기 · 병원 · 5호선',MID),(9.5,4.1,'감일지구','복합커뮤니티센터 2025.10',MID),(1.7,1.0,'미사강변도시','상권 · 5호선 미사역',MID)]
for x,y,t,d,c in out:
    ax.annotate('',xy=(x+(0.9 if x<5 else -0.9),y+(-0.25 if y>3 else 0.3)),xytext=(5.6+(-0.9 if x<5 else 0.9),2.55+(0.4 if y>3 else -0.4)),arrowprops=dict(arrowstyle='-|>',color=c,lw=2,mutation_scale=18))
    ax.add_patch(mp.FancyBboxPatch((x-1.35,y-0.4),2.7,0.85,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#F7F5F0',ec=c,lw=1.5))
    ax.text(x,y+0.13,t,ha='center',fontsize=14,color=NAVY,fontweight='bold',va='center')
    ax.text(x,y-0.2,d,ha='center',fontsize=11,color=TXT,va='center')
ax.add_patch(mp.FancyBboxPatch((7.9,0.35),3.1,1.6,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#FBEFEA',ec=WARN,lw=1.5))
ax.text(9.45,1.65,'초이동 안의 불편',ha='center',fontsize=13.5,color=WARN,fontweight='bold')
for k,t in enumerate(['좁은 길의 물류 트럭','제1항공여단 헬기','남쪽 광암동 변전소']):
    ax.text(8.15,1.25-k*0.33,'· '+t,fontsize=12,color=TXT,va='center')
finish(fig,O+'fig4.png','방향은 실제 지도가 아닙니다 · 무엇을 어디서 해결하는지만 나타냈습니다',allow_outside=True,strict=False)
