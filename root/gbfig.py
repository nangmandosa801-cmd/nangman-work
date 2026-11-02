import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.96,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.92,title,fontsize=23,color=NAVY,fontweight='bold',va='center')

# fig1 분양가 vs 옆 단지
R=[('강변역 센트럴아이파크 분양가',12.22,WARN),('래미안파크스위트 (2018)',18.5,MID),('구의현대2단지 (1996)',20.8,MID),('e편한세상 광진그랜드파크 (2021)',21.0,NAVY),('현대프라임 (1997)',21.5,MID),('극동2 광장동 (1989)',24.6,MID)]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.34,0.10,0.62,0.72])
head(fig,'전용 84㎡ · 2026년 3~8월 실거래 중앙값 · 광진구 구의동·광장동','강변역 센트럴아이파크 줍줍 12.2억, 옆 단지 84㎡는 18.5억~24.6억입니다')
n=len(R)
for i,(nm,v,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.6,color=c)
    ax.text(v+0.2,y,f'{v:.1f}억'+(' · 옆 단지의 58%' if i==0 else ''),va='center',fontsize=14.5,color=c,fontweight='bold')
    ax.text(-0.2,y,nm,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,32); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'gangbyeon_fig1.png','국토교통부 실거래가 · 센트럴아이파크는 올해 실거래 없음 · 그랜드파크 최고 22.9억 · 차익은 중앙값 기준 8~9억',allow_outside=True,strict=False)

# fig2 돈 구조
fig=plt.figure(figsize=(11.2,6.8)); ax=fig.add_axes([0.05,0.16,0.90,0.56])
head(fig,'분양가 12억 2,200만원 · 시세 15억 초과라 주택담보대출 4억 한도','당첨돼도 현금 8억 2천만원이 있어야 합니다')
parts=[('계약금 1.22억',1.22,WARN),('대출 4억',4.0,MID),('현금 잔금 7.0억',7.0,NAVY)]
x=0
for nm,v,c in parts:
    ax.barh(0,v,0.5,left=x,color=c); ax.text(x+v/2,0,nm,ha='center',va='center',fontsize=15,color='white',fontweight='bold'); x+=v
ax.text(12.22,0.45,'합계 12.22억',ha='right',va='bottom',fontsize=14,color=NAVY,fontweight='bold')
ax.text(0,-0.5,'+ 취득세 3,666만원(1주택 3%) · 6개월 내 전입 · 재당첨 제한 10년',ha='left',va='top',fontsize=13.5,color=MID)
ax.set_xlim(0,13); ax.set_ylim(-1.0,0.9); clean(ax)
finish(fig,O+'gangbyeon_fig2.png','대출은 분양가가 아니라 은행 감정·KB시세 기준 · 10·15 대책 15억 초과 4억 · DSR에 따라 더 줄 수 있음',allow_outside=True,strict=False)

render('서울 줍줍',['강변역 센트럴아이파크 84㎡','12.2억 · 옆 단지 21억'],'10월 6일 접수 · 서울 무주택 세대주 · 당첨 뒤 현금 8.2억',O+'gangbyeon_thumb.png')
print('ok')
