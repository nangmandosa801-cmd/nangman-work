import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 감북동 빌라 월별 매매 건수
M={'202501': 0, '202502': 3, '202503': 1, '202504': 2, '202505': 2, '202506': 6, '202507': 2, '202508': 7, '202509': 3, '202510': 3, '202511': 7, '202512': 6, '202601': 2, '202602': 1, '202603': 2, '202604': 3, '202605': 2, '202606': 1, '202607': 4, '202608': 14, '202609': 9, '202610': 2}
ks=list(M); vs=[M[k] for k in ks]
fig=plt.figure(figsize=(11.55,7.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'감북동 재개발 · 감북동 빌라(연립 · 다세대) 월별 매매 건수',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'8월 13일 대책 뒤 두 달 반 동안 20건, 그 앞 일곱 달 반도 20건',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.17,0.89,0.62])
cols=[NAVY if k in ('202608','202609','202610') else (BLUE if k.startswith('2026') else GRAY) for k in ks]
ax.bar(range(len(ks)),vs,color=cols,width=0.7)
for i,v in enumerate(vs):
    if v: ax.text(i,v+0.25,str(v),ha='center',fontsize=13,color=NAVY,fontweight='bold')
ax.set_xticks(range(len(ks))); ax.set_xticklabels([f"{k[2:4]}.{int(k[4:])}" for k in ks],fontsize=11.5,color='#555')
ax.set_ylim(0,17); ax.set_yticks([]); ax.set_xlim(-0.6,23.2)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axvline(18.9,color=NAVY,ls='--',lw=1.2); ax.text(18.75,16.2,'8.13 수도권 공급대책',fontsize=12.5,color=NAVY,ha='right')
ax.axvline(21.4,color=BLUE,ls='--',lw=1.2); ax.text(21.6,13.6,'10.29\n감일2\n후보지',fontsize=12.5,color=BLUE,ha='left')
fig.text(0.045,0.05,'회색 = 2025년 · 파랑 = 2026년 · 남색 = 8월 이후 · 10월은 신고 기한(30일)이 남아 늘어날 수 있음',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.022,'국토교통부 연립 · 다세대 매매 실거래(2025년 1월~2026년 10월 계약 · 11월 5일 내려받음 · 하남시 감북동 · 해제 거래 뺌 · 직거래 포함)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gambuk_redev_1_month.png'); plt.close()

# 2. 하남 동별 빌라 ㎡당 값 (2026년 1~10월 중개거래)
R=[('감북동','32건 · 2022년',907,NAVY),('감일동','16건 · 2023년',796,BLUE),('신장동','30건 · 2002년',680,GRAY),('덕풍동','50건 · 2007년',603,GRAY)]
fig=plt.figure(figsize=(11.55,6.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.95,'감북동 빌라 매매 · 전용 ㎡당 중앙값(2026년 1~10월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.89,'감북동 빌라는 ㎡당 907만원, 덕풍동의 1.5배',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.33,0.15,0.6,0.62])
ys=list(range(len(R)))[::-1]
ax.barh(ys,[r[2] for r in R],color=[r[3] for r in R],height=0.62)
ax.set_yticks(ys); ax.set_yticklabels([f'{r[0]}\n{r[1]}' for r in R],fontsize=14,color='#333')
for y,r in zip(ys,R): ax.text(r[2]+12,y,f'{r[2]}만원',va='center',fontsize=16,color=NAVY,fontweight='bold')
ax.set_xlim(0,1080); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.035,'국토교통부 연립 · 다세대 매매 실거래(2026년 1~10월 계약 · 해제 · 직거래 뺌) · 연도는 거래된 집의 건축년도 중앙값',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_gambuk_redev_2_sqm.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 감북동 · 빌라 실거래',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'감북동 재개발',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'8 · 13 대책 뒤 두 달 반',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'빌라 20건',font=kr(ser,104),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'그 앞 일곱 달 반 거래와 같은 수',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_gambuk_redev_thumb.png')
