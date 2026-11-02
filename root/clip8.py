import sys; sys.path.insert(0,'/home/claude'); from comic import *
import os; os.chdir('/mnt/user-data/outputs/int/clip8')
ICE=(120,170,210)
def window(d,x,y,w,h):
    d.rectangle((x,y,x+w,y+h),fill=(235,235,238),outline=FRAME,width=14)
    d.line((x+w//2,y,x+w//2,y+h),fill=FRAME,width=14)
    d.rectangle((x+20,y+20,x+w//2-14,y+h-20),fill=GLASS); d.rectangle((x+w//2+14,y+20,x+w-20,y+h-20),fill=GLASS)
def snow(d,x,y,r=22):
    for a in (0,60,120): 
        import math; d.line((x-r*math.cos(math.radians(a)),y-r*math.sin(math.radians(a)),x+r*math.cos(math.radians(a)),y+r*math.sin(math.radians(a))),fill=(255,255,255),width=6)
def save(im,n): im.save(f'w{n}.png')
# 1
im,d=base((225,235,245))
caption(d,['창가에만 앉으면','으슬으슬'])
window(d,160,420,760,720)
for x,y in [(300,560),(500,700),(720,560),(640,900),(380,860)]: snow(d,x,y)
d.rounded_rectangle((180,1330,900,1460),40,fill=(160,120,100))
person(d,540,1180,1.05,face='worry',shirt=WARN)
for k in range(3): d.arc((380-k*30,1150-k*20,420-k*30,1230-k*20),100,260,fill=ICE,width=6); d.arc((660+k*30,1150-k*20,700+k*30,1230-k*20),280,80,fill=ICE,width=6)
bubble(d,120,1540,840,200,['필름 한 장 붙일까?'],size=60,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['잠깐, 바람인가요','냉기인가요?'])
person(d,850,640,0.9,face='smile',shirt=NAVY,helmet=True)
for i,(a,b,c) in enumerate([('닫아도 바람이 든다','샷시 틈 · 모헤어',WARN),('바람은 없는데 서늘','단열필름',OK)]):
    y=980+i*400
    d.rounded_rectangle((80,y,1000,y+330),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+50,a,F(64),NAVY); ctext(d,y+170,'→ '+b,F(70),c)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['이름 말고','숫자 세 개'])
rows=[('열관류율','낮을수록 겨울에 따뜻',NAVY),('태양열 취득률','낮을수록 여름에 덜 더움',WARN),('가시광선 투과율','높을수록 방이 밝음',OK)]
for i,(a,b,c) in enumerate(rows):
    y=520+i*400
    d.rounded_rectangle((80,y,1000,y+320),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+55,a,F(80),c); ctext(d,y+185,b,F(58,False),NAVY)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['붙이기 전에','우리 집 유리부터'])
d.rectangle((190,450,890,1150),fill=FRAME)
d.rectangle((230,490,850,1110),fill=(250,200,150))
d.rectangle((330,590,750,1010),fill=(245,150,110))
ctext(d,760,'가운데 뜨거움',F(58),(255,255,255),540)
ctext(d,1160,'테두리는 차가움',F(52),FRAME,540)
d.line([(232,700),(275,730),(255,770),(300,810)],fill=(30,30,30),width=7); d.text((90,690),'금',font=F(56),fill=WARN); d.line((155,730,225,730),fill=WARN,width=5)
bubble(d,90,1290,900,380,['복층 · 로이 · 색유리','큰 남향 · 서향 창','→ 붙여도 되는지 확인'],size=58,fill=(251,239,234),c=WARN)
footer(d); save(im,5)
# 5
im,d=base()
caption(d,['한 겨울만','버틸 거라면'])
window(d,160,450,760,700)
for gx in range(200,880,50):
    for gy in range(490,1120,50): d.ellipse((gx,gy,gx+34,gy+34),outline=(170,190,205),width=4)
ctext(d,1230,'뽁뽁이도 괜찮습니다',F(78),OK)
ctext(d,1360,'싸고 떼기 쉽고',F(58,False),NAVY); ctext(d,1450,'대신 바깥이 뿌옇게',F(58,False),NAVY)
footer(d); save(im,6)
# 6 end
im,d=base(NAVY)
caption(d,['좋은 필름보다','우리 집 유리에','맞는 필름'],c=(255,255,255))
for i,t in enumerate(['① 창이 몇 개인지','② 한 장 유리 · 복층유리','③ 로이 · 색유리인지']):
    y=780+i*250
    d.rounded_rectangle((110,y,970,y+200),36,fill=(255,255,255))
    d.text((170,y+55),t,font=F(68),fill=NAVY)
ctext(d,1560,'알려 주시면 맞는 조합을 봐 드립니다',F(52),(240,190,40))
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235))
save(im,7)
