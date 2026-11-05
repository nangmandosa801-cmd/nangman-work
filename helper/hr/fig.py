import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_jijeharrington_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 풍경채어바니티 84㎡ 전세 달별 중앙값
M=[('2월',25000,4),('3월',25000,19),('4월',25000,19),('5월',26000,7),('6월',25000,13),('7월',26000,5)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평택 가재동 지제역반도체밸리풍경채어바니티 · 84㎡ 전세 달별 중앙값(2026년)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'입주 뒤 여섯 달, 전세는 2억 5천~2억 6천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
xs=range(len(M)); cols=[NAVY if n>=10 else BLUE for _,_,n in M]
ax.bar(xs,[v for _,v,_ in M],color=cols,width=0.6)
for x,(m,v,n) in zip(xs,M):
    ax.text(x,v+300,won(v),ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(x,800,f'{n}건',ha='center',fontsize=13,color='white')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_,_ in M],fontsize=16,color='#333')
ax.set_ylim(0,30000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 2~7월 계약 · 전용 84㎡ · 월세 없는 계약 중앙값) · 1월 1건 · 8~10월 4건은 뺌',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_urbanity.png'); plt.close()
# 2 84㎡ 분양권 · 매매 · 전세
R=[('지제역 주변 아파트 15곳\n84㎡ 매매',58000,GRAY),('해링턴플레이스\n84㎡ 분양권',47934,NAVY),('쌍용 더 플래티넘\n84㎡ 분양권',46440,GRAY),('풍경채어바니티\n84㎡ 분양권',44580,GRAY),('지제역 주변 아파트 15곳\n84㎡ 전세',28000,BLUE),('풍경채어바니티\n84㎡ 전세',25000,BLUE)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'지제역 반도체밸리 해링턴플레이스와 지제역 주변 · 84㎡ 2026년 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'분양권 4억 7,934만, 옆 단지 전세 2억 5천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.66,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+600,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,70000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 분양권 · 아파트 매매 · 전월세 실거래(2026년 1~11월 · 전용 80~86㎡ · 해제 거래 뺌 · 전세는 월세 없는 계약)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}2_compare.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 가재동 · 2027년 2월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,345),'지제역 반도체밸리',font=kr(ser,66),fill='#F4F1EA',anchor='mm')
d.text((W/2,435),'해링턴플레이스',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,530),'옆 단지 84㎡ 전세',font=kr(ser,54),fill='#F4F1EA',anchor='mm')
d.text((W/2,640),'2억 5천',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,735),'풍경채어바니티 · 올해 72건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')
