import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1: 5억대 84㎡ 단지 지은 해
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 5억대 아파트 · 84㎡ 매매 중앙값 5억대 단지를 지은 해로 나눔',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'64곳 가운데 2015년 이후는 한 곳',fontsize=31,color=NAVY,fontweight='bold',va='top')
cats=['1989년 전','1990년대','2000년대','2010~14년','2015년 이후']
S=[4,42,16,1,1]; W=[0,14,21,4,4]
for j,(nm,v,c) in enumerate([('서울 84㎡ 5억대 64곳',S,NAVY),('수원 84㎡ 5억대 43곳',W,GRAY)]):
    ax=fig.add_axes([0.07+j*0.47,0.12,0.42,0.62])
    b=ax.bar(range(5),v,color=[c]*4+[BLUE if j==0 else NAVY],width=0.62)
    for i,x in enumerate(v): ax.text(i,x+0.8,f'{x}곳',ha='center',fontsize=16,color=NAVY if x else '#999',fontweight='bold')
    ax.set_xticks(range(5)); ax.set_xticklabels(cats,fontsize=13,color='#444'); ax.set_yticks([]); ax.set_ylim(0,48)
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#D5DCE6'); ax.tick_params(length=0)
    ax.set_title(nm,fontsize=19,color=NAVY,fontweight='bold',loc='left',pad=14)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 2026년 1~10월 계약 · 해제 거래 뺌 · 같은 단지 같은 면적 3건 이상인 곳의 중앙값',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul5eok_1_year.png'); plt.close()
# 2: 5억대로 사는 집
fig=plt.figure(figsize=(11.55,9.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 5억대 아파트 · 같은 5억대로 고를 수 있는 세 가지',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'서울 새 59㎡ · 서울 오래된 84㎡ · 수원 새 84㎡',fontsize=29,color=NAVY,fontweight='bold',va='top')
G=[('서울 2015년 이후 59㎡',[('중계동 현대(6차) 2018',5.26),('응암동 삼흥리치 2016',5.37),('길동 골드클래스 2022',5.40),('장안동 스타파크 2016',5.40)],BLUE),
   ('서울 오래된 84㎡',[('방학동 동양크레오 2004',5.78),('창동 한승미메이드 2004',5.70),('도봉동 한양수자인 2010',5.67),('창동 초안산신도브래뉴 2005',5.90)],GRAY),
   ('수원 2015년 이후 84㎡',[('오목천동 서희스타힐스 2016',5.20),('호매실동 벨섬시티 2017',5.765),('호매실동 엔루체 2016',5.80),('세류동 센트럴타운3단지 2015',5.99)],NAVY)]
ax=fig.add_axes([0.40,0.06,0.55,0.77]); y=0; yt=[];yl=[]
import matplotlib.transforms as T
tr=T.blended_transform_factory(fig.transFigure,ax.transData)
for g,(nm,it,c) in enumerate(G):
    ax.text(0.045,y,nm,transform=tr,fontsize=19,color=c if c!=GRAY else '#6B7685',fontweight='bold',va='center'); y+=1
    for lab,v in it:
        ax.barh(y,v,color=c,height=0.6); ax.text(v+0.03,y,f'{v:.2f}억'.replace('0억','억'),va='center',fontsize=14,color=NAVY)
        yt.append(y); yl.append(lab); y+=1
    y+=0.4
ax.set_yticks(yt); ax.set_yticklabels(yl,fontsize=13,color='#444'); ax.invert_yaxis(); ax.set_xlim(4.8,6.3); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#D5DCE6'); ax.tick_params(length=0)
fig.text(0.045,0.025,'2026년 1~10월 매매 중앙값 · 단지 이름 뒤 숫자는 지은 해 · 국토교통부 실거래',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul5eok_2_three.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · ○억이면 이런 아파트',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'서울 5억대 아파트',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 64곳 중',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'새 아파트는 한 곳',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'2026년 실거래 · 서울과 수원 비교',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_seoul5eok_thumb.png')
