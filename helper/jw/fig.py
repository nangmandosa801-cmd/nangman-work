import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_jinwiseohee_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 세교파라곤 84㎡ 전세 달별 중앙값
M=[('3월',32000,7),('4월',31000,18),('5월',35000,17),('6월',37000,10),('7월',39000,6),('8월',38000,6)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'오산 세교파라곤(2026년 입주) · 84㎡ 전세 달별 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'첫 두 달 3억 1천~3억 2천, 셋째 달부터 올랐다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
xs=range(len(M)); cols=[GRAY]*2+[NAVY]*4
ax.bar(xs,[v for _,v,_ in M],color=cols,width=0.6)
for x,(m,v,n) in zip(xs,M):
    ax.text(x,v+400,won(v),ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(x,1200,f'{n}건',ha='center',fontsize=13,color='white')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_,_ in M],fontsize=16,color='#333')
ax.set_ylim(0,44000); ax.set_yticks([])
for s_ in ['top','right','left']: ax.spines[s_].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 3~8월 계약 · 전용 80~86㎡ · 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_segyo.png'); plt.close()
# 2 분양권 · 옆 새 아파트 매매 · 전세
R=[('옆 새 아파트 4곳\n84㎡ 매매',47800,GRAY),('옆 새 아파트 4곳\n59㎡ 매매',36550,GRAY),('진위역 서희스타힐스\n59㎡ 분양권',35200,BLUE),('옆 새 아파트 4곳\n84㎡ 전세',28350,NAVY),('옆 새 아파트 4곳\n59㎡ 전세',22050,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'진위역 서희스타힐스 분양권과 2024년 입주 옆 새 아파트 4곳(오산 3곳 · 평택 서정동 1곳)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.905,'59㎡ 분양권 3억 5천, 옆 단지 84㎡ 전세 2억 8천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+600,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,58000); ax.set_xticks([])
for s_ in ['top','right','bottom']: ax.spines[s_].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 · 전월세 · 분양권 실거래(2026년 1~11월 계약 · 해제 거래 뺌 · 전세는 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}2_compare.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 평택 진위 · 2027년 2월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'진위역 서희스타힐스',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'옆 단지 84㎡ 전세',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'2억 8천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2024년 입주 옆 새 아파트 4곳 · 올해 100건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_jinwiseohee_1_segyo_v2.png', '첫 두 달 3억 1천~3억 2천, 셋째 달부터 올랐다', [('3월', 32000.0, '3억 2,000만', False), ('4월', 31000.0, '3억 1,000만', False), ('5월', 35000.0, '3억 5,000만', True), ('7월', 39000.0, '3억 9,000만', False), ('8월', 38000.0, '3억 8,000만', False)], note='오산 세교파라곤(2026년 입주) · 84㎡ 전세 달별 중앙값')
bars('img/nangman_jinwiseohee_2_compare_v2.png', '59㎡ 분양권 3억 5천, 옆 단지 84㎡ 전세 2억 8천', [('옆 새 아파트 4곳 84㎡ 매매', 47800.0, '4억 7,800만', False), ('옆 새 아파트 4곳 59㎡ 매매', 36550.0, '3억 6,550만', False), ('진위역 서희스타힐스 59㎡ 분양권', 35200.0, '3억 5,200만', True), ('옆 새 아파트 4곳 84㎡ 전세', 28350.0, '2억 8,350만', False), ('옆 새 아파트 4곳 59㎡ 전세', 22050.0, '2억 2,050만', False)], note='진위역 서희스타힐스 분양권과 2024년 입주 옆 새 아파트 4곳(오산 3곳')
print('v2 ok')
