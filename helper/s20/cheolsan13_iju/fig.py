import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_cheolsan13_iju_'
# 그림 1 · 올해 1~10월 철산동 · 하안동 아파트 새 세입자 전세 계약 건수(달마다) + 2,460가구 비교
M=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월']
V=[250,200,214,161,112,91,88,97,76,58]
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'철산동 · 하안동 아파트 · 달마다 새 세입자 전세 계약 건수(2026년 1~10월 · 모든 면적)',fontsize=15,color=BLUE,va='top')
fig.text(0.045,0.9,'10개월 1,347건, 한 달 135건 · 철산주공13단지 2,460가구는 18개월치',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.14,0.9,0.62])
ax.bar(range(len(V)),V,color=[BLUE]*8+[GRAY]*2,width=0.7)
for i,v in enumerate(V): ax.text(i,v+5,str(v),ha='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_xticks(range(len(V))); ax.set_xticklabels(M,fontsize=13,color='#555')
ax.set_yticks([]); ax.set_ylim(0,300)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axhline(134.7,color=NAVY,lw=1.2,ls='--'); ax.text(9.45,140,'한 달 평균 135건',fontsize=12,color=NAVY,ha='right')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(광명시 철산동 · 하안동 · 전세 · 계약구분 신규 · 2026년 1~10월 계약 · 9~10월은 신고 기간이 남아 덜 들어옴 · 회색)',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'1_month.png'); plt.close()
# 그림 2 · 2030년에 옮길 집 · 올해 새 전세 가운데 보증금이 맞는 건수
fig=plt.figure(figsize=(11.55,7.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'올해 철산동 · 하안동 새 세입자 전세 · 보증금이 맞는 건수',fontsize=15,color=BLUE,va='top')
fig.text(0.045,0.9,'84㎡ 4억 이하 73건 가운데 40건은 주공 12 · 13단지',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.14,0.66,0.62])
labs=['84㎡ · 4억 이하\n(주공12 · 13 포함)','84㎡ · 4억 이하\n(주공12 · 13 빼고)','84㎡ · 6억 이하\n(주공12 · 13 빼고)','59㎡ · 3억 7천 이하']
vals=[73,33,72,283]; cols=[GRAY,BLUE,BLUE,NAVY]
y=range(len(vals))[::-1]
ax.barh(list(y),vals,color=cols,height=0.55)
for yy,v in zip(y,vals): ax.text(v+4,yy,f'{v}건',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(list(y)); ax.set_yticklabels(labs,fontsize=13,color='#333')
ax.set_xticks([]); ax.set_xlim(0,330)
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.03,'국토교통부 아파트 전월세 실거래(광명시 철산동 · 하안동 · 전세 · 신규 · 2026년 1~10월 계약 · 84㎡는 전용 83~86㎡ · 59㎡는 58~60.5㎡)',fontsize=11,color='#8A8578')
fig.savefig('img/'+S+'2_budget.png'); plt.close()
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 광명 철산 · 재건축 따라가기 6화',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,365),'재건축 이주',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,490),'철산주공13단지 2,460가구',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'새 전세 18개월치',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'올해 철산 · 하안 새 세입자 전세 한 달 135건',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
