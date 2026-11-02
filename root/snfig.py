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

# fig1 순서도
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.03,0.08,0.94,0.74])
head(fig,'성남 수정구·중원구 원도심 · 순환 재개발 · 2026년 10월 기준','성남 재개발 구역 순서, 완료 4곳 → 이주 수진1 → 진행 신흥1 → 지정 상대원3')
cols=[('완료','#1F3864',[('금광1 5,320','2020~23'),('중1 2,411','2022'),('신흥2 4,774','2023~24'),('산성 3,487','2025')]),('이주',WARN,[('수진1 5,060','6월 관리처분 · 8월 이주'),('',''),('',''),('','')]),('진행',MID,[('신흥1 4,183','사업시행인가 신청'),('신흥3 · 태평3','LH 순환정비'),('',''),('','')]),('지정',LB,[('상대원3 8,792','2026.2 LH 시행자 · 2031 착공'),('',''),('',''),('','')])]
for i,(t,c,items) in enumerate(cols):
    x=0.02+i*0.245
    ax.add_patch(plt.Rectangle((x,0.86),0.22,0.1,color=c)); ax.text(x+0.11,0.91,t,ha='center',va='center',fontsize=17,color='white',fontweight='bold')
    for j,(a,b) in enumerate(items):
        y=0.76-j*0.19
        if a or b:
            ax.add_patch(plt.Rectangle((x,y-0.07),0.22,0.15,fill=False,ec=c,lw=2))
            ax.text(x+0.01,y+0.03,a,fontsize=13.5,color=NAVY,fontweight='bold',va='center'); ax.text(x+0.01,y-0.035,b,fontsize=11.5,color=MID,va='center')
    if i<3: ax.annotate('',xy=(x+0.245,0.91),xytext=(x+0.22,0.91),arrowprops=dict(arrowstyle='-|>',color=LINE,lw=2))
ax.set_xlim(0,1); ax.set_ylim(0,1); clean(ax)
finish(fig,O+'snredev_fig1.png','수진1은 6월 16일 관리처분인가 뒤라 조합원 지위 양도 제한 · 2기부터 LH 시행 · 가구수는 보도 기준',allow_outside=True,strict=False)

# fig2 신축 vs 구축
R=[('산성역 포레스티아 (2020)',15.5,26.7),('신흥역 하늘채 랜더스원 (2022)',14.48,31.3),('산성역 자이푸르지오 (2023~24)',14.2,29.3),('금빛 그랑메종 (2022~23)',11.7,31.2),('그 외 2001년 이후',11.4,18.4),('2000년 이전 구축',8.67,11.5)]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.32,0.10,0.64,0.72])
head(fig,'전용 84㎡ 중앙값(2026.3~8) · 막대 끝은 1년 변동(같은 단지·면적)','산성역 아파트 시세, 재개발 신축 14.5억은 1년에 30% 구축 8.7억은 11.5%입니다')
n=len(R)
for i,(nm,p,ch) in enumerate(R):
    y=n-1-i; c=NAVY if i<4 else (MID if i==4 else WARN)
    ax.barh(y,p,0.6,color=c)
    ax.text(p+0.2,y,f'{p:.1f}억 · 1년 {ch:+.1f}%',va='center',fontsize=14,color=c,fontweight='bold')
    ax.text(-0.2,y,nm,ha='right',va='center',fontsize=13.5,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,22); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'snredev_fig2.png','국토교통부 실거래가 · 성남 수정구·중원구 · 해제 거래 제외 · 구축은 고점 대비 -11.1%, 재개발 신축은 +16.9%',allow_outside=True,strict=False)

render('성남 재개발 구역',['수진1 8월 이주 · 신흥1 LH','상대원3 2031년 착공'],'입주한 산성역·금광 신축은 1년에 +30% · 구축은 고점 아래',O+'snredev_thumb.png')
print('ok')
