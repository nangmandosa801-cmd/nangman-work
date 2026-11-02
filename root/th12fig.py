import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1
R=[('경기 12곳\n(토지거래허가)',17.3,'1,614쌍'),('서울 25개 구\n(토지거래허가)',16.3,'2,613쌍'),('경기 나머지\n(규제 없음)',0.6,'3,643쌍')]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.08,0.20,0.86,0.56])
head(fig,'같은 단지·같은 면적 · 지정 전 2025년 4~9월 → 지정 뒤 2026년 3~8월 중간값','토지거래허가구역 1년, 묶인 곳 17.3% · 안 묶인 곳 0.6%')
for i,(nm,v,c) in enumerate(R):
    col=NAVY if i<2 else GREY
    ax.bar(i,v,0.56,color=col); ax.text(i,v+0.5,f'+{v:.1f}%',ha='center',fontsize=22,color=NAVY,fontweight='bold')
    ax.text(i,-1.5,nm,ha='center',va='top',fontsize=16,color=NAVY,fontweight='bold'); ax.text(i,-5.2,c,ha='center',va='top',fontsize=13,color=MID)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-7,21); clean(ax)
finish(fig,O+'toheo12_fig1.png','경기 나머지는 2026년 7월 지정된 구리·동탄·기흥 제외 · 국토교통부 아파트 실거래',allow_outside=True,strict=False)
# fig2
R=[('성남 분당구',27.4),('하남시',21.0),('성남 중원구',20.9),('광명시',20.5),('성남 수정구',20.1),('용인 수지구',18.7),('안양 동안구',18.0),('수원 영통구',9.0),('과천시',8.0),('의왕시',7.3),('수원 팔달구',7.0),('수원 장안구',6.6)]
fig=plt.figure(figsize=(11.2,9.6)); ax=fig.add_axes([0.22,0.08,0.72,0.74])
head(fig,'경기 토지거래허가구역 12곳 · 같은 단지·같은 면적 · 지정 전 → 지정 뒤 1년','분당 27.4%부터 수원 장안 6.6%까지, 같은 규제인데 네 배 차이')
n=len(R)
for i,(nm,v) in enumerate(R):
    y=n-1-i; c=NAVY if v>=20 else (MID if v>=15 else GREY)
    ax.barh(y,v,0.62,color=c); ax.text(v+0.4,y,f'+{v:.1f}%',va='center',fontsize=15.5,color=NAVY,fontweight='bold')
    ax.text(-0.5,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(0.6,color=WARN,lw=2,ls='--'); ax.text(1.2,n-0.5,'경기 나머지 +0.6%',fontsize=13,color=WARN,fontweight='bold',va='center')
ax.set_xlim(0,32); ax.set_ylim(-0.6,n-0.3); clean(ax)
finish(fig,O+'toheo12_fig2.png','과천은 14쌍이라 한두 건에 흔들릴 수 있습니다 · 국토교통부 아파트 실거래',allow_outside=True,strict=False)
# fig3 monthly
M=['25.4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8']
G=[3277,4503,6725,2344,2708,5687,5023,1596,3030,3308,3399,3272,4794,4749,3500,3933,2331]
S=[5227,7578,11270,4146,4277,8665,8531,3390,4774,5373,5796,5515,8662,8987,5305,5844,3338]
R=[6918,7156,8893,5545,5185,6422,7432,8129,6932,8608,6955,9457,8967,9204,9460,9734,7966]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.07,0.14,0.86,0.64])
head(fig,'월별 아파트 매매 거래 · 2025년 4월~2026년 8월','토지거래허가구역 지정 다음 달, 경기 12곳 거래 68% 줄었습니다')
x=range(len(M))
ax.plot(x,G,color=NAVY,lw=3.2,marker='o',ms=6,label='경기 12곳'); ax.plot(x,S,color=MID,lw=2.4,marker='o',ms=5,label='서울'); ax.plot(x,R,color=GREY,lw=2.4,marker='o',ms=5,label='경기 나머지')
ax.axvline(6.5,color=WARN,lw=2,ls='--'); ax.text(6.6,11500,'10월 20일 지정',fontsize=14,color=WARN,fontweight='bold')
ax.annotate('1,596건',(7,1596),(8.2,900),fontsize=14,color=NAVY,fontweight='bold',arrowprops=dict(arrowstyle='->',color=NAVY))
for i,m in enumerate(M):
    if i%2==0: ax.text(i,-500,m+('월' if '.' not in m else '월'),ha='center',va='top',fontsize=12,color=MID)
lg=ax.legend(loc='upper right',frameon=False,fontsize=14)
ax.set_xlim(-0.5,len(M)-0.5); ax.set_ylim(-1200,12500); clean(ax)
finish(fig,O+'toheo12_fig3.png','8월은 9월 중순까지 신고분이라 더 늘 수 있습니다 · 해제 거래 제외',allow_outside=True,strict=False)
render('토지거래허가구역 해제',['토허제 12월 31일 만료','묶인 경기 12곳 1년 +17%'],'안 묶인 경기는 +0.6% · 2025년 강남 해제 39일의 교훈',O+'toheo12_thumb.png')
print('ok')
