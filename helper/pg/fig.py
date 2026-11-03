import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('동탄 새 아파트 84㎡\n새 세입자 전세',45150,GRAY),('동탄 파라곤 3차 82㎡\n임대보증금(타입 상한)',44032,NAVY),('동탄 새 아파트 84㎡\n갱신 전세',40000,GRAY),('동탄호수공원 자연&자이\n84㎡ 장기전세',31920,BLUE)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'동탄 파라곤 3차 임대료 · 동탄 2018년 이후 아파트 올해 전세와 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'82㎡ 4억 4천, 새 세입자 전세와 1,100만원 차이',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+600,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,56000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 공급금액(타입별 가장 높은 금액) · 국토교통부 전월세 실거래(2026년 1~10월 · 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_paragon3_1_jeonse.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 동탄2 · 공공지원 민간임대',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'동탄 파라곤 3차',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'82㎡ 보증금',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'4억 4천',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'옆 새 아파트 새 세입자 전세 4억 5천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_paragon3_thumb.png')
