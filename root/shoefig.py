import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
import numpy as np
from viz import NAVY, MID, SAND, WARN
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_shoe_'
WALL='#8A8578'; FLOOR='#F7F5F0'; CAB='#C9B89A'; TXT='#444'; OK='#3C7A5A'
render_interior('낭만 인테리어 · 현관',['현관 신발장,','중문과 같이 정해야 합니다'],'신발장 문과 중문 문짝이 부딪히지 않게','깊이 · 문 여는 방식 · 모양 · 아래 띄움',O+'thumb.png')
def canvas(w=11.2,h=6.0):
    fig=plt.figure(figsize=(w,h)); ax=fig.add_axes([0,0.09,1,0.91]); ax.set_xlim(0,w); ax.set_ylim(0,h*0.91); ax.set_aspect('equal'); ax.axis('off'); return fig,ax
def room(ax,x,y,w,h,top=True):
    ax.add_patch(mp.Rectangle((x,y),w,h,fc=FLOOR,ec='none'))
    for r in [(x-0.15,y-0.15,0.15,h+0.3),(x+w,y-0.15,0.15,h+0.3)]:
        ax.add_patch(mp.Rectangle(r[:2],r[2],r[3],color=WALL))
    ax.add_patch(mp.Rectangle((x-0.15,y-0.15),w*0.2+0.15,0.15,color=WALL)); ax.add_patch(mp.Rectangle((x+w*0.8,y-0.15),w*0.2+0.15,0.15,color=WALL))
    ax.text(x+w/2,y-0.45,'현관문',ha='center',fontsize=13,color=TXT)
    if top: ax.text(x+w/2,y+h+0.55,'거실',ha='center',fontsize=13,color=TXT)
def cab(ax,x,y,d,l,ly=None):  # along left wall
    ax.add_patch(mp.Rectangle((x,y),d,l,fc=CAB,ec='#8C7B5E',lw=1.2))
    ax.text(x+d/2,ly if ly else y+l/2,'신발장',rotation=90,ha='center',va='center',fontsize=13,color='#5A4A30',fontweight='bold')
def lab(ax,x,y,t,c,fs=14,**k): ax.text(x,y,t,fontsize=fs,color=c,fontweight='bold',**k)

# fig1 세 공간
fig,ax=canvas(11.2,6.2)
X,Y,W,Hh=2.2,0.8,4.0,4.0
room(ax,X,Y,W,Hh)
ax.add_patch(mp.Rectangle((X,Y+Hh),W,0.12,color=NAVY))  # 중문
cab(ax,X,Y+0.4,0.8,3.2,ly=Y+0.9)
# 신발장 문 열림 부채
for yy in [Y+0.4+0.8,Y+0.4+2.4]:
    ax.add_patch(mp.Wedge((X+0.8,yy),0.8,0,90,fc=MID,alpha=0.25,ec=MID,lw=1.5))
# 중문 움직임 (스윙 반원)
ax.add_patch(mp.Wedge((X+0.1,Y+Hh),1.9,270,360,fc=NAVY,alpha=0.2,ec=NAVY,lw=1.5))
# 사람
ax.add_patch(mp.Circle((X+2.3,Y+1.9),0.55,fc=WARN,alpha=0.35,ec=WARN,lw=1.5))
ax.text(X+2.3,Y+1.9,'사람',ha='center',va='center',fontsize=13,color=WARN,fontweight='bold')
# overlap mark
ax.add_patch(mp.Circle((X+1.35,Y+3.3),0.32,fc='none',ec='#C0392B',lw=2.5,ls='--'))
R=7.2
ax.annotate('',xy=(X+1.7,Y+3.35),xytext=(R-0.1,Y+3.35),arrowprops=dict(arrowstyle='->',color='#C0392B',lw=1.8))
lab(ax,R,Y+3.25,'여기서 부딪힙니다','#C0392B',16)
for i,(t,c) in enumerate([('① 사람이 신발을 신고 벗는 공간',WARN),('② 신발장 문이 열리는 공간',MID),('③ 중문 문짝이 움직이는 공간',NAVY)]):
    ax.add_patch(mp.Rectangle((R,Y+2.2-i*0.75),0.35,0.35,fc=c,alpha=0.35,ec=c))
    ax.text(R+0.5,Y+2.37-i*0.75,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig1.png','좁은 현관에서는 세 공간이 한 곳에 겹칩니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 슬라이딩 모이는 쪽
fig,ax=canvas(11.2,6.6)
for k,(ox,good) in enumerate([(0.9,False),(6.4,True)]):
    W,Hh=3.9,3.4; X,Y=ox,0.9
    room(ax,X,Y,W,Hh,top=False); cab(ax,X,Y+0.3,0.75,2.8,ly=Y+1.0)
    ax.add_patch(mp.Rectangle((X,Y+Hh),W,0.08,color='#B8C4D0'))  # 레일
    # 3연동 문짝 stack
    sx = X+0.05 if not good else X+W-1.35
    for j in range(3):
        ax.add_patch(mp.Rectangle((sx+j*0.1,Y+Hh-0.14-j*0.13),1.25,0.1,color=NAVY))
    lab(ax,sx+0.05,Y+Hh+0.2,'중문 문짝 세 장이 모이는 쪽',NAVY,12.5)
    if not good:
        ax.add_patch(mp.Wedge((X+0.75,Y+2.5),0.7,0,90,fc='#C0392B',alpha=0.25,ec='#C0392B',lw=1.5))
        ax.text(X+1.6,Y+2.2,'신발장 문이\n문짝에 막힘',fontsize=13,color='#C0392B',fontweight='bold')
    else:
        ax.add_patch(mp.Wedge((X+0.75,Y+2.5),0.7,0,90,fc=OK,alpha=0.25,ec=OK,lw=1.5))
        ax.text(X+1.6,Y+2.2,'중문을 열어 둬도\n신발장이 열림',fontsize=13,color=OK,fontweight='bold')
    ax.text(X+W/2,Y+Hh+0.85,'이러면 불편합니다' if not good else '이렇게 두면 편합니다',ha='center',fontsize=17,fontweight='bold',color='#C0392B' if not good else OK)
finish(fig,O+'fig2.png','슬라이딩 중문은 문짝이 모이는 쪽을 신발장 반대편으로',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig3 스윙
fig,ax=canvas(11.2,6.6)
for k,(ox,good) in enumerate([(0.9,False),(6.4,True)]):
    W,Hh=3.9,3.4; X,Y=ox,0.9
    room(ax,X,Y,W,Hh,top=False); cab(ax,X,Y+0.3,0.75,2.8,ly=Y+1.0)
    if not good:
        hx=X+0.8; ax.add_patch(mp.Wedge((hx,Y+Hh),1.8,270,360,fc=NAVY,alpha=0.18,ec=NAVY,lw=1.5))
        ax.plot([hx,hx],[Y+Hh,Y+Hh-1.8],color=NAVY,lw=4)
        ax.add_patch(mp.Wedge((X+0.75,Y+2.6),0.6,0,90,fc=MID,alpha=0.3,ec=MID,lw=1.5))
        ax.add_patch(mp.Circle((X+1.2,Y+2.75),0.28,fc='none',ec='#C0392B',lw=2.5,ls='--'))
        ax.text(X+2.0,Y+1.2,'중문이 도는 반원 안에\n신발장 문이 있음',fontsize=13,color='#C0392B',fontweight='bold')
    else:
        hx=X+W-0.1; ax.add_patch(mp.Wedge((hx,Y+Hh),1.8,180,270,fc=NAVY,alpha=0.18,ec=NAVY,lw=1.5))
        ax.plot([hx,hx],[Y+Hh,Y+Hh-1.8],color=NAVY,lw=4)
        ax.add_patch(mp.Wedge((X+0.75,Y+2.6),0.6,0,90,fc=OK,alpha=0.3,ec=OK,lw=1.5))
        ax.text(X+1.0,Y+0.9,'중문이 신발장 반대쪽으로 열림',fontsize=13,color=OK,fontweight='bold')
    ax.add_patch(mp.Rectangle((X,Y+Hh),W,0.08,color='#B8C4D0'))
    ax.text(X+W/2,Y+Hh+0.85,'이러면 부딪힙니다' if not good else '이렇게 두면 편합니다',ha='center',fontsize=17,fontweight='bold',color='#C0392B' if not good else OK)
finish(fig,O+'fig3.png','스윙 중문은 문이 도는 반원 안에 신발장 문이 없어야 합니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig4 유효폭
fig=plt.figure(figsize=(11.2,4.6)); ax=fig.add_axes([0,0.12,1,0.88]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.0); ax.axis('off')
x0=1.2
ax.add_patch(mp.Rectangle((x0,2.7),8.8,0.6,fc='#E4E0D6',ec='none')); ax.text(x0-0.15,3.0,'지금 현관 폭',ha='right',va='center',fontsize=14,color=TXT,fontweight='bold')
segs=[(2.4,CAB,'신발장 깊이'),(1.3,MID,'신발장 문이\n열리는 폭'),(0.9,NAVY,'중문 문틀 ·\n문짝')]
x=x0
for w,c,t in segs:
    ax.add_patch(mp.Rectangle((x,1.4),w,0.6,fc=c,ec='white',lw=2)); ax.text(x+w/2,0.95,t,ha='center',va='top',fontsize=13,color=TXT,linespacing=1.3); x+=w
ax.add_patch(mp.Rectangle((x,1.4),x0+8.8-x,0.6,fc=WARN,alpha=0.85,ec='white',lw=2))
ax.text(x+(x0+8.8-x)/2,1.7,'실제로 남는 폭',ha='center',va='center',fontsize=15,color='white',fontweight='bold')
ax.text(x+(x0+8.8-x)/2,0.95,'사람이 서서\n신발을 신는 폭',ha='center',va='top',fontsize=13,color=WARN,fontweight='bold',linespacing=1.3)
ax.text(x0-0.15,1.7,'다 짓고 나서',ha='right',va='center',fontsize=14,color=TXT,fontweight='bold')
finish(fig,O+'fig4.png','깊이는 지금 폭이 아니라 다 짓고 나서 남는 폭으로 정합니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig5 모양 세 가지 (정면)
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0,0.1,1,0.9]); ax.set_xlim(0,11.2); ax.set_ylim(-0.7,5.0); ax.axis('off')
ax.plot([0.4,10.8],[0.6,0.6],color=WALL,lw=3); ax.plot([0.4,10.8],[4.3,4.3],color=WALL,lw=1.5,ls=':')
ax.text(10.8,4.4,'천장',ha='right',fontsize=12,color=TXT)
def shoes(x,y,n):
    for i in range(n): ax.add_patch(mp.FancyBboxPatch((x+i*0.42,y),0.32,0.12,boxstyle='round,pad=0.02',fc='#5A4A30',ec='none'))
# 키큰장
ax.add_patch(mp.Rectangle((1.0,0.6),2.2,3.7,fc=CAB,ec='#8C7B5E',lw=1.5))
for yy in np.arange(1.05,4.2,0.55): ax.plot([1.0,3.2],[yy,yy],color='#8C7B5E',lw=0.8); shoes(1.15,yy-0.42+0.03,5)
# 하부장
ax.add_patch(mp.Rectangle((4.5,0.6),2.2,1.4,fc=CAB,ec='#8C7B5E',lw=1.5))
for yy in [1.05,1.5]: ax.plot([4.5,6.7],[yy,yy],color='#8C7B5E',lw=0.8)
for yy in [0.65,1.1,1.55]: shoes(4.65,yy,5)
ax.text(5.6,2.9,'위가 트여\n밝아 보임',ha='center',fontsize=13,color=MID,fontweight='bold')
# 벤치형
ax.add_patch(mp.Rectangle((8.0,0.6),2.6,0.75,fc=CAB,ec='#8C7B5E',lw=1.5))
ax.add_patch(mp.Rectangle((8.0,1.35),2.6,0.12,fc='#8C7B5E'))
shoes(8.2,0.75,5)
ax.text(9.3,1.9,'앉아서 신음',ha='center',fontsize=13,color=MID,fontweight='bold')
for x,t,s in [(2.1,'키큰장','많이 들어감 · 답답해 보임'),(5.6,'하부장','밝음 · 수납 적음'),(9.3,'벤치형','앉기 편함 · 폭 차지')]:
    ax.text(x,0.2,t,ha='center',fontsize=16,color=NAVY,fontweight='bold'); ax.text(x,-0.25,s,ha='center',fontsize=13,color=TXT)
finish(fig,O+'fig5.png','신발 수 · 현관 밝기 · 식구에 따라 맞는 모양이 다릅니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig6 띄움
fig=plt.figure(figsize=(11.2,5.4)); ax=fig.add_axes([0,0.1,1,0.9]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.9); ax.axis('off')
ax.plot([0.4,6.0],[0.6,0.6],color=WALL,lw=3)
ax.add_patch(mp.Rectangle((0.9,1.3),4.4,3.2,fc=CAB,ec='#8C7B5E',lw=1.5))
for xx in [2.37,3.83]: ax.plot([xx,xx],[1.3,4.5],color='#8C7B5E',lw=0.8)
# glow
for i,a in enumerate([0.35,0.22,0.12]):
    ax.add_patch(mp.Rectangle((0.9,0.6+i*0.0),4.4,0.7-i*0.2,fc='#F6D98A',alpha=a,ec='none'))
ax.plot([1.0,5.2],[1.27,1.27],color='#F2B53A',lw=3)
shoes(1.2,0.62,3); shoes(3.4,0.62,2)
for x in [1.9,3.1,4.2]: ax.add_patch(mp.Circle((x,0.66),0.03,color='#8A8578'))
ax.annotate('',xy=(5.55,1.3),xytext=(5.55,0.6),arrowprops=dict(arrowstyle='<->',color=TXT,lw=1.5)); ax.text(5.7,0.9,'띄운 높이',fontsize=13,color=TXT)
lab(ax,6.9,4.0,'얻는 것',OK,17)
for i,t in enumerate(['자주 신는 신발을 아래에','높이가 충분하면 로봇청소기','조명을 넣으면 넓어 보임']): ax.text(7.0,3.5-i*0.45,'· '+t,fontsize=14,color=TXT)
lab(ax,6.9,1.85,'잃는 것','#C0392B',17)
for i,t in enumerate(['띄운 만큼 수납이 줄어듦','먼지와 모래가 더 잘 보임']): ax.text(7.0,1.35-i*0.45,'· '+t,fontsize=14,color=TXT)
finish(fig,O+'fig6.png','중문을 달면 현관이 어두워지니 아래 조명을 같이 생각해 보십시오',brand='낭만 인테리어',allow_outside=True,strict=False)
