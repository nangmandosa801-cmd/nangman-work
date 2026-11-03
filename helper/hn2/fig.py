import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def clean(ax):
    for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
M=['2018.9','10','11','12','2019.1','2','3','4','5','6']; V=[9,13,31,45,0,0,2,2,0,0]
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남감일2지구 · 2018년 교산 일대 그린벨트 땅 거래 수(교산 · 춘궁 · 상사창 · 하사창 · 천현동)',fontsize=16.5,color=BLUE,va='top')
fig.text(0.045,0.905,'발표 직전 두 달 76건, 다음 석 달 2건',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.13,0.9,0.66])
ax.bar(range(len(V)),V,color=[NAVY if i in (2,3) else GRAY for i in range(len(V))],width=0.62)
for i,v in enumerate(V): ax.text(i,v+0.8,f'{v}건',ha='center',fontsize=15,color=NAVY if v else '#999',fontweight='bold')
ax.set_xticks(range(len(V))); ax.set_xticklabels(M,fontsize=14,color='#444'); ax.set_yticks([]); ax.set_ylim(0,55); clean(ax)
ax.annotate('12월 19일 교산 발표',xy=(3.45,46),xytext=(6,40),fontsize=15,color=NAVY,arrowprops=dict(arrowstyle='->',color=NAVY))
fig.text(0.045,0.025,'국토교통부 토지 매매 실거래 · 개발제한구역 · 지분 거래 포함 · 해제 거래 뺌 · 계약월 기준',fontsize=13,color='#8A8578')
fig.savefig('img/jisandream_hanamtaekji_1_gyosan.png'); plt.close()
D=[('감이동',97,238),('광암동',96,375),('항동',94,123),('교산동',89,160),('감북동',87,260),('춘궁동',74,130),('초이동',64,179),('미사동',59,46),('상산곡동',24,59)]
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 신규택지 · 하남 그린벨트 땅 거래 가운데 지분 거래 비율 (2024년 1월~2026년 10월)',fontsize=16.5,color=BLUE,va='top')
fig.text(0.045,0.905,'감일2 쪽 감이동은 238건 중 97%가 지분',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.2,0.08,0.74,0.74])
y=range(len(D)); ax.barh(list(y),[p for _,p,_ in D],color=[NAVY if n in('감이동','감북동','미사동') else GRAY for n,_,_ in D],height=0.62)
for i,(n,p,c) in enumerate(D): ax.text(p+1,i,f'{p}%  ({c}건)',va='center',fontsize=14.5,color=NAVY)
ax.set_yticks(list(y)); ax.set_yticklabels([n for n,_,_ in D],fontsize=15,color='#333'); ax.invert_yaxis(); ax.set_xlim(0,125); ax.set_xticks([]); clean(ax)
fig.text(0.045,0.022,'국토교통부 토지 매매 실거래 · 하남시 개발제한구역 · 거래 40건 넘는 동 · 짙은 색은 이번 후보지와 가까운 동',fontsize=12.5,color='#8A8578')
fig.savefig('img/jisandream_hanamtaekji_2_jibun.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'지산드림 · 하남 토지 · 신규택지 후보지',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'하남감일2지구 땅',font=kr(ser,90),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'교산 때는 발표 뒤',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'석 달 거래 2건',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'2018년 교산 · 지금 감이동 · 미사동 실거래',font=kr(san,34),fill='#D4B04C',anchor='mm')
im.save('img/jisandream_hanamtaekji_thumb.png')
