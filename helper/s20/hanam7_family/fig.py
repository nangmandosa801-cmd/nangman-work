import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
# 1. 미사 · 감일 · 덕풍 84㎡ 2026년 매매 중앙값 · 새 전세 중앙값과 7억
G=['미사\n(망월 · 풍산 · 선동)','감일\n(감일 · 감이동)','덕풍\n(구도심)']
sale=[12.0,14.1,7.7]; rent=[7.0,7.2,5.8]
fig=plt.figure(figsize=(11.55,7.6),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.955,'하남 신혼부부 아파트 · 84㎡ 2026년 매매 중앙값 · 새 전세 중앙값과 7억',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.905,'7억으로 사는 84㎡는 덕풍, 미사 84㎡는 전세 중앙값이 7억입니다',fontsize=24,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.08,0.16,0.88,0.62])
import numpy as np
x=np.arange(3); w=0.34
ax.bar(x-w/2,sale,w,color=NAVY,label='매매 중앙값'); ax.bar(x+w/2,rent,w,color=GRAY,label='새 전세 중앙값')
for i,(s,r) in enumerate(zip(sale,rent)):
    ax.text(i-w/2,s+0.25,f'{s:.1f}억'.replace('.0억','억'),ha='center',fontsize=16,color=NAVY,fontweight='bold')
    ax.text(i+w/2,r+0.25,f'{r:.1f}억'.replace('.0억','억'),ha='center',fontsize=15,color='#555',fontweight='bold')
ax.axhline(7,color=BLUE,lw=2,ls='--'); ax.text(2.55,7.15,'예산 7억',fontsize=14,color=BLUE,ha='right',fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(G,fontsize=14,color='#333'); ax.set_ylim(0,16); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C8D2DE')
ax.legend(loc='upper left',fontsize=13,frameon=False)
fig.text(0.045,0.045,'국토교통부 아파트 매매 · 전월세 실거래(2026년 1월~10월 23일 계약 · 하남 전용 83~86㎡ · 매매는 해제 · 직거래 뺌) · 매매 미사 419건 · 감일 110건 · 덕풍 251건',fontsize=12,color='#8A8578')
fig.text(0.045,0.02,'중앙값 = 거래를 금액 순으로 세웠을 때 한가운데 값 · 새 전세 = 계약구분 「신규」 · 전세 미사 287건 · 감일 119건 · 덕풍 110건',fontsize=12,color='#8A8578')
fig.savefig('img/nangman_hanam7_family_1_three.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 예시 가족 계산서',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,350),'하남 신혼부부 아파트',font=kr(ser,78),fill='#F4F1EA',anchor='mm')
d.text((W/2,480),'예산 7억으로 사는 84㎡',font=kr(ser,56),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'미사 0건 · 감일 0건 · 덕풍 76건',font=kr(ser,62),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'2026년 실거래 · 대출 · 취득세 · 이자 · 출퇴근까지',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam7_family_thumb.png')
