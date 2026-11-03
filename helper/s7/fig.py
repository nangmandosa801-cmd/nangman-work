import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1: 6억대 vs 7억대 84㎡ 단지 지은 해
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 7억대 아파트 · 84㎡ 매매 중앙값 6억대와 7억대 단지를 지은 해로 나눔',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'1억 더 쓰면 2010년 이후 84㎡가 3곳에서 23곳',fontsize=29,color=NAVY,fontweight='bold',va='top')
cats=['1989년 전','1990년대','2000년대','2010~14년','2015년 이후']
S6=[6,51,77,1,2]; S7=[7,66,102,19,4]
for j,(nm,v,c) in enumerate([('서울 84㎡ 6억대 137곳',S6,GRAY),('서울 84㎡ 7억대 198곳',S7,NAVY)]):
    ax=fig.add_axes([0.07+j*0.47,0.12,0.42,0.62])
    ax.bar(range(5),v,color=[c]*3+[BLUE,BLUE],width=0.62)
    for i,x in enumerate(v): ax.text(i,x+1,f'{x}곳',ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.set_xticks(range(5)); ax.set_xticklabels(cats,fontsize=13,color='#444'); ax.set_yticks([]); ax.set_ylim(0,115)
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#D5DCE6'); ax.tick_params(length=0)
    ax.set_title(nm,fontsize=19,color=NAVY,fontweight='bold',loc='left',pad=14)
fig.text(0.045,0.03,'국토교통부 아파트 매매 실거래 2026년 1~10월 계약 · 해제 거래 뺌 · 같은 단지 같은 면적 3건 이상인 곳의 중앙값',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul7eok_1_year.png'); plt.close()
# 2: 같은 7억대로 고르는 세 가지
fig=plt.figure(figsize=(11.55,9.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서울 7억대 아파트 · 같은 7억대로 고를 수 있는 세 가지',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'서울 2010년대 84㎡ · 서울 새 59㎡ · 경기 새 84㎡',fontsize=29,color=NAVY,fontweight='bold',va='top')
G=[('서울 2010~14년 84㎡',[('천왕동 천왕연지타운2단지 2014',7.8),('신내동 신내우디안1단지 2014',7.8),('신내동 신내데시앙포레 2013',7.75),('역촌동 역촌센트레빌 2011',7.5)],GRAY),
   ('서울 2015년 이후 59㎡',[('독산동 e편한세상독산더타워 2019',7.82),('미아동 꿈의숲한신더휴 2022',7.8),('진관동 은평뉴타운꿈에그린 2018',7.485),('진관동 은평뉴타운엘크루 2017',7.4)],BLUE),
   ('경기 2015년 이후 84㎡',[('수원 곡반정동 하늘채더퍼스트1단지 2022',7.9),('부천 범박동 일루미스테이트 2024',7.84),('구리 갈매동 한라비발디 2016',7.5),('고양 원흥동 동원로얄듀크비스타 2020',7.3)],NAVY)]
ax=fig.add_axes([0.42,0.06,0.53,0.77]); y=0; yt=[];yl=[]
import matplotlib.transforms as T
tr=T.blended_transform_factory(fig.transFigure,ax.transData)
for g,(nm,it,c) in enumerate(G):
    ax.text(0.045,y,nm,transform=tr,fontsize=19,color=c if c!=GRAY else '#6B7685',fontweight='bold',va='center'); y+=1
    for lab,v in it:
        ax.barh(y,v,color=c,height=0.6)
        man=round(v*10000)-70000
        s=f'7억 {man:,}만' if man else '7억'
        ax.text(v+0.02,y,s,va='center',fontsize=14,color=NAVY)
        yt.append(y); yl.append(lab); y+=1
    y+=0.4
ax.set_yticks(yt); ax.set_yticklabels(yl,fontsize=13,color='#444'); ax.invert_yaxis(); ax.set_xlim(6.8,8.25); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#D5DCE6'); ax.tick_params(length=0)
fig.text(0.045,0.025,'2026년 1~10월 매매 중앙값 · 단지 이름 뒤 숫자는 지은 해 · 국토교통부 실거래',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seoul7eok_2_three.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · ○억이면 이런 아파트 · 7억대',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'서울 7억대 아파트',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'2010년 이후 84㎡',font=kr(ser,64),fill='#F4F1EA',anchor='mm')
d.text((W/2,600),'3곳 → 23곳',font=kr(ser,84),fill='#D4B04C',anchor='mm')
d.text((W/2,712),'6억대보다 1억 더 쓰면 · 2026년 실거래',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_seoul7eok_thumb.png')
