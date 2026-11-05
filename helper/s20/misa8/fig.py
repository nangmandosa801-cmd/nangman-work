import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
SRC='국토교통부 아파트 매매 실거래(2025년 · 2026년 각 1~10월 계약 · 하남 망월동 · 해제 · 직거래 뺌 · 중앙값)'
def eok(v):
    e,r=divmod(int(v),10000)
    return f'{e}억 {r:,}만' if r else f'{e}억'
# 1. 스타힐스 평형별 1년 변화
T=[('51㎡ (공급 71㎡)',78000,106500,36.5),('59㎡ (공급 82㎡)',93500,117050,25.2),('75㎡ (공급 103㎡)',102400,131250,28.2),('84㎡ (공급 117㎡)',106000,134750,27.1)]
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'미사강변도시 8단지 매매 · 미사강변 스타힐스 평형별 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.918,'네 평형 모두 1년 새 25% 넘게 올랐습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.22,0.13,0.70,0.69])
ys=[];y=0;labels=[]
for nm,a,b,pc in T:
    ax.barh(y+0.21,a/10000,height=0.4,color=GRAY); ax.barh(y-0.21,b/10000,height=0.4,color=NAVY)
    ax.text(a/10000+0.15,y+0.21,f'2025년 {eok(a)}',va='center',fontsize=13.5,color='#555')
    ax.text(b/10000+0.15,y-0.21,f'2026년 {eok(b)}  (+{pc}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ys.append(y); labels.append(nm); y-=1.25
ax.set_yticks(ys); ax.set_yticklabels(labels,fontsize=15,color='#333')
ax.set_xlim(0,21); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.045,'회색 = 2025년 1~10월 · 남색 = 2026년 1~10월 · 앞 숫자는 전용면적',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.018,SRC,fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa8_1_size.png'); plt.close()

# 2. 같은 2016년 단지 84㎡
P=[('미사강변푸르지오\n미사역 795m',120000,143800,19.8),('미사강변 스타힐스(8단지)\n미사역 1,151m',106000,134750,27.1),('미사강변 센텀팰리스\n미사역 885m',98000,120000,22.4)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'미사강변도시 8단지 · 2016년에 지은 옆 단지 84㎡ 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'푸르지오와 차이가 1억 4천에서 9천으로 줄었습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.14,0.62,0.64])
ys=[];y=0
for nm,a,b,pc in P:
    c=NAVY if '8단지' in nm else BLUE
    ax.barh(y+0.21,a/10000,height=0.4,color=GRAY); ax.barh(y-0.21,b/10000,height=0.4,color=c)
    ax.text(a/10000+0.15,y+0.21,f'2025년 {eok(a)}',va='center',fontsize=13.5,color='#555')
    ax.text(b/10000+0.15,y-0.21,f'2026년 {eok(b)}  (+{pc}%)',va='center',fontsize=15,color=NAVY,fontweight='bold')
    ys.append(y); y-=1.25
ax.set_yticks(ys); ax.set_yticklabels([n for n,*_ in P],fontsize=15,color='#333')
ax.set_xlim(0,22); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.05,'회색 = 2025년 1~10월 · 색 막대 = 2026년 1~10월 · 미사역까지는 오픈스트리트맵 단지 가운데 기준 직선거리',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.022,'국토교통부 아파트 매매 실거래(전용 83~86㎡ · 해제 · 직거래 뺌 · 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa8_2_pair.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 미사 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'미사강변도시 8단지',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'스타힐스 84㎡ 1년 새',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'27% 상승',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,722),'10억 6,000만 → 13억 4,750만 · 1~10월 중앙값',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa8_thumb.png')
