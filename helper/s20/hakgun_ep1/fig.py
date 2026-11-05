import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_hakgun_ep1_'
# 그림 1: 대치동 84㎡ 새 세입자 전세 · 입주 달별 건수 (2024~2025년 계약 605건)
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
V=[58,140,46,20,26,39,55,53,41,37,26,64]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'대치동 84㎡ 새 세입자 전세 605건 · 입주 달별 건수 · 2024~2025년 계약',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.905,'2월 입주 140건, 넷 중 하나',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.13,0.9,0.66])
cols=[GRAY,NAVY]+[GRAY]*10
ax.bar(range(12),V,color=cols,width=0.62)
for i,v in enumerate(V): ax.text(i,v+2.5,f'{v}',ha='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_xticks(range(12)); ax.set_xticklabels(M,fontsize=14,color='#333')
ax.set_ylim(0,160); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(1,150,'새 학기 전 입주',ha='center',fontsize=14,color=NAVY)
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(서울 강남구 대치동 · 전용 83~86㎡ · 월세 없는 새 세입자 계약 · 입주 달은 신고서의 계약 기간 시작 달)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_movein.png'); plt.close()

# 그림 2: 2월 입주 몫 · 학군 동과 같은 구 비학군 동
R=[('대치동',23.1,True),('세곡 · 자곡 · 율현',8.8,False),('중계동',18.0,True),('하계동',13.7,False),('반포동',16.4,True),('방배동',12.7,False),('목동',15.0,True),('신월동',11.0,False)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'84㎡ 새 세입자 전세 가운데 2월에 입주한 계약의 몫 · 2024~2025년 계약',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.915,'학군 동 15~23%, 같은 구 비학군 동 9~14%',fontsize=28,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.26,0.08,0.68,0.76])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[NAVY if s else GRAY for _,_,s in R],height=0.62)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=15,color='#333')
for y,(_,v,s) in zip(ys,R): ax.text(v+0.4,y,f'{v}%',va='center',fontsize=15,color=NAVY if s else '#555',fontweight='bold')
ax.set_xlim(0,27); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.025,'국토교통부 아파트 전월세 실거래 · 전용 83~86㎡ · 월세 없는 새 세입자 계약 · 남색은 학군 동, 회색은 같은 구 안 비학군 동 · 목동 신시가지는 84㎡가 없어 빠짐',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_feb.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 1화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'학군지 아파트',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'2021 고점 대비 덜 빠진 곳',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'넷 중 둘',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'대치 · 반포는 버텼고 목동 · 중계는 15~19% 빠졌습니다',font=kr(san,31),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
