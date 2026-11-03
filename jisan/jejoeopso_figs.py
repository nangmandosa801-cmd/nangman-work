src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/jejoeopso/'
GRN='#2E7D50'
# fig1 제조업소 공장 차이 갈림표
fig,ax=plt.subplots(figsize=(10.6,8.0)); fig.subplots_adjust(bottom=0.10,top=0.80,left=0.04,right=0.96)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_axis_off()
def box(x,y,w,h,c,t,s=17,fc='white',font=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.25',fc=fc,ec=c,lw=2.4))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=s,color=c if fc=='white' else 'white',fontproperties=font or FB,linespacing=1.5)
box(2.6,8.0,4.8,1.5,DEEP,'물건을 만들고 고치는 건물',19,fc=DEEP)
box(0.4,5.0,4.2,1.9,CYAN,'질문 ①\n제조 용도 바닥면적 합계\n500㎡(약 151평) 미만?',16)
box(5.4,5.0,4.2,1.9,CYAN,'질문 ②\n배출시설 허가 · 신고 대상 아님\n또는 폐수 전부 위탁처리?',16)
box(0.6,0.9,4.6,2.4,GRN,'두 질문 모두 예\n제2종 근린생활시설\n제조업소',19,fc=GRN)
box(5.6,0.9,3.8,2.4,GREY,'하나라도 아니오\n공장',19,fc=GREY)
for (x0,y0,x1,y1) in [(4.2,8.0,2.5,6.95),(5.8,8.0,7.5,6.95),(2.5,5.0,2.9,3.35),(7.5,5.0,2.9,3.35)]:
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops=dict(arrowstyle='-|>',color=DEEP,lw=2))
ax.annotate('',xy=(7.5,3.35),xytext=(7.5,5.0),arrowprops=dict(arrowstyle='-|>',color=GREY,lw=2,ls='--'))
ax.text(7.75,4.15,'아니오',fontsize=14,color=GREY,fontproperties=FB)
ax.text(3.0,4.15,'예',fontsize=14,color=GRN,fontproperties=FB)
head(fig,'지산드림 · 제조업소 공장 차이','바닥 500㎡ 미만 · 배출시설 조건이면 제2종 근린생활시설입니다')
finish(fig,O+'jisandream_jejoeopso_fig1.png','건축법 시행령 별표 1 제4호 너목 · 배출 조건은 두 가지 가운데 하나만 맞으면 됩니다',brand='지산드림',allow_outside=True,strict=False)
# fig2 평당 가격
rows=[('송현리 계획관리 밭','2026년 실거래',70,GREY),('여주 산북면 956평','제조업소 허가 · 이 매물',115,CYAN),('송현리 계획관리 대지','2025년 실거래',132,DEEP)]
fig,ax=plt.subplots(figsize=(10.6,6.6)); fig.subplots_adjust(bottom=0.13,top=0.76,left=0.33,right=0.93)
ys=[2,1,0]
for y,(a,b,v,c) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+2,y,'평당 %d만원'%v,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-3,y+0.13,a,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-3,y-0.25,b,va='center',ha='right',fontsize=13,color=GREY,fontproperties=FR)
ax.set_xlim(0,175); ax.set_ylim(-0.6,2.6); ax.set_axis_off()
head(fig,'지산드림 · 여주 토지 매물, 평당 가격','허가가 난 땅은 밭과 대지 사이 가격입니다')
finish(fig,O+'jisandream_jejoeopso_fig2.png','송현리 실거래는 발행한 매물 글 본문 그대로 · 이 매물 11억원 ÷ 956평',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 여주 토지 매물',['제조업소 공장 차이','500㎡ 미만이면 근린생활시설'],'여주 산북면 956평 · 제조업소 허가가 이미 나 있습니다',O+'jisandream_jejoeopso_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'제조업소 공장 차이',font=F(52),fill=(255,226,63))
d.text((40,122),'바닥 500㎡ 미만이면 근린생활시설',font=F(33),fill=(255,255,255))
d.text((40,170),'여주 956평에 그 허가가 나 있습니다',font=F(33),fill=(255,255,255))
b.save(O+'jisandream_jejoeopso_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='제조업소 공장 차이, 여주 산북면 956평 제조업소 허가 매물'
f=F(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_jejoeopso_banner_small.png')
print('ok')
