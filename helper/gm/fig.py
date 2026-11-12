import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('갈매역아이파크(2018)',85000,GRAY),('구리갈매푸르지오(2017)',81000,GRAY),
   ('신안인스빌 디센트\n84㎡ 분양가 상단',78500,NAVY),('갈매동 84㎡ 전체\n올해 중앙값',76000,BLUE),
   ('한라비발디(2016)',75000,GRAY),('구리갈매스타힐스(2017)',73900,GRAY),('갈매더샵나인힐스(2016)',73300,GRAY),
   ('신안인스빌 디센트\n84㎡ 분양가 하단',72090,NAVY)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'구리갈매역세권 신안인스빌 분양가 · 갈매동 84㎡ 올해 매매 중앙값과 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'84㎡ 7억 8,500만, 갈매동 중앙값보다 2,500만원 높다',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.29,0.11,0.64,0.69])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14.5,color='#333')
for y,(_,v,c) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+600,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,100000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 모집공고(2026년 10월 30일) · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 구리시 갈매동 전용 83~86㎡ · 해제 거래 뺌 · 단지별 중앙값)',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_galmae_1_price.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 구리 갈매 · 분양가상한제',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'갈매 신안인스빌 디센트',font=kr(ser,72),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'84㎡ 분양가',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'7억 8,500만',font=kr(ser,90),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'갈매동 84㎡ 올해 매매 중앙값 7억 6천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_galmae_thumb.png')
