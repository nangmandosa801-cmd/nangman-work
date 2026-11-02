import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE, IVORY, PALE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_seoul5_'

render('낭만 부동산 분석 플랫폼 · 서울 5억대 아파트',
       ['서울 5억대 아파트,','금천 85㎡ 송파 32㎡'],
       '2026년 서울 매매 3,974건이 어디에 있는지 봤습니다', O+'thumb.png')

# fig1 : 금액대별 비중
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.07,0.17,0.70,0.60])
fig.text(0.04,0.955,'서울 아파트 매매 금액대별 비중 · 2021~2026년',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'5억대는 2025년 6.5%까지 줄었다가 2026년 8.1%입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
Y=['2021년','2023년','2024년','2025년','2026년\n1~8월']
lo=[18.0,15.7,12.7,10.7,13.5]; bd=[8.7,9.1,7.2,6.5,8.1]; hi=[73.3,75.2,80.1,82.7,78.4]
for i in range(5):
    ax.bar(i,lo[i],0.6,color='#8FA8C4')
    ax.bar(i,bd[i],0.6,bottom=lo[i],color=WARN)
    ax.bar(i,hi[i],0.6,bottom=lo[i]+bd[i],color=MID)
    ax.text(i,lo[i]/2,'%.1f%%'%lo[i],ha='center',va='center',fontsize=15,color='white',fontweight='bold')
    ax.text(i,lo[i]+bd[i]/2,'%.1f%%'%bd[i],ha='center',va='center',fontsize=15,color='white',fontweight='bold')
    ax.text(i,lo[i]+bd[i]+hi[i]/2,'%.1f%%'%hi[i],ha='center',va='center',fontsize=15,color='white',fontweight='bold')
    ax.text(i,-4,Y[i],ha='center',va='top',fontsize=15,color=NAVY,fontweight='bold')
ax.set_ylim(-14,104); ax.set_xlim(-0.6,4.6); ax.set_xticks([]); ax.set_yticks([])
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
fig.text(0.795,0.700,'■ 6억 이상',fontsize=16,color=MID,fontweight='bold')
fig.text(0.795,0.645,'■ 5억대',fontsize=16,color=WARN,fontweight='bold')
fig.text(0.795,0.590,'■ 5억 미만',fontsize=16,color='#8FA8C4',fontweight='bold')
fig.text(0.795,0.490,'중간값',fontsize=15,color=SAND,fontweight='bold')
for j,(t,v) in enumerate(zip(Y,['8.45억','8.70억','9.60억','10.45억','9.24억'])):
    fig.text(0.795,0.440-j*0.045,'%s  %s'%(t.replace('\n1~8월',''),v),fontsize=14,color=NAVY)
finish(fig,O+'fig1.png','국토교통부 실거래가 · 해제 거래 제외 · 2025년은 연간, 2026년은 1~8월 누적이라 표본 구성이 다릅니다',allow_outside=True,strict=False)

# fig2 : 구별 5억 5천으로 사는 전용면적
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.20,0.07,0.72,0.74])
fig.text(0.04,0.955,'같은 5억 5,000만원으로 사는 전용면적 · 구별 5억대 거래 중간값',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'금천 84.8㎡와 송파 31.9㎡, 2.7배 차이입니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
G=[('금천구',84.8,'5.50억 · 2002년',182),('도봉구',84.4,'5.50억 · 1993년',441),('양천구',68.3,'5.50억 · 2003년',112),
   ('강북구',63.8,'5.50억 · 1998년',143),('구로구',59.7,'5.51억 · 1998년',441),('노원구',54.6,'5.50억 · 1990년',1115),
   ('영등포구',53.4,'5.74억 · 1998년',72),('서초구',45.3,'5.40억 · 2003년',36),('마포구',38.9,'5.70억 · 2004년',39),
   ('송파구',31.9,'5.58억 · 2016년',18)]
n=len(G)
for i,(g,a,note,cnt) in enumerate(G):
    y=n-1-i
    c=WARN if g in('금천구','송파구') else (NAVY if g=='노원구' else MID)
    ax.barh(y,a,0.62,color=c)
    ax.text(a-1.5,y,'%.1f㎡'%a,ha='right',va='center',fontsize=17,fontweight='bold',color='white')
    ax.text(a+1.8,y,note,ha='left',va='center',fontsize=14,color=SAND)
    ax.text(-2.0,y,g,ha='right',va='center',fontsize=17,fontweight='bold',color=NAVY)
    ax.text(-2.0,y-0.33,'%s건'%format(cnt,','),ha='right',va='center',fontsize=12.5,color=SAND)
ax.set_xlim(0,108); ax.set_ylim(-0.7,n-0.3); ax.set_xticks([]); ax.set_yticks([])
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
finish(fig,O+'fig2.png','2026년 1~8월 서울 5억대(5억 이상 6억 미만) 거래의 구별 전용면적 중간값 · 10건 이상 구만',allow_outside=True,strict=False)

# fig3 : 5억대가 몰린 구 / 없는 구
fig=plt.figure(figsize=(11.2,7.6)); ax=fig.add_axes([0.06,0.13,0.88,0.64])
fig.text(0.04,0.955,'서울 5억대 거래 3,974건이 어느 구에 있나',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'노원·도봉·구로 세 구에 절반이 몰려 있습니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
A=[('노원구',1115),('도봉구',441),('구로구',441),('중랑구',316),('강서구',216),('은평구',202),('금천구',182),('강북구',143)]
B=[('성동구',0),('용산구',6),('강남구',9),('중구',9),('동작구',14),('송파구',18)]
for i,(g,v) in enumerate(A):
    ax.bar(i,v,0.62,color=NAVY if i==0 else MID)
    ax.text(i,v+30,format(v,','),ha='center',fontsize=15,fontweight='bold',color=NAVY if i==0 else MID)
    ax.text(i,-55,g,ha='center',va='top',fontsize=14.5,color=NAVY,fontweight='bold')
for j,(g,v) in enumerate(B):
    i=len(A)+0.7+j
    ax.bar(i,max(v,6),0.62,color=WARN)
    ax.text(i,max(v,6)+30,str(v),ha='center',fontsize=15,fontweight='bold',color=WARN)
    ax.text(i,-55,g,ha='center',va='top',fontsize=14.5,color=WARN,fontweight='bold')
ax.axvline(len(A)-0.15,color=LINE,lw=2,ymin=0.02,ymax=0.92)
ax.text(3.5,1230,'5억대가 몰린 구',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.text(10.2,1230,'5억대가 거의 없는 구',ha='center',fontsize=16,color=WARN,fontweight='bold')
ax.set_ylim(-330,1350); ax.set_xlim(-0.7,13.6); ax.set_xticks([]); ax.set_yticks([])
ax.axhline(0,color=LINE,lw=1.5)
for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
finish(fig,O+'fig3.png','2026년 1~8월 · 성동구는 5억 미만 거래는 있으나 5억 이상 6억 미만 구간만 0건',allow_outside=True,strict=False)
print('ok')
