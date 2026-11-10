import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    v=int(v); return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
g=pd.read_pickle('g.pkl').sort_values('m26',ascending=False)
fn='img/nangman_seoul_jeonse_ratio_1_gu.png'
fig=plt.figure(figsize=(11.55,13.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.972,'서울 전세가율 · 25개 구 84㎡ · 2026년 1~10월 · 매매 중앙값이 높은 구부터',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.942,'매매 31억 강남구는 32%, 매매 6억 2천 도봉구는 73%',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.21,0.07,0.72,0.835])
ys=list(range(len(g)))[::-1]
for y,(gu,row) in zip(ys,g.iterrows()):
    col=NAVY if row.m_rank<=5 else (BLUE if row.m_rank>=21 else GRAY)
    ax.barh(y,row.ratio,height=0.62,color=col)
    ax.text(row.ratio+0.8,y,f'{row.ratio:.1f}%',va='center',fontsize=14,color=NAVY if col!=GRAY else '#555',fontweight='bold' if col!=GRAY else 'normal')
ax.set_yticks(ys); ax.set_yticklabels([f'{gu}  매매 {won(r.m26)}' for gu,r in g.iterrows()],fontsize=13.5,color='#333')
ax.set_xlim(0,82); ax.set_xticks([])
for x in (40,50,60,70): ax.axvline(x,color='#E3E8EE',lw=1,zorder=0); ax.text(x,len(g)-0.2,f'{x}%',fontsize=11,color='#8A8578',ha='center',va='bottom')
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.036,'국토교통부 아파트 실거래 · 전용 83~86㎡ · 매매는 해제 · 직거래 뺀 중앙값 · 전세는 월세 없는 신규 계약 보증금 중앙값',fontsize=11.5,color='#8A8578')
fig.text(0.045,0.014,'남색 = 매매 중앙값 상위 5개 구 · 파랑 = 하위 5개 구 · 막대 = 전세 중앙값 ÷ 매매 중앙값',fontsize=11.5,color='#8A8578')
fig.savefig(fn); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 서울 25개 구 · 84㎡ 전세가율',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'서울 전세가율',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'비싼 동네일수록 낮을까',font=kr(ser,56),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'강남 32% · 도봉 73%',font=kr(ser,86),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'새 세입자 전세 ÷ 매매 중앙값 · 2026년 1~10월',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_seoul_jeonse_ratio_thumb.png')
print('ok')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_seoul_jeonse_ratio_1_gu_v2.png', '매매 31억 강남구는 32%, 매매 6억 2천 도봉구는 73%', [('강남구|매매 31억', 32.4, '32.4%', True), ('서초구|매매 29억 5,000만', 38.6, '38.6%', False), ('양천구|매매 11억 9,000만', 58.8, '58.8%', False), ('금천구|매매 7억 2,000만', 67.4, '67.4%', False), ('도봉구|매매 6억 2,000만', 72.6, '72.6%', False)], note='서울 84㎡ 전세가율 · 2026년 1~10월 · 25개 구는 아래 표')
print('v2 ok')
