import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def bars(fn,sub,head,R,xmax,foot,h=7.6,left=0.25):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.955,sub,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,head,fontsize=28,color=NAVY,fontweight='bold',va='top')
    ax=fig.add_axes([left,0.12,0.93-left,0.66])
    ys=list(range(len(R)))[::-1]
    for y,(lab,a,b) in zip(ys,R):
        ax.barh(y+0.19,a,height=0.36,color=GRAY); ax.barh(y-0.19,b,height=0.36,color=NAVY)
        ax.text(a+1500,y+0.19,'2025년 '+won(a),va='center',fontsize=14,color='#555')
        ax.text(b+1500,y-0.19,'2026년 '+won(b)+f'  (+{(b/a-1)*100:.0f}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
    ax.set_xlim(0,xmax); ax.set_xticks([])
    for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#C8D2DE')
    fig.text(0.045,0.03,foot,fontsize=12.5,color='#8A8578')
    fig.savefig(fn); plt.close()
F='국토교통부 아파트 매매 실거래(전용 83~86㎡ · 2013년 이후 지은 단지 · 해제 거래 뺌 · 2026년은 1~10월 계약 중앙값)'
bars('img/nangman_wirye_price_1_city.png','위례 아파트 시세 · 84㎡ 매매 중앙값 · 2025년과 2026년','84㎡ 송파 쪽 20억 6,500만, 성남 쪽 16억',
     [('송파 위례\n장지동 · 거여동',165000,206500),('하남 위례\n학암동',130000,165000),('성남 위례\n창곡동',144000,160000)],290000,F)
bars('img/nangman_wirye_price_2_pair.png','위례 아파트 시세 · 단지 짝 84㎡ 매매 중앙값','같은 2016년 준공, 하남 16억 5천 · 성남 18억 7,500만',
     [('위례롯데캐슬\n하남 · 2016',130000,165000),('위례 래미안이편한세상\n성남 · 2016',145000,187500),('위례더힐55\n성남 · 2015',131750,159500),('위례24단지(꿈에그린)\n송파 · 2013',163000,215500)],300000,F,h=8.4,left=0.3)
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 위례신도시 · 송파 성남 하남',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'위례 아파트 시세',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 올해 중앙값',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'16억 9천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'지난해 14억 5천에서',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_wirye_price_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_wirye_price_1_city_v2.png', '84㎡ 송파 쪽 20억 6,500만, 성남 쪽 16억', [('송파 위례|2025년', 165000.0, '16억 5,000만', False), ('송파 위례|2026년 (+25%)', 206500.0, '20억 6,500만', True), ('성남 위례|2025년', 144000.0, '14억 4,000만', False), ('성남 위례|2026년 (+11%)', 160000.0, '16억', False)], note='위례 아파트 시세 · 84㎡ 매매 중앙값 · 2025년과 2026년')
bars('img/nangman_wirye_price_2_pair_v2.png', '같은 2016년 준공, 하남 16억 5천 · 성남 18억 7,500만', [('위례롯데캐슬(하남)|2025년', 130000.0, '13억', False), ('위례롯데캐슬(하남)|2026년 (+27%)', 165000.0, '16억 5,000만', True), ('위례 래미안이편한세상(성남)|2025년', 145000.0, '14억 5,000만', False), ('위례 래미안이편한세상(성남)|2026년 (+29%)', 187500.0, '18억 7,500만', False)], note='위례 아파트 시세 · 단지 짝 84㎡ 매매 중앙값')
print('v2 ok')
