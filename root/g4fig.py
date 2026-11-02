import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp, numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_gyesan_wonga_'
TXT='#444'; GREY='#C9C4BA'; OK='#3C7A5A'
render('낭만 부동산 분석 플랫폼 · 부동산학개론 계산문제',['원가법 계산,','두 줄로 끝납니다'],'재조달원가 − 감가수정 = 적산가액 · 10년 기출 여섯 문제',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
# fig1 waterfall
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.08,0.18,0.86,0.58])
head(fig,'원가법 계산 · 제36회 39번 두 줄 풀이','지금 다시 지으면 3.5억, 6년 낡은 만큼 빼면 3.08억')
xs=['신축공사비\n140만 × 200㎡','재조달원가\n× 125 ÷ 100','감가수정\n3.5억 × 6 ÷ 50','적산가액']
ax.bar(0,2.8,color=GREY,width=0.6); ax.bar(1,3.5,color=MID,width=0.6); ax.bar(2,0.42,bottom=3.08,color=WARN,width=0.6); ax.bar(3,3.08,color=NAVY,width=0.6)
for x,v,t,c in [(0,2.8,'2.8억',SAND),(1,3.5,'3.5억',MID),(2,3.5,'− 4,200만',WARN),(3,3.08,'3.08억',NAVY)]:
    ax.text(x,v+0.08,t,ha='center',fontsize=15,color=c,fontweight='bold')
ax.set_xticks(range(4)); ax.set_xticklabels(xs,fontsize=12.5,color=TXT); ax.set_yticks([]); ax.set_ylim(0,4.1)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(LINE)
finish(fig,O+'fig1.png','첫 줄은 재조달원가, 둘째 줄은 감가수정 · 정답 ③ 308,000,000원',allow_outside=True,strict=False)
# fig2 보기
fig=plt.figure(figsize=(11.2,5.6)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,4.4); ax.axis('off')
head(fig,'원가법 계산 · 제36회 39번 보기','한 단계를 빼먹으면 그 값이 보기에 있습니다')
rows=[('①','2억 4,640만원','건축비지수를 빼먹음 · 2.8억 × 0.88',WARN),('③','3억 800만원','지수 반영 후 감가 · 3.5억 × 0.88 (정답)',OK),('⑤','3억 5,000만원','감가수정을 빼먹음 · 재조달원가 그대로',WARN)]
for i,(n,v,t,c) in enumerate(rows):
    y=3.3-i*1.15
    ax.add_patch(mp.FancyBboxPatch((0.4,y-0.4),10.4,0.82,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#EAF3EE' if c==OK else '#F7F5F0',ec=c,lw=2 if c==OK else 1))
    ax.text(0.8,y,n,fontsize=19,color=c,fontweight='bold',va='center'); ax.text(1.5,y,v,fontsize=16,color=NAVY,fontweight='bold',va='center'); ax.text(4.6,y,t,fontsize=14,color=TXT,va='center')
finish(fig,O+'fig2.png','경과연수 6년 ÷ 내용연수 50년 = 12%를 빼서 0.88을 곱합니다',allow_outside=True,strict=False)
# fig3 잔가율
fig=plt.figure(figsize=(11.2,6.0)); ax=fig.add_axes([0.2,0.18,0.74,0.58])
head(fig,'원가법 계산 · 제31회 38번 잔가율 10%','40년 뒤에도 10%는 남으니 90%만 나눠서 뺍니다')
vals=[('재조달원가',6600,MID,'6,600만원'),('40년 동안 뺄 돈',5940,SAND,'6,600만 × 90% = 5,940만원'),('1년 감가',148.5,WARN,'5,940만 ÷ 40 = 148만 5천원'),('적산가액',6303,NAVY,'6,600만 − 297만 = 6,303만원')]
for i,(n,v,c,t) in enumerate(vals):
    y=3-i; ax.barh(y,v,0.55,color=c); ax.text(max(v,300)+80,y,t,va='center',fontsize=13.5,color=c,fontweight='bold')
ax.set_yticks(range(4)); ax.set_yticklabels([v[0] for v in vals][::-1],fontsize=14,color=NAVY); ax.set_xlim(0,11500); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINE)
finish(fig,O+'fig3.png','잔가율을 빼지 않으면 6,270만원 · 보기 ③이 그 값입니다',allow_outside=True,strict=False)
# fig4 정액 vs 정률
fig=plt.figure(figsize=(11.2,6.2)); ax=fig.add_axes([0.1,0.2,0.84,0.56])
head(fig,'원가법 계산 · 정액법과 정률법','정액법은 매년 같은 금액, 정률법은 매년 같은 비율로 줄어듭니다')
t=np.arange(0,11)
ax.plot(t,1e4*(1-t/50),color=MID,lw=3,marker='o',ms=5); ax.plot(t,1e4*0.7**t,color=WARN,lw=3,marker='o',ms=5)
ax.text(10.2,1e4*(1-10/50),'정액법 · 내용연수 50년',color=MID,fontsize=13,fontweight='bold',va='center')
ax.text(10.2,1e4*0.7**10+300,'정률법 · 잔가율 70%',color=WARN,fontsize=13,fontweight='bold',va='center')
ax.scatter([2],[4900],s=110,color=WARN,zorder=3); ax.text(2.3,5200,'2년 뒤 4,900만원 (제28회 40번)',fontsize=13,color=WARN,fontweight='bold')
ax.set_xlim(0,14.5); ax.set_ylim(0,11000); ax.set_xticks([0,2,4,6,8,10]); ax.set_xticklabels(['0','2년','4년','6년','8년','10년'],fontsize=11,color=TXT)
ax.set_yticks([0,5000,10000]); ax.set_yticklabels(['0','5,000만','1억'],fontsize=11,color=TXT)
for s in ['top','right']: ax.spines[s].set_visible(False)
finish(fig,O+'fig4.png','재조달원가 1억원 기준 · 정률법은 1억 × 0.7 × 0.7',allow_outside=True,strict=False)
