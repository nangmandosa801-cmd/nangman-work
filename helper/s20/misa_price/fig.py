import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 같은 해 지은 단지 짝: 미사역 가까운 단지(남색) · 먼 단지(파랑)
PAIRS=[('2014년','미사강변 골든 센트로',427,24.4,'리버나인',1521,19.2),
       ('2016년','미사강변푸르지오',795,17.9,'미사강변스타힐스',1151,27.1),
       ('2017년','미사강변효성해링턴플레이스',539,10.8,'미사강변더샵센트럴포레',1170,23.6),
       ('2018년','미사강변브라운스톤',380,11.0,'미사강변동일하이빌',942,20.4),
       ('2019년','신안인스빌',739,20.1,'미사강변센트럴풍경채',1112,19.3)]
fig=plt.figure(figsize=(11.55,9.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.962,'미사 아파트 시세 · 같은 해 지은 84㎡ 단지 짝, 1년 전보다 오른 비율',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.922,'다섯 짝 중 세 짝은 미사역에서 먼 단지가 더 올랐습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.38,0.1,0.55,0.74])
labels=[];vals=[];cols=[];ys=[];y=0
for yr,a,da,pa,b,db,pb in PAIRS:
    for nm,dd,pp,c in [(a,da,pa,NAVY),(b,db,pb,BLUE)]:
        labels.append(f'{nm}\n{yr} · 역까지 {dd:,}m'); vals.append(pp); cols.append(c); ys.append(y); y-=1
    y-=0.6
ax.barh(ys,vals,color=cols,height=0.78)
ax.set_yticks(ys); ax.set_yticklabels(labels,fontsize=13.5,color='#333')
for yy,v in zip(ys,vals): ax.text(v+0.4,yy,f'+{v}%',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xlim(0,32); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.035,'남색 = 미사역에 더 가까운 단지 · 파랑 = 더 먼 단지 · 역까지는 직선거리(오픈스트리트맵 단지 가운데 기준)',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.012,'국토교통부 아파트 매매 실거래(2025년 · 2026년 각 1~10월 계약 · 하남 망월동 · 풍산동 · 선동 전용 83~86㎡ · 해제 · 직거래 뺌 · 단지별 중앙값)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_misa_price_1_pairs.png'); plt.close()

# 2. 미사역까지 거리와 1년 상승률 (20개 단지)
D=[(380,11.0),(427,24.4),(539,10.8),(691,27.0),(730,22.8),(739,20.1),(795,17.9),(885,21.8),(942,20.4),(991,17.4),
   (1112,19.3),(1151,27.1),(1170,23.6),(1180,25.0),(1194,26.2),(1298,14.6),(1462,18.2),(1521,19.2),(1616,13.5),(2157,5.8)]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'미사 아파트 시세 · 미사역까지 거리와 84㎡ 1년 상승률(20개 단지)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'역 700m 안 두 단지는 10~11% 오르는 데 그쳤습니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.1,0.14,0.85,0.64])
ax.axvspan(0,700,color='#EEF2F7')
ax.scatter([d for d,_ in D],[p for _,p in D],s=150,color=[NAVY if d<700 else BLUE for d,_ in D],zorder=3)
ax.set_xlim(0,2300); ax.set_ylim(0,32)
ax.set_xlabel('미사역까지 직선거리(m)',fontsize=14,color='#555'); ax.set_ylabel('1년 상승률(%)',fontsize=14,color='#555')
ax.tick_params(labelsize=13,colors='#555')
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
ax.text(350,29.5,'역 700m 안',fontsize=14,color=NAVY,ha='center',fontweight='bold')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(2025년 · 2026년 각 1~10월 · 하남 망월동 · 풍산동 · 선동 84㎡ · 두 해 모두 3건 넘게 팔린 단지 중 위치 확인한 20곳)',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_misa_price_2_dist.png'); plt.close()

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
d.text((W/2,370),'미사 아파트 시세',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 1년 새',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'10억 → 12억',font=kr(ser,88),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'망월동 · 풍산동 · 선동 1~10월 중앙값',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_misa_price_thumb.png')
