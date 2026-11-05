import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
rates=['4.88%\n(9월 평균)','5.13%\n(0.25%포인트 오름)','5.38%\n(0.5%포인트 오름)']
v4=[163,171,179]; v6=[244,257,269]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'한국 기준금리 발표일 11월 · 주담대 원금은 두고 이자만 낼 때',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'4억 빌린 집 한 달 이자 163만원, 0.25%포인트에 8만원',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.14,0.88,0.62])
x=range(3); w=0.36
b1=ax.bar([i-w/2-0.01 for i in x],v4,w,color=BLUE); b2=ax.bar([i+w/2+0.01 for i in x],v6,w,color=NAVY)
for i in x:
    ax.text(i-w/2-0.01,v4[i]+5,f'{v4[i]}만원',ha='center',fontsize=16,color=BLUE,fontweight='bold')
    ax.text(i+w/2+0.01,v6[i]+5,f'{v6[i]}만원',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(rates,fontsize=15,color='#333')
ax.set_ylim(0,300); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.08,0.80,'■ 4억 대출',color=BLUE,fontsize=15,fontweight='bold'); fig.text(0.22,0.80,'■ 6억 대출',color=NAVY,fontsize=15,fontweight='bold')
fig.text(0.045,0.03,'한국은행 2026년 9월 가중평균금리(신규 주택담보대출 4.88%) · 한 달 이자 = 빌린 돈 × 금리 ÷ 12 · 만원 아래 반올림',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_nov27_1_interest.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 기준금리 · 주담대 이자',font=kr(san,30),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'기준금리 발표일 11월 26일',font=kr(ser,66),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'4억 빌린 집 한 달 이자',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'163만원',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,718),'0.25%포인트 오르면 8만원 더',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_nov27_thumb.png')
