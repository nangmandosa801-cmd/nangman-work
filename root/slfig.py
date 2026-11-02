import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_sliding_'
TXT='#444'; GRY='#8A8578'; PANE='#EAF0F7'
render_interior('낭만 인테리어 · 중문',['중문 슬라이딩도어','빼는법'],'위로 들고, 아래를 앞으로','3연동 순서 · 원슬라이딩 커버 · 레일 청소',O+'thumb.png')
def canvas(t1,t2):
    fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=14,color=MID,va='center'); fig.text(0.04,0.9,t2,fontsize=19,color=NAVY,fontweight='bold',va='center')
    return fig,ax
# fig1: 3연동 order
fig,ax=canvas('중문 슬라이딩도어 빼는법 · 3연동 빼는 순서','고정문 → 손잡이문 → 중간문, 문짝마다 빼는 쪽이 다릅니다')
ax.plot([6,78],[56,56],color=GRY,lw=6); ax.plot([6,78],[10,10],color=GRY,lw=3)
ax.text(4,58,'위 레일',fontsize=12,color=GRY); ax.text(4,5,'아래 가이드',fontsize=12,color=GRY)
D=[(8,'고정문','①','거실 쪽',WARN),(32,'중간문','③','거실 쪽',NAVY),(56,'손잡이문','②','현관 쪽',MID)]
for x,n,o,s,c in D:
    ax.add_patch(mp.Rectangle((x,11),21,44,fc=PANE,ec=c,lw=3))
    ax.add_patch(mp.Circle((x+5,54.5),1.2,color=GRY)); ax.add_patch(mp.Circle((x+16,54.5),1.2,color=GRY))
    ax.text(x+10.5,36,o,ha='center',va='center',fontsize=34,fontweight='bold',color=c)
    ax.text(x+10.5,24,n,ha='center',fontsize=15,fontweight='bold',color=NAVY); ax.text(x+10.5,18,s+'에서',ha='center',fontsize=12.5,color=TXT)
ax.annotate('',xy=(18.5,63),xytext=(18.5,57),arrowprops=dict(arrowstyle='->',color=WARN,lw=2.5)); ax.text(20.5,60,'살짝 위로',fontsize=12.5,color=WARN,va='center')
S=[('① 스토퍼 나사를 풀어 옮기고','고정문을 들어 아래를 앞으로'),('② 손잡이문','현관 쪽에서 들어 앞으로'),('③ 중간문','거실 쪽에서 들어 앞으로')]
for i,(a,b) in enumerate(S):
    ax.text(84,48-i*14,a,fontsize=14,fontweight='bold',color=NAVY); ax.text(84,43-i*14,b,fontsize=12.5,color=TXT)
finish(fig,O+'fig1.png','한 사례로 본 순서 · 제품에 따라 다를 수 있습니다 · 안 빠지면 멈춥니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2: symptoms
fig,ax=canvas('중문 슬라이딩도어 고장 · 증상별로 볼 곳','문을 빼기 전에 레일 청소부터')
ax.plot([10,70],[56,56],color=GRY,lw=6); ax.plot([10,70],[12,12],color=GRY,lw=3)
ax.add_patch(mp.Rectangle((22,13),30,42,fc=PANE,ec=NAVY,lw=3))
ax.add_patch(mp.Circle((27,54.5),1.4,color=WARN)); ax.add_patch(mp.Circle((47,54.5),1.4,color=WARN))
ax.add_patch(mp.Rectangle((48,56.5),8,3,fc=MID,ec='none'))
for x in [30,34,40]: ax.plot([x,x+1.5],[12.5,13.5],color=WARN,lw=2)
ax.plot([52,70],[40,40],color=SAND,lw=2,ls='--')
T=[(60,'댐퍼 · 스토퍼','쾅 닫힘 → 위에서 봄, 문 안 빼도 됨',(52,58)),(46,'위 롤러','기울거나 끌림 → 부품 맞춰 교체',(47,54.5)),(32,'3연동 와이어','세 짝이 같이 안 움직임 → 기사',(56,40)),(18,'아래 레일','뻑뻑함 → 먼지·머리카락 청소',(40,13))]
for y,t,s,p in T:
    ax.text(76,y,t,fontsize=16,fontweight='bold',color=NAVY,va='center'); ax.text(76,y-4.5,s,fontsize=12.5,color=TXT,va='center')
    ax.plot([p[0],74],[p[1],y],color=GRY,lw=1.2)
finish(fig,O+'fig2.png','레일이 휘었거나 떨어졌으면 레일 교체라 기사 작업입니다',brand='낭만 인테리어',allow_outside=True,strict=False)
