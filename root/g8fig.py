import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_seungsu_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['부채감당률,','현금흐름 다섯 줄'],'승수 · 환원율 · 비율 · 10년 기출 여섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'부채감당률 계산 · 현금흐름 다섯 줄 (제34회 23번 숫자)','위에서부터 하나씩 빼 내려가면 세후현금흐름 3,600만원')
rows=[('가능총소득',6000,GREY,''),('유효총소득',5100,MID,'− 공실 15%'),('순영업소득',4600,NAVY,'− 재산세 500'),('세전현금흐름',4000,OK,'− 원리금 600'),('세후현금흐름',3600,WARN,'− 영업\n소득세 400')]
for i,(n,v,c,t) in enumerate(rows):
    ax.bar(i,v,color=c,width=0.6); ax.text(i,v+120,f'{v:,}만',ha='center',fontsize=14,color=c if c!=GREY else SAND,fontweight='bold')
    if t: ax.text(i,v/2,t,ha='center',va='center',fontsize=12,color='white',fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels([r[0] for r in rows],fontsize=13,color=TXT); ax.set_yticks([]); ax.set_ylim(0,6900)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig1.png','세후현금흐름승수 = 지분 36,000만 ÷ 3,600만 = 10 · 정답 ②',allow_outside=True,strict=False)
# fig2 짝
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.9); ax.axis('off')
head(fig,'부채감당률 계산 · 무엇끼리 나누나','총투자액은 순영업소득과, 지분투자액은 현금흐름과 짝입니다')
def bx(x,y,w,t,c):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,0.8,boxstyle='round,pad=0.02,rounding_size=0.1',fc=c,ec='none')); ax.text(x+w/2,y+0.4,t,ha='center',va='center',fontsize=15,color='white',fontweight='bold')
bx(0.4,3.4,2.8,'총투자액',NAVY); bx(4.1,3.4,2.8,'순영업소득',NAVY)
ax.text(7.2,4.0,'총투자액 ÷ 순영업소득 = 순소득승수',fontsize=13,color=NAVY,va='center'); ax.text(7.2,3.55,'뒤집으면 종합환원율',fontsize=13,color=SAND,va='center')
bx(0.4,1.4,2.8,'지분투자액',OK); bx(4.1,1.9,2.8,'세전현금흐름',OK); bx(4.1,0.8,2.8,'세후현금흐름',OK)
ax.text(7.2,2.3,'지분 ÷ 세전 = 세전현금흐름승수',fontsize=13,color=OK,va='center'); ax.text(7.2,1.2,'지분 ÷ 세후 = 세후현금흐름승수',fontsize=13,color=OK,va='center')
ax.text(7.2,1.75,'세전 ÷ 지분 = 지분환원율',fontsize=13,color=SAND,va='center')
for (y1,y2,c) in [(3.8,3.8,NAVY),(1.8,2.3,OK),(1.8,1.2,OK)]: ax.annotate('',xy=(4.05,y2),xytext=(3.25,y1),arrowprops=dict(arrowstyle='<->',color=c,lw=2))
finish(fig,O+'fig2.png','짝을 바꿔 나누면 보기에 있는 오답이 나옵니다',allow_outside=True,strict=False)
# fig3 DCR
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0.22,0.2,0.72,0.55])
head(fig,'부채감당률 계산 · 제34회 22번','순영업소득 3,240만원이 1년 원리금 3,000만원의 1.08배')
ax.barh(1,3240,0.5,color=NAVY); ax.barh(0,3000,0.5,color=WARN)
ax.text(3280,1,'3,240만 · 4,500만 × 72%',va='center',fontsize=14,color=NAVY,fontweight='bold'); ax.text(3040,0,'3,000만 · 2.5억 × 0.12',va='center',fontsize=14,color=WARN,fontweight='bold')
ax.set_yticks([0,1]); ax.set_yticklabels(['부채서비스액','순영업소득'],fontsize=14,color=NAVY); ax.set_xlim(0,5600); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig3.png','3,240 ÷ 3,000 = 1.08 · 정답 ① · 영업경비 28%는 유효총소득에 곱합니다',allow_outside=True,strict=False)
# fig4 34-25
fig=plt.figure(figsize=(11.2,5.6)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.4); ax.axis('off')
head(fig,'부채감당률 계산 · 제34회 25번 틀린 보기','지분환원율은 원리금을 뺀 돈으로 나눕니다')
for i,(t,f,v,c) in enumerate([('맞는 계산','(2억 − 2,000만) ÷ 8억','22.5%',OK),('보기 ③','2억 ÷ 8억 (원리금을 안 뺌)','25%',WARN)]):
    y=3.0-i*1.4
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.5),10.4,1.0,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#FBEFEA',ec=c,lw=2))
    ax.text(0.8,y,t,fontsize=16,color=c,fontweight='bold',va='center'); ax.text(3.2,y,f,fontsize=15,color=TXT,va='center'); ax.text(10.4,y,v,fontsize=26,color=c,fontweight='bold',va='center',ha='right')
finish(fig,O+'fig4.png','나머지 넷은 맞는 값 · 그래서 ③이 틀린 것입니다',allow_outside=True,strict=False)
