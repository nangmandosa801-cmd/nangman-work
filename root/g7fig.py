import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_suik_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['수익환원법 계산,','빼면 안 되는 셋'],'순영업소득 ÷ 환원율 · 10년 기출 다섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1 분류
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.9); ax.axis('off')
head(fig,'수익환원법 계산 · 영업경비에 넣나 빼나','건물 운영에 드는 돈만 넣고, 주인에 따라 달라지는 돈은 뺍니다')
for x,t,c,items in [(0.4,'영업경비에 넣음',OK,['수선유지비 · 유지관리비','화재보험료','재산세']),(5.8,'영업경비에서 뺌',WARN,['부채서비스액 (대출 원리금)','영업소득세','개인업무비'])]:
    ax.add_patch(mp.FancyBboxPatch((x,0.4),5.0,4.0,boxstyle='round,pad=0.02,rounding_size=0.12',fc='#F7F5F0',ec=c,lw=2))
    ax.add_patch(mp.Rectangle((x+0.02,3.7),4.96,0.68,fc=c,ec='none'))
    ax.text(x+2.5,4.04,t,ha='center',va='center',fontsize=17,color='white',fontweight='bold')
    for i,it in enumerate(items): ax.text(x+0.45,3.0-i*0.95,('○ ' if c==OK else '× ')+it,fontsize=16,color=NAVY,fontweight='bold',va='center')
finish(fig,O+'fig1.png','대출 이자 · 주인 소득세 · 주인 개인 비용은 누가 주인이냐에 따라 달라집니다',allow_outside=True,strict=False)
# fig2 waterfall
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.07,0.2,0.88,0.56])
head(fig,'수익환원법 계산 · 제30회 37번 순서','가능총소득 8,000만원에서 순영업소득 6,500만원까지')
b=[('가능총소득',8000,0,GREY),('− 공실 10%',800,7200,WARN),('유효총소득',7200,0,MID),('− 영업경비\n400+100+200',700,6500,WARN),('순영업소득',6500,0,NAVY)]
for i,(n,v,bot,c) in enumerate(b):
    ax.bar(i,v,bottom=bot,color=c,width=0.6); ax.text(i,bot+v+120,('−' if bot else '')+f'{v:,}만',ha='center',fontsize=14,color=c if c!=GREY else SAND,fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels([x[0] for x in b],fontsize=12.5,color=TXT); ax.set_yticks([]); ax.set_ylim(0,9300)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig2.png','6,500만 ÷ 환원율 10% = 6억 5천만원 · 정답 ③',allow_outside=True,strict=False)
# fig3 보기
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,5.2); ax.axis('off')
head(fig,'수익환원법 계산 · 넣으면 안 되는 걸 넣으면','빼야 할 항목 하나마다 오답 보기가 하나씩 있습니다')
rows=[('30회 ③','6억 5천만원','수선·보험·재산세만 영업경비 (정답)',OK),('30회 ②','6억원','부채서비스액 500만원까지 넣음',WARN),('30회 ①','5억 7천만원','영업소득세 300만원까지 넣음',WARN),('28회 ⑤','11억 2,500만원','환원율 5% 대신 기대이율 4%로 나눔',WARN)]
for i,(n,v,t,c) in enumerate(rows):
    y=4.2-i*1.05
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.38),10.4,0.78,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#F7F5F0',ec=c,lw=2 if c==OK else 1))
    ax.text(0.7,y,n,fontsize=15,color=c,fontweight='bold',va='center'); ax.text(2.2,y,v,fontsize=16,color=NAVY,fontweight='bold',va='center'); ax.text(5.0,y,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig3.png','제28회 37번 정답은 ④ 9억원 · 4,500만 ÷ 5%',allow_outside=True,strict=False)
# fig4 투자결합법
fig=plt.figure(figsize=(11.2,5.8)); ax=fig.add_axes([0.2,0.22,0.74,0.52])
head(fig,'수익환원법 계산 · 제33회 37번 물리적 투자결합법','토지·건물 환원율을 가치 비율대로 섞으면 7%')
ax.barh(0,3,0.55,color=MID); ax.barh(0,4,0.55,left=3,color=OK)
ax.text(1.5,0,'토지 60% × 5% = 3%',ha='center',va='center',fontsize=14,color='white',fontweight='bold')
ax.text(5.0,0,'건물 40% × 10% = 4%',ha='center',va='center',fontsize=14,color='white',fontweight='bold')
ax.text(7.15,0,'= 7%',va='center',fontsize=22,color=WARN,fontweight='bold')
ax.set_xlim(0,8.5); ax.set_yticks([0]); ax.set_yticklabels(['환원율'],fontsize=15,color=NAVY); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig4.png','순영업소득 3,850만 ÷ 7% = 5억 5,000만원 · 정답 ③',allow_outside=True,strict=False)
