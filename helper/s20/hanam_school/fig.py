import json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'

# 1. 권역별 84㎡ 매매 중앙값(2025 · 2026 각 1~10월)과 학교 수
R=[('위례 하남','중 1 · 고 1',12.9,16.5),('감일','중 2 · 고 1',11.7,14.1),('미사','중 5 · 고 3',10.0,12.0),('구도심','중 6 · 고 5',7.3,8.4)]
fig=plt.figure(figsize=(11.55,8.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.958,'하남 학군 비교 · 권역별 학교 수와 84㎡ 매매 중앙값',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.912,'학교가 가장 적은 위례 하남이 84㎡는 가장 비쌉니다',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.25,0.13,0.68,0.68])
y0=[3,2,1,0]
ax.barh([y+0.2 for y in y0],[r[2] for r in R],height=0.36,color=GRAY,label='2025년 1~10월')
ax.barh([y-0.2 for y in y0],[r[3] for r in R],height=0.36,color=NAVY,label='2026년 1~10월')
for y,r in zip(y0,R):
    ax.text(r[2]+0.2,y+0.2,f'{r[2]:.1f}억',va='center',fontsize=14,color='#555')
    ax.text(r[3]+0.2,y-0.2,f'{r[3]:.1f}억',va='center',fontsize=15,color=NAVY,fontweight='bold')
ax.set_yticks(y0); ax.set_yticklabels([f'{r[0]}\n{r[1]}' for r in R],fontsize=15,color='#333')
ax.set_xlim(0,19.5); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#C8D2DE')
ax.legend(loc='lower right',fontsize=13,frameon=False)
fig.text(0.045,0.035,'중 = 중학교 · 고 = 고등학교(구도심 고 5곳 중 2곳은 특성화고) · 학교 목록은 광주하남교육지원청 관내학교현황',fontsize=12.5,color='#8A8578')
fig.text(0.045,0.012,'국토교통부 아파트 매매 실거래(각 1~10월 계약 · 전용 83~86㎡ · 해제 · 직거래 뺌) · 권역 나눔은 본문 자료 설명 참고',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_school_1_area.png'); plt.close()

# 2. 하남 중학교 · 고등학교 위치
S=json.load(open('/tmp/dl/hs_geo.json'))
fig=plt.figure(figsize=(11.55,10.4),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.045,0.965,'하남 학군 비교 · 중학교 14곳 · 고등학교 10곳 위치',fontsize=17,color=BLUE,va='top')
fig.text(0.045,0.93,'미사 8곳 · 구도심 11곳 · 감일 3곳 · 위례 하남 2곳',fontsize=25,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.06,0.08,0.9,0.8])
for n,d,la,lo in S:
    mid=d=='중학교'
    ax.scatter(lo,la,s=170,marker='o' if mid else 's',color=NAVY if mid else BLUE,zorder=3)
    nm=n.replace('고등학교','고').replace('중학교','중')
    L={'미사강변중학교':(0.0015,0.0012,'left'),'미사강변고등학교':(-0.0015,0.0012,'right'),'은가람중학교':(-0.0015,0,'right'),'미사고등학교':(0.0015,0,'left'),
       '윤슬중학교':(-0.0015,0,'right'),'하남고등학교':(-0.0015,-0.0004,'right'),'미사중학교':(0.0015,0,'left'),'한홀중학교':(-0.0015,0,'right'),
       '덕풍중학교':(0.0015,0.0010,'left'),'풍산고등학교':(0.0015,-0.0012,'left'),'신평중학교':(0.0010,0.0030,'center'),'남한중학교':(-0.0015,-0.0018,'right'),'신장고등학교':(-0.0015,0.0020,'right'),
       '신장중학교':(0.0015,0,'left'),'하남경영고등학교':(0.0015,0.0008,'left'),'하남중학교':(-0.0015,-0.0010,'right'),'한국애니고등학교':(0.0015,-0.0010,'left'),
       '남한고등학교':(0.0015,0.0008,'left'),'동부중학교':(-0.0015,-0.0012,'right'),'감일백제중학교':(-0.0015,0,'right'),'감일고등학교':(0.0015,0,'left'),
       '감일중학교':(0.0015,0,'left'),'위례중학교':(-0.0015,0,'right'),'위례고등학교':(0.0015,0.0010,'left')}
    dx,dy,ha=L.get(n,(0.0015,0,'left'))
    ax.text(lo+dx,la+dy,nm,fontsize=13,color='#333',ha=ha,va='center')
for lab,x,y in [('미사',127.160,37.585),('구도심',127.238,37.548),('감일',127.140,37.512),('위례 하남',127.172,37.474)]:
    ax.text(x,y,lab,fontsize=22,color=GRAY,fontweight='bold',ha='center')
ax.scatter([],[],s=120,marker='o',color=NAVY,label='중학교'); ax.scatter([],[],s=120,marker='s',color=BLUE,label='고등학교')
ax.legend(loc='lower right',fontsize=14,frameon=False)
ax.set_xlim(127.12,127.255); ax.set_ylim(37.468,37.590); ax.set_aspect(1/0.79)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_color('#C8D2DE')
fig.text(0.045,0.02,'학교 좌표: 광주하남교육지원청 관내학교현황(11월 5일 조회) · 위아래 = 남북 · 지도 바탕 없이 위치만 찍음',fontsize=12.5,color='#8A8578')
fig.savefig('img/nangman_hanam_school_2_map.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 · 중학교 고등학교',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,370),'하남 학군 비교',font=kr(ser,92),fill='#F4F1EA',anchor='mm')
d.text((W/2,500),'위례 하남 중학교 1곳에',font=kr(ser,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,615),'1,369명',font=kr(ser,116),fill='#D4B04C',anchor='mm')
d.text((W/2,725),'하남 중학교 14곳 평균 702명',font=kr(san,34),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_school_thumb.png')
