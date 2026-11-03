src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
O='/mnt/user-data/outputs/jisandream/imya/'
rows=[('청평 삼회리','2,962평 · 2억 4,000만',8.1,'집 짓기'),('청평 상천리','4만 평 · 32억',7.8,'보전관리 필지'),
('청평 호명리','1만 6천 평 · 8억',5.0,'집 짓기'),('청평 호명리','3만 7천 평 · 14억 8,500만',4.0,'집 짓기'),
('북면 이곡리','6,390평 · 2억 5,500만',4.0,'쉼터 · 관리사'),('북면 이곡리','13,679평 · 5억 4,700만',4.0,'쉼터 · 임업'),('북면 이곡리','2만 평 · 7억',3.5,'쉼터 · 임업')]
fig,ax=plt.subplots(figsize=(10.6,8.4)); fig.subplots_adjust(bottom=0.08,top=0.82,left=0.34,right=0.95)
for i,(a,b,v,u) in enumerate(rows):
    y=len(rows)-1-i; c=CYAN if a.startswith('청평') else DEEP
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+0.12,y,('%.1f만원'%v).replace('.0만','만'),va='center',fontsize=16,color=DEEP,fontproperties=FB)
    ax.text(0.15,y,u,va='center',fontsize=12.5,color='white',fontproperties=FB)
    ax.text(-0.2,y+0.14,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
    ax.text(-0.2,y-0.2,b,ha='right',va='center',fontsize=12,color=GREY,fontproperties=FR)
ax.set_xlim(0,10.3); ax.set_ylim(-0.6,len(rows)-0.4); ax.set_axis_off()
head(fig,'지산드림 · 가평 임야 가격','가평 임야 일곱 곳 평당 3만 5천~8만 1천원')
finish(fig,O+'jisandream_imya_maemae_fig1.png','평당 = 매도가 ÷ 평수 · 매도가는 지산드림 매물 글 본문',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open(O+'jisandream_imya_maemae_map1.png').convert('RGB'); m=m.crop((60,178,m.width-60,m.height-170)).filter(ImageFilter.GaussianBlur(9))
thumb([m],'지산드림 · 가평 임야 일곱 곳','임야 매매 하는 방법','길 · 산지 구분 · 묘지','평당 3만 5천~8만 1천원',O+'jisandream_imya_maemae_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'임야 매매 하는 방법',font=F2(52),fill=(255,226,63))
d.text((40,122),'가평 임야 일곱 곳, 쓰임으로 골라',font=F2(33),fill=(255,255,255))
d.text((40,170),'지번 · 서류 들고 현장 같이 봅니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_imya_maemae_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='임야 매매 하는 방법, 가평 임야 매물 일곱 곳 평당 3만 5천~8만 1천원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_imya_maemae_banner_small.png')
print('ok')
