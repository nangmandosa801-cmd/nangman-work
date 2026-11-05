import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('남양주 다산동\n(왕숙 옆)',91950,GRAY),('의정부 의정부동\n(의정부역 펠리스타워)',84000,NAVY),('안산 상록구\n(아르뮤제자이)',65000,NAVY),('평택 고덕동\n(고덕 2곳)',57400,NAVY),('남양주 진접읍\n(왕숙 옆)',46000,GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'경기도 분양 예정 아파트 · 그 동네 2020년 이후 지은 84㎡ 올해 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'같은 84㎡라도 동네마다 4억 6천~9억 2천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.66,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+800,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,112000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 83~86㎡ · 2020년 이후 지은 아파트 · 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_bunyang12_1_price.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 경기 · 분양 예정',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'경기도 분양 예정',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'11월 경기',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'1만 1,275가구',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'평택 고덕 · 의정부 · 안산 · 왕숙 · 부천대장',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_bunyang12_thumb.png')
