import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 노선 그림(위치 관계만 나타낸 단순 그림)
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'송파하남선 노선도 · 오금역~하남시청역 11.7km · 새 정거장 6곳',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'하남 다섯 정거장 중 아파트 옆은 감일과 하남시청역',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.03,0.1,0.94,0.68]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
S=[('오금역','3호선 · 출발',5,GRAY),('100','송파 방이동\n위례성대로 삼거리',19,BLUE),('101','감일\n단샘초 앞 삼거리',34,NAVY),
   ('102','교산지구\n남쪽',49,BLUE),('103','교산지구\n가운데',63,BLUE),('104','교산지구\n북쪽',77,BLUE),('105','하남시청역\n5호선 갈아타기',93,NAVY)]
ax.plot([5,93],[55,55],color=BLUE,lw=7,solid_capstyle='round',zorder=1)
for nm,sub,x,c in S:
    ax.scatter([x],[55],s=900 if c==NAVY else 620,color='white',edgecolors=c,linewidths=5,zorder=3)
    ax.text(x,72,nm,ha='center',va='center',fontsize=19 if c!=GRAY else 17,fontweight='bold',color=c if c!=GRAY else '#555')
    ax.text(x,36,sub,ha='center',va='top',fontsize=14.5,color='#333',linespacing=1.5)
ax.add_patch(plt.Rectangle((27,8),14,8,color='#E8EEF5',zorder=0)); ax.text(34,12,'지금 아파트 있음',ha='center',va='center',fontsize=13.5,color=NAVY)
ax.add_patch(plt.Rectangle((86,8),14,8,color='#E8EEF5',zorder=0)); ax.text(93,12,'지금 아파트 있음',ha='center',va='center',fontsize=13.5,color=NAVY)
ax.add_patch(plt.Rectangle((42,8),42,8,color='#F4F6F9',zorder=0)); ax.text(63,12,'교산지구 안 · 아파트 짓기 전',ha='center',va='center',fontsize=13.5,color='#7A8590')
fig.text(0.045,0.03,'위치 관계만 나타낸 그림(거리 비율 아님) · 하남 Times 2024년 7월 3일 · 경인일보 2024년 7월 4일 · 땅집고 2025년 12월 26일 보도 · 번호는 계획상 정거장 번호',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_songpahanam_route_1_route.png'); plt.close()
# 2. 짝 비교
P=[('감일파크센트레빌 2021 · 140m',152000,1),('e편한세상감일 2021 · 560m',149000,0),
   ('힐스테이트포웰시티 2020 · 180m',161500,1),('감일센트레빌 2020 · 980m',130000,0),
   ('감일수자인 2022 · 410m',147500,1),('감일푸르지오마크베르 2023 · 580m',137000,0),
   ('하남한솔솔파크 2006 · 430m',86700,1),('하남자이 2006 · 880m',73000,0),
   ('에코타운(B블럭) 2004 · 420m',99000,1),('한솔리치빌(1단지) 2002 · 1.2km',70500,0)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'송파하남선 역 500m 안과 바깥 · 비슷한 해에 지은 단지끼리 84㎡ 올해 매매 중앙값',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.915,'감일은 3천만~3억 1,500만, 하남시청역은 1억 3,700만~2억 8,500만',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.36,0.1,0.57,0.74])
ys=[]; y=0
for i,(lab,v,ins) in enumerate(P):
    ys.append(y); y-= (1.0 if i%2==0 else (2.6 if i==5 else 1.6))
ax.barh(ys,[v for _,v,_ in P],color=[NAVY if ins else GRAY for *_,ins in P],height=0.8)
ax.set_yticks(ys); ax.set_yticklabels([l for l,_,_ in P],fontsize=13.5,color='#333')
for yy,(_,v,ins) in zip(ys,P):
    s=f'{v//10000}억 {v%10000:,}만' if v%10000 else f'{v//10000}억'
    ax.text(v+1500,yy,s,va='center',fontsize=14,color=NAVY,fontweight='bold' if ins else 'normal')
ax.set_xlim(0,190000); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.axhline(ys[5]-0.9,color='#C8D2DE',lw=1,ls='--')
ax.text(1500,ys[0]+0.8,'101 감일 (지하철 아직 없음)',ha='left',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.text(1500,ys[6]+0.8,'105 하남시청역 (5호선 운행 중)',ha='left',va='center',fontsize=14.5,color=NAVY,fontweight='bold')
ax.set_ylim(ys[-1]-0.7,ys[0]+1.3)
fig.text(0.045,0.03,'남색 = 역 500m 안 · 회색 = 바깥 · 거리는 구글 지도 좌표 직선(감일은 단샘초, 하남시청은 5호선 역 기준) · 국토교통부 실거래 2026년 1~10월 · 해제 · 직거래 뺌',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_songpahanam_route_2_pair.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감일 · 3호선 연장',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'송파하남선 노선도',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,495),'감일역 500m 안 84㎡',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 1천 더',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'500m 안 14억 7천 · 바깥 13억 6천',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_songpahanam_route_thumb.png')
