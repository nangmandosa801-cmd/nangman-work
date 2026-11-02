import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_bangmyochang_'
TXT='#444'; PANE='#EAF0F7'; GRY='#8A8578'
render_interior('낭만 인테리어 · 창문',['방묘창 설치,','틀부터 봅니다'],'망보다 먼저 방충망 틀이 빠지는지','망 · 프레임 · 창틀 고정 · 빈틈',O+'thumb.png')
def canvas(t1,t2):
    fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=14,color=MID,va='center'); fig.text(0.04,0.9,t2,fontsize=19,color=NAVY,fontweight='bold',va='center')
    return fig,ax
# fig1: three parts
fig,ax=canvas('방묘창 설치 · 방묘창은 세 부분이 같이 버텨야 합니다','망이 강해도 프레임이 빠지면 소용없습니다')
# window outer frame
ax.add_patch(mp.Rectangle((6,6),52,54,fc='none',ec=GRY,lw=6))            # 창틀
ax.add_patch(mp.Rectangle((12,11),40,44,fc=PANE,ec=NAVY,lw=4))           # 프레임
for x in range(14,52,3): ax.plot([x,x],[11,55],color='#B9C8D8',lw=0.8)
for y in range(13,55,3): ax.plot([12,52],[y,y],color='#B9C8D8',lw=0.8)  # 망
for (x,y) in [(12,11),(52,11),(12,55),(52,55)]: ax.add_patch(mp.Circle((x,y),1.4,color=WARN))
ax.annotate('',xy=(30,33),xytext=(22,33),arrowprops=dict(arrowstyle='->',color=WARN,lw=3)); ax.text(21,35.5,'고양이가 밉니다',fontsize=12,color=WARN)
L=[(52,'① 망','발톱에 찢어지거나 늘어나지 않는지',(40,40)),(36,'② 프레임','망을 잡은 틀이 휘거나 빠지지 않는지',(52,30)),(20,'③ 창틀 고정','레일·창틀에 단단히 잡혀 있는지 (붉은 점)',(58,12))]
for y,t,s,p in L:
    ax.text(70,y,t,fontsize=19,fontweight='bold',color=NAVY,va='center'); ax.text(70,y-5,s,fontsize=13.5,color=TXT,va='center')
    ax.plot([p[0],68],[p[1],y],color=GRY,lw=1.3)
finish(fig,O+'fig1.png','망 → 프레임 → 창틀 고정, 셋 중 하나만 약해도 빠집니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2: four checkpoints
fig,ax=canvas('방묘창 설치 · 꼭 볼 네 군데','끝까지 · 망 · 이탈 · 창 옆 가구')
ax.add_patch(mp.Rectangle((22,6),42,54,fc='none',ec=GRY,lw=6))
ax.add_patch(mp.Rectangle((25,9),36,48,fc=PANE,ec=NAVY,lw=3))
for x in range(27,61,3): ax.plot([x,x],[9,57],color='#B9C8D8',lw=0.8)
ax.add_patch(mp.Rectangle((58.5,52),2.5,5,fc='white',ec=WARN,lw=2,ls='--'))    # corner gap
ax.plot([25,61],[8.2,8.2],color=WARN,lw=3,ls='--')                               # rail
ax.plot([38,41],[34,30],color=WARN,lw=2.5); ax.plot([39.5,42.5],[34,30],color=WARN,lw=2.5); ax.plot([41,44],[34,30],color=WARN,lw=2.5)  # claw
ax.add_patch(mp.Rectangle((4,6),12,30,fc='#DDD8CE',ec=GRY,lw=2)); ax.add_patch(mp.Rectangle((2,36),16,3,fc='#C9C4BA',ec=GRY)); ax.text(10,20,'캣타워',ha='center',fontsize=13,color=TXT)
ax.annotate('',xy=(24,40),xytext=(14,40),arrowprops=dict(arrowstyle='->',color=WARN,lw=2.5,connectionstyle='arc3,rad=-0.4'))
L=[(55,'① 끝까지','모서리까지 막혔는지',(61,54)),(38,'② 망','긁어도 찢어지지 않는지',(44,32)),(18,'③ 빠지지 않나','밀어도 레일에서 안 빠지는지',(61,8.2))]
for y,t,s2,p in L:
    ax.text(72,y,t,fontsize=18,fontweight='bold',color=NAVY,va='center'); ax.text(72,y-4.5,s2,fontsize=13.5,color=TXT,va='center')
    ax.plot([p[0],70],[p[1],y],color=GRY,lw=1.2)
ax.text(1,56,'④ 창 옆 가구',fontsize=18,fontweight='bold',color=NAVY,va='center'); ax.text(1,51.5,'뛰어오를 발판이 없는지',fontsize=13.5,color=TXT,va='center')
finish(fig,O+'fig2.png','넷 중 하나라도 남으면 그쪽이 탈출로가 됩니다',brand='낭만 인테리어',allow_outside=True,strict=False)
