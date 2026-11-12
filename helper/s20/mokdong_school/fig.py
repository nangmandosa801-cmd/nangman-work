import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_mokdong_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
# 1. 단지별 65~75㎡ 2025 · 2026 중앙값
dans=list(range(1,15))
v25=[J['dan'][f's{d}']['2025']['med']/10000 for d in dans]
v26=[(J['dan'][f's{d}']['2026']['med'] or 0)/10000 for d in dans]
n26=[J['dan'][f's{d}']['2026']['n'] for d in dans]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'목동 아파트 시세 · 신시가지 단지별 65~75㎡ 매매 중앙값(2025년 · 2026년 1~10월)',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'앞단지(1~7) 23억 8,000만 · 뒷단지(8~14) 21억 9,500만',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.15,0.92,0.6])
x=list(range(14)); w=0.38
ax.bar([i-w/2 for i in x],v25,width=w,color=GRAY)
ax.bar([i+w/2 for i in x],v26,width=w,color=[NAVY if d<=7 else BLUE for d in dans])
for i,(a,b,n) in enumerate(zip(v25,v26,n26)):
    ax.text(i-w/2,a+0.3,f'{a:.1f}',ha='center',fontsize=10.5,color='#777')
    if b>0: ax.text(i+w/2,b+0.3,f'{b:.1f}',ha='center',fontsize=11.5,color=NAVY,fontweight='bold')
    else: ax.text(i+w/2,0.6,'0건',ha='center',fontsize=11,color=NAVY,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels([f'{d}단지' for d in dans],fontsize=12,color='#555')
ax.set_yticks([]); ax.set_ylim(0,30)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.axvline(6.5,color=NAVY,lw=1,ls='--'); ax.text(3,28.3,'앞단지 65㎡',fontsize=13,color=NAVY,ha='center'); ax.text(10,28.3,'뒷단지 71㎡ (11단지 66㎡)',fontsize=13,color=BLUE,ha='center')
fig.text(0.045,0.055,'회색 = 2025년 · 색 = 2026년 1~10월 · 숫자는 억원 · 6단지는 2026년 거래 없음(2025년 5월 조합설립인가)',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(양천구 목동신시가지 1~14단지 · 전용 64~75㎡ · 해제 거래 뺌 · 2026년은 10월 24일 신고분까지)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_dan.png'); plt.close()

# 2. 2021~2026 해마다 중앙값 · 앞단지 65㎡ · 뒷단지 71㎡ · 신길동 우성2 64㎡
yrs=['2021','2022','2023','2024','2025','2026']
f=[J['grp']['s_front'][y]['med']/10000 for y in yrs]; b=[J['grp']['s_back'][y]['med']/10000 for y in yrs]
sg=J['singil_ws2']; s_y=['2021','2023','2024','2025','2026']; s_v=[sg[y]['med']/10000 for y in s_y]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'목동 아파트 시세 · 65~75㎡ 해마다 매매 중앙값, 2021~2026년',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'2023년 앞단지 −9% · 뒷단지 −10% · 신길동 우성2 −21%',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.88,0.64])
xs=list(range(6))
ax.plot(xs,f,color=NAVY,lw=2.8,marker='o'); ax.plot(xs,b,color=BLUE,lw=2.8,marker='o')
ax.plot([yrs.index(y) for y in s_y],s_v,color=GRAY,lw=2.4,marker='o')
for i,(a,c) in enumerate(zip(f,b)):
    ax.text(i,a+0.6,f'{a:.1f}',ha='center',fontsize=12.5,color=NAVY,fontweight='bold')
    ax.text(i,c-1.3,f'{c:.1f}',ha='center',fontsize=12.5,color=BLUE,fontweight='bold')
for y,v in zip(s_y,s_v): ax.text(yrs.index(y),v-1.3,f'{v:.1f}',ha='center',fontsize=12,color='#777')
ax.text(5.15,f[-1],'앞단지 65㎡',fontsize=13,color=NAVY,va='center'); ax.text(5.15,b[-1],'뒷단지 71㎡',fontsize=13,color=BLUE,va='center'); ax.text(5.15,s_v[-1],'신길동 우성2 64㎡',fontsize=13,color='#777',va='center')
ax.set_xticks(xs); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555'); ax.set_xlim(-0.3,6.4)
ax.set_yticks([5,10,15,20,25]); ax.set_yticklabels(['5억','10억','15억','20억','25억'],fontsize=12,color='#555'); ax.set_ylim(5,27)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.055,'숫자는 억원 · 2022년은 신시가지 거래 86건뿐 · 신길동 우성2(1986년 · 영등포구)는 2022년 생략(거래 1건)',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(2021년 1월~2026년 10월 24일 계약 · 해제 거래 뺌 · 앞단지 = 1~7단지 · 뒷단지 = 8~14단지)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 3화 · 양천구 목동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'목동 아파트 시세',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'앞단지 · 뒷단지 차이',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'1억 8,500만',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'65㎡ 23억 8천 · 71㎡ 21억 9,500 · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')
