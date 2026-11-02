import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/clip_ht')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40); GREEN=(120,160,110)
def save(im,n): im.save(f'h{n}.png')
def field(d,y): 
    d.rectangle((0,y,1080,y+260),fill=GREEN)
    for x in range(60,1080,140): d.polygon([(x,y+120),(x+40,y+40),(x+80,y+120)],fill=(90,130,85))
# 1
im,d=base()
caption(d,['하남 땅 사려고','알아봤는데'])
field(d,520)
person(d,540,1080,1.05,face='smile',shirt=MID)
bubble(d,80,1540,920,230,['녹지가 싸다던데','이거 살까?'],size=70,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['8월 18일부터','허가 없이는 못 삽니다'],c=WARN)
d.rounded_rectangle((70,470,1010,1130),44,fill=(255,255,255),outline=WARN,width=9)
ctext(d,520,'하남 24개 동',F(66),NAVY); ctext(d,620,'자연녹지 전체',F(80),WARN)
ctext(d,760,'2만 4,237필지',F(90),NAVY); ctext(d,890,'70.14㎢',F(70),SAND)
ctext(d,1000,'12월 31일까지',F(64),WARN)
person(d,540,1400,0.9,face='shock',shirt=MID)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['몇 ㎡부터','허가를 받나'])
for i,(a,b,c) in enumerate([('주거지역','60㎡',MID),('상업·공업','150㎡',MID),('녹지지역','200㎡',WARN),('농지 (도시 밖)','500㎡',MID)]):
    y=460+i*250
    d.rounded_rectangle((70,y,1010,y+200),40,fill=(255,255,255),outline=c,width=8)
    d.text((130,y+55),a,font=F(66),fill=NAVY)
    w=d.textlength(b,font=F(84)); d.text((950-w,y+48),b,font=F(84),fill=c)
ctext(d,1520,'200㎡ 밑으로 쪼개도 합쳐서 봅니다',F(56),WARN)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['묶이기 직전 5일','계약이 몰렸습니다'])
R=[('8월 1~12일','8건',8,MID),('8월 13~17일','44건',44,WARN),('8월 18~29일','0건',0,NAVY)]
for i,(a,b,v,c) in enumerate(R):
    y=470+i*330
    d.text((70,y),a,font=F(58),fill=NAVY)
    w=int(v/44*700)
    if w: d.rounded_rectangle((70,y+90,70+w,y+210),24,fill=c)
    d.text((90+w,y+100),b,font=F(88),fill=c)
ctext(d,1540,'하남 녹지 땅 계약 건수',F(50,False),SAND)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['그런데 44건 중','28건은 한 필지'],c=WARN)
d.rounded_rectangle((70,470,1010,1000),44,fill=(255,255,255),outline=WARN,width=9)
ctext(d,520,'항동 산3* 임야',F(70),NAVY)
ctext(d,630,'이틀에 28번',F(96),WARN)
ctext(d,780,'220㎡씩 · 전부 직거래',F(56),SAND)
ctext(d,880,'중간 금액 1,210만원',F(56),SAND)
person(d,540,1260,0.95,face='shock',shirt=MID)
bubble(d,90,1560,900,200,['44필지가 팔린 게 아니네'],size=60,fill=(255,243,196))
footer(d); save(im,5)
# 6
im,d=base()
caption(d,['2024년에도','똑같았습니다'])
ctext(d,470,'감북·감일·감이·초이동',F(56),SAND)
for i,(a,b,c) in enumerate([('묶기 전 석 달','172건',MID),('묶인 석 달','4건',WARN),('풀린 뒤 석 달','71건',MID)]):
    y=560+i*290
    d.rounded_rectangle((70,y,1010,y+240),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+34,a,F(60),NAVY); ctext(d,y+120,b,F(96),c)
ctext(d,1470,'택지 발표에서 빠지자 11월 10일 해제',F(50),NAVY)
footer(d); save(im,6)
# 7
im,d=base()
caption(d,['허가 받으면','목적대로 써야 합니다'])
for i,(a,b) in enumerate([('직접 살 집','2년'),('농사','2년'),('사업','4년')]):
    y=470+i*250
    d.rounded_rectangle((70,y,1010,y+200),40,fill=(255,255,255),outline=MID,width=8)
    d.text((130,y+55),a,font=F(66),fill=NAVY)
    w=d.textlength(b,font=F(84)); d.text((950-w,y+48),b,font=F(84),fill=MID)
ctext(d,1300,'허가 없이 계약하면',F(56),SAND)
ctext(d,1390,'효력 없음 · 땅값 30% 이하 벌금',F(62),WARN)
person(d,540,1660,0.62,face='worry',shirt=MID)
footer(d); save(im,7)
# 8
im,d=base(NAVY)
caption(d,['사려면 둘 중 하나,','허가 받거나 기다리거나'],c=(255,255,255),size=74)
ctext(d,620,'지정 직전 5일 44건',F(84),Y)
ctext(d,750,'지정 뒤 12일 0건',F(84),(255,255,255))
person(d,540,1080,0.95,face='o',shirt=MID)
ctext(d,1440,'동별 표와 2024년 비교는',F(56,False),(210,220,235))
ctext(d,1520,'블로그에 있습니다',F(56,False),(210,220,235))
ctext(d,1740,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,8)
D=[3.0,3.4,3.6,3.4,3.4,3.6,3.6,3.4]
assemble([f'h{i}.png' for i in range(1,9)],D,'nangman_hanam_toheo_short.mp4')
Image.open('h2.png').save('nangman_hanam_toheo_cover.png')
ims=[Image.open(f'h{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_h.png')
print('ok')
