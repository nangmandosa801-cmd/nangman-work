import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
SRC='국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 하남시 · 전세 · 계약구분 「신규」 1,714건)'

# 1. 보증금 구간별 새 세입자 전세 건수
B=[('1억 5천 미만',6),('1억 5천~2억 5천',81),('2억 5천~3억 5천',44),('3억 5천~4억 5천',97),('4억 5천~5억 5천',176),('5억 5천 이상',1310)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'하남 전세 3억 · 새 세입자 전세 보증금 구간별 계약 건수',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.912,'3억 안팎 계약은 1,714건 중 44건(2.6%)입니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.70])
ys=list(range(len(B)))[::-1]
cols=[NAVY if '2억 5천~3억 5천' in b[0] else GRAY for b in B]
ax.barh(ys,[b[1] for b in B],color=cols,height=0.66)
ax.set_yticks(ys); ax.set_yticklabels([b[0] for b in B],fontsize=15,color='#333')
for y,(l,v) in zip(ys,B):
    ax.text(v+18,y,f'{v:,}건 ({v/1714*100:.1f}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(0,1650); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.035,'남색 = 3억 안팎(2억 5천만원 이상 3억 5천만원 미만)',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.012,SRC,fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_jeonse3_1_band.png'); plt.close()

# 2. 3억 안팎 새 전세 월별 건수
M=[('1월',12),('2월',7),('3월',6),('4월',5),('5월',4),('6월',6),('7월',0),('8월',2),('9월',1),('10월',1)]
fig=plt.figure(figsize=(11.55,7.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 전세 3억 · 3억 안팎 새 세입자 전세 계약, 달마다 몇 건',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1월 12건에서 9월 · 10월 1건씩으로 줄었습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.14,0.88,0.64])
x=range(len(M))
ax.bar(x,[m[1] for m in M],color=[NAVY if m[1]>=10 else BLUE for m in M],width=0.62)
for i,(l,v) in enumerate(M): ax.text(i,v+0.3,f'{v}건',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels([m[0] for m in M],fontsize=15,color='#333')
ax.set_ylim(0,14.5); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.035,'2026년 계약월 기준 · 10월 계약은 신고 기한(30일)이 남아 건수가 늘 수 있음',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.012,SRC+' 중 보증금 2억 5천만~3억 5천만원 미만 44건',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_jeonse3_2_month.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 전월세 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'하남 전세 3억',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'새 세입자 1,714건 중',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'44건',font=kr(ser,120),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'2026년 1~10월 아파트 · 2억 5천~3억 5천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_jeonse3_thumb.png')
