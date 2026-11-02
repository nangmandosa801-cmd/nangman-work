import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 역별 1년 변동
R=[('성남역 (백현·삼평)',23.7),('동탄역 (청계·영천)',17.3),('구성역 (마북·보정)',13.9),('경기 전체',3.4),('대곡역 (토당·행신)',0.0),('운정역 (목동·야당·동패)',-2.8),('킨텍스역 (대화·장항)',-4.4)]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.28,0.10,0.68,0.72])
head(fig,'같은 단지·같은 전용면적 중앙값 · 2025.3~8 → 2026.3~8 · 국토교통부 실거래가','GTX-A 역세권 집값, 남쪽 세 역은 두 자릿수 북쪽 세 역은 내렸습니다')
n=len(R)
for i,(nm,v) in enumerate(R):
    y=n-1-i; c=NAVY if v>5 else (GREY if nm=='경기 전체' else WARN)
    ax.barh(y,v,0.6,color=c)
    ax.text(v+(0.4 if v>=0 else -0.4),y,f'{v:+.1f}%',ha='left' if v>=0 else 'right',va='center',fontsize=15,color=c if c!=GREY else MID,fontweight='bold')
    ax.text(-6.5,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(0,color=LINE,lw=1.5)
ax.set_xlim(-6.5,30); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'gtxa_fig1.png','비교 쌍: 성남 57 · 동탄 131 · 구성 80 · 대곡 113 · 운정 156 · 킨텍스 57 · 경기 12,599 · 남쪽은 수서에서 강남 직결, 북쪽은 서울역',allow_outside=True,strict=False)

# fig2 동탄역 월별 거래
M=['25.1','2','3','4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8']
V=[80,134,165,128,148,308,113,94,189,389,342,207,350,252,299,274,363,462,34,36]
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.06,0.14,0.90,0.62])
head(fig,'동탄역 주변(청계동·영천동) 아파트 월별 거래 · 2026년 8월은 신고 진행 중','동탄역 아파트 거래, 7월 규제지역 지정 뒤 462건이 34건이 됐습니다')
import numpy as np
x=np.arange(len(M))
cols=[WARN if i>=18 else NAVY for i in range(len(M))]
ax.bar(x,V,0.7,color=cols)
for i in [5,9,17,18]:
    ax.text(x[i],V[i]+8,f'{V[i]}',ha='center',va='bottom',fontsize=13.5,color=NAVY if i<18 else WARN,fontweight='bold')
for i,m in enumerate(M):
    if i%2==0 or i>=17: ax.text(x[i],-12,m,ha='center',va='top',fontsize=12,color=MID)
ax.text(19.2,150,'7월 규제지역 지정\n(투기과열·조정대상·토허)',ha='center',va='bottom',fontsize=12.5,color=WARN,fontweight='bold',linespacing=1.4)
ax.set_xlim(-0.7,len(M)+1.2); ax.set_ylim(-40,540); clean(ax)
finish(fig,O+'gtxa_fig2.png','국토교통부 아파트 실거래가 · 해제 거래 제외 · 2025년 10월 389건은 10·15 대책 직전 매수',allow_outside=True,strict=False)

render('GTX-A 삼성역 개통',['철근 누락 · 2027년 중순으로','동탄 +17% 운정 -3%'],'남쪽은 강남 직결로 올랐고 북쪽은 삼성역을 기다립니다',O+'gtxa_thumb.png')
print('ok')
