import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_cheolsan13_'
M=['25.1','2','3','4','5','6','7','8','9','10','11','12','26.1','2','3','4','5','6','7','8','9','10']
V=[4,5,15,14,22,17,6,7,8,10,2,8,14,6,20,6,0,3,7,1,2,0]
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'철산주공13단지 재건축 · 달마다 신고된 매매 건수(모든 면적)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'2026년 1~4월 46건, 조합설립인가(4월 29일) 뒤 13건',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.14,0.9,0.62])
cols=[GRAY]*12+[BLUE]*4+[NAVY]*6
ax.bar(range(len(V)),V,color=cols,width=0.7)
for i,v in enumerate(V): ax.text(i,v+0.4,str(v),ha='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_xticks(range(len(V))); ax.set_xticklabels(M,fontsize=12,color='#555')
ax.set_yticks([]); ax.set_ylim(0,26)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axvline(15.5,color=NAVY,lw=1.2,ls='--'); ax.text(15.7,23.5,'4월 29일 조합설립인가',fontsize=13,color=NAVY)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(광명시 철산동 주공13 · 해제 거래 뺌 · 4월 6건 가운데 인가 뒤 계약은 없음 · 2026년 9~10월은 신고 기간이 남아 덜 들어옴)',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'1_count.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'철산주공13단지 재건축',font=kr(ser,76),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'새 84㎡ 조합원 분양가',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'11억 2천',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'조합 추정 · 지금 84㎡ 거래는 15억 3천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_cheolsan13_1_count_v2.png', '2026년 1~4월 46건, 조합설립인가(4월 29일) 뒤 13건', [('2026년 1~4월|조합설립인가 전', 46, '46건', False), ('인가 뒤 ~ 9월|4월 29일 인가', 13, '13건', True)], note='철산주공13단지 매매 건수')
print('v2 ok')
