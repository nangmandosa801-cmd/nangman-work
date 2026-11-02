import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_daechul_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['총부채상환비율 계산,','작은 쪽이 한도입니다'],'LTV · DTI · 부채감당률 · 10년 기출 여섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def canvas(h=6.4,yl=5.2):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,yl); ax.axis('off'); return fig,ax
def bx(ax,x,y,w,h,t,s,fc):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.1',fc=fc,ec='none'))
    ax.text(x+w/2,y+h*0.66,t,ha='center',va='center',fontsize=15,color='white',fontweight='bold')
    ax.text(x+w/2,y+h*0.28,s,ha='center',va='center',fontsize=13.5,color='white')
def arr(ax,x1,x2,y,t=''):
    ax.annotate('',xy=(x2,y),xytext=(x1,y),arrowprops=dict(arrowstyle='-|>',color=SAND,lw=2.2,mutation_scale=20))
    if t: ax.text((x1+x2)/2,y+0.3,t,ha='center',fontsize=12.5,color=TXT)
# fig1 DTI 한도
fig,ax=canvas(5.8,4.6)
head(fig,'총부채상환비율 계산 · DTI 한도 구하는 순서','1년에 갚을 수 있는 돈을 저당상수로 나눕니다')
bx(ax,0.3,2.0,2.8,1.3,'연소득','7,000만원',MID)
arr(ax,3.2,4.1,2.65,'× 40%')
bx(ax,4.2,2.0,2.8,1.3,'1년에 갚을 수 있는 돈','2,800만원',NAVY)
arr(ax,7.1,8.0,2.65,'÷ 0.2')
bx(ax,8.1,2.0,2.8,1.3,'DTI 한도','1억 4,000만원',WARN)
ax.text(5.6,1.0,'저당상수 0.2 = 1억을 빌리면 1년에 2,000만원을 갚는다는 뜻',ha='center',fontsize=14,color=TXT)
finish(fig,O+'fig1.png','제36회 31번 숫자 · 한도를 구할 때는 저당상수로 나눕니다',allow_outside=True,strict=False)

# fig2 여섯 문제
fig=plt.figure(figsize=(11.2,7.0)); ax=fig.add_axes([0.2,0.14,0.76,0.66])
head(fig,'총부채상환비율 계산 · 10년 기출 여섯 문제','작은 쪽이 매번 다릅니다, 두 개를 다 계산해야 합니다')
P=[('제26회 11번',1.8,2.0,0,'DTI'),('제27회 25번',3.0,2.5,1.0,'DCR'),('제28회 27번',2.5,2.4,0.7,'DTI'),('제31회 34번',1.5,2.0,0.5,'DTI'),('제35회 29번',3.5,3.6,0.5,'DTI'),('제36회 31번',2.4,1.4,0.5,'DTI')]
for i,(n,l,d,e,k) in enumerate(P):
    y=len(P)-1-i
    m=min(l,d)
    ax.barh(y+0.18,l,0.32,color=NAVY if l<=d else GREY)
    ax.barh(y-0.18,d,0.32,color=WARN if d<l else GREY)
    ax.text(l+0.05,y+0.18,f'LTV {l:g}억',va='center',fontsize=11.5,color=NAVY if l<=d else SAND,fontweight='bold')
    ax.text(d+0.05,y-0.18,f'{k} {d:g}억',va='center',fontsize=11.5,color=WARN if d<l else SAND,fontweight='bold')
    ans=m-e
    ax.text(5.9,y,(f'{m:g} − 기존 {e:g} = ' if e else '')+f'{ans:g}억',va='center',ha='right',fontsize=12.5,color=TXT)
ax.set_yticks(range(len(P))); ax.set_yticklabels([p[0] for p in P][::-1],fontsize=13,color=NAVY)
ax.set_xlim(0,5.9); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig2.png','진한 막대가 한도입니다 · LTV가 작은 문제 넷, DTI·DCR이 작은 문제 둘',allow_outside=True,strict=False)

# fig3 36회 31번 흐름
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0.2,0.18,0.76,0.6])
head(fig,'총부채상환비율 계산 · 제36회 31번','LTV 2.4억과 DTI 1.4억 중 작은 1.4억에서 기존 5천만원을 뺍니다')
vals=[('LTV 한도',2.4,GREY),('DTI 한도',1.4,NAVY),('기존 대출',0.5,SAND),('추가 한도',0.9,WARN)]
for i,(n,v,c) in enumerate(vals):
    y=3-i; ax.barh(y,v,0.55,color=c)
    ax.text(v+0.04,y,f'{v:g}억' if v>=1 else f'{int(v*10000):,}만원',va='center',fontsize=15,color=c if c!=GREY else SAND,fontweight='bold')
ax.set_yticks(range(4)); ax.set_yticklabels([v[0] for v in vals][::-1],fontsize=14,color=NAVY)
ax.set_xlim(0,3); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig3.png','정답 ② 9,000만원 · 4억 × 60% = 2.4억, 7,000만 × 40% ÷ 0.2 = 1.4억',allow_outside=True,strict=False)

# fig4 보기가 만들어지는 길
fig,ax=canvas(6.6,5.4)
head(fig,'총부채상환비율 계산 · 제36회 31번 보기 다섯 개','틀린 계산마다 보기가 하나씩 준비돼 있습니다')
rows=[('①','2,800만원','1년에 갚을 수 있는 돈을 한도로 착각',WARN),
      ('②','9,000만원','1.4억 − 기존 5,000만원 (정답)',OK),
      ('③','1억 4,000만원','기존 대출을 빼지 않음',WARN),
      ('④','1억 9,000만원','LTV 2.4억에서 기존 대출만 뺌',WARN),
      ('⑤','2억 4,000만원','LTV만 계산',WARN)]
for i,(n,v,t,c) in enumerate(rows):
    y=4.35-i*0.92
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.36),10.4,0.74,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#F7F5F0',ec=c,lw=2 if c==OK else 1))
    ax.text(0.8,y,n,fontsize=18,color=c,fontweight='bold',va='center')
    ax.text(1.5,y,v,fontsize=15,color=NAVY,fontweight='bold',va='center')
    ax.text(4.4,y,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig4.png','LTV와 DTI를 둘 다 계산하고, 기존 대출을 빼면 ②만 남습니다',allow_outside=True,strict=False)
