import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import json, math
plt.rcParams['font.family']='Noto Sans CJK KR'
NAVY='#1F3864'; BLUE='#2E5C8A'; GRAY='#A9B4C2'
LG='#E4E9EF'; RD='#CBD3DD'; WT='#D6DFE9'
G=json.load(open('geo.json'))
# 지도 범위
LAT0,LAT1=37.5375,37.5845; LON0,LON1=127.158,127.2175
K=math.cos(math.radians(37.561))
def X(lon): return (lon-LON0)*K*111.32   # km
def Y(lat): return (lat-LAT0)*111.32
W=X(LON1); Hh=Y(LAT1)
fig=plt.figure(figsize=(11.55,13.2),dpi=120); fig.patch.set_facecolor('white')
fig.text(0.04,0.975,'하남 9호선 연장 노선도 · 가칭 신미사역(944정거장) 예정지와 역 500m 안 단지',fontsize=16.5,color=BLUE,va='top')
fig.text(0.04,0.945,'신미사역 500m 안 84㎡ 올해 중앙값 12억 6,000만원',fontsize=27,color=NAVY,fontweight='bold',va='top')
ax=fig.add_axes([0.03,0.115,0.94,0.815]); ax.set_xlim(0,W); ax.set_ylim(0,Hh); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(plt.Rectangle((0,0),W,Hh,facecolor='#F7F9FB',edgecolor='none',zorder=0))
# 한강 · 물
if G['river']: ax.add_patch(Polygon([(X(lo),Y(la)) for la,lo in G['river']],closed=True,facecolor=WT,edgecolor='none',zorder=1))
for p in G['water']: ax.add_patch(Polygon([(X(lo),Y(la)) for la,lo in p],closed=True,facecolor=WT,edgecolor='none',zorder=1))
# 단지(연한 회색)
for nm,p in G['res'].items():
    ax.add_patch(Polygon([(X(lo),Y(la)) for la,lo in p],closed=True,facecolor=LG,edgecolor='#D3DAE3',lw=0.6,zorder=2))
# 길
for p in G['roads']: ax.plot([X(lo) for la,lo in p],[Y(la) for la,lo in p],color=RD,lw=0.7,zorder=3,solid_capstyle='round')
for nm,p in G['major']: ax.plot([X(lo) for la,lo in p],[Y(la) for la,lo in p],color='#B9C3CF',lw=1.8,zorder=3,solid_capstyle='round')
# 5호선(파랑 실선)
for p in G['sub5']: ax.plot([X(lo) for la,lo in p],[Y(la) for la,lo in p],color=BLUE,lw=3.2,zorder=5,solid_capstyle='round')
# 9호선 4단계 공사 구간(남색 점선) · 그 뒤 예정 구간은 보도 위치를 직선으로 이음
for p in G['l9c']: ax.plot([X(lo) for la,lo in p],[Y(la) for la,lo in p],color=NAVY,lw=4,ls=(0,(5,3)),zorder=6)
S942=(37.5623,127.1693); S943=(37.5665,127.1778); S944=(37.57201,127.18248)
seg=[S942,S943,S944,(37.5790,127.1925),(37.5818,127.1975)]
ax.plot([X(lo) for la,lo in seg],[Y(la) for la,lo in seg],color=NAVY,lw=4,ls=(0,(5,3)),zorder=6)
ax.annotate('',xy=(X(127.1988),Y(37.5825)),xytext=(X(127.1975),Y(37.5818)),arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=3,mutation_scale=22),zorder=7)
ax.text(X(127.1990),Y(37.5802),'한강 밑(2공구)\n→ 남양주 다산 · 왕숙',fontsize=13,color=NAVY,fontweight='bold',ha='left',va='center',zorder=7,linespacing=1.3)
ax.text(X(127.2060),Y(37.5755),'한강',fontsize=20,color='#8FA2B8',fontweight='bold',zorder=4)
# 역
ST5={'미사역':(37.5630546,127.192822),'하남풍산역':(37.5519584,127.2036311),'하남시청역':(37.5417742,127.2067037),'강일역':(37.5574822,127.1757633)}
def circ(c,r,col):
    la,lo=c; ax.add_patch(Circle((X(lo),Y(la)),r,facecolor=col,alpha=0.07,edgecolor=col,lw=2,ls=(0,(4,3)),zorder=4))
for k in ['미사역','하남풍산역','하남시청역']: circ(ST5[k],0.5,BLUE)
circ(S944,0.5,NAVY)
for k,(la,lo) in ST5.items():
    ax.plot(X(lo),Y(la),'o',ms=15,mfc='white',mec=BLUE,mew=3.5,zorder=8)
ax.text(X(127.192822)+0.12,Y(37.5630546)+0.2,'미사역 (5호선)',fontsize=15,color=BLUE,fontweight='bold',zorder=9)
ax.text(X(127.2036311)+0.14,Y(37.5519584)+0.12,'하남풍산역',fontsize=15,color=BLUE,fontweight='bold',zorder=9)
ax.text(X(127.2067037)+0.16,Y(37.5417742)-0.1,'하남시청역',fontsize=15,color=BLUE,fontweight='bold',zorder=9,ha='left')
ax.text(X(127.1757633)+0.05,Y(37.5574822)-0.33,'강일역 (5호선)',fontsize=13.5,color=BLUE,fontweight='bold',zorder=9,ha='center')
for c,txt,dx,dy,ha in [(S942,'942 고덕강일1지구역(가칭)\n9호선 4단계 · 공사 중',-0.15,-0.32,'right'),(S943,'943 강일(가칭)\n강일리버파크 4·5·7단지 부근',-0.45,0.05,'right')]:
    la,lo=c; ax.plot(X(lo),Y(la),'o',ms=14,mfc='white',mec=NAVY,mew=3.5,zorder=8)
    ax.text(X(lo)+dx,Y(la)+dy,txt,fontsize=12.5,color=NAVY,fontweight='bold',ha=ha,va='center',zorder=9,linespacing=1.35)
la,lo=S944; ax.plot(X(lo),Y(la),'o',ms=22,mfc=NAVY,mec='white',mew=3,zorder=8)
ax.text(X(lo)-0.05,Y(la)+0.55,'944 신미사역(가칭) 예정지\n미사강변대로 × 미사강변북로 교차로',fontsize=15,color=NAVY,fontweight='bold',ha='center',va='bottom',zorder=9,linespacing=1.3,
        bbox=dict(boxstyle='round,pad=0.35',fc='white',ec=NAVY,lw=1.5))
# 500m 안 단지(채움 + 이름 · 84㎡ 올해 중앙값)
def fillres(nm,col):
    if nm in G['res']: ax.add_patch(Polygon([(X(lo),Y(la)) for la,lo in G['res'][nm]],closed=True,facecolor=col,alpha=0.55,edgecolor=col,lw=1,zorder=4))
L944=[('미사강변 리슈빌엔에이치에프','리슈빌 NHF\n11억 8,000만',(37.5740,127.1778),'center'),('미사강변 스타힐스','스타힐스\n13억 1,150만',(37.5707,127.1868),'left'),
      ('미사강변 센트리버','센트리버\n12억 5,250만',(37.5745,127.1878),'left'),('미사강변도시 베라체','베라체\n10억 9,000만',(37.5716,127.1745),'center'),('미사강변루나리움','루나리움\n12억 6,500만',(37.5665,127.1808),'center')]
for nm,txt,(la,lo),ha in L944:
    fillres(nm,NAVY); ax.text(X(lo),Y(la),txt,fontsize=12.5,color=NAVY,fontweight='bold',ha=ha,va='center',zorder=9,linespacing=1.3)
L5=[('미사강변 골든센트로','골든센트로\n13억 2,500만',(37.5585,127.1992)),('미사강변 브라운스톤 엔에이치에프','브라운스톤\n11억 4,600만',(37.5572,127.1900)),
    ('미사강변 효성해링턴플레이스 엔에이치에프','해링턴플레이스\n10억 7,000만',(37.5651,127.2005)),('하남풍산아이파크5단지','풍산아이파크 5단지\n10억 4,700만',(37.5545,127.1975))]
for nm,txt,(la,lo) in L5:
    fillres(nm,BLUE); ax.text(X(lo),Y(la),txt,fontsize=12.5,color=BLUE,fontweight='bold',ha='center',va='center',zorder=9,linespacing=1.3)
# 하남시청역 주변(단지 모양 자료 없음 → 점)
P5=[('진모루마을현대\n8억 3,000만',(37.5412598,127.2055938),(37.5392,127.2010)),('더샵하남에디피스\n14억 500만',(37.5434332,127.2056028),(37.5428,127.1992)),
    ('더샵센트럴뷰\n10억 6,500만',(37.5444484,127.204189),(37.5468,127.1995)),('에코타운 2단지\n9억 9,000만',(37.5425145,127.2111623),(37.5440,127.2140)),('풍산아이파크 1단지\n10억 4,800만',(37.5460369,127.208464),(37.5480,127.2115))]
for txt,(la,lo),(tla,tlo) in P5:
    ax.plot(X(lo),Y(la),'s',ms=11,mfc=BLUE,mec='white',mew=1.5,zorder=8)
    ax.text(X(tlo),Y(tla),txt,fontsize=12,color=BLUE,fontweight='bold',ha='center',va='center',zorder=9,linespacing=1.3)
ax.text(X(127.1935),Y(37.5492),'풍산역 500m 안\n84㎡ 거래 단지는 1곳',fontsize=11.5,color='#55657A',ha='center',va='center',zorder=9,linespacing=1.3)
# 지명
for txt,(la,lo) in [('미사강변도시',(37.5660,127.1900)),('강일동(서울)',(37.5735,127.1690)),('풍산동',(37.5560,127.2100)),('신장동',(37.5392,127.2160))]:
    ax.text(X(lo),Y(la),txt,fontsize=13,color='#8A96A6',ha='center',va='center',zorder=9)
# 축척
ax.plot([0.3,1.3],[0.3,0.3],color='#555',lw=3,zorder=9); ax.text(0.8,0.42,'1km',fontsize=13,color='#555',ha='center',zorder=9)
# 범례(지도 아래)
lg=fig.add_axes([0.03,0.068,0.94,0.04]); lg.set_xlim(0,100); lg.set_ylim(0,10); lg.axis('off')
lg.plot([1,6],[5,5],color=NAVY,lw=4,ls=(0,(5,3))); lg.text(7,5,'9호선 연장 예정(강동하남남양주선)',fontsize=12.5,color='#333',va='center')
lg.plot([38,43],[5,5],color=BLUE,lw=3.2); lg.text(44,5,'5호선(운행 중)',fontsize=12.5,color='#333',va='center')
from matplotlib.patches import Ellipse
lg.add_patch(Ellipse((62.5,5),3.2,8,facecolor=NAVY,alpha=0.1,edgecolor=NAVY,lw=1.5,ls=(0,(4,3)))); lg.text(65,5,'역 500m(직선거리) · 색 칠한 단지 = 84㎡ 거래 있음',fontsize=12.5,color='#333',va='center')
fig.text(0.04,0.052,'역 위치: 944 · 943은 강동하남남양주선 전략환경영향평가 초안(2024년 2월 · 하남일보 보도) 기준 · 943 · 942는 어림 · 5호선 역 · 단지 · 길 · 강은 오픈스트리트맵',fontsize=11.5,color='#8A8578')
fig.text(0.04,0.033,'금액: 국토교통부 아파트 매매 실거래 2026년 1~10월 계약 · 전용 83~86㎡ 단지별 중앙값 · 해제 · 직거래 뺌 · 500m는 역과 단지 가운데 사이 직선거리',fontsize=11.5,color='#8A8578')
fig.text(0.04,0.014,'낭만 부동산 분석 플랫폼 · blog.naver.com/dong_jin_kim',fontsize=11.5,color='#8A8578')
fig.savefig('img/nangman_hanam_line9_map_1_map.png'); plt.close()

from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
Wd=1000; im=Image.new('RGB',(Wd,Wd),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,Wd,14],fill='#D4B04C'); d.rectangle([0,Wd-14,Wd,Wd],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 하남 미사 · 한 장 지도',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((Wd/2,360),'하남 9호선 연장',font=kr(ser,88),fill='#F4F1EA',anchor='mm')
d.text((Wd/2,490),'신미사역 500m 안 84㎡',font=kr(ser,60),fill='#F4F1EA',anchor='mm')
d.text((Wd/2,605),'12억 6천',font=kr(ser,92),fill='#D4B04C',anchor='mm')
d.text((Wd/2,710),'역 예정지는 미사강변대로 × 미사강변북로 교차로',font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/nangman_hanam_line9_map_thumb.png')
print('ok')
