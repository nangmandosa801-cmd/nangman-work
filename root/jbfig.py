import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_jeongbi_'
TXT='#444'; OK='#3C7A5A'; GREY='#B8B2A6'
render('낭만 부동산 분석 플랫폼 · 부동산공법',['정비사업 종류,','조합원 되는 방법부터 다릅니다'],'재개발은 모두 · 재건축은 동의한 사람만',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def box(ax,x,y,w,h,t,fc,tc='white',fs=14,ec=None,bold=True):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',fc=fc,ec=ec or fc,lw=1.6))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=tc,fontweight='bold' if bold else 'normal',linespacing=1.35)

# fig1 tree
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0,0.09,1,0.76]); ax.set_xlim(0,11.2); ax.set_ylim(0,5); ax.axis('off')
head(fig,'정비사업 종류 · 법으로 나누기','법 세 개에 사업 여덟 개입니다')
box(ax,4.1,4.25,3.0,0.65,'정비사업',NAVY,fs=17)
laws=[(0.3,'도시정비법','큰 동네 · 큰 단지',NAVY,['주거환경개선','재개발','재건축']),
      (4.0,'소규모주택정비법','작은 동네 · 작은 단지',MID,['자율주택','가로주택','소규모재건축','소규모재개발']),
      (7.9,'노후계획도시특별법','1기 신도시 같은 계획도시',WARN,['특별정비구역'])]
for x,n,s,c,subs in laws:
    w=3.0
    ax.plot([5.6,x+w/2],[4.25,3.55],color=LINE,lw=2)
    box(ax,x,2.85,w,0.7,n,c,fs=15)
    ax.text(x+w/2,2.6,s,ha='center',fontsize=12.5,color=TXT)
    for i,t in enumerate(subs):
        y=1.9-i*0.52
        box(ax,x+0.35,y,w-0.7,0.42,t,'#F7F5F0',tc=c,fs=13.5,ec=c)
finish(fig,O+'fig1.png','어느 법으로 하는 사업인지에 따라 절차와 동의 기준이 다릅니다',allow_outside=True,strict=False)

# fig2 재개발 vs 재건축
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0,0.09,1,0.76]); ax.set_xlim(0,11.2); ax.set_ylim(0,5); ax.axis('off')
head(fig,'정비사업 종류 · 재개발과 재건축','재개발은 동네를, 재건축은 건물을 새로 짓습니다')
import random; random.seed(3)
# 재개발 panel
ax.add_patch(mp.Rectangle((0.4,0.9),4.8,3.4,fc='#F7F5F0',ec=LINE))
for i in range(22):
    x=0.55+random.random()*4.3; y=1.05+random.random()*3.0
    ax.add_patch(mp.Rectangle((x,y),0.32+random.random()*0.2,0.26+random.random()*0.15,fc='#C9B89A',ec='#8C7B5E',lw=0.8))
xs=[0.4,1.3,1.6,2.9,3.2,5.2]; ys=[2.6,2.4,2.9,2.5,2.8,2.6]
ax.plot(xs,ys,color='#A9A294',lw=2.5)
ax.plot([2.2,2.4,2.1,2.5],[0.9,1.9,2.9,4.3],color='#A9A294',lw=2)
ax.text(2.8,4.55,'재개발',ha='center',fontsize=18,color=NAVY,fontweight='bold')
ax.text(2.8,0.5,'좁고 굽은 길 · 낡은 집이 빽빽 → 길 · 공원 · 건물 모두 새로',ha='center',fontsize=12.5,color=TXT)
# 재건축 panel
ax.add_patch(mp.Rectangle((6.0,0.9),4.8,3.4,fc='#F7F5F0',ec=LINE))
for yy in [2.55]: ax.add_patch(mp.Rectangle((6.0,yy),4.8,0.28,fc='#D9D4C8'))
for xx in [8.25]: ax.add_patch(mp.Rectangle((xx,0.9),0.28,3.4,fc='#D9D4C8'))
for x0,y0 in [(6.3,1.1),(6.3,3.05),(8.8,1.1),(8.8,3.05)]:
    for k in range(2):
        ax.add_patch(mp.Rectangle((x0+k*0.8,y0),0.62,1.1,fc='#B8B2A6',ec='#8A8578',lw=0.8))
        for r in range(4):
            ax.plot([x0+k*0.8+0.08,x0+k*0.8+0.54],[y0+0.2+r*0.24]*2,color='#8A8578',lw=0.6)
ax.text(8.4,4.55,'재건축',ha='center',fontsize=18,color=NAVY,fontweight='bold')
ax.text(8.4,0.5,'반듯한 길 · 학교는 그대로 → 낡은 아파트만 새로',ha='center',fontsize=12.5,color=TXT)
finish(fig,O+'fig2.png','기반시설이 나쁘면 재개발 · 기반시설은 괜찮고 건물만 낡으면 재건축',allow_outside=True,strict=False)

# fig3 조합원
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0,0.09,1,0.76]); ax.set_xlim(0,11.2); ax.set_ylim(0,5); ax.axis('off')
head(fig,'정비사업 종류 · 조합원이 되는 방법','재개발은 모두, 재건축은 동의한 사람만 조합원입니다')
def house(x,y,c,ec):
    ax.add_patch(mp.Polygon([[x,y],[x+0.5,y],[x+0.5,y+0.4],[x+0.25,y+0.62],[x,y+0.4]],closed=True,fc=c,ec=ec,lw=1.2))
for row,(name,y,cols,notes) in enumerate([
    ('재개발',3.2,[NAVY]*7+[NAVY]*3,('10명 모두 조합원','반대한 3명도 조합원\n원하지 않으면 수용으로 보상')),
    ('재건축',1.1,[OK]*7+[GREY]*3,('동의한 7명만 조합원','동의하지 않은 3명 → 매도청구'))]):
    ax.text(0.35,y+0.3,name,fontsize=18,color=NAVY,fontweight='bold',va='center')
    for i,c in enumerate(cols):
        house(1.7+i*0.62,y,c,'white' if c!=GREY else '#8A8578')
    for i in range(7,10):
        ax.text(1.95+i*0.62,y-0.28,'반대',ha='center',fontsize=11.5,color=WARN if name=='재개발' else '#8A8578',fontweight='bold')
    ax.text(8.1,y+0.75,notes[0],fontsize=15,color=NAVY if name=='재개발' else OK,fontweight='bold')
    ax.text(8.1,y+0.35,notes[1],fontsize=12.5,color=TXT,va='top',linespacing=1.5)
ax.plot([0.3,10.9],[2.35,2.35],color=LINE,lw=1.2)
finish(fig,O+'fig3.png','예시 · 구역 안 집주인 10명 가운데 3명이 반대한 경우',allow_outside=True,strict=False)

# fig4 소규모 네 가지
fig=plt.figure(figsize=(11.2,6.0)); ax=fig.add_axes([0,0.09,1,0.76]); ax.set_xlim(0,11.2); ax.set_ylim(0,5); ax.axis('off')
head(fig,'정비사업 종류 · 소규모주택정비법','작은 동네는 네 가지로 새로 짓습니다')
cells=[(0.3,'자율주택정비','이웃 몇 집이 모여 함께'),(3.0,'가로주택정비','도로로 둘러싸인 한 블록'),(5.7,'소규모재건축','작은 아파트 단지'),(8.4,'소규모재개발','역 가까운 곳 · 준공업지역')]
for x,t,s in cells:
    ax.add_patch(mp.FancyBboxPatch((x,1.0),2.5,3.2,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#F7F5F0',ec=MID,lw=1.8))
    ax.text(x+1.25,3.85,t,ha='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(x+1.25,0.65,s,ha='center',fontsize=12.5,color=TXT)
# 자율
for i in range(3): house(0.65+i*0.62,2.0,'#C9B89A','#8C7B5E')
ax.add_patch(mp.FancyBboxPatch((0.55,1.85),1.95,0.95,boxstyle='round,pad=0.02',fc='none',ec=WARN,lw=1.8,ls='--'))
# 가로
ax.add_patch(mp.Rectangle((3.25,1.4),2.0,2.1,fc='#D9D4C8'))
ax.add_patch(mp.Rectangle((3.5,1.65),1.5,1.6,fc='#F7F5F0',ec=WARN,lw=1.8,ls='--'))
for i in range(2):
    for j in range(2): house(3.62+i*0.72,1.8+j*0.72,'#C9B89A','#8C7B5E')
ax.text(4.25,1.45,'도로',ha='center',fontsize=10.5,color='#6E6A62',va='bottom')
# 소규모재건축
for k in range(3):
    ax.add_patch(mp.Rectangle((6.05+k*0.62,1.6),0.48,1.5,fc='#B8B2A6',ec='#8A8578'))
ax.add_patch(mp.FancyBboxPatch((5.95,1.5),1.95,1.75,boxstyle='round,pad=0.02',fc='none',ec=WARN,lw=1.8,ls='--'))
# 소규모재개발
ax.add_patch(mp.Circle((9.65,2.4),1.0,fc='none',ec=MID,lw=1.5,ls=':'))
box(ax,9.4,2.25,0.5,0.3,'역',NAVY,fs=11)
for dx,dy in [(-0.85,0.45),(0.35,0.55),(-0.75,-0.6),(0.3,-0.65)]: house(9.65+dx,2.4+dy-0.2,'#C9B89A','#8C7B5E')
ax.text(9.65,3.5,'승강장 350m',ha='center',fontsize=11,color=MID)
finish(fig,O+'fig4.png','정비구역 지정과 추진위원회 단계를 건너뛰어 기간이 짧습니다',allow_outside=True,strict=False)
