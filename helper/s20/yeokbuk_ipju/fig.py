import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_yeokbuk_ipju_'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 1 59㎡ 분양권 9건 (2026년, 해제 뺌) · 무순위 공급가 4억 5,700만
T=[('3월 6일',35527),('3월 20일',35456),('7월 16일',35456),('8월 4일',41807),('8월 5일',34607),('8월 6일',38070),('8월 12일',35527),('9월 14일',43251),('10월 8일',42200)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'역북 서희스타힐스 프라임시티 · 59㎡ 분양권 2026년 신고 9건',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'9건 모두 무순위 공급가 4억 5,700만원보다 낮았다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.13,0.9,0.64])
xs=range(len(T)); ax.bar(xs,[v for _,v in T],color=NAVY,width=0.6)
ax.axhline(45700,color=BLUE,lw=2.5,ls='--')
ax.text(-0.4,46600,'무순위 공급가 4억 5,700만',ha='left',fontsize=15,color=BLUE,fontweight='bold')
for x,(m,v) in zip(xs,T): ax.text(x,v+500,won(v).replace(' ','\n',1),ha='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_xticks(list(xs)); ax.set_xticklabels([m for m,_ in T],fontsize=13.5,color='#333')
ax.set_ylim(0,52000); ax.set_yticks([])
for s_ in ['top','right','left']: ax.spines[s_].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 분양권 실거래(2026년 1월~11월 4일 계약 · 해제 거래 뺌) · 무순위 공급가는 2026년 9월 위키트리 보도',fontsize=12.5,color='#8A8578')
fig.savefig(f'img/{S}1_bunyang59.png'); plt.close()
# 2 분양권과 옆 새 아파트 3곳 매매 · 전세
R=[('옆 새 아파트 3곳\n84㎡ 매매',55000,GRAY),('프라임시티 84㎡\n분양권(10월)',60550,BLUE),('옆 새 아파트 3곳\n84㎡ 전세',36000,NAVY),('프라임시티 59㎡\n분양권 중앙값',35527,BLUE),('옆 새 아파트 3곳\n59㎡ 전세',26250,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'프라임시티 분양권과 2023~2024년 입주 옆 새 아파트 3곳(역북동 · 김량장동 · 유방동)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.905,'84㎡ 분양권 6억, 옆 단지 84㎡ 전세 3억 6천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+600,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,72000); ax.set_xticks([])
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
d.text((70,95),'낭만 부동산 · 용인 처인구 역북동 · 2027년 3월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,345),'역북 서희스타힐스',font=kr(ser,76),fill='#F4F1EA',anchor='mm')
d.text((W/2,450),'프라임시티 입주',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,535),'옆 단지 84㎡ 전세',font=kr(ser,46),fill='#AFC0D8',anchor='mm')
d.text((W/2,640),'3억 6천',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,735),'2023~2024년 입주 옆 새 아파트 3곳 · 올해 25건 중앙값',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save(f'img/{S}thumb.png')
