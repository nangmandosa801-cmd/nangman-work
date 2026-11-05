import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    e,m=divmod(int(round(v)),10000)
    return f'{e}억 {m:,}만' if m else f'{e}억'
def bars(R,fn,sub,head,src,xmax,h=7.6):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.955,sub,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,head,fontsize=28,color=NAVY,fontweight='bold',va='top')
    ax=fig.add_axes([0.30,0.12,0.63,0.66])
    ys=list(range(len(R)))[::-1]
    ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
    ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
    for y,(_,v,c) in zip(ys,R): ax.text(v+xmax*0.012,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.set_xlim(0,xmax); ax.set_xticks([])
    for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#C8D2DE')
    fig.text(0.045,0.03,src,fontsize=12.5,color='#8A8578')
    fig.savefig(fn); plt.close()
# 국토교통부 매매 실거래 2026년 1~10월 · 수원 영통구 원천동 · 이의동 · 전용 55~65㎡ · 해제 뺌 · 중앙값(만원)
bars([('원천동 광교호반베르디움\n59㎡ (2014년 · 54건)',110000,GRAY),('이의동 광교역참누리포레스트\n59㎡ (2015년 · 36건)',74500,GRAY),
      ('광교 자연앤센트레빌\n59㎡B 분양가',68590,NAVY),('원천동 원천레이크파크\n59㎡ (1999년 · 53건)',49900,GRAY)],
     'img/nangman_gwanggyo_rate_1_price.png','광교 자연앤센트레빌 청약 · 59㎡ 분양가와 원천동 · 이의동 59㎡ 올해 매매',
     '59㎡B 6억 8,590만, 옆 광교호반베르디움은 11억',
     '공고문 분양가(59㎡B 10층 이상) · 국토교통부 아파트 매매 실거래(2026년 1~10월 · 해제 거래 뺌 · 단지별 중앙값)',130000)
# 국토교통부 전월세 실거래 2026년 1~10월 · 원천동 · 이의동 · 2010년 이후 · 전용 55~65㎡ · 월세 없는 계약 중앙값
bars([('원천동 · 이의동 59㎡\n새 세입자 전세 (63건)',55000,GRAY),('원천동 · 이의동 59㎡\n갱신 전세 (59건)',47250,GRAY),
      ('광교 자연앤센트레빌 59㎡\n첫 임대보증금',33000,NAVY),('광교 자연앤센트레빌 59㎡B\n입주 때 지분 대금 25%',17147,BLUE)],
     'img/nangman_gwanggyo_rate_2_deposit.png','광교 자연앤센트레빌 지분적립형 · 처음 드는 돈과 옆 59㎡ 전세',
     '첫 임대보증금 3억 3천, 옆 59㎡ 새 전세는 5억 5천',
     '입주자모집공고 · 비즈워치(2026년 10월 30일) · 국토교통부 전월세 실거래(2026년 1~10월 · 2010년 이후 지은 아파트 · 월세 없는 계약)',66000)
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광교 A17 · 청약 결과',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'광교 자연앤센트레빌',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'59㎡ 분양가',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'6억 8,590만',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,710),'옆 광교호반베르디움 59㎡ 올해 11억',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gwanggyo_rate_thumb.png')
