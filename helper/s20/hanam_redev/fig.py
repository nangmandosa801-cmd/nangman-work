import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 하남 84㎡ 값 사다리 (2026년 1~10월 중앙값)
R=[('덕풍 · 신장 1999년 이전 아파트','34건',64250,GRAY),
   ('덕풍 · 신장 2000~2010년 아파트','262건',83000,GRAY),
   ('덕풍 · 신장 2016~2021년 아파트','43건',109500,BLUE),
   ('미사 2014~2019년 아파트','419건',120000,BLUE),
   ('더샵하남에디피스 · C구역 재개발(2024년)','8건',140500,NAVY),
   ('감일 2019~2023년 아파트','110건',141000,BLUE)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 재개발 · 84㎡ 매매 중앙값(2026년 1~10월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'재개발로 지은 C구역 84㎡는 덕풍 1990년대 아파트의 2.2배',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.42,0.12,0.5,0.7])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[r[2] for r in R],color=[r[3] for r in R],height=0.66)
ax.set_yticks(ys); ax.set_yticklabels([f'{r[0]}\n{r[1]}' for r in R],fontsize=13.5,color='#333')
def won(v):
    e,m=divmod(v,10000); return f'{e}억 {m:,}만' if m else f'{e}억'
for y,r in zip(ys,R): ax.text(r[2]+1500,y,won(r[2]),va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(0,175000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.04,'남색 = 재개발로 새로 지은 단지 · 회색 = 덕풍 · 신장 2010년 이전 아파트 · 미사 = 망월 · 풍산 · 선동, 감일 = 감이 · 감일동',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.015,'국토교통부 아파트 매매 실거래(2026년 1~10월 계약 · 전용 83~86㎡ · 해제 · 직거래 뺌 · 11월 5일 내려받음)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_redev_1_ladder.png'); plt.close()

# 2. 하남 재개발 구역 단계
S=['추진위원회\n승인','정비구역\n지정','조합\n설립','사업시행\n인가','관리처분\n인가','이주 ·\n착공','입주']
Z=[('B구역 · 덕풍동 413-3 일원',0,'2026.6.25 추진위 승인 고시\n다음: 소유자 60% 동의로 정비계획 입안 신청',BLUE),
   ('E구역 · 하남시청역 일원 · 신장동 446-18',1,'2025.7.1 정비구역 지정 · 9월 추진위 승인\n다음: 조합 설립',BLUE),
   ('C구역 · 덕풍동 285-31 일원',6,'더샵하남에디피스 980가구\n2024년 입주',NAVY)]
fig=plt.figure(figsize=(11.55,7.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 재개발 지역 · 구역별 단계(2026년 11월 기준)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'다 지은 곳은 C구역 한 곳, B · E구역은 첫 단계입니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.04,0.1,0.92,0.7]); ax.set_xlim(-0.6,6.6); ax.set_ylim(-0.4,4.2); ax.axis('off')
for i,s in enumerate(S):
    ax.add_patch(plt.Rectangle((i-0.45,3.35),0.9,0.75,color='#EEF2F7'))
    ax.text(i,3.725,s,ha='center',va='center',fontsize=13.5,color=NAVY,fontweight='bold')
    if i<6: ax.annotate('',xy=(i+0.55,3.725),xytext=(i+0.45,3.725),arrowprops=dict(arrowstyle='->',color=GRAY))
for k,(nm,st,desc,c) in enumerate(Z):
    y=2.55-k*1.05
    ax.plot([-0.45,st],[y,y],color=c,lw=7,solid_capstyle='butt')
    ax.plot([st],[y],'o',ms=18,color=c)
    ax.text(-0.45,y+0.3,nm,fontsize=14.5,color=NAVY,fontweight='bold',va='bottom')
    ax.text(st+0.25,y-0.05,desc,fontsize=12.5,color='#333',va='center',ha='left') if st<4 else ax.text(st,y+0.3,desc.replace('\n',' · '),fontsize=12.5,color='#333',va='bottom',ha='right')
fig.text(0.045,0.05,'B구역은 2010년 지정 → 2015년 해제 뒤 다시 추진 · E구역은 2014년 지정 → 2017년 해제 뒤 2025년 다시 지정',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.022,'자료: 시티뉴스(2024 · 2025.7 · 2026.6.25) · 아주경제(2026.10.27) · MTN(2021.9.2)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_redev_2_steps.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 덕풍 · 신장 · 84㎡ 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'하남 재개발',font=kr(ser,96),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'다 지은 C구역 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'14억 500만',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'덕풍 1990년대 아파트 6억 4천의 2.2배',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_redev_thumb.png')
