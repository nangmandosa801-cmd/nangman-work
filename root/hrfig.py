import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_hanamre_'
render('낭만 부동산 분석 플랫폼 · 하남 부동산 시세',
       ['하남 부동산 시세,','감일·미사 +22~23%, 덕풍·신장 +9~11%'],
       '2026년 같은 단지 기준 하남 전체 +17.0% · 84㎡ 5.6억~16.5억', O+'thumb.png')

g=['감이동 (감일)','망월동 (미사)','학암동 (위례)','선동 (미사)','풍산동','창우동','덕풍동','신장동']
a=[23.3,22.1,20.9,16.0,15.9,15.6,10.9,9.3]; b=[62.7,16.8,17.9,14.3,9.6,3.2,1.1,4.5]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.24,0.11,0.70,0.68])
fig.text(0.04,0.955,'하남 동별 같은 단지·같은 면적 가격 변화 중간값',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'올해 하남 +17.0%, 감일·미사는 22~23%',fontsize=24,color=NAVY,fontweight='bold',va='center')
fig.text(0.24,0.83,'■ 2025년→2026년',fontsize=15,color=NAVY,fontweight='bold'); fig.text(0.46,0.83,'■ 2021년→2026년',fontsize=15,color=SAND,fontweight='bold')
for i in range(len(g)):
    y=len(g)-1-i; hi=a[i]>=20
    ax.barh(y+0.19,a[i],0.36,color=WARN if hi else NAVY); ax.barh(y-0.19,b[i],0.36,color=SAND)
    ax.text(a[i]+0.8,y+0.19,f'+{a[i]}%',va='center',fontsize=14,color=WARN if hi else NAVY,fontweight='bold')
    ax.text(b[i]+0.8,y-0.19,f'+{b[i]}%',va='center',fontsize=14,color='#6E675C',fontweight='bold')
    fig.text(0.225,0.11+0.68*(y+0.5)/len(g),g[i],ha='right',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_ylim(-0.6,len(g)-0.4); ax.set_xlim(0,72); ax.set_yticks([]); ax.set_xticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axvline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','국토교통부 아파트 매매 실거래 · 2026년은 8월 계약분까지 · 두 해 모두 거래 있는 단지만',allow_outside=True,strict=False)

g2=['학암동 (위례)','감이동 (감일)','망월동 (미사)','풍산동','선동 (미사)','신장동','창우동','덕풍동']
v=[16.50,14.10,12.00,11.83,11.63,9.30,8.22,7.68]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.24,0.11,0.66,0.70])
fig.text(0.04,0.955,'하남 동별 84㎡ 거래금액 중간값 · 2026년 1~8월',fontsize=16,color=MID,va='center')
fig.text(0.04,0.895,'위례 16.5억, 원도심 덕풍 7.7억',fontsize=24,color=NAVY,fontweight='bold',va='center')
for i in range(len(g2)):
    y=len(g2)-1-i; c=NAVY if v[i]>=11 else SAND
    ax.barh(y,v[i],0.62,color=c)
    ax.text(v[i]+0.2,y,f'{v[i]:.2f}억',va='center',fontsize=16,color=NAVY,fontweight='bold')
    fig.text(0.225,0.11+0.70*(y+0.5)/len(g2),g2[i],ha='right',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_ylim(-0.6,len(g2)-0.4); ax.set_xlim(0,19.5); ax.set_yticks([]); ax.set_xticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axvline(0,color=LINE,lw=1.5)
finish(fig,O+'fig2.png','국토교통부 아파트 매매 실거래 · 전용 83~86㎡ · 해제 거래 제외',allow_outside=True,strict=False)
