import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_gyeolro_'
TXT='#444'; GRY='#8A8578'; OK='#3C7A5A'
render_interior('낭만 인테리어 · 창문',['창문 결로 해결,','맺히는 곳부터'],'뽁뽁이·제습기보다 먼저 볼 것','유리 · 창틀 · 유리 사이 · 비 온 뒤',O+'thumb.png')
def canvas(t1,t2,h=6.6):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=17,color=MID,va='center'); fig.text(0.04,0.905,t2,fontsize=23,color=NAVY,fontweight='bold',va='center')
    return fig,ax
# fig1 window diagram + 4 callouts
fig,ax=canvas('창문 결로 · 맺히는 곳 네 군데','물이 생긴 위치가 먼저 볼 곳을 알려 줍니다',h=8.6)
ax.add_patch(mp.Rectangle((6,6),40,54,fc='#DDE3EA',ec=NAVY,lw=3))      # frame
ax.add_patch(mp.Rectangle((10,10),32,46,fc='#EEF4FA',ec=MID,lw=1.5))   # glass
ax.add_patch(mp.Rectangle((12,12),28,42,fc='none',ec=MID,lw=1,ls='--'))# inner pane
import numpy as np
rng=np.random.default_rng(3)
for _ in range(45): ax.add_patch(mp.Circle((rng.uniform(14,38),rng.uniform(22,52)),0.55,fc='#9DBBD8',ec='none'))
for x in (8,44): 
    for y in (8,58): ax.add_patch(mp.Circle((x,y),1.3,fc=WARN,ec='none'))
ax.add_patch(mp.Rectangle((8,6.5),36,2.2,fc=WARN,ec='none',alpha=.55))
ax.add_patch(mp.Ellipse((26,17),16,6,fc='#C9CED4',ec='none',alpha=.8))
ax.annotate('',xy=(44,36),xytext=(47,48),arrowprops=dict(arrowstyle='-|>',color=GRY,lw=2))

R=[('①','유리 안쪽 전체','실내 습도부터','습도계 · 환기 · 제습','#9DBBD8'),
   ('②','창틀 모서리 · 아래쪽','창틀이 특히 차가운지','창틀 상태 · 단열',WARN),
   ('③','복층유리 두 장 사이','유리 밀봉 이상','유리 업체 점검','#8A9199'),
   ('④','비 온 뒤에만','누수 가능성','실리콘 · 배수 · 외벽',GRY)]
for i,(n,a,b,c,col) in enumerate(R):
    y=55-i*15.6
    ax.add_patch(mp.FancyBboxPatch((52,y-6.3),58,13,boxstyle='round,pad=0.2,rounding_size=1.5',fc='#F4F6F9',ec=LINE,lw=1.2))
    ax.add_patch(mp.Rectangle((52,y-6.5),1.6,13.4,fc=col,ec='none'))
    ax.text(56,y+3.2,n+' '+a,fontsize=21,fontweight='bold',color=NAVY,va='center')
    ax.text(56,y-2.9,b+'  →  '+c,fontsize=17,color=TXT,va='center')
for (t,x,y) in [('①',2.5,40),('②',2.5,7),('③',2.5,17),('④',49.5,40)]: ax.text(x,y,t,fontsize=21,color=NAVY,fontweight='bold',va='center',ha='center')
finish(fig,O+'fig1.png','위치 하나로 원인을 확정하지 않습니다 · 결로와 누수가 같이 있는 집도 있습니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2 steps
fig,ax=canvas('창문 결로 해결 · 손보는 순서','돈 안 드는 것부터, 그래도 젖으면 창을 봅니다',h=8.6)
S=[('1','습도 · 환기','60% 넘지 않게\n결로 집 40~50%\n요리·샤워 후\n환풍기','돈 거의 안 듦',OK),
   ('2','뽁뽁이 · 필름','유리 표면을\n덜 차갑게\n창틀에는\n효과 제한','몇 만원',MID),
   ('3','샷시 점검·교체','계속 젖는 창틀\n복층·로이 유리\n창틀 단열 성능','공사',NAVY)]
for i,(n,t,d,c,col) in enumerate(S):
    x=4+i*37
    ax.add_patch(mp.FancyBboxPatch((x,4),31,56,boxstyle='round,pad=0.3,rounding_size=2',fc='#F4F6F9',ec=col,lw=3))
    ax.add_patch(mp.Circle((x+15.5,53),3.6,fc=col,ec='none')); ax.text(x+15.5,53,n,ha='center',va='center',fontsize=22,color='white',fontweight='bold')
    ax.text(x+15.5,44,t,ha='center',fontsize=24,fontweight='bold',color=col)
    ax.text(x+15.5,28,d,ha='center',va='center',fontsize=19,color=TXT,linespacing=1.7)
    ax.text(x+15.5,9,c,ha='center',fontsize=21,fontweight='bold',color=col)
    if i<2: ax.annotate('',xy=(x+36.5,32),xytext=(x+32,32),arrowprops=dict(arrowstyle='-|>',color=GRY,lw=2.2))
finish(fig,O+'fig2.png','복층유리 사이 습기는 1·2단계로 안 없어집니다',brand='낭만 인테리어',allow_outside=True,strict=False)
