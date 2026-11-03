# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_listing
O='/mnt/user-data/outputs/jisandream/jisandream_homyeong_'
INK='#333333'; WARM='#B5761A'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.895):
    fig.text(0.04,y1,sub,fontsize=15.5,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
# fig1 자연녹지 산 넓이별 평당 값
R=[('호명리 2,400평 (올해 7월)',15,'평당 15만원','1건',DEEP),('1천 평 넘는 산',15,'평당 15만원','43건',DEEP),('3천 평 넘는 산',7.7,'평당 7만 7천원','15건',CYAN),
   ('1만 평 넘는 산',3.6,'평당 3만 6천원','4건',GREY),('호명리 이 매물 3만 7천 평',4.0,'평당 4만원','매도가 · 포장도로 · 전기',WARM)]
fig=plt.figure(figsize=(11.2,8.2)); ax=fig.add_axes([0.34,0.12,0.62,0.66])
head(fig,'가평 자연녹지 산(임야) 실거래 · 2023년 1월~2026년 8월 · 평당 중앙값','자연녹지 산은 평당 7만~15만원, 이 땅은 4만원입니다')
n=len(R)
for i,(nm,v,lab,sub,c) in enumerate(R):
    y=n-1-i; ax.barh(y,v,0.56,color=c)
    ax.text(v+0.4,y+0.10,lab,va='center',fontsize=17,color=c if c!=GREY else INK,fontproperties=FB)
    ax.text(v+0.4,y-0.22,sub,va='center',fontsize=13.5,color=GREY)
    ax.text(-0.4,y,nm,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,24); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig1.png','산은 크게 살수록 평당 값이 낮아집니다 · 지분 거래는 뺐습니다 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
# fig2 감정가 · 매도가 · 공시지가
B_=[('감정가',15.9,'15억 9,000만원','평당 4만 2,829원',GREY,INK),('매도가',14.85,'14억 8,500만원','평당 4만원',WARM,WARM),('공시지가',8.63,'8억 6,300만원','평당 2만 3,236원',CYAN,CYAN)]
fig=plt.figure(figsize=(11.2,7.4)); ax=fig.add_axes([0.08,0.24,0.84,0.50])
head(fig,'가평군 청평면 호명리 산38-1 · 산40 · 임야 37,124평','매도가는 감정가보다 1억 500만원 낮습니다',0.95,0.885)
for i,(nm,v,lab,sub,c,tc) in enumerate(B_):
    ax.bar(i,v,0.5,color=c)
    ax.text(i,v+0.4,lab,ha='center',va='bottom',fontsize=19,color=tc,fontproperties=FB)
    ax.text(i,-0.9,nm,ha='center',va='top',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(i,-2.6,sub,ha='center',va='top',fontsize=14.5,color=GREY)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-4.2,19.5); clean(ax); ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig2.png','감정가와 공시지가는 매도인이 준 자료입니다',brand='지산드림',allow_outside=True,strict=False)
render_listing('가평 토지 매물 · 청평 호명리 임야','자연녹지 임야','3만 7천 평','감정가보다 1억 낮습니다','포장도로 · 전기 · 계곡','총 14억 8,500만원',O+'thumb.png')
print('ok')
