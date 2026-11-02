import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_rentalratio_'
TXT='#444'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 소셜믹스',['임대 아파트 비율 17%,','옆 단지보다 비쌉니다'],'센트라스 84㎡, 텐즈힐보다 1억 5,823만원 ↑',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=17,color=MID,va='center')
    fig.text(0.04,0.905,b,fontsize=23,color=NAVY,fontweight='bold',va='center')
# fig1
R=[('왕십리',[('센트라스','임대 17.1%',23.12,WARN),('텐즈힐 1·2단지','',21.53,GREY)]),
   ('고덕',[('고덕그라시움','임대 2.8%',24.06,MID),('고덕아르테온','임대 2.7%',22.51,MID),('래미안힐스테이트고덕','임대 5.8%',20.55,MID)]),
   ('개포',[('디에이치아너힐즈','임대 6.4%',35.07,MID),('래미안블레스티지','임대 5.7%',33.82,MID)])]
fig=plt.figure(figsize=(11.2,10.2)); ax=fig.add_axes([0.40,0.1,0.47,0.72])
head(fig,'임대 아파트 비율과 2026년 84㎡ 평균 거래 가격','임대 비율 높은 단지가 더 쌀까요?')
y=0; rows=[]
for g,items in R:
    ax.text(-0.02,y+0.1,g,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=18,color=SAND,fontweight='bold')
    y-=1
    for n,r,v,c in items:
        ax.barh(y,v,0.62,color=c)
        ax.text(v+0.4,y,f'{v:.2f}억',va='center',fontsize=17,color=c if c!=GREY else SAND,fontweight='bold')
        lab=n+(f'  {r}' if r else '')
        ax.text(-0.02,y,n,transform=ax.get_yaxis_transform(),ha='right',va='bottom',fontsize=16,color=NAVY,fontweight='bold' if c==WARN else 'normal')
        if r: ax.text(-0.02,y-0.05,r,transform=ax.get_yaxis_transform(),ha='right',va='top',fontsize=14,color=WARN if c==WARN else MID)
        else: ax.text(-0.02,y-0.05,'같은 왕십리뉴타운',transform=ax.get_yaxis_transform(),ha='right',va='top',fontsize=14,color=SAND)
        y-=1
    y-=0.4
ax.set_xlim(0,41); ax.set_ylim(y+0.6,0.7); ax.set_yticks([]); ax.set_xticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
finish(fig,O+'fig1.png','2026년 1~8월 전용 83~86㎡ 평균 · 해제 거래 제외 · 임대 비율은 분양 당시 자료·보도 기준',allow_outside=True,strict=False)
# fig2
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.07,0.2,0.88,0.58])
head(fig,'2021년 → 2026년 같은 단지 같은 평형 상승률','임대 비율 높은 단지도 구 평균만큼 올랐습니다')
D=[('센트라스','임대 17.1%',36.1,'성동구',36.4),('헬리오시티','임대 14.7%',34.9,'송파구',33.5),('마포래미안푸르지오','임대 17.0%',35.2,'마포구',24.9)]
w=0.36
for i,(n,r,v,g,gv) in enumerate(D):
    ax.bar(i-w/2-0.02,v,w,color=WARN); ax.bar(i+w/2+0.02,gv,w,color=GREY)
    ax.text(i-w/2-0.02,v+0.8,f'+{v}%',ha='center',fontsize=19,fontweight='bold',color=WARN)
    ax.text(i+w/2+0.02,gv+0.8,f'+{gv}%',ha='center',fontsize=19,fontweight='bold',color=SAND)
    ax.text(i,-6.6,f'{r}  vs  {g} 전체',ha='center',fontsize=15,color=TXT)
ax.set_xticks(range(3)); ax.set_xticklabels([d[0] for d in D],fontsize=19,color=NAVY,fontweight='bold')
ax.set_ylim(0,44); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
fig.text(0.62,0.84,'■ 임대 비율 높은 단지',fontsize=15,color=WARN,fontweight='bold'); fig.text(0.82,0.84,'■ 같은 구',fontsize=15,color=SAND,fontweight='bold')
finish(fig,O+'fig2.png','같은 단지 안 전용면적이 같은 거래끼리 2021년·2026년 짝지어 2026년 건수로 가중 · 해제 거래 제외',allow_outside=True,strict=False)
