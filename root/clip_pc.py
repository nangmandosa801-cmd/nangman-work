import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/clip_pc')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40)
def save(im,n): im.save(f'p{n}.png')
# 1
im,d=base()
caption(d,['우리 단지','선도지구 됐대!'])
person(d,330,900,1.0,face='smile',shirt=MID)
person(d,760,900,1.0,face='o',shirt=OK)
bubble(d,60,1300,460,230,['우린 됐어!'],size=64,fill=(255,243,196))
bubble(d,560,1300,460,230,['난 2차 신청…'],size=60,fill=(255,255,255))
ctext(d,1640,'평촌 선도지구 세 곳 5,460가구',F(56),NAVY)
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['발표 전보다','얼마나 올랐나'])
R=[('선도지구','+36.5%',WARN),('나머지 구축','+31.5%',MID),('2차 신청 단지','+26.8%',MID)]
for i,(a,b,c) in enumerate(R):
    y=470+i*290
    d.rounded_rectangle((70,y,1010,y+240),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+34,a,F(66),NAVY); ctext(d,y+124,b,F(96),c)
ctext(d,1400,'2024년 1~10월 대비',F(52,False),SAND)
person(d,540,1580,0.75,face='smile',shirt=OK)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['어? 우리도','많이 올랐는데?'])
person(d,540,620,1.0,face='smile',shirt=OK)
bubble(d,70,1080,940,260,['26.8%면 우리도','잘 나온 거 아냐?'],size=68,fill=(255,243,196))
ctext(d,1480,'출발점을 2021년으로 옮기면',F(66),NAVY)
ctext(d,1580,'이야기가 달라집니다',F(66),WARN)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['2021년 하반기와','비교하면'])
R=[('선도지구','+16.3%',OK),('나머지 구축','+4.5%',MID),('2차 신청 단지','−0.3%',WARN),('새 아파트','−0.3%',WARN)]
for i,(a,b,c) in enumerate(R):
    y=440+i*270
    d.rounded_rectangle((70,y,1010,y+225),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+28,a,F(62),NAVY); ctext(d,y+112,b,F(92),c)
ctext(d,1570,'2차 신청 단지는 5년 전 가격입니다',F(62),WARN)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['5년 걸려','제자리'])
person(d,540,620,1.05,face='shock',shirt=OK)
bubble(d,60,1100,960,300,['그동안 오른 줄','알았는데요'],size=72,fill=(255,243,196))
ctext(d,1540,'−0.3%',F(150),WARN)
footer(d); save(im,5)
# 6
im,d=base()
caption(d,['2차는','자리가 모자랍니다'])
d.rounded_rectangle((70,470,1010,820),44,fill=(255,255,255),outline=NAVY,width=9)
ctext(d,520,'신청',F(56,False),SAND); ctext(d,600,'6개 구역 1만 4,102가구',F(78),NAVY)
d.rounded_rectangle((70,890,1010,1240),44,fill=(255,255,255),outline=WARN,width=9)
ctext(d,940,'올해 지정 가능',F(56,False),SAND); ctext(d,1020,'4,866가구',F(90),WARN)
ctext(d,1360,'신청의 3분의 1만 됩니다',F(70),WARN)
person(d,540,1580,0.7,face='worry',shirt=MID)
footer(d); save(im,6)
# 7
im,d=base()
caption(d,['지정되면','이렇게 됩니다'])
for i,(n,a,b) in enumerate([('귀인블록','1,750가구','2,875가구'),('민백블록','1,376가구','2,395가구'),('샘마을','2,334가구','4,127가구')]):
    y=470+i*340
    d.rounded_rectangle((70,y,1010,y+280),40,fill=(255,255,255),outline=MID,width=8)
    ctext(d,y+30,n,F(64),NAVY)
    ctext(d,y+130,f'{a} → {b}',F(72),MID)
ctext(d,1580,'최고 49층 · 2033년 입주 목표',F(58),NAVY)
footer(d); save(im,7)
# 8
im,d=base(NAVY)
caption(d,['평촌은 다 올랐는데','한 단지만 더 갔습니다'],c=(255,255,255),size=76)
ctext(d,620,'선도지구 +16.3%',F(92),Y)
ctext(d,760,'2차 신청 −0.3%',F(92),(255,255,255))
person(d,330,1060,0.9,face='smile',shirt=MID)
person(d,760,1060,0.9,face='worry',shirt=OK)
ctext(d,1440,'단지별 표와 2차 여섯 구역은',F(56,False),(210,220,235))
ctext(d,1520,'블로그에 있습니다',F(56,False),(210,220,235))
ctext(d,1740,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,8)
D=[3.2,3.6,3.2,3.8,3.0,3.6,3.6,3.4]
assemble([f'p{i}.png' for i in range(1,9)],D,'nangman_pyeongchon_short.mp4')
Image.open('p4.png').save('nangman_pyeongchon_cover.png')
ims=[Image.open(f'p{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_p.png')
print('ok')
