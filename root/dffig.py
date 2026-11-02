import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from viz import NAVY, MID, SAND, WARN
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/'
render_interior('낭만 인테리어 · 창문 단열',['창문 단열필름,','붙이기 전에 유리부터 봅니다'],'복층유리라고 아무 필름이나 붙이면 안 됩니다','이름보다 성능표, 필름보다 우리 집 유리',O+'nangman_interior_danyeolfilm_thumb.png')

fig=plt.figure(figsize=(11.2,5.3)); ax=fig.add_axes([0,0.1,1,0.9]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.9); ax.axis('off')
# window: frame
FX,FY,FW,FH=0.9,0.45,4.2,3.9
ax.add_patch(mp.Rectangle((FX,FY),FW,FH,color='#8A8578'))
gx,gy,gw,gh=FX+0.3,FY+0.3,FW-0.6,FH-0.6
# gradient glass: hot center, cool edge
n=200; yy,xx=np.mgrid[-1:1:n*1j,-1:1:n*1j]; r=np.maximum(abs(xx),abs(yy))
cm=LinearSegmentedColormap.from_list('c',['#D9785E','#F2C9B8','#C7D6E6','#6F93BA'])
ax.imshow(r,extent=(gx,gx+gw,gy,gy+gh),cmap=cm,vmin=0,vmax=1,zorder=2)
ax.text(gx+gw/2,gy+gh/2+0.25,'가운데',ha='center',fontsize=17,fontweight='bold',color='#7A2E1C',zorder=3)
ax.text(gx+gw/2,gy+gh/2-0.2,'햇빛에 뜨거워짐',ha='center',fontsize=14,color='#7A2E1C',zorder=3)
for dx,dy,ang in [(0.75,0,0),(-0.75,0,180),(0,0.62,90),(0,-0.62,270)]:
    x0,y0=gx+gw/2+dx*0.55,gy+gh/2+0.03+dy*0.55
    ax.annotate('',xy=(x0+np.cos(np.radians(ang))*0.45,y0+np.sin(np.radians(ang))*0.45),xytext=(x0,y0),arrowprops=dict(arrowstyle='->',color='#7A2E1C',lw=2.2),zorder=3)
# crack at edge
cx=[gx+gw*0.72,gx+gw*0.72,gx+gw*0.78,gx+gw*0.74,gx+gw*0.82]; cy=[gy,gy+0.35,gy+0.6,gy+0.85,gy+1.1]
ax.plot(cx,cy,color='#222',lw=2,zorder=4)
ax.annotate('금은 테두리에서\n시작하는 경우가 많습니다',xy=(gx+gw*0.75,gy+0.45),xytext=(FX+FW+0.35,FY+0.55),fontsize=14,color=WARN,fontweight='bold',arrowprops=dict(arrowstyle='->',color=WARN,lw=1.8),va='center')
ax.annotate('테두리\n샷시에 가려 차가움',xy=(FX+0.2,FY+FH*0.72),xytext=(FX+FW+0.35,FY+FH*0.78),fontsize=14,color=MID,fontweight='bold',arrowprops=dict(arrowstyle='->',color=MID,lw=1.8),va='center')
# right explanation
X=7.9
ax.text(X,4.15,'가운데는 늘어나려 하고',fontsize=17,color=NAVY,fontweight='bold')
ax.text(X,3.7,'테두리는 그대로 있습니다',fontsize=17,color=NAVY,fontweight='bold')
ax.text(X,3.0,'이 차이가 커지면',fontsize=15,color='#444')
ax.text(X,2.6,'유리가 버티지 못합니다',fontsize=15,color='#444')
ax.text(X,1.75,'햇빛 열을 많이 머금는 필름은',fontsize=15,color='#444')
ax.text(X,1.35,'가운데를 더 뜨겁게 만들 수 있습니다',fontsize=15,color='#444')
finish(fig,O+'nangman_interior_danyeolfilm_fig1.png','붙여도 되는지는 유리 종류와 필름의 조합으로 정해집니다',brand='낭만 인테리어',allow_outside=True,strict=False)
