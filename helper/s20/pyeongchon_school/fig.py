import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_pyeongchon_school_'
J=json.load(open('ana.json'))
yrs=['2021','2022','2023','2024','2025','2026']
def ser(k): return [J[k]['sale'][y]['med']/10000 for y in yrs],[J[k]['sale'][y]['n'] for y in yrs]
# 1. 같은 현대홈타운 짝 · 2021~2026 해마다 중앙값
g,gn=ser('귀인현대홈타운80'); h,hn=ser('호계현대홈타운85'); s,sn=ser('비산삼성래미안85')
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평촌 학원가 아파트 · 같은 2002~2003년 단지 해마다 매매 중앙값, 2021~2026년',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'귀인마을 현대홈타운 80㎡ 14억 · 호계동 현대홈타운 85㎡ 7억 1,500',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.15,0.92,0.6])
x=list(range(6)); w=0.27
ax.bar([i-w for i in x],g,width=w,color=NAVY); ax.bar(x,h,width=w,color=BLUE); ax.bar([i+w for i in x],s,width=w,color=GRAY)
for i,(a,b,c) in enumerate(zip(g,h,s)):
    ax.text(i-w,a+0.25,f'{a:.1f}',ha='center',fontsize=11.5,color=NAVY,fontweight='bold')
    ax.text(i,b+0.25,f'{b:.1f}',ha='center',fontsize=11,color=BLUE,fontweight='bold')
    ax.text(i+w,c+0.25,f'{c:.1f}',ha='center',fontsize=10.5,color='#777')
ax.set_xticks(x); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555')
ax.set_yticks([]); ax.set_ylim(0,16.5)
for sp in ['top','right','left']: ax.spines[sp].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(0.3,15.6,'■ 귀인마을 현대홈타운 80㎡ (2002년 · 평촌동)',fontsize=12.5,color=NAVY)
ax.text(0.3,14.6,'■ 호계 1 · 2차 현대홈타운 85㎡ (2002 · 2003년 · 호계동)',fontsize=12.5,color=BLUE)
ax.text(0.3,13.6,'■ 비산동 삼성래미안 85㎡ (2003년)',fontsize=12.5,color='#777')
fig.text(0.045,0.055,'숫자는 억원 · 2022년은 거래가 적음(귀인 3건 · 호계 7건 · 삼성래미안 16건) · 2026년은 1~10월',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(안양시 동안구 · 2021년 1월~2026년 10월 23일 계약 · 해제 거래 · 직거래 뺌 · 80㎡는 전용 79~82㎡ · 85㎡는 83~86㎡)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_pair.png'); plt.close()

# 2. 전세가율 · 2026년 새 세입자 전세 ÷ 매매 중앙값
items=[('귀인마을 현대홈타운 80㎡','귀인현대홈타운80',True),('향촌 롯데 · 현대4 · 5차 85㎡','향촌3단지85',True),('초원마을 85㎡ (평촌동)','초원85',False),('관악마을 85㎡ (비산동)','관악85',False),('호계 현대홈타운 85㎡','호계현대홈타운85',False),('비산동 삼성래미안 85㎡','비산삼성래미안85',False),('무궁화마을 85㎡ (호계동)','무궁화85',False)]
vals=[(lab,J[k]['rent']['2026']['new_med']/J[k]['sale']['2026']['med']*100,J[k]['rent']['2026']['new_med']/10000,st) for lab,k,st in items]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'평촌 학원가 아파트 · 전세가율, 2026년 새 세입자 전세 중앙값 ÷ 매매 중앙값',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'학원가 옆 54~57%, 가장 높은 곳은 무궁화마을 66%',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.30,0.13,0.64,0.66])
ys=list(range(len(vals)))[::-1]
for y,(lab,v,r,st) in zip(ys,vals):
    ax.barh(y,v,color=NAVY if st else GRAY,height=0.6)
    ax.text(v+0.8,y,f'{v:.0f}%  (전세 {r:.1f}억)',va='center',fontsize=13,color=NAVY if st else '#555',fontweight='bold' if st else 'normal')
ax.set_yticks(ys); ax.set_yticklabels([v[0] for v in vals],fontsize=13,color='#333')
ax.set_xlim(0,85); ax.set_xticks([])
for sp in ['top','right','bottom']: ax.spines[sp].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
fig.text(0.045,0.055,'남색 = 평촌 학원가 옆 단지 · 회색 = 같은 동안구의 다른 단지 · 전세는 월세 0원 · 신고서 계약 구분 「신규」',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1월~10월 23일 계약 · 해제 거래 뺌 · 85㎡는 전용 83~86㎡ · 80㎡는 79~82㎡)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_rate.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 7화 · 안양 평촌',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'평촌 학원가 아파트',font=kr(ser_,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'같은 현대홈타운인데 차이',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'6억 8,500만',font=kr(ser_,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'귀인마을 80㎡ 14억 · 호계동 85㎡ 7억 1,500 · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')
