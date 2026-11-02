import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
O='/mnt/user-data/outputs/int/byeolnae/nangman_interior_byeolnae_fig1.png'
BR='#8C7A74'; GL='#DCE8F2'; PANEL='#A8958E'
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.02,0.1,0.96,0.76]); ax.set_xlim(0,100); ax.set_ylim(0,72); ax.axis('off')
fig.text(0.04,0.955,'비대칭 중문 · 별내 포스코더샵 시공',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'큰 문은 평소에, 작은 문은 짐 들일 때 엽니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
# front view
x0,y0=14,6; H=56; ws=9; wb=17
def leaf(x,w):
    ax.add_patch(Rectangle((x,y0),w,H,color=BR))
    ax.add_patch(Rectangle((x+1.2,y0+14),w-2.4,H-15.5,color=GL,ec='#222',lw=1.2,hatch='xx',alpha=1))
    ax.add_patch(Rectangle((x+1.2,y0+1.5),w-2.4,11,color=PANEL,ec='#222',lw=1.2))
leaf(x0,ws); leaf(x0+ws+0.4,wb)
ax.add_patch(Rectangle((x0+ws+2,y0+24),0.8,12,color='#111'))
ax.plot([x0-4,x0+ws+wb+4],[y0,y0],color=SAND,lw=2)
ax.text(x0+ws/2,y0+H+2.5,'작은 문',ha='center',fontsize=17,color=NAVY,fontweight='bold')
ax.text(x0+ws+0.4+wb/2,y0+H+2.5,'큰 문',ha='center',fontsize=17,color=NAVY,fontweight='bold')
def lab(xp,yp,xt,yt,t):
    ax.plot([xp,xt-1],[yp,yt],color=SAND,lw=1.2)
    ax.text(xt,yt,t,fontsize=17,color=NAVY,va='center')
lab(x0+ws+wb-2,y0+40,46,52,'망입 강화유리\n유리 면이 잘 보입니다')
lab(x0+ws+wb-2,y0+7,46,12,'하부고시 판\n아래쪽 자국이 덜 보입니다')
lab(x0+ws+wb+0.4,y0+28,46,31,'인디브라운 틀')
# plan view
px,py=74,16
ax.text(px+10,60,'위에서 본 모습',ha='center',fontsize=17,color=MID,fontweight='bold')
ax.plot([px-6,px+26],[py,py],color='#555',lw=4)
ax.plot([px,px],[py,py+1],color='#555')
ax.add_patch(Rectangle((px,py-0.6),6,1.2,color=BR)); ax.add_patch(Rectangle((px+6.3,py-0.6),12,1.2,color=BR))
ax.plot([px+18.3,px+18.3-0.1],[py,py+12],color=BR,lw=4)
ax.add_patch(Arc((px+18.3,py),24,24,theta1=90,theta2=180,color=WARN,lw=2,ls='--'))
ax.text(px+10,py+19,'현관 쪽',ha='center',fontsize=17,color=NAVY,fontweight='bold')
ax.text(px+10,py-7,'복도 쪽',ha='center',fontsize=17,color=NAVY,fontweight='bold')
ax.text(px+10,py+26,'큰 문이 현관 쪽으로 열려\n복도를 막지 않습니다',ha='center',fontsize=15,color=WARN)
finish(fig,O,'비대칭 중문 단점은 문이 도는 공간과 유리 면적에서 생깁니다',brand='낭만 인테리어',allow_outside=True,strict=False)
