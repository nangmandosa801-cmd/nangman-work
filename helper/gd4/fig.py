import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_geomdan4_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 2026년 입주 검단 새 아파트 5곳 84㎡ 전세 중앙값
R=[('검단호수공원역 호반써밋\n(불로동)',30000,19,NAVY),('신검단중앙역 칸타빌 더스위트\n(원당동)',30000,60,GRAY),('신검단중앙역 디에트르 더에듀\n(불로동)',35000,10,NAVY),('롯데캐슬 넥스티엘\n(원당동)',42500,22,GRAY),('e편한세상 검단 웰카운티\n(원당동)',43000,38,GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'올해 검단에 새로 들어온 아파트 5곳 · 84㎡ 전세 중앙값(2026년)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'같은 해 입주인데 3억에서 4억 3천까지',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.33,0.12,0.60,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=14.5,color='#333')
for y,(_,v,n,c) in zip(ys,R):
    ax.text(v+500,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(1200,y,f'{n}건',va='center',fontsize=13,color='white')
ax.set_xlim(0,52000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 인천 검단구 · 전용 80~86㎡ · 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_newapt.png'); plt.close()
# 2 84㎡ · 110㎡ 전세 · 매매
R=[('110㎡ 매매\n(38건)',70600,GRAY),('110㎡ 전세\n(90건)',42500,BLUE),('84㎡ 매매\n(845건)',61000,GRAY),('84㎡ 전세\n(1,256건)',35000,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'검단 2020년 이후 지은 아파트 · 넓이별 전세와 매매 중앙값(2026년)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'84㎡ 전세 3억 5천, 110㎡ 전세 4억 2천 5백',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.20,0.12,0.73,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+600,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,84000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1~10월 · 인천 검단구 · 해제 거래 뺌 · 전세는 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}2_size.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 인천 검단 · 2027년 2월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'검단 제일풍경채 4차',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'불로동 새 아파트 84㎡ 전세',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'3억 3천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2020년 이후 지은 아파트 · 올해 89건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_geomdan4_1_newapt_v2.png', '같은 해 입주인데 3억에서 4억 3천까지', [('검단호수공원역 호반써밋|불로동', 30000.0, '3억', False), ('신검단중앙역 칸타빌 더스위트|원당동', 30000.0, '3억', False), ('신검단중앙역 디에트르 더에듀|불로동', 35000.0, '3억 5,000만', False), ('롯데캐슬 넥스티엘|원당동', 42500.0, '4억 2,500만', False), ('e편한세상 검단 웰카운티|원당동', 43000.0, '4억 3,000만', True)], note='올해 검단에 새로 들어온 아파트 5곳 · 84㎡ 전세 중앙값(2026년)')
bars('img/nangman_geomdan4_2_size_v2.png', '84㎡ 전세 3억 5천, 110㎡ 전세 4억 2천 5백', [('110㎡ 매매|38건', 70600.0, '7억 600만', False), ('110㎡ 전세|90건', 42500.0, '4억 2,500만', False), ('84㎡ 매매|845건', 61000.0, '6억 1,000만', False), ('84㎡ 전세|1,256건', 35000.0, '3억 5,000만', True)], note='검단 2020년 이후 지은 아파트 · 넓이별 전세와 매매 중앙값(2026년)')
print('v2 ok')
