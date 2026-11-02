import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_seoul7_'
render('낭만 부동산 분석 플랫폼 · 서울 7억대 아파트',
       ['서울 7억대 아파트,','강북 84㎡ vs 노원 59㎡'],
       '같은 7억 4천 · 2004년 새 아파트와 1988년 재건축 단지', O+'thumb.png')

# fig1 경계 비교
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.17,0.88,0.60])
fig.text(0.04,0.955,'서울 아파트 매매 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'7억원에는 6억원 같은 계단이 약합니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.50,0.825,'■ 딱 그 금액',fontsize=15,color=NAVY,fontweight='bold'); fig.text(0.68,0.825,'■ 바로 위 1천만원 구간',fontsize=15,color=SAND,fontweight='bold')
b=['6억원','7억원','8억원']; e=[620,421,389]; u=[77,154,133]; r=['8.1배','2.7배','2.9배']
for i in range(3):
    c=WARN if i==0 else NAVY
    ax.bar(i-0.19,e[i],0.36,color=c); ax.bar(i+0.19,u[i],0.36,color=SAND)
    ax.text(i-0.19,e[i]+12,f'{e[i]}건',ha='center',fontsize=16,color=c,fontweight='bold')
    ax.text(i+0.19,u[i]+12,f'{u[i]}건',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i,-30,b[i],ha='center',va='top',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(i,-95,r[i]+' 차이',ha='center',va='top',fontsize=15,color=c,fontweight='bold')
ax.set_xlim(-0.6,2.6); ax.set_ylim(-170,720); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 서울 · 해제 거래 제외 · 바로 위 구간은 그 금액 제외',allow_outside=True,strict=False)

# fig2 면적
g=['관악구','은평구','양천구','구로구','서대문구','노원구','중랑구','강북구','도봉구']
a6=[60.0,65.3,64.0,70.2,60.0,59.3,81.9,83.7,83.9]; a7=[84.8,82.4,79.2,84.7,74.2,66.6,84.8,84.8,81.8]
lab=['+24.8㎡','+17.2㎡','+15.2㎡','+14.4㎡','+14.3㎡','+7.2㎡','+2.9㎡','+1.0㎡','-2.1㎡']
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.16,0.10,0.66,0.70])
fig.text(0.04,0.955,'같은 구 6억대와 7억대 전용면적 중간값 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'1억 더 쓰면 관악은 60㎡에서 85㎡로',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.16,0.835,'● 6억대',fontsize=15,color=SAND,fontweight='bold'); fig.text(0.28,0.835,'● 7억대',fontsize=15,color=NAVY,fontweight='bold')
for i,(n,x6,x7,t) in enumerate(zip(g,a6,a7,lab)):
    y=len(g)-1-i; yy=0.10+0.70*(y+0.5)/len(g)
    ax.plot([x6,x7],[y,y],color=LINE,lw=4,zorder=1)
    ax.scatter([x6],[y],s=170,color=SAND,zorder=2); ax.scatter([x7],[y],s=170,color=NAVY,zorder=3)
    fig.text(0.85,yy,t,fontsize=16,va='center',color=WARN if x7-x6>=10 else NAVY,fontweight='bold')
    fig.text(0.145,yy,n,fontsize=16,va='center',ha='right',color=NAVY,fontweight='bold')
ax.set_ylim(-0.5,len(g)-0.5); ax.set_xlim(55,90); ax.set_yticks([])
ax.set_xticks([60,70,80,85]); ax.set_xticklabels(['60㎡','70㎡','80㎡','85㎡'],fontsize=13,color=NAVY)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 6억대 6억 이상 7억 미만 · 7억대 7억 이상 8억 미만',allow_outside=True,strict=False)
