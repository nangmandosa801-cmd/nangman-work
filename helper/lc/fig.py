import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def clean(ax):
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#D5DCE6'); ax.tick_params(length=0)
# 1 neighbors 84 new-tenant jeonse
D=[('마포프레스티지자이 (2021)',12.5),('공덕SK리더스뷰 (2021)',12.4),('공덕더샵 (2018)',12.0),('마포그랑자이 (2020)',11.0),('더클래시 (2022)',10.95),('마포자이더센트리지 (2022)',10.5),('마포센트럴 아이파크 (2017)',9.0)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'라첼스 전세 · 옆 마포 새 아파트 84㎡ 올해 새 세입자 전세',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'2020년 뒤 지은 다섯 곳은 10억 5천~12억 5천',fontsize=31,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.08,0.58,0.74])
y=list(range(len(D)))
ax.barh(y,[v for _,v in D],color=[NAVY if int(n[-5:-1])>=2020 else GRAY for n,_ in D],height=0.6)
for i,(n,v) in enumerate(D): ax.text(v+0.1,i,f'{v:.2f}억'.replace('0억','억').replace('.0억','억'),va='center',fontsize=15,color=NAVY)
ax.set_yticks(y); ax.set_yticklabels([n for n,_ in D],fontsize=14,color='#444'); ax.invert_yaxis(); ax.set_xlim(0,14.5); ax.set_xticks([]); clean(ax)
fig.text(0.045,0.025,'국토교통부 아파트 전월세 실거래 · 2026년 1~10월 · 월세 없는 신규 계약 중앙값 · 공덕 · 아현 · 염리 · 대흥동',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_rachels_1_jeonse.png'); plt.close()
# 2 분양가 vs 매매 vs 전세
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'라첼스 84㎡ · 분양가와 옆 새 아파트 매매 · 전세',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'전세 11억이면 분양가의 63%',fontsize=31,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.12,0.86,0.66])
L=['라첼스 84㎡\n분양가(가장 높은 값)','옆 새 아파트 84㎡\n매매 중앙값','옆 새 아파트 84㎡\n새 세입자 전세','옆 새 아파트 84㎡\n갱신 전세']
V=[17.5,24.55,11.0,10.5]; C=[NAVY,GRAY,BLUE,GRAY]
ax.bar(range(4),V,color=C,width=0.58)
for i,v in enumerate(V): ax.text(i,v+0.4,f'{v}억'.replace('.0억','억'),ha='center',fontsize=19,color=NAVY,fontweight='bold')
ax.set_xticks(range(4)); ax.set_xticklabels(L,fontsize=14,color='#444'); ax.set_yticks([]); ax.set_ylim(0,28); clean(ax)
fig.text(0.045,0.025,'분양가: 2024년 6월 입주자모집공고 84D · E 가장 높은 값 · 매매 · 전세: 국토교통부 실거래 2026년 1~10월 · 같은 일곱 단지',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_rachels_2_ratio.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 2027년 3월 입주 · 1,101세대',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'라첼스 전세',font=kr(ser,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡는 옆 새 아파트',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'11억이 기준',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'마포 새 아파트 7곳 올해 실거래',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_rachels_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_rachels_1_jeonse_v2.png', '2020년 뒤 지은 다섯 곳은 10억 5천~12억 5천', [('마포프레스티지자이|2021', 12.5, '12.5억', True), ('공덕SK리더스뷰|2021', 12.4, '12.4억', False), ('마포그랑자이|2020', 11.0, '11억', False), ('더클래시|2022', 10.95, '10.95억', False), ('마포자이더센트리지|2022', 10.5, '10.5억', False)], note='라첼스 전세 · 옆 마포 새 아파트 84㎡ 올해 새 세입자 전세')
print('v2 ok')
