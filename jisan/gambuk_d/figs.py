# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_jisan
O='/mnt/user-data/outputs/jisandream/jisandream_gambuk_'
INK='#333333'; WARM='#B5761A'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.895):
    fig.text(0.04,y1,sub,fontsize=15.5,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
# fig1 네 가지 땅
R=[('마을 안 집터',1120,'평당 1,120만원','88평 · 11억원쯤',WARM),('그린벨트 밭 · 논',290,'평당 290만원','209평 · 5억 5천만원쯤',DEEP),
   ('지분 (대부분 산)',270,'평당 270만원','11평 · 2,600만원쯤',CYAN),('산 (통째로)',100,'평당 100만원','199평 · 2억원쯤',GREY)]
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.30,0.12,0.66,0.64])
head(fig,'하남 감북동 토지 실거래 · 2019년~2026년 8월 · 한가운데 값','같은 감북동인데 평당 100만원부터 1,120만원까지')
n=len(R)
for i,(nm,v,lab,sub,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.56,color=c)
    ax.text(v+25,y+0.10,lab,va='center',fontsize=17,color=c if c!=GREY else INK,fontproperties=FB)
    ax.text(v+25,y-0.22,sub,va='center',fontsize=13.5,color=GREY)
    ax.text(-30,y,nm,ha='right',va='center',fontsize=16.5,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,1700); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig1.png','통째로 판 땅은 100㎡(30평) 넘는 것만 셌습니다 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
# fig2 산 통째 vs 지분
fig=plt.figure(figsize=(11.2,6.8)); ax=fig.add_axes([0.10,0.26,0.80,0.50])
head(fig,'하남 감북동 산(임야) 실거래 · 평당 한가운데 값','같은 산인데 나눠 팔면 평당 값이 세 배입니다',0.95,0.885)
B_=[('통째로 팔 때',100,'평당 100만원','199평 · 2억원쯤',GREY,INK),('지분으로 나눠 팔 때',300,'평당 300만원','7평 · 1,800만원쯤',WARM,WARM)]
for i,(nm,v,lab,sub,c,tc) in enumerate(B_):
    ax.bar(i,v,0.5,color=c)
    ax.text(i,v+10,lab,ha='center',va='bottom',fontsize=20,color=tc,fontproperties=FB)
    ax.text(i,-18,nm,ha='center',va='top',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(i,-52,'한 번에 사는 크기 '+sub,ha='center',va='top',fontsize=14.5,color=GREY)
ax.set_xlim(-0.7,1.7); ax.set_ylim(-80,370); clean(ax); ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig2.png','통째로 판 산은 2019년부터 41건 · 지분은 2025년부터 229건 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
render_jisan('하남 부동산 · 하남 토지 매매',['감북동 그린벨트 밭 290만원','마을 안 집터 1,120만원'],'팔린 땅 열에 일곱은 지분입니다',O+'thumb.png')
print('ok')
