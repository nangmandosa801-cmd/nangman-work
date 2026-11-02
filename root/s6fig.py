import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_seoul6_'
render('낭만 부동산 분석 플랫폼 · 서울 6억대 아파트',
       ['서울 6억대 아파트,','딱 6억 620건, 6억 1천 아래 77건'],
       '2026년 1~8월 서울 매매 4,635건 · 6억원이 경계선', O+'thumb.png')

# fig1 거래금액 계단
lab=['5억 8천\n만원대','5억 9천\n만원대','정확히\n6억원','6억 초과\n~6.1억 미만','6억 1천\n만원대','6억 2천\n만원대']
v=[440,625,620,77,303,426]; col=[SAND,SAND,WARN,NAVY,MID,MID]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.19,0.88,0.60])
fig.text(0.04,0.955,'서울 아파트 매매 거래금액별 건수 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'딱 6억원에 620건, 바로 위는 77건입니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
ax.bar(range(6),v,0.64,color=col)
for i,n in enumerate(v): ax.text(i,n+14,f'{n}건',ha='center',fontsize=17,color=NAVY,fontweight='bold')
for i,l in enumerate(lab): ax.text(i,-25,l,ha='center',va='top',fontsize=14,color=NAVY,linespacing=1.35)
ax.axvline(2.5,color=WARN,lw=2,ls='--'); ax.text(2.56,560,'6억원 경계',fontsize=15,color=WARN,fontweight='bold')
ax.set_xlim(-0.6,5.6); ax.set_ylim(-190,720); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 서울 · 해제 거래 제외 · 2026년 8월 계약분까지',allow_outside=True,strict=False)

# fig2 면적 비교
g=['중랑구','강북구','강동구','동대문구','구로구','노원구','금천구','도봉구','강서구']
a5=[59.6,63.8,60.8,59.5,59.7,54.6,84.8,84.4,51.5]; a6=[81.9,83.7,76.0,72.2,70.2,59.3,84.8,83.9,49.8]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.16,0.10,0.66,0.70])
fig.text(0.04,0.955,'같은 구 5억대와 6억대 전용면적 중간값 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.900,'1억 더 쓰면 중랑·강북은 20㎡ 넓어집니다',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.16,0.835,'● 5억대',fontsize=15,color=SAND,fontweight='bold'); fig.text(0.28,0.835,'● 6억대',fontsize=15,color=NAVY,fontweight='bold')
for i,(n,x5,x6) in enumerate(zip(g,a5,a6)):
    y=len(g)-1-i
    ax.plot([x5,x6],[y,y],color=LINE,lw=4,zorder=1)
    ax.scatter([x5],[y],s=170,color=SAND,zorder=2); ax.scatter([x6],[y],s=170,color=NAVY,zorder=3)
    d=x6-x5; d=4.8 if n=='노원구' else d; t=f'+{d:.1f}㎡' if d>0.05 else ('그대로' if abs(d)<0.05 else f'{d:.1f}㎡')
    fig.text(0.85,0.10+0.70*(y+0.5)/len(g),t,fontsize=16,va='center',color=WARN if d>=10 else NAVY,fontweight='bold')
    fig.text(0.145,0.10+0.70*(y+0.5)/len(g),n,fontsize=16,va='center',ha='right',color=NAVY,fontweight='bold')
ax.set_ylim(-0.5,len(g)-0.5); ax.set_xlim(45,90); ax.set_yticks([])
ax.set_xticks([50,60,70,80,85]); ax.set_xticklabels(['50㎡','60㎡','70㎡','80㎡','85㎡'],fontsize=13,color=NAVY)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 5억대 5억 이상 6억 미만 · 6억대 6억 이상 7억 미만',allow_outside=True,strict=False)
