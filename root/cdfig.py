import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_catdoor_'
TXT='#444'; GRY='#8A8578'; DOOR='#E9E3D8'; PANE='#EAF0F7'
render_interior('낭만 인테리어 · 문',['캣도어 설치,','문 종류부터 봅니다'],'구멍 내기 전에 문짝 속부터','방문 · 베란다문 · 미닫이 · 방화문',O+'thumb.png')
def canvas(t1,t2):
    fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=14,color=MID,va='center'); fig.text(0.04,0.9,t2,fontsize=19,color=NAVY,fontweight='bold',va='center')
    return fig,ax
def door(ax,x,w=20,h=44,fc=DOOR,ec=GRY):
    ax.add_patch(mp.Rectangle((x,10),w,h,fc=fc,ec=ec,lw=2.5)); ax.add_patch(mp.Circle((x+w-3,32),0.9,color=GRY))
# fig1
fig,ax=canvas('캣도어 설치 · 방식 세 가지','지금 문을 자를지, 문짝을 바꿀지, 방묘문에 달지')
door(ax,8); ax.add_patch(mp.Rectangle((13,10),9,10,fc='white',ec=WARN,lw=2.5,ls='--'))
ax.text(18,58,'① 문에 구멍 내기',ha='center',fontsize=16,fontweight='bold',color=NAVY); ax.text(18,5,'되돌릴 수 없음',ha='center',fontsize=13,color=WARN,fontweight='bold')
door(ax,46,fc='#DDE6F0',ec=NAVY); ax.add_patch(mp.Rectangle((51,10),9,10,fc='white',ec=NAVY,lw=2.5))
ax.text(56,58,'② 펫도어 문짝 교체',ha='center',fontsize=16,fontweight='bold',color=NAVY); ax.text(56,5,'기존 문 보관 → 되돌릴 수 있음',ha='center',fontsize=13,color=NAVY)
ax.add_patch(mp.Rectangle((82,10),24,34,fc='white',ec=NAVY,lw=2.5))
for x in range(85,106,3): ax.plot([x,x],[10,44],color='#9DB3CC',lw=1.5)
ax.add_patch(mp.Rectangle((89,10),8,9,fc=PANE,ec=NAVY,lw=2))
ax.text(94,58,'③ 방묘문·패널 일체형',ha='center',fontsize=16,fontweight='bold',color=NAVY); ax.text(94,5,'지금 문은 그대로',ha='center',fontsize=13,color=NAVY)
finish(fig,O+'fig1.png','원상복구가 중요하면 ②나 ③부터 봅니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2
fig,ax=canvas('캣도어 설치 · 문 종류별로 먼저 볼 것','그 문을 잘라도 되는지가 크기보다 먼저입니다')
items=[('방문','속이 빈 문?\n단면 마감 틀',NAVY),('화장실문','습기에 맞는\n재질?',NAVY),('베란다문','유리·복층유리?\n→ 자르지 않음',SAND),('미닫이문','겹칠 때\n틀이 걸리나',SAND),('현관 방화문','임의로 구멍\n내지 않음',WARN)]
for i,(n,s,c) in enumerate(items):
    x=3+i*22
    ax.add_patch(mp.Rectangle((x+3,22),14,30,fc=DOOR if i<4 else '#D9D4CB',ec=c,lw=3))
    if i==2: ax.add_patch(mp.Rectangle((x+5,34),10,15,fc=PANE,ec=GRY,lw=1.5))
    if i==3: ax.add_patch(mp.Rectangle((x+7,22),14,30,fc='none',ec=GRY,lw=1.5,ls=':'))
    if i==4: ax.plot([x+6,x+14],[26,34],color=WARN,lw=4); ax.plot([x+14,x+6],[26,34],color=WARN,lw=4)
    ax.text(x+10,57,n,ha='center',fontsize=15,fontweight='bold',color=c)
    ax.text(x+10,12,s,ha='center',va='center',fontsize=12.5,color=TXT,linespacing=1.5)
finish(fig,O+'fig2.png','공동주택 현관 방화문은 인정받은 상태를 유지해야 합니다 · 현관은 중문이나 방묘문으로',brand='낭만 인테리어',allow_outside=True,strict=False)
