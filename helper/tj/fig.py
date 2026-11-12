import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_tangjeong2_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 힐스테이트자이아산센텀 84㎡ 전세 달별 중앙값
M=[('1월',35000,15),('2월',35000,5),('3월',36000,2),('4월',40000,3)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'아산 배방읍 세교리 힐스테이트자이아산센텀 · 84㎡ 전세 달별 중앙값(2026년)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1~3월 3억 5천~3억 6천, 4월 4억',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.88,0.64])
xs=range(len(M)); cols=[GRAY]*3+[NAVY]
ax.bar(xs,[v for _,v,_ in M],color=cols,width=0.55)
for x,(m,v,n) in zip(xs,M):
    ax.text(x,v+500,won(v),ha='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(x,1500,f'{n}건',ha='center',fontsize=14,color='white')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_,_ in M],fontsize=16,color='#333')
ax.set_ylim(0,46000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~4월 계약 · 전용 80~86㎡ · 월세 없는 계약 중앙값 · 5월 이후는 1건 이하)',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_centum.png'); plt.close()
# 2 분양가 vs 탕정·배방 새 아파트
R=[('84㎡ 분양가\n(더샵 탕정인피니티시티 2차)',49000,BLUE,'4억 7,110만~4억 9,000만'),('탕정 · 배방 새 아파트\n84㎡ 매매',57400,GRAY,None),('탕정 · 배방 새 아파트\n84㎡ 전세',37000,NAVY,None),
   ('70㎡ 분양가\n(더샵 탕정인피니티시티 2차)',41200,BLUE,'4억 100만~4억 1,200만'),('탕정 · 배방 새 아파트\n70㎡대 매매',42500,GRAY,None),('탕정 · 배방 새 아파트\n70㎡대 전세',28000,NAVY,None)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'더샵 탕정인피니티시티 2차 분양가와 옆 새 아파트 올해 실거래 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'84㎡ 전세 3억 7천, 70㎡대 전세 2억 8천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.10,0.63,0.70])
ys=[6.4,5.4,4.4,2.2,1.2,0.2]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for _,_,c,_ in R],height=0.72)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_,_ in R],fontsize=14.5,color='#333')
for y,(_,v,c,lab) in zip(ys,R): ax.text(v+600,y,lab or won(v),va='center',fontsize=15.5,color=NAVY,fontweight='bold')
ax.set_xlim(0,78000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'분양가: 2024년 4월 입주자모집공고(층별) · 실거래: 국토교통부(2026년 1~10월 · 2021년 이후 준공 · 해제 거래 뺌 · 전세는 월세 없는 계약)',fontsize=12,color='#8A8578')
fig.savefig(f'img/{S}2_compare.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 아산 탕정 · 2027년 2월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'탕정 더샵 2차 입주',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'옆 새 아파트 84㎡ 전세',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'3억 7천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'탕정 · 배방 새 아파트 올해 296건 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_tangjeong2_1_centum_v2.png', '1~3월 3억 5천~3억 6천, 4월 4억', [('1월', 35000.0, '3억 5,000만', False), ('2월', 35000.0, '3억 5,000만', False), ('3월', 36000.0, '3억 6,000만', False), ('4월', 40000.0, '4억', True)], note='아산 배방읍 세교리 힐스테이트자이아산센텀 · 84㎡ 전세 달별 중앙값(2026년)')
bars('img/nangman_tangjeong2_2_compare_v2.png', '84㎡ 전세 3억 7천, 70㎡대 전세 2억 8천', [('84㎡ 분양가|더샵 탕정인피니티시티 2차', 49000.0, '4억 7,110만~4억 9,000만', False), ('탕정 · 배방 새 아파트 84㎡ 매매', 57400.0, '5억 7,400만', False), ('탕정 · 배방 새 아파트 84㎡ 전세', 37000.0, '3억 7,000만', True), ('70㎡ 분양가|더샵 탕정인피니티시티 2차', 41200.0, '4억 100만~4억 1,200만', False), ('탕정 · 배방 새 아파트 70㎡대 전세', 28000.0, '2억 8,000만', False)], note='더샵 탕정인피니티시티 2차 분양가와 옆 새 아파트 올해 실거래 중앙값')
print('v2 ok')
