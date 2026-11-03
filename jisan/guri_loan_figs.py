# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
O='/mnt/user-data/outputs/jisandream/jisandream_guri_loan_'
INK='#333333'; WARM='#B5761A'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.905):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
def won(v):
    e=int(v//10000); m=int(round(v-e*10000))
    return (f'{e}억' if e else '')+(f' {m:,}만' if m else '')
# fig1 내 돈 (만원)
R=[('구리 갈매동','7억 5,000만원',45000,45000),('남양주 별내동','6억 9,350만원',20805,29350),('남양주 다산동','9억 2,000만원',32000,52000)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.06,0.20,0.88,0.56])
head(fig,'84㎡ 아파트 한 채 · 일반 무주택자 · 2026년 1~8월 한가운데 값','84㎡ 한 채에 드는 내 돈')
fig.text(0.06,0.835,'■ 지금 (한도 6억)',fontsize=15,color=DEEP,fontproperties=FB); fig.text(0.30,0.835,'■ 한도가 4억으로 줄면',fontsize=15,color=WARM,fontproperties=FB)
for i,(nm,pr,a,b) in enumerate(R):
    ax.bar(i-0.2,a,0.36,color=DEEP); ax.bar(i+0.2,b,0.36,color=WARM)
    ax.text(i-0.2,a+1200,won(a),ha='center',fontsize=15,color=DEEP,fontproperties=FB)
    ax.text(i+0.2,b+1200,won(b),ha='center',fontsize=15,color=WARM,fontproperties=FB)
    ax.text(i,-2600,nm,ha='center',va='top',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(i,-7400,'집값 '+pr,ha='center',va='top',fontsize=14,color=GREY)
    d=b-a; ax.text(i,-11400,'그대로' if d==0 else '+'+won(d).strip(),ha='center',va='top',fontsize=15,color=INK if d==0 else WARM,fontproperties=FB)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-17000,62000); clean(ax); ax.axhline(0,color=LINE,lw=1.5)
finish(fig,O+'fig1.png','구리는 집값의 40%, 남양주는 70%까지 빌릴 수 있습니다 · 4억은 정해진 숫자가 아닙니다',brand='지산드림',allow_outside=True,strict=False)

# fig2 동네별 비율
G=[('구리 토평동',34.8,'구리'),('구리 교문동',13.2,'구리'),('구리 수택동',8.1,'구리'),('구리 인창동',3.6,'구리'),('구리 갈매동',0.3,'구리'),
   ('남양주 다산동',96.3,'남'),('남양주 별내동',93.5,'남'),('남양주 와부읍',34.3,'남'),('남양주 퇴계원읍',22.4,'남'),('남양주 호평동',14.7,'남'),('남양주 진접읍',3.6,'남')]
fig=plt.figure(figsize=(11.2,10.2)); ax=fig.add_axes([0.25,0.09,0.62,0.70])
head(fig,'일반 무주택자가 집을 살 때 · 아파트 매매 2026년 1~8월','한도가 4억으로 줄면 대출이 줄어드는 집',0.960,0.912)
fig.text(0.25,0.850,'■ 구리 (집값의 40% · 10억 넘는 집)',fontsize=14.5,color=DEEP,fontproperties=FB); fig.text(0.25,0.815,'■ 남양주 (집값의 70% · 5억 7천 넘는 집)',fontsize=14.5,color=WARM,fontproperties=FB)
n=len(G)
for i,(nm,v,k) in enumerate(G):
    y=n-1-i-(0.5 if k=='남' else 0); c=DEEP if k=='구리' else WARM
    ax.barh(y,v,0.62,color=c)
    ax.text(v+1.5,y,f'{v:.0f}%' if v>=1 else f'{v:.1f}%',va='center',fontsize=15.5,color=c,fontproperties=FB)
    ax.text(-2,y,nm,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,112); ax.set_ylim(-1.2,n-0.4); clean(ax)
finish(fig,O+'fig2.png','구리 전체 7% · 남양주 전체 43% · 4억은 정해진 숫자가 아닙니다',brand='지산드림',allow_outside=True,strict=False)
