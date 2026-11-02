import sys; sys.path.insert(0,'/home/claude')
from comic import F
from PIL import Image,ImageDraw,ImageEnhance
IMG='/home/claude/watch/fanout_run/gunpo/img/'; OUT='/home/claude/sns/w1025_gunpo/'
NAVY=(31,56,100); Y=(240,190,40); WH=(255,255,255)
def cover(path):
    im=Image.open(path).convert('RGB'); im=im.crop((0,0,im.width,int(im.height*0.76)))
    W,H=1080,1350; r=max(W/im.width,H/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1))
    x=(im.width-W)//2; y=(im.height-H)//2; return im.crop((x,y,x+W,y+H))
def ctext(d,y,t,size,c,maxw=980):
    s=size
    while d.textlength(t,font=F(s))>maxw: s-=4
    w=d.textlength(t,font=F(s)); d.text(((1080-w)/2,y),t,font=F(s),fill=c,stroke_width=max(2,s//22),stroke_fill=(0,0,0))
def slide(src,lines,n,big=None):
    im=cover(IMG+src); im=ImageEnhance.Brightness(im).enhance(0.55); d=ImageDraw.Draw(im); y=150
    if big: ctext(d,y,big,230,Y); y+=300
    for t,s,c in lines: ctext(d,y,t,s,c); y+=s+40
    d.rectangle((0,1260,1080,1350),fill=NAVY); ctext(d,1278,'낭만 인테리어 · 010-2882-8165',52,WH)
    im.save(OUT+f'nangman_interior_sns_gunpo_{n:02d}.jpg',quality=92)
slide('g5.png',[('베란다 곰팡이',92,WH),('판 대기 전에',86,WH),('끝낼 일이 둘',86,Y)],1,big='4단계')
slide('g3.png',[('세탁기 위 선반',86,WH),('편하지만 벽은',80,WH),('늘 가려져 있음',80,Y)],2)
slide('g4.png',[('창 옆 붙박이장',86,WH),('뒤로 공기가',80,WH),('돌지 않음',86,Y)],3)
slide('g5.png',[('떼어 보니',86,WH),('숨어 있던 곰팡이',90,Y),('경기 군포 구축 아파트',62,WH)],4)
slide('g6.png',[('걷어 내고 살균',92,Y),('판 뒤에 가두지',80,WH),('않기 위해',80,WH)],5)
slide('g7.png',[('얼룩 한 곳 말고',86,WH),('바깥 벽 전체',96,Y),('창 둘레까지 이보드',70,WH)],6)
slide('g2.png',[('들뜸 없이 밀착',92,Y),('벽과 판 사이',80,WH),('찬 공기층 없게',80,WH)],7)
im=Image.new('RGB',(1080,1350),NAVY); d=ImageDraw.Draw(im)
for y,t,s_,c in [(170,'우리 집 베란다',100,WH),(320,'장 뒤 벽',120,Y),(500,'얼룩진 벽 한 장',76,WH),(600,'베란다 전체 한 장',76,WH),(780,'문자',90,WH),(900,'010-2882-8165',130,WH),(1100,'낭만 인테리어',90,Y)]:
    w=d.textlength(t,font=F(s_)); d.text(((1080-w)/2,y),t,font=F(s_),fill=c)
im.save(OUT+'nangman_interior_sns_gunpo_08.jpg',quality=92)
c=Image.new('RGB',(8*270,338))
for i in range(8): c.paste(Image.open(OUT+f'nangman_interior_sns_gunpo_{i+1:02d}.jpg').resize((270,338)),(270*i,0))
c.save('/home/claude/watch/fanout_run/gunpo/feed_sheet.jpg')
