src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
G='/tmp/claude-0/-home-claude/cbfac2e5-e5d5-531e-ad5d-28b72a0f7fcf/scratchpad/gs/img/'
O='/mnt/user-data/outputs/jisandream/sangga/'
# fig1 수익률
fig,ax=plt.subplots(figsize=(10.6,6.2)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.33,right=0.93)
vals=[('사는 가격 그대로','3억 7,500만원',6.4,CYAN),('보증금 3천을 빼면','3억 4,500만원',7.0,DEEP)]
for i,(a,b,v,c) in enumerate(vals):
    y=1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+0.12,y,'%.1f%%'%v,va='center',fontsize=22,color=DEEP,fontproperties=FB)
    ax.text(-0.2,y+0.12,a,ha='right',va='center',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-0.2,y-0.2,b,ha='right',va='center',fontsize=13,color=GREY,fontproperties=FR)
ax.text(0.15,1,'1년 월세 2,400만원',va='center',fontsize=14,color='white',fontproperties=FB)
ax.set_xlim(0,9); ax.set_ylim(-0.6,1.6); ax.set_axis_off()
head(fig,'지산드림 · 1층 상가 수익률','가산동 1층 11평, 월세 200만원은 사는 가격의 6.4%')
finish(fig,O+'jisandream_sangga_upjong_fig1.png','사는 가격은 가산동 1층 상가 최근 1년 중앙값 · 월세는 105호 조건',brand='지산드림',allow_outside=True,strict=False)
# fig3 층별
fig,ax=plt.subplots(figsize=(10.6,6.4)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.22,right=0.93)
for i,(a,v,c) in enumerate([('1층',2753,'#C9962E'),('2층',1395,DEEP),('3층 위',1133,DEEP)]):
    y=2-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+40,y,'%s만원'%format(v,','),va='center',fontsize=19,color=DEEP,fontproperties=FB)
    ax.text(-40,y,a,ha='right',va='center',fontsize=19,color=DEEP,fontproperties=FB)
ax.set_xlim(0,3600); ax.set_ylim(-0.6,2.6); ax.set_axis_off()
head(fig,'지산드림 · 1층 상가 업종','가산동 상가, 1층 평당 가격은 2층의 2배')
finish(fig,O+'jisandream_sangga_upjong_fig3.png','전용 평당 중앙값 · 국토교통부 실거래 · 최근 1년',brand='지산드림',allow_outside=True,strict=False)
# fig2 1종 2종
fig,ax=plt.subplots(figsize=(10.6,7.0)); fig.subplots_adjust(bottom=0.06,top=0.8,left=0.04,right=0.96)
ax.set_xlim(0,10); ax.set_ylim(0,6); ax.set_axis_off()
from matplotlib.patches import FancyBboxPatch
for x0,t,sub,c,items in [(0.2,'제1종 근린생활시설','동네 가게',CYAN,['커피 · 샌드위치 · 김밥','(휴게음식점 300㎡ 미만)','제과점 (300㎡ 미만)','편의점 (1,000㎡ 미만)']),
                          (5.2,'제2종 근린생활시설','술을 파는 식당까지',DEEP,['술을 파는 식당','(일반음식점)','휴게음식점 300㎡ 이상',''])]:
    ax.add_patch(FancyBboxPatch((x0,0.3),4.6,5.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc='white',ec=c,lw=3))
    ax.add_patch(FancyBboxPatch((x0,4.3),4.6,1.2,boxstyle='round,pad=0.02,rounding_size=0.15',fc=c,ec=c,lw=3))
    ax.text(x0+2.3,5.05,t,ha='center',va='center',fontsize=19,color='white',fontproperties=FB)
    ax.text(x0+2.3,4.6,sub,ha='center',va='center',fontsize=13,color='white',fontproperties=FR)
    for k,it in enumerate(items):
        if it: ax.text(x0+2.3,3.6-k*0.75,it,ha='center',va='center',fontsize=16 if not it.startswith('(') else 13,color=DEEP if not it.startswith('(') else GREY,fontproperties=FB if not it.startswith('(') else FR)
head(fig,'지산드림 · 상가 업종 확인방법','건축물대장 용도가 1종이면 커피 · 김밥 가게가 됩니다')
finish(fig,O+'jisandream_sangga_upjong_fig2.png','건축법 시행령 별표1 · 넓이는 같은 건물 같은 용도를 합친 바닥 넓이',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
p1=Image.open(G+'jisandream_firstar_photo1.png').convert('RGB').crop((212,8,754,548))
p2=Image.open(G+'jisandream_firstar_photo2.png').convert('RGB').crop((224,8,740,520))
card(p1,'1층 상가 업종 · 하우스디 가산 퍼스타','파란 원이 1층 105호, 코너 통창',O+'jisandream_sangga_upjong_photo1.png')
card(p2,'1층 상가 업종 · 건물 앞 광장','점심에 사람이 나와 앉는 광장 앞 1층',O+'jisandream_sangga_upjong_photo2.png')
f4=Image.open(G+'jisandream_firstar_fig1.png').convert('RGB').crop((0,0,966,480))
card(f4,'1층 상가 업종 · 105호 넓이','전용 11.43평 · 10평 창업 아이템에 맞는 크기',O+'jisandream_sangga_upjong_fig4.png')
thumb([p1],'지산드림 · 가산동 1층 11평','1층 상가 업종','김밥 · 샌드위치 · 커피','보증금 3천 · 월 200만원',O+'jisandream_sangga_upjong_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'1층 상가 업종',font=F2(52),fill=(255,226,63))
d.text((40,122),'가산동 1층 11평, 김밥 · 샌드위치 · 커피',font=F2(33),fill=(255,255,255))
d.text((40,170),'보증금 3천 · 월 200만원 · 바로 입주',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_sangga_upjong_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='1층 상가 업종, 가산동 1층 11평 보증금 3천 · 월 200만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_sangga_upjong_banner_small.png')
print('ok')
