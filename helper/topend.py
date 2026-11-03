from PIL import Image, ImageDraw
from viz import kr, SANS, SANSR
NAVY=(31,56,100); BG=(244,246,249); RED=(181,50,40)
def card(out,lines,end=False):
    W=966; H=636 if end else 478
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,6],fill=(140,160,195)); d.rectangle([0,H-6,W,H],fill=(140,160,195)); d.rectangle([0,0,14,H],fill=NAVY)
    y=48
    for t in lines: d.text((62,y),t,font=kr(SANS,34),fill=NAVY); y+=50
    y+=12; d.text((62,y),'사진 한 장 문자로 보내 주시면 무료로 봐 드립니다',font=kr(SANS,30),fill=(51,51,51)); y+=58
    d.text((62,y),'11월 30일까지 연락한 집은 견적 금액에서 5% 할인',font=kr(SANS,30),fill=RED); y+=62
    d.text((62,y),'전화 · 문자  010-2882-8165',font=kr(SANS,58),fill=NAVY); y+=90
    if end:
        d.line([62,y,W-36,y],fill=(200,205,215),width=2); y+=18
        for t in ['낭만 부동산 분석 플랫폼 · 시공 · 이사는 제휴 팀이 맡습니다.','계약이 되면 수수료를 받습니다.','매수 · 매도를 권하지 않습니다.']:
            d.text((62,y),t,font=kr(SANSR,30),fill=(90,90,90)); y+=44
    im.save(out)
