import sys; sys.path.insert(0,'/home/claude')
from comic import F
from PIL import Image,ImageDraw,ImageEnhance
IMG='/home/claude/watch/fanout_run/brain5bl/img/'; OUT='/home/claude/sns/w1025_brain5bl/'
NAVY=(31,56,100); Y=(240,190,40); WH=(255,255,255)
def cover(path):
    im=Image.open(path).convert('RGB'); W,H=1080,1350
    r=max(W/im.width,H/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1))
    x=(im.width-W)//2; y=(im.height-H)//2; return im.crop((x,y,x+W,y+H))
def ctext(d,y,t,size,c,maxw=980):
    s=size
    while d.textlength(t,font=F(s))>maxw: s-=4
    w=d.textlength(t,font=F(s)); d.text(((1080-w)/2,y),t,font=F(s),fill=c,stroke_width=max(2,s//22),stroke_fill=(0,0,0))
def photo_slide(src,lines,n,big=None):
    im=cover(IMG+src); im=ImageEnhance.Brightness(im).enhance(0.55); d=ImageDraw.Draw(im)
    y=150
    if big:
        ctext(d,y,big[0],230,Y); y+=300
    for t,s,c in lines: ctext(d,y,t,s,c); y+=s+40
    d.rectangle((0,1260,1080,1350),fill=NAVY); ctext(d,1278,'낭만 인테리어 · 010-2882-8165',52,WH)
    im.save(OUT+f'nangman_interior_sns_brain5bl_{n:02d}.jpg',quality=92)
def graphic_slide(src,n):
    im=Image.new('RGB',(1080,1350),(244,246,249)); g=Image.open(IMG+src).convert('RGB')
    g=g.resize((1040,int(g.height*1040/g.width))); im.paste(g,(20,(1350-g.height)//2)); im.save(OUT+f'nangman_interior_sns_brain5bl_{n:02d}.jpg',quality=92)
# 문의 장
P='nangman_interior_brain5bl_jungmun_'
photo_slide(P+'02_m_open.jpg',[('브레인시티 대광로제비앙',80,WH),('그랜드센텀 사전점검',84,WH),('10/30 ~ 11/1',96,Y)],1,big=('1,182세대',))
im=Image.new('RGB',(1080,1350),(244,239,228)); d=ImageDraw.Draw(im)
d.rectangle((120,330,470,1000),outline=(120,110,100),width=14); d.rectangle((490,330,960,1000),fill=(200,170,130),outline=(120,90,60),width=10)
for k in (1,2): d.line((490,330+k*223,960,330+k*223),fill=(120,90,60),width=6)
for y,t,s_,c in [(120,'평택 동삭동 어느 집',76,NAVY),(620,'신발장',80,NAVY),(1040,'신발장이 벽 끝까지',88,(196,70,60)),(1150,'→ 문짝을 잘라 문을 달았다',70,NAVY)]:
    w=d.textlength(t,font=F(s_)); d.text(((1080-w)/2 if t!='신발장' else 725-w/2,y),t,font=F(s_),fill=c)
d.rectangle((0,1260,1080,1350),fill=NAVY); ctext(d,1278,'낭만 인테리어 · 010-2882-8165',52,WH)
im.save(OUT+'nangman_interior_sns_brain5bl_02.jpg',quality=92)
photo_slide(P+'03_m_slat.jpg',[('스위치 · 인터폰',96,Y),('문이 닿을 벽에',84,WH),('붙어 있는지 보기',84,WH)],3)
photo_slide(P+'04_m_slat_open.jpg',[('줄자로 숫자 셋',96,Y),('현관 폭 · 천장 높이',80,WH),('옆 벽 길이',80,WH),('사진은 두 장',90,Y),('1월 입주 = 겨울 성수기',70,WH)],4)
im=Image.new('RGB',(1080,1350),NAVY); d=ImageDraw.Draw(im)
for y,t,s,c in [(170,'공동구매 모집',120,WH),(360,'사전점검 · 중문 · 줄눈',84,Y),(500,'잰 치수 + 사진 두 장',84,Y),(760,'문자',90,WH),(880,'010-2882-8165',130,WH),(1090,'낭만 인테리어',90,Y)]:
    w=d.textlength(t,font=F(s)); d.text(((1080-w)/2,y),t,font=F(s),fill=c)
im.save(OUT+'nangman_interior_sns_brain5bl_05.jpg',quality=92)
c=Image.new('RGB',(5*270,338))
for i in range(5): c.paste(Image.open(OUT+f'nangman_interior_sns_brain5bl_{i+1:02d}.jpg').resize((270,338)),(270*i,0))
c.save('/home/claude/watch/fanout_run/brain5bl/feed_sheet.jpg')
