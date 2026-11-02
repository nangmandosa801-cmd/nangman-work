import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd, numpy as np
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

a=pd.read_pickle('/home/claude/songdo/apt.pkl')
x=a[a.a.between(83,86)]; s=x.groupby(['zone',a.ym//100]).p.median().unstack(0)/1e4

# fig1: 연도별 84㎡ 중간값 국제도시 vs 옛 송도
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.08,0.14,0.80,0.64])
head(fig,'인천 연수구 아파트 84㎡ · 연도별 실거래 중간값','송도 집값, 국제도시는 2021년 8억 2천에서 올해 7억 3천')
yrs=list(s.index)
for z,c in [('국제도시',NAVY),('연수구 원도심',SAND)]:
    v=s[z].values; ax.plot(yrs,v,color=c,lw=3.2,marker='o',ms=7)
    ax.text(yrs[-1]+0.25,v[-1],('송도국제도시' if z=='국제도시' else '연수구 원도심')+f'\n{v[-1]:.2f}억',va='center',fontsize=15,color=c,fontweight='bold')
pk=s['국제도시'].loc[2021]; ax.annotate(f'2021년 {pk:.2f}억',(2021,pk),(2018.2,pk+0.6),fontsize=14.5,color=NAVY,fontweight='bold',arrowprops=dict(arrowstyle='->',color=NAVY))
for y in [2015,2018,2021,2024,2026]: ax.text(y,-0.25,str(y),ha='center',va='top',fontsize=14,color=MID)
ax.set_xlim(2014.5,2028.2); ax.set_ylim(0,9.6); clean(ax)
finish(fig,O+'sd1_fig1.png','송도국제도시(송도동)와 옥련·연수·동춘동 원도심 1990년대 단지는 2배 넘게 차이 납니다',allow_outside=True,strict=False)

# fig2: 86쌍 고점 대비 분포
t=pd.read_pickle('/home/claude/songdo/pairs.pkl')
k=['단지명','ar']
pkq=a[(a.ym>=202107)&(a.ym<=202206)].groupby(k).p.agg(['median','size']); nw=a[a.ym>=202604].groupby(k).p.agg(['median','size'])
j=pkq.join(nw,lsuffix='_pk',rsuffix='_nw',how='inner'); j=j[(j.size_pk>=3)&(j.size_nw>=3)].reset_index()
j=j[j['단지명'].isin(a[a.zone=='국제도시']['단지명'].unique())]; j['v']=(j.median_nw/j.median_pk-1)*100
bins=[-45,-30,-25,-20,-15,-10,-5,0,5]; lab=['-30% 아래','-30~-25%','-25~-20%','-20~-15%','-15~-10%','-10~-5%','-5~0%','고점 넘음']
cnt=pd.cut(j.v,bins).value_counts().sort_index().values
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.06,0.20,0.88,0.56])
head(fig,f'송도국제도시 · 같은 단지·같은 면적 {len(j)}쌍 · 2021년 고점 → 2026년 4~9월','2021년 고점을 넘은 쌍은 하나뿐입니다')
for i,c in enumerate(cnt):
    col=WARN if i==len(cnt)-1 else (NAVY if i>=5 else GREY)
    ax.bar(i,c,0.7,color=col); ax.text(i,c+0.4,f'{c}쌍',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i,-0.8,lab[i],ha='center',va='top',fontsize=13,color=NAVY)
ax.axvline(len(cnt)-1.5,color=WARN,lw=2,ls='--'); ax.text(len(cnt)-1.55,max(cnt)*0.95,'2021년 고점',ha='right',fontsize=14,color=WARN,fontweight='bold')
ax.set_xlim(-0.6,len(cnt)-0.4); ax.set_ylim(-4,max(cnt)+4); clean(ax)
finish(fig,O+'sd1_fig2.png',f'중간값 {j.v.median():.1f}% · 고점과 10% 안쪽 차이는 {(j.v>=-10).sum()}쌍입니다',allow_outside=True,strict=False)

# fig3: 월별 신고가 건수
m=[6,8,7,8,10,15,13,11,10]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.06,0.18,0.88,0.58])
head(fig,'송도국제도시 · 2026년 월별 · 같은 단지·같은 면적의 이전 모든 거래보다 비싼 거래','송도 아파트 신고가, 1월 6건에서 6월 15건')
for i,v in enumerate(m):
    ax.bar(i,v,0.62,color=NAVY if v>=10 else MID); ax.text(i,v+0.3,f'{v}건',ha='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(i,-0.5,f'{i+1}월',ha='center',va='top',fontsize=15,color=NAVY)
ax.set_xlim(-0.6,8.6); ax.set_ylim(-2.5,18); clean(ax)
finish(fig,O+'sd1_fig3.png','올해 신고가 88건은 송도국제도시 거래 2,483건의 3.5% · 새 아파트와 센트럴파크·바다 앞 단지에서 나왔습니다',allow_outside=True,strict=False)

# fig4: 84㎡ 대장 순위 위·아래
R=[('송도더샵파크애비뉴','2018',13.2),('송도더샵퍼스트파크F15BL','2017',12.0),('힐스테이트송도더스카이','2024',11.95),('송도더샵퍼스트파크F14BL','2017',11.0),('송도더샵퍼스트파크F13-1BL','2017',10.55),
   ('송도캐슬&해모로','2013',5.99),('송도풍림아이원2단지','2005',5.8),('송도풍림아이원1단지','2005',5.755),('송도금호어울림','2005',5.74),('송도풍림아이원3단지','2005',5.55)]
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.40,0.08,0.50,0.74])
head(fig,'송도국제도시 84㎡ · 2026년 4~9월 실거래 중간값','송도 대장 아파트 순위, 13억 2천과 5억 5,500만원은 2.4배')
n=len(R)
for i,(nm,by,v) in enumerate(R):
    y=n-1-i+(0 if i<5 else -0.6); c=NAVY if i<5 else GREY
    ax.barh(y,v,0.62,color=c); ax.text(v+0.15,y,f'{v:.2f}억',va='center',fontsize=15.5,color=NAVY,fontweight='bold')
    fig.text(0.39,0.08+0.74*(y+1.1)/(n+0.6),f'{nm} ({by})',ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_xlim(0,15.5); ax.set_ylim(-1.1,n-0.5); clean(ax)
finish(fig,O+'sd1_fig4.png','비싼 쪽은 센트럴파크·바다를 바로 보는 고층 단지 · 싼 쪽은 2005년 입주한 초기 단지',allow_outside=True,strict=False)

# fig5: 전세가율
R=[('송도더샵파크애비뉴',5.07,13.2),('힐스테이트송도더스카이',4.72,11.95),('송도더샵퍼스트파크F15BL',4.8,12.0),('송도SKVIEW',3.9,7.2),('송도풍림아이원2단지',3.725,5.8)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.36,0.10,0.56,0.70])
head(fig,'송도국제도시 84㎡ · 2026년 4~9월 · 전세 중간값과 매매 중간값','송도 전세 아파트, 대장 단지일수록 전세가율이 낮습니다')
n=len(R)
for i,(nm,js,mm) in enumerate(R):
    y=n-1-i; ax.barh(y,mm,0.6,color=GREY); ax.barh(y,js,0.6,color=NAVY)
    ax.text(js/2,y,f'전세 {js:.1f}억',ha='center',va='center',fontsize=13,color='white',fontweight='bold')
    ax.text(mm+0.2,y,f'매매 {mm:.1f}억 · {js/mm*100:.0f}%',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
    fig.text(0.35,0.10+0.70*(y+0.5)/n,nm,ha='right',va='center',fontsize=14,color=NAVY,fontweight='bold')
ax.set_xlim(0,17.5); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'sd1_fig5.png','송도국제도시 84㎡ 전체는 전세 4억 · 매매 7억 4천 · 전세가율 54.1%',allow_outside=True,strict=False)

render('송도 아파트 시세',['송도 신고가 쏟아지는데','고점 넘은 곳은 80쌍 중 1쌍'],'2021년 고점 대비 -14.4% · 송도동 실거래 3만 건',O+'sd1_thumb.png')
print('ok')
