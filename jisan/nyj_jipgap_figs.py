# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
O='/mnt/user-data/outputs/jisandream/jisandream_nyj_jipgap_'
INK='#333333'; WARM='#B5761A'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.960,y2=0.912):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
# fig1 동네별 84㎡ 값 (억)
R=[('다산동',9.2,'9억 2,000만원'),('별내동',6.935,'6억 9,350만원'),('와부읍',5.3,'5억 3,000만원'),('퇴계원읍',4.725,'4억 7,250만원'),('호평동',4.5,'4억 5,000만원'),('진접읍',4.25,'4억 2,500만원'),
   ('평내동',3.88,'3억 8,800만원'),('화도읍',3.2,'3억 2,000만원'),('별내면',3.195,'3억 1,950만원'),('오남읍',2.945,'2억 9,450만원'),('진건읍',2.5275,'2억 5,275만원')]
fig=plt.figure(figsize=(11.2,10.0)); ax=fig.add_axes([0.20,0.08,0.74,0.76])
head(fig,'남양주 아파트 전용 84㎡ · 2026년 1~8월 한가운데 값','남양주 집값, 다산 9억 2천부터 진건 2억 5천까지')
n=len(R)
for i,(nm,v,lab) in enumerate(R):
    y=n-1-i; c=WARM if i==0 else DEEP
    ax.barh(y,v,0.62,color=c)
    ax.text(v+0.15,y,lab,va='center',fontsize=15.5,color=c,fontproperties=FB)
    ax.text(-0.15,y,nm,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,12.6); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig1.png','다산동 84㎡ 한 채 값이 진건읍의 3.6배입니다',brand='지산드림',allow_outside=True,strict=False)
# fig2 1년 상승률
R=[('다산동',10.8),('와부읍',7.3),('퇴계원읍',4.3),('호평동',3.1),('평내동',2.6),('별내동',2.4),('진접읍',1.3),('오남읍',-0.2),('화도읍',-0.4)]
fig=plt.figure(figsize=(11.2,9.2)); ax=fig.add_axes([0.20,0.08,0.74,0.74])
head(fig,'같은 단지 같은 넓이 집끼리 비교 · 작년 3~8월과 올해 3~8월','남양주 집값 상승률, 다산만 11% 올랐습니다',0.958,0.906)
n=len(R)
for i,(nm,v) in enumerate(R):
    y=n-1-i; c=WARM if v>=5 else (GREY if v<0 else DEEP)
    ax.barh(y,v,0.6,color=c)
    ax.text(v+0.18 if v>=0 else 0.18,y,f'{v:+.1f}%',va='center',fontsize=16,color=c,fontproperties=FB)
    ax.text(-1.5,y,nm,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB,clip_on=False)
ax.axvline(0,color=LINE,lw=1.5)
ax.set_xlim(-1.3,13); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig2.png','남양주 전체는 2.7% · 화도읍과 오남읍은 1년 전보다 내렸습니다',brand='지산드림',allow_outside=True,strict=False)
