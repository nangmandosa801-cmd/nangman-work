import sys; sys.path.insert(0,'/home/claude'); from comic import *
import comic, os
from PIL import ImageDraw
os.chdir('/mnt/user-data/outputs/clip_hs')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
GREY=(201,196,186)
def save(im,n): im.save(f'h{n}.png')
# 1
im,d=base()
caption(d,['화성 아파트,','다 같이 회복했을까?'])
names=['동탄1','동탄2','병점·진안','봉담','남양','향남','송산·새솔','우정·장안']
ctext(d,470,'화성시 = 서울의 1.4배 · 생활권 8곳',F(48),SAND)
for i,t in enumerate(names):
    x=110+(i%2)*450; y=570+(i//2)*150
    d.rounded_rectangle((x,y,x+410,y+120),30,fill=(255,255,255),outline=WARN if t=='동탄2' else MID,width=6)
    ctext(d,y+28,t,F(56),WARN if t=='동탄2' else NAVY,x+205)
person(d,540,1370,1.0,face='worry',shirt=WARN)
bubble(d,90,1680,900,130,['어디를 봐야 하지?'],size=56,fill=(255,243,196))
save(im,1)
# 2 45%
im,d=base()
caption(d,['거래 열 건 중','네 건 반이 동탄2'])
for i in range(100):
    x=150+(i%10)*80; y=520+(i//10)*80
    d.rounded_rectangle((x,y,x+62,y+62),12,fill=WARN if i<45 else GREY)
ctext(d,1360,'2025년 이후 2만 5,246건 중',F(54,False),NAVY)
ctext(d,1450,'1만 1,316건 = 45%',F(80),WARN)
footer(d); save(im,2)
# 3 순위
im,d=base()
caption(d,['그런데 회복률은','꼴찌입니다'])
R=[('우정·장안',119.9),('남양',105.8),('병점·진안',101.0),('봉담',99.4),('향남',96.9),('동탄1',95.5),('송산·새솔',93.0),('동탄2',91.5)]
for i,(n,v) in enumerate(R):
    y=470+i*150; w=int((v-80)/40*420)
    c=WARN if n=='동탄2' else (OK if i==0 else MID)
    d.text((70,y+20),n,font=F(50),fill=NAVY)
    d.rounded_rectangle((360,y+14,360+w,y+96),16,fill=c)
    d.text((370+w,y+18),f'{v}%',font=F(52),fill=c)
d.line((360+int(20/40*420),450,360+int(20/40*420),1690),fill=SAND,width=4)
ctext(d,1700,'100% = 2021년 가격',F(44,False),SAND,360+int(20/40*420))
footer(d); save(im,3)
# 4 신축 비중
im,d=base()
caption(d,['차이는','새 아파트 비중'])
def bld(x,y,w,h,c,floors):
    d.rectangle((x,y,x+w,y+h),fill=c)
    for f in range(floors):
        for k in range(3): d.rectangle((x+20+k*(w-40)//3,y+20+f*(h-40)//floors,x+10+(k+1)*(w-40)//3,y+10+(f+1)*(h-40)//floors-20),fill=(255,255,255))
bld(140,760,300,560,SAND,6); bld(640,560,300,760,MID,9)
ctext(d,1360,'우정·장안',F(58),NAVY,290); ctext(d,1440,'신축 1.2%',F(56),SAND,290); ctext(d,1530,'119.9%',F(72),OK,290)
ctext(d,1360,'동탄2',F(58),NAVY,790); ctext(d,1440,'신축 98.5%',F(56),MID,790); ctext(d,1530,'91.5%',F(72),WARN,790)
footer(d); save(im,4)
# 5 같은 동탄
im,d=base()
caption(d,['같은 동탄인데도'])
for i,(n,v,s,c) in enumerate([('동탄1',95.5,'2007년 첫 입주 · 공급 끝',MID),('동탄2',91.5,'지금도 입주 중',WARN)]):
    y=520+i*560
    d.rounded_rectangle((90,y,990,y+460),44,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+50,n,F(76),NAVY); ctext(d,y+170,f'{v}%',F(120),c); ctext(d,y+340,s,F(52,False),NAVY)
footer(d); save(im,5)
# 6 지산
im,d=base()
caption(d,['영천동 지식산업센터,','언제 샀느냐가 갈랐다'.replace('갈랐다','차이를 만들었다')] if False else ['영천동 지식산업센터','산 해에 따라 다릅니다'])
for i,(n,v,c) in enumerate([('2021년에 산 호실','+10.3%',OK),('2023년에 산 호실','-13.0%',WARN)]):
    y=560+i*520
    d.rounded_rectangle((90,y,990,y+420),44,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+60,n,F(66),NAVY); ctext(d,y+180,v,F(130),c)
ctext(d,1640,'같은 건물 같은 평형끼리 비교',F(46,False),SAND)
footer(d); save(im,6)
# 7 end
im,d=base(NAVY)
caption(d,['화성은','한 도시로 보면','안 보입니다'],c=(255,255,255))
ctext(d,900,'권역별로 봐야',F(84),(240,190,40))
ctext(d,1030,'우정·장안 119.9%',F(64),(255,255,255)); ctext(d,1130,'동탄2 91.5%',F(64),(255,255,255))
ctext(d,1330,'8개 권역 전체 표와 지식산업센터는',F(50,False),(210,220,235)); ctext(d,1410,'블로그에 정리했습니다',F(50,False),(210,220,235))
ctext(d,1720,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,7)
