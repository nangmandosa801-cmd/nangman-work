import sys; sys.path.insert(0,'/home/claude'); from comic import *
from assemble import assemble
from PIL import Image
import os
Y=(240,190,40)
def cards(d,rows,y0=470,h=250,gap=40,fs=(66,54)):
    for i,r in enumerate(rows):
        a,b=r[0],r[1]; c=r[2] if len(r)>2 else NAVY
        y=y0+i*(h+gap)
        d.rounded_rectangle((70,y,1010,y+h),40,fill=(255,255,255),outline=c,width=8)
        ctext(d,y+h*0.16,a,F(fs[0]),NAVY); ctext(d,y+h*0.56,b,F(fs[1]),c)
def photo(im,path,box):
    p=Image.open(path).convert('RGB'); p=p.crop((18,18,p.width-18,p.height-140)); x0,y0,x1,y1=box; w,h=x1-x0,y1-y0
    r=max(w/p.width,h/p.height); p=p.resize((int(p.width*r),int(p.height*r)))
    l=(p.width-w)//2; t=(p.height-h)//2; im.paste(p.crop((l,t,l+w,t+h)),(x0,y0))
def sheet(prefix,n,path):
    ims=[Image.open(f'{prefix}{i}.png').resize((270,480)) for i in range(1,n+1)]
    c=Image.new('RGB',(1080,960),'white');[c.paste(x,((i%4)*270,(i//4)*480)) for i,x in enumerate(ims)];c.save(path)
def fdoor(d,x,y,w,h,col):
    d.rectangle((x,y,x+w,y+h),fill=col); 
    for k in range(3): d.rectangle((x+18+k*(w-36)//3,y+18,x+(k+1)*(w-36)//3+10,y+h-18),fill=GLASS)

# ===== 투명 중문 파크리오
C='/mnt/user-data/outputs/int/case06/'
D='/mnt/user-data/outputs/int/clip15'; os.makedirs(D,exist_ok=True); os.chdir(D)
def sv(im,n): im.save(f'p{n}.png')
im,d=base(); caption(d,['중문 달면','현관이 어두워질까?'])
d.rectangle((150,470,930,1250),fill=(120,120,128)); fdoor(d,300,560,480,690,FRAME)
person(d,540,1290,0.8,face='worry',shirt=MID)
bubble(d,90,1580,900,180,['답답해 보이면 어쩌지'],size=70,fill=(255,243,196)); footer(d); sv(im,1)
im,d=base(); caption(d,['잠실 파크리오는','화이트 통유리'])
photo(im,C+'case06_01_closed.jpg',(110,440,970,1560)); d=__import__('PIL.ImageDraw',fromlist=['x']).Draw(im)
d.rounded_rectangle((110,1580,970,1720),30,fill=NAVY); ctext(d,1605,'프레임 화이트 · 투명 강화 통유리',F(52),(255,255,255))
footer(d); sv(im,2)
im,d=base(); caption(d,['문을 닫아도','거실 빛이 현관까지'])
photo(im,C+'case06_03_living.jpg',(110,440,970,1400)); d=__import__('PIL.ImageDraw',fromlist=['x']).Draw(im)
ctext(d,1450,'현관이 거실과 이어져',F(66),NAVY); ctext(d,1550,'넓어 보입니다',F(66),OK)
footer(d); sv(im,3)
im,d=base(); caption(d,['대신','단점도 셋'])
cards(d,[('문이 잘 안 보임','부딪힐 수 있음',WARN),('거실이 다 보임','현관문 열면 그대로',WARN),('손자국','자주 닦아야',WARN)],y0=470,h=300,gap=50,fs=(72,62))
footer(d); sv(im,4)
im,d=base(); caption(d,['부딪힘은','이렇게 줄여요'])
d.rectangle((250,470,830,1250),fill=(255,255,255),outline=(220,220,220),width=14); d.rectangle((270,490,810,1230),fill=GLASS)
d.ellipse((490,800,590,900),fill=WARN)
ctext(d,1320,'눈높이에 작은 표시 하나',F(72),WARN); ctext(d,1440,'또는 긴 손잡이',F(66),NAVY)
footer(d); sv(im,5)
im,d=base(); caption(d,['거실이 다 보이는 게','싫다면'])
cards(d,[('아래만 불투명 유리','위는 빛 그대로',MID),('간살 섞기','칸 무늬로 시선 나눔',MID)],y0=520,h=380,gap=80,fs=(74,62))
footer(d); sv(im,6)
im,d=base(NAVY); caption(d,['통유리? 칸 나눔?','한쪽만 열림?'],c=(255,255,255))
for i,t in enumerate(['① 현관 정면 사진','② 입구 폭']):
    y=620+i*260; d.rounded_rectangle((110,y,970,y+210),36,fill=(255,255,255)); d.text((160,y+60),t,font=F(72),fill=NAVY)
ctext(d,1260,'보내 주시면 우리 집에',F(60),Y); ctext(d,1350,'맞는 문부터 봐 드립니다',F(60),Y)
ctext(d,1720,'낭만 인테리어 · 블로그에서 전체 보기',F(46,False),(210,220,235)); sv(im,7)
assemble([f'p{i}.png' for i in range(1,8)],[3.0,3.4,3.2,3.2,3.0,3.0,3.2],'nangman_interior_tumyeong_short.mp4')
Image.open('p2.png').save('nangman_interior_tumyeong_cover.png'); sheet('p',7,'/tmp/claude-0/sh_p.png')
print('ok')
