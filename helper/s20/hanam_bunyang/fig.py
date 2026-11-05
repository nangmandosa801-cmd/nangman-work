import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def won(v): return f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
def bars(R,title,head,foot,fn,xmax,h=7.8):
    fig=plt.figure(figsize=(11.55,h),dpi=120); fig.patch.set_facecolor('white')
    fig.text(0.045,0.955,title,fontsize=16,color=BLUE,va='top')
    fig.text(0.045,0.905,head,fontsize=25,color=NAVY,fontweight='bold',va='top')
    ax=fig.add_axes([0.33,0.15,0.6,0.64])
    ys=list(range(len(R)))[::-1]
    ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
    ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=14,color='#333')
    for y,(_,v,c) in zip(ys,R):
        ax.text(v+1500,y,won(v),va='center',fontsize=15,color=NAVY,fontweight='bold')
    ax.set_xlim(0,xmax); ax.set_xticks([])
    for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#C8D2DE')
    fig.text(0.045,0.025,foot,fontsize=11.5,color='#8A8578')
    fig.savefig(fn); plt.close()

R=[('위례 하남 위례롯데캐슬\n2016 · 올해 매매',165000,GRAY),('감일 새 아파트\n2019~2023 · 올해 매매',141000,GRAY),('더샵하남에디피스\n2024 · 올해 매매',140500,GRAY),
   ('하남유니온시티에일린의뜰\n2017 · 올해 매매',112150,GRAY),('교산 민간분양\n평당 3,200만원 × 34평',108800,BLUE),
   ('감일스윗시티 10단지 분양전환\n2025년 7월 1차 감정가',78500,BLUE),('교산 공공분양\n평당 2,200만원 × 34평',74800,NAVY)]
bars(R,'하남 분양 예정 · 84㎡ 보도 단가와 감정가를 옆 새 아파트 올해 매매 중앙값과 나란히',
     '교산 공공분양 84㎡ 7억 4,800만 · 감일 14억 1천',
     '분양 단가: 하남일보 2026년 3월 8일(업계 전망 · 확정 분양가 아님) · 감정가: 2025년 11월 21일 보도\n매매: 국토교통부 실거래 2026년 1~10월 · 전용 83~86㎡ · 해제 · 직거래 뺌',
     'img/nangman_hanam_bunyang_1_84.png',195000)

R=[('더샵하남에디피스 59㎡\n2024 · 올해 24건',116000,GRAY),('하남호반써밋에듀파크 59㎡\n2021 · 올해 29건',107500,GRAY),
   ('교산 A2 59㎡ 본청약\n2025년 평균 분양가',56800,BLUE),('교산 A5 59㎡\nA2처럼 17% 오르면',53400,NAVY),('교산 A5 59㎡\n2023년 사전청약 추정가',45639,NAVY)]
bars(R,'교산 A5 59㎡ 분양가 · 사전청약 추정가와 옆 새 아파트 59㎡ 올해 매매 중앙값',
     'A5가 17% 올라도 옆 59㎡보다 5억 4천 낮습니다',
     '분양가: 연합뉴스 · 매일경제 2023년 9월 20일(A5 추정) · 뉴시스 2025년 3월 31일(A2 본청약 · 사전청약 대비 약 17%)\n매매: 국토교통부 실거래 2026년 1~10월 · 하남시 덕풍동 · 신장동 · 전용 57~60㎡ · 해제 · 직거래 뺌',
     'img/nangman_hanam_bunyang_2_59.png',140000,h=7.0)

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 교산 · 감일 · 위례',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'하남 분양 예정 아파트',font=kr(ser,80),fill='#F4F1EA',anchor='mm')
d.text((W/2,492),'2027년 일정이 나온 곳',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'교산 2곳',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'A5 본청약 2027년 9월 · S1 2027년 분양 목표',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_bunyang_thumb.png')
