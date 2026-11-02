import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_lotto_gwacheon_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 로또분양 5편',['과천 로또 청약,','미달도 415대 1도 13억'],'써밋 1.91배 · 라비엔오 2.66배',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.05,0.14,0.9,0.64])
head(fig,'과천 로또 청약 · 84㎡ 분양가와 2026년 평균 거래 가격','오른 금액은 둘 다 13억, 출발 분양가는 5.9억 차이')
X=[0,1,3,4]; V=[13.85,26.51,7.92,21.09]; C=[GREY,MID,GREY,WARN]
T=['13.85억','26.51억','7.92억','21.09억']; L=['분양가\n2019.7','2026년','분양가\n2020.11','2026년']
for x,v,c,t in zip(X,V,C,T):
    ax.bar(x,v,0.72,color=c); ax.text(x,v+0.5,t,ha='center',fontsize=19,fontweight='bold',color=SAND if c==GREY else c)
ax.set_xticks(X); ax.set_xticklabels(L,fontsize=16,color=TXT); ax.set_ylim(0,36)
ax.text(0.5,33.8,'과천 푸르지오 써밋',ha='center',fontsize=19,color=MID,fontweight='bold')
ax.text(0.5,31.4,'1순위 미달 · +12.7억 · 1.91배',ha='center',fontsize=17,color=MID)
ax.text(3.5,33.8,'라비엔오 (지정타)',ha='center',fontsize=19,color=WARN,fontweight='bold')
ax.text(3.5,31.4,'415.7대 1 · +13.2억 · 2.66배',ha='center',fontsize=17,color=WARN)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.set_yticks([])
finish(fig,O+'fig1.png','84㎡ 최고 분양가 기준 · 2026년 평균은 써밋 10건, 라비엔오 5건',allow_outside=True,strict=False)
# fig2 slope
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.36,0.14,0.36,0.66])
head(fig,'과천 로또 청약 · 최근 2년 같은 평형 거래 가격','둘 다 30% 안팎 올랐습니다')
for a,b,c,n,r in [(20.85,26.51,MID,'과천 푸르지오 써밋','+27.2%'),(15.97,21.19,WARN,'라비엔오','+32.7%')]:
    ax.plot([0,1],[a,b],color=c,lw=5,marker='o',ms=13)
    ax.text(-0.06,a,f'{n}\n{a:.2f}억',ha='right',va='center',fontsize=17,color=c,fontweight='bold',linespacing=1.3)
    ax.text(1.06,b,f'{b:.2f}억\n{r}',ha='left',va='center',fontsize=19,color=c,fontweight='bold',linespacing=1.3)
ax.set_xlim(-0.05,1.05); ax.set_ylim(13.5,28.5); ax.axis('off')
ax.text(0,13.6,'2024년',ha='center',fontsize=17,color=TXT); ax.text(1,13.6,'2026년',ha='center',fontsize=17,color=TXT)
finish(fig,O+'fig2.png','같은 단지 안에서 전용면적이 같은 평형끼리 짝지은 평균 · 2026년 써밋 10건, 라비엔오 4건',allow_outside=True,strict=False)
