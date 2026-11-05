import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 고지서 금액(농어촌특별세 포함, 만원) → 12월 15일까지 / 이듬해 6월 15일까지
def split(t):
    if t<=300: return t,0
    if t<=600: return 300,t-300
    return t/2,t/2
T=[250,400,600,800,1200]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'종부세 납부기간 · 고지서 금액별로 나눠 낼 수 있는 돈 (가장 많이 미룰 때)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'300만원 넘는 부분은 6월 15일까지 미뤄 냅니다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.20,0.14,0.70,0.62])
ys=list(range(len(T)))[::-1]
for y,t in zip(ys,T):
    a,b=split(t)
    ax.barh(y,a,color=NAVY,height=0.58)
    ax.text(a/2,y,f'{a:,.0f}만',va='center',ha='center',fontsize=16,color='white',fontweight='bold')
    if b:
        ax.barh(y,b,left=a,color=GRAY,height=0.58)
        ax.text(a+b/2,y,f'{b:,.0f}만',va='center',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([f'고지서 {t:,}만원' for t in T],fontsize=15.5,color='#333'); ax.tick_params(axis='y',length=0,pad=10)
ax.set_xlim(0,1250); ax.set_xticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
fig.text(0.20,0.80,'■ 12월 15일까지',fontsize=15,color=NAVY,fontweight='bold')
fig.text(0.40,0.80,'■ 이듬해 6월 15일까지(이자 없음)',fontsize=15,color='#7F8C9D',fontweight='bold')
fig.text(0.045,0.03,'국세청 2025년 귀속 종부세 안내(택스워치 2025년 11월 26일 · 한국세정신문 2025년 12월 1일) · 금액은 농어촌특별세 포함',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_jongbuse_napbu_1_bunnap.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 종부세 납부기간 · 분납',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'종부세 고지서',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'300만원 넘으면',font=kr(ser,70),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'6월까지 나눠 냄',font=kr(ser,86),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'납부는 12월 15일 · 이자 없음',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_jongbuse_napbu_thumb.png')
