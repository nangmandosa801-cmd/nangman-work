import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
O='/mnt/user-data/outputs/nangman_new/nangman_dtjupjup_'
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
def clean(ax):
    for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
# fig2 신청자 비교
fig=plt.figure(figsize=(11.2,9.4)); head(fig,'동탄 줍줍 경쟁률 · 무순위 신청자 수 비교','294만명에서 22만명, 5만명대로 줄었습니다')
ax=fig.add_axes([0.04,0.14,0.92,0.68])
R=[('동탄역 롯데캐슬','2024년 7월 · 1가구 · 시세차 약 10억원','전국 19세 이상 · 집이 있어도 가능',294.478,WARN,'294만 4,780명'),
   ('올림픽파크포레온','2025년 7월 · 4가구 · 시세차 약 10억원','무주택자',22.4693,MID,'22만 4,693명'),
   ('광명 철산자이 더 헤리티지','2026년 9월 · 4가구 · 시세차 약 6억~7억원','경기도 거주 무주택 세대구성원',5.4626,MID,'5만 4,626명')]
for k,(n,d,q,v,c,lab) in enumerate(R):
    y=(2-k)*1.35
    ax.text(0,y+0.36,n,fontsize=19,fontweight='bold',color=NAVY,va='bottom')
    ax.text(0,y+0.24,d,fontsize=13.5,color='#555',va='top')
    ax.barh(y-0.18,v,0.3,color=c,left=0)
    ax.text(v+4,y-0.18,lab,va='center',fontsize=18,fontweight='bold',color=c)
    ax.text(0,y-0.42,'신청 자격: '+q,fontsize=13.5,color=c if k==0 else NAVY,va='top',fontweight='bold')
ax.set_xlim(0,360); ax.set_ylim(-0.8,3.55); clean(ax)
finish(fig,O+'fig2.png','신청자는 공고 기준 · 가구 수와 면적, 대출 조건도 단지마다 다릅니다',allow_outside=True,strict=False)
# fig3 자기자금
fig=plt.figure(figsize=(11.2,7.6)); head(fig,'동탄역 롯데캐슬 84㎡ · 2024년 줍줍 당첨자와 지금 사는 사람','지금 22억원대에 사면 약 18억원이 필요합니다')
ax=fig.add_axes([0.04,0.2,0.92,0.58])
ax.barh(1,4.82,0.42,color=WARN); ax.text(4.82+0.3,1,'4억 8,200만원',va='center',fontsize=18,fontweight='bold',color=WARN)
ax.text(0,1.33,'2024년 7월 줍줍 당첨자 · 공급가',fontsize=17,fontweight='bold',color=NAVY)
ax.barh(0,18.25,0.42,color=NAVY); ax.barh(0,4,0.42,left=18.25,color=SAND)
ax.text(9.1,0,'직접 마련 약 18억 2,500만원',va='center',ha='center',fontsize=18,fontweight='bold',color='white')
ax.text(20.25,-0.3,'대출 최대 4억',va='top',ha='center',fontsize=15,fontweight='bold',color='#6b6457')
ax.text(0,0.33,'2026년 6월 최고 실거래 22억 2,500만원에 산다면',fontsize=17,fontweight='bold',color=NAVY)
ax.set_xlim(0,24); ax.set_ylim(-0.6,1.6); clean(ax)
fig.text(0.04,0.13,'규제지역 주택담보대출 한도(시가): 15억원 이하 6억 · 15억~25억원 4억 · 25억원 초과 2억',fontsize=14,color=NAVY)
fig.text(0.04,0.09,'실제 대출은 LTV 40% · DSR · 소득에 따라 더 적을 수 있고, 취득세·부대비용은 따로 듭니다',fontsize=14,color=NAVY)
finish(fig,O+'fig3.png','동탄은 2026년 7월 1일부터 규제지역 · 대출 4억원은 한도 상한 가정',allow_outside=True,strict=False)
