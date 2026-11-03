src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from matplotlib.patches import FancyBboxPatch
O='/mnt/user-data/outputs/jisandream/sangim/'
GOLD='#C9962E'
# fig1
fig,ax=plt.subplots(figsize=(10.6,6.6)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
rows=[('서울 기준',9.0,GREY,'9억원'),('가산 1층 11평',2.3,GOLD,'2억 3,000만원'),('과밀억제권역 기준',6.9,GREY,'6억 9천만원'),('갈매 1층 38평',2.8,CYAN,'2억 8,000만원')]
for i,(a,v,c,lab) in enumerate(rows):
    y=len(rows)-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+0.12,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.12,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.set_xlim(0,11.5); ax.set_ylim(-0.6,len(rows)-0.4); ax.set_axis_off()
head(fig,'지산드림 · 상가임대차보호법','환산보증금 = 보증금 + 월세 × 100, 두 매물 모두 기준 안')
finish(fig,O+'jisandream_sangim_fig1.png','상가건물 임대차보호법 시행령 제2조 · 매물 조건은 지산드림 매물 글',brand='지산드림',allow_outside=True,strict=False)
# fig2 timeline
fig,ax=plt.subplots(figsize=(10.6,5.6)); fig.subplots_adjust(bottom=0.08,top=0.78,left=0.04,right=0.96)
ax.set_xlim(0,10.6); ax.set_ylim(0,4); ax.set_axis_off()
ax.plot([0.5,10.1],[2,2],color=GREY,lw=4)
for x,t,c in [(0.5,'처음 계약',DEEP),(2.4,'2년',DEEP),(4.3,'4년',DEEP),(6.2,'6년',DEEP),(8.1,'8년',DEEP),(10.1,'10년',GOLD)]:
    ax.plot(x,2,'o',ms=16,color=c); ax.text(x,1.3,t,ha='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.add_patch(FancyBboxPatch((1.55,2.5),1.0,0.8,boxstyle='round,pad=0.02',fc=CYAN,ec=CYAN))
ax.text(2.05,2.9,'갱신 요구',ha='center',va='center',fontsize=13,color='white',fontproperties=FB)
ax.text(2.05,3.6,'2년이 끝나기 6~1개월 전',ha='center',fontsize=13,color=DEEP,fontproperties=FR)
head(fig,'지산드림 · 상가임대차보호법 10년','요구만 하면 처음 계약일부터 10년까지')
finish(fig,O+'jisandream_sangim_fig2.png','상가건물 임대차보호법 제10조 · 월세 3번 밀림 등 법에 적힌 경우는 거절 가능',brand='지산드림',allow_outside=True,strict=False)
# fig3
fig,ax=plt.subplots(figsize=(10.6,6.0)); fig.subplots_adjust(bottom=0.12,top=0.76,left=0.30,right=0.93)
rows=[('가산 지금',200,GREY,'200만원'),('가산 최대',210,GOLD,'210만원 (+5%)'),('갈매 지금',250,GREY,'250만원'),('갈매 최대',262.5,CYAN,'262만 5천원 (+5%)')]
for i,(a,v,c,lab) in enumerate(rows):
    y=len(rows)-1-i; ax.barh(y,v,color=c,height=0.55); ax.text(v+3,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-3,y,a,ha='right',va='center',fontsize=16,color=DEEP,fontproperties=FB)
ax.set_xlim(0,360); ax.set_ylim(-0.6,len(rows)-0.4); ax.set_axis_off()
head(fig,'지산드림 · 상가임대차보호법 5%','갱신 때 월세는 5%까지만 오릅니다')
finish(fig,O+'jisandream_sangim_fig3.png','환산보증금 기준 안 · 올린 뒤 1년 안에는 다시 못 올림',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
G='/tmp/claude-0/-home-claude/cbfac2e5-e5d5-531e-ad5d-28b72a0f7fcf/scratchpad/gs/img/'
p1=Image.open(G+'jisandream_firstar_photo1.png').convert('RGB').crop((212,8,754,548))
C='/mnt/user-data/outputs/jisandream/cafe/'
import glob
cp=sorted(glob.glob(C+'*photo1*.png'))[0]
p2=Image.open(cp).convert('RGB'); p2=p2.crop((40,160,p2.width-40,p2.height-70))
card(p1,'상가임대차보호법 · 가산 1층 11평','보증금 3천 · 월 200만원 · 환산 2억 3천',O+'jisandream_sangim_photo1.png')
card(p2,'상가임대차보호법 · 갈매 1층 38평','보증금 3천 · 월 250만원 · 권리금 없음',O+'jisandream_sangim_photo2.png')
thumb([p1,p2],'지산드림 · 가산 · 갈매 1층 상가','상가임대차보호법','10년 · 5% 다 받습니다','환산보증금 2억 3천 · 2억 8천',O+'jisandream_sangim_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'상가임대차보호법',font=F2(52),fill=(255,226,63))
d.text((40,122),'가산 11평 · 갈매 38평 권리금 없음',font=F2(33),fill=(255,255,255))
d.text((40,170),'계약서 갱신 · 원상복구 같이 봅니다',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_sangim_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='상가임대차보호법, 가산 월 200만원 · 갈매 월 250만원 모두 10년 · 5%'
f=F2(19); tw=d.textlength(t,font=f); d.text(((773-tw)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_sangim_banner_small.png')
print('ok',cp)
