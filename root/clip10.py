import sys; sys.path.insert(0,'/home/claude'); from comic import *
import os; os.chdir('/mnt/user-data/outputs/int/clip10')
CAT=(230,150,70); SHOE=(170,125,95)
def cat(d,x,y,s=1.0):
    d.ellipse((x-int(70*s),y-int(40*s),x+int(70*s),y+int(45*s)),fill=CAT)
    d.ellipse((x+int(40*s),y-int(85*s),x+int(120*s),y-int(5*s)),fill=CAT)
    d.polygon([(x+int(48*s),y-int(65*s)),(x+int(58*s),y-int(110*s)),(x+int(80*s),y-int(78*s))],fill=CAT)
    d.polygon([(x+int(85*s),y-int(78*s)),(x+int(108*s),y-int(110*s)),(x+int(115*s),y-int(62*s))],fill=CAT)
    d.ellipse((x+int(62*s),y-int(55*s),x+int(72*s),y-int(43*s)),fill=HAIR); d.ellipse((x+int(90*s),y-int(55*s),x+int(100*s),y-int(43*s)),fill=HAIR)
    d.line((x-int(65*s),y,x-int(130*s),y-int(70*s)),fill=CAT,width=int(18*s))
def gate(d,x,y,w,h):
    d.rectangle((x,y,x+w,y+h),outline=FRAME,width=12)
    for gx in range(x+40,x+w,45): d.line((gx,y,gx,y+h),fill=FRAME,width=7)
def save(im,n): im.save(f'm{n}.png')
# 1
im,d=base((240,236,228))
caption(d,['150cm 방묘문','달았는데'])
d.rectangle((0,1400,1080,1920),fill=(215,205,190))
gate(d,480,850,300,550)
d.rectangle((150,1000,470,1400),fill=SHOE); d.rectangle((170,1020,450,1380),outline=(140,100,75),width=6)
cat(d,300,950,1.0)
person(d,880,1080,0.95,face='shock',shirt=WARN)
bubble(d,90,1560,900,200,['또 나갔어?!'],size=76,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['높이는','옆 가구가 정합니다'])
d.rectangle((600,520,700,1400),fill=(200,210,225)); ctext(d,440,'180cm',F(64),NAVY,650)
d.rectangle((300,1080,560,1400),fill=SHOE); ctext(d,1180,'신발장',F(50),(255,255,255),430); ctext(d,1250,'80cm',F(56),(255,255,255),430)
d.line((560,1080,760,1080),fill=WARN,width=6); d.line((740,520,740,1080),fill=WARN,width=8)
d.text((770,740),'100cm',font=F(80),fill=WARN)
ctext(d,1480,'고양이가 넘을 높이',F(64),NAVY); ctext(d,1580,'180 − 80 = 100cm',F(84),WARN)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['고양이는','높이보다 길을 찾습니다'])
for i,t in enumerate(['뛰어넘고','간살 타고 오르고','틈에 머리 넣고','손잡이 누르고','옆 가구 밟고']):
    y=420+i*235
    d.rounded_rectangle((110,y,970,y+190),36,fill=(255,255,255),outline=WARN if i==4 else NAVY,width=7)
    ctext(d,y+50,t,F(76),WARN if i==4 else NAVY)
ctext(d,1640,'하나만 남아도 나갑니다',F(66),WARN)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['현관은','중문으로 막을 수 있어요'])
person(d,860,560,0.85,face='smile',shirt=NAVY,helmet=True)
door(d,150,820,620,760,panels=3)
d.rectangle((130,760,790,800),fill=OK); ctext(d,690,'위까지 막아 시공',F(52),OK,460)
bubble(d,90,1640,900,160,['상부까지 막아 넘을 틈을 줄입니다'],size=52)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['방묘 중문','네 군데는 꼭'])
for i,(a,b) in enumerate([('간살 사이','머리가 들어가나'),('문 아래','발이 들어가나'),('손잡이·잠금','앞발로 열리나'),('상부','위가 열려 있나')]):
    y=430+i*320
    d.rounded_rectangle((80,y,1000,y+270),40,fill=(255,255,255),outline=NAVY,width=8)
    ctext(d,y+40,a,F(84),NAVY); ctext(d,y+160,b,F(60,False),WARN)
footer(d); save(im,5)
# 6
im,d=base(NAVY)
caption(d,['몇 cm보다','빠져나갈 틈이','남았는지'],c=(255,255,255),size=92)
cat(d,540,1080,1.6)
ctext(d,1400,'현관 사진을 보내 주시면',F(60),(240,190,40))
ctext(d,1490,'방묘 되는 구조부터 봐 드립니다',F(60),(240,190,40))
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235))
save(im,6)
