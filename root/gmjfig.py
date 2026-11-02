import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gmjupjup_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 광명 줍줍',['광명 줍줍 경쟁률,','4대 1에서 1만 3천대 1로'],'철산자이 4가구에 5만 4,626명',O+'thumb.png')
fig=plt.figure(figsize=(11.2,9.2)); ax=fig.add_axes([0.05,0.12,0.9,0.68])
fig.text(0.04,0.955,'광명 줍줍 · 최근 2년 네 번의 신청자 수',fontsize=17,color=MID,va='center')
fig.text(0.04,0.905,'시세보다 쌀수록 신청자가 몰렸습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
D=[('2024년 4월 트리우스 광명',225,'52가구 · 4.32대 1','입주권이 분양가보다 약 2억 쌈',GREY),
   ('2026년 1월 힐스테이트 광명11',1020,'2가구 · 510대 1','16억원대 · 차이 작음',GREY),
   ('2026년 9월 철산자이 브리에르',7007,'2가구 · 약 3,500대 1','시세보다 약 4억 쌈',MID),
   ('2026년 9월 철산자이 더 헤리티지',54626,'4가구 · 13,656.5대 1','시세보다 약 6억~7억 쌈',WARN)]
for i,(n,v,a,b,c) in enumerate(D):
    y=(len(D)-1-i)*1.35
    w=np.log10(v)-1.5
    ax.barh(y,w,0.34,left=0,color=c)
    ax.text(0,y+0.36,n,fontsize=18,color=NAVY,fontweight='bold',va='bottom')
    ax.text(w+0.05,y,f'{v:,}명',fontsize=21,fontweight='bold',color=c if c!=GREY else SAND,va='center')
    ax.text(0,y-0.3,a+'   ·   '+b,fontsize=15,color=TXT,va='top')
ax.set_xlim(0,4.3); ax.set_ylim(-0.75,4.85); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig1.png','막대 길이는 신청자 수의 로그 눈금 · 브리에르는 특별공급 1가구 포함이라 참고용',allow_outside=True,strict=False)
