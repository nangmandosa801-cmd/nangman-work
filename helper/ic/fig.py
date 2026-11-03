import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'

# 1. 이천 2026년 새 아파트 84㎡ 전세 중앙값
R=[('트리쉐이드(중리동)',34000,46,NAVY),('어반퍼스트(중리동)',33000,32,NAVY),('힐스테이트 이천역 1단지',33000,23,BLUE),
   ('힐스테이트 이천역 2단지',31500,10,BLUE),('빌리브 어바인시티 1단지',30000,36,GRAY),('빌리브 어바인시티 2단지',30000,24,GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'이천 예미지 전세 기준 · 이천 2026년 새 아파트 84㎡ 올해 전세',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'중리동 우미린 두 단지 3억 3천~3억 4천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.12,0.63,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,*_ in R],fontsize=15,color='#333')
for y,(_,v,n,c) in zip(ys,R):
    ax.text(v+500,y,f'{won(v)}  ({n}건)',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,44000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(2026년 1~10월 계약 · 이천시 · 2026년 지은 아파트 · 전용 84㎡ · 월세 없는 계약 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_icheonyemiji_1_jeonse.png'); plt.close()

# 2. 예미지 84㎡A 분양가 · 중리동 매매 · 전세
R=[('예미지 84㎡A\n10층 이상 분양가',54700,NAVY),('중리동 새 아파트 84㎡\n올해 매매 중앙값',53000,GRAY),('중리동 새 아파트 84㎡\n올해 전세 중앙값',33400,BLUE)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'이천 예미지 잔금 · 전세를 받아도 남는 돈',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'분양가 5억 4,700만 − 전세 3억 3,400만 = 2억 1,300만',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.14,0.63,0.62])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.55)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    ax.text(v+600,y,won(v),va='center',fontsize=17,color=NAVY,fontweight='bold')
ax.set_xlim(0,66000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'청약홈 입주자모집공고(2025년 12월 12일) · 국토교통부 매매 · 전월세 실거래(2026년 1~10월 · 중리동 우미린 두 단지 · 매매 해제 거래 뺌)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_icheonyemiji_2_jangeum.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 이천 중리지구 · 11월 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'이천 예미지',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'입주기간',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'11개월',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'2026년 11월 ~ 2027년 9월 30일',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_icheonyemiji_thumb.png')
