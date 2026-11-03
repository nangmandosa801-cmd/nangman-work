src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/magok/'
rows=[('르웨스트 46A · 1.5룸','분양가 · 전용 13.99평',8.9853,'#5B8FB0','8억 9,853만'),
      ('르웨스트 69 · 3룸','분양가 · 전용 21.13평',13.8787,CYAN,'13억 8,787만'),
      ('마곡 아파트 59㎡','실거래 중앙값 · 33건',14.8,GREY,'14억 8,000만'),
      ('르웨스트 83A · 3룸','분양가 · 전용 25.27평',15.7541,CYAN,'15억 7,541만'),
      ('마곡 아파트 84㎡','실거래 중앙값 · 72건',16.925,GREY,'16억 9,250만')]
fig,ax=plt.subplots(figsize=(10.6,8.0)); fig.subplots_adjust(bottom=0.11,top=0.80,left=0.33,right=0.92)
n=len(rows); ys=list(range(n))[::-1]
for y,(a,b,v,c,lab) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+0.2,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.3,y+0.13,a,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-0.3,y-0.27,b,va='center',ha='right',fontsize=13,color=GREY,fontproperties=FR)
ax.set_xlim(0,21.5); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
head(fig,'지산드림 · 마곡 르웨스트 매매','방 셋 69타입이 마곡 아파트 59㎡보다 9,213만원 낮습니다')
finish(fig,O+'jisandream_magok_maemae_fig1.png','아파트는 강서구 마곡동 2014년 이후 지은 단지 · 2026년 1~8월 계약 · 르웨스트는 분양 자료',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 마곡 롯데캐슬 르웨스트',['마곡 르웨스트 매매','방 셋 13억 8,787만원'],'마곡 아파트 59㎡ 14억 8천보다 낮고 전용은 3평 넓습니다',O+'jisandream_magok_maemae_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'마곡 르웨스트 매매',font=F(52),fill=(255,226,63))
d.text((40,122),'방 셋 69타입 13억 8,787만원',font=F(33),fill=(255,255,255))
d.text((40,170),'마곡 아파트 59㎡보다 낮습니다',font=F(33),fill=(255,255,255))
b.save(O+'jisandream_magok_maemae_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='마곡 르웨스트 매매, 방 셋 오피스텔과 마곡 아파트 가격 비교'
f=F(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_magok_maemae_banner_small.png')
print('ok')
