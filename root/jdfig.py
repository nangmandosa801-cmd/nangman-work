import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_jungdong_'
TXT='#444'; GREY='#C9C4BA'; LB='#9DBFE0'
render('낭만 부동산 분석 플랫폼 · 1기 신도시 중동',['중동 재건축,','은하마을 25%'],'같은 선도지구 반달마을A는 14.4%, 나머지 구축 8.8%',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.08,0.17,0.66,0.61])
head(fig,'중동 재건축 · 선도지구 발표 전(2024.1~10) 대비 상승률','특별정비구역이 된 은하마을이 가장 먼저, 가장 많이 올랐습니다')
P=['발표 전','2024.12~\n2025.3','2025.4~9','2025.10~\n2026.2','2026.3~8']
G=[('은하마을 (지정 완료)',[0,13.0,9.6,17.3,25.0],NAVY),('반달마을A (계획 준비)',[0,9.6,7.7,12.3,14.4],LB),('나머지 구축',[0,3.2,3.5,4.4,8.8],SAND),('2005년 이후 준공',[0,0.0,1.7,2.2,4.1],GREY)]
for n,v,c in G:
    ax.plot(range(5),v,color=c,lw=3.5 if c==NAVY else 2.8,marker='o',ms=7)
    ax.text(4.12,v[-1],f'{n} +{v[-1]}%',va='center',fontsize=13,color=c if c!=GREY else '#8A8578',fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels(P,fontsize=12,color=TXT); ax.set_ylim(-1.5,28)
ax.set_yticks([0,10,20]); ax.set_yticklabels(['0%','10%','20%'],fontsize=12,color=TXT)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color(LINE)
finish(fig,O+'fig1.png','같은 단지·같은 전용면적이 두 기간에 모두 거래된 경우만 비교 · 부천시 원미구 중동·상동',allow_outside=True,strict=False)
# fig3 2021H2
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0.26,0.14,0.66,0.62])
head(fig,'중동 재건축 · 2021년 하반기 평균 대비 2026년 3~8월 가격','2021년 하반기 가격을 넘은 곳은 은하마을뿐입니다')
D=[('2005년 이후 준공',-8.3,GREY),('나머지 구축',-8.9,SAND),('반달마을A',-12.9,LB),('은하마을',8.6,NAVY)]
for i,(n,v,c) in enumerate(D):
    ax.barh(i,v,0.58,color=c); ax.text(v+(0.4 if v>0 else -0.4),i,f'{v:+.1f}%',va='center',ha='left' if v>0 else 'right',fontsize=15,fontweight='bold',color=NAVY)
ax.axvline(0,color=TXT,lw=1.2); ax.set_xlim(-17,13); ax.set_xticks([])
ax.set_yticks(range(4)); ax.set_yticklabels([d[0] for d in D],fontsize=15,color=NAVY)
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
ax.text(0.3,3.55,'2021년 하반기 가격 →',fontsize=12,color=MID); ax.set_ylim(-0.6,3.8)
finish(fig,O+'fig2.png','두 기간에 모두 거래된 같은 단지·같은 전용면적만 비교',allow_outside=True,strict=False)
# fig2 5 cities
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.07,0.2,0.9,0.56])
head(fig,'1기 신도시 재건축 · 선도지구 발표 전 대비 2026년 3~8월 상승률','다섯 도시, 선도지구 뒤 가격 모습은 다섯 가지였습니다')
C=['분당','일산','산본','평촌','중동']
S=[(' 1차 선도지구',[46.3,-0.4,18.2,36.5,20.1],NAVY),(' 나머지 구축',[47.0,-5.1,4.0,31.5,8.8],LB),(' 2005년 이후 준공',[30.4,-4.4,9.0,18.2,4.1],GREY)]
x=np.arange(5); w=0.26
for k,(n,v,c) in enumerate(S):
    b=ax.bar(x+(k-1)*w,v,w*0.92,color=c,label=n.strip())
    for xi,vi in zip(x+(k-1)*w,v): ax.text(xi,vi+(1 if vi>=0 else -1),f'{vi:.1f}',ha='center',va='bottom' if vi>=0 else 'top',fontsize=10.5,color=NAVY)
ax.axhline(0,color=TXT,lw=1); ax.set_xticks(x); ax.set_xticklabels(C,fontsize=15,color=NAVY,fontweight='bold'); ax.set_yticks([]); ax.set_ylim(-9,53)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.legend(loc='upper right',fontsize=12,frameon=False,ncol=3)
finish(fig,O+'fig3.png','단위 % · 같은 단지·같은 전용면적 기준 · 중동 선도지구는 은하마을과 반달마을A 합산',allow_outside=True,strict=False)
