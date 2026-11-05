import sys; sys.path.insert(0,'/home/claude/blogkit')
from PIL import Image, ImageDraw
from thumbnail import render_interior, F, _mark_door
O='/mnt/user-data/outputs/int/byeolnae/'
U='/root/.claude/uploads/0c32fbc6-c708-59b2-959b-9e774c0e2364/'
render_interior('낭만 인테리어 · 시공 사례',['비대칭 중문 단점,','별내 포스코더샵 시공'],'망입유리와 하부고시로 줄였습니다','남양주 별내동 포스코더샵 · 비대칭 양개 중문',O+'nangman_interior_byeolnae_thumb.png')
def frame(src,cap,out):
    im=Image.open(src).convert('RGB'); W=780; m=18
    pw=W-2*m; ph=int(im.height*pw/im.width); im=im.resize((pw,ph),Image.LANCZOS)
    H=m+ph+140
    c=Image.new('RGB',(W,H),'white'); c.paste(im,(m,m)); d=ImageDraw.Draw(c)
    y=m+ph+18; d.text((m,y),cap,font=F(19,False,False),fill='#555555')
    y2=y+42; d.line([(m,y2),(W-m,y2)],fill='#DDD8CE',width=2)
    _mark_door(d,m,y2+18,26,36,frame='#FFFFFF')
    d.text((m+48,y2+18),'낭만 인테리어',font=F(26,False,True),fill='#1F3864')
    ph_t='010-7678-9967'; f=F(24,False,True); tw=d.textlength(ph_t,font=f)
    d.text((W-m-tw,y2+20),ph_t,font=f,fill='#8A8578')
    c.save(out,quality=92)
P=[('a9b86067-image.jpg','현관 안쪽에서 본 모습 — 큰 문과 작은 문이 닫힌 비대칭 양개 중문','01_closed'),
   ('ec6bd7f7-image.jpg','복도에서 본 모습 — 인디브라운 틀에 검은 긴 손잡이','02_hall'),
   ('49dbc1b5-image.jpg','큰 문을 연 모습 — 망입 강화유리와 아래쪽 하부고시 판','03_open'),
   ('cf200a1e-image.jpg','복도 쪽에서 연 모습 — 큰 문이 현관 쪽으로 열려 복도를 막지 않습니다','04_open_hall')]
for s,c,n in P: frame(U+s,c,O+f'nangman_interior_byeolnae_{n}.jpg')
