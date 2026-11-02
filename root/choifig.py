import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_choi_dev_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 경기 하남',['초이동 개발 계획,','확정은 하나뿐입니다'],'교산 기업이전단지 · 도시기본계획 · 군부대 · 신규택지',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def canvas(h=6.4,yl=5.2):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,yl); ax.axis('off'); return fig,ax

# fig1 단계 사다리
fig,ax=canvas(6.6,5.4)
head(fig,'초이동 개발 계획 · 사업별 단계','공사 직전까지 간 것은 기업이전단지 하나입니다')
steps=['건의','구상','계획 승인','사업 확정','보상·공사']
X0,W=3.9,1.35
for j,s in enumerate(steps): ax.text(X0+j*W+W/2,4.9,s,ha='center',fontsize=13.5,color=SAND,fontweight='bold')
rows=[('교산 기업이전단지(광암)',5,'보상 82% · 2024년 12월',NAVY),
      ('2040 하남 도시기본계획',3,'2023년 4월 경기도 승인',MID),
      ('제1항공여단 이전',2,'2023년 5월 주민 설문',SAND),
      ('8·13 신규택지 포함',1,'2026년 9월 주민 건의서',WARN)]
for i,(n,k,d,c) in enumerate(rows):
    y=4.0-i*1.05
    ax.text(0.35,y+0.12,n,fontsize=15,color=NAVY,fontweight='bold',va='center')
    ax.text(0.35,y-0.3,d,fontsize=11.5,color=TXT,va='center')
    for j in range(5):
        ax.add_patch(mp.FancyBboxPatch((X0+j*W+0.06,y-0.22),W-0.12,0.5,boxstyle='round,pad=0.01,rounding_size=0.08',fc=c if j<k else '#EFECE6',ec='none'))
        if j==k-1 and i==0:
            ax.add_patch(mp.Rectangle((X0+j*W+0.06+(W-0.12)/2,y-0.22),(W-0.12)/2,0.5,fc='#EFECE6',ec='none'))
    ax.plot([0.3,10.9],[y-0.52,y-0.52],color=LINE,lw=1)
finish(fig,O+'fig1.png','기업이전단지는 보상 중 · 나머지 셋은 아직 사업이 아닙니다',allow_outside=True,strict=False)

# fig2 교산 신도시 구성
fig,ax=canvas(6.0,4.9)
head(fig,'교산 기업이전단지 · 교산 신도시 안에서의 크기','초이동은 아파트 본단지가 아니라 공장 단지로 들어갔습니다')
items=[('본단지','631만㎡','아파트 3만 6,697호 · 천현·교산·춘궁·상사창·하사창동',631,MID),
       ('광암 기업이전단지','약 28만㎡','제조 단지 · LH · 초이동 일부 포함',28,WARN),
       ('상산곡 기업이전단지','26만㎡','물류 단지 · GH',26,SAND)]
for i,(n,a,d,v,c) in enumerate(items):
    y=3.55-i*1.25
    ax.text(0.35,y+0.2,n,fontsize=15,color=NAVY,fontweight='bold',va='center')
    ax.text(0.35,y-0.25,a,fontsize=13,color=c,fontweight='bold',va='center')
    w=max(v/631*6.6,0.12)
    ax.add_patch(mp.Rectangle((3.9,y-0.2),w,0.55,fc=c,ec='none'))
    ax.text(3.9+w+0.15 if v<600 else 4.05,y-0.52 if v>600 else y+0.08,d,fontsize=12,color=TXT if v<600 else TXT,va='center')
finish(fig,O+'fig2.png','기업이전단지 두 곳을 합쳐도 본단지의 9%입니다',allow_outside=True,strict=False)

# fig3 택지 후보 연표
fig,ax=canvas(6.2,5.0)
head(fig,'신규택지 발표 하남 · 초이동 주변이 후보에 오른 기록','후보에 오르고 빠지기를 반복했고, 지금은 주민 건의 단계입니다')
ev=[(0.9,'2010','감북동 보금자리\n지구 지정',MID,True),(2.5,'2014','감북동\n지정 취소',GREY,False),
    (4.3,'2024.8','초이동 포함\n허가구역 지정',MID,True),(5.9,'2024.11','신규택지 제외\n허가구역 해제',GREY,False),
    (7.6,'2026.8.13','정부 신규택지\n10만 가구 발표',NAVY,True),(9.4,'2026.9.8','주민\n건의서',WARN,True)]
ax.plot([0.5,10.7],[2.6,2.6],color=LINE,lw=3)
for i,(x,d,t,c,up) in enumerate(ev):
    ax.add_patch(mp.Circle((x,2.6),0.18,fc=c,ec='white',lw=2,zorder=3))
    yy=3.35 if i%2==0 else 1.2
    ax.text(x,yy+0.62 if i%2==0 else yy+0.72,d,ha='center',fontsize=13.5,color=c if c!=GREY else SAND,fontweight='bold')
    ax.text(x,yy,t,ha='center',va='center',fontsize=12.5,color=TXT,linespacing=1.35)
ax.add_patch(mp.FancyBboxPatch((9.9,3.75),1.1,0.7,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#FFF3C4',ec=WARN,lw=1.5))
ax.text(10.45,4.1,'연내\n발표',ha='center',va='center',fontsize=12,color=WARN,fontweight='bold',linespacing=1.2)
finish(fig,O+'fig3.png','나머지 7.3만 가구 후보지가 2026년 안에 발표됩니다',allow_outside=True,strict=False)

# fig4 네 가지 경우
fig,ax=canvas(6.4,5.2)
head(fig,'초이동 개발 계획 · 앞으로 네 가지 경우','무엇이 일어나야 하는지가 다릅니다')
cards=[('물류·공장 그린벨트','지금 흐름 그대로','지금~2030년',NAVY,'가장 가능성 큼'),
       ('연구시설·주거 개발','군부대 이전 결정','2030년대 이후',MID,''),
       ('공공주택지구 지정','연내 신규택지 포함','입주는 2030년대 중후반',WARN,''),
       ('그대로 멈춤','택지·군부대 둘 다 무산','—',SAND,'')]
for i,(t,cond,when,c,tag) in enumerate(cards):
    x=0.3+i*2.7
    ax.add_patch(mp.FancyBboxPatch((x,0.55),2.45,3.75,boxstyle='round,pad=0.02,rounding_size=0.12',fc='#F7F5F0',ec=c,lw=3 if tag else 1.5))
    ax.add_patch(mp.Rectangle((x+0.02,3.55),2.41,0.72,fc=c,ec='none'))
    ax.text(x+1.225,3.91,t,ha='center',va='center',fontsize=13.5,color='white',fontweight='bold')
    ax.text(x+1.225,3.0,'필요한 일',ha='center',fontsize=11.5,color=SAND)
    ax.text(x+1.225,2.5,cond,ha='center',fontsize=12.8,color=NAVY,fontweight='bold')
    ax.text(x+1.225,1.75,'시점',ha='center',fontsize=11.5,color=SAND)
    ax.text(x+1.225,1.25,when,ha='center',fontsize=12.5,color=TXT)
    if tag: ax.text(x+1.225,4.6,tag,ha='center',fontsize=13,color=c,fontweight='bold')
finish(fig,O+'fig4.png','감일지구는 지정에서 입주까지 10년이 넘게 걸렸습니다',allow_outside=True,strict=False)
