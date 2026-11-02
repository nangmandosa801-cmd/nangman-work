import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 신축 84 전세 비교
R=[('래미안원펜타스 (반포 2024)',21.0,MID),('래미안원베일리 (반포 2023)',20.0,MID),('디에이치반포라클라스 (반포 2021)',17.7,MID),('디에이치방배 호가 (2026)',15.0,WARN),('방배그랑자이 (2021)',14.0,NAVY),('서리풀e편한세상 (2010)',12.8,NAVY),('롯데캐슬아르떼 (2013)',12.5,NAVY),('방배아트자이 (2018)',12.1,NAVY)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.34,0.10,0.62,0.72])
head(fig,'전용 84㎡ 전세 보증금 중앙값 · 2026년 실거래 · 디에이치방배는 호가','디에이치방배 전세 호가 15억, 옆 방배그랑자이 실거래는 14억입니다')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+0.2,y,f'{v:.1f}억',va='center',fontsize=15.5,color=c,fontweight='bold')
    ax.text(-0.2,y,nm,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,25); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'dhbangbae_fig1.png','국토교통부 실거래가 서초구 전월세(2026.1~9) · 반포 신축은 20억, 방배 신축은 14억 · 호가는 아시아경제(7.10) 기준',allow_outside=True,strict=False)

# fig2 분기별 전세 중앙값
Q=['25.3Q','25.4Q','26.1Q','26.2Q','26.3Q']; A=[10.5,11.0,10.1,11.0,9.5]; B=[13.4,10.2,10.0,10.6,9.5]
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.07,0.14,0.88,0.62])
head(fig,'전용 84㎡ 전세 보증금 중앙값 · 분기별 · 2026년 3분기는 9월 신고 진행 중','방배동 전세, 입주 전 한 분기에 11.0억에서 9.5억으로 내렸습니다')
x=np.arange(len(Q))
ax.plot(x,A,color=WARN,lw=3.5,marker='o',ms=10); ax.plot(x,B,color=LB,lw=3,marker='o',ms=9)
for i in range(len(Q)):
    ax.text(x[i],A[i]+0.25,f'{A[i]}억',ha='center',va='bottom',fontsize=14,color=WARN,fontweight='bold')
    ax.text(x[i],B[i]-0.3,f'{B[i]}억',ha='center',va='top',fontsize=13,color='#5F7FA6',fontweight='bold')
    ax.text(x[i],8.3,Q[i],ha='center',va='top',fontsize=13.5,color=MID)
ax.plot([-0.3,0.0],[14.2,14.2],color=WARN,lw=3.5); ax.text(0.08,14.2,'방배동',fontsize=14,color=WARN,fontweight='bold',va='center')
ax.plot([-0.3,0.0],[13.6,13.6],color=LB,lw=3); ax.text(0.08,13.6,'서초구 나머지 동',fontsize=13,color='#5F7FA6',fontweight='bold',va='center')
ax.axvspan(3.6,4.4,color='#F3E3DD',zorder=0); ax.text(4.0,14.2,'9월 1일 입주',ha='center',fontsize=13,color=WARN,fontweight='bold')
ax.set_xlim(-0.4,4.6); ax.set_ylim(8.0,14.8); clean(ax)
finish(fig,O+'dhbangbae_fig2.png','2025년 3분기 서초구 13.4억은 반포 래미안원베일리 고가 계약이 몰린 분기 · 방배동 올해 전세 662건 중 갱신 304건(46%)',allow_outside=True,strict=False)

render('디에이치방배 전세',['3,064가구 9월 입주','호가 15억 · 옆 단지 14억'],'방배동 전세 중앙값은 입주 전 11억 → 9.5억',O+'dhbangbae_thumb.png')
print('ok')
