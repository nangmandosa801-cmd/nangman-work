import sys,json
from PIL import Image,ImageDraw,ImageFont
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc';R='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
f=lambda p,s:ImageFont.truetype(p,s,index=1)
NAVY=(31,56,100);GOLD=(185,138,46);INK=(34,34,34);GR=(110,110,110);LINE=(220,224,230)
def card(title,sub,items,foot,out):
    W=966;H=230+len(items)*150+90;im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,10],fill=NAVY)
    d.text((60,72),title,font=f(B,44),fill=INK,anchor='lm');d.text((60,128),sub,font=f(R,28),fill=GR,anchor='lm')
    d.line([60,170,W-60,170],fill=LINE,width=2);y=200
    for i,(a,b) in enumerate(items):
        d.rounded_rectangle([60,y,W-60,y+130],radius=14,fill=(246,240,228) if i==0 else (244,246,250))
        d.text((100,y+42),a,font=f(B,36),fill=NAVY if i else GOLD,anchor='lm');d.text((100,y+92),b,font=f(R,27),fill=INK,anchor='lm')
        y+=150
    d.text((W-60,H-45),foot,font=f(R,24),fill=GR,anchor='rm');im.save(out)
card('평택 제휴팀이 잘하는 것','지제역 쌍용 입주청소 · 새집증후군을 맡는 팀',[
 ('외주 없이 직영팀이 들어갑니다','2018년부터 아파트 100곳 넘게 · 청소 · 줄눈 1만 세대 넘게'),
 ('청소 전에 하자부터 찍어 보냅니다','스크래치 · 찍힘 · 페인트 얼룩을 영상으로'),
 ('떼어 낼 수 있는 건 다 떼어 닦습니다','서랍 · 선반 · 배수구 · 걸레받이 · 환풍기 · 방충망 · 전등갓'),
 ('바닥은 네 번 닦습니다','건식 흡입 → 전용 세제 → 바닥 장비 → 손걸레'),
 ('계약금 없이 끝나고 냅니다','현장에서 붙는 추가 요금 없음 · 측정값 사진은 단계마다')],
 '낭만 인테리어 · 평택 입주','/home/claude/ssang/ph/strength.png')
card('부산 제휴팀이 잘하는 것','에코델타시티 중흥S클래스 입주청소 · 새집증후군을 맡는 팀',[
 ('부부가 직접, 하루 한 집만','다른 집 일정에 밀려 서두르지 않습니다'),
 ('25~34평 입주청소 65만원','청소 + 새집증후군 묶음은 90만원'),
 ('현장에서 붙는 추가금이 없습니다','계약 때 정한 금액 그대로'),
 ('청소 다음 날 새집증후군','시공 전후 포름알데히드를 재서 사진으로')],
 '낭만 인테리어 · 부산 에코델타시티','/home/claude/eco/eco_strength.png')
