src=open('/home/claude/jisan/gpimfigs.py').read()
exec(src.split('# fig1 크기별')[0])
from PIL import Image,ImageDraw,ImageFont
O='/mnt/user-data/outputs/jisandream/xi/'
RED='#B5654E'
rows=[('당산동1가','2022년 준공',3942,GREY),('자이타워 F-614','분양금 그대로 · 2026년 준공',3874,RED),('영등포 신축','39건 중앙값',3787,GREY),('영등포동6가','2023년 준공',3601,GREY),('자이타워 10% 낮추면','가정',3487,'#D9A08C'),('양평동5가','2020년 준공',3250,GREY),('자이타워 20% 낮추면','가정',3099,'#D9A08C')]
fig,ax=plt.subplots(figsize=(10.6,8.8)); fig.subplots_adjust(bottom=0.10,top=0.81,left=0.31,right=0.93)
n=len(rows); ys=list(range(n))[::-1]
for y,(a,b,v,c) in zip(ys,rows):
    ax.barh(y,v,color=c,height=0.6)
    ax.text(v+40,y,'%s만원'%format(v,','),va='center',fontsize=17,color=DEEP,fontproperties=FB)
    ax.text(-40,y+0.13,a,va='center',ha='right',fontsize=16,color=DEEP,fontproperties=FB)
    ax.text(-40,y-0.27,b,va='center',ha='right',fontsize=12,color=GREY,fontproperties=FR)
ax.set_xlim(0,4800); ax.set_ylim(-0.7,n-0.3); ax.set_axis_off()
head(fig,'지산드림 · 영등포 자이타워','분양금 그대로면 영등포 신축 실거래와 거의 같습니다')
finish(fig,O+'jisandream_xi_tower_fig1.png','국토교통부 실거래 · 영등포 지식산업센터 전용 70~110㎡ · 2024~2026년 · 10 · 20%는 가정',brand='지산드림',allow_outside=True,strict=False)
exec(open('/home/claude/jisan/photo/kwphoto.py').read())
S='/tmp/claude-0/-home-claude/cbfac2e5-e5d5-531e-ad5d-28b72a0f7fcf/scratchpad/xi/'
ph={k:Image.open(S+f'x{k}.png').convert('RGB').crop((0,0,966,540)) for k in (3,4,5,6)}
cards=[(3,'영등포 자이타워 매매 · F-614','전용 27.24평, 천장 마감 · 시스템 에어컨 완료'),
       (4,'영등포 사무실 매매 · 코너 호실','두 면이 창이라 안쪽까지 밝습니다'),
       (5,'영등포 사무실 · 실내','기둥을 벽 쪽으로 붙여 가운데가 트입니다'),
       (6,'영등포 자이타워 · 6층','앞이 트인 창밖 전망')]
for i,(k,a,b) in enumerate(cards,1): card(ph[k],a,b,O+f'jisandream_xi_tower_photo{i}.png')
thumb([ph[4]],'지산드림 · 영등포 양평 자이타워 F-614','영등포 자이타워','주차 177% · 전용 27평','2026년 3월 준공 · 코너 호실 · 바로 입주',O+'jisandream_xi_tower_thumb.png')
FBp='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def F2(s): return ImageFont.truetype(FBp,s,index=1)
H='/mnt/user-data/outputs/jisandream/hwesonji/'
b=Image.open(H+'jisandream_hwesonji_banner.png').convert('RGB'); d=ImageDraw.Draw(b)
d.rectangle((0,0,773,227),fill=(44,79,83))
d.text((40,38),'영등포 자이타워',font=F2(52),fill=(255,226,63))
d.text((40,122),'F-614 전용 27평 코너 · 바로 입주',font=F2(33),fill=(255,255,255))
d.text((40,170),'주차 177% · 냉난방기 · 도시가스',font=F2(33),fill=(255,255,255))
b.save(O+'jisandream_xi_tower_banner.png')
s=Image.open(H+'jisandream_hwesonji_banner_small.png').convert('RGB')
strip=s.crop((0,92,773,98)).resize((773,46)); s.paste(strip,(0,94)); d=ImageDraw.Draw(s)
t='영등포 자이타워 매매, 영등포 사무실 F-614 전용 27평 코너'
f=F2(19); w=d.textlength(t,font=f); d.text(((773-w)/2,105),t,font=f,fill=(170,190,192))
s.save(O+'jisandream_xi_tower_banner_small.png')
print('ok')
