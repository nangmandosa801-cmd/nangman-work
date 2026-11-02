import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_gongsi_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['공시지가기준법 계산,','곱하기 다섯 번'],'시점 · 지역 · 개별 · 그 밖의 요인 · 10년 기출 다섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'공시지가기준법 계산 · 제36회 37번 곱하기 순서','500만원에서 출발해 비율을 차례로 곱하면 861만 8,400원')
steps=[('표준지\n공시지가',500,''),('× 1.05\n지가변동',525,''),('× 1.00\n지역요인',525,''),('× 0.95\n가로 5% 열세',498.75,''),('× 1.08\n획지 8% 우세',538.65,''),('× 1.6\n그 밖의 요인',861.84,'')]
cols=[GREY,MID,MID,WARN,OK,NAVY]
for i,(n,v,_) in enumerate(steps):
    ax.bar(i,v,color=cols[i],width=0.62); ax.text(i,v+18,f'{v:,.2f}'.rstrip('0').rstrip('.')+'만',ha='center',fontsize=13,color=cols[i] if cols[i]!=GREY else SAND,fontweight='bold')
ax.set_xticks(range(6)); ax.set_xticklabels([s[0] for s in steps],fontsize=12,color=TXT); ax.set_yticks([]); ax.set_ylim(0,980)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig1.png','단위는 원/㎡ · 면적은 곱하지 않습니다 · 정답 ④ 8,618,400원',allow_outside=True,strict=False)
# fig2 보기
fig=plt.figure(figsize=(11.2,5.6)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.4); ax.axis('off')
head(fig,'공시지가기준법 계산 · 제36회 37번 보기','지가변동률을 잘못 고르거나 그 밖의 요인을 빼면 오답입니다')
rows=[('①','5,386,500원','그 밖의 요인 60%를 빼먹음',WARN),('④','8,618,400원','주거지역 5% · 그 밖의 요인 1.6 (정답)',OK),('⑤','9,028,800원','이용상황만 보고 상업지역 10%를 씀',WARN)]
for i,(n,v,t,c) in enumerate(rows):
    y=3.3-i*1.15
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.4),10.4,0.82,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#F7F5F0',ec=c,lw=2 if c==OK else 1))
    ax.text(0.8,y,n,fontsize=19,color=c,fontweight='bold',va='center'); ax.text(1.5,y,v,fontsize=16,color=NAVY,fontweight='bold',va='center'); ax.text(4.4,y,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig2.png','대상토지는 제2종일반주거지역 · 지가변동률은 용도지역으로 고릅니다',allow_outside=True,strict=False)
# fig3 표준지 고르기
fig=plt.figure(figsize=(11.2,6.0)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.8); ax.axis('off')
head(fig,'공시지가기준법 계산 · 표준지가 두 개일 때','대상토지와 용도지역이 같은 표준지를 고릅니다')
def card(x,y,t,s,c,mark=None):
    ax.add_patch(mp.FancyBboxPatch((x,y),3.2,1.6,boxstyle='round,pad=0.02,rounding_size=0.12',fc='white',ec=c,lw=2.5))
    ax.text(x+1.6,y+1.1,t,ha='center',fontsize=15,color=NAVY,fontweight='bold'); ax.text(x+1.6,y+0.5,s,ha='center',fontsize=13,color=TXT)
    if mark: ax.text(x+3.0,y+1.35,mark,fontsize=24,color=c,fontweight='bold',ha='center',va='center')
card(0.5,2.6,'대상토지','일반상업지역 · 상업용',NAVY)
card(4.2,3.1,'표준지 기호 1','준주거지역 · 600만원',GREY,'X')
card(4.2,0.9,'표준지 기호 2','일반상업지역 · 800만원',OK,'O')
for yy in [3.9,1.7]: ax.annotate('',xy=(4.15,yy),xytext=(3.75,3.4),arrowprops=dict(arrowstyle='-|>',color=SAND,lw=2))
ax.text(7.7,2.3,'800만 × 1.05\n× 0.97 × 1.5\n= 12,222,000원',fontsize=15,color=OK,fontweight='bold',linespacing=1.5)
finish(fig,O+'fig3.png','제34회 35번 · 제30회 39번도 같은 방식 · 지가변동률도 상업지역 것을 씁니다',allow_outside=True,strict=False)
# fig4 상승식
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0.2,0.2,0.74,0.55])
head(fig,'공시지가기준법 계산 · 상승식은 곱합니다','제26회 35번 · 가로 5% 열세, 환경 20% 우세')
vals=[('곱하기 (상승식)','0.95 × 1.20 = 1.14 → 2,394,000원',2394000,OK),('더하기 (틀림)','1 − 0.05 + 0.20 = 1.15 → 2,415,000원',2415000,WARN)]
for i,(n,t,v,c) in enumerate(vals):
    y=1-i; ax.barh(y,v,0.5,color=c); ax.text(v*0.02,y,t,va='center',fontsize=14,color='white',fontweight='bold')
ax.set_yticks([0,1]); ax.set_yticklabels([v[0] for v in vals][::-1],fontsize=14,color=NAVY); ax.set_xlim(0,2600000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig4.png','더하면 2,415,000원 · 보기에 없는 값입니다 · 정답 ④ 2,394,000원',allow_outside=True,strict=False)
