import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 외풍 차단율
R=[('방풍비닐',100,'환기 안 됨 · 안 여는 창만',GREY),('노후주택 방풍재 (27가구 현장)',48.7,'창 침기량 감소 · 2017 논문',NAVY),('문풍지 (건설연 바람 실험)',25,'20~30% · 새는 압력 7→5',NAVY),('문풍지 (에너지관리공단 기밀 시험)',14,'신내9단지 노인정 · 2013',MID)]
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.33,0.12,0.64,0.66])
head(fig,'틈새바람 차단율 · 실험마다 잰 방법이 다릅니다','문풍지 효과, 기밀 시험 14%부터 낡은 집 49%까지입니다')
n=len(R)
for i,(nm,v,memo,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+1.5,y+0.1,f'{v:g}%',va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(v+1.5,y-0.22,memo,va='center',fontsize=12.5,color=MID)
    ax.text(-2,y,nm,ha='right',va='center',fontsize=14,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,130); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'moonpung_fig1.png','이데일리(2013.1.24) · YTN(2014.1.9) · Applied Mechanics and Materials 865(2017) · 새 아파트 창은 가스켓·모헤어가 있어 효과가 작음',brand='낭만 인테리어',allow_outside=True,strict=False)

# fig2 창 그림에 붙이는 곳
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.04,0.06,0.92,0.74])
head(fig,'미닫이창 기준 · 틈마다 맞는 문풍지가 다릅니다','문풍지 붙이는 곳, 겹침선은 풍지판이고 레일은 모헤어입니다')
# frame
ax.add_patch(Rectangle((0.08,0.08),0.56,0.80,fill=False,lw=10,ec=NAVY))
ax.add_patch(Rectangle((0.10,0.10),0.26,0.76,fill=False,lw=4,ec=MID))
ax.add_patch(Rectangle((0.36,0.10),0.26,0.76,fill=False,lw=4,ec=MID))
ax.add_patch(Rectangle((0.105,0.105),0.25,0.75,color='#E8F0F8'))
ax.add_patch(Rectangle((0.365,0.105),0.25,0.75,color='#E8F0F8'))
# 겹침선
ax.plot([0.36,0.36],[0.10,0.86],color=WARN,lw=6)
# 물구멍
ax.add_patch(Rectangle((0.20,0.085),0.05,0.012,color=WARN))
ax.add_patch(Rectangle((0.46,0.085),0.05,0.012,color=WARN))
# 레일
ax.plot([0.10,0.62],[0.112,0.112],color=NAVY,lw=3,ls='--')
marks=[('①',0.36,0.62,NAVY),('②',0.30,0.112,NAVY),('③',0.625,0.48,NAVY),('④',0.115,0.845,NAVY),('⑤',0.225,0.09,WARN)]
for t,x,y,c in marks:
    ax.plot(x,y,'o',ms=30,color='white',markeredgecolor=c,markeredgewidth=2.5,zorder=5)
    ax.text(x,y,t,ha='center',va='center',fontsize=16,color=c,fontweight='bold',zorder=6)
legend=[('① 두 짝 겹침선','풍지판',NAVY),('② 레일','모헤어',NAVY),('③ 창짝이 닿는 창틀 면','고무(EVA) 테이프',NAVY),('④ 창틀 귀퉁이','스펀지 (한 철용)',NAVY),('⑤ 물구멍','막지 말고 방충 배수캡',WARN)]
for i,(a,b,c) in enumerate(legend):
    y=0.80-i*0.16
    ax.text(0.69,y+0.035,a,ha='left',va='center',fontsize=14,color=MID,fontweight='bold')
    ax.text(0.69,y-0.035,'→ '+b,ha='left',va='center',fontsize=15.5,color=c,fontweight='bold')
ax.set_xlim(0,1.0); ax.set_ylim(0,0.95); clean(ax)
finish(fig,O+'moonpung_fig2.png','LX Z:IN 창호 부자재 설명(2022.6.7)·외풍 차단 방법(2023.12.7) · 위키트리(2026.9.25) · 틈 크기를 재고 두께를 고르세요',brand='낭만 인테리어',allow_outside=True,strict=False)

render_interior('낭만 인테리어 · 겨울 준비',['문풍지 붙이는 법','틈 크기부터 재세요'],'틈새바람 14~30% 차단 · 겹침선은 풍지판','물구멍은 막지 않기 · 현관 찬 공기는 중문',O+'moonpung_thumb.png')
print('ok')
