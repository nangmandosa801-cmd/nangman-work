import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
R=[('반포 · 잠원 2015년 이후\n84㎡ 올해 매매 중앙값',508000,GRAY),
   ('메이플자이 84㎡\n올해 매매 중앙값',501000,GRAY),
   ('잠원동 2015년 이후\n84㎡ 올해 매매 중앙값',475000,GRAY),
   ('디에이치 신반포 에스테라\n입찰 기준가 가장 높은 세대',439800,NAVY),
   ('디에이치 신반포 에스테라\n입찰 기준가 가장 낮은 세대',400900,NAVY),
   ('디에이치 클래스트(반포124)\n84㎡ 예상 분양가 높은 쪽',338000,BLUE)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'디에이치 신반포 에스테라 분양가 · 84㎡ 입찰 기준가와 옆 새 아파트 매매',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'입찰 시작 40억 900만, 잠원동 중앙값보다 7억 4천 낮습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.29,0.11,0.64,0.68])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14.5,color='#333')
for y,(_,v,c) in zip(ys,R):
    r=v%10000; s=f'{v//10000}억 {r//1000}천' if r and r%1000==0 else (f'{v//10000}억 {r:,}만' if r else f'{v//10000}억')
    ax.text(v+5000,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,620000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'입찰공고(2026년 10월 30일) · 국토교통부 매매 실거래(2026년 1~9월 계약 · 해제 거래 뺌 · 83~86㎡) · 클래스트는 보도된 예상 금액',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_estera_1_price.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 잠원동 · 신반포22차',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'디에이치 신반포 에스테라',font=kr(ser,70),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'청약통장 없이',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,610),'입찰로 삽니다',font=kr(ser,72),fill='#F4F1EA',anchor='mm')
d.text((W/2,715),'84㎡ 28세대 · 입찰 기준가 40억 900만원부터',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_estera_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_estera_1_price_v2.png', '입찰 시작 40억 900만, 잠원동 중앙값보다 7억 4천 낮습니다', [('반포 · 잠원 2015년 이후 84㎡ 올해 매매 중앙값', 508000.0, '50억 8천', False), ('잠원동 2015년 이후 84㎡ 올해 매매 중앙값', 475000.0, '47억 5천', False), ('디에이치 신반포 에스테라 입찰 기준가 가장 높은 세대', 439800.0, '43억 9,800만', False), ('디에이치 신반포 에스테라 입찰 기준가 가장 낮은 세대', 400900.0, '40억 900만', True), ('디에이치 클래스트 84㎡ 예상 분양가 높은 쪽|반포124', 338000.0, '33억 8천', False)], note='디에이치 신반포 에스테라 분양가 · 84㎡ 입찰 기준가와 옆 새 아파트 매매')
print('v2 ok')
