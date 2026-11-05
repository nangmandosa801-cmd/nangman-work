import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 2026년 1~10월 전용 83~86㎡ 매매 중앙값(만원) · 해제 거래 뺌
R=[('과천시',238250),('성남 분당구',177000),('성남 수정구',122800),('하남시',112300),('용인 수지구',97000),('성남 중원구',88700),('광주시',41500)]
LINE1=174000; LINE2=130000
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'종부세 대상 · 경기 동남부 84㎡ 올해 실거래 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'한 채로 기준선을 넘는 곳은 과천 · 분당',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.2,0.12,0.74,0.66])
ys=list(range(len(R)))[::-1]
cols=[NAVY if v>=LINE1 else (BLUE if v>=100000 else GRAY) for _,v in R]
ax.barh(ys,[v for _,v in R],color=cols,height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_ in R],fontsize=16,color='#333')
for y,(_,v) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+2500,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.axvline(LINE1,color=NAVY,ls='--',lw=1.6); ax.text(LINE1,len(R)-0.35,'한 채 기준선\n시세 약 17억 4천',ha='center',va='bottom',fontsize=13,color=NAVY)
ax.set_xlim(0,290000); ax.set_ylim(-0.6,len(R)+0.4); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 83~86㎡ · 해제 거래 뺌) · 기준선은 공시가격 12억을 시세 반영률 69%로 바꾼 어림값',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_jongbuse_1_median.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 2026 종합부동산세 · 경기 동남부',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'종부세 대상',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'하남 84㎡ 두 채면',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'기준 9억',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'한 채 기준은 12억 · 하남 84㎡ 중앙값 11억 2천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_jongbuse_thumb.png')
