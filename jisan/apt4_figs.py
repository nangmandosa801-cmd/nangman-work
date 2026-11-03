# -*- coding: utf-8 -*-
import sys,json; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
O='/mnt/user-data/outputs/jisandream/jisandream_'
INK='#333333'; WARM='#B5761A'
S=json.load(open('/home/claude/jisan/apt4_series.json'))
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.900):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
def won(v):
    m=int(round(v*10000)); e=m//10000; r=m%10000
    return f'{e}억'+(f' {r:,}만' if r else '원')
YS=[str(y) for y in range(2018,2027)]
def line(path,main,others,title,note,marks=(2021,2023,2026)):
    fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.07,0.15,0.74,0.60])
    head(fig,'전용 84㎡ 한가운데 값 · 2018년~2026년 8월',title)
    for nm,c in others:
        v=[S[nm][0][y] for y in YS]; ax.plot(range(9),v,color=c,lw=2.5,marker='o',ms=5,zorder=2)
        fig.text(0.825,0.15+0.60*(v[-1]-lo)/(hi-lo),f'{nm} {won(v[-1])}',fontsize=14.5,color=c,fontproperties=FB,va='center')
    v=[S[main][0][y] for y in YS]; ax.plot(range(9),v,color=WARM,lw=5,marker='o',ms=9,zorder=3)
    fig.text(0.825,0.15+0.60*(v[-1]-lo)/(hi-lo),f'{main} {won(v[-1])}',fontsize=16,color=WARM,fontproperties=FB,va='center')
    for y in marks[:-1]:
        i=y-2018; up=(y==2021)
        ax.text(i,v[i]+(hi-lo)*(0.045 if up else -0.045),won(v[i]),ha='center',va='bottom' if up else 'top',fontsize=14.5,color=WARM,fontproperties=FB)
    ax.set_xlim(-0.3,8.3); ax.set_ylim(lo,hi)
    ax.set_xticks(range(9)); ax.set_xticklabels([y+'년' for y in YS],fontsize=13,color=GREY); ax.set_yticks([]); ax.tick_params(length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.axhline(lo,color=LINE,lw=1.2)
    finish(fig,path,note,brand='지산드림',allow_outside=True,strict=False)
def bars(path,rows,sub,title,note,xmax,hl=0,figh=8.6,left=0.40):
    fig=plt.figure(figsize=(11.2,figh)); ax=fig.add_axes([left,0.10,0.96-left,0.70])
    head(fig,sub,title)
    n=len(rows)
    for i,(nm,v,lab) in enumerate(rows):
        y=n-1-i; c=WARM if i==hl else DEEP
        ax.barh(y,v,0.62,color=c); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=15.5,color=c,fontproperties=FB)
        ax.text(-xmax*0.012,y,nm,ha='right',va='center',fontsize=15,color=DEEP,fontproperties=FB,clip_on=False)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); clean(ax)
    finish(fig,path,note,brand='지산드림',allow_outside=True,strict=False)
# 다산
lo,hi=3.2,10.6
line(O+'dasan_apt_fig1.png','다산',[('별내',GREY),('구리',DEEP)],'다산 84㎡ 9억 2천, 2021년 값을 넘었습니다','다산은 2023년 7억 3,400만원에서 25% 올랐습니다')
bars(O+'dasan_apt_fig2.png',[('다산자이아이비플레이스 (2021)',12.05,'12억 500만원'),('힐스테이트다산 (2018)',10.275,'10억 2,750만원'),('다산 이편한세상자이 (2018)',10.1,'10억 1,000만원'),('다산한양수자인리버팰리스 (2017)',10.055,'10억 550만원'),('다산자이폴라리스 (2021)',10.02,'10억 200만원'),('다산롯데캐슬 (2017)',9.9,'9억 9,000만원'),('e편한세상 다산 (2017)',9.6,'9억 6,000만원')],
     '다산동 단지별 전용 84㎡ · 2026년 3~8월에 팔린 값','다산 아파트, 10억 넘는 단지가 다섯 곳입니다','표에 있는 단지는 모두 1년에 9% 넘게 올랐습니다',17.5)
# 별내
lo,hi=3.6,9.0
line(O+'byeolnae_apt_fig1.png','별내',[('구리',DEEP)],'별내 84㎡ 6억 9천, 2021년보다 낮습니다','거래는 올해 가장 많은데 값은 1년에 2.4% 올랐습니다')
bars(O+'byeolnae_apt_fig2.png',[('별내자이더스타 (2023)',11.3,'11억 3,000만원'),('별내아이파크2차 (2015)',8.1,'8억 1,000만원'),('별가람역 한라비발디 (2013)',7.225,'7억 2,250만원'),('신안인스빌 (2012)',7.185,'7억 1,850만원'),('포레나별내 (2012)',7.175,'7억 1,750만원'),('별내푸르지오 (2015)',6.28,'6억 2,800만원'),('모아미래도 (2014)',6.175,'6억 1,750만원')],
     '별내동 단지별 전용 84㎡ · 2026년 3~8월에 팔린 값','별내자이더스타만 11억, 나머지는 6억에서 8억입니다','별내역에서 가까운 단지일수록 2021년보다 덜 내렸습니다',16.5)
# 구리
lo,hi=3.8,8.6
line(O+'guri8_fig1.png','구리',[],'구리 84㎡ 7억 4천, 2021년 값에 거의 돌아왔습니다','2024년 8월에 8호선이 열렸고 2026년 7월에 규제지역이 됐습니다')
bars(O+'guri8_fig2.png',[('구리역 (수택동)',19.8,'+20%'),('장자호수공원역 (교문동)',17.3,'+17%'),('동구릉역 (인창동)',12.6,'+13%'),('장자호수공원역 (토평동)',11.5,'+12%'),('갈매역 · 경춘선 (갈매동)',5.6,'+6%')],
     '구리 동네별 전용 84㎡ · 작년 3~8월과 올해 3~8월 비교','구리역 쪽 수택동이 1년에 20% 올랐습니다','구리 전체는 14% · 8호선이 없는 갈매동은 6%',26,figh=7.4,left=0.36)
# 갈매
lo,hi=4.0,9.2
line(O+'galmae_apt_fig1.png','갈매',[('별내',GREY)],'갈매 84㎡ 7억 5천, 2021년보다 7% 낮습니다','2023년 6억 5,000만원에서 15% 올랐습니다')
R=[('갈매역아이파크 (2018)',8.58,5.8),('구리갈매푸르지오 (2017)',8.075,5.4),('한라비발디 (2016)',7.6,5.45),('구리갈매스타힐스 (2017)',7.385,5.3),('갈매더샵나인힐스 (2016)',7.375,5.5),('갈매6단지 (2018)',7.295,5.5)]
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.34,0.09,0.62,0.68])
head(fig,'갈매동 단지별 전용 84㎡ · 2026년에 거래된 값','갈매 아파트, 매매 7억 3천~8억 6천 전세 5억 3천~5억 8천')
fig.text(0.34,0.815,'■ 매매',fontsize=15,color=DEEP,fontproperties=FB); fig.text(0.46,0.815,'■ 전세',fontsize=15,color=WARM,fontproperties=FB)
n=len(R)
for i,(nm,a,b) in enumerate(R):
    y=n-1-i
    ax.barh(y+0.19,a,0.34,color=DEEP); ax.barh(y-0.19,b,0.34,color=WARM)
    ax.text(a+0.12,y+0.19,won(a)+('원' if not won(a).endswith('원') else ''),va='center',fontsize=14.5,color=DEEP,fontproperties=FB)
    ax.text(b+0.12,y-0.19,won(b)+('원' if not won(b).endswith('원') else ''),va='center',fontsize=14.5,color=WARM,fontproperties=FB)
    ax.text(-0.12,y,nm,ha='right',va='center',fontsize=15,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,12.2); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'galmae_apt_fig2.png','갈매역에서 가까운 순서가 값 순서입니다',brand='지산드림',allow_outside=True,strict=False)
