from PIL import Image,ImageDraw,ImageFont
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; R='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
F=lambda s,b=True:ImageFont.truetype(B if b else R,s,index=1)
BG='#F7F5F0'; INK='#1E2A27'; MUT='#6B746F'; ACC='#1F7A5C'; ACC2='#D9822B'; LINE='#E2DED5'
W=966; POST='청주 신영지웰푸르지오센트럴 옵션, 안 고른 집이 볼 다섯 곳'
def base(h,ctx,title):
    im=Image.new('RGB',(W,h),BG); d=ImageDraw.Draw(im)
    d.text((48,40),ctx,font=F(26),fill=ACC)
    d.text((48,80),title,font=F(44),fill=INK)
    d.text((48,h-44),POST,font=F(20,False),fill='#B9B4A8')
    return im,d
# 1) 옵션 금액 막대 (84㎡)
rows=[('시스템에어컨 4대',642),('욕실특화',531),('바닥 포세린 타일',248),('주방 상판 엔지니어드스톤',234),('현관 중문 3연동',165),('붙박이장 (방 하나)',132)]
im,d=base(880,'청주 신영지웰푸르지오센트럴 · 84㎡ 옵션','안 고르면 입주 뒤에 채울 금액')
y=190; mx=642; L=48; bw=W-96
for n,v in rows:
    d.text((L,y),n,font=F(32),fill=INK)
    w=int((bw-160)*v/mx); d.rounded_rectangle((L,y+52,L+w,y+92),8,fill=ACC if n!='현관 중문 3연동' else ACC2)
    d.text((L+w+16,y+50),f'{v}만원',font=F(34),fill=INK)
    y+=98
d.text((48,y+6),'공고 금액 · 부가세 포함 · 84A 기준 (욕실 84C 516만 · 주방 84B 214만)',font=F(22,False),fill=MUT)
im.save('fig1_option_price.png')
# 2) 중문: 옵션 vs 입주 뒤
im,d=base(700,'청주 신영지웰푸르지오센트럴 · 현관 중문','옵션 165만원 vs 입주 뒤에 달기')
cw=(W-96-30)//2
for i,(h,big,lines,c) in enumerate([('분양 옵션','165만원',['3연동 슬라이딩','틀 · 레일 상자 포함','공간 나눔 용도'],ACC2),('입주 뒤에 달기','55만~90만원대',['3연동 기준','+ 틀 새로 세우는 비용','문 종류 · 유리 고르기'],ACC)]):
    x=48+i*(cw+30); d.rounded_rectangle((x,190,x+cw,600),18,fill='white',outline=LINE,width=3)
    d.rectangle((x,190,x+cw,200),fill=c)
    d.text((x+32,226),h,font=F(32),fill=MUT); d.text((x+32,278),big,font=F(52),fill=c)
    for k,t in enumerate(lines): d.text((x+32,380+k*62),'· '+t,font=F(32),fill=INK)
d.text((48,622),'옵션을 안 고른 집은 중문틀이 없습니다 — 견적은 틀까지 넣어 비교',font=F(26),fill=INK)
im.save('fig2_jungmun.png')
# 3) 사전점검 5곳
items=[('현관','폭 · 높이 · 양옆 수납장','중문 틀 자리'),('에어컨 배관','거실 · 침실 위치','실내기 놓을 곳'),('욕실','줄눈 · 실리콘','줄눈 넣을지'),('냉장고장','폭 · 깊이','냉장고 사기 전'),('확장 창 둘레','실리콘 빠진 곳','결로 하자 접수')]
im,d=base(900,'청주 신영지웰푸르지오센트럴 · 사전점검','옵션 안 고른 집이 재고 찍을 5곳')
y=190
for k,(a,b,c) in enumerate(items):
    d.ellipse((48,y,108,y+60),fill=ACC); n=str(k+1); d.text((78-d.textlength(n,font=F(34))/2,y+6),n,font=F(34),fill='white')
    d.text((132,y-2),a,font=F(38),fill=INK); d.text((132,y+50),b,font=F(28,False),fill=MUT)
    tw=d.textlength(c,font=F(30)); d.rounded_rectangle((W-48-tw-36,y+8,W-48,y+58),25,fill='#E6F1EC'); d.text((W-48-tw-18,y+12),c,font=F(30),fill=ACC)
    y+=128
im.save('fig3_jeomgeom.png')
