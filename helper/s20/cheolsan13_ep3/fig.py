import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_cheolsan13_ep3_'
# 분담금(만원) = 조합원 분양가 − 감정가 × 1.096 · 73㎡ 2026 중앙값 12억 8,000만
cases=['감정가 60%\n7억 6,800만','감정가 70%\n8억 9,600만','감정가 80%\n10억 2,400만']
v84=[27827,13798,-230]; v102=[50927,36898,22870]
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'철산주공 13단지 분담금 · 2015년에 73㎡를 산 예시 조합원 · 비례율 109.6%',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'새 84㎡는 2억 7,827만 ~ 230만 돌려받음, 102㎡는 5억 927만 ~ 2억 2,870만',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.17,0.9,0.6])
x=range(3); w=0.36
b1=ax.bar([i-w/2 for i in x],[v/10000 for v in v84],w,color=NAVY,label='새 84㎡ (조합원 분양가 11억 2,000만)')
b2=ax.bar([i+w/2 for i in x],[v/10000 for v in v102],w,color=GRAY,label='새 102㎡ (13억 5,100만)')
def lab(v):
    if v<0: return f'{-v:,}만 돌려받음'
    return f'{v//10000}억 {v%10000:,}만' if v>=10000 else f'{v:,}만'
for i,v in enumerate(v84): ax.text(i-w/2,(v/10000)+(0.12 if v>=0 else -0.45),lab(v),ha='center',fontsize=13,color=NAVY,fontweight='bold')
for i,v in enumerate(v102): ax.text(i+w/2,v/10000+0.12,lab(v),ha='center',fontsize=13,color='#555',fontweight='bold')
ax.axhline(0,color='#C8D2DE',lw=1)
ax.set_xticks(list(x)); ax.set_xticklabels(cases,fontsize=13,color='#555')
ax.set_yticks([]); ax.set_ylim(-1.0,6.2)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.legend(loc='upper right',fontsize=12,frameon=False)
fig.text(0.045,0.055,'분담금 = 조합원 분양가(조합 추정 · 하우징워치 2026년 4월 29일) − 감정가 × 비례율 109.6%',fontsize=11,color='#8A8578')
fig.text(0.045,0.022,'감정가는 73㎡ 2026년 실거래 중앙값 12억 8,000만(29건)의 60 · 70 · 80%로 둔 예시 · 실제 감정평가 전',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'1_bundam.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축 따라가기 3화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,350),'철산주공 13단지 분담금',font=kr(ser,78),fill='#F4F1EA',anchor='mm')
d.text((W/2,465),'73㎡ 조합원이 새 84㎡로 갈 때',font=kr(ser,52),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'감정가 60 · 70 · 80%',font=kr(ser,86),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2억 7,827만부터 돌려받는 경우까지 · 예시 계산서',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
