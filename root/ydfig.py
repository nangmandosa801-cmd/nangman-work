import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_yeouido_'

render('낭만 부동산 분석 플랫폼 · 여의도 재건축',
       ['여의도 재건축, 1971년 시범이','2005년보다 평당 30% 비쌉니다'],
       '전용 90~120㎡ 57건을 전용 평당가로 놓았습니다', O+'thumb.png')

# fig1 : U자
fig=plt.figure(figsize=(11.2,7.4)); ax=fig.add_axes([0.07,0.14,0.88,0.66])
fig.text(0.04,0.955,'여의도동 전용 평당가 · 전용 90~120㎡ 2026년 1~8월 57건',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'새 아파트 다음으로 비싼 건 50년 된 아파트입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
X=['1970~80년대\n재건축 대기','2000년대\n주상복합','2023년\n브라이튼여의도']
V=[1.01,0.77,1.40]; N=['45건 · 7개 단지','10건 · 4개 단지','2건 · 1개 단지']
M=['30.50억','26.00억','48.23억']
C=[WARN,MID,NAVY]
for i,(v,c) in enumerate(zip(V,C)):
    ax.bar(i,v,0.5,color=c)
    ax.text(i,v-0.07,'%.2f억'%v,ha='center',va='top',fontsize=24,fontweight='bold',color='white')
    ax.text(i,v+0.055,'중간가 '+M[i],ha='center',fontsize=15,color=c,fontweight='bold')
    ax.text(i,-0.075,X[i],ha='center',va='top',fontsize=16,color=NAVY,fontweight='bold',linespacing=1.5)
    ax.text(i,-0.40,N[i],ha='center',va='top',fontsize=13.5,color=SAND)
ax.plot([0,1,2],[1.01,0.77,1.40],color=SAND,lw=2.2,ls='--',zorder=0)
ax.set_ylim(-0.62,1.62); ax.set_xlim(-0.6,2.6); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.50,0.855,'전용 평당가 (거래금액 ÷ 전용 평수)',fontsize=14.5,color=SAND,ha='center')
finish(fig,O+'fig1.png','거래가 적은 단지는 층·조망 차이가 중간값에 크게 반영될 수 있습니다 · 2023년 신축은 2건 기준',allow_outside=True,strict=False)

# fig2 : 9호선 급행역 84㎡
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.16,0.10,0.80,0.70])
fig.text(0.04,0.955,'9호선 급행역 전용 84㎡ · 가장 오래된 단지와 가장 새 단지',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'면적을 맞추면 전부 신축이 앞섭니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
G=[('마곡나루',9.40,17.35,'1991년','2021년'),('가양',12.05,16.00,'1990년','2013년'),
   ('염창',11.50,17.20,'1990년','2019년'),('당산',13.45,19.00,'1986년','2017년'),
   ('노량진',14.80,17.85,'1997년','2026년'),('동작 · 흑석',15.10,23.70,'2003년','2025년'),
   ('봉은사 · 삼성',26.25,41.10,'1992년','2018년'),('고속터미널 · 반포',20.10,58.75,'1994년','2023년')]
n=len(G); h=0.34
for i,(g,o,nw,yo,yn) in enumerate(G):
    y=n-1-i
    ax.barh(y+h/1.8,o,h,color=SAND)
    ax.barh(y-h/1.8,nw,h,color=MID)
    ax.text(o+0.8,y+h/1.8,'%.2f억  %s'%(o,yo),ha='left',va='center',fontsize=13,color=SAND,fontweight='bold')
    ax.text(nw+0.8,y-h/1.8,'%.2f억  %s'%(nw,yn),ha='left',va='center',fontsize=13,color=MID,fontweight='bold')
    ax.text(-1.2,y,g,ha='right',va='center',fontsize=15,fontweight='bold',color=NAVY)
ax.set_xlim(0,76); ax.set_ylim(-0.8,n-0.2); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.52,0.845,'■ 가장 오래된 단지',fontsize=15,color=SAND,fontweight='bold')
fig.text(0.72,0.845,'■ 가장 새 단지',fontsize=15,color=MID,fontweight='bold')
finish(fig,O+'fig2.png','전용 83~86㎡ · 단지당 3건 이상 · 2026년 1~8월 중간값 · 여의도는 84㎡ 거래가 2건뿐이라 제외',allow_outside=True,strict=False)
print('ok')
