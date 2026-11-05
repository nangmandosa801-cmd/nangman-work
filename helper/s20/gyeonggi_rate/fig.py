import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# (이름, 분양가, 옆 실거래 중앙값) 만원
R=[('한화포레나 지제역\n84A 21층 이상',70875,53000),
   ('중앙하이츠 구성\n플랫폼시티 84㎡',85210,72600),
   ('엘리프 시흥 더프라임\n84㎡ 상단',59930,54300),
   ('고덕 우미린 더 프리미어\n84A 기준층',59130,56900),
   ('광교 자연앤 센트레빌\n59B(지분적립형)',68590,110000)]
def won(v):
    a=abs(v); s=(f'{a//10000}억 {a%10000:,}만' if a%10000 else f'{a//10000}억') if a>=10000 else f'{a:,}만'
    return ('+' if v>0 else '−')+s
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'경기도 청약 경쟁률 · 11월 1순위 5곳 분양가와 옆 단지 올해 실거래',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'분양가 − 옆 실거래 중앙값, 광교만 4억 1천 낮습니다',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.12,0.60,0.66])
ys=list(range(len(R)))[::-1]
d=[a-b for _,a,b in R]
ax.barh(ys,d,color=[NAVY if v<0 else (BLUE if v>=10000 else GRAY) for v in d],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([n for n,_,_ in R],fontsize=14.5,color='#333'); ax.tick_params(axis='y',length=0,pad=10)
for y,v in zip(ys,d):
    if v>0: ax.text(v+900,y,won(v),va='center',ha='left',fontsize=16,color=NAVY,fontweight='bold')
    else: ax.text(v+1500,y,won(v),va='center',ha='left',fontsize=17,color='white',fontweight='bold')
ax.axvline(0,color='#8A97A8',lw=1.2)
ax.set_xlim(-60000,30000); ax.set_xticks([])
for s in ['top','right','bottom','left']: ax.spines[s].set_visible(False)
fig.text(0.045,0.03,'분양가: 각 단지 입주자모집공고(2026년 10월 29~30일) · 실거래: 국토교통부 아파트 매매(2026년 1~10월 · 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gyeonggi_rate_1_gap.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 경기도 청약 경쟁률 · 11월',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'광교 자연앤 센트레빌',font=kr(ser,78),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'옆 단지 59㎡보다',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'4억 1천 낮음',font=kr(ser,90),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'11월 경기 1순위 5곳 분양가 · 경쟁률',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gyeonggi_rate_thumb.png')
