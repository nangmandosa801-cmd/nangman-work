import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'

# 1. 분양가와 주변 동별 84㎡ 올해 매매 중앙값
R=[('군자동 84㎡\n(45건)',70500,GRAY),('엘리프 시흥 더프라임\n84㎡ 분양가 상단',59930,NAVY),('엘리프 시흥 더프라임\n84㎡ 분양가 하단',56910,BLUE),
   ('장현동 84㎡\n(192건)',55000,GRAY),('4개 동 합계 84㎡\n(298건)',54300,GRAY),('정왕동 84㎡\n(50건)',41200,GRAY),('거모동 84㎡\n(11건)',39500,GRAY)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'엘리프 시흥 더프라임 분양가 · 주변 2015년 이후 아파트 84㎡ 올해 매매 중앙값',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.912,'4개 동 중앙값보다 2,610만~5,630만원 높다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.11,0.66,0.7])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14.5,color='#333')
for y,(_,v,c) in zip(ys,R):
    ax.text(v+700,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,86000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'모집공고(2026년 10월 29일) 주택가격 · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 시흥 거모·정왕·군자·장현동 · 2015년 이후 · 전용 80~86㎡ · 해제 거래 뺌)',fontsize=11,color='#8A8578')
fig.savefig('img/nangman_siheung_1_price.png'); plt.close()

# 2. 단지별 84㎡ 올해 매매 중앙값 (9건 이상)
C=[('시흥장현금강펜테리움센트럴파크\n군자동 · 2021',72500,30),('장현호반써밋\n장현동 · 2020',59700,60),('시흥능곡역모아미래도에듀포레\n장현동 · 2020',55000,59),
   ('제일풍경채에듀\n장현동 · 2020',54000,23),('장현동원로얄듀크메트로포레\n군자동 · 2021',53000,15),('시흥능곡역장현리슈빌퍼스트클래스\n장현동 · 2020',50900,45),
   ('시흥금강펜테리움오션베이\n정왕동 · 2023',49000,17),('시화MTV호반써밋더퍼스트오션\n정왕동 · 2022',40500,9),('파라곤센트럴오션시티\n정왕동 · 2023',39500,18),('군자서희스타힐스\n거모동 · 2023',39500,11)]
fig=plt.figure(figsize=(11.55,10.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'시흥 거모동 · 주변 2015년 이후 아파트 84㎡ · 단지별 올해 매매 중앙값(9건 이상)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.922,'분양가 5억 9,930만원보다 높은 단지는 1곳',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.09,0.58,0.76])
ys=list(range(len(C)))[::-1]
ax.barh(ys,[v for _,v,_ in C],color=[NAVY if v>=59930 else GRAY for _,v,_ in C],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in C],fontsize=13,color='#333')
for y,(_,v,n) in zip(ys,C):
    ax.text(v+600,y,f'{won(v)} ({n}건)',va='center',fontsize=14,color=NAVY,fontweight='bold',zorder=3,bbox=dict(fc='white',ec='none',pad=1.5))
[ax.plot([59930,59930],[k+0.32,k+0.68],color=BLUE,lw=2.5) for k in range(-1,len(C)-1)]; ax.text(59930,len(C)-0.35,'분양가 상단 5억 9,930만',color=BLUE,fontsize=13,ha='center',va='bottom',bbox=dict(fc='white',ec='none',pad=1.5))
ax.set_xlim(0,92000); ax.set_ylim(-0.6,len(C)-0.1); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 · 전용 80~86㎡ · 해제 거래 뺌) · 동 이름은 실거래 신고 기준',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_siheung_2_danji.png'); plt.close()

# 썸네일 C형
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 시흥 거모지구 · 분양가',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'엘리프 시흥 더프라임',font=kr(ser,78),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'84㎡ 분양가',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'5억 9,930만',font=kr(ser,90),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'주변 84㎡ 올해 매매 중앙값 5억 4,300만',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_siheung_thumb.png')
