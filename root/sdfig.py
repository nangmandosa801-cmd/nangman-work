import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_songdo_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 송도',['송도 아파트 시세,','신축 6·8공구가 구축 가격'],'2020년 신축과 2005년 구축이 같은 6억대',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
R=[('송도더샵파크애비뉴 (2018)',13.01,'3'),('송도더샵퍼스트파크 F15BL (2017)',11.96,'3'),('힐스테이트송도더스카이 (2024)',11.80,''),
   ('송도더샵퍼스트파크 F14BL (2017)',10.95,'3'),('송도센트럴파크푸르지오 (2015)',10.55,'1'),('송도더샵퍼스트파크 F13-1BL (2017)',10.22,'3'),
   ('송도자이더스타 (2024)',9.88,''),('더샵송도프라임뷰 20BL (2022)',9.76,'3'),('더샵송도센터니얼 (2023)',9.63,'3'),('송도글로벌파크베르디움 (2017)',9.36,'7')]
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.44,0.14,0.44,0.68])
head(fig,'송도 아파트 시세 순위 · 2026년 84㎡ 평균 거래 가격','10위 안에 3공구 단지가 여섯 곳입니다')
for i,(n,v,g) in enumerate(R):
    y=len(R)-1-i; c=WARN if g=='3' else GREY
    ax.barh(y,v,0.62,color=c)
    ax.text(v+0.15,y,f'{v:.2f}억',va='center',fontsize=17,color=WARN if g=='3' else SAND,fontweight='bold')
    ax.text(-0.02,y,n,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=15.5,color=WARN if g=='3' else NAVY,fontweight='bold' if g=='3' else 'normal')
ax.set_xlim(0,15.5); ax.set_yticks([]); ax.set_xticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
fig.text(0.44,0.095,'■ 3공구 (인천대입구역)',fontsize=15,color=WARN,fontweight='bold')
finish(fig,O+'fig1.png','2026년 1~8월 84㎡ 거래 5건 이상 단지 · 해제 거래 제외',allow_outside=True,strict=False)
# fig2
G=[('1공구','센트럴파크',-0.9,2.0,MID),('3공구','인천대입구역',-5.3,6.6,MID),('7공구','연세대 캠퍼스',-6.8,3.3,MID),('2·4공구','초기 구축',-8.7,1.5,GREY),('6·8공구','랜드마크시티',-15.0,0.2,WARN)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.07,0.22,0.88,0.56])
head(fig,'송도 공구별 비교 · 같은 단지 같은 평형 2021년 대비','가장 새 아파트인 6·8공구가 가장 덜 회복했습니다')
for i,(g,d,v,y1,c) in enumerate(G):
    ax.bar(i,v,0.6,color=c)
    ax.text(i,v-0.7,f'{v:+.1f}%',ha='center',va='top',fontsize=22,fontweight='bold',color=c if c!=GREY else SAND)
    ax.text(i,3.4,g,ha='center',fontsize=19,color=NAVY,fontweight='bold')
    ax.text(i,1.0,d,ha='center',fontsize=14,color=TXT)
    ax.text(i,-21.5,f'1년 {y1:+.1f}%',ha='center',fontsize=16,color=MID if y1<5 else WARN,fontweight='bold')
ax.axhline(0,color=LINE,lw=1.5)
fig.text(0.95,0.845,'송도 전체  2021년 대비 -8.4% · 1년 +2.5%',ha='right',fontsize=15,color=NAVY,fontweight='bold')
ax.set_ylim(-23,6.5); ax.set_xlim(-0.6,4.6); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','같은 단지 · 같은 전용면적 짝 · 2023년 이후 준공 제외 · 6·8공구는 랜드마크로 다섯 단지',allow_outside=True,strict=False)
