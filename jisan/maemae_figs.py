src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/maemae/'
GOLD='#C9962E'; RED='#B5503C'
def hbar(rows,xmax,title,sub,note,out,left=0.26,h=6.4):
    fig,ax=plt.subplots(figsize=(10.6,h)); fig.subplots_adjust(bottom=0.12,top=0.78,left=left,right=0.93); n=len(rows)
    for i,(a,v,c,lab) in enumerate(rows):
        y=n-1-i; ax.barh(y,v,color=c,height=0.6); ax.text(v+xmax*0.012,y,lab,va='center',fontsize=17,color=DEEP,fontproperties=FB)
        ax.text(-xmax*0.012,y,a,ha='right',va='center',fontsize=15.5,color=DEEP,fontproperties=FB)
    ax.set_xlim(0,xmax); ax.set_ylim(-0.6,n-0.4); ax.set_axis_off(); head(fig,title,sub); finish(fig,out,note,brand='지산드림',allow_outside=True,strict=False)
D=[('창우동',318),('감북동',316),('초일동',270),('미사동',241),('초이동',230),('상산곡동',195),('하산곡동',195),('춘궁동',171)]
hbar([(a,v,GOLD if v>300 else (GREY if v<200 else CYAN),f'{v}만원') for a,v in D],420,'지산드림 · 하남 토지 매매','동네별 그린벨트 밭 · 논 평당 중앙값','국토교통부 토지 실거래 · 2024.1~2026.8 · 통째 거래 · 100~1,000평',O+'jisandream_hanam_maemae_fig1.png',h=7.4)
hbar([('도로에 붙은 땅',281,GOLD,'281만원 (74필지)'),('길이 없는 땅',161,GREY,'161만원 (56필지)')],400,'지산드림 · 하남 땅값','그린벨트 밭 · 논, 길이 붙으면 1.7배','국토교통부 토지 실거래 · 2024.1~2026.8 · 실거래 신고 도로 조건 기준',O+'jisandream_hanam_maemae_fig2.png',h=5.0)
fig,ax=plt.subplots(figsize=(10.6,6.0)); fig.subplots_adjust(bottom=0.14,top=0.78,left=0.08,right=0.95)
Y=list(range(2010,2027)); V=[100,120,116,105,120,130,150,166,159,184,200,231,270,242,289,240,185]
ax.plot(Y,V,color=DEEP,lw=3.5,marker='o',ms=7)
for y,v in [(2010,100),(2015,130),(2020,200),(2024,289),(2026,185)]: ax.text(y,v+14,f'{v}만',ha='center',fontsize=15,color=RED if y==2024 else DEEP,fontproperties=FB)
ax.set_ylim(60,340); ax.set_xticks([2010,2014,2018,2022,2026]); ax.set_xticklabels(['2010','2014','2018','2022','2026'],fontproperties=FB,fontsize=14)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.set_yticks([])
head(fig,'지산드림 · 하남 그린벨트 땅값','밭 · 논 평당 중앙값, 2010~2026년')
finish(fig,O+'jisandream_hanam_maemae_fig3.png','국토교통부 토지 실거래 · 통째 · 100~1,000평 · 2026년은 1~8월',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
m=Image.open('/mnt/user-data/outputs/jisandream/taekji/jisandream_hanam_taekji_map1.png').convert('RGB'); m=m.crop((40,170,m.width-40,m.height-90))
thumb([m],'지산드림 · 하남 땅','하남 토지 매매','평당 171만~318만원','그린벨트 밭 · 동네별 · 길 붙으면 1.7배',O+'jisandream_hanam_maemae_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'하남 토지 매매',font=F2(52),fill=(255,226,63))
d.text((40,122),'지번 주시면 내 땅 위치부터',font=F2(33),fill=(255,255,255))
d.text((40,170),'땅 파실 분 · 사실 분 모두 연락 주세요',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_hanam_maemae_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='하남 토지 매매, 그린벨트 밭 동네별 평당 171만~318만원'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_hanam_maemae_banner_small.png')
print('ok')
