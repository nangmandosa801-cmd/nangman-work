import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_'
GREY='#C9C3B6'
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ['top','right','left','bottom']: ax.spines[sp].set_visible(False)
def head(fig,sub,title):
    fig.text(0.04,0.955,sub,fontsize=16,color=MID,va='center'); fig.text(0.04,0.905,title,fontsize=23,color=NAVY,fontweight='bold',va='center')
def pmt(P,r,n=360): m=r/12; return P*m/(1-(1+m)**-n)
rates=[3.5,4.0,4.66,5.0,5.5,6.0]
fig=plt.figure(figsize=(11.2,8.4)); ax=fig.add_axes([0.09,0.14,0.86,0.64])
head(fig,'30년 원리금 균등 · 거치 없음 · 금리별 월 상환액','주담대 월 상환액, 4억 빌리면 0.25%포인트마다 6만원씩 늘어납니다')
for P,c,lab in [(6,NAVY,'6억'),(4,MID,'4억'),(3,'#7E97B8','3억'),(2,GREY,'2억')]:
    v=[pmt(P*1e8,r/100)/1e4 for r in rates]; ax.plot(rates,v,color=c,lw=3,marker='o',ms=7)
    ax.text(6.08,v[-1],f'{lab} · {v[-1]:.0f}만원',va='center',fontsize=14.5,color=c,fontweight='bold')
    ax.text(4.78,v[2]-4,f'{v[2]:.0f}만',ha='left',va='top',fontsize=13,color=c,fontweight='bold')
ax.axvline(4.66,color=WARN,lw=2,ls='--'); ax.text(4.60,378,'지금 4.66%',ha='right',fontsize=14,color=WARN,fontweight='bold')
for r in rates: ax.text(r,55,f'{r}%',ha='center',va='top',fontsize=13.5,color=MID)
ax.set_xlim(3.3,6.6); ax.set_ylim(40,390); clean(ax)
finish(fig,O+'rate10_fig1.png','한국은행 8월 신규취급액 주담대 평균 4.66% 기준 · 개인 금리는 은행·신용에 따라 다릅니다',allow_outside=True,strict=False)
# fig2
R=[('과천',23.35,4.0),('성남 분당구',18.0,4.0),('하남',11.68,4.67),('용인 수지구',10.27,4.11),('광명',9.10,3.64),('안양 동안구',9.05,3.62),('의왕',7.90,3.16),('수원 영통구',7.88,3.15)]
fig=plt.figure(figsize=(11.2,9.0)); ax=fig.add_axes([0.20,0.10,0.74,0.72])
head(fig,'경기 규제지역 84㎡ 중간값(2026년 4~8월) · LTV 40%와 구간 한도(15억 초과 4억) 적용','주담대 한도, 하남 84㎡는 4억 7천 빌리고 7억은 현금입니다')
n=len(R)
for i,(nm,p,l) in enumerate(R):
    y=n-1-i; ax.barh(y,p,0.6,color=GREY); ax.barh(y,l,0.6,color=NAVY)
    ax.text(l/2,y,f'대출 {l:.1f}억',ha='center',va='center',fontsize=12.5,color='white',fontweight='bold')
    ax.text(p+0.25,y,f'집값 {p:.1f}억 · 현금 {p-l:.1f}억',va='center',fontsize=14,color=NAVY,fontweight='bold')
    ax.text(-0.3,y,nm,ha='right',va='center',fontsize=15,color=NAVY,fontweight='bold',clip_on=False)
ax.set_xlim(0,32); ax.set_ylim(-0.6,n-0.4); clean(ax)
finish(fig,O+'rate10_fig2.png','15억 넘는 집은 LTV 40%가 4억을 넘어도 4억까지 · 국토교통부 아파트 실거래 · 10·15 대책 기준',allow_outside=True,strict=False)
render('기준금리 발표일',['10월 22일 기준금리 발표','4억 대출 0.25%포인트에 월 6만원'],'주담대 4.66% · 규제지역은 금리보다 한도 40%가 먼저',O+'rate10_thumb.png')
print('ok')
