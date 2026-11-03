src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/budget/'
GRN='#2E7D50'; GRY='#8A8F96'; GOLDc='#C9962E'
rows=[('갈매동 휴밸나인 원룸','월세 65만~70만원 · 연 8%',1.05,CYAN),('별내자이 더 스타 59타입','전세 끼고 · 취득세 포함',1.87,'#5B8FB0'),('가평 삼회리 땅','2,962평 · 집 지을 땅',2.4,GRN),('가평 이곡리 땅','6,390평 · 6m 임도',2.55,GRN),('송산그린시티 단독주택 땅','94평 · 평당 477만원',4.5,GOLDc),('가산어반워크2 513호','지식산업센터 44.69평',5.05,DEEP),('영등포 자이타워 F-614','지식산업센터 전용 27.24평',10.856,DEEP)]
fig,ax=plt.subplots(figsize=(10.6,8.4)); fig.subplots_adjust(bottom=0.10,top=0.80,left=0.35,right=0.92)
n=len(rows); ys=list(range(n))[::-1]; xmax=12.5
for y,(a,b,v,c) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    lab=('%.2f'%v).rstrip('0').rstrip('.') if v<10 else '10.86'
    lab={1.05:'1억 500만',1.87:'1억 8,700만',2.4:'2억 4천',2.55:'2억 5,500만',4.5:'4억 5천',5.05:'5억 500만',10.856:'10억 8,560만'}[v]
    ax.text(v+0.15,y,lab,va='center',fontsize=18,color=DEEP,fontproperties=FB)
    ax.text(-0.25,y+0.13,a,va='center',ha='right',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-0.25,y-0.27,b,va='center',ha='right',fontsize=12.5,color=GREY,fontproperties=FR)
ax.set_xlim(0,xmax); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
head(fig,'지산드림 · 1억 투자 부동산, 예산별 매물','1억 500만원 원룸부터 10억대 지식산업센터까지')
finish(fig,O+'jisandream_budget_invest_fig1.png','금액은 각 매물 글 본문 그대로 · 별내 59타입은 분양가에서 전세 중앙값을 빼고 취득세를 더한 돈',brand='지산드림',allow_outside=True,strict=False)
render_jisan('지산드림 · 1억 투자 부동산',['1억 투자 부동산','1억 500만원 원룸 연 8%'],'예산별 매물 여섯 개 · 원룸 · 오피스텔 · 땅 · 지식산업센터',O+'jisandream_budget_invest_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'1억 투자 부동산',font=F(52),fill=(255,226,63))
d.text((40,122),'1억 500만원 원룸은 월세 70만원',font=F(33),fill=(255,255,255))
d.text((40,170),'예산별 매물 여섯 개를 골랐습니다',font=F(33),fill=(255,255,255))
b.save(O+'jisandream_budget_invest_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='1억 투자 부동산, 1억 500만원 원룸부터 예산별 매물 여섯 개'
f=F(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_budget_invest_banner_small.png')
print('ok')
