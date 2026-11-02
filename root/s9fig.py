import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_seoul9_'
render('낭만 부동산 분석 플랫폼 · 서울 9억대 아파트',
       ['서울 9억대 아파트,','딱 10억 358건, 10억 1천 아래 46건'],
       '성북·은평 84㎡는 9억대부터 · 2026년 1~8월 3,432건', O+'thumb.png')

# fig1 경계 비교
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.17,0.88,0.60])
fig.text(0.04,0.955,'서울 아파트 매매 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'10억 문턱은 9억보다 두 배 셉니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.50,0.825,'■ 딱 그 금액',fontsize=15,color=NAVY,fontweight='bold'); fig.text(0.68,0.825,'■ 바로 위 1천만원 구간',fontsize=15,color=SAND,fontweight='bold')
b=['9억원','10억원','11억원','12억원','15억원']; e=[426,358,329,381,333]; u=[92,46,43,20,19]; r=['4.6배','7.8배','7.7배','19.1배','17.5배']
for i in range(5):
    c=WARN if i in (1,3,4) else NAVY
    ax.bar(i-0.19,e[i],0.36,color=c); ax.bar(i+0.19,u[i],0.36,color=SAND)
    ax.text(i-0.19,e[i]+12,f'{e[i]}건',ha='center',fontsize=16,color=c,fontweight='bold')
    ax.text(i+0.19,u[i]+12,f'{u[i]}건',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i,-30,b[i],ha='center',va='top',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(i,-95,r[i]+' 차이',ha='center',va='top',fontsize=15,color=c,fontweight='bold')
ax.set_xlim(-0.6,4.6); ax.set_ylim(-170,560); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 서울 · 해제 거래 제외 · 바로 위 구간은 그 금액 제외',allow_outside=True,strict=False)

# fig2 면적
g=['성북구','은평구','강서구','양천구','노원구','동대문구','구로구','강동구','영등포구','관악구']
a6=[75.5,75.7,74.9,77.2,84.5,84.8,84.9,83.0,84.1,84.6]; a7=[84.7,84.6,80.9,78.4,84.6,84.9,84.9,59.9,60.8,60.0]
lab=['+9.2㎡','+8.9㎡','+6.0㎡','+1.3㎡','+0.1㎡','0.0㎡','0.0㎡','-23.1㎡','-23.3㎡','-24.7㎡']
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.16,0.10,0.66,0.70])
fig.text(0.04,0.955,'같은 구 8억대와 9억대 전용면적 중간값 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'1억 더 쓰면 성북은 84㎡로, 관악은 59㎡ 신축으로',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.16,0.835,'● 8억대',fontsize=15,color=SAND,fontweight='bold'); fig.text(0.28,0.835,'● 9억대',fontsize=15,color=NAVY,fontweight='bold')
for i,(n,x6,x7,t) in enumerate(zip(g,a6,a7,lab)):
    y=len(g)-1-i; yy=0.10+0.70*(y+0.5)/len(g)
    ax.plot([x6,x7],[y,y],color=LINE,lw=4,zorder=1)
    ax.scatter([x6],[y],s=170,color=SAND,zorder=2); ax.scatter([x7],[y],s=170,color=NAVY,zorder=3)
    fig.text(0.85,yy,t,fontsize=16,va='center',color=WARN if abs(x7-x6)>=6 else NAVY,fontweight='bold')
    fig.text(0.145,yy,n,fontsize=16,va='center',ha='right',color=NAVY,fontweight='bold')
ax.set_ylim(-0.5,len(g)-0.5); ax.set_xlim(55,92); ax.set_yticks([])
ax.set_xticks([60,70,80,85]); ax.set_xticklabels(['60㎡','70㎡','80㎡','85㎡'],fontsize=13,color=NAVY)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 8억대 8억 이상 9억 미만 · 9억대 9억 이상 10억 미만',allow_outside=True,strict=False)
