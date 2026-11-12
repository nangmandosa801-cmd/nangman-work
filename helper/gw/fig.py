import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
R=[('힐스테이트고덕센트럴\n(2024년 · 4건)',86000,GRAY),('힐스테이트고덕스카이시티\n(2024년 · 3건)',80000,GRAY),('제일풍경채 2차 에듀\n(2023년 · 42건)',69000,GRAY),('호반써밋고덕신도시\n(2021년 · 23건)',65000,GRAY),('호반써밋 에듀파크\n(2022년 · 47건)',59900,GRAY),('고덕 우미린 더 프리미어\n84A 기준층 분양가',59130,NAVY),('고덕동 84㎡ 전체\n(401건)',56900,BLUE),('대광로제비앙 THE ART\n(2022년 · 50건)',52500,GRAY),('리슈빌레이크파크\n(2021년 · 48건)',52350,GRAY)]
fig=plt.figure(figsize=(11.55,9.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'고덕 우미린 더 프리미어 분양가 · 고덕동 84㎡ 올해 매매 중앙값과 나란히',fontsize=16.5,color=BLUE,va='top')
fig.text(0.045,0.912,'84A 5억 9,130만, 고덕동 중앙값보다 2,230만 높다',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.31,0.10,0.62,0.71])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+1200,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,105000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 모집공고(2026년 10월 30일) · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 평택 고덕동 · 전용 80~86㎡ · 해제 거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_godeokwoomi_1_price.png'); plt.close()

F=['1층\n(9세대)','2층\n(10세대)','3층\n(10세대)','4층\n(17세대)','5~9층\n(95세대)','기준층\n(168세대)']; V=[53210,54390,55580,56760,57940,59130]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'고덕 우미린 더 프리미어 84A(309세대) 층별 분양가 · 고덕동 84㎡ 올해 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'4층까지는 고덕동 중앙값 5억 6,900만보다 낮다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
ax.bar(F,[v-48000 for v in V],bottom=48000,color=[BLUE]*4+[NAVY]*2,width=0.6)
for i,v in enumerate(V): ax.text(i,v+250,won(v),ha='center',fontsize=15.5,color=NAVY,fontweight='bold')
ax.axhline(56900,color=GRAY,lw=2.5,ls='--'); ax.text(-0.45,57150,'고덕동 84㎡ 중앙값 5억 6,900만',fontsize=14,color='#555')
ax.set_ylim(48000,61500); ax.set_yticks([]); ax.tick_params(axis='x',labelsize=14.5,colors='#333')
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 모집공고(2026년 10월 30일) 84A 공급금액 · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 해제 거래 뺌) · 세로축은 4억 8천만부터',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_godeokwoomi_2_floor.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 고덕 · 11월 10일 1순위',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,350),'고덕 우미린 더 프리미어',font=kr(ser,70),fill='#F4F1EA',anchor='mm')
d.text((W/2,465),'84㎡ 분양가',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'5억 9,130만',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'고덕동 84㎡ 올해 중앙값 5억 6,900만',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_godeokwoomi_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_godeokwoomi_1_price_v2.png', '84A 5억 9,130만, 고덕동 중앙값보다 2,230만 높다', [('힐스테이트고덕센트럴|2024년 · 4건', 86000.0, '8억 6,000만', False), ('제일풍경채 2차 에듀|2023년 · 42건', 69000.0, '6억 9,000만', False), ('고덕 우미린 더 프리미어 84A 기준층 분양가', 59130.0, '5억 9,130만', True), ('고덕동 84㎡ 전체|401건', 56900.0, '5억 6,900만', False), ('리슈빌레이크파크|2021년 · 48건', 52350.0, '5억 2,350만', False)], note='고덕 우미린 더 프리미어 분양가 · 고덕동 84㎡ 올해 매매 중앙값과 나란히')
bars('img/nangman_godeokwoomi_2_floor_v2.png', '4층까지는 고덕동 중앙값 5억 6,900만보다 낮다', [('1층|9세대', 53210, '5억 3,210만', False), ('4층|17세대', 56760, '5억 6,760만', False), ('고덕동 84㎡ 중앙값', 56900, '5억 6,900만', True), ('5~9층|95세대', 57940, '5억 7,940만', False), ('기준층|168세대', 59130, '5억 9,130만', False)], note='고덕 우미린 더 프리미어 84A(309세대) 층별 분양가 · 고덕동 84㎡ 올해 중앙값')
print('v2 ok')
