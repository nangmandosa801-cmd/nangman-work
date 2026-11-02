import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/clip_uj')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40)
def save(im,n): im.save(f'u{n}.png')
def train(d,x,y,w):
    d.rounded_rectangle((x,y,x+w,y+170),50,fill=MID); d.rectangle((x+w-120,y,x+w,y+170),fill=MID)
    for k in range(4): d.rounded_rectangle((x+40+k*(w-80)//4,y+30,x+20+(k+1)*(w-80)//4,y+100),14,fill=GLASS)
    d.line((x-40,y+190,x+w+40,y+190),fill=FRAME,width=10)
# 1
im,d=base()
caption(d,['GTX-A 열렸다!','운정에서 서울역 22분'])
train(d,160,560,760); ctext(d,780,'운정중앙역 · 2024.12.28',F(56),NAVY)
person(d,540,1080,1.05,face='smile',shirt=MID)
bubble(d,80,1540,920,230,['이제 우리 집','오르는 일만 남았다'],size=68,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['석 달 만에','361만 명이 탔습니다'])
ctext(d,560,'361만 명',F(180),MID)
ctext(d,830,'예측 이용객의 91.1%',F(68),NAVY)
person(d,540,1180,1.0,face='smile',shirt=OK)
bubble(d,150,1560,780,200,['사람이 이렇게 많은데'],size=64,fill=(255,243,196))
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['그래서','아파트값은요?'])
ctext(d,620,'−5.3%',F(260),WARN)
ctext(d,980,'개통 전보다',F(80),NAVY)
person(d,540,1300,1.0,face='shock',shirt=MID)
ctext(d,1700,'51개 단지 152개 면적 · 같은 단지 같은 평형',F(44,False),SAND)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['기다리면 오르겠지,','했는데'])
R=[('개통 직후','−0.6%'),('반년 뒤','−1.5%'),('1년 뒤','−3.8%'),('1년 반 뒤','−5.3%')]
for i,(a,b) in enumerate(R):
    y=460+i*250
    c=WARN if i==3 else MID
    d.rounded_rectangle((70,y,1010,y+200),40,fill=(255,255,255),outline=c,width=8)
    d.text((130,y+55),a,font=F(70),fill=NAVY)
    w=d.textlength(b,font=F(90)); d.text((950-w,y+45),b,font=F(90),fill=c)
ctext(d,1540,'내려가기만 했습니다',F(72),WARN)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['그럼 역 앞은','괜찮겠지?'])
R=[('역에서 1km 안','−3.6%',MID),('1~2km','−7.0%',WARN),('2km 밖','−4.5%',MID)]
for i,(a,b,c) in enumerate(R):
    y=480+i*300
    d.rounded_rectangle((70,y,1010,y+250),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+40,a,F(66),NAVY); ctext(d,y+130,b,F(100),c)
ctext(d,1480,'중간이 제일 많이 깎였습니다',F(70),WARN)
ctext(d,1600,'가까울수록 덜 내리지 않았습니다',F(56,False),SAND)
footer(d); save(im,5)
# 6
im,d=base()
caption(d,['버틴 집도','있습니다'])
d.rounded_rectangle((70,480,1010,1060),44,fill=(255,255,255),outline=OK,width=9)
ctext(d,530,'운정신도시 아이파크 85㎡',F(62),NAVY)
ctext(d,640,'역에서 0.5km',F(52,False),SAND)
ctext(d,740,'7.24억 → 7.26억',F(96),OK)
ctext(d,900,'1년 반 동안 200만원',F(60),NAVY)
person(d,540,1300,0.95,face='o',shirt=OK)
bubble(d,120,1560,840,210,['이게 선방입니다'],size=70,fill=(255,243,196))
footer(d); save(im,6)
# 7
im,d=base()
caption(d,['2019년 이전 단지는','더 깊습니다'])
ctext(d,580,'−25.2%',F(230),WARN)
ctext(d,900,'2021년 하반기 대비',F(70),NAVY)
ctext(d,1030,'GTX가 와도 고점은 멀었습니다',F(58,False),SAND)
person(d,540,1300,0.95,face='worry',shirt=MID)
footer(d); save(im,7)
# 8
im,d=base(NAVY)
caption(d,['사람은 91.1%까지 왔는데','가격은 안 따라왔습니다'],c=(255,255,255),size=76)
ctext(d,620,'이용객 91.1%',F(96),Y)
ctext(d,760,'아파트값 −5.3%',F(96),(255,255,255))
person(d,540,1080,0.95,face='o',shirt=MID)
ctext(d,1440,'거리별 표와 단지별 사례는',F(56,False),(210,220,235))
ctext(d,1520,'블로그에 있습니다',F(56,False),(210,220,235))
ctext(d,1740,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,8)
D=[3.0,3.0,3.2,3.6,3.6,3.4,3.0,3.4]
assemble([f'u{i}.png' for i in range(1,9)],D,'nangman_unjeong_gtxa_short.mp4')
Image.open('u3.png').save('nangman_unjeong_gtxa_cover.png')
ims=[Image.open(f'u{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_u.png')
print('ok')
