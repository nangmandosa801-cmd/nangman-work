src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
O='/mnt/user-data/outputs/jisandream/yangdo/'
GOLD='#C9962E'; RED='#B5503C'
fig,ax=plt.subplots(figsize=(10.6,6.8)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
rows=[('1,400만원 이하',6),('5,000만원 이하',15),('8,800만원 이하',24),('1억 5천 이하',35),('3억 이하',38)]
for i,(a,v) in enumerate(rows):
    y=len(rows)-1-i
    ax.barh(y+0.18,v,color=CYAN,height=0.34); ax.text(v+0.5,y+0.18,f'{v}%',va='center',fontsize=14,color=DEEP,fontproperties=FB)
    ax.barh(y-0.18,v+10,color=RED,height=0.34); ax.text(v+10.5,y-0.18,f'{v+10}%',va='center',fontsize=14,color=RED,fontproperties=FB)
    ax.text(-0.6,y,a,ha='right',va='center',fontsize=15,color=DEEP,fontproperties=FB)
ax.text(30,4.35,'■ 사업용(기본세율)',color=CYAN,fontsize=13,fontproperties=FB); ax.text(30,3.95,'■ 비사업용 토지',color=RED,fontsize=13,fontproperties=FB)
ax.set_xlim(0,58); ax.set_ylim(-0.6,len(rows)-0.3); ax.set_axis_off()
head(fig,'지산드림 · 임야 양도세율','근처에 살지 않은 산은 구간마다 10% 더')
finish(fig,O+'jisandream_imya_yangdo_fig1.png','소득세법 기본세율(2023년~) · 과세표준 구간 · 지방소득세 10% 따로',brand='지산드림',allow_outside=True,strict=False)
fig,ax=plt.subplots(figsize=(10.6,5.8)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
for i,(a,v,c) in enumerate([('사업용 (재촌)',1284,CYAN),('비사업용',2059,RED)]):
    y=1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+25,y,f'{v:,}만원',va='center',fontsize=20,color=DEEP,fontproperties=FB)
    ax.text(-25,y,a,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB)
ax.text(1300,0.5,'차이 775만원',fontsize=17,color=GOLD,fontproperties=FB)
ax.set_xlim(0,2700); ax.set_ylim(-0.6,1.6); ax.set_axis_off()
head(fig,'지산드림 · 임야 양도세 계산','이곡리 산 104를 10년 뒤 1억 남기고 판다면')
finish(fig,O+'jisandream_imya_yangdo_fig3.png','판 값은 가정 · 장기보유특별공제 20% · 기본공제 250만원 · 필요경비 · 지방소득세 빼고',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open('/mnt/user-data/outputs/jisandream/imya/jisandream_imya_maemae_map1.png').convert('RGB'); m=m.crop((60,178,m.width-60,m.height-170))
card(m,'임야 양도세 · 가평 임야 매물','청평 넷 · 북면 셋, 일곱 곳 위치',O+'jisandream_imya_yangdo_map1.png')
w=m.filter(ImageFilter.GaussianBlur(9))
thumb([w],'지산드림 · 가평 임야 일곱 곳','임야 양도세','근처에 살면 775만원 덜','1억 남길 때 사업용 · 비사업용 차이',O+'jisandream_imya_yangdo_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'임야 양도세',font=F2(52),fill=(255,226,63))
d.text((40,122),'사시는 곳으로 재촌부터 봅니다',font=F2(33),fill=(255,255,255))
d.text((40,170),'가평 임야 일곱 곳 안내',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_imya_yangdo_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='임야 양도세, 가평 산 1억 남기면 재촌 1,284만원 · 비사업용 2,059만원'
f=F2(19); tw=d.textlength(t,font=f); d.text(((773-tw)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_imya_yangdo_banner_small.png')
print('ok')
