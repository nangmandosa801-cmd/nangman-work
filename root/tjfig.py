import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patches as mp
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_tojideung_'
TXT='#444'; OK='#3C7A5A'; GREY='#B8B2A6'
render('낭만 부동산 분석 플랫폼 · 부동산공법',['토지등소유자 뜻,','재개발은 또는, 재건축은 그리고'],'땅이나 건물 · 건물과 땅을 함께',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def canvas(h=6.4,yl=5.2):
    fig=plt.figure(figsize=(11.2,h)); ax=fig.add_axes([0,0.09,1,0.77]); ax.set_xlim(0,11.2); ax.set_ylim(0,yl); ax.axis('off'); return fig,ax
def land(ax,x,y,w,c): ax.add_patch(mp.Rectangle((x,y),w,0.15,fc=c,ec='none'))
def bld(ax,x,y,c): ax.add_patch(mp.Polygon([[x,y],[x+0.6,y],[x+0.6,y+0.38],[x+0.3,y+0.6],[x,y+0.38]],fc=c,ec='white',lw=1.2))
# fig1
fig,ax=canvas(6.6,5.4)
head(fig,'토지등소유자 뜻 · 누가 들어가나','재개발은 「또는」, 재건축은 「그리고」입니다')
cases=[('땅만 가진 사람','land'),('건물만 가진 사람','bld'),('땅의 지상권자','sup'),('건물과 땅을 함께','both')]
ax.text(6.2,4.85,'재개발 · 주거환경개선',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.text(9.1,4.85,'재건축',ha='center',fontsize=15,color=WARN,fontweight='bold')
for i,(t,k) in enumerate(cases):
    y=3.85-i*1.05
    x=0.5
    if k in('land','both','sup'): land(ax,x+2.6,y+0.08,1.2,'#C9B89A')
    if k=='both': bld(ax,x+2.9,y+0.23,MID)
    if k=='bld': bld(ax,x+2.9,y+0.08,MID)
    if k=='sup': ax.add_patch(mp.Polygon([[x+2.9,y+0.23],[x+3.5,y+0.23],[x+3.5,y+0.61],[x+3.2,y+0.83],[x+2.9,y+0.61]],fc='none',ec=MID,lw=1.5,ls='--'))
    ax.text(x,y+0.4,t,fontsize=14,color=TXT,va='center')
    for cx,ok in [(6.2,True),(9.1,k=='both')]:
        ax.text(cx,y+0.4,'O' if ok else 'X',ha='center',va='center',fontsize=24,fontweight='bold',color=(NAVY if cx<7 else WARN) if ok else GREY)
    ax.plot([0.4,10.8],[y-0.12,y-0.12],color=LINE,lw=1)
finish(fig,O+'fig1.png','시험 함정 · 재건축에는 지상권자가 들어가지 않습니다',allow_outside=True,strict=False)

# fig2 사람을 센다
fig,ax=canvas(6.6,5.4)
head(fig,'토지등소유자 뜻 · 머릿수 세는 법','집이 아니라 사람을 셉니다')
groups=[('갑 · 을','집 1채를 반씩',1,1),('병','집 3채',3,1),('정','땅만',0,1),('무','그 땅 위 건물만',1,1),('기 · 경','땅 · 지상권',0,1),('국공유지','관리기관',0,1)]
for i,(n,d,houses,cnt) in enumerate(groups):
    x=0.35+i*1.8
    ax.add_patch(mp.FancyBboxPatch((x,1.05),1.6,3.3,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#F7F5F0',ec=LINE,lw=1.5))
    ax.text(x+0.8,4.0,n,ha='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(x+0.8,3.6,d,ha='center',fontsize=11.5,color=TXT)
    if houses:
        for j in range(houses):
            s=0.42
            px=x+0.8-(houses*0.5)/2+j*0.5
            ax.add_patch(mp.Polygon([[px,2.3],[px+s,2.3],[px+s,2.62],[px+s/2,2.85],[px,2.62]],fc=MID,ec='white'))
    else:
        ax.add_patch(mp.Rectangle((x+0.35,2.35),0.9,0.22,fc='#C9B89A'))
    ax.add_patch(mp.Circle((x+0.8,1.55),0.32,fc=WARN))
    ax.text(x+0.8,1.55,'1',ha='center',va='center',fontsize=17,color='white',fontweight='bold')
ax.text(5.6,0.55,'집은 여섯 채가 넘지만 토지등소유자는 6명',ha='center',fontsize=16,color=WARN,fontweight='bold')
finish(fig,O+'fig2.png','공유는 대표 1명 · 여러 채도 1명 · 땅과 지상권은 대표 1명',allow_outside=True,strict=False)

# fig3 토지등소유자 vs 조합원
fig,ax=canvas(6.2,5.0)
head(fig,'토지등소유자 뜻 · 조합원과 다른 점','부부는 토지등소유자 2명, 조합원 1명입니다')
def person(x,y,c):
    ax.add_patch(mp.Circle((x,y+0.55),0.18,fc=c)); ax.add_patch(mp.FancyBboxPatch((x-0.25,y),0.5,0.35,boxstyle='round,pad=0.02,rounding_size=0.12',fc=c,ec='none'))
ax.add_patch(mp.FancyBboxPatch((0.5,1.2),3.4,2.7,boxstyle='round,pad=0.02,rounding_size=0.1',fc='#F7F5F0',ec=LINE))
ax.text(2.2,3.55,'한 세대 (부부)',ha='center',fontsize=15,color=NAVY,fontweight='bold')
person(1.55,2.2,MID); person(2.85,2.2,MID)
for x in [1.3,2.6]: ax.add_patch(mp.Polygon([[x,1.5],[x+0.5,1.5],[x+0.5,1.8],[x+0.25,2.0],[x,1.8]],fc='#C9B89A',ec='white'))
ax.text(2.2,0.85,'각자 집 한 채씩',ha='center',fontsize=13,color=TXT)
for y,t,n,c,s in [(3.1,'토지등소유자 수','2명',NAVY,'동의율을 셀 때 · 두 사람 모두 동의서'),(1.6,'조합원 수','1명',WARN,'새 아파트 받을 사람 · 한 세대는 1명')]:
    ax.annotate('',xy=(5.2,y+0.25),xytext=(4.0,2.55),arrowprops=dict(arrowstyle='-|>',color=c,lw=2.2,mutation_scale=20))
    ax.text(5.35,y+0.4,t,fontsize=15,color=c,fontweight='bold'); ax.text(8.2,y+0.4,n,fontsize=26,color=c,fontweight='bold')
    ax.text(5.35,y-0.05,s,fontsize=12.5,color=TXT)
finish(fig,O+'fig3.png','같은 세대라도 동의율을 셀 때는 사람마다 따로 셉니다',allow_outside=True,strict=False)

# fig4 신탁
fig,ax=canvas(6.0,4.8)
head(fig,'토지등소유자 뜻 · 신탁 방식','신탁을 맡겨도 토지등소유자는 원래 주인입니다')
def bx(x,y,w,h,t,fc,tc='white',fs=15,ec=None):
    ax.add_patch(mp.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.1',fc=fc,ec=ec or fc,lw=2))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=tc,fontweight='bold',linespacing=1.4)
bx(0.5,1.6,2.8,1.4,'주민 수백 명\n(원래 주인)',MID)
bx(7.9,1.6,2.8,1.4,'신탁회사\n(사업시행자)',NAVY)
ax.annotate('',xy=(7.85,2.3),xytext=(3.35,2.3),arrowprops=dict(arrowstyle='-|>',color='#8A8578',lw=2.5,mutation_scale=22))
ax.text(5.6,2.55,'땅 · 건물을 맡김 (등기 이전)',ha='center',fontsize=13,color=TXT)
ax.text(1.9,1.1,'토지등소유자로 봄',ha='center',fontsize=15,color=OK,fontweight='bold')
ax.text(9.3,1.1,'1명으로 세지 않음',ha='center',fontsize=15,color='#8A8578',fontweight='bold')
ax.text(5.6,3.7,'신탁회사를 1명으로 세면 수백 명의 동의가 한 표가 됩니다',ha='center',fontsize=13.5,color=WARN)
finish(fig,O+'fig4.png','평촌 귀인 · 민백블록은 2026년 4월 신탁회사를 사업시행자로 지정했습니다',allow_outside=True,strict=False)
