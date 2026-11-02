import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_lotto_gyeyang_a6_'
TXT='#444'; GREY='#C9C4BA'; LB='#9DBFE0'
render('낭만 부동산 분석 플랫폼 · 로또분양 2편',['인천계양 a6 청약,','84㎡ 7억의 위치'],'계양 신축보다 1억 비싸고 대장보다 1억 쌉니다',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1 분양가 변화
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'인천계양 a6 분양가 · 84㎡ 최고가 기준','사전청약 추정가 5.28억에서 본청약 7.17억으로 1.89억 올랐습니다')
X=['A6 사전청약 추정가','A2 본청약 (2024.10)','A6 본청약 (2026.8)']; V=[5.277,5.8411,7.1654]; C=[GREY,LB,NAVY]
for i,(v,c) in enumerate(zip(V,C)):
    ax.bar(i,v,0.55,color=c); ax.text(i,v+0.12,f'{v:.2f}억',ha='center',fontsize=16,fontweight='bold',color=NAVY)
ax.annotate('',xy=(2,7.75),xytext=(0,5.95),arrowprops=dict(arrowstyle='->',color=WARN,lw=2,connectionstyle='arc3,rad=-0.25'))
ax.text(1.0,8.05,'+1억 8,900만',fontsize=16,color=WARN,fontweight='bold',ha='center')
ax.set_xticks(range(3)); ax.set_xticklabels(X,fontsize=14,color=TXT); ax.set_ylim(0,8.9); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig1.png','A2와 A6는 본청약 시점과 위치가 다른 블록입니다 · 84㎡ 최고 분양가 기준',allow_outside=True,strict=False)
# fig2 84 구성
fig=plt.figure(figsize=(11.2,5.4)); ax=fig.add_axes([0.15,0.2,0.8,0.54])
head(fig,'인천계양 a6 84㎡ 42가구 공급 구성','일반공급은 84A 1가구뿐, 84B는 0가구입니다')
rows=[('84A 26가구',[18,1,6,1]),('84B 16가구',[11,0,5,0])]
cols=[GREY,'#DDD8CE',LB,WARN]; labs=['사전청약','이주자','특별공급','일반공급']
for y,(n,v) in enumerate(rows[::-1]):
    left=0
    for k,(x,c) in enumerate(zip(v,cols)):
        if x==0: continue
        ax.barh(y,x,0.55,left=left,color=c,edgecolor='white',lw=2)
        if k!=3 and x>=3: ax.text(left+x/2,y+0.42,f'{labs[k]} {x}',ha='center',va='bottom',fontsize=13,color=NAVY,fontweight='bold')
        left+=x
ax.annotate('일반공급 1',xy=(25.5,1.3),xytext=(27,1.62),fontsize=14,color=WARN,fontweight='bold',arrowprops=dict(arrowstyle='->',color=WARN))
ax.text(16.6,0,'  일반공급 0',va='center',fontsize=14,color=WARN,fontweight='bold')
ax.text(18.5,1.42,'이주자 1',ha='center',va='bottom',fontsize=12,color=MID); ax.set_yticks([0,1]); ax.set_yticklabels([r[0] for r in rows[::-1]],fontsize=15,color=NAVY); ax.set_xlim(0,31); ax.set_xticks([]); ax.set_ylim(-0.5,2.0)
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig2.png','A6 전체 일반공급은 38가구 · 일반공급이 많은 주택형은 59㎡',allow_outside=True,strict=False)
# fig3 ladder
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.36,0.16,0.56,0.62])
head(fig,'인천계양 a6 84㎡ 분양가와 계양구 주요 아파트 84㎡ 2026년 거래 가격','A6는 보통 신축보다 약 1억 비싸고 힐스테이트자이계양보다 약 1억 쌉니다')
D=[('계양하늘채파크포레 (2023, 1건)',5.70,GREY),('인천계양코아루센트럴파크 (2017)',5.84,GREY),('계양효성해링턴플레이스 (2021)',6.02,GREY),('e편한세상 계양 더프리미어 (2021)',6.25,GREY),('인천계양 A6 분양가 (2029 입주)',7.17,NAVY),('힐스테이트자이계양 (2024)',8.23,LB)]
for i,(n,v,c) in enumerate(D):
    ax.barh(i,v,0.62,color=c); ax.text(v+0.06,i,f'{v:.2f}억',va='center',fontsize=14,fontweight='bold',color=NAVY)
ax.set_yticks(range(len(D))); ax.set_yticklabels([d[0] for d in D],fontsize=13,color=TXT)
ax.get_yticklabels()[4].set_color(NAVY); ax.get_yticklabels()[4].set_fontweight('bold')
ax.axvline(7.17,color=NAVY,ls=':',lw=1.2); ax.set_xlim(5,8.9); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig3.png','A6는 84A 최고 분양가 · 나머지는 같은 단지·같은 평형 2026년 1~8월 평균 (힐스테이트자이계양은 두 평형 중 높은 쪽)',allow_outside=True,strict=False)
