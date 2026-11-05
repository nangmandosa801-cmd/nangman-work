import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 월별 거래 건수 2025.1 ~ 2026.10
m25=[139,283,455,234,355,663,259,309,629,600,156,303]
m26=[246,277,254,324,361,300,314,237,184,173]
fig=plt.figure(figsize=(11.55,7.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 부동산 전망 채점 · 하남 아파트 월별 매매 건수(2025년 1월~2026년 10월 계약)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'두 달 전 글은 「한 달 300건 안팎」이라 적었는데 9월은 184건입니다',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.07,0.17,0.9,0.62])
xs=list(range(22)); vals=m25+m26
cols=[GRAY]*12+[BLUE]*8+[NAVY]*2
ax.bar(xs,vals,color=cols,width=0.72)
for x,v in zip(xs,vals):
    if x>=12 or v>=600: ax.text(x,v+12,f'{v:,}',ha='center',fontsize=12,color=NAVY if x>=12 else '#555',fontweight='bold' if x>=20 else 'normal')
labs=[f'25.{i}' for i in range(1,13)]+[f'26.{i}' for i in range(1,11)]
ax.set_xticks(xs); ax.set_xticklabels(labs,fontsize=11.5,color='#555',rotation=0)
ax.set_ylim(0,760); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.annotate('10·15 대책\n(2025년 10월 20일)',xy=(9.5,615),xytext=(7.2,700),fontsize=12,color='#555',ha='center',arrowprops=dict(arrowstyle='-',color='#9FB3C8'))
ax.annotate('글이 본 마지막 달(8월)',xy=(19,250),xytext=(16.4,560),fontsize=12,color=BLUE,ha='center',arrowprops=dict(arrowstyle='-',color=BLUE))
ax.text(20.5,330,'9 · 10월',fontsize=13,color=NAVY,ha='center',fontweight='bold')
fig.text(0.045,0.055,'회색 = 2025년 · 파랑 = 2026년 1~8월(10월 2일 글이 본 기간) · 남색 = 그 뒤 두 달 · 10월은 신고 기한(30일)이 남아 더 늘어납니다',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(하남시 · 해제 거래 뺌 · 11월 5일 내려받음)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_forecast_check_1_monthly.png'); plt.close()

# 2. 두 달 전 숫자 vs 지금 숫자
ROWS=[('같은 단지 222쌍 → 229쌍',17.0,17.9),('감일',23.3,23.6),('위례',20.9,21.5),('미사',18.5,19.3),('원도심(덕풍 · 신장 · 창우)',10.8,12.2),('작년 5억 이하 집',6.9,6.8),('작년 11억 넘는 집',18.5,19.4)]
fig=plt.figure(figsize=(11.55,8.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.96,'하남 부동산 전망 채점 · 2025년 대비 2026년 상승률, 글(1~8월) vs 지금(1~10월)',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.915,'일곱 숫자 중 여섯이 더 커졌고 순서는 하나도 바뀌지 않았습니다',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.3,0.12,0.64,0.72])
ys=[];labels=[];y=0
for lab,a,b in ROWS:
    ax.barh(y,a,color=GRAY,height=0.36); ax.barh(y-0.4,b,color=NAVY,height=0.36)
    ax.text(a+0.3,y,f'{a}%',va='center',fontsize=13,color='#555')
    ax.text(b+0.3,y-0.4,f'{b}%',va='center',fontsize=14,color=NAVY,fontweight='bold')
    ys.append(y-0.2); labels.append(lab); y-=1.15
ax.set_yticks(ys); ax.set_yticklabels(labels,fontsize=14,color='#333')
ax.set_xlim(0,30); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.barh(-9,0,color=GRAY,label='10월 2일 글(2026년 1~8월 계약)'); ax.barh(-9,0,color=NAVY,label='지금(2026년 1~10월 계약)')
ax.legend(loc='lower right',fontsize=12.5,frameon=False)
fig.text(0.045,0.045,'상승률 = 2025년과 2026년에 모두 거래된 같은 단지 · 같은 전용면적의 연간 거래금액 중앙값 변화의 중앙값 · 가격대는 2025년 중앙값 기준',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.018,'국토교통부 아파트 매매 실거래(하남시 · 해제 거래 뺌 · 11월 5일 내려받음)',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_forecast_check_2_score.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 두 달 전 글 채점',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'하남 부동산 전망',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'두 달 뒤 다시 재니',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,610),'17% → 17.9%',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'맞은 것 · 빗나간 것 · 아직 모르는 것',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_forecast_check_thumb.png')
