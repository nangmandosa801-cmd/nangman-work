import sys,math; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, Arc, FancyBboxPatch
from viz import NAVY, MID, SAND, WARN, LINE, PALE
from note import finish
O='/mnt/user-data/outputs/int/ipju_gwanjeo/nangman_interior_ipju_gwanjeo_'
GR='#8A8578'; BL='#3E5470'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.905,fs=23):
    fig.text(0.04,y1,sub,fontsize=15.5,color=MID,va='center'); fig.text(0.04,y2,title,fontsize=fs,color=NAVY,fontweight='bold',va='center')

# fig1 가격
fig=plt.figure(figsize=(11.2,7.2)); ax=fig.add_axes([0.36,0.15,0.60,0.58])
head(fig,'관저 푸르지오 센트럴파크 입주자모집공고 · 입주 뒤 다는 가격은 자주 보이는 범위','옵션은 자동 235만원, 따로 다는 3연동은 55만~90만원대입니다',0.95,0.88,22)
R=[('옵션 · 3연동 자동 (한 가지)',235,235,WARN,'235만원'),('입주 뒤 · 손으로 여는 3연동',55,90,NAVY,'55만~90만원대 + 틀 세우는 비용'),('참고 · 서대전역 센트로 옵션 자동',365,365,SAND,'365만원')]
n=len(R)
for i,(nm,a,b,c,t) in enumerate(R):
    y=n-1-i
    if a==b: ax.barh(y,b,0.52,color=c)
    else:
        ax.barh(y,a,0.52,color=c); ax.barh(y,b-a,0.52,left=a,color=c,alpha=0.45)
    ax.text(b+8,y,t,va='center',fontsize=16,color=c if c!=SAND else GR,fontweight='bold')
    ax.text(-8,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,560); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig1.png','같은 조건이 아닙니다 · 옵션은 자동이고 틀까지 들어 있습니다 · 따로 달면 유리와 색을 고릅니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 고를 수 있는 것
fig=plt.figure(figsize=(11.2,9.6)); ax=fig.add_axes([0.02,0.08,0.96,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
head(fig,'옵션은 3연동 자동 한 가지 · 유리와 색은 정해져 있었습니다','입주 뒤에 달면 문 종류, 유리, 틀 색을 고릅니다',0.96,0.915)
def row(y,label): ax.text(3,y+7,label,fontsize=19,color=NAVY,fontweight='bold',va='center')
# 문 종류
row(58,'문 종류')
for k,(nm,sub) in enumerate([('3연동','세 짝이 겹칩니다'),('스윙도어','앞으로 돌며 열립니다'),('원슬라이딩','한 짝이 옆으로 빠집니다')]):
    cx=30+k*25; y=62
    ax.add_patch(FancyBboxPatch((cx-10,y-8),20,20,boxstyle='round,pad=0.3,rounding_size=1.2',fc='#F4F6FA',ec=LINE,lw=1.5))
    ax.plot([cx-8,cx+8],[y,y],color=LINE,lw=2,ls=':')
    if k==0:
        for dy in (0,1.3,2.6): ax.add_patch(Rectangle((cx+2,y-0.5+dy),6,1.0,color=BL))
    elif k==1:
        for hx,ang in [(cx-8,70),(cx+8,110)]:
            ax.plot([hx,hx+7.5*math.cos(math.radians(ang))],[y,y+7.5*math.sin(math.radians(ang))],color=BL,lw=5,solid_capstyle='round')
    else:
        ax.add_patch(Rectangle((cx+1,y+1.6),8.5,1.0,color=BL)); ax.add_patch(Rectangle((cx+1,y-0.9),8.5,1.6,color=GR)); ax.text(cx+5.2,y-3.6,'옆 벽',ha='center',fontsize=10.5,color=GR)
    ax.text(cx,y-12.5,nm,ha='center',fontsize=17,color=NAVY,fontweight='bold'); ax.text(cx,y-16.5,sub,ha='center',fontsize=12.5,color=MID)
# 유리
row(30,'유리')
G=[('투명','안이 비칩니다','#EAF2F8',None),('모루','세로 무늬 · 흐리게','#EEF3F6','v'),('브론즈','어두운 빛 · 흐리게','#B79B7A',None),('망입','철망이 든 유리','#E9EEF0','g')]
for k,(nm,sub,fc,pat) in enumerate(G):
    cx=26+k*19.5; y=27
    ax.add_patch(Rectangle((cx-7,y),14,15,fc=fc,ec=BL,lw=2.5))
    if pat=='v':
        for i in range(1,14): ax.plot([cx-7+i,cx-7+i],[y+0.4,y+14.6],color='#B8C7D3',lw=1.6)
    if pat=='g':
        for i in range(1,7): ax.plot([cx-7+i*2,cx-7+i*2],[y+0.4,y+14.6],color='#9AA7B0',lw=0.9)
        for i in range(1,8): ax.plot([cx-6.6,cx+6.6],[y+i*1.9,y+i*1.9],color='#9AA7B0',lw=0.9)
    ax.text(cx,y-3.5,nm,ha='center',fontsize=17,color=NAVY,fontweight='bold'); ax.text(cx,y-7.5,sub,ha='center',fontsize=12.5,color=MID)
# 틀 색
row(2,'틀 색')
for k,(nm,fc,ec) in enumerate([('화이트','#FFFFFF','#B8BEC6'),('우드','#B88A5A','#8A6238'),('블랙','#2A2D33','#2A2D33')]):
    cx=30+k*25; y=6
    ax.add_patch(Rectangle((cx-9,y),18,5.5,fc=fc,ec=ec,lw=2.2)); ax.text(cx,y-3.6,nm,ha='center',fontsize=17,color=NAVY,fontweight='bold')
finish(fig,O+'fig2.png','유리와 색은 업체와 제품에 따라 더 있습니다 · 현관 사진을 보내 주시면 바꾼 모습을 그림으로 보여 드립니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig3 옵션 넣은 집 vs 안 넣은 집
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.02,0.10,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
head(fig,'관저 푸르지오 센트럴파크 모집공고에 적힌 내용을 그림으로 옮김 · 위에서 본 모습','옵션을 안 넣은 집은 중문틀이 없습니다')
for cx,name in [(26,'옵션을 넣은 집'),(74,'옵션을 안 넣은 집')]:
    x0=cx-15; x1=cx+15; y0=8; y1=40
    ax.add_patch(Rectangle((x0-1.2,y0-1.2),x1-x0+2.4,2.4,color=GR))
    ax.add_patch(Rectangle((cx-5,y0-1.8),10,3.0,color='#5B4A3A')); ax.text(cx,y0-5.5,'현관문',ha='center',fontsize=13,color=SAND)
    ax.add_patch(Rectangle((x0-1.2,y0),1.2,y1-y0+10,color=GR)); ax.add_patch(Rectangle((x1,y0),1.2,y1-y0+10,color=GR))
    ax.add_patch(Rectangle((x1-7,y0+2),7,y1-y0-4,facecolor='#BDB7AB',edgecolor=GR,lw=1.5)); ax.text(x1-3.5,(y0+y1)/2,'신발장',ha='center',va='center',fontsize=14,color='white',fontweight='bold',rotation=90)
    ax.text(x0+4.5,y0+4,'현관',ha='center',fontsize=14,color=SAND); ax.text(x0+5.5,y1+8,'거실 쪽',ha='center',fontsize=14,color=SAND)
    ax.text(cx,y1+21,name,ha='center',fontsize=21,color=NAVY,fontweight='bold')
cx=26; x0=cx-15; x1=cx+15; y1=40
for a,b,dy in [(x0,x0+11,0),(x0+9.5,x0+20.5,1.4),(x0+19,x1,2.8)]: ax.add_patch(Rectangle((a,y1-0.6+dy),b-a,1.2,color=BL))
ax.text(cx-1,y1+14,'3연동 자동 중문 (235만원)',ha='center',fontsize=14.5,color=BL,fontweight='bold')
ax.add_patch(FancyArrowPatch((cx-1,y1+12.5),(cx-1,y1+4.6),arrowstyle='-|>',mutation_scale=16,color=BL,lw=2))
ax.add_patch(Circle((cx-6,25),1.6,color=WARN)); ax.text(cx-6,20.5,'현관\n화재감지기',ha='center',va='top',fontsize=14,color=WARN,fontweight='bold')
cx=74; x0=cx-15; x1=cx+15
ax.plot([x0,x1],[y1,y1],color=WARN,lw=2.4,ls='--')
ax.text(cx-1,y1+14,'중문틀 없음 · 틀부터 세웁니다',ha='center',fontsize=14.5,color=WARN,fontweight='bold')
ax.add_patch(FancyArrowPatch((cx-1,y1+12.5),(cx-1,y1+1.2),arrowstyle='-|>',mutation_scale=16,color=WARN,lw=2))
ax.add_patch(Circle((cx-6,25),1.6,fill=False,ec=WARN,lw=2.2,ls='--')); ax.text(cx-6,20.5,'감지기가\n없을 수 있음',ha='center',va='top',fontsize=14,color=WARN,fontweight='bold')
finish(fig,O+'fig3.png','실제 현관 모양은 타입마다 다릅니다 · 감지기를 더 달아야 하는지는 관리사무소에 먼저 물어보세요',brand='낭만 인테리어',allow_outside=True,strict=False)
print('figs ok')
