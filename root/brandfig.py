import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render_interior
O='/mnt/user-data/outputs/int/nangman_interior_'
GREY='#C9C3B6'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1 가격대 range
R=[('온라인 직판',50,70),('일반 시공업체',60,90),('중견 브랜드',100,150),('대기업 브랜드',150,250)]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.26,0.14,0.68,0.64])
head(fig,'3연동 중문 · 제품+시공 · 업체 급별 가격대','3연동 중문 가격, 50만원대부터 250만원 이상까지')
n=len(R)
for i,(nm,a,b) in enumerate(R):
    y=n-1-i; c=NAVY if i>=2 else MID
    ax.plot([a,b],[y,y],color=c,lw=26,solid_capstyle='butt')
    ax.text(a-3,y,f'{a}만',ha='right',va='center',fontsize=16,color=MID,fontweight='bold'); ax.text(b+3,y,f'{b}만'+(' 이상' if i==3 else ''),ha='left',va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(10,y,nm,ha='right',va='center',fontsize=17,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(10,300); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'brand_fig1.png','견적 1,000건 이상을 모은 견적 플랫폼 집계 · 차이는 프레임·유리·부품·보증에서 납니다',brand='낭만 인테리어',allow_outside=True,strict=False)
# fig2 현장 브랜드 945건
R=[('공장 제작 (사제)',98),('영림',65),('예림',34),('LX하우시스',12),('대림',8),('한샘',1)]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.24,0.12,0.68,0.66])
head(fig,'남양주·구리 일대 중문 업체 20곳 · 시공 글 945건에서 센 브랜드','중문 브랜드, 현관에 가장 많이 달린 건 공장 제작과 영림')
n=len(R)
for i,(nm,v) in enumerate(R):
    y=n-1-i; c=NAVY if i<2 else (MID if i<4 else GREY)
    ax.barh(y,v,0.62,color=c); ax.text(v+1.5,y,f'{v}건',va='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(-2,y,nm,ha='right',va='center',fontsize=17,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,115); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'brand_fig2.png','브랜드를 밝히지 않은 글이 많아 합이 945건이 되지 않습니다 · 검색은 한샘이 앞이지만 현장은 1건',brand='낭만 인테리어',allow_outside=True,strict=False)
render_interior('낭만 인테리어 · 중문 고르기',['중문 브랜드 순위','브랜드보다 유리와 시공점'],'3연동 50만원대~250만원 · 보증은 누가 다느냐','영림 · 한샘 · LX지인 · 이건라움 · 예림',O+'brand_thumb.png')
print('ok')
