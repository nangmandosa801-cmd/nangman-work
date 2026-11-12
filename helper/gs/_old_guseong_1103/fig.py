import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
R=[('e편한세상 구성역 플랫폼시티\n(2024년 · 마북동)',147500,GRAY),('보정동 84㎡\n(199건)',95800,GRAY),('힐스테이트 구성\n(2023년 · 언남동)',87500,GRAY),('중앙하이츠 구성 플랫폼시티\n84㎡ 분양가',85210,NAVY),('마북동 84㎡\n(294건)',72600,BLUE),('언남동 84㎡\n(151건)',62500,GRAY),('청덕동 84㎡\n(82건)',41250,GRAY)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'중앙하이츠 구성 플랫폼시티 분양가 · 구성역 주변 84㎡ 올해 매매 중앙값과 나란히',fontsize=16.5,color=BLUE,va='top')
fig.text(0.045,0.905,'84㎡ 8억 5,210만, 마북동 중앙값보다 1억 2,610만 높다',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.11,0.63,0.69])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14.5,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+1500,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,180000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 모집공고(2026년 10월 29일) · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 전용 80~86㎡ · 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_guseong_1_price.png'); plt.close()

M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']; C=[293,160,179,200,190,293,41,55,58,39]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'구성역 주변 4개 동(마북 · 언남 · 청덕 · 보정) 아파트 매매 건수 · 2026년',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'7월 5일 토지거래허가 뒤 한 달 39~58건',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.12,0.88,0.66])
ax.bar(M,C,color=[BLUE]*6+[NAVY]*4,width=0.62)
for i,c in enumerate(C): ax.text(i,c+5,f'{c}',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_ylim(0,330); ax.set_yticks([]); ax.tick_params(axis='x',labelsize=15,colors='#333')
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 모든 면적 · 해제 거래 뺌) · 10월은 신고 기한이 남아 늘어날 수 있음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_guseong_2_count.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 용인 기흥 · 구성역 청약',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,350),'중앙하이츠 구성',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,465),'84㎡ 분양가',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'8억 5,210만',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'마북동 84㎡ 올해 중앙값 7억 2,600만',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_guseong_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_guseong_1_price_v2.png', '84㎡ 8억 5,210만, 마북동 중앙값보다 1억 2,610만 높다', [('e편한세상 구성역 플랫폼시티|2024년 · 마북동', 147500.0, '14억 7,500만', False), ('보정동 84㎡|199건', 95800.0, '9억 5,800만', False), ('중앙하이츠 구성 플랫폼시티 84㎡ 분양가', 85210.0, '8억 5,210만', True), ('마북동 84㎡|294건', 72600.0, '7억 2,600만', False), ('청덕동 84㎡|82건', 41250.0, '4억 1,250만', False)], note='중앙하이츠 구성 플랫폼시티 분양가 · 구성역 주변 84㎡ 올해 매매 중앙값과 나란히')
bars('img/nangman_guseong_2_count_v2.png', '7월 5일 토지거래허가 뒤 한 달 39~58건', [('6월', 293.0, '293건', False), ('7월', 41.0, '41건', True), ('8월', 55.0, '55건', False), ('9월', 58.0, '58건', False), ('10월', 39.0, '39건', False)], note='구성역 주변 4개 동(마북 · 언남 · 청덕 · 보정) 아파트 매매 건수 · 2026년')
print('v2 ok')
