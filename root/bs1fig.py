import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_bosang1_'
render('낭만 부동산 분석 플랫폼 · 토지보상',['토지수용 절차,','보상금 먼저 받고 다툴 수 있습니다'],'9단계와 기한 · 공탁금은 이의 유보하고 수령',O+'thumb.png')
GREY='#C9C3B6'
def box(ax,x,y,w,h,fc,title,sub=None,tc='white',fs=16,ss=12.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.06',fc=fc,ec=fc,lw=2))
    if sub:
        ax.text(x+w/2,y+h*0.64,title,ha='center',va='center',fontsize=fs,fontweight='bold',color=tc)
        ax.text(x+w/2,y+h*0.27,sub,ha='center',va='center',fontsize=ss,color=tc)
    else: ax.text(x+w/2,y+h/2,title,ha='center',va='center',fontsize=fs,fontweight='bold',color=tc)
def arr(ax,x1,y1,x2,y2,c):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>,head_width=0.25,head_length=0.5',color=c,lw=2.2))
# fig1: 9단계 (3줄 × 3칸, ㄹ자)
S=[('1. 사업인정','고시일이 기준일',False),('2. 토지·물건 조사','빠진 물건 확인',False),('3. 보상계획 공고','열람 14일 이상',False),
   ('4. 감정평가','2~4곳 평균',True),('5. 보상금 통지·협의','30일 이상',False),('6. 수용재결','위원회가 금액 결정',True),
   ('7. 지급·공탁','이의 유보하고 수령',False),('8. 이의신청','재결서 받고 30일',True),('9. 행정소송','90일 · 이의재결 뒤 60일',False)]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.03,0.06,0.94,0.76]); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,7)
fig.text(0.04,0.955,'토지보상 절차 · 공고 우편부터 행정소송까지',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'9단계 중 다투는 곳은 감정평가 · 수용재결 · 이의신청',fontsize=23,color=NAVY,fontweight='bold',va='center')
W,Hh=2.8,1.45; xs=[0.3,3.6,6.9]; ys=[5.1,2.9,0.7]
pos=[]
for r in range(3):
    order=[0,1,2] if r%2==0 else [2,1,0]
    for c in order: pos.append((xs[c],ys[r]))
for i,((t,s,k),(x,y)) in enumerate(zip(S,pos)):
    box(ax,x,y,W,Hh,WARN if k else (NAVY if i!=4 else MID),t,s)
for i in range(8):
    (x1,y1),(x2,y2)=pos[i],pos[i+1]
    if y1==y2:
        if x2>x1: arr(ax,x1+W+0.03,y1+Hh/2,x2-0.03,y2+Hh/2,LINE)
        else: arr(ax,x1-0.03,y1+Hh/2,x2+W+0.03,y2+Hh/2,LINE)
    else: arr(ax,x1+W/2,y1-0.03,x2+W/2,y2+Hh+0.03,LINE)
ax.text(5.0,4.72,'5번에서 계약하면 그 뒤로는 다투기 어렵습니다',ha='center',fontsize=14,color=MID,fontweight='bold')
finish(fig,O+'fig1.png','붉은 칸이 보상금을 다투는 단계 · 기한은 모두 서류를 받은 날부터 셉니다',allow_outside=True,strict=False)
# fig2: 감정평가 구조
fig=plt.figure(figsize=(11.2,8.0)); ax=fig.add_axes([0.03,0.06,0.94,0.76]); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,6.4)
fig.text(0.04,0.955,'토지보상 감정평가 · 누가 감정평가법인을 고르나',fontsize=17,color=MID,va='center')
fig.text(0.04,0.900,'최대 4곳 중 1곳은 땅 주인이 추천합니다',fontsize=23,color=NAVY,fontweight='bold',va='center')
cols=[('사업시행자','2곳 · 기본',NAVY,[0.2,1.75]),('시·도지사','1곳 · 추천할 때',MID,[3.5]),('토지소유자','1곳 · 조건 채우면',WARN,[6.6])]
for name,sub,c,xs_ in cols:
    for x in xs_:
        box(ax,x,3.6,1.45 if len(xs_)>1 else 2.9,1.5,c,'감정평가법인',None,fs=15)
    x0=xs_[0]; x1=xs_[-1]+(1.45 if len(xs_)>1 else 2.9)
    ax.text((x0+x1)/2,5.62,name,ha='center',fontsize=19,color=c,fontweight='bold'); ax.text((x0+x1)/2,5.25,sub,ha='center',fontsize=13.5,color=MID)
    for x in xs_:
        cx=x+(0.725 if len(xs_)>1 else 1.45); arr(ax,cx,3.55,5.0,2.25,LINE)
box(ax,3.2,1.0,3.6,1.2,NAVY,'보상액 = 평가 금액의 평균',None,fs=18)
ax.text(8.05,2.9,'땅 면적 절반 이상 소유자\n+ 소유자 수 절반 이상 동의',ha='center',va='center',fontsize=13.5,color=WARN,fontweight='bold')
finish(fig,O+'fig2.png','소유자 추천 1곳이 들어가면 적어도 한 곳은 소유자 쪽 자료를 꼼꼼히 봅니다',allow_outside=True,strict=False)
