import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_sanghwan_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['원리금균등상환 계산,','몇 회차인지 봅니다'],'원금균등 · 원리금균등 · 10년 기출 일곱 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,6.6))
head(fig,'원리금균등상환 계산 · 두 방식이 매년 내는 돈','4억원, 연 6%, 20년 · 원금균등은 점점 줄고 원리금균등은 같습니다')
yr=np.arange(1,21); L=4e4; r=0.06
bal=L-2000*(yr-1); i1=bal*r; p1=np.full(20,2000)
pay=3480; b=L; p2=[];i2=[]
for k in range(20): ii=b*r; pp=pay-ii; i2.append(ii); p2.append(pp); b-=pp
for j,(p,i,t) in enumerate([(p1,i1,'원금균등'),(np.array(p2),np.array(i2),'원리금균등')]):
    ax=fig.add_axes([0.07+j*0.48,0.2,0.42,0.55])
    ax.bar(yr,p,color=NAVY,width=0.75); ax.bar(yr,i,bottom=p,color=WARN,width=0.75)
    ax.set_title(t,fontsize=16,color=NAVY,fontweight='bold',loc='left')
    ax.set_ylim(0,4800); ax.set_xticks([1,5,10,15,20]); ax.set_xticklabels(['1년','5년','10년','15년','20년'],fontsize=11,color=TXT)
    ax.set_yticks([0,2000,4000]); ax.set_yticklabels(['0','2,000만','4,000만'],fontsize=11,color=TXT)
    for s in ['top','right']: ax.spines[s].set_visible(False)
    ax.text(20.5,p[-1]/2,'원금',fontsize=12,color=NAVY,va='center',fontweight='bold'); ax.text(20.5,p[-1]+i[-1]+250,'이자',fontsize=12,color=WARN,va='center',fontweight='bold')
finish(fig,O+'fig1.png','이자는 두 방식 모두 직전 잔금 × 금리 · 원리금균등은 저당상수 0.087로 계산',allow_outside=True,strict=False)
# fig2 회차 함정
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.6); ax.axis('off')
head(fig,'원리금균등상환 계산 · 제36회 32번 회차 함정','10회차 이자는 9번 갚고 남은 잔금에 금리를 곱합니다')
for k in range(11):
    x=0.6+k*0.95
    c=NAVY if k<9 else (WARN if k==9 else GREY)
    ax.add_patch(mp.FancyBboxPatch((x,2.3),0.8,0.8,boxstyle='round,pad=0.01,rounding_size=0.08',fc=c,ec='none'))
    ax.text(x+0.4,2.7,f'{k+1}',ha='center',va='center',fontsize=14,color='white',fontweight='bold')
ax.text(0.6,3.45,'원금 3,000만원씩 9번 갚음',fontsize=14,color=NAVY,fontweight='bold')
ax.text(9.15,3.45,'10회차',fontsize=14,color=WARN,fontweight='bold')
ax.text(0.6,1.6,'맞게: 잔금 9억 − 3,000만 × 9 = 6.3억 → 이자 6.3억 × 3% = 1,890만원 (③)',fontsize=14,color=OK,fontweight='bold')
ax.text(0.6,0.85,'틀리게: 10번 갚은 잔금 6억 × 3% = 1,800만원 (②)',fontsize=14,color=WARN)
finish(fig,O+'fig2.png','금리 3%는 1회차 이자 2,700만원 ÷ 9억으로 거꾸로 구합니다',allow_outside=True,strict=False)
# fig3 금리 거꾸로
fig=plt.figure(figsize=(11.2,5.6)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.4); ax.axis('off')
head(fig,'원리금균등상환 계산 · 제32회 27번 금리 거꾸로 구하기','1회차 원리금에서 원금을 빼면 이자, 이자를 대출금으로 나누면 금리')
ax.add_patch(mp.Rectangle((0.6,2.2),4.0,0.9,fc=NAVY)); ax.add_patch(mp.Rectangle((4.6,2.2),4.8,0.9,fc=WARN))
ax.text(2.6,2.65,'원금 2,000만',ha='center',va='center',fontsize=15,color='white',fontweight='bold')
ax.text(7.0,2.65,'이자 2,400만',ha='center',va='center',fontsize=15,color='white',fontweight='bold')
ax.annotate('',xy=(9.4,3.35),xytext=(0.6,3.35),arrowprops=dict(arrowstyle='<->',color=SAND,lw=2))
ax.text(5.0,3.55,'1회차 원리금 4,400만원',ha='center',fontsize=14,color=TXT)
ax.text(0.6,1.4,'원금 = 6억 ÷ 30년 = 2,000만원',fontsize=14.5,color=NAVY)
ax.text(0.6,0.8,'금리 = 2,400만 ÷ 6억 = 4%',fontsize=16,color=WARN,fontweight='bold')
finish(fig,O+'fig3.png','3회차 원리금 = 2,000만 + 5.6억 × 4% = 4,240만원 (①)',allow_outside=True,strict=False)
# fig4 잔금
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0.1,0.2,0.84,0.56])
head(fig,'원리금균등상환 계산 · 제33회 29번 대출 잔금','5년을 갚아도 1억 중 9,237만원이 남습니다')
m=np.arange(0,361); rm=0.05/12; pay=54
B=[1e4]; 
for k in range(360): B.append(B[-1]*(1+rm)-pay)
B=np.array(B[:361]); B[B<0]=0
ax.plot(m/12,B,color=NAVY,lw=3)
ax.scatter([5],[9237],color=WARN,s=90,zorder=3); ax.text(5.6,9500,'5년 뒤 9,237만원',fontsize=14,color=WARN,fontweight='bold')
ax.set_xlim(0,30); ax.set_ylim(0,10800); ax.set_xticks([0,5,10,15,20,25,30]); ax.set_xticklabels(['0','5년','10년','15년','20년','25년','30년'],fontsize=11,color=TXT)
ax.set_yticks([0,5000,10000]); ax.set_yticklabels(['0','5,000만','1억'],fontsize=11,color=TXT)
for s in ['top','right']: ax.spines[s].set_visible(False)
finish(fig,O+'fig4.png','잔금 = 월 원리금 54만 × 남은 25년 연금현가계수 171.06',allow_outside=True,strict=False)
