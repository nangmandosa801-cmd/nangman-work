import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from viz import NAVY, MID, SAND, WARN, LINE
from note import finish
from thumbnail import render
O='/mnt/user-data/outputs/nangman_new/nangman_lotto_dongtan_gwanggyo_'
TXT='#444'; OK='#3C7A5A'; GREY='#C9C4BA'
render('낭만 부동산 분석 플랫폼 · 로또분양 1편',['동탄 광교 집값 비교,','분양가 4억이 19억'],'동탄은 8년 반, 광교는 16년 반 걸렸습니다',O+'thumb.png')
def head(fig,a,b):
    fig.text(0.04,0.955,a,fontsize=14,color=MID,va='center')
    fig.text(0.04,0.9,b,fontsize=19,color=NAVY,fontweight='bold',va='center')
def clean(ax):
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(LINE); ax.set_yticks([])
# fig1
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.06,0.18,0.9,0.6])
head(fig,'동탄 광교 집값 비교 · 84㎡ 분양가와 2026년 평균 거래 가격','동탄역 롯데캐슬과 광교 자연앤힐스테이트, 분양가도 지금 가격도 비슷합니다')
X=[0,1,3,4]; V=[4.82,19.04,4.0,18.59]; C=[GREY,NAVY,GREY,OK]
L=['분양가\n(2017.12)','2026년','분양가\n(2009.12)','2026년']
for x,v,c in zip(X,V,C):
    ax.bar(x,v,0.7,color=c); ax.text(x,v+0.4,('약 4억' if v==4.0 else f'{v:.2f}억'),ha='center',fontsize=15,fontweight='bold',color=c if c!=GREY else SAND)
ax.set_xticks(X); ax.set_xticklabels(L,fontsize=13,color=TXT); ax.set_ylim(0,23)
ax.text(0.5,21.8,'동탄역 롯데캐슬 · 8년 반 · 4.0배',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.text(3.5,21.8,'광교 자연앤힐스테이트 · 16년 반 · 4.6배',ha='center',fontsize=15,color=OK,fontweight='bold')
clean(ax)
finish(fig,O+'fig1.png','분양가 최고값 기준 · 자연앤힐스테이트 분양가는 3.3㎡당 1,178만원 × 공급면적 계산값',allow_outside=True,strict=False)
# fig2 years since sale
fig=plt.figure(figsize=(11.2,6.4)); ax=fig.add_axes([0.08,0.18,0.86,0.6])
head(fig,'동탄 광교 집값 비교 · 분양 후 몇 년 만에 몇 억이 됐나','동탄역 롯데캐슬은 8년 반, 자연앤힐스테이트는 16년 반 만에 19억 안팎')
lt=[(0,4.82),(2023.5-2017.96,15.0),(2024.5-2017.96,15.5),(2025.5-2017.96,16.18),(2026.4-2017.96,19.04)]
jy={2013:4.98,2014:5.59,2015:6.27,2016:6.77,2017:7.02,2018:9.18,2019:10.24,2020:13.06,2021:15.01,2022:13.43,2023:13.03,2024:14.28,2025:15.96}
jt=[(0,4.0)]+[(y+0.5-2009.96,v) for y,v in jy.items()]+[(2026.4-2009.96,18.59)]
for pts,c,n in [(jt,OK,'광교 자연앤힐스테이트 (2009.12 분양)'),(lt,NAVY,'동탄역 롯데캐슬 (2017.12 분양)')]:
    xs,ys=zip(*pts); ax.plot(xs,ys,color=c,lw=3,marker='o',ms=6,label=n)
    ax.text(xs[-1]+0.2,ys[-1],f'{ys[-1]:.2f}억',fontsize=14,color=c,fontweight='bold',va='center')
ax.axvline(8.44,color=NAVY,ls=':',lw=1.2); ax.text(8.44,1.2,'8년 반',ha='center',fontsize=13,color=NAVY,backgroundcolor='white')
ax.set_xlim(-0.5,18.6); ax.set_ylim(0,21); ax.set_xticks(range(0,19,2)); ax.set_xticklabels([f'{i}년' for i in range(0,19,2)],fontsize=12,color=TXT)
ax.set_yticks([0,5,10,15,20]); ax.set_yticklabels(['0','5억','10억','15억','20억'],fontsize=12,color=TXT)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color(LINE)
ax.legend(loc='upper left',fontsize=13,frameon=False)
finish(fig,O+'fig2.png','가로축은 분양 후 지난 햇수 · 점은 해마다 84㎡ 평균 거래 가격 (첫 점은 분양가)',allow_outside=True,strict=False)
# fig3 slope
fig=plt.figure(figsize=(11.2,6.0)); ax=fig.add_axes([0.33,0.16,0.44,0.62])
head(fig,'동탄 광교 집값 비교 · 최근 3년 같은 평형 거래 가격','2023년 뒤로는 광교 자연앤힐스테이트가 더 올랐습니다')
for a,b,c,n,r in [(13.03,18.64,OK,'광교 자연앤힐스테이트','43.3%'),(14.96,19.12,NAVY,'동탄역 롯데캐슬','27.9%')]:
    ax.plot([0,1],[a,b],color=c,lw=4,marker='o',ms=10)
    ax.text(-0.04,a,f'{n} {a:.2f}억',ha='right',va='center',fontsize=14,color=c,fontweight='bold')
    ax.text(1.04,b+(0.35 if c==NAVY else -0.35),f'{b:.2f}억  +{r}',ha='left',va='center',fontsize=15,color=c,fontweight='bold')
ax.set_xlim(-0.05,1.05); ax.set_ylim(12,20.5); ax.axis('off')
ax.text(0,12.2,'2023년',ha='center',fontsize=14,color=TXT); ax.text(1,12.2,'2026년',ha='center',fontsize=14,color=TXT)
finish(fig,O+'fig3.png','같은 단지 안에서 전용면적이 같은 평형끼리 짝지은 평균 · 2026년은 8월 계약까지',allow_outside=True,strict=False)
