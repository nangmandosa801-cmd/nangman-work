import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 그림 1 · 59㎡ 분양가와 원천동 · 이의동 올해 59㎡ 매매
R=[('원천동 광교호반베르디움\n(2014년) 59㎡ 매매',110000,GRAY),('이의동 광교역참누리포레스트\n(2015년) 59㎡ 매매',74500,GRAY),('광교 자연앤 센트레빌\n59㎡ 분양가(가장 높은 타입)',68590,NAVY),('원천동 원천레이크파크\n(1999년) 59㎡ 매매',49900,BLUE)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 자연앤 센트레빌 분양가 · 원천동 · 이의동 올해 59㎡ 매매 중앙값과 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'59㎡ 6억 8,590만, 옆 광교호반베르디움보다 4억 1천 낮다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.12,0.63,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+1500,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,135000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'입주자모집공고(2026년 10월 30일) · 국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 해제 거래 뺌 · 전용 55~65㎡ 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gwanggyo_1_price.png'); plt.close()
# 그림 2 · 지분 나눠 내는 순서 (59㎡B)
S=[('입주 때\n(계약금+잔금)',17147,25),('5년 뒤',13718,45),('10년 뒤',13718,65),('15년 뒤',13718,85),('20년 뒤',10288,100)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 자연앤 센트레빌 지분적립형 · 59㎡B(10층 이상) 6억 8,590만원 기준',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'입주 때 25%, 나머지 75%는 20년 동안 네 번',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.17,0.88,0.58])
xs=range(len(S))
ax.bar(xs,[v for _,v,_ in S],color=[NAVY]+[BLUE]*3+[GRAY],width=0.58)
for x,(_,v,p) in zip(xs,S):
    ax.text(x,v+500,won(v),ha='center',fontsize=17,color=NAVY,fontweight='bold')
    ax.text(x,v/2,f'내 지분\n{p}%',ha='center',va='center',fontsize=15,color='white',fontweight='bold')
ax.set_xticks(list(xs)); ax.set_xticklabels([a for a,_,_ in S],fontsize=15,color='#333')
ax.set_ylim(0,20500); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'입주자모집공고 · 비즈워치(2026년 10월 30일) · 5년 뒤부터 내는 돈에는 기간이자가 더해짐',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gwanggyo_2_share.png'); plt.close()
# 썸네일 C형
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광교 A17 · 지분적립형',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'광교 자연앤 센트레빌',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'59㎡ 입주 때',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 7천',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'분양가 6억 8,590만원의 25%',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gwanggyo_thumb.png')
