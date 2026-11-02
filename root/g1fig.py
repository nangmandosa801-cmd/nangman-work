import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan1_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['자기자본수익률 계산,','가격상승분을 넣습니다'],'10년 기출 네 문제 · 제27·29·33·36회',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def canvas(h=6.4,yl=5.2):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,yl); ax.axis('off'); return fig,ax
def bx(ax,x,y,w,h,t,s,fc,fs=15):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.1',fc=fc,ec='none'))
    ax.text(x+w/2,y+h*0.64,t,ha='center',va='center',fontsize=fs,color='white',fontweight='bold')
    ax.text(x+w/2,y+h*0.28,s,ha='center',va='center',fontsize=13,color='white')
# fig1 공식
fig,ax=canvas(6.2,5.0)
head(fig,'자기자본수익률 계산 · 공식에 제36회 27번 숫자 넣기','번 돈 4,800만원을 내 돈 1.6억원으로 나눕니다')
bx(ax,0.5,2.75,2.6,1.2,'순영업소득','4,000만원',MID)
ax.text(3.35,3.35,'+',fontsize=30,color=NAVY,ha='center',va='center',fontweight='bold')
bx(ax,3.6,2.75,2.6,1.2,'가격상승분','8억 × 5% = 4,000만원',OK)
ax.text(6.45,3.35,'−',fontsize=30,color=NAVY,ha='center',va='center',fontweight='bold')
bx(ax,6.7,2.75,2.6,1.2,'대출이자','6.4억 × 5% = 3,200만원',WARN)
ax.text(10.1,3.35,'= 4,800만원',fontsize=15,color=NAVY,ha='center',va='center',fontweight='bold')
ax.plot([0.5,11.0],[2.45,2.45],color=NAVY,lw=3)
bx(ax,3.6,1.0,2.6,1.2,'자기자본','8억 − 6.4억 = 1.6억원',NAVY)
ax.text(8.2,1.6,'= 30%',fontsize=30,color=WARN,ha='center',va='center',fontweight='bold')
finish(fig,O+'fig1.png','대출 원금 6.4억원은 빼지 않습니다 · 1년 뒤 판 돈으로 갚습니다',allow_outside=True,strict=False)

# fig2 대출 쓰기 전과 후
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0.08,0.2,0.88,0.58])
head(fig,'자기자본수익률 계산 · 대출을 쓰기 전과 후','세 문제 모두 대출을 쓰면 자기자본수익률이 올라갑니다')
lab=['제29회 24번\n대출 50%','제33회 26번\n대출 40%','제36회 27번\n대출 80%']
a=[5,6.5,10]; b=[6,7.5,30]
x=np.arange(3); w=0.34
ax.bar(x-w/2,a,w,color=GREY); ax.bar(x+w/2,b,w,color=NAVY)
for i in range(3):
    ax.text(x[i]-w/2,a[i]+0.6,f'{a[i]:g}%',ha='center',fontsize=14,color=SAND,fontweight='bold')
    ax.text(x[i]+w/2,b[i]+0.6,f'{b[i]:g}%',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(lab,fontsize=13,color=TXT); ax.set_yticks([]); 
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE); ax.set_ylim(0,35)
ax.text(-0.4,31,'■ 대출 없이',color=SAND,fontsize=13,fontweight='bold'); ax.text(-0.4,28,'■ 대출을 써서',color=NAVY,fontsize=13,fontweight='bold')
finish(fig,O+'fig2.png','제36회 27번 대출 없이 10%는 참고로 계산한 값입니다 · 문제는 80% 대출만 물었습니다',allow_outside=True,strict=False)

# fig3 틀린 계산
fig,ax=canvas(5.8,4.6)
head(fig,'자기자본수익률 계산 · 틀리는 곳','제36회 27번, 같은 조건에서 계산을 틀리면 나오는 값')
rows=[('맞게 계산','(4,000 + 4,000 − 3,200) ÷ 1.6억','30%',OK),
      ('가격상승분을 빼먹음','(4,000 − 3,200) ÷ 1.6억','5%',WARN),
      ('분모에 매입가격을 씀','4,800만 ÷ 8억','6%',WARN)]
for i,(t,f,v,c) in enumerate(rows):
    y=3.4-i*1.2
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.45),10.4,0.95,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#F7F5F0' if i else '#EAF3EE',ec=c,lw=1.5))
    ax.text(0.8,y,t,fontsize=15,color=c,fontweight='bold',va='center')
    ax.text(4.2,y,f,fontsize=14,color=TXT,va='center')
    ax.text(10.3,y,v,fontsize=24,color=c,fontweight='bold',va='center',ha='right')
finish(fig,O+'fig3.png','「1년 뒤 처분」과 「가격상승률」이 보이면 가격상승분을 넣습니다',allow_outside=True,strict=False)

# fig4 레버리지
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.09,0.19,0.82,0.6])
head(fig,'자기자본수익률 계산 · 빚을 늘리면','빚 없이 번 수익률이 금리보다 높을 때만 빚이 수익률을 올립니다')
L=np.linspace(0,0.8,81)
for r,c,t in [(0.05,NAVY,'금리 5% · 정(+)의 레버리지'),(0.10,SAND,'금리 10% · 변화 없음'),(0.12,WARN,'금리 12% · 부(−)의 레버리지')]:
    y=(0.10-r*L)/(1-L)*100
    ax.plot(L*100,y,color=c,lw=3)
    ax.text(81,y[-1],t,fontsize=13,color=c,fontweight='bold',va='center')
ax.set_xlim(0,112); ax.set_ylim(-5,35)
ax.set_xticks([0,20,40,60,80]); ax.set_xticklabels(['0%','20%','40%','60%','80%'],fontsize=12,color=TXT)
ax.set_yticks([0,10,20,30]); ax.set_yticklabels(['0%','10%','20%','30%'],fontsize=12,color=TXT)
ax.set_xlabel('대출비율',fontsize=13,color=TXT); ax.set_ylabel('자기자본수익률',fontsize=13,color=TXT)
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.axhline(0,color=LINE,lw=1)
finish(fig,O+'fig4.png','제36회 27번 조건 · 빚 없이 번 수익률 10%에 금리만 바꿨습니다',allow_outside=True,strict=False)
