import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
# 그림 1 · 내 지분과 GH 지분이 바뀌는 순서
S=[('입주 때',25),('5년 뒤',45),('10년 뒤',65),('15년 뒤',85),('20년 뒤',100)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 지분적립형 · 한 집 안에서 내 지분과 GH 지분이 바뀌는 순서',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'GH 지분 75% → 0%, 사용료도 그만큼 줄어든다',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.17,0.88,0.58])
xs=list(range(len(S)))
mine=[p for _,p in S]; gh=[100-p for _,p in S]
ax.bar(xs,mine,color=NAVY,width=0.6)
ax.bar(xs,gh,bottom=mine,color=GRAY,width=0.6)
for x,(m,g) in zip(xs,zip(mine,gh)):
    ax.text(x,m/2,f'내 지분\n{m}%',ha='center',va='center',fontsize=15,color='white',fontweight='bold')
    if g: ax.text(x,m+g/2,f'GH\n{g}%',ha='center',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(xs); ax.set_xticklabels([a for a,_ in S],fontsize=16,color='#333')
ax.set_ylim(0,104); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'입주자모집공고 · 비즈워치(2026년 10월 30일) · 회색 GH 지분에 사용료(임대료)가 붙음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gwanggyojibun_1_share.png'); plt.close()
# 그림 2 · 처음 내 것이 되는 금액, 이의동 · 원천동 84㎡ 매매와 나란히
R=[('원천동 84㎡\n올해 매매 중앙값',128000,GRAY),('이의동 84㎡\n올해 매매 중앙값',119000,GRAY),('같은 단지 84㎡\n일반 공공분양가',94930,BLUE),('59㎡ 지분적립형\n입주 때 내는 지분 대금',17147,NAVY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'광교 지분적립형 · 수원 이의동 · 원천동 84㎡ 올해 매매와 나란히',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'이의동 84㎡ 11억 9천, 지분적립형 첫 대금 1억 7천',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.12,0.68,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+1500,y,won(v),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,150000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1~10월 · 전용 80~90㎡ · 해제 거래 뺌) · 입주자모집공고(59㎡B 6억 8,590만원의 25%)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gwanggyojibun_2_first.png'); plt.close()
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
d.text((W/2,360),'광교 지분적립형',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'처음 내 지분',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'25%',font=kr(ser,130),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'나머지 75%는 20년 동안 네 번',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gwanggyojibun_thumb.png')
