import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_seoul8_'
render('낭만 부동산 분석 플랫폼 · 서울 8억대 아파트',
       ['서울 8억대 아파트,','딱 9억 426건, 9억 1천 아래 92건'],
       '노원 84㎡는 8억대부터 · 2026년 1~8월 3,906건', O+'thumb.png')

# fig1 경계 비교
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.17,0.88,0.60])
fig.text(0.04,0.955,'서울 아파트 매매 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'9억원 앞에서 거래가 멈춥니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.50,0.825,'■ 딱 그 금액',fontsize=15,color=NAVY,fontweight='bold'); fig.text(0.68,0.825,'■ 바로 위 1천만원 구간',fontsize=15,color=SAND,fontweight='bold')
b=['6억원','7억원','8억원','9억원']; e=[620,421,389,426]; u=[77,154,133,92]; r=['8.1배','2.7배','2.9배','4.6배']
for i in range(4):
    c=WARN if i in (0,3) else NAVY
    ax.bar(i-0.19,e[i],0.36,color=c); ax.bar(i+0.19,u[i],0.36,color=SAND)
    ax.text(i-0.19,e[i]+12,f'{e[i]}건',ha='center',fontsize=16,color=c,fontweight='bold')
    ax.text(i+0.19,u[i]+12,f'{u[i]}건',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i,-30,b[i],ha='center',va='top',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(i,-95,r[i]+' 차이',ha='center',va='top',fontsize=15,color=c,fontweight='bold')
ax.set_xlim(-0.6,3.6); ax.set_ylim(-170,720); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 서울 · 해제 거래 제외 · 바로 위 구간은 그 금액 제외',allow_outside=True,strict=False)

# fig2 면적
g=['영등포구','마포구','노원구','강서구','동대문구','서대문구','구로구','중랑구','은평구']
a6=[61.2,59.9,66.6,60.0,70.4,74.2,84.7,84.8,82.4]; a7=[84.1,78.4,84.5,74.9,84.8,84.3,84.9,84.7,75.7]
lab=['+22.9㎡','+18.5㎡','+17.9㎡','+15.0㎡','+14.5㎡','+10.1㎡','+0.2㎡','-0.1㎡','-6.7㎡']
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.16,0.10,0.66,0.70])
fig.text(0.04,0.955,'같은 구 7억대와 8억대 전용면적 중간값 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'1억 더 쓰면 노원은 67㎡에서 84㎡로',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.16,0.835,'● 7억대',fontsize=15,color=SAND,fontweight='bold'); fig.text(0.28,0.835,'● 8억대',fontsize=15,color=NAVY,fontweight='bold')
for i,(n,x6,x7,t) in enumerate(zip(g,a6,a7,lab)):
    y=len(g)-1-i; yy=0.10+0.70*(y+0.5)/len(g)
    ax.plot([x6,x7],[y,y],color=LINE,lw=4,zorder=1)
    ax.scatter([x6],[y],s=170,color=SAND,zorder=2); ax.scatter([x7],[y],s=170,color=NAVY,zorder=3)
    fig.text(0.85,yy,t,fontsize=16,va='center',color=WARN if x7-x6>=10 else NAVY,fontweight='bold')
    fig.text(0.145,yy,n,fontsize=16,va='center',ha='right',color=NAVY,fontweight='bold')
ax.set_ylim(-0.5,len(g)-0.5); ax.set_xlim(55,90); ax.set_yticks([])
ax.set_xticks([60,70,80,85]); ax.set_xticklabels(['60㎡','70㎡','80㎡','85㎡'],fontsize=13,color=NAVY)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 7억대 7억 이상 8억 미만 · 8억대 8억 이상 9억 미만',allow_outside=True,strict=False)
