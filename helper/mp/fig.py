import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'일산 메이포레 입주 · 84㎡ 일반분양가와 분양권 거래',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'분양권은 분양가보다 1억원 넘게 낮게 신고',fontsize=29,color=NAVY,fontweight='bold',va='top')
R=[('84㎡ 일반분양가\n(84A 위쪽 · 84B)',7.9,8.0,GRAY),('3단지 84㎡ 분양권\n(2026년 5~9월 · 6건)',6.4,6.8,NAVY),('일산자이더헤리티지 84㎡\n(식사동 · 2022년 · 7~10월 매매)',6.4,7.45,BLUE)]
ax=fig.add_axes([0.36,0.12,0.58,0.68])
for i,(n,lo,hi,c) in enumerate(R):
    ax.plot([lo,hi],[i,i],color=c,lw=26,solid_capstyle='butt')
    ax.text(hi+0.06,i,f'{lo:.1f}~{hi:.1f}억'.replace('.0~','~').replace('.0억','억'),va='center',fontsize=17,color=NAVY,fontweight='bold')
ax.set_yticks(range(len(R))); ax.set_yticklabels([n for n,*_ in R],fontsize=14,color='#333'); ax.invert_yaxis(); ax.set_ylim(2.6,-0.6); ax.set_xlim(5.8,9.0); ax.set_xticks([])
for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
ax.tick_params(length=0)
fig.text(0.045,0.03,'청약홈 입주자모집공고(2024.11) · 국토교통부 분양권 · 아파트 매매 실거래 · 해제 거래 뺌 · 확장비 별도',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_maypore_1_price.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 2027년 3월 입주 · 1,342세대',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'일산 메이포레 입주',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 분양권',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'6억 4천만원대',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'분양가보다 1억 넘게 낮게 신고',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_maypore_thumb.png')
