import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_georae_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['거래사례비교법 계산,','면적 비율을 곱합니다'],'비준가액 · 사정보정 · 10년 기출 다섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1 사정보정
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0.2,0.2,0.74,0.55])
head(fig,'거래사례비교법 계산 · 사정보정','20% 싸게 팔린 사례는 100 ÷ 80 = 1.25를 곱해 정상가격으로 되돌립니다')
ax.barh(1,80,0.5,color=WARN); ax.barh(0,100,0.5,color=NAVY)
ax.text(81,1,'80 · 실제로 팔린 값',va='center',fontsize=14,color=WARN,fontweight='bold'); ax.text(101,0,'100 · 정상가격',va='center',fontsize=14,color=NAVY,fontweight='bold')
ax.set_yticks([0,1]); ax.set_yticklabels(['정상 거래라면','급매로 팔림'],fontsize=14,color=NAVY); ax.set_xlim(0,150); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig1.png','제28회 34번 답 1.25 · 제33회 39번처럼 사정보정치 0.9를 주면 그대로 곱합니다',allow_outside=True,strict=False)
# fig2 steps
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'거래사례비교법 계산 · 제35회 37번 곱하는 순서','6억 2,500만원 사례에서 대상토지 2억 8,600만원이 나옵니다')
st=[('거래가격',6.25,GREY),('× 80%\n토지 몫만',5.0,MID),('× 1.04\n주거지역',5.2,MID),('× 1.10\n개별 10% 우세',5.72,OK),('× 100 ÷ 200\n면적 비율',2.86,NAVY)]
for i,(n,v,c) in enumerate(st):
    ax.bar(i,v,color=c,width=0.6); ax.text(i,v+0.12,f'{v:g}억',ha='center',fontsize=15,color=c if c!=GREY else SAND,fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels([s[0] for s in st],fontsize=12.5,color=TXT); ax.set_yticks([]); ax.set_ylim(0,7.2)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig2.png','정답 ② 286,000,000원 · 마지막에 면적 비율 0.5를 곱해 절반이 됩니다',allow_outside=True,strict=False)
# fig3 보기
fig=plt.figure(figsize=(11.2,5.6)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.4); ax.axis('off')
head(fig,'거래사례비교법 계산 · 제35회 37번 보기','단계 하나를 틀리면 그 값이 보기에 있습니다')
rows=[('②','2억 8,600만원','토지 80% · 주거 4% · 면적 0.5 (정답)',OK),('③','2억 8,875만원','상업용이라고 상업지역 5%를 씀',WARN),('④','5억 7,200만원','면적 비율 0.5를 빼먹음',WARN)]
for i,(n,v,t,c) in enumerate(rows):
    y=3.3-i*1.15
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.4),10.4,0.82,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#F7F5F0',ec=c,lw=2 if c==OK else 1))
    ax.text(0.8,y,n,fontsize=19,color=c,fontweight='bold',va='center'); ax.text(1.5,y,v,fontsize=16,color=NAVY,fontweight='bold',va='center'); ax.text(4.6,y,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig3.png','대상토지는 제3종일반주거지역 · 지가변동률은 용도지역으로 고릅니다',allow_outside=True,strict=False)
# fig4 면적
fig=plt.figure(figsize=(11.2,6.0)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.8); ax.axis('off')
head(fig,'거래사례비교법 계산 · 면적 비율','대상이 작으면 값이 줄고, 크면 값이 늘어납니다')
def sq(x,y,s,c,t):
    ax.add_patch(mp.Rectangle((x,y),s,s,fc=c,ec='white',lw=2)); ax.text(x+s/2,y+s/2,t,ha='center',va='center',fontsize=14,color='white',fontweight='bold')
sq(0.6,1.0,2.4,SAND,'사례\n200㎡'); sq(3.3,1.0,1.7,NAVY,'대상\n100㎡')
ax.text(2.8,0.5,'제35회 37번 · × 0.5',ha='center',fontsize=15,color=NAVY,fontweight='bold')
sq(6.2,1.0,2.0,SAND,'사례\n100㎡'); sq(8.5,1.0,2.2,MID,'대상\n120㎡')
ax.text(8.4,0.5,'제29회 40번 · × 1.2',ha='center',fontsize=15,color=MID,fontweight='bold')
finish(fig,O+'fig4.png','면적 비율 = 대상 면적 ÷ 사례 면적 · 빼먹으면 제29회 40번 ② 2억 9,640만원',allow_outside=True,strict=False)
