import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os; os.chdir('/mnt/user-data/outputs/int/clip_sb')
def footer(d): ctext(d,1830,'낭만 인테리어',F(40,False),SAND)
Y=(240,190,40); SHOE=(170,125,95); WOOD=(196,160,120)
def save(im,n): im.save(f's{n}.png')
def shelf(d,x,y,w,h,open_deg=0):
    d.rectangle((x,y,x+w,y+h),fill=SHOE); d.rectangle((x+14,y+14,x+w-14,y+h-14),outline=(140,100,75),width=6)
    for k in range(1,4): d.line((x+14,y+k*(h-28)//4+14,x+w-14,y+k*(h-28)//4+14),fill=(140,100,75),width=5)
    d.ellipse((x+w-56,y+h//2-14,x+w-30,y+h//2+14),fill=(90,90,95))
def sldoor(d,x,y,w,h,piled=False):
    d.rectangle((x-16,y-34,x+w+16,y),fill=FRAME)
    if piled:
        for i in range(3):
            px=x+i*26
            d.rectangle((px,y,px+120,y+h),fill=FRAME); d.rectangle((px+12,y+12,px+108,y+h-12),fill=GLASS)
    else:
        pw=w//3
        for i in range(3):
            px=x+i*pw
            d.rectangle((px,y,px+pw-6,y+h),fill=FRAME); d.rectangle((px+12,y+12,px+pw-18,y+h-12),fill=GLASS)
# 1
im,d=base((243,240,233))
caption(d,['신발장 먼저','예쁘게 짰습니다'])
d.rectangle((0,1330,1080,1920),fill=(219,210,196))
shelf(d,300,620,480,710)
person(d,860,1180,0.8,face='smile',shirt=MID)
bubble(d,70,1450,700,220,['깔끔하네!'],size=76,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base((243,240,233))
caption(d,['한 달 뒤','중문을 달았습니다'])
d.rectangle((0,1330,1080,1920),fill=(219,210,196))
shelf(d,90,620,380,710)
sldoor(d,540,600,480,730)
person(d,300,1500,0.62,face='o',shirt=MID)
footer(d); save(im,2)
# 3
im,d=base((243,240,233))
caption(d,['신발장 문이','안 열립니다'],c=WARN)
d.rectangle((0,1330,1080,1920),fill=(219,210,196))
shelf(d,90,620,380,710)
sldoor(d,470,600,340,730,piled=True)
d.line((430,780,560,910),fill=WARN,width=22); d.line((560,780,430,910),fill=WARN,width=22)
person(d,860,1180,0.8,face='shock',shirt=MID)
bubble(d,70,1480,880,230,['열린 문짝이','딱 그 앞에…'],size=66,fill=(255,243,196))
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['현관에서는 세 공간이','겹칩니다'],size=72)
for i,(n,t) in enumerate([('하나','사람이 서서 신 신는 공간'),('둘','신발장 문이 열리는 공간'),('셋','중문 문짝이 움직이는 공간')]):
    y=480+i*300
    d.rounded_rectangle((70,y,1010,y+250),40,fill=(255,255,255),outline=MID,width=8)
    ctext(d,y+34,n,F(58),SAND); ctext(d,y+118,t,F(64),NAVY)
ctext(d,1480,'셋이 겹치는 곳에서 매일 불편이 생깁니다',F(56),WARN)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['부딪히는 곳은','딱 네 군데'])
for i,t in enumerate(['슬라이딩 문짝이 모이는 쪽','스윙 중문이 도는 반원 안','신발장 여닫이 문이 열리는 폭','신발장 옆면과 윗부분']):
    y=460+i*260
    d.rounded_rectangle((70,y,1010,y+215),36,fill=(255,255,255),outline=WARN,width=8)
    ctext(d,y+40,f'{i+1}',F(52),SAND); ctext(d,y+110,t,F(62),NAVY)
footer(d); save(im,5)
# 6
im,d=base((243,240,233))
caption(d,['이렇게 하면','안 부딪힙니다'])
d.rounded_rectangle((70,480,1010,820),40,fill=(255,255,255),outline=OK,width=9)
ctext(d,530,'슬라이딩 중문이면',F(58),SAND)
ctext(d,620,'문짝 모이는 쪽을 신발장 반대편으로',F(58),OK)
d.rounded_rectangle((70,890,1010,1230),40,fill=(255,255,255),outline=OK,width=9)
ctext(d,940,'스윙 중문이면',F(58),SAND)
ctext(d,1030,'문이 도는 반원 안에 손잡이가 없게',F(58),OK)
person(d,540,1460,0.85,face='smile',shirt=OK)
footer(d); save(im,6)
# 7
im,d=base()
caption(d,['신발장 문도','같이 고릅니다'])
for i,(a,b,c) in enumerate([('여닫이','한 번에 다 열림 · 앞이 비어야 함',MID),('미닫이','앞으로 안 나옴 · 절반만 열림',OK),('문 없는 선반','꺼내기 편함 · 먼지가 보임',SAND)]):
    y=480+i*300
    d.rounded_rectangle((70,y,1010,y+250),40,fill=(255,255,255),outline=c,width=8)
    ctext(d,y+34,a,F(70),NAVY); ctext(d,y+128,b,F(52),c)
ctext(d,1460,'현관이 좁고 중문이 가까우면 미닫이',F(58),WARN)
footer(d); save(im,7)
# 8
im,d=base(NAVY)
caption(d,['중문을 달 거면','신발장부터 같이'],c=(255,255,255),size=80)
ctext(d,620,'깊이 · 위치 · 문 여는 방향',F(76),Y)
ctext(d,740,'이 셋을 한 번에 정하세요',F(66),(255,255,255))
person(d,540,1060,0.95,face='smile',shirt=MID)
ctext(d,1420,'현관 사진과 신발장 벽 길이를 주시면',F(52,False),(210,220,235))
ctext(d,1500,'부딪히는지부터 봐 드립니다',F(52,False),(210,220,235))
ctext(d,1740,'낭만 인테리어',F(48),(210,220,235))
save(im,8)
D=[3.0,3.0,3.4,3.6,3.6,3.6,3.6,3.4]
assemble([f's{i}.png' for i in range(1,9)],D,'int_hyeongwan_sinbaljang_short.mp4')
Image.open('s3.png').save('int_hyeongwan_sinbaljang_cover.png')
ims=[Image.open(f's{i}.png').resize((270,480)) for i in range(1,9)]
c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save('/tmp/claude-0/sheet_s.png')
print('ok')
