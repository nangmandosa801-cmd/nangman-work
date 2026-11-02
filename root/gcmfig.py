import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gcmusunwi_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 과천 무순위',['과천 무순위,','13억 싸도 특별공급입니다'],'라비엔오 84㎡ 7.6~8.0억, 실거래 21억',O+'thumb.png')
D=[('라비엔오 84㎡','특별공급 2가구 · 9월 28일',7.80,21.09,'7.61~8.03억','21.09억'),
   ('벨라르테 99㎡','일반공급 1가구 · 9월 28일',9.52,20.80,'9.52억','20.80억'),
   ('디에트르 퍼스티지 59㎡','일반 5가구 · 4월 · 650대 1',8.28,18.80,'7.85~8.70억','18.6~19.0억')]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
fig.text(0.04,0.955,'과천 무순위 · 공급가와 같은 평형 최근 실거래',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'분양 때 가격으로 다시 나와 10억~13억원 차이가 납니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
w=0.34
for i,(n,s,a,b,la,lb) in enumerate(D):
    ax.bar(i-w/2-0.02,a,w,color=MID); ax.bar(i+w/2+0.02,b,w,color=WARN)
    ax.text(i-w/2-0.02,a+0.4,la,ha='center',fontsize=15,fontweight='bold',color=MID)
    ax.text(i+w/2+0.02,b+0.4,lb,ha='center',fontsize=15,fontweight='bold',color=WARN)
    ax.text(i,-2.4,n,ha='center',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(i,-4.1,s,ha='center',fontsize=14,color=TXT)
ax.axhline(0,color=LINE,lw=1.5)
ax.set_ylim(-5,24); ax.set_xlim(-0.6,2.6); ax.set_xticks([]); ax.set_yticks([])
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
fig.text(0.60,0.84,'■ 이번 공급가',fontsize=15,color=MID,fontweight='bold'); fig.text(0.78,0.84,'■ 최근 실거래',fontsize=15,color=WARN,fontweight='bold')
finish(fig,O+'fig1.png','실거래는 같은 단지 같은 평형 2026년 거래(디에트르는 옆 래미안슈르 59㎡ 7월) · 해제 거래 제외',allow_outside=True,strict=False)
