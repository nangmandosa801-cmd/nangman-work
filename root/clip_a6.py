import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
import os; os.chdir('/mnt/user-data/outputs/clip_a6')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40); GREY=(201,196,186)
def save(im,n): im.save(f'a{n}.png')
# 1
im,d=base()
caption(d,['인천계양 A6','84㎡ 7억'])
d.rounded_rectangle((140,470,940,900),44,fill=(255,255,255),outline=NAVY,width=9)
ctext(d,510,'LH 공공분양 663가구',F(56,False),NAVY); ctext(d,620,'일반공급',F(64),NAVY); ctext(d,730,'10월 1~2일',F(96),WARN)
person(d,540,1130,1.0,face='worry',shirt=MID)
bubble(d,90,1520,900,220,['로또분양일까?'],size=88,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['사전청약 때보다','1억 8,900만 올랐습니다'])
B=[('사전청약 추정','5억 2,770만',5.277,GREY),('A2 본청약 (2024)','5억 8,411만',5.841,MID),('A6 본청약 (2026)','7억 1,654만',7.165,WARN)]
for i,(n,v,x,c) in enumerate(B):
    y=480+i*390
    ctext(d,y,n,F(60),NAVY)
    w=int(x/7.3*880)
    d.rounded_rectangle((100,y+100,100+w,y+250),30,fill=c)
    ctext(d,y+130,v,F(74),(255,255,255) if c!=GREY else NAVY,100+w/2)
ctext(d,1680,'84㎡ 최고 분양가 기준',F(46,False),SAND)
save(im,2)
# 3 ladder
im,d=base()
caption(d,['계양구 84㎡','가격 사다리'])
L=[('8억 2,300만','힐스테이트자이계양',NAVY,False),('7억 1,654만','인천계양 A6',WARN,True),('6억 안팎','계양 주요 신축',MID,False)]
for i,(v,n,c,hl) in enumerate(L):
    y=450+i*420
    d.rounded_rectangle((80,y,1000,y+340),40,fill=(255,243,196) if hl else (255,255,255),outline=c,width=10 if hl else 6)
    ctext(d,y+45,v,F(104),c); ctext(d,y+215,n,F(64),NAVY)
    if i<2: ctext(d,y+345,'▼ 약 1억',F(56),SAND)
footer(d); save(im,3)
# 4 1가구
im,d=base()
caption(d,['84㎡ 42가구 중','일반공급은 1가구'])
for i in range(42):
    x=130+(i%7)*120; y=470+(i//7)*120
    d.rounded_rectangle((x,y,x+96,y+96),16,fill=WARN if i==41 else GREY)
ctext(d,1230,'사전청약 29 · 특별공급 11',F(58),NAVY); ctext(d,1320,'이주자 1 · 일반공급 1',F(58),NAVY)
ctext(d,1480,'일반공급이 많은 건 59㎡',F(70),WARN)
footer(d); save(im,4)
# 5 조건
im,d=base()
caption(d,['청약 조건','한눈에'])
for i,(a,b) in enumerate([('실거주 의무','없음'),('전매제한','3년'),('당첨자 발표','10월 21일'),('입주','2029년 6월')]):
    y=440+i*300
    d.rounded_rectangle((80,y,1000,y+250),40,fill=(255,255,255),outline=NAVY,width=7)
    d.text((140,y+75),a,font=F(70),fill=NAVY)
    w=d.textlength(b,font=F(80)); d.text((940-w,y+70),b,font=F(80),fill=WARN)
footer(d); save(im,5)
# 6
im,d=base(NAVY)
caption(d,['당첨되는 순간','시세차익이 생기는','가격은 아닙니다'],c=(255,255,255),size=86)
ctext(d,760,'2029년 계양 신축에',F(70),Y); ctext(d,870,'대장보다 1억 낮은 가격',F(70),Y); ctext(d,980,'낼 것인가',F(70),Y)
person(d,540,1230,0.95,face='o',shirt=MID)
ctext(d,1580,'분양가 · 실거래 표 전체는',F(54,False),(210,220,235)); ctext(d,1655,'블로그에 정리했습니다',F(54,False),(210,220,235))
ctext(d,1770,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,6)
D=[3.2,3.6,3.6,3.4,3.4,3.6]
assemble([f'a{i}.png' for i in range(1,7)],D,'nangman_gyeyang_a6_short.mp4')
from PIL import Image; Image.open('a3.png').save('nangman_gyeyang_a6_cover.png')
ims=[Image.open(f'a{i}.png').resize((360,640)) for i in range(1,7)]
c=Image.new('RGB',(1080,1280));[c.paste(im,((i%3)*360,(i//3)*640)) for i,im in enumerate(ims)];c.save('/tmp/claude-0/sheet_a6.png')
