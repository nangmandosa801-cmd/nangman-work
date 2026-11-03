# -*- coding: utf-8 -*-
# 지금 나온 매물 글 그림 3장 (2026.10.4) — 값과 한 줄은 발행한 매물 글 본문 그대로
import sys; sys.path.insert(0,'/home/claude/blogkit')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from jisan_viz import DEEP, CYAN, COOL, GREY, LINE, FB, FR
from note import finish
O='/mnt/user-data/outputs/jisandream/jisandream_maemul_hub_'
INK='#333333'
# 종류 색 — dataviz validate_palette.js 통과(밝기 · 채도 · 색각 구분 · 대비)
CT={'토지':'#1F6FA8','오피스텔 · 원룸':'#B5761A','지식산업센터 · 상가':'#2BA39B','창고':DEEP}
def clean(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
def head(fig,sub,title,y1=0.955,y2=0.905):
    fig.text(0.04,y1,sub,fontsize=15,color=CYAN,va='center'); fig.text(0.04,y2,title,fontsize=24,color=DEEP,fontproperties=FB,va='center')
def legend(fig,keys,x=0.04,y=0.85):
    for k in keys:
        fig.patches.append(Rectangle((x,y-0.008),0.016,0.016,transform=fig.transFigure,color=CT[k]))
        fig.text(x+0.022,y,k,fontsize=14,color=INK,va='center'); x+=0.05+0.0135*len(k)

# fig1 값 순 막대 (매매 열 건)
R=[('별내역 도보 7분 원룸',10500,'1억 500만원','오피스텔 · 원룸'),('가평 삼회리 임야 2,962평',24000,'2억 4,000만원','토지'),('가평 이곡리 임야 6,390평',25500,'2억 5,500만원','토지'),
   ('화성 새솔동 단독주택용지 94평',45000,'4억 5,000만원','토지'),('가산어반워크2 5층',50500,'5억 500만원','지식산업센터 · 상가'),('별내자이 더 스타 이그제큐티브',60900,'6억 900만원부터','오피스텔 · 원룸'),
   ('가평 이곡리 임야 2만 평',70000,'7억원','토지'),('마곡 롯데캐슬 르웨스트',83700,'8억 3,700만원부터','오피스텔 · 원룸'),('영등포 양평 자이타워 F-614',108560,'분양금 10억 8,560만원','지식산업센터 · 상가'),('여주 산북면 토지 956평',110000,'11억원','토지')]
fig=plt.figure(figsize=(11.2,9.4)); ax=fig.add_axes([0.36,0.10,0.60,0.70])
head(fig,'지산드림에 나온 매매 매물 열 건 · 2026년 10월 4일 기준','갈매동 부동산 매물, 1억 500만원부터 11억원까지')
legend(fig,['토지','오피스텔 · 원룸','지식산업센터 · 상가'])
n=len(R)
for i,(nm,v,lab,k) in enumerate(R):
    y=n-1-i
    ax.barh(y,v,0.58,color=CT[k])
    ax.text(v+2200,y,lab,va='center',fontsize=15,color=INK,fontproperties=FB)
    ax.text(-2500,y,nm,ha='right',va='center',fontsize=14,color=DEEP,fontproperties=FB,clip_on=False)
ax.set_xlim(0,170000); ax.set_ylim(-0.7,n-0.3); clean(ax)
finish(fig,O+'fig1.png','이그제큐티브와 르웨스트는 가장 낮은 호실 값 · 양평 자이타워는 부가세를 넣은 분양금',brand='지산드림',allow_outside=True,strict=False)

# fig2 열두 건 카드
C=[('토지','가평 이곡리 임야 6,390평','2억 5,500만원','폭 6m 임도가 붙어\n대형 덤프까지 드나듭니다'),
   ('토지','가평 이곡리 임야 2만 평','7억원','6.6ha · 임업인 면적 기준\n3ha를 넘습니다'),
   ('토지','가평 삼회리 임야 2,962평','2억 4,000만원','3m 포장도로가 붙어\n길을 새로 낼 필요가 없습니다'),
   ('토지','여주 산북면 토지 956평','11억원','개발행위허가가\n이미 나 있습니다'),
   ('토지','화성 새솔동 단독주택용지 94평','4억 5,000만원','같은 크기가 2025년에\n5억 4,000만원에 팔렸습니다'),
   ('오피스텔 · 원룸','별내역 도보 7분 원룸','1억 500만원','월세 70만원이면\n세전 연 8%입니다'),
   ('오피스텔 · 원룸','별내자이 더 스타 이그제큐티브','6억 900만원부터','별내역 걸어서 1분 ·\n오피스텔로 전환을 마쳤습니다'),
   ('오피스텔 · 원룸','마곡 롯데캐슬 르웨스트','8억 3,700만원부터','단지 지하에서\n마곡역 · 마곡나루역으로 갑니다'),
   ('지식산업센터 · 상가','가산어반워크2 5층','5억 500만원','이 건물에 나온 매물 중\n가장 낮은 값입니다'),
   ('지식산업센터 · 상가','영등포 양평 자이타워 F-614','분양금 10억 8,560만원','2026년 3월 준공 ·\n바로 입주합니다'),
   ('지식산업센터 · 상가','하우스디 가산 퍼스타 1층 상가','보증금 3,000만 / 월 200만원','70m 앞 맞은편 건물에\n상가가 없습니다'),
   ('창고','남양주 진건읍 창고 317평','보증금 1억 5,000만 / 월 1,200만원','그린벨트 안 허가받은 창고 ·\n2층에 5톤 리프트가 있습니다')]
fig=plt.figure(figsize=(11.2,13.2)); ax=fig.add_axes([0.03,0.055,0.94,0.86]); ax.set_xlim(0,99); ax.set_ylim(0,100); ax.axis('off')
head(fig,'지산드림 · 2026년 10월 4일 기준','지금 나온 열두 건, 매물마다 한 줄씩',0.972,0.942)
cw,chh,gx,gy=31.5,23.2,2.25,1.9
for i,(k,nm,pr,ap) in enumerate(C):
    r,c=divmod(i,3); x=c*(cw+gx); y=100-(r+1)*chh-r*gy
    ax.add_patch(FancyBboxPatch((x,y),cw,chh,boxstyle='round,pad=0,rounding_size=1.0',facecolor='white',edgecolor=LINE,lw=1.5))
    ax.add_patch(Rectangle((x,y+chh-1.0),cw,1.0,color=CT[k]))
    ax.text(x+1.6,y+chh-3.6,k,fontsize=13.5,color=CT[k],fontproperties=FB,va='center')
    ax.text(x+1.6,y+chh-7.6,nm,fontsize=14.5 if len(nm)<15 else 13.5,color=DEEP,fontproperties=FB,va='center')
    ax.text(x+1.6,y+chh-12.3,pr,fontsize=17 if len(pr)<12 else 14.5,color=INK,fontproperties=FB,va='center')
    ax.plot([x+1.6,x+cw-1.6],[y+chh-15.2,y+chh-15.2],color=LINE,lw=1.2)
    ax.text(x+1.6,y+chh-19.0,ap,fontsize=13.5,color=INK,va='center',linespacing=1.5)
finish(fig,O+'fig2.png','값은 내놓은 값이며 바뀔 수 있습니다 · 자세한 것은 매물마다 따로 쓴 글에 있습니다',brand='지산드림',allow_outside=True,strict=False)

# fig3 어디에 있나
G=[('구리 · 남양주',['별내역 도보 7분 원룸 (구리 갈매동)','별내자이 더 스타 이그제큐티브 (남양주 별내동)','창고 317평 임대 (남양주 진건읍)']),
   ('가평',['이곡리 임야 6,390평 (북면)','이곡리 임야 2만 평 (북면)','삼회리 임야 2,962평 (청평면)']),
   ('서울',['가산어반워크2 (금천구 가산동)','하우스디 가산 퍼스타 1층 상가 (금천구 가산동)','양평 자이타워 F-614 (영등포구 양평동)','롯데캐슬 르웨스트 (강서구 마곡동)']),
   ('여주',['산북면 토지 956평 (송현리)']),
   ('화성',['송산그린시티 단독주택용지 94평 (새솔동)'])]
fig=plt.figure(figsize=(11.2,8.6)); ax=fig.add_axes([0.04,0.10,0.92,0.74]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
head(fig,'매물이 있는 곳 · 사무소는 구리 갈매동','가평 · 여주 · 화성 · 서울까지 다섯 지역에 있습니다')
y=100
for reg,items in G:
    n=len(items); h=6.6+n*5.2; cy=y-(h-1.6)/2
    ax.add_patch(FancyBboxPatch((0,y-h+1.6),100,h-1.6,boxstyle='round,pad=0,rounding_size=1.0',facecolor=COOL,edgecolor='none'))
    ax.text(3,cy,reg,fontsize=19,color=DEEP,fontproperties=FB,va='center')
    ax.text(27,cy,'%d건'%n,fontsize=19,color=CYAN,fontproperties=FB,va='center',ha='right')
    for j,it in enumerate(items):
        ax.text(31,cy+(n-1)/2*5.2-j*5.2,it,fontsize=14.5,color=INK,va='center')
    y-=h
finish(fig,O+'fig3.png','상세 주소는 문의하시면 알려 드립니다 · 현장은 같이 가서 봅니다',brand='지산드림',allow_outside=True,strict=False)
print('ok')
