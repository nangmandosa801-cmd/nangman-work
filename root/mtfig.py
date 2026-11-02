import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
D='/mnt/user-data/outputs/int/mutagong/'; import os; os.makedirs(D,exist_ok=True)
render_interior('낭만 인테리어 · 중문 고르기',['무타공 중문,','구멍 대신 눌러서 버팁니다'],'전세집은 수평부터 잽니다','종류 · 실측 5곳 · 셀프 설치 · 전세 중문',D+'nangman_interior_mutagong_thumb.png')
WALL='#EFEBE4'; FR='#2E2E2E'; GL='#DCE8F2'
def arr(ax,a,b,c,lw=2.4): ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=24,color=c,lw=lw))
# fig1
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.02,0.1,0.96,0.75]); ax.set_xlim(0,100); ax.set_ylim(0,72); ax.axis('off')
fig.text(0.04,0.955,'무타공 중문 구조 · 현관 안쪽에서 본 모습',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'기둥이 천장과 바닥을 눌러 문틀을 잡습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x0,y0,W,H=8,6,52,54
ax.add_patch(Rectangle((x0-6,y0+H),W+12,3,color='#D6D0C6')); ax.add_patch(Rectangle((x0-6,y0-3),W+12,3,color='#D6D0C6'))
ax.text(x0+W/2,y0+H+4.3,'천장',ha='center',fontsize=15,color='#6B6457',fontweight='bold'); ax.text(x0+W/2,y0-6.8,'바닥',ha='center',fontsize=15,color='#6B6457',fontweight='bold')
for xc in (x0,x0+W-3):
    ax.add_patch(Rectangle((xc,y0),3,H,color=NAVY))
ax.add_patch(Rectangle((x0+3,y0+H-3),W-6,3,color=NAVY))
ax.add_patch(Rectangle((x0+4,y0+0.5),(W-8)/2-0.5,H-4.5,fc=GL,ec=MID,lw=2))
ax.add_patch(Rectangle((x0+4+(W-8)/2+0.5,y0+0.5),(W-8)/2-0.5,H-4.5,fc=GL,ec=MID,lw=2))
for xc in (x0+1.5,x0+W-1.5):
    arr(ax,(xc,y0+H-8),(xc,y0+H-0.3),WARN); arr(ax,(xc,y0+8),(xc,y0+0.3),WARN)
lx=x0+W+10
def lab(yl,t,d,c,px,py):
    ax.plot([px,lx-1],[py,yl],color=c,lw=1.2)
    ax.text(lx,yl+1.3,t,fontsize=17,color=c,fontweight='bold',va='center'); ax.text(lx,yl-2.6,d,fontsize=13.5,color='#555',va='center')
lab(56,'누르는 힘','천장·바닥이 평평해야 고르게 눌림',WARN,x0+W-0.2,y0+H-3)
lab(40,'늘어나는 기둥','천장과 바닥 사이를 꽉 누름',NAVY,x0+W,y0+H/2+6)
lab(24,'문틀 · 문','기둥에 걸어 답니다',MID,x0+W-6,y0+H/2-6)
lab(9,'벽','나사 구멍을 내지 않습니다',SAND,x0+W+1,y0+4)
finish(fig,D+'nangman_interior_mutagong_fig1.png','제품마다 고정 방식이 조금씩 다릅니다 · 천장이 약하면 누른 자국이 날 수 있습니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2 실측 5곳
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.02,0.1,0.96,0.75]); ax.set_xlim(0,100); ax.set_ylim(0,72); ax.axis('off')
fig.text(0.04,0.955,'무타공 중문 설치 전 실측',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'폭은 세 군데, 높이는 두 군데를 잽니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x0,y0,W,H=8,6,46,56
ax.add_patch(Rectangle((x0-4,y0),W+8,H+3,color=WALL)); ax.add_patch(Rectangle((x0,y0),W,H,fc='white',ec='#999',lw=1.5))
def dim(a,b,c,lab,pos,ha='center'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='<->',mutation_scale=18,color=c,lw=2))
    ax.text(pos[0],pos[1],lab,fontsize=14.5,color=c,fontweight='bold',ha=ha,va='center')
for yy,t in ((y0+H-6,'① 위'),(y0+H/2,'② 가운데'),(y0+7,'③ 아래')):
    dim((x0+1,yy),(x0+W-1,yy),WARN,t,(x0+W/2,yy+2.6))
dim((x0+5,y0+1),(x0+5,y0+H-1),MID,'④',(x0+8,y0+H/2-8),'left'); dim((x0+W-5,y0+1),(x0+W-5,y0+H-1),MID,'⑤',(x0+W-8,y0+H/2-8),'right')
tx=64
for i,(t,d) in enumerate([('① ② ③ 폭 세 군데','벽이 기울면 값이 다르게 나옵니다'),('④ ⑤ 높이 두 군데','천장이 기울면 기둥이 한쪽만 눌립니다'),('바닥 단차','현관 턱이 있으면 문 아래 틈이 뜹니다'),('몰딩 · 걸레받이','튀어나온 만큼 기둥이 벽에 안 붙습니다'),('문 열리는 방향','신발장 문·현관문이 부딪히는지 봅니다')]):
    y=60-i*11.5
    ax.text(tx,y,t,fontsize=17,color=NAVY,fontweight='bold',va='center'); ax.text(tx,y-4,d,fontsize=13.5,color='#555',va='center')
finish(fig,D+'nangman_interior_mutagong_fig2.png','세 군데 폭이 몇 mm씩 다르면 무거운 3연동보다 가벼운 문이 낫습니다',brand='낭만 인테리어',allow_outside=True,strict=False)
