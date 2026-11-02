import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, LINE, WARN
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/'
# fig1
x=[0,1,2,3,4]
S={'1차 선도지구':([0,6.9,17.9,31.2,36.5],NAVY,'-'),
   '나머지 구축':([0,2.4,7.8,19.1,31.5],WARN,'-'),
   '2차 신청 단지':([0,2.9,5.3,13.8,26.8],MID,'-'),
   '2005년 이후 준공':([0,3.5,5.4,9.7,18.2],SAND,'--')}
fig,ax=plt.subplots(figsize=(11,6.8)); fig.subplots_adjust(left=0.07,right=0.99,top=0.84,bottom=0.2)
lab_y={'1차 선도지구':37.5,'나머지 구축':31.2,'2차 신청 단지':26.0,'2005년 이후 준공':18.2}
for k,(v,c,ls) in S.items():
    ax.plot(x,v,color=c,lw=3.2 if c==NAVY else 2.6,ls=ls,marker='o',ms=8,zorder=3)
    ax.text(4.2,lab_y[k],f'{k} +{v[-1]}%',color=c,fontsize=16,fontweight='bold',va='center')
ax.axvline(3.45,color=LINE,lw=2,ls='--',zorder=1)
ax.text(3.4,40.5,'2025.12.30\n귀인·민백 지정',ha='right',va='top',color=MID,fontsize=13.5,fontweight='bold')
ax.axhline(0,color=SAND,lw=1.2)
ax.set_xticks(x); ax.set_xticklabels(['발표 전\n2024.1~10','2024.12\n~2025.3','2025.4\n~2025.9','2025.10\n~2026.2','2026.3\n~2026.8'],fontsize=13,color='#555')
ax.set_yticks([0,10,20,30,40]); ax.set_yticklabels(['0%','+10%','+20%','+30%','+40%'],fontsize=13,color='#555')
ax.set_ylim(-3,43); ax.set_xlim(-0.3,5.7)
ax.grid(axis='y',color=LINE,lw=1); [s.set_visible(False) for s in ax.spines.values()]; ax.tick_params(length=0)
fig.text(0.04,0.955,'평촌 아파트 시세 · 선도지구 발표 뒤',fontsize=14,color=MID,va='center')
fig.text(0.04,0.9,'선도지구가 먼저 올랐고, 주변 구축이 차이를 줄였습니다',fontsize=19,color=NAVY,fontweight='bold',va='center')
finish(fig,O+'nangman_pyeongchon_fig1.png','같은 단지·같은 면적 기준 · 2024년 1~10월 가격 대비',allow_outside=True,strict=False)
# fig2
import numpy as np
C=['분당','일산','산본','평촌']; A=[46.3,-0.4,18.2,36.5]; B=[47.0,-5.1,4.0,31.5]
D=['먼저 오르고\n주변이 따라옴','내릴 때\n덜 내림','절차가 앞설수록\n더 오름','먼저 오르고\n주변이 따라오는 중']
fig,ax=plt.subplots(figsize=(11,6.6)); fig.subplots_adjust(left=0.04,right=0.97,top=0.8,bottom=0.33)
xi=np.arange(4); w=0.34
ax.bar(xi-w/2-0.01,A,w,color=NAVY,label='1차 선도지구'); ax.bar(xi+w/2+0.01,B,w,color=WARN,label='나머지 구축')
for i in range(4):
    for dx,v,c in [(-w/2-0.01,A[i],NAVY),(w/2+0.01,B[i],WARN)]:
        ax.text(i+dx,v+(1.2 if v>=0 else -1.3),f'{v:+.1f}%'.replace('-','−'),ha='center',va='bottom' if v>=0 else 'top',fontsize=15,fontweight='bold',color=c)
    ax.text(i,-15.5,C[i],ha='center',va='center',fontsize=18,fontweight='bold',color='#222')
    ax.text(i,-23.5,D[i],ha='center',va='center',fontsize=13.5,color='#555',linespacing=1.4)
ax.axhline(0,color=SAND,lw=1.2); ax.set_ylim(-9,53); ax.set_xlim(-0.6,3.6); ax.axis('off')
ax.legend(loc='upper right',frameon=False,fontsize=13.5,ncol=2,bbox_to_anchor=(1.0,1.08))
fig.text(0.04,0.955,'1기 신도시 재건축 · 선도지구 발표 뒤 가격',fontsize=14,color=MID,va='center')
fig.text(0.04,0.9,'분당은 따라잡았고, 평촌은 따라오는 중입니다',fontsize=19,color=NAVY,fontweight='bold',va='center')
finish(fig,O+'nangman_pyeongchon_fig2.png','2024년 1~10월 → 2026년 3~8월 · 같은 단지·같은 면적 기준',allow_outside=True,strict=False)
render('낭만 부동산 분석 플랫폼 · 평촌신도시',['평촌 아파트 시세,','선도지구는 2021년 가격을 넘었습니다'],'2021년 대비 선도지구 16.3% · 2차 신청 −0.3%',O+'nangman_pyeongchon_thumb.png')
