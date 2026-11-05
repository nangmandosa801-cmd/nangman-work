import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def head(fig,sub,h):
    fig.text(0.045,0.955,sub,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,h,fontsize=28,color=NAVY,fontweight='bold',va='top')

# 1. 학암동 100㎡ 안팎 단지별 2026년 중앙값
R=[('위례신도시신안인스빌아스트로 · 2017',209000,5,1),('위례 센트로엘 · 2016',204500,7,1),('플로리체위례 · 2015',190000,9,1),('위례그린파크푸르지오 · 2016',169500,23,1),
   ('위례호반써밋 · 2021',173000,11,0),('힐스테이트센트럴위례 · 2021',172250,12,0),('위례숲우미린 · 2022',167500,3,0),('위례포레자이 · 2021',161500,4,0),('위례중흥에스-클래스 · 2022',158000,3,0),('위례우미린 · 2022',147000,5,0)]
fig=plt.figure(figsize=(11.55,9.2),dpi=120); fig.patch.set_facecolor('white')
head(fig,'학암동 아파트 · 전용 95~105㎡ 매매 중앙값 · 2026년 1~10월','남색 = 2015~2017년 단지 · 파랑 = 2021~2022년 단지')
ax=fig.add_axes([0.38,0.1,0.56,0.7])
ys=list(range(len(R)))[::-1]
for y,(lab,v,n,old) in zip(ys,R):
    ax.barh(y,v,height=0.62,color=NAVY if old else BLUE)
    ax.text(v+1500,y,f'{won(v)}  ({n}건)',va='center',fontsize=14,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in R],fontsize=14,color='#333')
ax.set_xlim(0,290000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(하남 학암동 · 전용 95~105㎡ · 해제 · 직거래 뺌 · 2026년 1~10월 계약) · 거래 3~5건 단지는 한두 건으로 값이 크게 움직일 수 있음',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_hagam_apt_1_danji.png'); plt.close()

# 2. 84㎡ 하남 위례와 감일
R=[('위례롯데캐슬\n학암동 · 2016',130000,165000),('감일 84㎡ 전체\n감이동 · 감일동',118000,141000),('감일한라비발디\n감이동 · 2019',110000,136250)]
fig=plt.figure(figsize=(11.55,7.0),dpi=120); fig.patch.set_facecolor('white')
head(fig,'학암동 아파트 · 84㎡ 매매 중앙값 · 2025년과 2026년','위례롯데캐슬 16억 5천, 감일보다 2억 4천 높습니다')
ax=fig.add_axes([0.25,0.13,0.68,0.62])
ys=list(range(len(R)))[::-1]
for y,(lab,a,b) in zip(ys,R):
    ax.barh(y+0.19,a,height=0.36,color=GRAY); ax.barh(y-0.19,b,height=0.36,color=NAVY if y==2 else BLUE)
    ax.text(a+1500,y+0.19,'2025년 '+won(a),va='center',fontsize=14,color='#555')
    ax.text(b+1500,y-0.19,'2026년 '+won(b)+f'  (+{(b/a-1)*100:.0f}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in R],fontsize=15,color='#333')
ax.set_xlim(0,250000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 · 직거래 뺌 · 2025년은 한 해, 2026년은 1~10월 계약)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_hagam_apt_2_84.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 위례 · 학암동 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'학암동 아파트',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'10년 된 단지가 더 높다',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,612),'1억 2천',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,722),'100㎡ 안팎 올해 중앙값 차이',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hagam_apt_thumb.png')
