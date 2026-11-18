# -*- coding: utf-8 -*-
# 하남 그린벨트 해제 지역 그림: 01 썸네일(C형) · 02 택지 세 곳 집 수 · 03 허가 남은 동네 거래 → .../jisandream/gbhaeje/img/
import os
from PIL import Image, ImageDraw, ImageFont
F='/home/claude/tools/tistory/fonts/Pretendard-'
def ft(w,s): return ImageFont.truetype(F+w+'.otf',s)
O='/mnt/user-data/outputs/jisandream/gbhaeje/img/'; os.makedirs(O,exist_ok=True)
NAVY=(13,59,92); CYAN=(27,122,158); GREY=(176,186,196); INK=(34,40,46); SUB=(110,120,130); BG=(255,255,255); PALE=(244,246,248); GOLD=(201,150,40)
def ctext(d,y,t,f,c,W):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)

# 01 썸네일 1080x1080 · 그 글만의 조건 하나를 크게
W=H=1080; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,150],fill=NAVY)
ctext(d,48,'지산드림 · 하남 그린벨트 해제 지역',ft('Bold',44),(255,255,255),W)
ctext(d,250,'11월 3일 풀린 것은',ft('SemiBold',62),SUB,W)
ctext(d,350,'허가뿐',ft('ExtraBold',230),CYAN,W)
ctext(d,640,'그린벨트는 그대로입니다',ft('Bold',70),INK,W)
d.rectangle([90,790,W-90,960],fill=PALE)
ctext(d,815,'그린벨트가 풀릴 곳은 네 곳',ft('Bold',48),NAVY,W)
ctext(d,885,'교산 · 감일2 · 미사섬 · 캠프콜번',ft('SemiBold',44),SUB,W)
im.save(O+'01.jpg',quality=92)

def hbar(rows,xmax,title,sub,note,out):
    W=1200; n=len(rows); H=300+n*150+90
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.text((60,50),title,font=ft('ExtraBold',54),fill=INK)
    d.text((60,135),sub,font=ft('Medium',32),fill=SUB)
    x0=330; x1=W-80; y=250
    for lab,v,col,txt in rows:
        d.text((60,y+28),lab,font=ft('Bold',38),fill=INK)
        L=int((x1-x0)*v/xmax); d.rectangle([x0,y+10,x0+max(L,6),y+100],fill=col)
        tw=d.textlength(txt,font=ft('Bold',36))
        if L>tw+40: d.text((x0+L-tw-20,y+33),txt,font=ft('Bold',36),fill=(255,255,255))
        else: d.text((x0+L+16,y+33),txt,font=ft('Bold',36),fill=INK)
        y+=150
    d.text((60,H-70),note,font=ft('Medium',26),fill=SUB)
    im.save(out,quality=92)

hbar([('교산신도시',37000,CYAN,'3만 7천 호'),('미사섬 K-컬처',12000,GREY,'1만 2천 가구'),('감일2',6500,GREY,'6,500가구')],40000,
 '하남 그린벨트에 들어설 집 5만 5천여 채','풀렸거나 풀릴 하남 택지 세 곳의 집 수 · 캠프콜번은 집 수 미정',
 '교산: 2026.7 하남시 발표 · 미사섬 · 감일2: 국토교통부 2026.10.29 후보지 발표',O+'02.jpg')
hbar([('하남 전체',2024,GREY,'2,024건'),('감북 · 감일 · 미사',359,CYAN,'359건 (18%)')],2300,
 '하남 땅 거래 다섯 건 중 한 건은 아직 허가','2025.1~2026.8 하남 땅 거래 · 허가가 남은 세 동',
 '국토교통부 토지 실거래 · 해제 거래 빼고 · 세 동은 「일원」이라 일부 필지만 허가 대상',O+'03.jpg')
print('ok',sorted(os.listdir(O)))
