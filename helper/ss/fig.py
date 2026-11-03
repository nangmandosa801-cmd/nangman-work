import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
def clean(ax):
    for s in ['top','right','left','bottom']: ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
D=[('전주효천대방노블랜드에코파크 (2020)',5.15),('에코시티더샵 (2018)',4.8),('힐스테이트어울림효자 (2022)',4.7),('태평아이파크 (2022)',4.6),('서신아이파크이편한세상 (2020)',4.51)]
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서신더샵에피트 입주 · 전주 새 아파트 84㎡ 올해 새 세입자 전세',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'같은 서신동은 4억 5천, 전주 새 아파트는 4억 5천~5억',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.40,0.1,0.55,0.7])
ax.barh(range(len(D)),[v for _,v in D],color=[NAVY if '서신' in n else GRAY for n,_ in D],height=0.6)
for i,(n,v) in enumerate(D): ax.text(v+0.05,i,f'{v:.2f}억'.replace('0억','억'),va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_yticks(range(len(D))); ax.set_yticklabels([n for n,_ in D],fontsize=14,color='#333'); ax.invert_yaxis(); ax.set_xlim(0,6); ax.set_xticks([]); clean(ax)
fig.text(0.045,0.025,'국토교통부 아파트 전월세 실거래 · 2026년 1월~10월 23일 · 월세 없는 신규 계약 중앙값 · 전주시',fontsize=13,color='#8A8578')
fig.savefig('img/nangman_seosin_1_jeonse.png'); plt.close()
fig=plt.figure(figsize=(11.55,8.0),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'서신더샵에피트 입주 · 84㎡ 분양가와 옆 서신아이파크이편한세상 84㎡',fontsize=18,color=BLUE,va='top')
fig.text(0.045,0.905,'분양가와 옆 단지 전세가 5천만원 차이',fontsize=29,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.13,0.86,0.66])
L=['에피트 84㎡\n분양가(약)','서신아이파크 84㎡\n매매','서신아이파크 84㎡\n새 세입자 전세','서신아이파크 84㎡\n갱신 전세']
V=[5.0,6.615,4.51,4.07]; C=[NAVY,GRAY,BLUE,GRAY]
ax.bar(range(4),V,color=C,width=0.58)
for i,v in enumerate(V): ax.text(i,v+0.12,f'{v:.2f}억'.replace('0억','억').replace('.0억','억'),ha='center',fontsize=19,color=NAVY,fontweight='bold')
ax.set_xticks(range(4)); ax.set_xticklabels(L,fontsize=14,color='#444'); ax.set_yticks([]); ax.set_ylim(0,7.6); clean(ax)
fig.text(0.045,0.03,'분양가: 3.3㎡당 평균 약 1,642만원 기준 84㎡ 5억원 안팎(보도) · 매매 · 전세: 국토교통부 실거래 2026년 1~10월 중앙값',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_seosin_2_ratio.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 전주 서신동 · 1,914세대 입주',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,375),'서신더샵에피트 입주',font=kr(ser,82),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'84㎡ 전세 기준은',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,590),'옆 단지 4억 5천',font=kr(ser,62),fill='#F4F1EA',anchor='mm')
d.text((W/2,700),'11월 20일 입주 · 전주 새 아파트 실거래',font=kr(san,34),fill='#D4B04C',anchor='mm')
im.save('img/nangman_seosin_thumb.png')
