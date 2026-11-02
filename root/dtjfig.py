import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_dtjupjup_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 동탄 줍줍',['동탄 줍줍,','294만명 몰린 4.82억 아파트'],'동탄역 롯데캐슬 84㎡, 2026년 22억대 거래',O+'thumb.png')
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.07,0.2,0.88,0.58])
fig.text(0.04,0.955,'동탄 줍줍 · 동탄역 롯데캐슬 84㎡ 공급가와 연도별 실거래',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'4억 8,200만원 줍줍이 최고 22억원대까지',fontsize=23,color=NAVY,fontweight='bold',va='center')
X=['줍줍 공급가\n(2024년 7월)','2023년','2024년','2025년','2026년\n1~8월']
avg=[4.82,15.0,15.5,16.18,19.04]; mx=[None,16.2,16.6,17.95,22.25]
for i,(a,m) in enumerate(zip(avg,mx)):
    c=WARN if i==0 else MID
    ax.bar(i,a,0.55,color=c)
    if i==0: ax.text(i,a+0.35,'4.82억',ha='center',fontsize=18,fontweight='bold',color=c)
    else: ax.text(i,a-0.6,f'{a:.2f}억',ha='center',va='top',fontsize=18,fontweight='bold',color='white')
    if m:
        ax.plot([i-0.3,i+0.3],[m,m],color=NAVY,lw=2.5)
        ax.text(i,m+0.35,f'최고 {m:.2f}억',ha='center',fontsize=14,color=NAVY,fontweight='bold')
    ax.text(i,-1.6,X[i],ha='center',va='top',fontsize=15,color=NAVY,fontweight='bold')
ax.text(0,7.2,'294만 4,780명\n신청',ha='center',fontsize=15,color=WARN,fontweight='bold')
ax.set_ylim(-4.5,25); ax.set_xlim(-0.6,4.9); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.60,0.84,'■ 연도별 평균',fontsize=15,color=MID,fontweight='bold'); fig.text(0.77,0.84,'━ 그해 최고가',fontsize=15,color=NAVY,fontweight='bold')
finish(fig,O+'fig1.png','동탄역 롯데캐슬 전용 84.7~84.8㎡ 실거래 · 해제 거래 제외 · 2026년은 8월 계약까지',allow_outside=True,strict=False)
