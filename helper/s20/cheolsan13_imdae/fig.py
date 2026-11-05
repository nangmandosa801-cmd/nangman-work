import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_cheolsan13_imdae_'
# 그림 1 · 일반분양이 줄 때 비례율(둔 계산)
L=['그대로','100가구','140가구\n(시 제안 3.75%)','200가구','300가구']
A59=[109.6,105.7,104.1,101.7,97.8]; A84=[109.6,104.2,102.1,98.9,93.5]
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'철산주공13단지 · 일반분양이 줄 때 비례율 · 조합 추정 109.6%에서 시작하는 둔 계산',fontsize=15,color=BLUE,va='top')
fig.text(0.045,0.9,'100가구 줄면 105.7%, 300가구 줄면 97.8%(일반분양 한 가구를 59㎡로 둘 때)',fontsize=23,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.19,0.9,0.56])
x=np.arange(len(L)); w=0.36
ax.bar(x-w/2,A59,w,color=BLUE,label='일반분양 한 가구 = 59㎡(9억 2,500만)')
ax.bar(x+w/2,A84,w,color=GRAY,label='일반분양 한 가구 = 84㎡(12억 5,800만)')
for i,(a,b) in enumerate(zip(A59,A84)):
    ax.text(i-w/2,a+0.5,f'{a}%',ha='center',fontsize=12,color=NAVY,fontweight='bold')
    if 97.5<b<100.5: ax.text(i+w/2,b-1.9,f'{b}%',ha='center',fontsize=12,color='white',fontweight='bold')
    else: ax.text(i+w/2,b+0.5,f'{b}%',ha='center',fontsize=12,color='#555',fontweight='bold')
ax.axhline(100,color=NAVY,lw=1.2,ls='--'); ax.text(4.45,100.6,'100% = 감정가 그대로',fontsize=12,color=NAVY,ha='right')
ax.set_xticks(x); ax.set_xticklabels(L,fontsize=13,color='#333'); ax.set_ylim(85,114); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper right',fontsize=12,frameon=False)
fig.text(0.045,0.055,'하우징워치 2026년 4월 29일(조합 추정 비례율 109.6% · 일반분양 약 1,500가구 · 3.3㎡당 3,700만) · 더팩트 2026년 9월 14일(시 제안 3.75%)',fontsize=11,color='#8A8578')
fig.text(0.045,0.02,'종전자산은 올해 거래 중앙값×가구 수의 70%(2조 3,400억)로 둔 값 · 임대 매각 수입 0 · 지출 그대로 · 공급면적 59㎡ 25평 · 84㎡ 34평',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'1_ratio.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축 따라가기 7화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'재건축 비례율',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'철산주공13단지 일반분양 100가구 줄면',font=kr(ser,50),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'109.6% → 105.7%',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'조합 추정 숫자로 둔 계산 · 공공임대 변수',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
