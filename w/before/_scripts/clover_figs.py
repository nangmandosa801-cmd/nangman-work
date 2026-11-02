import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, FancyArrowPatch, Polygon
from viz import NAVY, MID, SAND, WARN, LINE, PALE
from note import finish
O='/mnt/user-data/outputs/int/'; BL='#3E5470'; GR='#8A8578'
def base(kick,title):
    fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
    fig.text(0.04,0.955,kick,fontsize=17,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
    return fig,ax
def wall(ax,x0,x1,y,h=2.4,c=GR): ax.add_patch(Rectangle((x0,y-h/2),x1-x0,h,color=c))
def cab(ax,x0,x1,y0,y1,label=None):
    ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor='#BDB7AB',edgecolor=GR,lw=1.5))
    if label: ax.text((x0+x1)/2,(y0+y1)/2,label,ha='center',va='center',fontsize=14,color='white',fontweight='bold',rotation=90)
def leaf(ax,hx,y,L,ang,arc=True):
    import math
    ex=hx+L*math.cos(math.radians(ang)); ey=y+L*math.sin(math.radians(ang))
    ax.plot([hx,ex],[y,ey],color=BL,lw=5,solid_capstyle='round')
    if arc:
        a0,a1=(0,ang) if ang<=90 else (ang,180)
        ax.add_patch(Arc((hx,y),2*L,2*L,theta1=a0,theta2=a1,color=WARN,lw=2,ls='--'))
def fin(fig,slug,note): finish(fig,O+f'{slug}/nangman_interior_{slug}_fig1.png',note,brand='낭만 인테리어',allow_outside=True,strict=False)

# A 정대칭 vs 비대칭
fig,ax=base('스윙도어 중문 · 위에서 본 모습','두 짝 폭이 같으면 정대칭, 다르면 비대칭입니다')
y=22
for cx,name,(l,r),sub in [(26,'정대칭',(14,14),'두 짝이 같은 폭'),(74,'비대칭',(20,8),'큰 문 + 작은 문')]:
    x0=cx-14; x1=cx+14
    cab(ax,x0-7,x0,y-14,y+30,'수납장'); cab(ax,x1,x1+7,y-14,y+30,'수납장')
    leaf(ax,x0,y,l,78); leaf(ax,x1,y,r,102)
    ax.plot([x0,x1],[y,y],color=LINE,lw=2,ls=':')
    ax.text(cx,y+38,name,ha='center',fontsize=21,color=NAVY,fontweight='bold')
    ax.text(cx,y+33,sub,ha='center',fontsize=15,color=MID,fontweight='bold')
    ax.text(cx,y-7,'현관',ha='center',fontsize=14,color=SAND); ax.text(cx,y+24,'거실 쪽',ha='center',fontsize=14,color=SAND)
ax.text(26,y-13,'입구가 넉넉한 집',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.text(74,y-13,'입구가 좁은 집 · 평소엔 큰 문만',ha='center',fontsize=15,color=WARN,fontweight='bold')
fin(fig,'daejeon_doan','점선은 문이 도는 길입니다 · 이 바닥에는 신발과 화분을 둘 수 없습니다')

# B 파티션 → ㄱ자
fig,ax=base('현관 파티션과 ㄱ자 중문 · 위에서 본 모습','파티션은 옆만 가리고, ㄱ자 중문은 앞까지 막습니다')
for cx,name in [(26,'시공 전 · 파티션'),(74,'시공 뒤 · ㄱ자 중문')]:
    x0=cx-16; x1=cx+16; y0=10; y1=40
    wall(ax,x0,x1,y0-1.2)                       # 현관문 쪽 벽
    ax.add_patch(Rectangle((cx-5,y0-2.4),10,2.4,color='#5B4A3A')); ax.text(cx,y0-6,'현관문',ha='center',fontsize=13,color=SAND)
    ax.add_patch(Rectangle((x1-1.2,y0),2.4,y1-y0,color=GR))          # 오른쪽 벽(신발장 쪽)
    cab(ax,x1-7,x1-1.2,y0+2,y1-4,'신발장')
    ax.text(cx+3,y0+5,'현관',ha='center',fontsize=14,color=SAND)
    ax.text(cx,y1+17,name,ha='center',fontsize=20,color=NAVY,fontweight='bold')
# before
cx=26; x0=cx-16; x1=cx+16; y0=10; y1=40
ax.add_patch(Rectangle((x0-1,y0),2,y1-y0-8,color='#3B4252')); ax.text(x0-4,y0+11,'파티션',ha='center',va='center',fontsize=14,color='#3B4252',fontweight='bold',rotation=90)
ax.add_patch(FancyArrowPatch((cx-7,y0+6),(cx-7,y1+8),arrowstyle='-|>',mutation_scale=22,color=WARN,lw=2.5))
ax.text(cx-7,y1+11,'바람 · 냄새 · 소리',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.text(cx+4,y1+3,'앞이 뚫려 있음',ha='center',fontsize=14,color=MID,fontweight='bold')
# after
cx=74; x0=cx-16; x1=cx+16
ax.add_patch(Rectangle((x0-0.8,y0),1.6,y1-y0,color=BL)); ax.text(x0-4,y0+15,'옆 고정벽 (아쿠아유리)',ha='center',va='center',fontsize=14,color=BL,fontweight='bold',rotation=90)
for k,(a,b,dy) in enumerate([(x0,x0+10,0),(x0+9,x0+19,1.3),(x0+18,x1-1.2,2.6)]):
    ax.add_patch(Rectangle((a,y1-0.6+dy),b-a,1.1,color=BL))
ax.text(cx,y1+7,'앞 3연동 문 (세 짝이 겹쳐 열림)',ha='center',fontsize=15,color=BL,fontweight='bold')
ax.text(cx,y1+11.5,'바람 · 냄새 · 소리 막힘',ha='center',fontsize=15,color=WARN,fontweight='bold')
fin(fig,'daejeon_dure','옆면은 열리지 않는 벽, 앞면은 여닫는 문으로 나눕니다')

# C 유리 세 가지 정면
fig,ax=base('중문 유리 · 정면에서 본 모습','모루유리에 아래를 막으면 신발이 안 보입니다')
import numpy as np
for cx,name,kind,l1,l2 in [(18,'투명 통유리','clear','현관 안이 그대로 보임','신발 · 택배 상자도 보임'),(50,'모루유리','moru','형체만 흐리게 보임','아래로 신발은 비침'),(82,'모루유리 + 1단 고시','gosi','형체만 흐리게 보임','아래는 판으로 막아 안 보임')]:
    x0=cx-11; x1=cx+11; y0=8; y1=52
    ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor='#F4F7FA',edgecolor='#9AA4AE',lw=4))
    gy0=y0+13 if kind=='gosi' else y0
    if kind!='clear':
        for xx in np.arange(x0+0.9,x1-0.2,0.9): ax.plot([xx,xx],[gy0+0.6,y1-0.6],color='#C9B79B',lw=1.3)
    if kind=='gosi': ax.add_patch(Rectangle((x0,y0),x1-x0,13,facecolor='#9AA4AE',edgecolor='#9AA4AE',lw=4)); ax.text(cx,y0+6.5,'막힌 판',ha='center',va='center',fontsize=14,color='white',fontweight='bold')
    # 사람 실루엣과 신발
    al=1.0 if kind=='clear' else 0.28
    ax.add_patch(plt.Circle((cx,y0+34),3.2,color=NAVY,alpha=al)); ax.add_patch(Rectangle((cx-4,y0+15),8,15.5,color=NAVY,alpha=al))
    if kind!='gosi': ax.add_patch(Rectangle((cx-8,y0+1),5,2.2,color=WARN,alpha=1.0 if kind=='clear' else 0.45)); ax.add_patch(Rectangle((cx+2,y0+1),5,2.2,color=WARN,alpha=1.0 if kind=='clear' else 0.45))
    ax.add_patch(Rectangle((x0+1.2,y0+20),0.9,6,color='#222'))
    ax.text(cx,y1+9,name,ha='center',fontsize=19,color=NAVY,fontweight='bold')
    ax.text(cx,y1+4,l1,ha='center',fontsize=14,color=MID,fontweight='bold')
    ax.text(cx,y0-5,l2,ha='center',fontsize=14,color=WARN,fontweight='bold')
fin(fig,'cheongju_jiwell','고시는 유리 대신 막힌 판을 넣은 칸입니다 · 아래 한 칸이면 1단 고시')

# D 비대칭: 평소 vs 큰 짐
fig,ax=base('비대칭 스윙도어 · 위에서 본 모습','평소엔 큰 문 하나, 큰 짐이 올 때만 두 짝을 엽니다')
y=30
for cx,name,both in [(26,'평소',False),(74,'이사 · 큰 짐',True)]:
    x0=cx-14; x1=cx+14; sm=8; big=20
    cab(ax,x0-7,x0,y-8,y+22,'수납장'); cab(ax,x1,x1+7,y-8,y+22,'수납장')
    # 큰 문: 오른쪽 경첩, 현관(아래) 쪽으로 열림
    import math
    ax.plot([x1,x1+0.0-big*math.cos(math.radians(75))],[y,y-big*math.sin(math.radians(75))],color=BL,lw=5,solid_capstyle='round')
    ax.add_patch(Arc((x1,y),2*big,2*big,theta1=180,theta2=255,color=WARN,lw=2,ls='--'))
    if both:
        ax.plot([x0,x0+sm*math.cos(math.radians(80))],[y,y-sm*math.sin(math.radians(80))],color=BL,lw=5,solid_capstyle='round')
        ax.add_patch(Arc((x0,y),2*sm,2*sm,theta1=280,theta2=360,color=WARN,lw=2,ls='--'))
        ax.add_patch(FancyArrowPatch((x0+2.5,y+3),(x1-6.5,y+3),arrowstyle='<->',mutation_scale=18,color=WARN,lw=2)); ax.text(cx-2,y+6,'입구 전체',ha='center',fontsize=15,color=WARN,fontweight='bold')
    else:
        ax.plot([x0,x0+sm],[y,y],color=BL,lw=5,solid_capstyle='round'); ax.text(x0+sm/2,y+5.5,'작은 문\n닫아 둠',ha='center',fontsize=13,color=NAVY,fontweight='bold')
        ax.add_patch(FancyArrowPatch((x0+sm+0.5,y+3),(x1-6.5,y+3),arrowstyle='<->',mutation_scale=18,color=WARN,lw=2)); ax.text(x0+sm+7.5,y+6,'큰 문 폭',ha='center',fontsize=15,color=WARN,fontweight='bold')
    ax.text(cx,y+30,name,ha='center',fontsize=21,color=NAVY,fontweight='bold')
    ax.text(cx,y+15,'복도 쪽',ha='center',fontsize=14,color=SAND); ax.text(cx-8,y-17,'현관',ha='center',fontsize=14,color=SAND)
    ax.text(x1-9,y-24,'큰 문이 도는 길',ha='center',fontsize=14,color=WARN,fontweight='bold')
fin(fig,'sejong_surubae','작은 문은 위아래를 걸어 고정해 두고, 큰 짐이 올 때만 풉니다')
print('ok')
