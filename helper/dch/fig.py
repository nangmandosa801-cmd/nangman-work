import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 그림 1: 대치동 84㎡ 월세 없는 전세 계약 월별 건수 (2026년 1~10월)
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
V=[73,36,33,27,36,35,36,24,18,10]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'대치동 84㎡ 전세 계약 건수 · 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1월 73건, 다른 달의 두 배',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.9,0.66])
cols=[NAVY]+[GRAY]*7+['#D5DCE5','#D5DCE5']
ax.bar(range(10),V,color=cols,width=0.62)
for i,v in enumerate(V): ax.text(i,v+1.2,f'{v}건',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xticks(range(10)); ax.set_xticklabels(M,fontsize=15,color='#333')
ax.set_ylim(0,85); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(8.5,30,'신고 기한 30일이 안 지나\n아직 덜 잡힌 달',ha='center',fontsize=13.5,color='#7A8590')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 10월 24일 기준 · 전용 83~86㎡ · 월세 없는 계약 328건)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_daechijeonse_1_month.png'); plt.close()

# 그림 2: 단지별 84㎡ 전세 중앙값 (건수 7건 이상)
R=[('대치SKVIEW (2017)',200000),('래미안대치팰리스 (2015)',180000),('대치르엘 (2021)',175000),('대치푸르지오써밋 (2023)',167500),('대치아이파크 (2008)',157500),
   ('대치삼성 (2000)',131000),('대치현대 (1999)',107000),('한보미도맨션1 (1983)',101500),('한보미도맨션2 (1985)',99750),('은마 (1979)',78000),('대치우성1 (1984)',77325),('쌍용대치1 (1983)',75500)]
fig=plt.figure(figsize=(11.55,9.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'대치동 단지별 84㎡ 전세 중앙값 · 2026년 1~10월',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.918,'같은 84㎡, 은마 7억 8천 · 래미안대치팰리스 18억',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.3,0.08,0.62,0.78])
ys=list(range(len(R)))[::-1]
c=[NAVY if '은마' in a or '팰리스' in a else (BLUE if v>=150000 else GRAY) for a,v in R]
ax.barh(ys,[v for _,v in R],color=c,height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_ in R],fontsize=14.5,color='#333')
for y,(_,v) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+2500,y,s,va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(0,245000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.025,'국토교통부 아파트 전월세 실거래 · 월세 없는 계약 · 7건 이상 단지 · 괄호는 지은 해',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_daechijeonse_2_danji.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 강남구 대치동 · 학군 이사',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'대치동 전세 시세',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 새 세입자',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'10억',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'2026년 1~10월 계약 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_daechijeonse_thumb.png')
