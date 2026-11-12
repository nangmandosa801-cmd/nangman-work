import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_yeongtong_remodel_'
# 1. 59㎡ 2025년 중앙값 → 2026년 7~10월 중앙값 상승률
R=[('벽적골 8단지 두산·우성·한신\n이주 중',10.9,NAVY),('벽적골주공 8단지\n2027년 5~9월 이주 예정',31.1,BLUE),('신나무실 신성·신안·쌍용·진흥\n2027년 1분기 이주 예정',36.1,BLUE),('신나무실 주공5단지\n이주 일정 보도 없음',39.8,BLUE),('청명마을 주공\n리모델링 안 함',39.1,GRAY),('벽적골 9단지 주공\n리모델링 안 함',42.9,GRAY),('황골마을 주공1단지\n리모델링 안 함',45.4,GRAY)]
fig=plt.figure(figsize=(11.55,8.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'영통 리모델링 현황 · 영통동 59㎡ 2025년 중앙값 → 2026년 7~10월 중앙값',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.905,'이주 중인 단지 +11%, 리모델링 안 하는 옆 단지 +39~45%',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.33,0.1,0.6,0.7])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[v for _,v,_ in R],color=[c for *_,c in R],height=0.6)
ax.set_yticks(ys); ax.set_yticklabels([a for a,_,_ in R],fontsize=13.5,color='#333')
for y,(_,v,c) in zip(ys,R): ax.text(v+0.8,y,f'+{v:.1f}%',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,55); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래(수원 영통구 영통동 · 전용 58~61㎡ · 해제 거래 뺌 · 2026년 10월 계약은 신고 기간이 남아 덜 들어옴)',fontsize=11.5,color='#8A8578')
fig.savefig('img/'+S+'1_rise.png'); plt.close()
# 2. 이주 일정
fig=plt.figure(figsize=(11.55,6.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.94,'영통 리모델링 이주 일정 · 보도로 확인된 3개 단지',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.875,'2026년 8월부터 2027년 9월까지 5,006가구',fontsize=26,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.3,0.16,0.64,0.58])
import datetime as dt
def m(y,mo,d=1): return (dt.date(y,mo,d)-dt.date(2026,7,1)).days
J=[('벽적골 8단지 두산·우성·한신\n1,842가구',m(2026,8,28),m(2026,12,27),NAVY,'2026.8.28~12.27'),
   ('신나무실 신성·신안·쌍용·진흥\n1,616가구',m(2027,1,1),m(2027,3,31),BLUE,'2027년 1분기'),
   ('벽적골주공 8단지\n1,548가구',m(2027,5,1),m(2027,9,30),BLUE,'2027년 5~9월')]
ys=[2,1,0]
for y,(lab,a,b,c,t) in zip(ys,J):
    ax.barh(y,b-a,left=a,color=c,height=0.5); ax.text(b+6,y,t,va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(ys); ax.set_yticklabels([j[0] for j in J],fontsize=14,color='#333')
ticks=[m(2026,7),m(2027,1),m(2027,7),m(2028,1)]; ax.set_xticks(ticks); ax.set_xticklabels(['2026.7','2027.1','2027.7','2028.1'],fontsize=13,color='#555')
ax.set_xlim(0,m(2028,1)); ax.set_ylim(-0.6,2.6)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE'); ax.tick_params(left=False)
fig.text(0.045,0.03,'경인일보 2026년 11월 3일 · 7월 12일 보도 · 신나무실 단지 · 벽적골주공 8단지는 예정 일정',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_ijoo.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 수원 영통 · 리모델링',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'영통 리모델링 현황',font=kr(ser,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'3개 단지 이주',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'5,006가구',font=kr(ser,96),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'벽적골 8단지부터 2027년 9월까지',font=kr(san,36),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
