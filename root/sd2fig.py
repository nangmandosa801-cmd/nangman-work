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

# fig1 연기 연혁
S=[('처음 계획','2021년'),('1차 연기','2024년'),('2차 연기','2025년 6월'),('3차 연기','2026년 12월'),('4차 연기\n(2026년 9월)','2027년 상반기')]
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.04,0.12,0.92,0.66])
head(fig,'인천발 KTX 개통 목표 · 발표 때마다 바뀐 날짜','인천발 KTX 개통 연기, 다섯 번째 목표는 2027년 상반기')
for i,(a,b) in enumerate(S):
    c=WARN if i==4 else (NAVY if i==0 else MID)
    ax.add_patch(plt.Rectangle((i*2.2,1.0),1.9,1.6,color=c))
    ax.text(i*2.2+0.95,2.15,b,ha='center',va='center',fontsize=18,color='white',fontweight='bold')
    ax.text(i*2.2+0.95,0.7,a,ha='center',va='top',fontsize=14.5,color=NAVY,fontweight='bold')
    if i<4: ax.annotate('',xy=(i*2.2+2.18,1.8),xytext=(i*2.2+1.92,1.8),arrowprops=dict(arrowstyle='-|>',color=GREY,lw=2.5))
ax.text(5.4,3.3,'공정률 86% · 남은 것은 시운전 (밤 3시간 반만 가능)',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(-0.2,10.9); ax.set_ylim(-0.6,3.8); clean(ax)
finish(fig,O+'sd2_fig1.png','수인분당선 열차가 다니는 선로라 열차가 끊긴 밤에만 시험할 수 있습니다',allow_outside=True,strict=False)

# fig2 동별 1년 변화
R=[('송도동\n(송도국제도시)',3.0,106),('연수동',2.6,23),('동춘동',2.1,31),('옥련동\n(KTX 송도역)',-1.2,21)]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.08,0.20,0.86,0.56])
head(fig,'인천 연수구 · 같은 단지·같은 면적 · 2025년 4~9월 → 2026년 4~9월','옥련동 아파트, 연수구에서 유일하게 1년 새 내렸습니다')
for i,(n,v,c) in enumerate(R):
    col=WARN if v<0 else NAVY
    ax.bar(i,v,0.6,color=col); ax.text(i,v+(0.15 if v>0 else -0.15),f'{v:+.1f}%',ha='center',va='bottom' if v>0 else 'top',fontsize=21,color=col,fontweight='bold')
    ax.text(i,-2.2,n,ha='center',va='top',fontsize=15.5,color=NAVY,fontweight='bold'); ax.text(i,-3.3,f'{c}쌍',ha='center',va='top',fontsize=13,color=MID)
ax.axhline(0,color=LINE,lw=1.5); ax.set_xlim(-0.6,3.6); ax.set_ylim(-4.2,4.2); clean(ax)
finish(fig,O+'sd2_fig2.png','KTX 송도역이 있는 옥련동만 값이 내렸고, 송도국제도시는 3.0% 올랐습니다',allow_outside=True,strict=False)

# fig3 연도별 84
a=pd.read_pickle('/home/claude/songdo/apt.pkl'); x=a[a.a.between(83,86)&a.dong.isin(['송도동','옥련동'])]
s=x.groupby(['dong',x.ym//100]).p.median().unstack(0)/1e4
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.08,0.14,0.78,0.64])
head(fig,'인천 연수구 아파트 84㎡ · 연도별 실거래 중간값','옥련동 84㎡, 2022년 4억 500만원에서 올해 2억 9,200만원')
for d,c,lab in [('송도동',NAVY,'송도국제도시'),('옥련동',WARN,'옥련동 (송도역)')]:
    v=s[d]; ax.plot(v.index,v.values,color=c,lw=3.2,marker='o',ms=7); ax.text(v.index[-1]+0.25,v.values[-1],f'{lab}\n{v.values[-1]:.2f}억',va='center',fontsize=15,color=c,fontweight='bold')
ax.annotate(f'2022년 {s.loc[2022,"옥련동"]:.2f}억',(2022,s.loc[2022,'옥련동']),(2023.2,s.loc[2022,'옥련동']+1.6),fontsize=14,color=WARN,fontweight='bold',arrowprops=dict(arrowstyle='->',color=WARN))
for y in [2015,2018,2021,2024,2026]: ax.text(y,-0.25,str(y),ha='center',va='top',fontsize=14,color=MID)
ax.set_xlim(2014.5,2028.6); ax.set_ylim(0,9.5); clean(ax)
finish(fig,O+'sd2_fig3.png','옥련동은 대부분 1990년대 단지 · 송도국제도시와 84㎡ 가격 차이가 2.5배입니다',allow_outside=True,strict=False)

# fig4 옥련동 단지 고점 vs 지금
R=[('럭키송도 85㎡ (1993)',4.44,2.82),('현대4 85㎡ (1997)',5.20,3.37),('우성 85㎡ (1996)',4.40,2.90),('현대2차 85㎡ (1995)',5.00,3.69),('삼성 60㎡ (1996)',3.31,2.40)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.34,0.10,0.58,0.70])
head(fig,'옥련동 아파트 · 2021~22년 고점 → 2026년 4~9월 실거래 중간값','송도역 앞 옥련동 아파트, 고점보다 26~37% 낮습니다')
n=len(R)
for i,(nm,p0,p1) in enumerate(R):
    y=n-1-i; ax.plot([p1,p0],[y,y],color=GREY,lw=6,solid_capstyle='round',zorder=1)
    ax.scatter([p0],[y],s=230,color=GREY,zorder=3); ax.scatter([p1],[y],s=260,color=WARN,zorder=3)
    ax.text(p0+0.12,y,f'{p0:.2f}억',va='center',fontsize=14,color=MID); ax.text(p1-0.12,y,f'{p1:.2f}억',va='center',ha='right',fontsize=15,color=WARN,fontweight='bold')
    ax.text(5.95,y,f'{(p1/p0-1)*100:.1f}%',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(1.5,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.scatter([],[],s=120,color=GREY,label='2021~22년 고점'); ax.scatter([],[],s=120,color=WARN,label='2026년 4~9월')
lg=ax.legend(loc='lower center',bbox_to_anchor=(0.45,1.0),ncol=2,frameon=False,fontsize=13)
ax.set_xlim(1.6,6.5); ax.set_ylim(-0.9,n-0.4); clean(ax)
finish(fig,O+'sd2_fig4.png','같은 단지·같은 면적 중간값 · 거래가 많은 옥련동 1990년대 단지입니다',allow_outside=True,strict=False)

# fig5 송도역 새 아파트 vs 구축 vs 국제도시
R=[('송도국제도시 84㎡ 중간값',7.40,NAVY),('송도역서해그랑블더파크 84㎡ (2025)',6.03,MID),('송도역 한신더휴 프레스턴 59㎡ 입주권',4.49,MID),('송도역서해그랑블 59㎡ (2024)',4.38,MID),('송도역경남아너스빌 60㎡ (2025)',4.20,MID),('옥련동 1990년대 85㎡ (럭키송도·우성)',2.86,WARN)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.42,0.10,0.50,0.70])
head(fig,'2026년 실거래 · 송도역 앞 새 아파트와 옥련동 구축, 송도국제도시','송도역 아파트, 새 단지 59㎡ 4억 중반 · 구축 85㎡ 3억 아래')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c); ax.text(v+0.1,y,f'{v:.2f}억',va='center',fontsize=15.5,color=NAVY,fontweight='bold')
    fig.text(0.41,0.10+0.70*(y+0.5)/n,nm,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
ax.set_xlim(0,8.8); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'sd2_fig5.png','같은 송도역 앞이라도 새 아파트와 1990년대 구축은 다른 가격대입니다 · 거래가 적은 단지는 몇 건의 값입니다',allow_outside=True,strict=False)

render('인천발 KTX',['인천발 KTX 또 연기','송도역 옥련동 1년 -1.2%'],'2027년 상반기로 네 번째 연기 · 송도동은 +3.0%',O+'sd2_thumb.png')
print('ok')
