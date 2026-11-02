import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_rentaldong_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 소셜믹스',['임대동 확인 방법,','옆 동은 싸지 않았다'],'매매 0건 동 옆, 서울 14개 단지 실거래',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
C={101:13,102:12,103:16,104:6,105:7,106:14,107:5,108:5,109:7,110:2,111:10,112:9,113:8,114:9,115:10,116:8,117:12,118:17,119:23,120:4,121:10,122:6,123:0,124:0,125:0,126:0,127:49,128:47,129:73,130:63}
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.07,0.2,0.9,0.58])
head(fig,'센트라스 동별 매매 건수 · 2023년 1월 ~ 2026년 8월','123~126동만 3년 넘게 0건입니다')
ks=list(C)
for i,k in enumerate(ks):
    v=C[k]
    if v==0:
        ax.bar(i,1.2,0.7,color='white',edgecolor=WARN,lw=2)
    else:
        ax.bar(i,v,0.7,color=GREY)
ax.text(ks.index(124)+0.5,6,'0건',ha='center',fontsize=22,color=WARN,fontweight='bold')
ax.text(ks.index(124)+0.5,-9.5,'123~126동',ha='center',fontsize=17,color=WARN,fontweight='bold')
for k in [101,110,120,130]:
    ax.text(ks.index(k),-5,str(k),ha='center',fontsize=15,color=TXT)
ax.text(ks.index(129),76,'73건',ha='center',fontsize=16,color=SAND,fontweight='bold')
ax.set_xlim(-1,len(ks)); ax.set_ylim(0,82); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
fig.text(0.62,0.84,'거래 있는 26개 동 · 445건',fontsize=16,color=SAND,fontweight='bold')
finish(fig,O+'fig1.png','국토교통부 실거래가 상세 자료 · 소유권 이전등기 완료 건의 동 번호 · 해제 거래 제외',allow_outside=True,strict=False)
# fig2
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'임대동 후보 동에서 실제 거리별 값 차이 · 5개 단지','가까운 동이 더 싸지 않았습니다')
D=[('80m 안쪽',0.15,182),('80~160m',0.15,369),('160m 넘게',-0.32,258)]
for i,(n,v,c) in enumerate(D):
    col=MID if v>=0 else GREY
    ax.bar(i,v,0.56,color=col)
    ax.text(i,v+(0.04 if v>=0 else -0.04),f'{v:+.2f}%',ha='center',va='bottom' if v>=0 else 'top',fontsize=24,fontweight='bold',color=MID if v>=0 else SAND)
    ax.text(i,-0.58,n,ha='center',fontsize=19,color=NAVY,fontweight='bold')
    ax.text(i,-0.68,f'{c}건',ha='center',fontsize=15,color=TXT)
ax.axhline(0,color=LINE,lw=1.5)
ax.text(2.45,0.03,'단지 평균',ha='right',va='bottom',fontsize=15,color=SAND)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-0.72,0.4); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
finish(fig,O+'fig2.png','같은 단지·같은 평형·같은 반기 비교 후 층 효과 제외 · 동 위치는 OpenStreetMap',allow_outside=True,strict=False)
