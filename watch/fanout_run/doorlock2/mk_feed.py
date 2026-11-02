import sys; sys.path.insert(0,'/home/claude')
from comic import F
from PIL import Image,ImageDraw,ImageEnhance
IMG='/home/claude/watch/fanout_run/doorlock2/img/'; OUT='/home/claude/sns/w1025_doorlock2/'
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
    im.save(OUT+f'nangman_interior_sns_doorlock2_{n:02d}.jpg',quality=92)
def graphic_slide(src,n):
    im=Image.new('RGB',(1080,1350),(244,246,249)); g=Image.open(IMG+src).convert('RGB')
    g=g.resize((1040,int(g.height*1040/g.width))); im.paste(g,(20,(1350-g.height)//2)); im.save(OUT+f'nangman_interior_sns_doorlock2_{n:02d}.jpg',quality=92)

photo_slide('dl2_jamsil_after.jpg',[('현관 도어락 교체',90,WH),('사진 네 장이면',84,WH),('옛 구멍 처리까지',84,Y)],1,big=('사진 4장',))
photo_slide('dl2_jamsil_before.jpg',[('서울 잠실 어느 주택',80,WH),('보조키 + 원형 손잡이',84,Y),('둘 다 떼면 구멍 두 개',80,WH)],2)
photo_slide('dl2_junggok_after.jpg',[('보강판으로 덮기',96,Y),('광진 중곡동',76,WH),('은색 판 위 번호키 하나',76,WH)],3)
photo_slide('dl2_hwamyeong_after.jpg',[('손잡이가 멀쩡하면',88,Y),('번호키만 바꿈',88,WH),('부산 화명동 · 옛 구멍 그대로',64,WH)],4)
photo_slide('dl2_dmc_after.jpg',[('구멍이 어긋나면',90,Y),('문을 다듬어 맞춤',88,WH),('마포 아파트 · 지문 푸시풀',64,WH)],5)
photo_slide('dl2_hakjang_after.jpg',[('빈집일 때 바꾸면',88,Y),('이삿날 바로 열림',88,WH),('부산 학장동 · 이사 전 푸시풀',62,WH)],6)
im=Image.new('RGB',(1080,1350),NAVY); d=ImageDraw.Draw(im)
for y,t,s_,c in [(150,'열쇠 · 도어락 시공',100,WH),(300,'전국 연결',110,Y),(470,'서울 · 인천 · 부천',76,WH),(570,'경기 북부 · 부산',76,WH),(760,'문자',90,WH),(880,'010-2882-8165',130,WH),(1090,'낭만 인테리어',90,Y)]:
    w=d.textlength(t,font=F(s_)); d.text(((1080-w)/2,y),t,font=F(s_),fill=c)
im.save(OUT+'nangman_interior_sns_doorlock2_07.jpg',quality=92)
c=Image.new('RGB',(7*270,338))
for i in range(7): c.paste(Image.open(OUT+f'nangman_interior_sns_doorlock2_{i+1:02d}.jpg').resize((270,338)),(270*i,0))
c.save('/home/claude/watch/fanout_run/doorlock2/feed_sheet.jpg')
