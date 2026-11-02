import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_lotto_misa_gamil_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 로또분양 3편',['미사 감일 아파트 비교,','둘 다 10억 올랐다'],'감일은 8년, 미사는 13년 걸렸습니다',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.05,0.14,0.9,0.66])
head(fig,'미사 감일 아파트 비교 · 84㎡ 분양가와 2026년 평균 거래 가격','둘 다 10억 안팎 올랐고, 걸린 시간이 다릅니다')
X=[0,1,3,4]; V=[4.38,14.25,5.72,15.96]; C=[GREY,MID,GREY,WARN]
T=['4.38억','14.25억','5.72억','15.96억']
L=['분양가\n2013.10','2026년','분양가\n2018.5','2026년']
for x,v,c,t in zip(X,V,C,T):
    ax.bar(x,v,0.72,color=c); ax.text(x,v+0.35,t,ha='center',fontsize=19,fontweight='bold',color=SAND if c==GREY else c)
ax.set_xticks(X); ax.set_xticklabels(L,fontsize=16,color=TXT); ax.set_ylim(0,21.5)
ax.text(0.5,20.2,'미사강변푸르지오',ha='center',fontsize=19,color=MID,fontweight='bold')
ax.text(0.5,18.7,'+9.9억 · 약 13년 · 3.25배',ha='center',fontsize=17,color=MID)
ax.text(3.5,20.2,'힐스테이트포웰시티',ha='center',fontsize=19,color=WARN,fontweight='bold')
ax.text(3.5,18.7,'+10.2억 · 약 8년 · 2.79배',ha='center',fontsize=17,color=WARN)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.set_yticks([])
finish(fig,O+'fig1.png','84㎡ 최고 분양가 기준 · 2026년 평균은 미사 24건, 감일 7건',allow_outside=True,strict=False)
# fig2 slope
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.36,0.14,0.36,0.66])
head(fig,'미사 감일 아파트 비교 · 최근 3년 같은 평형 거래 가격','2023년엔 감일이 쌌고, 2026년엔 1.7억 비쌉니다')
for a,b,c,n,r,dy0,dy1 in [(10.08,14.25,MID,'미사강변푸르지오','+41.4%',0.75,0),(9.93,15.96,WARN,'힐스테이트포웰시티','+60.8%',-0.75,0)]:
    ax.plot([0,1],[a,b],color=c,lw=5,marker='o',ms=13)
    ax.text(-0.06,a+dy0,f'{n}\n{a:.2f}억',ha='right',va='center',fontsize=17,color=c,fontweight='bold',linespacing=1.3)
    ax.text(1.06,b,f'{b:.2f}억\n{r}',ha='left',va='center',fontsize=19,color=c,fontweight='bold',linespacing=1.3)
ax.set_xlim(-0.05,1.05); ax.set_ylim(8.2,17); ax.axis('off')
ax.text(0,8.3,'2023년',ha='center',fontsize=17,color=TXT); ax.text(1,8.3,'2026년',ha='center',fontsize=17,color=TXT)
finish(fig,O+'fig2.png','같은 단지 안에서 전용면적이 같은 평형끼리 짝지은 평균 · 포웰시티 2026년은 7건',allow_outside=True,strict=False)
