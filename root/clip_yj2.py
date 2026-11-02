import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/clip_yj2')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40)
def save(im,n): im.save(f'q{n}.png')
def train(d,x,y,w):
    d.rounded_rectangle((x,y,x+w,y+170),50,fill=MID); d.rectangle((x+w-120,y,x+w,y+170),fill=MID)
    for k in range(4): d.rounded_rectangle((x+40+k*(w-80)//4,y+30,x+20+(k+1)*(w-80)//4,y+100),14,fill=GLASS)
    d.line((x-40,y+190,x+w+40,y+190),fill=FRAME,width=10)
# 1
im,d=base()
caption(d,['GTX-C 오는 덕정동,','많이 올랐겠지?'])
train(d,160,520,760); ctext(d,740,'GTX-C 덕정역',F(64),NAVY)
person(d,540,1050,1.05,face='smile',shirt=MID)
bubble(d,90,1520,900,220,['역 생기면 오르잖아!'],size=74,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['그런데 덕정동은','2021년보다'])
ctext(d,560,'−28.9%',F(220),WARN)
ctext(d,900,'2021년 가격의 71.1%',F(70),NAVY)
ctext(d,1010,'양주 10개 동네 중 꼴찌',F(66),WARN)
person(d,540,1300,0.9,face='shock',shirt=MID)
ctext(d,1690,'같은 단지 같은 평형 비교',F(46,False),SAND)
footer(d); save(im,2)
# 3 ranking
im,d=base()
caption(d,['고점을 넘긴 곳은','외곽 구축'])
R=[('광적면',112.8,OK),('장흥면',105.4,OK),('백석읍',103.0,OK),('옥정동',75.9,MID),('고암동',74.0,MID),('덕정동',71.1,WARN)]
for i,(n,v,c) in enumerate(R):
    y=450+i*190; w=int((v-50)/65*460)
    d.text((70,y+18),n,font=F(62),fill=NAVY)
    d.rounded_rectangle((330,y+10,330+w,y+120),20,fill=c)
    d.text((345+w,y+18),f'{v}%',font=F(62),fill=c)
    if i==2: ctext(d,y+140,'⋯',F(50),SAND)
ctext(d,1640,'100% = 2021년 가격',F(50,False),SAND)
footer(d); save(im,3)
# 4 half
im,d=base()
caption(d,['덕정동에선','반값이 된 집도'])
for i,(n,a,b,c) in enumerate([('한국아파트 54㎡','2.00억','1.05억',WARN),('양주서희스타힐스2단지 85㎡','5.25억','3.27억',WARN)]):
    y=470+i*620
    d.rounded_rectangle((70,y,1010,y+540),44,fill=(255,255,255),outline=c,width=9)
    ctext(d,y+50,n,F(60),NAVY); ctext(d,y+180,'2021년 → 최근',F(52,False),SAND)
    ctext(d,y+280,f'{a} → {b}',F(110),c)
footer(d); save(im,4)
# 5 rails
im,d=base()
caption(d,['철도 넷은','전부 착공했습니다'])
for i,(n,t,c) in enumerate([('GTX-C 덕정역','2031년 9월',WARN),('7호선 도봉산~옥정','2029년 말',MID),('7호선 옥정~포천','2031년',MID),('1호선 회천중앙역','2030년',MID)]):
    y=450+i*300
    d.rounded_rectangle((70,y,1010,y+250),40,fill=(255,255,255),outline=c,width=7)
    d.text((120,y+40),n,font=F(64),fill=NAVY); d.text((120,y+140),'개통 목표 '+t,font=F(58),fill=c)
footer(d); save(im,5)
# 6 delay
im,d=base()
caption(d,['개통은','계속 밀렸습니다'])
for i,(n,a,b) in enumerate([('7호선 도봉산~옥정','2025년','2029년 말'),('회천중앙역','2024년','2030년'),('GTX-C','964일 멈춤','2026.9 본공사')]):
    y=470+i*380
    d.rounded_rectangle((70,y,1010,y+320),40,fill=(255,255,255),outline=NAVY,width=7)
    ctext(d,y+40,n,F(66),NAVY); ctext(d,y+170,f'{a} → {b}',F(66),WARN)
ctext(d,1640,'착공에서 개통까지 4~5년',F(64),NAVY)
footer(d); save(im,6)
# 7
im,d=base(NAVY)
caption(d,['호재가 서는 동네가','가장 덜 회복했습니다'],c=(255,255,255),size=84)
ctext(d,560,'덕정동 71.1%',F(92),Y); ctext(d,690,'광적면 112.8%',F(92),(255,255,255))
person(d,540,1000,0.95,face='o',shirt=MID)
ctext(d,1380,'10개 동네 전체 표와',F(56,False),(210,220,235)); ctext(d,1460,'양주 땅값은 블로그에',F(56,False),(210,220,235))
ctext(d,1720,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,7)
D=[3.0,3.2,3.4,3.2,3.2,3.2,3.0]
assemble([f'q{i}.png' for i in range(1,8)],D,'nangman_yangju_gtx_short.mp4')
Image.open('q2.png').save('nangman_yangju_gtx_cover.png')
ims=[Image.open(f'q{i}.png').resize((270,480)) for i in range(1,8)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_q.png')
