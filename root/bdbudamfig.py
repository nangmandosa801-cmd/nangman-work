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

# fig1 양지마을 분담금 (400%)
R=[('31평 → 24평',-2.87),('31평 → 34평',2.06),('31평 → 44평',6.97),('48평 → 24평',-7.45),('48평 → 34평',-2.52),('48평 → 44평',2.38),('48평 → 54평',7.01)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.20,0.10,0.76,0.72])
head(fig,'양지마을 추정 분담금 · 용적률 400% 안 · 일반분양 평당 5,800만원 · 공사비 900만원 가정','분당 재건축 분담금, 양지마을 31평이 34평 가면 2억 600만원입니다')
n=len(R)
for i,(nm,v) in enumerate(R):
    y=n-1-i; c=WARN if v>0 else NAVY
    ax.barh(y,v,0.6,color=c)
    lab=(f'{v:.2f}억 부담' if v>0 else f'{-v:.2f}억 환급')
    if v>0: ax.text(v+0.15,y,lab,ha='left',va='center',fontsize=14,color=c,fontweight='bold')
    else: ax.text(v/2,y,lab,ha='center',va='center',fontsize=13.5,color='white',fontweight='bold')
    ax.text(-8.0,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(0,color=LINE,lw=1.5)
ax.set_xlim(-8.0,10.5); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'bdbudam_fig1.png','위클리한국주택경제신문 2025년 양지마을 추정치 · 용적률 350% 안은 34평 기준 4,100만원 더 부담 · 확정 금액 아님',allow_outside=True,strict=False)

# fig2 2차 5곳 늘어나는 비율
R=[('푸른마을 신성·쌍용·벽산',2598,4964),('한솔 1·2·3단지',1872,3447),('시범 삼성한신·한양',4200,7107),('파크타운 4개 단지',3028,4755),('이매촌 삼성·삼환',1734,2700)]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.25,0.10,0.72,0.72])
head(fig,'분당 2차 특별정비구역 5곳 · 기존 가구 → 계획 가구 (각 구역 제안서 기준)','늘어나는 가구 비율, 푸른마을 91%와 이매촌 56%는 분담금이 달라집니다')
n=len(R)
for i,(nm,a,b) in enumerate(R):
    y=n-1-i; r=(b/a-1)*100
    ax.barh(y,a,0.6,color='#9AA7B8'); ax.barh(y,b-a,0.6,left=a,color=NAVY if r>=80 else MID)
    ax.text(a/2,y,f'{a:,}',ha='center',va='center',fontsize=13,color='white',fontweight='bold')
    ax.text(b+80,y,f'→ {b:,}가구 · +{r:.0f}%',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
    ax.text(-120,y,nm,ha='right',va='center',fontsize=14.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,10200); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'bdbudam_fig2.png','회색은 기존 가구, 진한 색은 늘어나는 가구 · 늘어나는 가구가 많을수록 일반분양 몫이 커져 분담금이 줄어드는 구조',allow_outside=True,strict=False)

# fig3 가격 변동 1차/2차/나머지
G=['1차 선도지구 4곳','2차 선정 5곳','나머지 분당']; A=[43.5,39.0,37.6]; Bv=[21.9,26.9,28.0]
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.06,0.14,0.90,0.62])
head(fig,'같은 단지·같은 전용면적 중앙값 비교 · 국토교통부 실거래가 (해제 거래 제외)','분당 선도지구 집값, 선정 뒤 1차 +43.5%인데 나머지도 +37.6%입니다')
import numpy as np
x=np.arange(3); w=0.34
ax.bar(x-w/2,A,w,color=NAVY); ax.bar(x+w/2,Bv,w,color='#7E97B8')
for i in range(3):
    ax.text(x[i]-w/2,A[i]+1,f'+{A[i]}%',ha='center',va='bottom',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(x[i]+w/2,Bv[i]+1,f'+{Bv[i]}%',ha='center',va='bottom',fontsize=15,color='#5F7FA6',fontweight='bold')
    ax.text(x[i],-2.5,G[i],ha='center',va='top',fontsize=15,color=NAVY,fontweight='bold')
ax.bar([0],[0],color=NAVY,label='선정 전(2024.5~10) → 2026.3~8'); ax.bar([0],[0],color='#7E97B8',label='최근 1년(2025.3~8 → 2026.3~8)')
ax.legend(loc='upper right',fontsize=13,frameon=False)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-9,55); clean(ax)
finish(fig,O+'bdbudam_fig3.png','1차 64쌍 · 2차 62쌍 · 나머지 422쌍 · 2026년 8월은 신고 진행 중',allow_outside=True,strict=False)

render('분당 재건축 분담금',['양지마을 31평→34평 2억','시범 한양 33평→35평은 환급'],'2차 5곳 12월 지정 · 늘어나는 가구 비율이 분담금을 정합니다',O+'bdbudam_thumb.png')
print('ok')
