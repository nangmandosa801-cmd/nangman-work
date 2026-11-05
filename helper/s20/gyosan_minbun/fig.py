import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('감일 84㎡\n올해 매매 중앙값',141000,BLUE),('교산 민간분양 84㎡\n평당 3,200만원 × 34평',108800,NAVY),('감일 84㎡\n새 세입자 전세',72000,GRAY),('교산 민간분양 84㎡\n평당 2,000만원 × 34평',68000,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'교산신도시 민간분양 · 보도된 평당 단가를 84㎡로 바꿔 감일 실거래와 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'평당 3,200만원이어도 감일 매매보다 3억 2천 낮음',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.66,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+1500,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,172000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'평당 단가: 하남일보 · 하남 Times 보도(업계 전망) · 감일: 국토교통부 실거래(2026년 1~10월 · 감이동 · 감일동 · 전용 83~86㎡ · 해제 · 직거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gyosan_minbun_1_price.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 교산신도시 · 민간분양',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'교산신도시 민간분양',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'84㎡ 평당 3,200만원이면',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'10억 8천',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'옆 감일 84㎡ 올해 매매 중앙값 14억 1천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gyosan_minbun_thumb.png')
