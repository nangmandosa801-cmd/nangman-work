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

# fig1 6법 문항 배분
R=[('국토계획법',12,'신규택지 · 개발행위허가 · 지구단위계획'),('건축법',7,'건폐율·용적률 · 대지 분할 60㎡'),('주택법',7,'10·15 대책 규제지역 · 분양가상한제'),('도시개발법',6,'광주 탄벌지구 환지'),('도시정비법',6,'수택2구역 · 은마 조합원 지위'),('농지법',2,'농지취득자격증명')]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.19,0.10,0.78,0.72])
head(fig,'공인중개사 2차 부동산공법 40문항 · 최근 회차 기준 (회차마다 1~2문항 다를 수 있음)','부동산공법 문항 배분, 국토계획법 12문항이 공법의 30%입니다')
n=len(R)
for i,(nm,c,memo) in enumerate(R):
    y=n-1-i; col=NAVY if i==0 else (MID if c>=6 else GREY)
    ax.barh(y,c,0.62,color=col)
    ax.text(c+0.2,y+0.12,f'{c}문항',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(c+0.2,y-0.22,memo,va='center',fontsize=12.5,color=MID)
    ax.text(-0.3,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,19); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'gongbeop37_fig1.png','올해 뉴스로 보는 법별 주제 · 토지거래허가구역은 중개실무, 분당 선도지구는 노후계획도시특별법이라 공법 밖입니다',allow_outside=True,strict=False)

# fig2 36회 난이도 분포 & 55점 전략
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.06,0.14,0.90,0.62])
head(fig,'36회(2025년) 공법 EBS 총평 · 상급 18문항 · 중급 이하 22문항','공법 55점 전략, 중급 이하 22문항에서 20개를 맞히면 50점입니다')
ax.barh(1,22,0.55,color=NAVY); ax.barh(1,18,0.55,left=22,color='#7E97B8')
ax.text(11,1,'중급 이하 22문항',ha='center',va='center',fontsize=16,color='white',fontweight='bold')
ax.text(31,1,'상급·극상 18문항',ha='center',va='center',fontsize=16,color='white',fontweight='bold')
ax.barh(0,20,0.55,color=NAVY); ax.barh(0,4,0.55,left=20,color=WARN)
ax.text(10,0,'20개 맞힘 = 50점',ha='center',va='center',fontsize=16,color='white',fontweight='bold')
ax.text(22,0,'+4',ha='center',va='center',fontsize=14,color='white',fontweight='bold')
ax.text(24.8,0,'찍어서 4개 더 맞히면 60점',ha='left',va='center',fontsize=16,color=WARN,fontweight='bold')
ax.text(-0.5,1,'36회 출제',ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.text(-0.5,0,'목표 점수',ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.text(20,-0.55,'과락 기준 40점 = 16문항 · 평균 60점이면 다른 과목 부담이 줄어듭니다',ha='center',va='top',fontsize=13.5,color=MID)
ax.set_xlim(-8,42); ax.set_ylim(-1.0,1.6); clean(ax)
finish(fig,O+'gongbeop37_fig2.png','베리타스알파 2025년 11월 EBS 총평 인용 · 36회 응시 165,112명 · 최종 합격률 32.14%',allow_outside=True,strict=False)

# fig3 시험 당일 시간표
fig=plt.figure(figsize=(11.2,6.8)); ax=fig.add_axes([0.05,0.12,0.90,0.62])
head(fig,'제37회 공인중개사 자격시험 · 2026년 10월 31일(토) · 합격자 발표 12월 2일(수)','공인중개사 시험 시간표, 공법은 2차 1교시 13시에 중개실무와 함께 100분입니다')
T=[(9.5,11.17,'1차 09:30~11:10','학개론 · 민법',MID),(13,14.67,'2차 1교시 13:00~14:40','중개실무 · 부동산공법',NAVY),(15.5,16.33,'2교시 15:30~16:20','공시법 · 세법',MID)]
for s,e,a,b,c in T:
    ax.barh(0,e-s,0.5,left=s,color=c)
    ax.text((s+e)/2,0.42,a,ha='center',va='bottom',fontsize=14,color=NAVY,fontweight='bold')
    ax.text((s+e)/2,0,b,ha='center',va='center',fontsize=13.5,color='white',fontweight='bold')
ax.annotate('공법 40문항',xy=(13.83,-0.27),xytext=(13.83,-0.75),ha='center',fontsize=16,color=WARN,fontweight='bold',arrowprops=dict(arrowstyle='-|>',color=WARN,lw=2))
for h in [9,10,11,12,13,14,15,16,17]: ax.text(h,-1.05,f'{h}시',ha='center',va='top',fontsize=12.5,color=MID)
ax.set_xlim(8.7,17.3); ax.set_ylim(-1.4,0.9); clean(ax)
finish(fig,O+'gongbeop37_fig3.png','한국산업인력공단 제37회 시행 공고 · 합격 기준 과목당 40점 이상 · 평균 60점 이상',allow_outside=True,strict=False)

render('공인중개사 공법',['37회 시험 10월 31일','올해 뉴스로 여섯 법 복습'],'국토계획법 12문항 · 36회 상급 18문항 · 55점 전략',O+'gongbeop37_thumb.png')
print('ok')
