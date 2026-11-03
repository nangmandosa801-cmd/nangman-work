def frame(im,dst,kick,title,note):
    W=1400; h=int(im.height*(W-120)/im.width); im=im.resize((W-120,h))
    top=178; bot=130; Hh=h+top+bot+40
    c=Image.new('RGB',(W,Hh),'#F4F6F8'); d=ImageDraw.Draw(c)
    d.rectangle([0,0,W-1,Hh-1],outline='#0D3B5C',width=6); d.rectangle([0,0,W,14],fill='#1B7A9E')
    d.text((60,42),kick,font=F(30,False,False),fill='#1B7A9E'); d.text((60,84),title,font=F(44,False,True),fill='#0D3B5C')
    d.rectangle([50,top-10,50+im.width+19,top+im.height+9],fill='#FFFFFF',outline='#9CBBCC',width=3); c.paste(im,(60,top))
    d.text((60,top+im.height+30),note,font=F(28,False,False),fill='#5A6A78')
    s='지도·위성사진 © NAVER'; d.text((60,Hh-58),s,font=F(22,False,False),fill='#9AA4AE')
    t='지산드림  blog.naver.com/jisandream01'; f=F(24,False,False); d.text((W-60-d.textlength(t,font=f),Hh-58),t,font=f,fill='#9AA4AE')
    c.save(dst)
