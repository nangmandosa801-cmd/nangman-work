import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, FancyBboxPatch
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
D='/mnt/user-data/outputs/int/3yeondong/'; import os; os.makedirs(D,exist_ok=True)
render_interior('낭만 인테리어 · 중문 수리',['3연동 중문 수리,','한 짝만 열리면 와이어'],'와이어 · 벨트 · 연동 부품부터 봅니다','증상별 고장 부위 · 수리 비용 · 셀프 전 확인',D+'nangman_interior_3yeondong_thumb.png')
WALL='#EFEBE4'; FR='#2E2E2E'; GL='#DCE8F2'
# fig1 구조
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.02,0.1,0.96,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,70); ax.axis('off')
fig.text(0.04,0.955,'3연동 중문 구조 · 현관 안쪽에서 본 모습',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'세 장을 이어 주는 부품이 끊어지면 한 짝만 움직입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
x0,y0,W,H=6,11,60,44
ax.add_patch(Rectangle((x0-4,y0),W+8,H+6,color=WALL))
ax.add_patch(Rectangle((x0,y0+H),W,2.6,color=NAVY))
w=W/3
for i in range(3):
    xx=x0+i*w+0.4
    ax.add_patch(Rectangle((xx,y0+1.2),w-0.8,H-1.4,fc=GL,ec=MID,lw=2.2))
    ax.text(xx+(w-0.8)/2,y0+H/2+4,f'문 {i+1}',ha='center',fontsize=18,color=NAVY,fontweight='bold')
    for dx in (3,w-3.8):
        ax.add_patch(Circle((xx+dx,y0+H-1.2),1.1,color=WARN,zorder=5))
ax.add_patch(Rectangle((x0,y0),W,1.2,color='#C7D3E0'))
ax.plot([x0+w/2,x0+W-w/2],[y0+H+5.5,y0+H+5.5],color=WARN,lw=2.4,ls='--')
for i in range(3): ax.plot([x0+w/2+i*w]*2,[y0+H+2.6,y0+H+5.5],color=WARN,lw=1.2,ls=':'); ax.add_patch(Circle((x0+w/2+i*w,y0+H+5.5),0.7,color=WARN))
ax.add_patch(FancyArrowPatch((x0+W-4,y0-6),(x0+4,y0-6),arrowstyle='-|>',mutation_scale=22,color='#8A8578',lw=2.2))
ax.text(x0+W/2,y0-9.8,'문 하나를 밀면 나머지 두 장이 따라옵니다',ha='center',fontsize=15,color='#6B6457',fontweight='bold')
lx=x0+W+9
def lab(yl,t,d,c,px,py):
    ax.plot([px,lx-1],[py,yl],color=c,lw=1.2)
    ax.text(lx,yl+1.2,t,fontsize=17,color=c,fontweight='bold',va='center')
    ax.text(lx,yl-2.6,d,fontsize=13.5,color='#555',va='center')
lab(62,'연동 부품','와이어 · 벨트',WARN,x0+W-w/2,y0+H+5.5)
lab(51,'상부 레일','문이 움직이는 길',NAVY,x0+W,y0+H+1.3)
lab(40,'호차 · 롤러','문이 굴러가는 바퀴',WARN,x0+W-3,y0+H-1.2)
lab(y0+4,'하부 가이드','앞뒤 흔들림을 잡음',MID,x0+W,y0+0.6)
finish(fig,D+'nangman_interior_3yeondong_fig1.png','제품마다 연동 방식과 부품 위치가 다릅니다 · 뜯기 전에 사진부터 찍어 두세요',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2 증상 → 먼저 볼 곳
fig=plt.figure(figsize=(11.2,9.6)); ax=fig.add_axes([0.02,0.08,0.96,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
fig.text(0.04,0.955,'3연동 중문 수리 · 증상별로 먼저 볼 곳',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'문이 움직이는 모습만 봐도 어디부터 볼지 나옵니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
R=[('한 짝만 열리고 나머지가 안 따라온다','와이어 · 벨트 · 연동 부품',WARN),
   ('문 세 장이 제각각 움직인다','연동 부품 빠짐 · 깨짐',WARN),
   ('한쪽 문이 내려앉았다','호차 · 높이 조절 부품',MID),
   ('문이 레일에서 빠진다','호차 · 레일 · 하부 가이드',MID),
   ('드르륵 소리가 나고 무겁다','호차 마모 · 레일 모래',MID),
   ('아래쪽이 앞뒤로 흔들린다','하부 가이드',MID),
   ('끝에서 쾅 닫힌다','댐퍼 · 스토퍼',NAVY)]
for i,(a,b,c) in enumerate(R):
    y=73-i*10.6
    ax.add_patch(FancyBboxPatch((2,y-3.6),48,7.2,boxstyle='round,pad=0.2,rounding_size=1.2',fc='#F2F4F7',ec='none'))
    ax.text(4,y,a,fontsize=16.5,color='#333',va='center')
    ax.add_patch(FancyArrowPatch((51.5,y),(58.5,y),arrowstyle='-|>',mutation_scale=20,color=c,lw=2))
    ax.add_patch(FancyBboxPatch((60,y-3.6),38,7.2,boxstyle='round,pad=0.2,rounding_size=1.2',fc=c,ec='none'))
    ax.text(79,y,b,fontsize=16.5,color='white',va='center',ha='center',fontweight='bold')
finish(fig,D+'nangman_interior_3yeondong_fig2.png','부품만 바꿔 고치는 경우가 많습니다 · 끊어진 채로 억지로 밀지 마세요',brand='낭만 인테리어',allow_outside=True,strict=False)
