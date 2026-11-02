import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'; LB='#7E97B8'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.965,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.93,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
df=pd.read_pickle('/home/claude/w/lotto_bunyang.pkl').sort_values('배율',ascending=False)
short={'미사강변푸르지오':'미사강변푸르지오','미사강변 골든 센트로':'미사 골든센트로','감일한라비발디':'감일 한라비발디','위례 래미안이편한세상':'위례 자연앤래미안','위례롯데캐슬':'위례롯데캐슬','광교중흥에스클래스':'광교 중흥S클래스','동탄역 시범한화 꿈에그린 프레스티지':'동탄역 시범 한화','동탄역롯데캐슬':'동탄역 롯데캐슬','다산 이편한세상자이':'다산 e편한세상자이','별내아이파크2차':'별내아이파크2차','고양원흥동일스위트':'원흥 동일스위트','한강신도시롯데캐슬':'김포한강 롯데캐슬','운정신도시 센트럴 푸르지오':'운정 센트럴푸르지오','고덕국제신도시파라곤':'고덕 파라곤','시흥배곧한신더휴':'배곧 한신더휴','e편한세상옥정에듀써밋':'옥정 에듀써밋'}

# fig1 배율 bar with 분양가→현재
fig=plt.figure(figsize=(11.2,12.5)); ax=fig.add_axes([0.26,0.05,0.70,0.83])
head(fig,'경기 공공택지 16개 단지 · 최초 분양가 → 2026년 3~8월 전용 84㎡ 실거래 중앙값','로또 청약 검증, 미사·동탄역·위례는 4배인데 고덕·옥정·김포는 1.6배입니다')
n=len(df)
for i,(_,r) in enumerate(df.iterrows()):
    y=n-1-i; v=r['배율']; c=NAVY if v>=2.9 else (MID if v>=2.0 else WARN)
    ax.barh(y,v,0.62,color=c)
    ax.text(v+0.05,y,f"{v:.2f}배 · {r['분양가']:.2f}억 → {r['현재84']:.2f}억",va='center',fontsize=12.5,color=c,fontweight='bold')
    ax.text(-0.08,y,short[r['단지']]+f" ({int(r['분양'])})",ha='right',va='center',fontsize=12.5,color=NAVY,fontweight='bold',clip_on=False)
ax.axvline(1,color=LINE,lw=1.2)
ax.set_xlim(0,6.3); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'lotto16_fig1.png','진한 파랑 = 2.9배 이상(연 10% 넘음) · 주황 = 2배 미만(경기 평균 수준) · 분양가는 당시 보도 기준, 확장비 제외',allow_outside=True,strict=False)

# fig2 경쟁률 vs 배율
pts=[('동탄역 롯데캐슬',77.5,4.04),('고덕 파라곤',49,1.59),('광교 중흥S클래스',38.9,2.99),('감일 한라비발디',14.1,2.93),('다산 e편한세상자이',9.4,3.16),('위례 자연앤래미안',4.1,4.01),('동탄역 시범 한화',3.0,4.04),('옥정 에듀써밋',1.6,1.65),('배곧 한신더휴',1.6,2.10),('위례롯데캐슬',1.08,3.64),('운정 센트럴푸르지오',0.8,1.94)]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.08,0.12,0.88,0.70])
head(fig,'가로: 청약 경쟁률(로그) · 세로: 분양가 대비 올해 배율 · 경쟁률 수치가 있는 11곳','경쟁률 49대 1이 꼴찌이고 84㎡ 미달 단지가 5위입니다')
for nm,c_,v in pts:
    x=np.log10(max(c_,0.8)); col=NAVY if v>=2.9 else (MID if v>=2 else WARN)
    ax.plot(x,v,'o',ms=13,color=col)
    dx,dy,ha=0.04,0,'left'
    if nm in ('동탄역 시범 한화',): dy=0.18
    if nm in ('위례 자연앤래미안',): dy=-0.18
    if nm in ('배곧 한신더휴',): dy=0.2
    if nm in ('옥정 에듀써밋',): dy=-0.2
    if nm in ('운정 센트럴푸르지오',): dy=0.12
    if nm in ('동탄역 롯데캐슬','고덕 파라곤'): dx,ha=-0.04,'right'
    ax.text(x+dx,v+dy,f'{nm} ({c_:g}:1)' if c_>=1 else f'{nm} (미달)',ha=ha,va='center',fontsize=12,color=col,fontweight='bold')
for t,lab in [(1,'1:1'),(10,'10:1'),(100,'100:1')]:
    ax.axvline(np.log10(t),color=LINE,lw=1,ls='--'); ax.text(np.log10(t),1.1,lab,ha='center',va='top',fontsize=12,color=MID)
ax.set_xlim(-0.25,2.2); ax.set_ylim(1.0,4.6); clean(ax)
ax.text(-0.22,4.5,'배율',fontsize=12,color=MID,va='top')
finish(fig,O+'lotto16_fig2.png','경쟁률은 당시 보도 · 위례롯데캐슬은 84㎡ 1순위 미달(0.63~0.88:1) · 운정은 2순위 미달 · 경쟁률과 결과 배율 사이에 관계가 없음',allow_outside=True,strict=False)

render('로또 청약 검증',['경기 공공택지 16곳 10년','미사 4.1배 · 고덕 1.6배'],'경쟁률 49대 1이 꼴찌 · 차이는 서울까지 30분이냐 1시간이냐',O+'lotto16_thumb.png')
print('ok')
