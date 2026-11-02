import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gmredev_'

render('낭만 부동산 분석 플랫폼 · 광명 재개발',
       ['광명 재개발, 다 지은 뉴타운보다','1986년 철산주공이 더 비쌉니다'],
       '3년 된 신축 13.15억, 40년 된 구축 13.95억', O+'thumb.png')

# fig1 : 뉴타운 입주 완료 3단지 연도별
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.07,0.15,0.72,0.64])
fig.text(0.04,0.955,'광명뉴타운 입주 완료 단지 전용 84㎡ · 연도별 중간값',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'세 단지 모두 2026년에 1억 5천 이상 올랐습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
X=['2023년','2025년','2026년']
S=[('광명푸르지오포레나 · 14R',[None,11.45,13.15],NAVY),
   ('광명푸르지오센트베르 · 15R',[10.50,10.70,12.20],MID),
   ('광명아크포레자이위브 · 16R',[9.14,9.65,11.30],WARN)]
for nm,v,c in S:
    xs=[i for i,y in enumerate(v) if y]; ys=[y for y in v if y]
    ax.plot(xs,ys,marker='o',ms=13,lw=3.4,color=c)
    for x,y in zip(xs,ys):
        ax.text(x,y+0.30,'%.2f억'%y,ha='center',fontsize=15,fontweight='bold',color=c)
for i,x in enumerate(X): ax.text(i,8.35,x,ha='center',va='top',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(-0.35,2.45); ax.set_ylim(8.0,14.2); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
for j,(nm,v,c) in enumerate(S):
    fig.text(0.805,0.690-j*0.062,'━ '+nm.split(' · ')[0],fontsize=14,color=c,fontweight='bold')
    fig.text(0.822,0.655-j*0.062,nm.split(' · ')[1]+' 입주 '+['2023년','2022년','2021년'][j],fontsize=12.5,color=SAND)
fig.text(0.805,0.470,'2025년 대비',fontsize=14.5,color=NAVY,fontweight='bold')
for j,t in enumerate(['포레나  +1.70억','센트베르 +1.50억','아크포레 +1.65억']):
    fig.text(0.805,0.425-j*0.042,t,fontsize=13.5,color=NAVY)
finish(fig,O+'fig1.png','국토교통부 실거래가 · 전용 83~86㎡ · 단지당 3건 이상 · 해제 거래 제외 · 2026년은 8월 계약까지',allow_outside=True,strict=False)

# fig2 : 광명시 84㎡ 상단 비교
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.30,0.09,0.66,0.71])
fig.text(0.04,0.955,'광명시 전용 84㎡ · 2026년 거래 3건 이상 단지',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'40년 된 철산주공이 3년 된 뉴타운 신축보다 위입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
G=[('철산역롯데캐슬&SKVIEW','철산 · 2022년',16.62,MID),
   ('철산센트럴푸르지오','철산 · 2021년',15.20,MID),
   ('철산주공13','철산 · 1986년',13.95,WARN),
   ('철산래미안자이','철산 · 2009년',13.50,SAND),
   ('철산주공12','철산 · 1986년',13.30,WARN),
   ('광명푸르지오포레나','광명뉴타운 14R · 2023년',13.15,NAVY),
   ('광명푸르지오센트베르','광명뉴타운 15R · 2022년',12.20,NAVY),
   ('광명아크포레자이위브','광명뉴타운 16R · 2021년',11.30,NAVY),
   ('광명해모로이연','광명동 · 2015년',9.50,SAND),
   ('중앙하이츠2','광명동 · 1993년',4.90,SAND)]
n=len(G)
for i,(a,sub,v,c) in enumerate(G):
    y=n-1-i
    ax.barh(y,v,0.60,color=c)
    ax.text(v-0.28,y,'%.2f억'%v,ha='right',va='center',fontsize=16,fontweight='bold',color='white')
    ax.text(-0.35,y+0.13,a,ha='right',va='center',fontsize=14.5,fontweight='bold',color=NAVY)
    ax.text(-0.35,y-0.22,sub,ha='right',va='center',fontsize=11.5,color=SAND)
ax.set_xlim(0,18.6); ax.set_ylim(-0.7,n-0.3); ax.set_xticks([]); ax.set_yticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
fig.text(0.30,0.838,'■ 철산 재건축 대기',fontsize=13.5,color=WARN,fontweight='bold')
fig.text(0.475,0.838,'■ 광명뉴타운 신축',fontsize=13.5,color=NAVY,fontweight='bold')
fig.text(0.645,0.838,'■ 철산 신축',fontsize=13.5,color=MID,fontweight='bold')
fig.text(0.775,0.838,'■ 그 밖',fontsize=13.5,color=SAND,fontweight='bold')
finish(fig,O+'fig2.png','전용 83~86㎡ · 단지당 3건 이상 · 2026년 1~8월 중간값 · 해제 거래 제외',allow_outside=True,strict=False)
print('ok')
