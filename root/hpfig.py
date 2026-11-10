import sys; sys.path.insert(0,'/home/claude/blogkit')
from PIL import Image, ImageDraw
from thumbnail import render_interior, F, _mark_door
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
import os
O='/mnt/user-data/outputs/int/hopyeong/'; os.makedirs(O,exist_ok=True)
U='/root/.claude/uploads/0c32fbc6-c708-59b2-959b-9e774c0e2364/'
render_interior('낭만 인테리어 · 시공 사례',['양개도어 중문,','호평동 임광그대가 시공'],'어반블루 틀에 브론즈 유리','남양주 호평동 임광그대가 · 비대칭 양개도어',O+'nangman_interior_hopyeong_thumb.png')
def frame(src,cap,out):
    im=Image.open(src).convert('RGB'); W=780; m=18
    pw=W-2*m; ph=int(im.height*pw/im.width); im=im.resize((pw,ph),Image.LANCZOS)
    H=m+ph+140
    c=Image.new('RGB',(W,H),'white'); c.paste(im,(m,m)); d=ImageDraw.Draw(c)
    y=m+ph+18; d.text((m,y),cap,font=F(19,False,False),fill='#555555')
    y2=y+42; d.line([(m,y2),(W-m,y2)],fill='#DDD8CE',width=2)
    _mark_door(d,m,y2+18,26,36,frame='#FFFFFF')
    d.text((m+48,y2+18),'낭만 인테리어',font=F(26,False,True),fill='#1F3864')
    t='010-7678-9967'; f=F(24,False,True); tw=d.textlength(t,font=f)
    d.text((W-m-tw,y2+20),t,font=f,fill='#8A8578')
    c.save(out,quality=92)
P=[('4b7c7be5-image.jpg','복도 쪽에서 본 닫힌 모습 — 큰 문과 작은 문, 어반블루 틀과 브론즈 유리','01_closed'),
   ('b7dad76d-image.jpg','현관 쪽에서 본 모습 — 브론즈 유리 너머로 거실이 보입니다','02_entrance'),
   ('7d623f1e-image.jpg','큰 문을 연 모습 — 금색 긴 손잡이와 아래쪽 하부고시 판','03_open'),
   ('fd20b6f1-image.jpg','복도 끝에서 본 모습 — 갈색 몰딩 사이의 어반블루 틀','04_hall'),
   ('f71b00b1-image.jpg','큰 문을 연 뒤 통로 — 작은 문은 닫아 둔 채로 씁니다','05_open_wide')]
for s,c,n in P: frame(U+s,c,O+f'nangman_interior_hopyeong_{n}.jpg')
# fig1: 위에서 본 모습 비교
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
fig.text(0.04,0.955,'양개도어 vs 슬라이딩 · 위에서 본 모습',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'슬라이딩은 옆 벽, 양개도어는 문이 돌 공간이 필요합니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
BL='#3E5470'
def wall(x0,x1,y): ax.add_patch(Rectangle((x0,y-1.2),x1-x0,2.4,color='#8A8578'))
# 슬라이딩
y=26; wall(2,10,y); wall(38,48,y)
ax.add_patch(Rectangle((38,y+1.6),10,1.3,color=BL)); ax.text(43,y+5,'문이 선 자리',ha='center',fontsize=14,color=WARN,fontweight='bold')
ax.add_patch(FancyArrowPatch((22,y+2.3),(36,y+2.3),arrowstyle='-|>',mutation_scale=20,color=BL,lw=2))
ax.text(24,y-6,'입구',ha='center',fontsize=15,color=SAND,fontweight='bold')
ax.add_patch(FancyArrowPatch((38,y-3.5),(48,y-3.5),arrowstyle='<->',mutation_scale=16,color=WARN,lw=1.8)); ax.text(43,y-7.5,'옆 벽 필요',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.text(24,y+22,'슬라이딩',ha='center',fontsize=20,color=NAVY,fontweight='bold')
# 양개
y=26; wall(54,60,y); wall(90,98,y)
hx=60; big=19; sm=11
ax.plot([hx,hx+0.1],[y,y+big],color=BL,lw=5)
ax.add_patch(Arc((hx,y),2*big,2*big,theta1=0,theta2=90,color=WARN,lw=2,ls='--'))
ax.plot([hx+big,90],[y,y],color=BL,lw=5)
ax.text(hx+big/2+1,y+big*0.45,'문이\n도는 공간',ha='center',fontsize=14,color=WARN,fontweight='bold')
ax.text(hx+2,y+big+1.5,'큰 문',fontsize=14,color=NAVY,fontweight='bold')
ax.text(84.5,y-5,'작은 문 (닫아 둠)',ha='center',fontsize=14,color=NAVY,fontweight='bold')
ax.text(76,y+26,'비대칭 양개도어',ha='center',fontsize=20,color=NAVY,fontweight='bold')
ax.text(76,y-11,'옆 벽 없어도 됨',ha='center',fontsize=15,color=MID,fontweight='bold')
ax.text(50,4,'복도 쪽 ↑  ·  현관 쪽 ↓',ha='center',fontsize=14,color=SAND)
finish(fig,O+'nangman_interior_hopyeong_fig1.png','양개도어는 문이 도는 길에 신발장 문 · 욕실 문 · 스위치가 걸리지 않는지 먼저 봅니다',brand='낭만 인테리어',allow_outside=True,strict=False)
