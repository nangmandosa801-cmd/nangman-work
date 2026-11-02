import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
D='/mnt/user-data/outputs/int/onesliding/'; import os; os.makedirs(D,exist_ok=True)
render_interior('낭만 인테리어 · 중문 고르기',['원슬라이딩 중문 단점,','입구보다 옆 벽이 먼저'],'문 한 짝이 서 있을 빈 벽이 있어야 답니다','3연동 비교 · 가격 · 모루유리 · 레일',D+'nangman_interior_onesliding_thumb.png')
WALL='#EFEBE4'; FR='#2E2E2E'; GL='#DCE8F2'
def arrow(ax,x1,x2,y,c):
    ax.add_patch(FancyArrowPatch((x1,y),(x2,y),arrowstyle='<->',mutation_scale=22,color=c,lw=2.2))
# fig1
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
fig.text(0.04,0.955,'원슬라이딩 3연동 비교 · 문을 다 열었을 때',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'원슬라이딩은 옆 벽에, 3연동은 입구 안에 문이 섭니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
def panel(x0,kind):
    y0=12;H=40;W=30
    ax.add_patch(Rectangle((x0-2,y0),W+4+ (16 if kind=='one' else 8),H+3,color=WALL))
    ax.add_patch(Rectangle((x0,y0),W,H,fc='white',ec='#999',lw=1.5))
    if kind=='one':
        ax.add_patch(Rectangle((x0+W+0.6,y0),W*0.52,H,fc=GL,ec=FR,lw=2.5))
        ax.text(x0+W+0.6+W*0.26,y0+H/2,'열린\n문',ha='center',va='center',fontsize=15,color=NAVY,fontweight='bold')
        arrow(ax,x0+0.8,x0+W-0.8,y0+6,MID)
        ax.text(x0+W/2,y0+9,'지나가는 폭 넓음',ha='center',fontsize=15,color=MID,fontweight='bold')
        ax.text(x0+W+0.6+W*0.26,y0-4,'문이 설 옆 벽 필요',ha='center',fontsize=15,color=WARN,fontweight='bold')
        ax.text(x0+W/2+8,y0+H+7,'원슬라이딩',ha='center',fontsize=20,color=NAVY,fontweight='bold')
    else:
        for i in range(3):
            ax.add_patch(Rectangle((x0+W*2/3+i*0.9,y0),W/3,H,fc=GL,ec=FR,lw=2,alpha=1))
        ax.text(x0+W*5/6+1,y0+H/2,'겹친\n문 3장',ha='center',va='center',fontsize=14,color=NAVY,fontweight='bold')
        arrow(ax,x0+0.8,x0+W*2/3-0.8,y0+6,MID)
        ax.text(x0+W/3,y0+9,'약 3분의 2',ha='center',fontsize=15,color=MID,fontweight='bold')
        ax.text(x0+W/2,y0-4,'옆 벽 부담 적음',ha='center',fontsize=15,color=NAVY,fontweight='bold')
        ax.text(x0+W/2+4,y0+H+7,'3연동',ha='center',fontsize=20,color=NAVY,fontweight='bold')
panel(5,'one'); panel(62,'three')
finish(fig,D+'nangman_interior_onesliding_fig1.png','현관 안쪽에서 본 모습 · 실제 지나가는 폭은 문틀·손잡이만큼 더 좁습니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
fig.text(0.04,0.955,'원슬라이딩 중문 실측 · 옆 벽에서 볼 것',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'문이 서는 자리에 무엇이 있는지 먼저 봅니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x0,y0,W,H=4,8,26,46
ax.add_patch(Rectangle((x0-2,y0),W*2+6,H+3,color=WALL))
ax.add_patch(Rectangle((x0,y0),W,H,fc='white',ec='#999',lw=1.5)); ax.text(x0+W/2,y0+H/2,'입구',ha='center',va='center',fontsize=17,color='#888')
ax.add_patch(Rectangle((x0+W+0.8,y0),W,H,fc=GL,ec=FR,lw=2.5,alpha=0.55))
ax.text(x0+W+0.8+W/2,y0+H+2.2,'문을 열면 한 짝이 여기에 섭니다',ha='center',fontsize=15,color=WARN,fontweight='bold')
sx=x0+W+8
ax.add_patch(Rectangle((sx,y0+26),3.2,4.4,fc='white',ec=NAVY,lw=2)); ax.text(sx+1.6,y0+23.6,'①',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.add_patch(Rectangle((sx+9,y0+28),5,7,fc='#CFD6DE',ec=NAVY,lw=2)); ax.text(sx+11.5,y0+25.6,'②',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.add_patch(Rectangle((sx+16,y0),5,H*0.7,fc='#D9CFC4',ec=NAVY,lw=2)); ax.text(sx+13.2,y0+14,'③',ha='center',fontsize=16,color=NAVY,fontweight='bold')
tx=66
for i,(n,t,d) in enumerate([('①','스위치','문에 가려 손이 안 닿습니다'),('②','인터폰','문을 닫아야 화면이 보입니다'),('③','신발장 문','문을 연 채로는 못 엽니다'),('④','옆 벽 길이','문 한 짝 폭보다 짧으면 못 답니다')]):
    y=50-i*11.5
    ax.text(tx,y,n+' '+t,fontsize=18,color=NAVY,fontweight='bold',va='center')
    ax.text(tx+3.2,y-4.2,d,fontsize=14.5,color='#555',va='center')
arrow(ax,x0+W+0.8,x0+2*W+0.8,y0-3.5,WARN); ax.text(x0+W+0.8+W/2,y0-7.5,'④ 옆 벽 길이',ha='center',fontsize=15,color=WARN,fontweight='bold')
finish(fig,D+'nangman_interior_onesliding_fig2.png','스위치·인터폰은 옮길 수 있지만 전기 작업과 비용이 따로 듭니다',brand='낭만 인테리어',allow_outside=True,strict=False)
