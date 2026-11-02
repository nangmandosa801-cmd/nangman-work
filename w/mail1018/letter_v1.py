# 우편 1쪽 「중개사님께」 (사용자 10/18 「지금 보내야 할 단지 그리고 중개사 같이 넣어서 만들어 줘 바로 e그린 우편으로 보내 보게」)
import sys, json, os, qrcode
from PIL import Image, ImageDraw, ImageFont
DPI=300; mm=lambda v:int(round(v/25.4*DPI)); W,H=mm(210),mm(297)
NAVY=(31,56,100); INK=(36,40,48); GREY=(112,120,132); LINE=(220,224,230); GOLD=(201,152,45); SOFT=(246,247,249)
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/opentype/noto/NotoSansCJK-{w}.ttc',s,index=1)
def page(x,OD):
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); M=mm(20); y=M
    def wrap(t,f,width,col,lh,yy,xx=M):
        line=''
        for wd in t.split(' '):
            if d.textlength(line+wd,font=f)>width: d.text((xx,yy),line.rstrip(),font=f,fill=col); yy+=lh; line=''
            line+=wd+' '
        d.text((xx,yy),line.rstrip(),font=f,fill=col); return yy+lh
    d.text((M,y),'낭만 인테리어',font=F('Bold',44),fill=NAVY); t='입주 · 이사 손님 소개 제휴 안내'; f=F('Regular',30); d.text((W-M-d.textlength(t,font=f),y+12),t,font=f,fill=GREY)
    y+=90; d.line([M,y,W-M,y],fill=NAVY,width=5); y+=70
    ceo=x['ceo']; d.text((M,y),f"{x['office']}",font=F('Bold',44),fill=INK); y+=70
    d.text((M,y),f"{ceo} 대표님께",font=F('Bold',58),fill=INK); y+=120
    body=[f"안녕하세요. 네이버 블로그 「낭만 부동산 분석 플랫폼」과 「낭만 인테리어」를 운영하는 김동진입니다.",
          f"{x['danji'].split(' (')[0]} "+'입주가 한창인 지금'+", 대표님 사무소에 들르는 입주 · 이사 손님께 건넬 안내 한 장을 함께 보내 드립니다.",
          "낭만 부동산 분석 플랫폼에서는 경기 입주 단지의 시세 · 분양 · 전세 분석 글을 꾸준히 쓰고 있고, 검색 노출과 독자 문의도 꾸준히 이어지고 있습니다. 이 글을 보고 찾아오는 손님을 대표님 사무소와 함께 맞이하고 싶습니다.",
          "손님이 뒷장 아래 카드의 QR을 찍으면 저희에게 바로 문자가 옵니다. 중문 · 입주청소 · 줄눈 · 매트처럼 따로 찾기 번거로운 공사를, 저희가 시공 사례 금액과 맞춰 보고 검증한 제휴 시공팀 한두 곳으로 연결합니다."]
    for b in body: y=wrap(b,F('Regular',39),W-2*M,INK,64,y); y+=30
    y+=20
    d.text((M,y),'대표님께 드리는 것',font=F('Bold',46),fill=NAVY); y+=85
    pts=[('소개비','계약이 되면 저희가 시공팀에게서 받는 소개 수수료의 절반을 드립니다. 매달 정산합니다.'),
         ('번거로움 없음','손님 연락처를 넘기실 필요가 없습니다. 카드만 건네시면 손님이 직접 문자합니다.'),
         ('없는 품목만','이미 거래하는 업체가 있는 품목은 빼고, 없는 품목만 이 카드로 쓰셔도 됩니다.'),
         ('손님 편의','견적 비교와 거절 연락은 저희가 대신합니다. 비교 · 연결은 손님에게 무료입니다.')]
    for a,b in pts:
        d.rectangle([M,y+8,M+10,y+92],fill=GOLD); d.text((M+34,y+4),a,font=F('Bold',38),fill=INK)
        y=wrap(b,F('Regular',34),W-2*M-340,GREY,52,y+8,M+340); y+=44
    y+=10
    d.text((M,y),'소개비 예시',font=F('Bold',46),fill=NAVY); y+=85
    rows=[('품목','계약 금액','대표님 소개비'),('중문','150만원','7만 5천원'),('창틀 코킹','80만원','4만원'),('필름','300만원','7만 5천원'),('강아지 · 층간소음 매트','건당','7만 5천원')]
    cw=[(W-2*M)*r for r in (0.46,0.27,0.27)]; rh=92
    for i,r in enumerate(rows):
        xx=M
        if i==0: d.rectangle([M,y,W-M,y+rh],fill=SOFT)
        for j,c in enumerate(r):
            d.text((xx+24,y+22),c,font=F('Bold' if i==0 or j==2 else 'Regular',35),fill=NAVY if (j==2 and i) else INK); xx+=cw[j]
        y+=rh; d.line([M,y,W-M,y],fill=LINE,width=3)
    y+=24; d.text((M,y),'품목과 시공팀마다 비율이 다릅니다. 실제 금액은 계약서 금액으로 정산합니다.',font=F('Regular',30),fill=GREY); y+=110
    d.text((M,y),'이렇게 쓰시면 됩니다',font=F('Bold',46),fill=NAVY); y+=95
    st=[('1','뒷장을 손님께','카드 부분만 잘라 드려도 됩니다'),('2','손님이 QR로 문자','코드가 문자에 저절로 들어갑니다'),('3','계약되면 알림 · 정산','동네 · 품목 · 소개비를 문자로')]
    sw=(W-2*M-2*30)//3
    for i,(n,a,b) in enumerate(st):
        xx=M+i*(sw+30); d.ellipse([xx,y,xx+76,y+76],fill=NAVY); tw=d.textlength(n,font=F('Bold',42)); d.text((xx+38-tw/2,y+10),n,font=F('Bold',42),fill='white')
        d.text((xx+96,y+4),a,font=F('Bold',34),fill=INK); d.text((xx+96,y+58),b,font=F('Regular',25),fill=GREY)
    y+=130
    # 연락
    bh=mm(44); by=H-M-bh
    d.rounded_rectangle([M,by,W-M,by+bh],radius=28,fill=SOFT)
    d.text((M+50,by+46),'오른쪽 QR을 찍어 문자 한 통 주세요',font=F('Bold',40),fill=INK)
    d.text((M+50,by+112),'010-2882-8165',font=F('Black',92),fill=NAVY)
    d.text((M+50,by+240),f"사무소 이름이 담긴 문자가 바로 열립니다 · 김동진",font=F('Regular',32),fill=GREY)
    d.text((M+50,by+300),'낭만 부동산 분석 플랫폼 blog.naver.com/dong_jin_kim  ·  낭만 인테리어 blog.naver.com/champion_chart',font=F('Regular',28),fill=GREY)
    msg=f"[{x['code']}] {x['office']}입니다. 보내 주신 우편 잘 받았습니다. 협업 문의드립니다."
    q=qrcode.QRCode(border=0,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_L); q.add_data('SMSTO:01028828165:'+msg); q.make(fit=True)
    qs=bh-150; qi=q.make_image(fill_color=NAVY,back_color='white').convert('RGB').resize((qs,qs),Image.NEAREST)
    qx=W-M-50-qs; im.paste(qi,(qx,by+50))
    t=f"QR을 찍으면 문자가 열립니다 · {x['code']}"; f=F('Regular',26); d.text((qx+qs/2-d.textlength(t,font=f)/2,by+60+qs),t,font=f,fill=GREY)
    assert y<by-20,(x['code'],y,by)
    p=os.path.join(OD,f"letter_{x['code']}.png"); im.save(p,dpi=(DPI,DPI)); return p
if __name__=='__main__':
    L=json.load(open('list.json')); OD=sys.argv[1]; os.makedirs(OD,exist_ok=True)
    for x in L: page(x,OD)
