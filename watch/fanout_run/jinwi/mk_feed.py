import sys; sys.path.insert(0,'/home/claude')
from comic import F
from PIL import Image,ImageDraw,ImageEnhance
IMG='/home/claude/watch/fanout_run/jinwi/img/'; OUT='/home/claude/sns/w1025_jinwi/'
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
    im.save(OUT+f'nangman_interior_sns_jinwi_seohui_{n:02d}.jpg',quality=92)
def graphic_slide(src,n):
    im=Image.new('RGB',(1080,1350),(244,246,249)); g=Image.open(IMG+src).convert('RGB')
    g=g.resize((1040,int(g.height*1040/g.width))); im.paste(g,(20,(1350-g.height)//2)); im.save(OUT+f'nangman_interior_sns_jinwi_seohui_{n:02d}.jpg',quality=92)
photo_slide('nangman_interior_jinwi_parkview_sajeon_01_nano.jpg',[('진위역 서희스타힐스 59㎡',84,WH),('1,659세대의 절반이 넘습니다',70,WH),('사전점검 11월 14~15일',80,Y)],1,big=('846세대',))
photo_slide('nangman_interior_jinwi_parkview_sajeon_02_nano.jpg',[('71㎡는 욕실이 두 곳',96,Y),('두드리기 → 물 붓기',80,WH),('→ 세면대 밑 실리콘',80,WH),('두 곳 다 같은 순서로',80,WH)],2)
photo_slide('nangman_interior_jinwi_parkview_sajeon_03_nano.jpg',[('84㎡ C타입',96,Y),('꺾인 창 모서리',84,WH),('실리콘을 가까이서',84,WH),('같은 단지 30세대가 모이면',70,Y),('욕실 나노코팅 무료',90,Y)],3)
graphic_slide('nangman_interior_jinwi_parkview_sajeon_top.png',4)
# 문의 장
im=Image.new('RGB',(1080,1350),NAVY); d=ImageDraw.Draw(im)
for y,t,s,c in [(220,'세대를 모으면',110,WH),(400,'사전점검',120,Y),(560,'공동구매 단가로 안내',96,Y),(820,'문자',90,WH),(940,'010-2882-8165',130,WH),(1140,'낭만 인테리어',90,Y)]:
    w=d.textlength(t,font=F(s)); d.text(((1080-w)/2,y),t,font=F(s),fill=c)
im.save(OUT+'nangman_interior_sns_jinwi_seohui_05.jpg',quality=92)
c=Image.new('RGB',(5*270,338))
for i in range(5): c.paste(Image.open(OUT+f'nangman_interior_sns_jinwi_seohui_{i+1:02d}.jpg').resize((270,338)),(270*i,0))
c.save('/home/claude/watch/fanout_run/jinwi/feed_sheet.jpg')
