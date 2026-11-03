src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/songsan/'
GOLD='#C9962E'; RED='#B5503C'
# fig1
fig,ax=plt.subplots(figsize=(10.6,6.0)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.34,right=0.93)
for i,(a,v,c,lab) in enumerate([('단독주택 토지 평당',40,GOLD,'+40% (382만 → 534만원)'),('아파트 84㎡',-10,RED,'−10%')]):
    y=1-i; ax.barh(y,abs(v),color=c,height=0.55); ax.text(abs(v)+0.8,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.8,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.set_xlim(0,75); ax.set_ylim(-0.6,1.6); ax.set_axis_off()
head(fig,'지산드림 · 송산그린시티 새솔동','2021년보다 아파트는 내리고 단독주택 토지는 올랐습니다')
finish(fig,O+'jisandream_songsan_fig1.png','국토교통부 실거래 · 지산드림 새솔동 단독주택 글 본문 그대로',brand='지산드림',allow_outside=True,strict=False)
# fig2
fig,ax=plt.subplots(figsize=(10.6,6.6)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
rows=[('2023년 312㎡',360,GREY,'360만원'),('2025년 312㎡',572,CYAN,'572만원'),('2026년 326㎡',521,CYAN,'521만원'),('2026년 327㎡',627,CYAN,'627만원'),('103블록 매물 312㎡',477,GOLD,'477만원')]
for i,(a,v,c,lab) in enumerate(rows):
    y=len(rows)-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+8,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-8,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.set_xlim(0,800); ax.set_ylim(-0.6,len(rows)-0.4); ax.set_axis_off()
head(fig,'지산드림 · 송산그린시티 단독주택','새솔동 단독주택용지 평당 가격')
finish(fig,O+'jisandream_songsan_fig2.png','국토교통부 토지 실거래 · 제1종전용주거지역 대지 280~350㎡',brand='지산드림',allow_outside=True,strict=False)
# fig3
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.06,top=0.8,left=0.03,right=0.97)
ax.set_xlim(0,10); ax.set_ylim(0,6); ax.set_axis_off()
for k,(h,c,lines) in enumerate([('주거전용 단독주택용지',CYAN,[('살 집을 짓는 땅',1),('직접 살 분',0),('103블록이 여기',0)]),('점포겸용 단독주택',GOLD,[('1층에 가게',1),('세 · 가게를 할 분',0),('',0)])]):
    x0=k*5+0.15
    ax.add_patch(FancyBboxPatch((x0,0.3),4.7,5.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
    ax.add_patch(FancyBboxPatch((x0,4.3),4.7,1.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c,lw=3))
    ax.text(x0+2.35,4.9,h,ha='center',va='center',fontsize=18,color='white',fontproperties=FB)
    for j,(t,big) in enumerate(lines):
        if t: ax.text(x0+2.35,3.5-j*0.85,t,ha='center',va='center',fontsize=21 if big else 16,color=c if big else DEEP,fontproperties=FB if big else FR)
head(fig,'지산드림 · 단독주택용지 뜻','신도시에서 단독주택만 짓도록 나눠 놓은 땅')
finish(fig,O+'jisandream_songsan_fig3.png','지을 수 있는 것은 지구단위계획으로 확인',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open('/mnt/user-data/outputs/jisandream/dandok/jisandream_dandok_biyong_map1.png').convert('RGB'); m=m.crop((60,178,m.width-60,m.height-170))
card(m,'송산그린시티 단독주택 · 103블록','새솔동 단독주택용지 94.4평 위치',O+'jisandream_songsan_map2.png')
w=Image.open(O+'jisandream_songsan_map1.png').convert('RGB'); w=w.crop((60,178,w.width-60,w.height-170)).filter(ImageFilter.GaussianBlur(8))
thumb([w],'지산드림 · 화성 새솔동 103블록','송산그린시티 단독주택','94평 땅 4억 5천','같은 크기가 2025년 5억 4천에 팔림',O+'jisandream_songsan_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'송산그린시티',font=F2(52),fill=(255,226,63))
d.text((40,122),'새솔동 단독주택용지 94평 4억 5천',font=F2(33),fill=(255,255,255))
d.text((40,170),'땅 · 건축비 예산을 같이 맞춰 봅니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_songsan_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='송산그린시티, 새솔동 단독주택용지 94평 4억 5,000만원'
f=F2(19); tw=d.textlength(t,font=f); d.text(((773-tw)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_songsan_banner_small.png')
print('ok')
