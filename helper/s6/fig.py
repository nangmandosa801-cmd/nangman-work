import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1: 5억대 84㎡ 단지 지은 해
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 6억대 아파트 · 84㎡ 매매 중앙값 6억대 단지를 지은 해로 나눔',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'137곳 가운데 2015년 이후는 두 곳',fontsize=31,color=NAVY,fontweight='bold',va='top')
cats=['1989년 전','1990년대','2000년대','2010~14년','2015년 이후']
S=[6,51,77,1,2]; W=[10,59,49,5,8]
for j,(nm,v,c) in enumerate([('서울 84㎡ 6억대 137곳',S,NAVY),('서울 59㎡ 6억대 131곳',W,GRAY)]):
    ax=fig.add_axes([0.07+j*0.47,0.12,0.42,0.62])
    b=ax.bar(range(5),v,color=[c]*4+[BLUE if j==0 else NAVY],width=0.62)
    for i,x in enumerate(v): ax.text(i,x+0.8,f'{x}곳',ha='center',fontsize=16,color=NAVY if x else '#999',fontweight='bold')
    ax.set_xticks(range(5)); ax.set_xticklabels(cats,fontsize=13,color='#444'); ax.set_yticks([]); ax.set_ylim(0,88)
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#D5DCE6'); ax.tick_params(length=0)
    ax.set_title(nm,fontsize=19,color=NAVY,fontweight='bold',loc='left',pad=14)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 2026년 1~10월 계약 · 해제 거래 뺌 · 같은 단지 같은 면적 3건 이상인 곳의 중앙값',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul6eok_1_year.png'); plt.close()
# 2: 5억대로 사는 집
fig=plt.figure(figsize=(11.55,9.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 6억대 아파트 · 같은 6억대로 고를 수 있는 세 가지',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'서울 새 59㎡ · 서울 오래된 84㎡ · 고양 새 84㎡',fontsize=29,color=NAVY,fontweight='bold',va='top')
G=[('서울 2015년 이후 59㎡',[('홍은동 HDX휴팰리스 2018',6.505),('공릉동 화랑대디오베이션 2021',6.69),('항동 하버라인3단지 2019',6.8),('항동 하버라인2단지 2019',6.895)],BLUE),
   ('서울 오래된 84㎡',[('도봉동 한신 1995',6.1),('신내동 성원 1994',6.65),('미아동 벽산라이브파크 2004',6.8),('정릉동 정릉풍림아이원 2005',6.95)],GRAY),
   ('고양 2015년 이후 84㎡',[('중산동 일산센트럴아이파크 2018',6.38),('신원동 삼송동일스위트파크뷰 2017',6.45),('식사동 일산자이더헤리티지 2022',6.9),('도내동 도래울센트럴더힐 2015',6.925)],NAVY)]
ax=fig.add_axes([0.40,0.06,0.55,0.77]); y=0; yt=[];yl=[]
import matplotlib.transforms as T
tr=T.blended_transform_factory(fig.transFigure,ax.transData)
for g,(nm,it,c) in enumerate(G):
    ax.text(0.045,y,nm,transform=tr,fontsize=19,color=c if c!=GRAY else '#6B7685',fontweight='bold',va='center'); y+=1
    for lab,v in it:
        ax.barh(y,v,color=c,height=0.6); ax.text(v+0.03,y,f'{v:.2f}억'.replace('0억','억'),va='center',fontsize=14,color=NAVY)
        yt.append(y); yl.append(lab); y+=1
    y+=0.4
ax.set_yticks(yt); ax.set_yticklabels(yl,fontsize=13,color='#444'); ax.invert_yaxis(); ax.set_xlim(5.8,7.3); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#D5DCE6'); ax.tick_params(length=0)
fig.text(0.045,0.025,'2026년 1~10월 매매 중앙값 · 단지 이름 뒤 숫자는 지은 해 · 국토교통부 실거래',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul6eok_2_three.png'); plt.close()
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
d.text((W/2,375),'서울 6억대 아파트',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 137곳 중',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'새 아파트는 두 곳',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'2026년 실거래 · 서울과 고양 비교',font=kr(san,36),fill='#D4B04C',anchor='mm')
im.save('img/nangman_seoul6eok_thumb.png')
