import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os
Y=(240,190,40); WH=(255,255,255); GR=(200,195,185)
def footer(d,c=SAND): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),c)
def apt(d,x,y,w,h,c=(170,175,185),fl=6):
    d.rectangle((x,y,x+w,y+h),fill=c)
    for i in range(fl):
        for j in range(3): d.rectangle((x+20+j*(w-40)//3,y+20+i*(h-40)//fl,x+10+(j+1)*(w-40)//3,y+10+(i+1)*(h-40)//fl),fill=GLASS)
def stamp(d,x,y,t,c):
    d.ellipse((x-110,y-110,x+110,y+110),outline=c,width=14); ctext(d,y-58,t,F(96),c,x=x)
O='/mnt/user-data/outputs/clip_bd2'; os.makedirs(O,exist_ok=True); os.chdir(O)
def sv(im,n): im.save(f'b{n}.png')
# 1
im,d=base()
caption(d,['9월 29일','분당 재건축 2차 발표 날'],size=80)
for i,c in enumerate([MID,WARN,OK,NAVY,MID]): person(d,150+i*195,820,0.6,face='o',shirt=c)
ctext(d,1180,'두근',F(110),WARN,x=300); ctext(d,1300,'두근',F(110),WARN,x=760)
ctext(d,1560,'"우리 단지 될까?"',F(70),NAVY)
footer(d); sv(im,1)
# 2
im,d=base()
caption(d,['뽑는 건 1만 2천 가구','신청은 6만 6천 가구'],size=78)
ctext(d,520,'5.5대 1',F(220),WARN)
for i in range(11): person(d,110+i*86,1150,0.36,face='worry',shirt=[MID,WARN,OK,NAVY][i%4])
d.rounded_rectangle((380,1400,700,1520),30,fill=Y); ctext(d,1420,'합격 1명',F(64),NAVY)
ctext(d,1620,'여섯 명 중 한 명꼴',F(60),SAND)
footer(d); sv(im,2)
# 3
im,d=base()
caption(d,['발표!','선정 5곳'],c=OK,size=90)
for i,(a,b) in enumerate([('이매촌1','1,734가구'),('시범단지1','4,200가구'),('파크타운','3,025가구'),('푸른마을','2,598가구'),('한솔마을2','1,872가구')]):
    yy=440+i*230; d.rounded_rectangle((90,yy,990,yy+190),34,fill=WH,outline=OK,width=8)
    d.text((140,yy+50),a,font=F(76),fill=NAVY); w=d.textlength(b,font=F(62)); d.text((940-w,yy+62),b,font=F(62),fill=SAND)
ctext(d,1640,'합계 1만 3,429가구',F(70),OK)
footer(d); sv(im,3)
# 4
im,d=base()
caption(d,['그런데','효자촌이 없다?'],c=WARN,size=90)
apt(d,160,480,360,620)
ctext(d,1140,'서현 효자촌',F(70),NAVY,x=340)
stamp(d,780,700,'탈락',WARN)
person(d,780,1100,0.8,face='shock',shirt=MID)
bubble(d,70,1400,940,230,['우리가 제일 많이 올랐는데?','(발표 전 +53.0%, 후보 1위)'],size=58,fill=(255,243,196))
footer(d); sv(im,4)
# 5
im,d=base()
caption(d,['알고 보니','선정 5곳은 덜 오른 쪽'],size=80)
d.rectangle((200,1400-int(41.4*16),460,1400),fill=NAVY); d.rectangle((620,1400-int(45.1*16),880,1400),fill=GR)
ctext(d,1400-int(41.4*16)-100,'41.4%',F(80),NAVY,x=330); ctext(d,1400-int(45.1*16)-100,'45.1%',F(80),SAND,x=750)
ctext(d,1440,'선정',F(66),NAVY,x=330); ctext(d,1440,'탈락',F(66),SAND,x=750)
ctext(d,1600,'시장 예상 ≠ 성남시 채점',F(70),WARN)
footer(d); sv(im,5)
# 6
im,d=base()
caption(d,['더 웃긴 건','파크타운'],size=90)
apt(d,90,500,400,560,(140,160,190)); apt(d,590,500,400,560,GR)
ctext(d,1100,'대림 · 롯데',F(66),NAVY,x=290); ctext(d,1100,'서안 · 삼익',F(66),SAND,x=790)
ctext(d,1190,'선정',F(80),OK,x=290); ctext(d,1190,'탈락',F(80),WARN,x=790)
person(d,290,1470,0.6,face='smile',shirt=OK); person(d,790,1470,0.6,face='worry',shirt=MID)
ctext(d,1720,'같은 파크타운, 다른 운명',F(62),NAVY)
footer(d); sv(im,6)
# 7
im,d=base()
caption(d,['1차 때는 어땠냐면','토끼와 거북이'],size=80)
card=lambda y,a,b,c: (d.rounded_rectangle((70,y,1010,y+240),36,fill=WH,outline=c,width=8), ctext(d,y+36,a,F(66),c), ctext(d,y+136,b,F(58),SAND))
card(470,'발표 뒤 넉 달','선정 +9.9%  vs  탈락 +5.3%',NAVY)
card(760,'발표 뒤 1년 반','선정 +46.3%  vs  탈락 +47.0%',WARN)
ctext(d,1100,'탈락 단지가 따라잡음',F(76),WARN)
person(d,540,1380,0.7,face='smile',shirt=OK)
footer(d); sv(im,7)
# 8
im,d=base(NAVY)
caption(d,['탈락 단지도 끝이 아닙니다'],c=WH,size=78)
ctext(d,420,'예비 특별정비구역',F(88),Y)
ctext(d,560,'2027~2030년 약 2만 5천 가구',F(62),WH)
ctext(d,660,'2027년 7월 다시 제안',F(62),WH)
person(d,540,960,0.85,face='smile',shirt=OK)
ctext(d,1330,'선정 5곳과 탈락 후보 비교는',F(54,False),(210,220,235))
ctext(d,1410,'블로그에 있습니다',F(54,False),(210,220,235))
ctext(d,1530,'석 달 뒤 다시 세어 봅니다',F(60),Y)
footer(d,(210,220,235)); sv(im,8)
assemble([f'b{i}.png' for i in range(1,9)],[3.0,3.4,3.6,3.6,3.6,3.6,3.8,3.6],'nangman_bundang2_result_short.mp4')
Image.open('b4.png').save('nangman_bundang2_result_cover.png')
ims=[Image.open(f'b{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_bd.png')
print('ok')
