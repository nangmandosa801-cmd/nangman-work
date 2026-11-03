# -*- coding: utf-8 -*-
# 오남역 서희스타힐스 글의 썸네일 · 그림 셋 · 위치 지도 (2026.10.5 01:52 사용자: 「이거 썸네일하고 시각화 자료」)
import sys; sys.path.insert(0,'/home/claude/blogkit'); sys.path.insert(0,'/home/claude/gs')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_jisan
from locmap import locmap
O='/mnt/user-data/outputs/jisandream/jisandream_onam_seohee_'
WARM='#B5761A'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.895,fs=24):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=fs,color=DEEP,fontproperties=FB,va='center')
# fig1 분양가와 오남 · 진접 84㎡ 실거래
R=[('금강펜테리움 (진접 · 2010년)',4.80,'4억 8,000만원',CYAN),('더샵남양주퍼스트시티 (진접 · 2021년)',4.685,'4억 6,850만원',CYAN),
   ('대림e편한세상 1단지 (오남 양지리 · 2009년)',4.50,'4억 5,000만원',DEEP),('대림e편한세상 2단지 (오남 양지리 · 2009년)',4.28,'4억 2,800만원',DEEP),
   ('남양주오남푸르지오 (오남리 · 2009년)',3.95,'3억 9,500만원',DEEP),('오남아이파크 (오남리 · 2009년)',3.885,'3억 8,850만원',DEEP)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.42,0.10,0.54,0.66])
head(fig,'전용 84㎡ · 2026년 3~8월에 팔린 값의 중앙값 · 국토교통부 실거래가','분양가는 오남에서 가장 비싼 거래보다 1억 8천 넘게 높습니다')
n=len(R)+1; y0=n-1
ax.barh(y0,7.19-6.70,0.58,left=6.70,color=WARM)
ax.text(7.29,y0,'6억 7,000만~\n7억 1,900만원',ha='left',va='center',fontsize=14.5,color=WARM,fontproperties=FB,linespacing=1.25)
ax.text(1.85,y0,'오남역 서희스타힐스 분양가 (2030년 입주)',ha='right',va='center',fontsize=14,color=WARM,fontproperties=FB,clip_on=False)
for i,(nm,v,lab,c) in enumerate(R):
    y=n-2-i; ax.barh(y,v-2,0.58,left=2,color=c)
    ax.text(v+0.08,y,lab,va='center',fontsize=15,color=c,fontproperties=FB)
    ax.text(1.85,y,nm,ha='right',va='center',fontsize=13.5,color=DEEP,fontproperties=FB,clip_on=False)
ax.plot([4.84,4.84],[n-2+0.36,n-0.3],color=WARM,lw=1.6,ls=(0,(5,4)))
ax.text(4.84,n-0.05,'올해 오남읍에서 가장 비싸게 팔린 84㎡ 4억 8,400만원',ha='center',va='center',fontsize=13.5,color=WARM,fontproperties=FB)
ax.set_xlim(2,9.3); ax.set_ylim(-0.6,n+0.25); clean(ax)
finish(fig,O+'fig1.png','막대는 2억원부터 그렸습니다 · 짙은 색은 오남읍 단지 · 분양가에 발코니 확장비 3,000만원은 따로입니다',brand='지산드림',allow_outside=True,strict=False)
# fig2 12가구를 층 순서로
U=[('1층','6억 7,000만')]*3+[('2층','6억 7,700만')]*2+[('3층','6억 8,400만')]*3+[('5~15층','6억 9,800만')]*3+[('26층 이상','7억 1,900만')]
fig=plt.figure(figsize=(11.2,6.6)); ax=fig.add_axes([0.04,0.16,0.92,0.50])
head(fig,'오남역 서희스타힐스 여의재 1단지 무순위 12가구 · 전용 84㎡ · 분양가','12가구 가운데 8가구가 3층 이하입니다',y1=0.94,y2=0.86)
for i,(fl,pr) in enumerate(U):
    r,c=divmod(i,6); x=c; y=1-r; low=i<8; col=DEEP if low else WARM
    ax.add_patch(FancyBboxPatch((x+0.06,y+0.08),0.88,0.84,boxstyle='round,pad=0,rounding_size=0.08',fc=col,ec='none'))
    ax.text(x+0.5,y+0.62,fl,ha='center',va='center',fontsize=17,color='white',fontproperties=FB)
    ax.text(x+0.5,y+0.30,pr+'원',ha='center',va='center',fontsize=12.5,color='white')
ax.set_xlim(0,6); ax.set_ylim(0,2); clean(ax)
fig.text(0.04,0.745,'■',fontsize=17,color=DEEP,va='center'); fig.text(0.065,0.745,'1~3층 8가구',fontsize=15.5,color=DEEP,fontproperties=FB,va='center')
fig.text(0.26,0.745,'■',fontsize=17,color=WARM,va='center'); fig.text(0.285,0.745,'5층 이상 4가구',fontsize=15.5,color=WARM,fontproperties=FB,va='center')
finish(fig,O+'fig2.png','어느 집에 당첨될지는 추첨으로 정해집니다 · 104동 4가구 · 105동 6가구 · 107동 2가구',brand='지산드림',allow_outside=True,strict=False)
# fig3 8월 첫 청약: 가구 수와 넣은 사람
Z=[('59㎡',122,56),('75㎡',15,12),('84㎡',9,19)]
fig=plt.figure(figsize=(11.2,6.8)); ax=fig.add_axes([0.14,0.16,0.80,0.52])
head(fig,'2026년 8월 첫 청약 · 일반공급 · 1순위와 2순위를 합친 접수 건수 · 청약홈','일반공급 146가구에 87명이 넣었습니다',y1=0.94,y2=0.86)
for i,(nm,a,b) in enumerate(Z):
    y=len(Z)-1-i
    ax.barh(y+0.19,a,0.34,color=GREY); ax.text(a+2,y+0.19,f'공급 {a}가구',va='center',fontsize=15,color='#5A6A78',fontproperties=FB)
    ax.barh(y-0.19,b,0.34,color=DEEP); ax.text(b+2,y-0.19,f'접수 {b}명',va='center',fontsize=15,color=DEEP,fontproperties=FB)
    ax.text(-4,y,nm,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB)
ax.set_xlim(0,160); ax.set_ylim(-0.6,len(Z)-0.4); clean(ax)
finish(fig,O+'fig3.png','84㎡만 1순위에서 마감됐습니다 · 이번 12가구는 그 84㎡ 가운데 계약되지 않은 집입니다',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 남양주 줍줍',['오남역 서희스타힐스','84㎡ 12가구 · 10월 6일'],'분양가 6억 7천~7억 2천 · 오남 실거래는 4억대',O+'thumb.png')
locmap(O+'map1.png','지산드림 · 남양주 줍줍','오남역 서희스타힐스 위치, 오남역까지 직선으로 1.2km입니다',
 '남색 점은 2026년 3~8월 전용 84㎡ 실거래 중앙값 · 붉은 점이 서희스타힐스 여의재 1단지입니다',
 site=(37.69986,127.20323,'오남역 서희스타힐스 여의재 1단지','분양가 6억 7,000만~7억 1,900만원',-40,-95),
 pts=[(37.69941,127.19554,'대림e편한세상 1단지','4억 5,000만원',-150,60),
      (37.70071,127.19692,'대림e편한세상 2단지','4억 2,800만원',-190,-45),
      (37.69556,127.19987,'남양주오남푸르지오','3억 9,500만원',-30,80),
      (37.69654,127.19958,'오남아이파크','3억 8,850만원',190,40)],
 stations=[(37.70516,127.19110,'오남역 4호선',0,-40)],pad=0.004,z=16,brand='지산드림')
print('ok')
