import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 미사 84㎡ 월별 매매 중앙값 2021.01~2026.10
mm=json.load(open('monthly.json'))
xs=list(range(len(mm))); ys=[r['median']/10000 for r in mm]; lab=[str(r['ym']) for r in mm]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'미사 집값 · 84㎡ 매매 중앙값, 2021년 1월~2026년 10월(월별)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'고점 11억 2,200만 → 바닥 7억 9,000만 → 올해 12억 5,350만',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.88,0.64])
ax.plot(xs,ys,color=NAVY,lw=2.6)
ax.fill_between(xs,ys,6,color='#EEF2F7')
ax.set_ylim(6,14); ax.set_xlim(-1,len(xs))
ticks=[i for i,r in enumerate(mm) if r['ym']%100==1]
ax.set_xticks(ticks); ax.set_xticklabels([f"{r['ym']//100}년" for r in mm if r['ym']%100==1],fontsize=13,color='#555')
ax.set_yticks([6,8,10,12,14]); ax.set_yticklabels(['6억','8억','10억','12억','14억'],fontsize=13,color='#555')
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
def mark(ym,txt,dy,ha='center'):
    i=[k for k,r in enumerate(mm) if r['ym']==ym][0]; v=ys[i]
    ax.scatter([i],[v],s=120,color=BLUE,zorder=4)
    ax.text(i,v+dy,txt,fontsize=14,color=NAVY,fontweight='bold',ha=ha,va='bottom' if dy>0 else 'top')
mark(202106,'2021년 6월\n11억 2,200만',0.5)
mark(202212,'2022년 12월\n7억 9,000만',-0.5)
mark(202608,'2026년 8월\n12억 5,350만',0.45,'right')
ax.axhline(10.8,color=GRAY,lw=1.2,ls='--'); ax.text(len(xs)-1,10.85,'2021년 하반기 중앙값 10억 8,000만',fontsize=12.5,color='#7A8590',ha='right',va='bottom')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2021년 1월~2026년 10월 계약 · 하남 망월동 · 풍산동 · 선동 전용 83~86㎡ · 해제 · 직거래 뺌 · 달마다 중앙값)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa_peak_1_monthly.png'); plt.close()

# 2. 20개 단지: 2021년 하반기 고점 거래 대비 2026년 중앙값
T=json.load(open('track.json')); T=sorted(T,key=lambda r:r['pct26'])
short={'미사강변푸르지오':'미사강변푸르지오','미사강변센트럴풍경채':'센트럴풍경채','미사강변 골든 센트로':'골든 센트로','미사강변더샵센트럴포레':'더샵센트럴포레','신안인스빌':'신안인스빌','미사강변 하우스디 더 레이크':'하우스디 더 레이크','미사강변루나리움':'루나리움','미사강변 센트리버':'센트리버(선동)','이편한세상미사':'이편한세상미사','리버나인RIVERNINE':'리버나인(선동)','미사강변동원로얄듀크':'동원로얄듀크','미사강변스타힐스아파트':'스타힐스','미사강변파밀리에':'파밀리에','미사레스티아':'미사레스티아','미사강변 파크뷰':'파크뷰','미사강변 센텀팰리스':'센텀팰리스','미사강변동일하이빌':'동일하이빌','미사강변도시 베라체':'베라체(선동)','미사강변한신휴플러스':'한신휴플러스','하남힐즈파크푸르지오2단지':'힐즈파크푸르지오2'}
fig=plt.figure(figsize=(11.55,10.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'미사 집값 · 2021년 하반기 고점 거래와 2026년 84㎡ 중앙값(20개 단지)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.928,'20곳 중 17곳은 올해 중앙값이 고점 거래보다 높습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.08,0.66,0.8])
ys=list(range(len(T))); vals=[r['pct26'] for r in T]; cols=[NAVY if v>=0 else GRAY for v in vals]
ax.barh(ys,vals,color=cols,height=0.72)
ax.set_yticks(ys); ax.set_yticklabels([f"{short[r['cx']]}\n고점 {r['pk']//10000}억 {r['pk']%10000:,}만".replace(' 0만','') for r in T],fontsize=12.5,color='#333')
for y,v in zip(ys,vals): ax.text(v+(0.3 if v>=0 else -0.3),y,f'{v:+.1f}%',va='center',ha='left' if v>=0 else 'right',fontsize=13.5,color=NAVY if v>=0 else '#555',fontweight='bold')
ax.axvline(0,color=NAVY,lw=1.2); ax.set_xlim(-12,18); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_visible(False)
fig.text(0.045,0.04,'고점 = 그 단지 84㎡의 2021년 7~12월 가장 높은 거래 금액 · 비율 = 2026년 1~10월 중앙값 ÷ 고점 − 1 · 회색 = 아직 고점 아래',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.017,'국토교통부 아파트 매매 실거래(하남 망월동 · 풍산동 · 선동 전용 83~86㎡ · 해제 · 직거래 뺌 · 단지 이름은 줄여 씀)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa_peak_2_cx.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 미사 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'미사 집값',font=kr(ser,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'2021년 고점에 산 84㎡',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'20곳 중 17곳 고점 위',font=kr(ser,74),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'13억 9천에 산 집은 2024년 6월에 본전',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa_peak_thumb.png')
