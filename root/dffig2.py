import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN
from note import finish
O='/mnt/user-data/outputs/int/'
GRAY='#8A8578'; GLASS='#C7D6E6'; FILM='#2E5C8A'; TXT='#444'
def arrow(ax,a,b,c,lw=3,ls='-'):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=c,lw=lw,ls=ls,mutation_scale=22))
def canvas(h=5.4):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.1,1,0.9]); ax.set_xlim(0,11.2); ax.set_ylim(0,h*0.9); ax.axis('off'); return fig,ax

# fig2 두 갈래 열 손실 — 창 단면
fig,ax=canvas(5.6)
ax.text(1.3,4.55,'방 안',fontsize=17,fontweight='bold',color=WARN,ha='center')
ax.text(9.9,4.55,'바깥',fontsize=17,fontweight='bold',color=MID,ha='center')
X=5.6
ax.add_patch(mp.Rectangle((X-0.5,3.55),1.0,0.6,color=GRAY))          # 위 샷시
ax.add_patch(mp.Rectangle((X-0.5,0.55),1.0,0.6,color=GRAY))          # 아래 샷시
ax.add_patch(mp.Rectangle((X-0.12,1.15),0.24,2.4,color=GLASS))       # 유리
ax.add_patch(mp.Rectangle((X-0.2,1.15),0.08,2.4,color=FILM))          # 필름(안쪽)
ax.annotate('필름',xy=(X-0.17,3.0),xytext=(X-1.4,3.05),fontsize=14,color=FILM,fontweight='bold',va='center',arrowprops=dict(arrowstyle='->',color=FILM,lw=1.6))
# 틈바람
ax.plot([X-0.5,X+0.5],[3.55,3.55],color='white',lw=2.5)
arrow(ax,(2.2,3.6),(8.8,3.6),SAND,lw=3,ls='--')
ax.text(8.95,3.6,'① 틈으로 새는 공기',fontsize=15,color=TXT,va='center',fontweight='bold')
ax.text(8.95,3.2,'필름과 상관없음 → 샷시',fontsize=13.5,color=TXT,va='center')
# 유리 통과 열
arrow(ax,(2.2,2.35),(X-0.25,2.35),WARN,lw=4)
arrow(ax,(X-0.25,2.35),(3.2,1.75),WARN,lw=3)
arrow(ax,(X+0.15,2.35),(8.8,2.35),WARN,lw=1.6)
ax.text(8.95,2.35,'② 유리로 빠지는 열',fontsize=15,color=TXT,va='center',fontweight='bold')
ax.text(8.95,1.95,'필름이 줄이는 쪽',fontsize=13.5,color=FILM,va='center',fontweight='bold')
ax.text(2.2,1.45,'일부를 방 안으로 되돌림',fontsize=13.5,color=WARN,fontweight='bold')
finish(fig,O+'nangman_interior_danyeolfilm_fig2.png','단열필름은 ②를 줄입니다 · ①은 샷시 모헤어와 창짝을 봐야 합니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig3 성능표 세 숫자
fig,ax=canvas(5.2)
cards=[('열관류율 (U값)','방 안의 열이\n얼마나 빠져나가나','낮을수록','겨울에 따뜻','겨울',WARN),
       ('태양열 취득률 (SHGC)','햇빛 열이\n얼마나 들어오나','낮을수록','여름에 덜 더움','여름',MID),
       ('가시광선 투과율','빛이\n얼마나 들어오나','높을수록','방이 밝음','밝기',NAVY)]
for i,(n,d,dirn,res,tag,c) in enumerate(cards):
    x=0.45+i*3.65; w=3.3
    ax.add_patch(mp.FancyBboxPatch((x,0.45),w,3.85,boxstyle='round,pad=0.02,rounding_size=0.12',fc='#F7F5F0',ec=c,lw=2))
    ax.add_patch(mp.FancyBboxPatch((x,3.55),w,0.75,boxstyle='round,pad=0.02,rounding_size=0.12',fc=c,ec=c))
    ax.text(x+w/2,3.92,tag,ha='center',va='center',fontsize=18,color='white',fontweight='bold')
    ax.text(x+w/2,3.05,n,ha='center',va='center',fontsize=15,color=c,fontweight='bold')
    ax.text(x+w/2,2.25,d,ha='center',va='center',fontsize=14,color=TXT,linespacing=1.5)
    ax.text(x+w/2,1.35,dirn,ha='center',va='center',fontsize=14,color=TXT)
    ax.text(x+w/2,0.88,res,ha='center',va='center',fontsize=17,color=c,fontweight='bold')
finish(fig,O+'nangman_interior_danyeolfilm_fig3.png','이름보다 성능표 · 우리 집 고민에 맞는 숫자를 봅니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig4 고르는 순서
fig,ax=canvas(6.4)
def box(x,y,w,h,t,fc,tc='white',fs=15):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.1',fc=fc,ec=fc))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=tc,fontweight='bold',linespacing=1.4)
box(0.4,4.3,3.2,0.95,'창을 닫아도\n바람이 드나요?',NAVY)
box(4.6,4.3,3.4,0.95,'예 → 샷시부터\n모헤어 · 창짝 · 잠금',SAND,fs=14)
arrow(ax,(3.65,4.78),(4.55,4.78),SAND)
arrow(ax,(2.0,4.25),(2.0,3.55),NAVY); ax.text(2.15,3.85,'아니오',fontsize=13,color=NAVY,fontweight='bold')
box(0.4,2.55,3.2,0.95,'가장 큰 고민은?',NAVY)
opts=[('겨울 창가 냉기','열관류율 낮은 것',WARN),('여름 거실 더위','태양열 취득률 낮은 것',MID),('어두워질까 걱정','가시광선 투과율 높은 것',NAVY)]
for i,(a,b,c) in enumerate(opts):
    y=3.3-i*1.0
    arrow(ax,(3.65,3.02),(4.55,y+0.3),c,lw=2)
    box(4.6,y,2.7,0.62,a,'#F7F5F0',c,14)
    ax.add_patch(mp.FancyBboxPatch((4.6,y),2.7,0.62,boxstyle='round,pad=0.02,rounding_size=0.1',fc='none',ec=c,lw=1.8))
    arrow(ax,(7.35,y+0.31),(7.8,y+0.31),c,lw=2)
    ax.text(7.9,y+0.31,b,fontsize=14,color=c,va='center',fontweight='bold')
arrow(ax,(2.0,2.5),(2.0,1.2),NAVY)
box(0.4,0.3,10.4,0.85,'마지막: 우리 집 유리(한 장 · 복층 · 로이 · 색유리)에 붙여도 되는 조합인지 확인',WARN,fs=15)
finish(fig,O+'nangman_interior_danyeolfilm_fig4.png','바람 → 고민 → 숫자 → 유리 순서로 보면 됩니다',brand='낭만 인테리어',allow_outside=True,strict=False)
