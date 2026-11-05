import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# (라벨, 84㎡ 2026년 1~10월 매매 중앙값 만원, 500m 안 여부)
P=[('하남풍산아이파크 5단지 2008 · 120m',104700,1),('동원베네스트 2008 · 680m',94250,0),('하남풍산센트레빌 2008 · 550m',91500,0),
   ('에코타운(B블럭) 2004 · 400m',99000,1),('진모루마을현대 2000 · 110m',83000,1),('한솔리치빌 1단지 2002 · 1.2km',70500,0),
   ('대명강변타운 2007 · 250m',92250,1),('벽산블루밍 2007 · 630m',82750,0),
   ('꿈동산신안 1994·95 · 370m',82500,1),('덕풍현대 1995·97 · 1.1km',63000,0)]
fig=plt.figure(figsize=(11.55,9.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'5호선 하남풍산 · 하남시청 · 하남검단산역 · 비슷한 해에 지은 단지끼리 84㎡ 올해 매매 중앙값',fontsize=15,color=BLUE,va='top')
fig.text(0.045,0.925,'역 500m 안이 9,500만~2억 8,500만원 높습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.37,0.09,0.56,0.76])
gap={2:2.8,5:2.8,7:1.6}
ys=[]; y=0
for i in range(len(P)):
    ys.append(y); y-=gap.get(i,1.0)
ax.barh(ys,[v for _,v,_ in P],color=[NAVY if ins else GRAY for *_,ins in P],height=0.78)
ax.set_yticks(ys); ax.set_yticklabels([l for l,_,_ in P],fontsize=13.5,color='#333')
for yy,(_,v,ins) in zip(ys,P):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+1500,yy,s,va='center',fontsize=14,color=NAVY,fontweight='bold' if ins else 'normal')
for i,t in [(0,'하남풍산역'),(3,'하남시청역 (3호선 환승 예정)'),(6,'하남검단산역')]:
    ax.text(1500,ys[i]+1.0,t,ha='left',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
for i in (2,5): ax.axhline(ys[i]-1.4,color='#C8D2DE',lw=1,ls='--')
ax.set_xlim(0,135000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.set_ylim(ys[-1]-0.7,ys[0]+1.6)
fig.text(0.045,0.03,'남색 = 역 500m 안 · 회색 = 밖 · 거리: 단지 가운데에서 가장 가까운 5호선 역까지 직선(오픈스트리트맵)\n국토교통부 실거래 2026년 1~10월 · 전용 83~86㎡ · 해제 · 직거래 뺌',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_hanam_station_1_pair.png'); plt.close()

# 2) 1994~2008년 단지 묶음 · 작년 vs 올해
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'5호선 하남 세 역 · 1994~2008년에 지은 단지 84㎡ 매매 중앙값 (각 해 1~10월)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.905,'차이가 1억 2,600만에서 1억 7,500만원으로 늘었습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.2,0.86,0.58])
xs=[0,1]; w=0.34
inn=[76700,89250]; out=[64100,71750]
b1=ax.bar([x-w/2-0.01 for x in xs],inn,w,color=NAVY,label='역 500m 안 8개 단지')
b2=ax.bar([x+w/2+0.01 for x in xs],out,w,color=GRAY,label='역 500m 밖 16개 단지')
for bars,vals in [(b1,inn),(b2,out)]:
    for b,v in zip(bars,vals):
        ax.text(b.get_x()+b.get_width()/2,v+1500,f'{v//10000}억 {v%10000:,}만',ha='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xticks(xs); ax.set_xticklabels(['2025년 1~10월\n(231건 · 199건)','2026년 1~10월\n(156건 · 182건)'],fontsize=15,color='#333')
ax.set_ylim(0,105000); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=14,frameon=False)
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래 · 하남시 덕풍 · 신장 · 창우동 · 전용 83~86㎡ · 해제 · 직거래 뺌\n500m: 단지 가운데에서 가장 가까운 5호선 역까지 직선(오픈스트리트맵)',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_hanam_station_2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 5호선 · 하남시청역',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'하남시청역 아파트',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,492),'5호선 역 500m 안 84㎡',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 7,500만원 더',font=kr(ser,88),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'1994~2008년 단지 · 올해 중앙값 8억 9천 vs 7억 2천',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_station_thumb.png')
