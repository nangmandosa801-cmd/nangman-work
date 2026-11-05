import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v):
    return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def head(fig,sub,h):
    fig.text(0.045,0.955,sub,fontsize=17,color=BLUE,va='top')
    fig.text(0.045,0.905,h,fontsize=28,color=NAVY,fontweight='bold',va='top')

# 1. 2026년 월별 84㎡ 중앙값
M=[('1월',127000,3),('2월',123000,2),('3월',132500,2),('4월',136000,5),('5월',135500,4),('6월',137400,1),('7월',138250,6),('8월',145000,3),('9월',143000,3),('10월',143000,3)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
head(fig,'감일한라비발디 시세 · 84㎡ 매매 월별 중앙값 · 2026년 1~10월','1월 12억 7천에서 10월 14억 3천')
ax=fig.add_axes([0.06,0.14,0.9,0.62])
xs=range(len(M))
for x,(lab,v,n) in zip(xs,M):
    c=NAVY if x>=7 else BLUE
    ax.bar(x,v-100000,bottom=100000,color=c,width=0.62)
    ax.text(x,v+700,f'{v/10000:.2f}억',ha='center',fontsize=13.5,color=NAVY,fontweight='bold')
    ax.text(x,101200,f'{n}건',ha='center',fontsize=12.5,color='white')
ax.axhline(110000,color=GRAY,lw=1.5,ls='--'); ax.text(-0.45,110600,'점선 = 2025년 중앙값 11억',ha='left',fontsize=13,color='#444',bbox=dict(facecolor='white',edgecolor='none',pad=2),zorder=5)
ax.set_xticks(list(xs)); ax.set_xticklabels([m[0] for m in M],fontsize=15,color='#333')
ax.set_ylim(100000,152000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(하남 감이동 감일한라비발디 · 전용 84.87~84.92㎡ · 해제 · 직거래 뺌 · 막대 안 숫자는 거래 건수)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_gamil_hanra_1_month.png'); plt.close()

# 2. 비슷한 연식 단지 짝
R=[('감일한라비발디\n2019 · 550m',110000,136250),('감일센트레빌\n2020 · 980m',104750,130000),('힐스테이트포웰시티\n2020 · 190m',131250,161500),('감일스타힐스\n2021 · 270m',115000,145000),('감일파크센트레빌\n2021 · 150m',123000,152000)]
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
head(fig,'감일한라비발디 시세 · 비슷한 연식 단지 84㎡ 매매 중앙값','2019~2021년 단지, 1년 새 오른 비율은 23~26%')
ax=fig.add_axes([0.27,0.11,0.66,0.67])
ys=list(range(len(R)))[::-1]
for y,(lab,a,b) in zip(ys,R):
    hi=lab.startswith('감일한라')
    ax.barh(y+0.19,a,height=0.36,color=GRAY); ax.barh(y-0.19,b,height=0.36,color=NAVY if hi else BLUE)
    ax.text(a+1500,y+0.19,'2025년 '+won(a),va='center',fontsize=13.5,color='#555')
    ax.text(b+1500,y-0.19,'2026년 '+won(b)+f'  (+{(b/a-1)*100:.0f}%)',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in R],fontsize=14.5,color='#333')
ax.set_xlim(0,240000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 · 직거래 뺌 · 2026년은 1~10월) · 거리는 단샘초 삼거리(3호선 감일 정거장 예정)까지 카카오맵 직선 거리',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_gamil_hanra_2_pair.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감일 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'감일한라비발디',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'84㎡ 올해 중앙값',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'13억 6천',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,722),'지난해 11억에서',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gamil_hanra_thumb.png')
