# 10/18 06:02 사용자 「문자로 보내 카드 형태로 만들어 줘」 — 중개사무소에 문자(MMS)로 보낼 카드 한 장 · 특정 사무소 이름 없음
import qrcode
from PIL import Image, ImageDraw, ImageFont
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/opentype/noto/NotoSansCJK-{w}.ttc',s,index=1)
W,H=1080,1350; NAVY=(31,56,100); INK=(15,17,22); GREY=(70,76,86); GOLD=(214,160,40); SOFT=(244,246,250)
URL='https://nangmaninterior.tistory.com/18'
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
M=70
d.rectangle((0,0,W,150),fill=NAVY)
d.text((M,40),'낭만 인테리어',font=F('Bold',58),fill='white')
t='공인중개사 대표님께'; f=F('Medium',40); d.text((W-M-d.textlength(t,font=f),54),t,font=f,fill=(210,220,240))
y=200
for ln,c in [('잔금 날, 손님께',INK),('쿠폰 한 장만',NAVY),('건네 주세요',INK)]:
    d.text((M,y),ln,font=F('Black',98),fill=c); y+=128
y+=20; d.rectangle((M,y,M+140,y+10),fill=GOLD); y+=50
for a in ['계약되면 소개비 매달 정산','견적 비교 · 거절 연락은 저희가','사무소 이름 든 쿠폰 무료 제작']:
    d.rounded_rectangle((M,y+8,M+52,y+60),8,outline=NAVY,width=6)
    d.line((M+12,y+34,M+24,y+48,M+44,y+18),fill=GOLD,width=8)
    d.text((M+76,y-4),a,font=F('Bold',56),fill=INK); y+=92
y+=30
d.rounded_rectangle((M-10,y,W-M+10,H-60),28,fill=SOFT)
qs=270; q=qrcode.make(URL,box_size=10,border=1).convert('RGB').resize((qs,qs),Image.NEAREST)
im.paste(q,(W-M-20-qs,y+30))
tx=M+30
d.text((tx,y+40),'자세한 안내',font=F('Bold',52),fill=NAVY)
d.text((tx,y+105),'QR을 찍어 보세요',font=F('Medium',44),fill=GREY)
d.text((tx,y+180),'문자 한 통이면',font=F('Medium',44),fill=GREY)
d.text((tx,y+232),'010-2882-8165',font=F('Black',62),fill=INK)
print('bottom',y+30+qs,H-60)
im.save('/mnt/user-data/outputs/mail1018/nangman_interior_sms_card.jpg',quality=88)
