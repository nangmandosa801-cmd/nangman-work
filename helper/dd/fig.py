import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 시도별 84㎡ 단지 중 중앙값 6억 이하
R=[('서울',92,1603),('경기',1906,2933),('인천',444,553)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'신혼부부 디딤돌대출 · 주택가격 6억 이하 84㎡ 단지 수',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'수도권 2,442곳, 서울은 92곳',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.13,0.13,0.8,0.64])
ys=[2,1,0]
ax.barh(ys,[t for _,_,t in R],color=GRAY,height=0.58,label='올해 84㎡ 거래 3건 이상 단지')
ax.barh(ys,[v for _,v,_ in R],color=NAVY,height=0.58,label='그중 중앙값 6억 이하')
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=19,color='#333')
for y,(_,v,t) in zip(ys,R):
    ax.text(t+40,y,f'{v:,}곳 / {t:,}곳 ({v/t*100:.0f}%)',va='center',fontsize=17,color=NAVY,fontweight='bold')
ax.set_xlim(0,4300); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.legend(loc='lower right',fontsize=14,frameon=False)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 · 해제 거래 뺌) · 전용 84~85㎡ · 같은 단지 거래 3건 이상 · 단지별 중앙값',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_didim_1_count.png'); plt.close()
# 2. 집값별 대출 3억 2천과 내 돈
P=[(40000,28000),(50000,32000),(56000,32000),(60000,32000)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'신혼부부 디딤돌대출 한도 · 수도권 집 기준(LTV 70% · 한도 3억 2천)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'6억 집은 내 돈 2억 8천이 듭니다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.13,0.86,0.62])
xs=range(len(P))
ax.bar(xs,[l for _,l in P],color=NAVY,width=0.56,label='디딤돌 대출')
ax.bar(xs,[p-l for p,l in P],bottom=[l for _,l in P],color=GRAY,width=0.56,label='내 돈')
def won(v): return f'{v//10000}억 {v%10000:,}만'.replace(' 0만','') if v%10000 else f'{v//10000}억'
for x,(p,l) in zip(xs,P):
    ax.text(x,l/2,won(l),ha='center',va='center',fontsize=16,color='white',fontweight='bold')
    ax.text(x,l+(p-l)/2,won(p-l),ha='center',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xticks(list(xs)); ax.set_xticklabels([f'집값 {won(p)}' for p,_ in P],fontsize=16,color='#333')
ax.set_ylim(0,66000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=14,frameon=False)
fig.text(0.045,0.03,'서울시 주거포털 신혼부부전용 구입자금 안내 · 헤럴드경제(2026년 6월 24일) · 집값은 은행이 보는 평가액 기준 · 취득세 · 이사비는 뺌',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_didim_2_cash.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 수도권 84㎡ · 2026년 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'신혼부부 디딤돌대출',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'6억 이하 84㎡',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'2,442곳',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'그중 서울은 92곳',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_didim_thumb.png')
