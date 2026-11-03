src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
GRN='#2E7D50'
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
def banners(O,slug,big,l1,l2,small):
    b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
    d.rectangle((0,0,773,227),fill=(44,79,83))
    d.text((40,38),big,font=F(52),fill=(255,226,63)); d.text((40,122),l1,font=F(33),fill=(255,255,255)); d.text((40,170),l2,font=F(33),fill=(255,255,255))
    b.save(O+f'jisandream_{slug}_banner.png')
    s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
    strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
    f=F(19); w=d.textlength(small,font=f); d.text(((773-w)/2,105),small,font=f,fill=(170,190,192))
    s.save(O+f'jisandream_{slug}_banner_small.png')
# 카페
O='/mnt/user-data/outputs/jisandream/cafe/'
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.05,right=0.95)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_axis_off()
from matplotlib.patches import FancyBboxPatch
def box(x,c,head_,big,sub):
    ax.add_patch(FancyBboxPatch((x,0.6),4.3,8.6,boxstyle='round,pad=0.02,rounding_size=0.3',fc='white',ec=c,lw=3))
    ax.text(x+2.15,8.2,head_,ha='center',va='center',fontsize=22,color=c,fontproperties=FB)
    ax.text(x+2.15,5.6,big,ha='center',va='center',fontsize=34,color=DEEP,fontproperties=FB)
    ax.text(x+2.15,2.6,sub,ha='center',va='center',fontsize=15,color=GREY,fontproperties=FR,linespacing=1.6)
box(0.4,CYAN,'빌리기','1년 3,528만원','권리금 0원 · 보증금 3,000만원\n월세 250만 + 관리비 44만')
box(5.3,GREY,'사기','19억 3,237만원','1층 전용 평당 5,127만원\n× 37.69평')
head(fig,'지산드림 · 카페 창업 비용','갈매동 1층 38평, 빌리면 1년 3,528만원 · 사면 19억이 넘습니다')
finish(fig,O+'jisandream_cafe_biyong_fig1.png','사기 쪽은 갈매동 1층 근린생활 상가 최근 2년 실거래 16건 중앙값 · 취득세 · 인테리어 비용 빼고',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 갈매동 1층 카페 임대',['카페 창업 비용','권리금 0원 · 월 294만원'],'현대테라타워 1층 38평 · 보증금 3,000만원',O+'jisandream_cafe_biyong_thumb.png')
banners(O,'cafe_biyong','카페 창업 비용','갈매동 1층 38평 권리금 0원','보증금 3천 · 한 달 294만원','카페 창업 비용, 갈매동 1층 38평 권리금 없는 카페 임대')
# 별내역 오피스텔
O='/mnt/user-data/outputs/jisandream/byop/'
rows=[('휴밸나인 복층 원룸','월세 65만~70만원 받음',1.05,CYAN,'1억 500만'),('이그제큐티브 59타입','전세 4억 5천 끼고 · 취득세 포함',1.8701,DEEP,'1억 8,701만'),('두 채 함께','',2.9201,GRN,'2억 9,201만')]
fig,ax=plt.subplots(figsize=(10.6,6.4)); fig.subplots_adjust(bottom=0.13,top=0.76,left=0.33,right=0.92)
for y,(a,b,v,c,lab) in zip([2,1,0],rows):
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+0.05,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.08,y+(0.13 if b else 0),a,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
    if b: ax.text(-0.08,y-0.27,b,va='center',ha='right',fontsize=12.5,color=GREY,fontproperties=FR)
ax.set_xlim(0,3.9); ax.set_ylim(-0.6,2.6); ax.set_axis_off()
head(fig,'지산드림 · 별내역 오피스텔','1억 500만원은 월세 받고 1억 8,701만원은 새 59타입')
finish(fig,O+'jisandream_byeolnaeyeok_op_fig1.png','금액은 지산드림 매물 글 본문 그대로 · 59타입은 분양가 6억 900만원 + 취득세 4.6% − 전세 중앙값',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 별내역 오피스텔 매물 두 건',['별내역 오피스텔','1억 500만원 월세 70만원'],'새 59타입은 전세 끼고 1억 8,700만원',O+'jisandream_byeolnaeyeok_op_thumb.png')
banners(O,'byeolnaeyeok_op','별내역 오피스텔','1억 500만원 복층 원룸 월세 70만원','새 59타입은 1억 8,700만원','별내역 오피스텔, 복층 원룸 1억 500만원 · 59타입 1억 8,700만원')
print('ok')
