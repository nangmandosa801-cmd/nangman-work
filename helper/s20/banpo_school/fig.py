import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, json
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
S='nangman_banpo_school_'
J=json.load(open('ana.json'))
D=['래미안원베일리','아크로리버파크','래미안퍼스티지','반포자이']; LAB=['래미안원베일리\n(2023년)','아크로리버파크\n(2016년)','래미안퍼스티지\n(2009년)','반포자이\n(2009년)']
# 1. 84㎡ 2025 · 2026 매매 중앙값 + 새 세입자 전세
v25=[J['d'][d]['84']['2025']['med']/10000 for d in D]; v26=[J['d'][d]['84']['2026']['med']/10000 for d in D]; jn=[J['d'][d]['84']['jn']['med']/10000 for d in D]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'반포 아파트 시세 · 84㎡ 매매 중앙값(2025년 · 2026년 1~10월)과 새 세입자 전세',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'매매 48억~58억 7,500만 · 전세 16억 5,000만~21억',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.17,0.92,0.58])
x=list(range(4)); w=0.26
ax.bar([i-w for i in x],v25,width=w,color=GRAY); ax.bar(x,v26,width=w,color=NAVY); ax.bar([i+w for i in x],jn,width=w,color=BLUE)
for i in x:
    ax.text(i-w,v25[i]+0.8,f'{v25[i]:.1f}',ha='center',fontsize=11.5,color='#777')
    ax.text(i,v26[i]+0.8,f'{v26[i]:.1f}',ha='center',fontsize=13,color=NAVY,fontweight='bold')
    ax.text(i+w,jn[i]+0.8,f'{jn[i]:.1f}',ha='center',fontsize=12.5,color=BLUE,fontweight='bold')
    ax.text(i+w,jn[i]/2,f'{jn[i]/v26[i]*100:.0f}%',ha='center',va='center',fontsize=12,color='white',fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(LAB,fontsize=13,color='#555')
ax.set_yticks([]); ax.set_ylim(0,68)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.text(3.45,62,'회색 2025년 매매 · 남색 2026년 매매 · 파랑 새 세입자 전세(막대 안 = 전세가율)',fontsize=12,color='#7A8590',ha='right')
fig.text(0.045,0.055,'숫자는 억원 · 전세가율 = 새 세입자 전세 중앙값 ÷ 2026년 매매 중앙값',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 · 전월세 실거래(서초구 반포동 · 잠원동 · 전용 83~86㎡ · 해제 거래 뺌 · 전세는 2026년 월세 0원 신규 계약 · 10월 24일 신고분까지)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'1_price.png'); plt.close()

# 2. 2021~2026 해마다 84㎡ 중앙값 · 아크로 · 퍼스티지 · 반포자이 · 잠실엘스
yrs=['2021','2022','2023','2024','2025','2026']
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'반포 아파트 시세 · 84㎡ 해마다 매매 중앙값, 2021~2026년',fontsize=16,color=BLUE,va='top')
fig.text(0.045,0.9,'2023년은 2021년보다 반포 세 단지 +2~6% · 잠실엘스 −7%',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.09,0.14,0.86,0.64])
xs=list(range(6))
series=[('아크로리버파크',[J['d']['아크로리버파크']['84'][y]['med']/10000 for y in yrs],NAVY,2.8),('래미안퍼스티지',[J['d']['래미안퍼스티지']['84'][y]['med']/10000 for y in yrs],BLUE,2.8),('반포자이',[J['d']['반포자이']['84'][y]['med']/10000 for y in yrs],'#6F8FB0',2.4),('잠실엘스(송파 · 2008년)',[J['jamsil'][y]['med']/10000 for y in yrs],GRAY,2.4)]
OFF={'아크로리버파크':(0,1.0,'center','bottom'),'래미안퍼스티지':(-0.22,0.3,'right','bottom'),'반포자이':(0,-1.0,'center','top'),'잠실엘스(송파 · 2008년)':(0,-1.0,'center','top')}
for nm,v,c,lw in series:
    ax.plot(xs,v,color=c,lw=lw,marker='o')
    ax.text(5.15,v[-1],nm,fontsize=12.5,color=c if c!=GRAY else '#777',va='center')
    dx,dy,ha,va=OFF[nm]
    for i in [0,2,5]:
        ax.text(i+dx,v[i]+dy,f'{v[i]:.1f}',ha=ha,fontsize=12,color=c if c!=GRAY else '#777',fontweight='bold',va=va)
ax.set_xticks(xs); ax.set_xticklabels([y+'년' for y in yrs],fontsize=13,color='#555'); ax.set_xlim(-0.3,6.6)
ax.set_yticks([20,30,40,50,60]); ax.set_yticklabels(['20억','30억','40억','50억','60억'],fontsize=12,color='#555'); ax.set_ylim(18,62)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color('#C8D2DE')
fig.text(0.045,0.055,'숫자는 억원 · 2022년은 아크로리버파크 2건 · 반포자이 9건 · 래미안원베일리는 2023년 입주라 뺌',fontsize=12,color='#8A8578')
fig.text(0.045,0.025,'국토교통부 아파트 매매 실거래(2021년 1월~2026년 10월 24일 계약 · 전용 83~86㎡ · 해제 거래 뺌)',fontsize=12,color='#8A8578')
fig.savefig('img/'+S+'2_year.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 4화 · 서초구 반포',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'반포 아파트 시세',font=kr(ser,86),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'래미안원베일리 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'58억 7,500',font=kr(ser,100),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'새 세입자 전세 21억 · 전세가율 36% · 2026년 실거래',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')
