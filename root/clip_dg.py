import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
import os; os.chdir('/mnt/user-data/outputs/clip_dg')
def footer(d): ctext(d,1830,'낭만 부동산 분석 플랫폼',F(40,False),SAND)
Y=(240,190,40)
def bld(d,x,y,w,h,c,floors):
    d.rectangle((x,y,x+w,y+h),fill=c)
    for f in range(floors):
        for k in range(3): d.rectangle((x+20+k*(w-40)//3,y+20+f*(h-40)//floors,x+10+(k+1)*(w-40)//3,y+10+(f+1)*(h-40)//floors-20),fill=(255,255,255))
def save(im,n): im.save(f'g{n}.png')
# 1
im,d=base()
caption(d,['분양가 4억대였던','두 아파트'])
bld(d,120,560,340,620,MID,7); bld(d,620,560,340,620,OK,7)
ctext(d,1210,'동탄역',F(58),NAVY,290); ctext(d,1285,'롯데캐슬',F(58),NAVY,290)
ctext(d,1210,'광교',F(58),NAVY,790); ctext(d,1285,'자연앤힐',F(58),NAVY,790)
bubble(d,90,1450,900,260,['지금은','둘 다 19억?!'],size=80,fill=(255,243,196))
footer(d); save(im,1)
# 2
im,d=base()
caption(d,['2026년 84㎡','평균 거래 가격'])
for i,(n,v,s,c) in enumerate([('동탄역 롯데캐슬','19억 400만','분양가 4억 8,200만',MID),('광교 자연앤힐','18억 5,900만','분양가 약 4억',OK)]):
    y=440+i*640
    d.rounded_rectangle((80,y,1000,y+560),44,fill=(255,255,255),outline=c,width=9)
    ctext(d,y+50,n,F(72),NAVY); ctext(d,y+190,v,F(118),c); ctext(d,y+400,s,F(58,False),SAND)
footer(d); save(im,2)
# 3
im,d=base()
caption(d,['차이는','걸린 시간'])
for i,(n,yrs,x4,c) in enumerate([('동탄',8.5,'4.0배',MID),('광교',16.5,'4.6배',OK)]):
    y=560+i*520
    ctext(d,y,n,F(80),NAVY)
    w=int(yrs/16.5*860)
    d.rounded_rectangle((110,y+130,110+w,y+260),28,fill=c)
    ctext(d,y+150,f'{yrs:g}년'.replace('.5년','년 반'),F(80),(255,255,255),110+w/2)
    ctext(d,y+290,x4,F(64),c)
ctext(d,1640,'동탄이 두 배 빨랐습니다',F(70),WARN)
footer(d); save(im,3)
# 4
im,d=base()
caption(d,['속도를 바꾼 건','분양한 해'])
for i,(yr,a,b,c) in enumerate([('2009년','금융위기 바로 뒤','입주 뒤에도 한동안 하락',OK),('2017년','공사 중 2020~21 상승기','2024년 GTX-A 개통',MID)]):
    y=470+i*620
    d.rounded_rectangle((80,y,1000,y+540),44,fill=(255,255,255),outline=c,width=9)
    ctext(d,y+50,('광교 ' if i==0 else '동탄 ')+yr+' 분양',F(76),c)
    ctext(d,y+220,a,F(64),NAVY); ctext(d,y+340,b,F(64),NAVY)
footer(d); save(im,4)
# 5
im,d=base()
caption(d,['그런데 최근 3년은','광교가 더 올랐습니다'])
for i,(n,a,b,p,c) in enumerate([('광교 자연앤힐','13억 300만','18억 6,400만','+43.3%',OK),('동탄역 롯데캐슬','14억 9,600만','19억 1,200만','+27.9%',MID)]):
    y=460+i*620
    d.rounded_rectangle((80,y,1000,y+540),44,fill=(255,255,255),outline=c,width=9)
    ctext(d,y+40,n,F(66),NAVY); ctext(d,y+150,f'{a} → {b}',F(58,False),NAVY); ctext(d,y+280,p,F(140),c)
ctext(d,1720,'같은 단지 · 같은 평형 2023 → 2026',F(44,False),SAND)
save(im,5)
# 6
im,d=base(NAVY)
caption(d,['분양가가 같아도','언제 분양했느냐가','속도를 바꿉니다'],c=(255,255,255),size=86)
ctext(d,760,'동탄 8년 반',F(84),Y); ctext(d,880,'광교 16년 반',F(84),Y)
person(d,540,1180,1.0,face='smile',shirt=MID)
ctext(d,1560,'분양가 · 가격 표 전체는',F(54,False),(210,220,235)); ctext(d,1640,'블로그에 정리했습니다',F(54,False),(210,220,235))
ctext(d,1760,'낭만 부동산 분석 플랫폼',F(48),(210,220,235))
save(im,6)
D=[3.2,3.4,3.4,3.6,3.6,3.4]
assemble([f'g{i}.png' for i in range(1,7)],D,'nangman_dongtan_gwanggyo_short.mp4')
from PIL import Image; Image.open('g3.png').save('nangman_dongtan_gwanggyo_cover.png')
print(sum(D))
