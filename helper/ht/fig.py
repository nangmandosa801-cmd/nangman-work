import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
Q=['25년\n1분기','2분기','3분기','4분기','26년\n1분기','2분기','3분기']
GAM=[114000,117000,119000,122000,136500,141000,141000]
MIS=[96500,98250,101250,105000,113000,120000,125000]
GN=[61,65,89,45,36,38,33]; MN=[147,230,234,220,143,157,114]
def won(v): return f'{v//10000}억 {v%10000:,}' if v%10000 else f'{v//10000}억'

fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 감일 · 미사 아파트 84㎡ 실거래 중앙값 (분기별)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1년 반 동안 감일 2억 7천만원, 미사 2억 8,500만원 올랐습니다',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.84,0.64]); x=range(len(Q))
ax.plot(x,GAM,color=NAVY,lw=3.5,marker='o',ms=9); ax.plot(x,MIS,color=BLUE,lw=3.5,marker='o',ms=9)
for i,ha,dx in ((0,'center',0),(len(Q)-1,'right',-0.12)):
    ax.text(i+dx,GAM[i]+1600,won(GAM[i]),ha=ha,fontsize=15,color=NAVY,fontweight='bold')
    ax.text(i+dx,MIS[i]+1600 if i else MIS[i]-3600,won(MIS[i]),ha=ha,fontsize=15,color=BLUE,fontweight='bold')
ax.text(len(Q)-1+0.15,GAM[-1],'   감일',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.text(len(Q)-1+0.15,MIS[-1],'   미사',va='center',fontsize=16,color=BLUE,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(Q,fontsize=14,color='#333')
ax.set_ylim(85000,152000); ax.set_xlim(-0.4,len(Q)-0.2); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 1월~2026년 9월 계약 · 전용 83~86㎡ · 해제 거래 뺌) · 감일=감일동 · 감이동, 미사=망월동 · 풍산동 · 선동 · 단위 만원',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_hanamtoji_1_price.png'); plt.close()

fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 감일 · 미사 아파트 84㎡ 매매 건수 (분기별)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'3분기 거래, 1년 전보다 미사 120건 · 감일 56건 적었습니다',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.84,0.64]); w=0.38
ax.bar([i-w/2 for i in x],MN,width=w,color=BLUE,label='미사'); ax.bar([i+w/2 for i in x],GN,width=w,color=NAVY,label='감일')
for i in x:
    ax.text(i-w/2,MN[i]+4,str(MN[i]),ha='center',fontsize=13,color=BLUE,fontweight='bold')
    ax.text(i+w/2,GN[i]+4,str(GN[i]),ha='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(Q,fontsize=14,color='#333'); ax.set_yticks([]); ax.set_ylim(0,265)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(frameon=False,fontsize=15,loc='upper right')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 1월~2026년 9월 계약 · 전용 83~86㎡ · 해제 거래 뺌) · 단위 건',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_hanamtoji_2_count.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 토지거래허가',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'하남 토지거래허가구역',font=kr(ser,72),fill='#F4F1EA',anchor='mm')
d.text((W/2,460),'감일 · 감북 · 미사',font=kr(ser,56),fill='#F4F1EA',anchor='mm')
d.text((W/2,595),'다시 3년',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2026년 11월 3일 ~ 2029년 11월 2일',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanamtoji_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_hanamtoji_2_count_v2.png', '3분기 거래, 1년 전보다 미사 120건 · 감일 56건 적었습니다', [('미사|2025년 3분기', 234.0, '234건', False), ('미사|2026년 3분기', 114.0, '114건', True), ('감일|2025년 3분기', 89.0, '89건', False), ('감일|2026년 3분기', 33.0, '33건', False)], note='하남 감일 · 미사 아파트 84㎡ 매매 건수 (분기별)')
print('v2 ok')
