import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyosan_hub_'
render('낭만 부동산 분석 플랫폼 · 하남 교산신도시',
       ['교산 첫 분양 5억 6,800만원,','옆 59㎡는 지금 10억 9천'],
       '청약 일정 · 분양가 · 3호선 2032년까지', O+'thumb.png')

# fig1 : 호반써밋에듀파크 59㎡ 월별 중간값 vs A2 분양가
ym=['25.1','25.2','25.3','25.4','25.5','25.6','25.7','25.8','25.9','25.10','25.11','25.12','26.2','26.3','26.4','26.5','26.6','26.7','26.8']
v=[8.30,8.40,8.475,8.46,8.555,8.775,8.90,8.90,8.825,8.995,9.25,9.585,9.95,10.55,10.60,10.10,10.775,10.95,11.17]
x=list(range(len(ym)))
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.08,0.16,0.86,0.62])
fig.text(0.04,0.955,'하남호반써밋에듀파크 59㎡ 월별 중간값 vs 교산 A2 59㎡ 분양가',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'분양가는 그대로, 옆 아파트만 올랐습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.plot(x,v,color=WARN,lw=3.2,marker='o',ms=6)
ax.plot([x[0],x[-1]],[5.68,5.68],color=NAVY,lw=3.2)
ax.text(x[-1],5.68-0.45,'교산 A2 59㎡ 분양가 5.68억',ha='right',fontsize=15,color=NAVY,fontweight='bold')
ax.text(x[0],v[0]+0.35,'8.30억',ha='left',fontsize=14,color=WARN,fontweight='bold')
ax.text(x[-1],v[-1]+0.35,'11.17억',ha='right',fontsize=14,color=WARN,fontweight='bold')
ax.annotate('',xy=(4,5.78),xytext=(4,8.45),arrowprops=dict(arrowstyle='<->',color=SAND,lw=2))
ax.text(4.3,7.0,'분양 때\n약 2.8억',fontsize=15,color=SAND,fontweight='bold',va='center')
ax.annotate('',xy=(17,5.78),xytext=(17,10.85),arrowprops=dict(arrowstyle='<->',color=WARN,lw=2))
ax.text(16.7,8.2,'지금\n약 5.2억',fontsize=15,color=WARN,fontweight='bold',va='center',ha='right')
ax.text(8.5,4.55,'2026년 1월은 거래 없음',fontsize=12.5,color=SAND,ha='center')
for i in [0,3,6,9,12,15,18]: ax.text(i,4.0,ym[i],ha='center',va='top',fontsize=13,color=NAVY)
ax.set_xlim(-0.6,18.6); ax.set_ylim(3.6,12.2); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
finish(fig,O+'fig1.png','국토교통부 실거래 · 월별 중간값 · 2026년 8월까지 · 단순 가격 차이이며 당첨자 수익이 아님',allow_outside=True,strict=False)

# fig2 : 타임라인
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.04,0.12,0.92,0.66]); ax.set_xlim(2018,2033.2); ax.set_ylim(0,10); ax.axis('off')
fig.text(0.04,0.955,'하남 교산신도시 · 발표부터 3호선 개통까지',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'첫 입주와 3호선 개통 사이 약 3년',fontsize=23,color=NAVY,fontweight='bold',va='center')
ax.plot([2018.3,2032.9],[5,5],color=LINE,lw=6)
ax.axvspan(2029.45,2032.0,ymin=0.44,ymax=0.56,color='#F6E3DA')
E=[(2018.95,'2018.12','3기 신도시 발표',NAVY,1),(2019.8,'2019.10','지구 지정',NAVY,-1),(2023.7,'2023.9','땅 공사 시작',NAVY,1),
   (2025.35,'2025.5','A2 첫 청약\n263.2대 1',MID,-1),(2025.55,'2025.7','3호선\n기본계획 승인',MID,1),(2027.0,'2027','3호선 착공 목표',MID,-1),
   (2029.45,'2029.6','A2 입주 예정',WARN,1),(2032.0,'2032','3호선 개통 목표',WARN,-1)]
for xx,t,lab,c,up in E:
    ax.plot(xx,5,'o',color=c,ms=13)
    y=7.2 if up>0 else 2.8
    ax.plot([xx,xx],[5.4 if up>0 else 4.6,y-0.7 if up>0 else y+0.7],color=c,lw=1.5)
    nl=lab.count('\n'); ax.text(xx,y+((0.9+0.75*nl) if up>0 else -0.2),t,ha='center',fontsize=14,color=c,fontweight='bold',va='bottom' if up>0 else 'top')
    ax.text(xx,y+(0.1 if up>0 else -1.0),lab,ha='center',fontsize=13.5,color='#444444',va='bottom' if up>0 else 'top')
ax.text(30.72+2000,5.9,'약 3년',ha='center',fontsize=16,color=WARN,fontweight='bold')
finish(fig,O+'fig2.png','국토교통부·LH·경기도 발표 기준 · 착공·개통·입주는 목표이며 바뀔 수 있음',allow_outside=True,strict=False)
