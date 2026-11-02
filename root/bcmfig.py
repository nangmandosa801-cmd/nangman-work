import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_bangchungmang_cat_'
TXT='#444'; GRY='#8A8578'; PANE='#EAF0F7'
render_interior('낭만 인테리어 · 창문',['방충망 고양이 교체,','같은 망이면 또 뜯습니다'],'망 재질 · 프레임 · 이탈방지 고정','반려동물용 망 · 틀 고정까지 같이',O+'thumb.png')
def canvas(t1,t2,h=6.6):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.08,1,0.8]); ax.set_xlim(0,112); ax.set_ylim(0,66); ax.axis('off')
    fig.text(0.04,0.955,t1,fontsize=14,color=MID,va='center'); fig.text(0.04,0.9,t2,fontsize=19,color=NAVY,fontweight='bold',va='center')
    return fig,ax
# fig1: five mesh swatches
fig,ax=canvas('방충망 고양이 교체 · 방충망 종류 다섯 가지','고양이가 자주 긁는 집은 반려동물용 망부터 비교합니다')
M=[('유리섬유망','가볍고 값이 낮음','긁힘에 손상될 수 있음',0.5,'#C9D3DE',False),
   ('알루미늄망','모양 유지가 좋음','오래되면 약해질 수 있음',0.7,'#AEB8C2',False),
   ('반려동물용\n폴리에스터망','굵고 비닐 코팅','찢김·펑크에 강하게 만든 제품',1.8,'#6B7B8C',True),
   ('스테인리스망','금속, 내구성 높은 편','굵기·메시 확인',1.2,'#8C9AA8',True),
   ('블랙 스텐망','검은 마감 스테인리스','업체마다 사양 차이 큼',1.3,'#3A3F46',True)]
for i,(n,a,b,lw,c,good) in enumerate(M):
    x=2+i*22
    ax.add_patch(mp.Rectangle((x,26),18,26,fc='white',ec=NAVY if good else GRY,lw=3 if good else 1.5))
    for k in range(1,9):
        ax.plot([x+k*2,x+k*2],[26,52],color=c,lw=lw); ax.plot([x,x+18],[26+k*2.9,26+k*2.9],color=c,lw=lw)
    ax.text(x+9,58,n,ha='center',va='center',fontsize=14,fontweight='bold',color=NAVY)
    ax.text(x+9,20,a,ha='center',fontsize=12,color=TXT); ax.text(x+9,14,b,ha='center',fontsize=12,color=WARN if good else GRY,fontweight='bold' if good else 'normal')
ax.text(56,4,'파란 테두리: 고양이 집에서 비교해 볼 만한 망',ha='center',fontsize=13,color=NAVY)
finish(fig,O+'fig1.png','같은 이름이어도 굵기·메시·코팅이 다릅니다 · 실제 사양을 확인하십시오',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2: three checks
fig,ax=canvas('방충망 고양이 교체 · 견적 받을 때 세 가지','강한 망도 틀째 빠지면 소용없습니다',h=5.8)
B=[('① 망 재질','반려동물용\n찢김·펑크에 강한 망'),('② 프레임 상태','휘거나 헐겁지\n않은지'),('③ 이탈방지 고정','밀어도 레일에서\n빠지지 않게')]
for i,(t,s) in enumerate(B):
    x=6+i*35
    ax.add_patch(mp.FancyBboxPatch((x,14),28,36,boxstyle='round,pad=0.3,rounding_size=2',fc='#F2F4F7',ec=NAVY if i<2 else WARN,lw=2.5))
    ax.text(x+14,42,t,ha='center',va='center',fontsize=18,fontweight='bold',color=NAVY if i<2 else WARN)
    ax.text(x+14,26,s,ha='center',va='center',fontsize=14,color=TXT,linespacing=1.6)
    if i<2: ax.text(x+31.5,32,'+',ha='center',va='center',fontsize=30,color=GRY)
ax.text(56,5,'망만 바꾸면 수리 · 망과 틀 고정을 같이 해야 방묘',ha='center',fontsize=15,color=NAVY,fontweight='bold')
finish(fig,O+'fig2.png','사고가 나는 길은 두 가지 · 망이 손상되는 것, 틀이 빠지는 것',brand='낭만 인테리어',allow_outside=True,strict=False)
