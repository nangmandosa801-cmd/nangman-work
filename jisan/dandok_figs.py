src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
O='/mnt/user-data/outputs/jisandream/dandok/'
fig,ax=plt.subplots(figsize=(10.6,6.6)); fig.subplots_adjust(bottom=0.13,top=0.76,left=0.31,right=0.93)
ax.barh(1,4.5,color=CYAN,height=0.55); ax.barh(1,3.4,left=4.5,color='#C9962E',height=0.55)
ax.text(2.25,1,'땅 4억 5천',ha='center',va='center',fontsize=16,color='white',fontproperties=FB)
ax.text(6.2,1,'40평 건축 3억 4천',ha='center',va='center',fontsize=15,color='white',fontproperties=FB)
ax.text(8.0,1,'7억 9,000만',va='center',fontsize=18,color=DEEP,fontproperties=FB)
ax.barh(0,5.45,color=GREY,height=0.55); ax.text(5.6,0,'5억 4,500만',va='center',fontsize=18,color=DEEP,fontproperties=FB)
for y,a,b in [(1,'94평 땅 + 40평 집','쓰는 넓이 40평 · 마당 · 주차'),(0,'새솔동 아파트 84㎡','전용 25.4평')]:
    ax.text(-0.15,y+0.12,a,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-0.15,y-0.22,b,ha='right',va='center',fontsize=12.5,color=GREY,fontproperties=FR)
ax.set_xlim(0,10); ax.set_ylim(-0.6,1.6); ax.set_axis_off()
head(fig,'지산드림 · 단독주택 짓기 비용','아파트보다 2억 4,500만원 더 들고 쓰는 넓이는 1.6배입니다')
finish(fig,O+'jisandream_dandok_biyong_fig1.png','땅은 지산드림 매물 · 건축비 평당 850만원은 계산용 가정 · 취득세 · 설계비 빼고',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open(O+'jisandream_dandok_biyong_map1.png').convert('RGB'); m=m.crop((60,178,m.width-60,m.height-170)).filter(ImageFilter.GaussianBlur(8))
thumb([m],'지산드림 · 송산그린시티 103블록','단독주택 짓기 비용','94평 땅 4억 5천만원','같은 크기가 2025년 5억 4천에 팔림',O+'jisandream_dandok_biyong_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'단독주택 짓기 비용',font=F2(52),fill=(255,226,63))
d.text((40,122),'새솔동 94평 땅 4억 5천만원',font=F2(33),fill=(255,255,255))
d.text((40,170),'40평 집을 지으면 합계 7억 9천',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_dandok_biyong_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='단독주택 짓기 비용, 새솔동 단독주택 토지 94평 4억 5천만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_dandok_biyong_banner_small.png')
print('ok')
