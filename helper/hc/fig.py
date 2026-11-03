import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def clean(ax):
    for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'회천중앙역 로제비앙 그랜드센텀 잔금 · 84㎡ 5층 이상 4억 8,600만원 기준',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'입주 날 갚고 낼 돈 4억 3,740만원',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.14,0.68,0.62])
rows=[('입주 날 낼 돈',[(2.916,NAVY,'중도금 대출 상환 2억 9,160만'),(1.458,BLUE,'잔금 1억 4,580만')]),
      ('전세 3억을 받으면',[(3.0,GRAY,'전세 보증금 3억'),(1.374,NAVY,'내 돈 1억 3,740만')]),
      ('전세 2억 7천이면',[(2.7,GRAY,'전세 2억 7천'),(1.674,NAVY,'내 돈 1억 6,740만')])]
for i,(n,parts) in enumerate(rows):
    x=0
    for v,c,lab in parts:
        ax.barh(i,v,left=x,color=c,height=0.55); ax.text(x+v/2,i,lab,ha='center',va='center',fontsize=13.5,color='white',fontweight='bold'); x+=v
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in rows],fontsize=16,color='#333'); ax.invert_yaxis(); ax.set_xlim(0,4.5); ax.set_xticks([]); clean(ax)
fig.text(0.045,0.03,'입주자모집공고(2025.7) 계약금 10% · 중도금 60% · 잔금 30% · 취득세 · 확장비 · 중도금 이자는 따로 · 전세는 옆 디아르떼 84㎡ 입주장 실거래',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_hoecheon_1_jangeum.png'); plt.close()
D=[('회천중앙역 로제비앙 그랜드센텀 분양가',4.86,NAVY),('양주회천신도시디에트르센트럴시티 (2022)',5.13,GRAY),('회천대광로제비앙더센트럴 (2023)',4.79,GRAY),('덕계역대광로제비앙더메트로팰리스 (2023)',4.75,GRAY),('회천파밀리에더퍼스트 (2024)',4.705,GRAY),('회천베네스트하우스 (2023)',4.6,GRAY)]
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'회천중앙역 로제비앙 그랜드센텀 · 84㎡ 분양가와 옆 회천 새 아파트 84㎡ 올해 매매',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'분양가가 옆 새 아파트 매매값과 같은 4억 후반',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.43,0.1,0.52,0.7])
ax.barh(range(len(D)),[v for _,v,_ in D],color=[c for *_,c in D],height=0.6)
for i,(n,v,c) in enumerate(D): ax.text(v+0.05,i,f'{v:.2f}억'.replace('0억','억'),va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(range(len(D))); ax.set_yticklabels([n for n,_,_ in D],fontsize=13.5,color='#333'); ax.invert_yaxis(); ax.set_xlim(0,6); ax.set_xticks([]); clean(ax)
fig.text(0.045,0.025,'분양가: 5층 이상 · 매매: 국토교통부 실거래 2026년 1~10월 84㎡ 중앙값 · 양주 회정 · 덕계동',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_hoecheon_2_price.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 양주 회천 · 642세대 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'회천중앙역 로제비앙',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,450),'그랜드센텀 잔금',font=kr(ser,74),fill='#F4F1EA',anchor='mm')
d.text((W/2,580),'전세 3억이면 1억 4천',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'입주 날 필요한 돈 계산서',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_hoecheon_thumb.png')
