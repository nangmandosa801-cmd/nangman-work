import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 그림 1: 목동 · 신정동 단지별 84㎡ 새 세입자 전세 중앙값 (새 세입자 계약 7건 이상)
R=[('아이파크 (신정동 · 2002)',112500),('목동힐스테이트 (2016)',98350),('래미안목동아델리체 (2021)',96500),('목동파크자이 (2019)',95000),
   ('목동청구한신 (1997)',91000),('목동현대3차 (1997)',83000),('목동롯데캐슬마에스트로 (2019)',83000),('롯데캐슬위너 (2005)',81500),
   ('호반써밋목동 (2022)',80000),('목동대림 (1994)',77000),('쌍용 (신정동 · 1992)',66000),('신트리3 (2000)',61000),('목동우성2 (2000)',55000),('푸른마을4 (2002)',49000)]
HI={'목동힐스테이트 (2016)','목동우성2 (2000)','래미안목동아델리체 (2021)','호반써밋목동 (2022)'}
fig=plt.figure(figsize=(11.55,9.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'목동 전세 시세 · 단지별 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.922,'같은 84㎡, 4억 9천부터 11억 2,500만까지',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.33,0.07,0.6,0.79])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v in R],color=[NAVY if a in HI else GRAY for a,_ in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_ in R],fontsize=14.5,color='#333')
for y,(_,v) in zip(ys,R): ax.text(v+1200,y,won(v),va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(0,135000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.022,'국토교통부 아파트 전월세 실거래(2026년 1~10월 · 전용 83~86㎡ · 월세 없는 신규 계약 · 단지별 7건 이상) · 남색은 본문 짝 비교 단지',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_mokdong_jeonse_1_danji.png'); plt.close()

# 그림 2: 목동 · 신정동 아파트 전세 계약 월별 건수 (전체 면적 · 월세 없는 계약)
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
V=[512,382,420,381,410,371,435,328,283,238]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'목동 · 신정동 아파트 전세 계약 건수 · 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1월 512건, 2~8월 평균의 1.3배',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.9,0.66])
cols=[NAVY]+[GRAY]*7+['#D5DCE5','#D5DCE5']
ax.bar(range(10),V,color=cols,width=0.62)
for i,v in enumerate(V): ax.text(i,v+8,f'{v}건',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(range(10)); ax.set_xticklabels(M,fontsize=15,color='#333')
ax.set_ylim(0,590); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(8.5,330,'신고 기한 30일이 안 지나\n아직 덜 잡힌 달',ha='center',fontsize=13.5,color='#7A8590')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 10월 23일 계약까지 · 양천구 목동 · 신정동 · 전체 면적 · 월세 없는 계약)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_mokdong_jeonse_2_month.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 양천구 목동 · 신정동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'목동 전세 시세',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 새 세입자',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'7억 5천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'대치동 10억보다 2억 5천 낮게',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_mokdong_jeonse_thumb.png')

# ==== 11/10 새 기준(2D · 막대 5개 이하 · 결론 한 줄) — fig2d ====
import sys; sys.path.insert(0, '/home/claude/helper/pg')
from fig2d import bars, cards3
bars('img/nangman_mokdong_jeonse_1_danji_v2.png', '같은 84㎡, 4억 9천부터 11억 2,500만까지', [('아이파크|신정동 · 2002', 112500.0, '11억 2,500만', True), ('목동힐스테이트|2016', 98350.0, '9억 8,350만', False), ('롯데캐슬위너|2005', 81500.0, '8억 1,500만', False), ('목동우성2|2000', 55000.0, '5억 5,000만', False), ('푸른마을4|2002', 49000.0, '4억 9,000만', False)], note='목동 전세 시세 · 단지별 84㎡ 새 세입자 전세 중앙값 · 2026년 1~10월')
bars('img/nangman_mokdong_jeonse_2_month_v2.png', '1월 512건, 2~8월 평균의 1.3배', [('1월', 512.0, '512건', True), ('2월', 382.0, '382건', False), ('5월', 410.0, '410건', False), ('8월', 328.0, '328건', False), ('10월', 238.0, '238건', False)], note='목동 · 신정동 아파트 전세 계약 건수 · 2026년 1~10월')
print('v2 ok')
