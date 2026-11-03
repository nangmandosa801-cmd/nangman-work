# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
from thumbnail import render_jisan
OUT='/mnt/user-data/outputs/jisandream/'
INK='#333333'; WARM='#B5761A'
def clean(ax,keepx=False):
    if not keepx: ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.895,fs=24):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=fs,color=DEEP,fontproperties=FB,va='center')
# ───── 1편 가평 땅값 ─────
O=OUT+'jisandream_gp_ttang_'
# fig1 밭논 용도지역 × 도로
Z=[('자연녹지지역',73,48),('계획관리지역',52,43),('생산관리지역',42,37),('보전관리지역',33,20),('농림지역',28,27)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.24,0.10,0.72,0.66])
head(fig,'가평 밭과 논 · 100~1천 평 · 2023년 1월~2026년 8월 · 평당 중앙값','같은 밭도 계획관리지역 52만원, 농림지역 28만원입니다')
n=len(Z)
for i,(nm,a,b) in enumerate(Z):
    y=(n-1-i)*1.0; hi=nm in('계획관리지역','농림지역')
    ax.barh(y+0.19,a,0.34,color=DEEP if hi else CYAN); ax.barh(y-0.19,b,0.34,color=GREY)
    ax.text(a+1.2,y+0.19,f'{a}만원',va='center',fontsize=17 if hi else 15.5,color=DEEP if hi else CYAN,fontproperties=FB)
    ax.text(b+1.2,y-0.19,f'{b}만원',va='center',fontsize=14.5,color=INK)
    ax.text(-1.5,y,nm,ha='right',va='center',fontsize=16.5,color=DEEP,fontproperties=FB,clip_on=False)
ax.barh(n-0.25,6,0.2,left=58,color=CYAN); ax.text(65.5,n-0.25,'도로 붙음',va='center',fontsize=14,color=INK)
ax.barh(n-0.25,6,0.2,left=79,color=GREY); ax.text(86.5,n-0.25,'도로 표시 없음',va='center',fontsize=14,color=INK)
ax.set_xlim(0,100); ax.set_ylim(-0.6,n+0.05); clean(ax)
finish(fig,O+'fig1.png','지분으로 판 땅은 뺐습니다 · 칸마다 42건에서 506건 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
# fig2 면별 밭 · 대지
M=[('청평면',79,147),('설악면',57,86),('상면',53,69),('조종면',50,57),('가평읍',45,79),('북면',33,36)]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.16,0.10,0.80,0.66])
head(fig,'가평 계획관리지역 · 도로 붙은 땅 · 2023년 1월~2026년 8월 · 평당 중앙값','같은 조건의 밭, 청평면 79만원이고 북면 33만원입니다')
n=len(M)
for i,(nm,a,b) in enumerate(M):
    y=(n-1-i)*1.0; hi=nm in('청평면','북면')
    ax.barh(y+0.19,a,0.34,color=DEEP if hi else CYAN); ax.barh(y-0.19,b,0.34,color=WARM,alpha=0.85)
    ax.text(a+2.5,y+0.19,f'밭 · 논 {a}만원',va='center',fontsize=16.5 if hi else 15,color=DEEP if hi else CYAN,fontproperties=FB)
    ax.text(b+2.5,y-0.19,f'대지 {b}만원',va='center',fontsize=14.5,color=WARM,fontproperties=FB)
    ax.text(-3,y,nm,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,200); ax.set_ylim(-0.6,n-0.3); clean(ax)
finish(fig,O+'fig2.png','밭 · 논은 100~1천 평 · 대지는 넓이를 가리지 않았습니다 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
# fig3 임야 넓이 × 용도지역
S=['1천 평 미만','1천~3천 평','3천~1만 평','1만 평 넘음']
V={'자연녹지지역':([57,15,15,3.6],DEEP),'계획관리지역':([43,13,3.9,6.7],CYAN),'농림지역':([8,4,2.6,1.0],GREY)}
def won(v): return f'{int(v)}만원' if v>=10 or float(v).is_integer() else (f'{int(v)}만 {int(round((v-int(v))*10))}천원')
fig=plt.figure(figsize=(11.2,10.2)); ax=fig.add_axes([0.20,0.09,0.76,0.70])
head(fig,'가평 임야 · 2023년 1월~2026년 8월 · 평당 중앙값','임야는 넓을수록 평당 값이 낮아집니다',0.962,0.912)
names=list(V); nS=len(S)
for i,sz in enumerate(S):
    y0=(nS-1-i)*1.25
    for k,nm in enumerate(names):
        vals,c=V[nm]; v=vals[i]; y=y0+(1-k)*0.3
        ax.barh(y,v,0.26,color=c)
        ax.text(v+0.9,y,won(v),va='center',fontsize=14.5,color=INK if c==GREY else c,fontproperties=FB)
    ax.text(-1.2,y0,sz,ha='right',va='center',fontsize=16.5,color=DEEP,fontproperties=FB,clip_on=False)
for k,nm in enumerate(names):
    c=V[nm][1]; ax.barh(nS*1.25-0.45,3.2,0.16,left=24+k*15.5,color=c); ax.text(28+k*15.5,nS*1.25-0.45,nm,va='center',fontsize=13.5,color=INK)
ax.set_xlim(0,72); ax.set_ylim(-0.6,nS*1.25-0.15); clean(ax)
finish(fig,O+'fig3.png','1만 평 넘는 자연녹지 임야는 4건, 계획관리지역 임야는 11건이라 건수가 적습니다 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
render_jisan('가평 부동산 · 가평 땅값',['가평 땅값, 같은 밭도','계획관리 52만원 · 농림 28만원'],'청평면 79만원 · 북면 33만원 · 2023~2026년 실거래',O+'thumb.png')
# ───── 2편 가평 부동산 ─────
O=OUT+'jisandream_gp_ipji_'
C5=[('남양주시',156,138),('양평군',54,600),('가평군',52,506),('포천시',41,677),('연천군',27,406)]
fig=plt.figure(figsize=(11.2,7.8)); ax=fig.add_axes([0.16,0.11,0.80,0.64])
head(fig,'계획관리지역 · 밭과 논 · 도로 붙음 · 100~1천 평 · 2023년 1월~2026년 8월','같은 조건의 밭, 가평은 양평과 비슷하고 남양주의 3분의 1입니다',fs=22.5)
n=len(C5)
for i,(nm,v,k) in enumerate(C5):
    y=n-1-i; hi=nm=='가평군'; c=DEEP if hi else CYAN
    ax.barh(y,v,0.58,color=c)
    ax.text(v+3,y,f'평당 {v}만원',va='center',fontsize=18 if hi else 16,color=c,fontproperties=FB)
    ax.text(v+3+46,y,f'{k}건',va='center',fontsize=14,color=GREY)
    ax.text(-3,y,nm,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,230); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'fig1.png','평당 값은 평균이 아니라 중앙값입니다 · 지분 거래는 뺐습니다 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
Y=list(range(2015,2026)); N=[2304,2255,2601,2470,1962,2525,3518,2534,1666,1249,1162]; PV=[39.2,41.9,43.4,42.0,39.6,43.0,50.8,53.1,52.1,53.9,51.7]
fig=plt.figure(figsize=(11.2,8.8)); ax=fig.add_axes([0.06,0.10,0.90,0.40]); ax2=fig.add_axes([0.06,0.54,0.90,0.22])
head(fig,'가평 밭 · 논 · 임야 · 대지 통째 거래 건수와 같은 조건 밭의 평당 값','값은 52만원에 멈췄고 거래는 2021년의 3분의 1입니다')
for y,v in zip(Y,N):
    hi=y in(2021,2025); c=DEEP if y==2021 else (WARM if y==2025 else '#C3CDD6')
    ax.bar(y,v,0.7,color=c); ax.text(y,v+60,f'{v:,}건' if hi else f'{v:,}',ha='center',va='bottom',fontsize=16 if hi else 13,color=c if hi else INK,fontproperties=FB if hi else FR)
ax.set_xticks(Y); ax.set_xticklabels([f"'{str(y)[2:]}" for y in Y],fontsize=14,color=INK); ax.tick_params(length=0)
ax.set_xlim(2014.4,2025.6); ax.set_ylim(0,4200); clean(ax,keepx=True); ax.spines['bottom'].set_visible(True); ax.spines['bottom'].set_color(LINE)
ax2.plot(Y,PV,color=CYAN,lw=4,marker='o',ms=9)
for y,v in zip(Y,PV):
    if y in(2019,2021,2023,2025): ax2.text(y,v+3.2,f'{round(v)}만원',ha='center',va='bottom',fontsize=15,color=DEEP,fontproperties=FB)
ax2.text(2014.5,60,'같은 조건 밭 평당 값',fontsize=13.5,color=CYAN,va='center'); ax.text(2014.5,3950,'거래 건수',fontsize=13.5,color=GREY,va='center')
ax2.set_xlim(2014.4,2025.6); ax2.set_ylim(30,64); clean(ax2)
finish(fig,O+'fig2.png','평당 값은 계획관리지역 · 도로 붙은 100~1천 평 밭과 논의 중앙값 · 국토교통부 실거래가',brand='지산드림',allow_outside=True,strict=False)
render_jisan('가평 부동산 · 가평 토지',['가평 토지, 새 길은 착공했는데','거래는 3분의 1입니다'],'제2경춘국도 2032년 목표 · 접경지역 지정 · 평당 52만원',O+'thumb.png')
print('figs ok')
