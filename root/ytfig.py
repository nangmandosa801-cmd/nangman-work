import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_yeongtong_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 영통',['영통 아파트 시세,','6.7억 영통동도 1년 +11.6%'],'13억 광교 이의동과 같은 비율로 올랐습니다',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
R=[('자연앤힐스테이트 (2012)',18.59,'이의동'),('광교중흥에스클래스 (2019)',17.68,'원천동'),('광교센트럴뷰 (2013)',15.90,'이의동'),('광교에듀포레 (2014)',15.10,'이의동'),
   ('광교푸르지오월드마크 (2015)',14.86,'이의동'),('광교아이파크 (2018)',14.09,'원천동'),('광교더리브 (2013)',13.94,'하동'),('광교호반베르디움 (2014)',13.49,'원천동'),
   ('광교더샵 (2018)',12.76,'원천동'),('힐스테이트영통 (2017)',12.70,'망포동')]
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.40,0.14,0.47,0.68])
head(fig,'영통 아파트 가격 순위 · 2026년 84㎡ 평균 거래 가격','1~9위가 모두 광교 단지입니다')
for i,(n,v,d) in enumerate(R):
    y=len(R)-1-i; c=MID if d!='망포동' else WARN
    ax.barh(y,v,0.62,color=c)
    ax.text(v+0.2,y,f'{v:.2f}억',va='center',fontsize=17,color=c,fontweight='bold')
    ax.text(-0.02,y,f'{n} · {d}',transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=15,color=NAVY if d!='망포동' else WARN,fontweight='bold' if d=='망포동' else 'normal')
ax.set_xlim(0,22); ax.set_yticks([]); ax.set_xticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
fig.text(0.40,0.095,'영통동 84㎡ 평균은 6억 7,200만원입니다',fontsize=15,color=WARN,fontweight='bold')
finish(fig,O+'fig1.png','2026년 1~8월 84㎡ 거래 5건 이상 단지 · 해제 거래 제외',allow_outside=True,strict=False)
G=[('하동','광교 호수',12.1,3.0,11.07),('망포동','망포역',11.9,7.9,7.72),('영통동','영통지구',11.6,2.7,6.72),('이의동','광교 중심',11.5,8.2,13.08),('원천동','광교 남쪽',9.1,2.9,12.09),('매탄동','매탄 주공',3.2,-0.2,6.04)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.07,0.24,0.88,0.52])
head(fig,'영통 집값 상승률 · 같은 단지 같은 평형 2025년 → 2026년','6.7억 영통동과 13억 이의동이 같은 비율로 올랐습니다')
for i,(g,d,v,r21,pr) in enumerate(G):
    c=WARN if g in('영통동','이의동') else (GREY if g=='매탄동' else MID)
    ax.bar(i,v,0.6,color=c)
    ax.text(i,v+0.4,f'+{v}%',ha='center',fontsize=21,fontweight='bold',color=c if c!=GREY else SAND)
    ax.text(i,-1.6,g,ha='center',fontsize=18,color=NAVY,fontweight='bold')
    ax.text(i,-2.9,d,ha='center',fontsize=13.5,color=TXT)
    ax.text(i,-4.5,f'84㎡ {pr:.2f}억',ha='center',fontsize=14,color=TXT)
fig.text(0.95,0.845,'영통구 전체  1년 +10.1% · 2021년 대비 +3.6%',ha='right',fontsize=15,color=NAVY,fontweight='bold')
ax.set_ylim(-5.2,15.5); ax.set_xlim(-0.6,5.6); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','같은 단지 · 같은 전용면적 짝 · 2023년 이후 준공 제외 · 해제 거래 제외',allow_outside=True,strict=False)
