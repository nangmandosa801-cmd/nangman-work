import sys; sys.path.insert(0,'/home/claude/blogkit')
from thumbnail import render_listing, F
from PIL import Image, ImageDraw
O='/mnt/user-data/outputs/jisandream/'
render_listing('가평 토지 매물 · 청평 삼회리 임야','포장도로 붙은','계곡 앞','임야 2,962평','계획관리 · 보전관리 · 청평시내 5분','총 2억 4,000만원',O+'jisandream_samhoe_thumb.png')
def frame(src,dst,kick,title,note):
    im=Image.open(src).convert('RGB')
    W=1400; h=int(im.height*(W-120)/im.width); im=im.resize((W-120,h))
    top=178; bot=110; H=h+top+bot+60
    c=Image.new('RGB',(W,H),'#F4F6F8'); d=ImageDraw.Draw(c)
    d.rectangle([0,0,W-1,H-1],outline='#0D3B5C',width=6)
    d.rectangle([0,0,W,14],fill='#1B7A9E')
    d.text((60,42),kick,font=F(30,False,False),fill='#1B7A9E')
    d.text((60,84),title,font=F(44,False,True),fill='#0D3B5C')
    x0,y0=60,top
    d.rectangle([x0-10,y0-10,x0+im.width+9,y0+im.height+9],fill='#FFFFFF',outline='#9CBBCC',width=3)
    c.paste(im,(x0,y0))
    d.text((60,y0+im.height+36),note,font=F(28,False,False),fill='#5A6A78')
    t='지산드림  blog.naver.com/jisandream01'; f=F(24,False,False)
    tw=d.textlength(t,font=f); d.text((W-60-tw,H-50),t,font=f,fill='#9AA4AE')
    c.save(dst)
frame(O+'jisandream_samhoe_map1.png',O+'jisandream_samhoe_map1_frame.png','지산드림 · 가평 토지 매물 위치','청평 삼회리 산 25-2, 북한강 바로 옆 마을 뒤','삼회1리 마을 뒤 · 북한강로(391번 지방도) · 수풀로 삼회리 인근')
frame(O+'jisandream_samhoe_map2.png',O+'jisandream_samhoe_map2_frame.png','지산드림 · 가평 토지 매물 위성사진','임야 2,962평, 아래쪽이 포장도로에 붙습니다','파란 선이 필지 경계 · 삼회1리 마을회관·삼회보건진료소 뒤쪽')
print('ok')
