import sys; sys.path.insert(0,'/home/claude/blogkit')
from thumbnail import render_interior
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE, PALE
from note import finish
O='/mnt/user-data/outputs/int/'
render_interior('낭만 인테리어 · 겨울 준비',['샷시 모헤어 교체,','틈새막이보다 먼저'],'털이 누웠으면 교체, 가운데 틈은 풍지판','휴지 테스트 · 셀프 교체 · 비용 · 롤러 조절',O+'nangman_interior_mohair_thumb.png')

# fig1 창 정면: 휴지가 흔들리는 곳 → 먼저 확인할 것
fig=plt.figure(figsize=(11.2,9.6)); ax=fig.add_axes([0.02,0.08,0.96,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
fig.text(0.04,0.955,'창문 외풍 차단 · 휴지 테스트',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'어디서 새느냐에 따라 먼저 볼 곳이 다릅니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.add_patch(Rectangle((26,10),48,60,fc='#EEEAE2',ec='#8A8578',lw=5))            # 창틀(벽 쪽)
ax.add_patch(Rectangle((29,13),22,54,fc='#D8E6F2',ec='#6E7C8C',lw=4))            # 왼쪽 창짝
ax.add_patch(Rectangle((49,13),22,54,fc='#D8E6F2',ec='#6E7C8C',lw=4))            # 오른쪽 창짝
for x in (29.6,50.4,70.4,48.4): ax.add_patch(Rectangle((x,14),0.9,52,color=SAND))  # 모헤어 띠
ax.add_patch(Rectangle((48.3,39),3.4,4,color=NAVY))                                 # 크리센트
def tag(p,s,t1,t2,c):
    ax.add_patch(FancyArrowPatch(s,p,arrowstyle='-|>',mutation_scale=16,color=c,lw=2))
    tx,ty=s; ha='right' if tx<p[0] else 'left'; tx=tx-1 if ha=='right' else tx+1
    ax.text(tx,ty+1.8,t1,fontsize=16,color=c,fontweight='bold',ha=ha,va='center')
    ax.text(tx,ty-2.2,t2,fontsize=13.5,color='#555555',ha=ha,va='center')
tag((29.5,50),(18,58),'창짝 세로 테두리','모헤어가 닳았는지',NAVY)
tag((50,66),(80,74),'가운데 위아래 끝','풍지판 · 가운데 틈',MID)
tag((51.5,41),(82,48),'잠금장치 부근','창이 끝까지 닫히는지',WARN)
tag((40,13.5),(18,20),'창짝 아래','롤러 · 처짐 · 레일 이물질',MID)
tag((74,28),(82,24),'창틀과 벽 사이','실리콘 · 창 문제 아님',SAND)
finish(fig,O+'nangman_interior_mohair_fig1.png','바람이 새는 위치를 찾는 방법입니다 · 얼마나 새는지 재는 시험은 아닙니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 증상 세 갈래
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.03,0.08,0.94,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
fig.text(0.04,0.955,'샷시 모헤어는 단열재가 아닙니다',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'증상이 다르면 보는 곳도 다릅니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
R=[('바람이 샌다','모헤어 · 롤러 · 풍지판 · 실리콘','틈을 고치는 수리',NAVY),
   ('창 자체가 차갑다','유리 · 창틀의 단열 성능','유리·틀 교체를 비교',MID),
   ('물이 맺힌다','창 표면 온도 + 실내 습도','환기 · 습도부터',WARN)]
for i,(a,b,c,col) in enumerate(R):
    y=64-i*24
    ax.add_patch(FancyBboxPatch((3,y-8),28,16,boxstyle='round,pad=0.5',fc=col,ec=col))
    ax.text(17,y,a,fontsize=20,color='white',fontweight='bold',ha='center',va='center')
    ax.add_patch(FancyArrowPatch((32.5,y),(40,y),arrowstyle='-|>',mutation_scale=22,color=col,lw=3))
    ax.add_patch(FancyBboxPatch((41,y-8),56,16,boxstyle='round,pad=0.5',fc='white',ec=col,lw=2))
    ax.text(45,y+2.8,b,fontsize=18,color=NAVY,fontweight='bold',va='center')
    ax.text(45,y-3.6,c,fontsize=15,color='#555555',va='center')
finish(fig,O+'nangman_interior_mohair_fig2.png','모헤어는 미닫이 창이 움직이면서 생기는 틈을 막는 부품입니다',brand='낭만 인테리어',allow_outside=True,strict=False)
