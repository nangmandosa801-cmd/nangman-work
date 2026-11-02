import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, math
from matplotlib.patches import Rectangle, Arc, FancyArrowPatch, Wedge, PathPatch
from matplotlib.path import Path
from viz import NAVY, MID, SAND, WARN, LINE, PALE
from note import finish
O='/mnt/user-data/outputs/int/'; BL='#3E5470'; GR='#8A8578'
def base(kick,title):
    fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
    fig.text(0.04,0.955,kick,fontsize=17,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
    return fig,ax
def wall(ax,x0,x1,y,h=2.4,c=GR): ax.add_patch(Rectangle((x0,y-h/2),x1-x0,h,color=c))
def box(ax,x0,x1,y0,y1,label,rot=0):
    ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor='#BDB7AB',edgecolor=GR,lw=1.5)); ax.text((x0+x1)/2,(y0+y1)/2,label,ha='center',va='center',fontsize=14,color='white',fontweight='bold',rotation=rot)
def fin(fig,slug,note): finish(fig,O+f'{slug}/nangman_interior_{slug}_fig1.png',note,brand='낭만 인테리어',allow_outside=True,strict=False)

# 1 사상: 원슬라이딩 vs 여닫이
fig,ax=base('원슬라이딩과 여닫이 · 위에서 본 모습','원슬라이딩은 문이 벽 앞으로 가서 섭니다')
y=30
# 원슬라이딩
wall(ax,4,10,y); wall(ax,26,46,y)
ax.add_patch(Rectangle((27,y+1.7),16,1.4,color=BL)); ax.text(35,y+6,'열린 문이 서는 곳',ha='center',fontsize=14,color=BL,fontweight='bold')
ax.add_patch(FancyArrowPatch((12,y+2.4),(25,y+2.4),arrowstyle='-|>',mutation_scale=20,color=BL,lw=2))
ax.add_patch(FancyArrowPatch((27,y-4),(43,y-4),arrowstyle='<->',mutation_scale=16,color=WARN,lw=1.8)); ax.text(35,y-8.5,'옆 벽이 문 폭만큼 필요',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.text(18,y-6,'입구',ha='center',fontsize=15,color=SAND,fontweight='bold'); ax.text(25,y+24,'원슬라이딩',ha='center',fontsize=21,color=NAVY,fontweight='bold')
ax.text(25,y+18,'문이 복도로 튀어나오지 않음',ha='center',fontsize=15,color=MID,fontweight='bold')
# 여닫이
wall(ax,56,62,y); wall(ax,78,96,y); L=16
ax.plot([62,62+L*math.cos(math.radians(80))],[y,y+L*math.sin(math.radians(80))],color=BL,lw=5,solid_capstyle='round')
ax.add_patch(Wedge((62,y),L,0,80,facecolor='#F3D9D0',edgecolor='none')); ax.add_patch(Arc((62,y),2*L,2*L,theta1=0,theta2=80,color=WARN,lw=2,ls='--'))
ax.text(70,y-6,'입구',ha='center',fontsize=15,color=SAND,fontweight='bold'); ax.text(76,y+24,'여닫이 (스윙)',ha='center',fontsize=21,color=NAVY,fontweight='bold')
ax.text(76,y+18,'옆 벽은 없어도 됨',ha='center',fontsize=15,color=MID,fontweight='bold')
ax.text(86,y+9,'문이 도는 바닥을\n비워야 함',ha='center',fontsize=15,color=WARN,fontweight='bold')
fin(fig,'busan_sasang','옆 벽이 있으면 원슬라이딩, 벽이 없으면 여닫이나 3연동을 봅니다')

# 2 당감: 닫힘/열림과 수납장
fig,ax=base('원슬라이딩 · 위에서 본 모습','문을 열면 수납장 앞에 문이 섭니다')
for cx,name,opened in [(26,'문을 닫았을 때',False),(74,'문을 열었을 때',True)]:
    x0=cx-20; y=26
    wall(ax,x0,x0+4,y); wall(ax,x0+20,x0+40,y)
    box(ax,x0+21,x0+39,y+4.2,y+12,'수납장')
    if opened:
        ax.add_patch(Rectangle((x0+21,y+1.6),17,1.5,color=BL)); ax.text(x0+30,y-6,'수납장 문을 못 엶',ha='center',fontsize=15,color=WARN,fontweight='bold')
        ax.text(x0+12,y-6,'입구 전체 열림',ha='center',fontsize=14,color=MID,fontweight='bold')
    else:
        ax.add_patch(Rectangle((x0+4,y+1.6),17,1.5,color=BL)); ax.text(x0+30,y-6,'수납장 쓸 수 있음',ha='center',fontsize=15,color=MID,fontweight='bold')
        ax.text(x0+12,y-6,'문 닫힘',ha='center',fontsize=14,color=SAND,fontweight='bold')
    ax.text(cx,y+26,name,ha='center',fontsize=21,color=NAVY,fontweight='bold')
    ax.text(x0+12,y+16,'거실 쪽',ha='center',fontsize=14,color=SAND); ax.text(x0+12,y-13,'현관',ha='center',fontsize=14,color=SAND)
fin(fig,'busan_danggam','문이 서는 벽에 무엇이 있는지 달기 전에 먼저 봅니다')

# 3 김해: 자동 중문 정면
fig,ax=base('자동 중문 · 정면에서 본 모습','위쪽 레일에 장치가 들어가고 전선 한 가닥이 필요합니다')
x0,x1,y0,y1=30,58,6,50
ax.add_patch(Rectangle((x0-16,y0),x1-x0+16,y1-y0,facecolor='#F2F0EB',edgecolor='none'))   # 벽
ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor='#C9B79B',edgecolor='#9AA4AE',lw=4,alpha=0.85))  # 문(브론즈)
ax.add_patch(Rectangle((x0-16,y1),x1-x0+16,4.5,facecolor='#E3E6EA',edgecolor='#9AA4AE',lw=2))  # 상부 레일
ax.add_patch(plt.Circle((x0+14,y1+2.2),1.1,color='#222'))  # 센서
ax.plot([x0-16,x0-16],[y1+4.5,y1+12],color=WARN,lw=2.5); ax.plot([x0-16,x0-8],[y1+12,y1+12],color=WARN,lw=2.5)
ax.add_patch(Rectangle((x0-16,y0-1.2),x1-x0+16,1.2,color='#9AA4AE'))  # 하부 레일
ax.add_patch(Rectangle((x0+2,y0+18),0.9,7,color='#222'))
def lab(x,y,t,c=NAVY,tx=66): 
    ax.add_patch(FancyArrowPatch((tx-1,y),(x,y),arrowstyle='-|>',mutation_scale=14,color=c,lw=1.6)); ax.text(tx,y,t,va='center',fontsize=15,color=c,fontweight='bold')
lab(x0+15.5,y1+2.2,'센서 · 사람이 서면 문이 열림')
lab(x1+0.5,y1+7.5,'위쪽 레일 · 장치가 들어가 두꺼움',MID)
lab(x0-7.5,y1+12,'전선 한 가닥 · 미리 빼 둠',WARN)
lab(x1+0.5,y0-0.6,'바닥 레일 · 문이 흔들리지 않게 잡아 줌',MID)
lab(x0+3.5,y0+21.5,'손잡이 · 없어도 되고 달 수도 있음',SAND)
fin(fig,'gimhae_gusan','도배를 새로 한다면 전선 빼는 곳을 도배 전에 정합니다')

# 4 창원: 아치 정면
fig,ax=base('아치 중문 · 정면에서 본 모습','네모난 문틀 안에 유리만 둥글게 넣습니다')
x0,x1,y0,y1=34,62,6,54; r=(x1-x0)/2-2.5; cx=(x0+x1)/2; gy0=y0+3; top=y1-3-r; split=y0+16
ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor='#FAFAF8',edgecolor='#9AA4AE',lw=4))
th=np.linspace(0,np.pi,60); xs=cx+r*np.cos(th); ys=top+r*np.sin(th)
verts=[(cx+r,gy0)]+list(zip(xs,ys))+[(cx-r,gy0),(cx+r,gy0)]
ax.add_patch(PathPatch(Path(verts),facecolor='#E4EEF5',edgecolor='#9AA4AE',lw=2.5))
ax.add_patch(Rectangle((cx-r,gy0),2*r,split-gy0,facecolor='#EDEFF0',edgecolor='#9AA4AE',lw=2))
for xx in np.arange(cx-r+0.8,cx+r-0.2,0.85): ax.plot([xx,xx],[gy0+0.4,split-0.4],color='#B9C2CA',lw=1.2)
ax.add_patch(plt.Circle((cx,split+15),3,color=NAVY,alpha=0.85)); ax.add_patch(Rectangle((cx-3.8,split+1),7.6,10.6,color=NAVY,alpha=0.85))
ax.add_patch(Rectangle((x0+0.9,y0+22),0.9,7,color='#9AA4AE'))
def lab(x,y,t,c=NAVY,tx=70):
    ax.add_patch(FancyArrowPatch((tx-1,y),(x,y),arrowstyle='-|>',mutation_scale=14,color=c,lw=1.6)); ax.text(tx,y,t,va='center',fontsize=15,color=c,fontweight='bold')
lab(cx+r*0.72,top+r*0.7,'둥근 선 · 유리를 둥글게 깎음')
lab(x1-1,y1-2,'둥근 선 바깥 · 틀과 같은 흰 판',SAND)
lab(cx+r,split+10,'위쪽 투명 유리 · 그대로 보임',MID)
lab(cx+r,gy0+6,'아래쪽 모루유리 · 신발을 흐리게 가림',WARN)
ax.text(18,30,'문틀은\n네모',ha='center',fontsize=16,color=SAND,fontweight='bold')
fin(fig,'changwon_daewon','아래를 흐린 유리로 넣으면 가리면서도 빛이 들어옵니다')
print('ok')
