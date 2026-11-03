import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'

# 1. 감일2지구 주변 84㎡ 올해 매매 중앙값
R=[('위례 하남 쪽(학암동)\n32건',165000,BLUE),('감일지구(감이 · 감일동)\n111건',141000,NAVY),('미사(망월 · 풍산 · 선동)\n425건',120000,GRAY),('하남 전체\n973건',112300,GRAY)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남감일2지구 위치 · 주변 동네 84㎡ 올해 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'감일지구 84㎡ 14억 1천, 위례보다 2억 4천 낮음',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.27,0.12,0.66,0.66])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.58)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,c) in zip(ys,R):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+1500,y,s,va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,205000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2026년 1월~10월 23일 계약 · 전용 83~86㎡ · 해제 거래 뺌) · 학암동 32건은 모두 위례롯데캐슬',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gamil2_1_price.png'); plt.close()

# 2. 일정
E=[('2026.10.29','신규택지\n후보지 발표',NAVY),('2026.11.3','토지거래허가\n3년 재지정',BLUE),('2027','3호선 연장\n착공 목표',GRAY),('2030','감일2 착공\n목표',NAVY),('2032','3호선 감일역\n개통 목표',BLUE),('2033~','신규택지\n입주 예상',GRAY)]
fig=plt.figure(figsize=(11.55,6.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.95,'하남감일2지구 · 발표에서 입주까지 나온 날짜',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.885,'3호선 감일역 2032년, 감일2 첫 입주는 2033년부터',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.04,0.12,0.92,0.62]); ax.set_xlim(-0.6,len(E)-0.4); ax.set_ylim(-1.3,1.3); ax.axis('off')
ax.plot([-0.4,len(E)-0.6],[0,0],color='#C8D2DE',lw=4,zorder=1)
for i,(d,t,c) in enumerate(E):
    ax.scatter([i],[0],s=520,color=c,zorder=2)
    ax.text(i,0.42,d,ha='center',va='bottom',fontsize=17,color=c,fontweight='bold')
    ax.text(i,-0.38,t,ha='center',va='top',fontsize=15,color='#333',linespacing=1.4)
fig.text(0.045,0.04,'국토교통부 10월 29일 발표 · 하남시 토지거래허가구역 재지정 보도 · 송파하남선 착공 · 개통 목표(MTN 10월 27일) · 비즈워치 10월 29일',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gamil2_2_steps.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감일 · 신규택지',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'하남감일2지구 위치',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'서하남IC → 감일역',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'860m',font=kr(ser,110),fill='#D4B04C',anchor='mm')
d.text((W/2,720),'감일동 · 감북동 일부 · 6,500가구',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gamil2_thumb.png')
