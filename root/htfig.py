import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_hntoheo_'

render('낭만 부동산 분석 플랫폼 · 하남 토지거래허가',
       ['하남 토지거래허가,','지정 직전 5일 44건, 뒤엔 0건'],
       '24개 동 자연녹지 · 8월 18일부터 12월 31일까지', O+'thumb.png')

# fig1 : 8월 일별 계약 (항동 한 필지 구분)
days=list(range(1,30))
other={5:2,6:2,11:1,12:3,13:2,14:6,15:3,16:1,17:4}
hang={13:13,14:14,15:1}
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.06,0.17,0.90,0.60])
fig.text(0.04,0.955,'하남 녹지 토지 일별 계약 · 2026년 8월 1~29일',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'지정 직전 5일 44건, 지정 뒤 12일 0건',fontsize=23,color=NAVY,fontweight='bold',va='center')
for d in days:
    o=other.get(d,0); h=hang.get(d,0)
    if o: ax.bar(d,o,0.72,color=MID)
    if h: ax.bar(d,h,0.72,bottom=o,color=WARN)
    if o+h: ax.text(d,o+h+0.5,str(o+h),ha='center',fontsize=14,fontweight='bold',color=NAVY)
ax.plot([12.6,12.6,17.4,17.4],[21.2,22.4,22.4,21.2],color=NAVY,lw=2.2)
ax.axvline(17.5,color=NAVY,lw=2.4,ls='--')
ax.text(15,23.2,'8.13 발표 ~ 8.17',ha='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.text(23.5,6.5,'8.18 지정 뒤\n0건',ha='center',fontsize=20,color=NAVY,fontweight='bold',linespacing=1.4)
for d in [1,5,10,13,15,18,20,25,29]:
    ax.text(d,-1.2,f'{d}일',ha='center',va='top',fontsize=13,color=NAVY)
ax.set_xlim(0.2,29.8); ax.set_ylim(-3.2,26); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.55,0.835,'■ 항동 산3* 한 필지 (28건)',fontsize=14,color=WARN,fontweight='bold')
fig.text(0.80,0.835,'■ 그 밖 (16건)',fontsize=14,color=MID,fontweight='bold')
finish(fig,O+'fig1.png','용도지역 자연녹지·개발제한구역 · 해제 거래 제외 · 8월 29일 계약분까지 · 신고 기한이 남아 조금 늘 수 있음',allow_outside=True,strict=False)

# fig2 : 2024 에피소드
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.07,0.16,0.88,0.60])
fig.text(0.04,0.955,'2024년 감북·감일·감이·초이동 녹지 토지 계약',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'묶인 석 달 동안 172건이 4건이 됐습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
X=['지정 전 석 달\n2024.5.15~8.12','지정 중\n2024.8.13~11.10','해제 뒤 석 달\n2024.11.11~2025.2.8']
A=[172,4,71]; B=[50,65,172]; w=0.36
for i in range(3):
    ax.bar(i-w/2,A[i],w,color=WARN); ax.bar(i+w/2,B[i],w,color=SAND)
    ax.text(i-w/2,A[i]+4,str(A[i]),ha='center',fontsize=18,fontweight='bold',color=WARN)
    ax.text(i+w/2,B[i]+4,str(B[i]),ha='center',fontsize=16,fontweight='bold',color=SAND)
    ax.text(i,-10,X[i],ha='center',va='top',fontsize=14.5,color=NAVY,fontweight='bold',linespacing=1.5)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-48,200); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.44,0.815,'■ 묶인 네 개 동',fontsize=14.5,color=WARN,fontweight='bold')
fig.text(0.66,0.815,'■ 하남 나머지 동',fontsize=14.5,color=SAND,fontweight='bold')
finish(fig,O+'fig2.png','녹지 100㎡ 초과 허가 · 11월 5일 신규택지 발표에서 하남 제외 뒤 11월 10일부터 해제',allow_outside=True,strict=False)
print('ok')
