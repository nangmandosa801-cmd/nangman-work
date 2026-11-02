import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_lotto_3gi_price_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 로또분양 4편',['3기 신도시 분양가 비교,','옆 신축보다 얼마 싼가'],'왕숙 −2~3억 · 창릉 −0.2~0.8억 · 계양 +1억',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1 dumbbell
R=[('왕숙 A-1',6.94,9.39,10.11,'다산','26~31% 낮음',WARN),
   ('왕숙 A-3',7.32,9.39,10.11,'다산','22~28% 낮음',WARN),
   ('창릉 S-1',7.83,8.81,9.38,'원흥','11~16% 낮음',MID),
   ('창릉 S-4',8.6,8.81,9.38,'원흥','2~8% 낮음',MID),
   ('계양 A6',7.17,5.70,6.25,'계양 신축','15~26% 높음',NAVY)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.17,0.12,0.62,0.7])
head(fig,'3기 신도시 분양가 비교 · 84㎡ 분양가와 옆 신축 2026년 평균','왕숙은 옆 신축보다 2~3억 낮고, 계양은 오히려 높습니다')
for i,(n,p,lo,hi,nb,t,c) in enumerate(R):
    y=len(R)-1-i
    ax.plot([lo,hi],[y,y],color=GREY,lw=16,solid_capstyle='round')
    ax.text((lo+hi)/2,y+0.33,nb,ha='center',fontsize=14,color=SAND)
    ax.plot([p],[y],'o',color=c,ms=20)
    ax.text(p,y-0.4,f'{p:.2f}억',ha='center',fontsize=15,color=c,fontweight='bold')
    ax.text(-0.02,y,n,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=19,color=NAVY,fontweight='bold')
    ax.text(1.02,y,t,transform=ax.get_yaxis_transform(),ha='left',va='center',fontsize=17,color=c,fontweight='bold')
ax.set_xlim(5.3,10.6); ax.set_ylim(-0.8,4.7); ax.set_yticks([])
ax.set_xticks([6,7,8,9,10]); ax.set_xticklabels(['6억','7억','8억','9억','10억'],fontsize=15,color=TXT)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig1.png','점 = 84㎡ 분양가(최고) · 회색 막대 = 옆 신축 84㎡ 2026년 평균 범위',allow_outside=True,strict=False)
# fig2 competition
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.07,0.2,0.88,0.58])
head(fig,'3기 신도시 청약 · 2026년 5월 같은 주 본청약 블록 평균 경쟁률','왕숙 두 블록은 100대 1을 넘었습니다')
B=[('왕숙 A-3',126.8,'다산보다 22~28% 낮음',WARN),('왕숙 A-1',105.5,'다산보다 26~31% 낮음',WARN),('창릉 S-1',61.2,'원흥보다 11~16% 낮음',MID)]
for i,(n,v,t,c) in enumerate(B):
    ax.bar(i,v,0.6,color=c); ax.text(i,v+3,f'{v}대 1',ha='center',fontsize=22,fontweight='bold',color=c)
    ax.text(i,-26,t,ha='center',fontsize=15,color=TXT)
ax.set_xticks(range(3)); ax.set_xticklabels([b[0] for b in B],fontsize=19,color=NAVY,fontweight='bold')
ax.set_ylim(0,148); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig2.png','경쟁률은 공급 가구수 · 주택형 · 입지 · 지역 조건에 따라서도 달라집니다',allow_outside=True,strict=False)
