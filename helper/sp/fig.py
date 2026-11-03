import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'

# 1. 공구별 길이 · 시공사
R=[('2공구\n감일동~항동',4.79,'남광토건 컨소시엄 96.13점 (대보 88.93점)',NAVY),
   ('3공구\n감일동~교산동',1.70,'금광기업',GRAY),
   ('4공구\n교산동~신장동',4.30,'극동건설',GRAY)]
fig=plt.figure(figsize=(11.55,7.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송파하남선 2공구 · 경기도가 맡은 하남 구간 세 공구',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'감일 구간 2공구가 4.79km로 가장 깁니다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.20,0.16,0.74,0.62])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.56)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=16,color='#333')
for y,(_,v,who,c) in zip(ys,R):
    ax.text(v+0.08,y+0.06,f'{v:.2f}km',va='bottom',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(v+0.08,y-0.06,who,va='top',fontsize=14,color=BLUE)
ax.set_xlim(0,8.6); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.075,'1공구(서울 송파 구간)는 서울시가 맡고 입찰이 두 번 유찰됐습니다. 노선 전체 11.7km · 새 역 6곳',fontsize=14,color=NAVY)
fig.text(0.045,0.03,'MTN 2026년 6월 23일 · 9월 1일 · 10월 7일 · 10월 27일 보도 · 2공구는 가격 평가를 더해 최종 결정',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_songpahanam_1_gonggu.png'); plt.close()

# 2. 역 예정지 주변 84㎡ 매매 중앙값 (2025년 · 2026년 1~10월)
S=[('방이동 100정거장\n올림픽선수기자촌',247500,283500),('오금역\n오금동',149000,160000),
   ('감일 101정거장\n감일동 · 감이동',118000,141000),('하남시청역\n신장동 · 덕풍동',75950,84000)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송파하남선 역 예정지 주변 · 전용 84㎡ 아파트 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'감일 84㎡ 14억 1천, 작년보다 19.5% 높습니다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.16,0.90,0.62])
import numpy as np
x=np.arange(len(S)); w=0.36
ax.bar(x-w/2,[a for _,a,_ in S],w,color=GRAY,label='2025년')
ax.bar(x+w/2,[b for *_,b in S],w,color=[NAVY if i==2 else BLUE for i in range(len(S))],label='2026년 1~10월')
def won(v): return f'{v//10000}억 {v%10000//1000}천' if v%10000>=1000 else f'{v//10000}억'
for i,(_,a,b) in enumerate(S):
    ax.text(i-w/2,a+2500,won(a),ha='center',fontsize=13,color='#555')
    ax.text(i+w/2,b+2500,won(b),ha='center',fontsize=14,color=NAVY,fontweight='bold')
    ax.text(i,max(a,b)+22000,f'+{(b/a-1)*100:.1f}%',ha='center',fontsize=17,color=NAVY if i==2 else BLUE,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels([s for s,*_ in S],fontsize=14,color='#333')
ax.set_ylim(0,330000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',frameon=False,fontsize=14)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 1월~2026년 10월 계약 · 전용 80~86㎡ · 해제 거래 뺌) · 교산 쪽 역 주변은 아파트 거래가 아직 없음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_songpahanam_2_price.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감일 · 3호선 연장',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'송파하남선 2공구',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'감일동~항동',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'4.79km',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,720),'2027년 착공 · 2032년 개통 목표',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_songpahanam_thumb.png')
