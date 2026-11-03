src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/gasan/'
RED='#B5654E'
rows=[('같은 건물 9층','2024년 8월 거래',1376,GREY),('같은 건물 9층','2024년 8월 거래',1348,GREY),('2021년 분양가','부가세 빼고',1240,'#5B8FB0'),('다른 매물 최저 호가','이 건물',1210,'#5B8FB0'),('5층 513호','지산드림 매물 · 5억 500만원',1130,RED)]
fig,ax=plt.subplots(figsize=(10.6,7.6)); fig.subplots_adjust(bottom=0.11,top=0.79,left=0.31,right=0.93)
n=len(rows); ys=list(range(n))[::-1]
for y,(a,b,v,c) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+15,y,'%s만원'%format(v,','),va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-15,y+0.13,a,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-15,y-0.27,b,va='center',ha='right',fontsize=12.5,color=GREY,fontproperties=FR)
ax.set_xlim(0,1700); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
head(fig,'지산드림 · 가산디지털단지 사무실 매매','513호는 같은 건물 거래보다 평당 16~18% 낮습니다')
finish(fig,O+'jisandream_gasan_samusil_fig1.png','계약면적 평당 · 부가세 빼고 · 같은 건물 거래는 국토교통부 실거래(전용률 50%로 계약면적 환산)',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open(O+'jisandream_gasan_samusil_map1.png').convert('RGB'); m=m.crop((60,178,m.width-60,m.height-170))
thumb([m],'지산드림 · 가산어반워크2 5층 513호','가산디지털단지 사무실','5억 500만원','같은 건물 거래보다 16% 낮음 · 인테리어 완료',O+'jisandream_gasan_samusil_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'가산디지털단지 사무실',font=F2(52),fill=(255,226,63))
d.text((40,122),'가산어반워크2 전용 22평 5억 500만원',font=F2(33),fill=(255,255,255))
d.text((40,170),'인테리어 완료 · 공실 · 역 8분',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_gasan_samusil_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='가산디지털단지 사무실 매매, 가산어반워크2 513호 5억 500만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_gasan_samusil_banner_small.png')
print('ok')
