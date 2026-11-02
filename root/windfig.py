import sys; sys.path.insert(0,'/home/claude/blogkit')
from thumbnail import render_interior
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from viz import NAVY, MID, SAND, WARN, LINE, PALE
from note import finish
O='/mnt/user-data/outputs/int/'
render_interior('낭만 인테리어 · 겨울 준비',['현관 외풍 차단,','휴지 한 장으로 찾습니다'],'새는 곳부터 찾고 작은 수리부터 5단계','문풍지 · 틈새막이 · 고무패킹 · 방풍커튼 · 중문',O+'nangman_interior_wind_thumb.png')

# fig1: 현관문 정면 — 휴지가 흔들리는 곳과 먼저 볼 것
fig=plt.figure(figsize=(11.2,9.6)); ax=fig.add_axes([0.02,0.08,0.96,0.78]); ax.set_xlim(0,100); ax.set_ylim(0,80); ax.axis('off')
fig.text(0.04,0.955,'현관 외풍 차단 · 휴지 테스트',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'휴지가 흔들리는 곳에 따라 먼저 볼 것이 다릅니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
# 문틀과 문
ax.add_patch(Rectangle((30,6),30,68,fill=False,ec='#8A8578',lw=6))
ax.add_patch(Rectangle((31.5,7.5),27,65,color='#E9EDF2'))
ax.add_patch(Rectangle((53,38),3.5,7,color=NAVY))  # 손잡이
for y in (16,62): ax.add_patch(Rectangle((31.2,y),1.6,5,color=SAND))  # 경첩
def tag(x,y,tx,ty,t1,t2,c):
    sx=tx+11 if tx<x else (tx-12 if tx>x+5 else tx)
    sy=ty if sx!=tx else ty-5
    ax.add_patch(FancyArrowPatch((sx,sy),(x,y),arrowstyle='-|>',mutation_scale=16,color=c,lw=2))
    ax.text(tx,ty+2.2,t1,fontsize=16,color=c,fontweight='bold',ha='center')
    ax.text(tx,ty-2.2,t2,fontsize=14,color='#555555',ha='center')
tag(59.5,41,82,50,'손잡이 쪽 세로 틈','문이 끝까지 닫히는지',WARN)
ax.add_patch(FancyArrowPatch((60,77),(47,74.2),arrowstyle='-|>',mutation_scale=16,color=MID,lw=2)); ax.text(62,78.5,'위쪽 · 경첩 쪽 일부  →  그 부분 문풍지',fontsize=15,color=MID,fontweight='bold',va='center')
tag(45,6.5,82,12,'문 아래','바닥 틈새막이',MID)
tag(30.5,50,12,56,'테두리 전체','고무패킹 상태',NAVY)
ax.add_patch(FancyBboxPatch((3,18),22,20,boxstyle='round,pad=0.6',fc='#FFF6E0',ec=WARN,lw=1.6))
ax.text(14,33,'거의 안 흔들리는데',ha='center',fontsize=14,color=WARN,fontweight='bold')
ax.text(14,28.5,'현관이 춥다',ha='center',fontsize=14,color=WARN,fontweight='bold')
ax.text(14,23,'문 · 벽 · 바닥이',ha='center',fontsize=13,color='#555555')
ax.text(14,19.5,'차가운지',ha='center',fontsize=13,color='#555555')
finish(fig,O+'nangman_interior_wind_fig1.png','후드나 환풍기를 켜 두면 틈으로 들어오는 바람이 세져 찾기 쉽습니다',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2: 5단계
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.03,0.07,0.94,0.8]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
fig.text(0.04,0.955,'현관 외풍 차단 5단계',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'앞 단계에서 해결되면 거기서 멈춥니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
S=[('1','문이 제대로 닫히는지 확인','손잡이 쪽을 밀어 보기 · 조정은 관리사무소에',NAVY),
   ('2','문풍지 · 틈새막이','한두 군데 새는 틈만',NAVY),
   ('3','고무패킹 점검 · 교체','테두리 전체가 새고 고무가 굳었을 때',NAVY),
   ('4','방풍커튼 · 방풍비닐','틈을 막아도 추울 때 · 현관을 나누기',MID),
   ('5','중문 검토','오래 살 집 · 출입 편의까지 원할 때',MID)]
for i,(n,t,d,c) in enumerate(S):
    y=84-i*17; x=4+i*6
    ax.add_patch(FancyBboxPatch((x,y-6),58,12,boxstyle='round,pad=0.4',fc='white',ec=c,lw=2))
    ax.text(x+4,y,n,fontsize=26,color=c,fontweight='bold',va='center',ha='center')
    ax.text(x+10,y+2.2,t,fontsize=18,color=c,fontweight='bold',va='center')
    ax.text(x+10,y-2.8,d,fontsize=13.5,color='#555555',va='center')
ax.plot([90,90],[90,46],color=NAVY,lw=3); ax.text(91.5,68,'바람이\n새는 집',fontsize=15,color=NAVY,fontweight='bold',va='center')
ax.plot([90,90],[39,12],color=MID,lw=3); ax.text(91.5,25.5,'문 자체가\n차가운 집',fontsize=15,color=MID,fontweight='bold',va='center')
finish(fig,O+'nangman_interior_wind_fig2.png','비용은 제품과 시공 범위에 따라 수천원부터 중문 시공비까지 크게 다릅니다',brand='낭만 인테리어',allow_outside=True,strict=False)
