import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
r=pd.read_pickle('r.pkl')  # rec 내림차순
FEW={'종로구','중구','용산구','금천구'}
fig=plt.figure(figsize=(11.55,13.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.972,'서울 구별 아파트 가격 · 84㎡ 매매 중앙값 · 2021년을 100으로 둔 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.942,'2021년 고점 넘긴 구 21곳, 못 넘긴 구 4곳',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.13,0.07,0.80,0.835])
labs=[]; vals=[]; cols=[]; ns=[]
for gu,row in r.iterrows():
    labs.append(gu[:-1]+(' ※' if gu in FEW else '')); vals.append(row.rec); cols.append(NAVY if row.rec>=100 else GRAY); ns.append(int(row.n26))
ys=list(range(len(labs)))[::-1]
ax.barh(ys,vals,height=0.62,color=cols)
for y,v,n,c in zip(ys,vals,ns,cols):
    ax.text(v+1,y,f'{v:.1f}  ({n:,}건)',va='center',fontsize=13.5,color=NAVY if c==NAVY else '#555',fontweight='bold' if c==NAVY else 'normal',bbox=None if c==NAVY else dict(facecolor='white',edgecolor='none',pad=1.5))
ax.axvline(100,color=BLUE,ls='--',lw=1.6)
ax.text(100.5,len(labs)-0.2,'2021년 = 100',fontsize=13,color=BLUE,va='bottom')
ax.set_yticks(ys); ax.set_yticklabels(labs,fontsize=14,color='#333')
ax.set_xlim(60,165); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.038,'국토교통부 아파트 매매 실거래 · 전용 83~86㎡ · 해제 거래 뺌 · 2022년 이후 직거래 뺌 · 괄호는 2026년 1~10월 거래 건수',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.016,'※ 종로 · 중구 · 용산 · 금천은 해마다 거래 200건 안팎이라 중앙값이 크게 움직일 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_seoul_recovery_1_rec.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 서울 25개 구 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'서울 구별 아파트 가격',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'2021년 고점 못 넘긴 구',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'4곳',font=kr(ser,120),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'강남 144 · 도봉 93 (2021년 = 100)',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_seoul_recovery_thumb.png')
print('ok')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_seoul_recovery_1_rec_v2.png', '2021년 고점 넘긴 구 21곳, 못 넘긴 구 4곳', [('강남구', 144.2, '144.2', False), ('서초구', 134.1, '134.1', False), ('마포구', 113.9, '113.9', False), ('강북구', 98.1, '98.1', False), ('도봉구', 93.5, '93.5', True)], note='84㎡ 매매 중앙값 · 2021년 = 100 · 2026년 1~10월')
print('v2 ok')
