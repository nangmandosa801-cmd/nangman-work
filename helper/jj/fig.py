import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 국토교통부 아파트 매매 실거래 2026년 1~10월 · 평택 지제동 · 동삭동 · 세교동 · 2018년 이후 · 전용 80~86㎡ · 해제 뺌 · 중앙값(만원), 건수
R=[('지제역 더샵 센트럴시티 (2022)',81000,101,NAVY),('평택 지제역 자이 (2023)',71700,37,BLUE),('힐스테이트 지제역 (2020)',60000,37,BLUE),
   ('힐스테이트 지제역 퍼스티움 (2022)',58450,44,BLUE),('더샵 지제역 센트럴파크 2BL (2020)',53000,33,BLUE),('e편한세상 지제역 (2022)',51700,40,BLUE),
   ('더샵 지제역 센트럴파크 1BL (2020)',50425,20,BLUE),('지제역 푸르지오 엘리아츠 (2024)',50000,13,BLUE),('평택 센트럴자이 3단지 (2019)',42250,66,BLUE),
   ('힐스테이트 평택 2차 (2018)',40000,19,GRAY),('힐스테이트 평택 3차 (2019)',39500,10,GRAY),('힐스테이트 평택 1차 (2018)',38350,28,GRAY)]
def won(v):
    e,m=divmod(int(round(v)),10000)
    return f'{e}억 {m:,}만' if m else f'{e}억'
fig=plt.figure(figsize=(11.55,9.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'지제역 아파트 시세 · 2018년 이후 84㎡ · 2026년 1~10월 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.925,'같은 지제역 84㎡, 3억 8천에서 8억 1천까지',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.11,0.58,0.74])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.62)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=14.5,color='#333')
for y,(_,v,n,c) in zip(ys,R):
    ax.text(v+700,y,won(v),va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.text(v-900,y,f'{n}건',va='center',ha='right',fontsize=12.5,color='white')
ax.set_xlim(0,100000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.055,'남색 지제동 · 파랑 동삭동 · 회색 세교동(한화포레나 지제역이 들어서는 동) · 괄호는 지은 해',fontsize=13,color='#555')
fig.text(0.045,0.022,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 80~86㎡ · 해제 거래 뺌) · 한화포레나 지제역 분양가는 모집공고로 발표',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_hanwhajije_1_sise.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 지제역 · 분양',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'한화포레나 지제역',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'지제역 더샵 84㎡ 올해',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'8억 1천',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'분양가 비교선 · 1순위 11월 10일',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanwhajije_thumb.png')
