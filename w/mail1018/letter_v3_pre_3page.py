# 우편 1쪽 「중개사님께」 (사용자 10/18 「지금 보내야 할 단지 그리고 중개사 같이 넣어서 만들어 줘 바로 e그린 우편으로 보내 보게」)
import sys, json, os, re, qrcode
from PIL import Image, ImageDraw, ImageFont
DPI=300; mm=lambda v:int(round(v/25.4*DPI)); W,H=mm(210),mm(297)
NAVY=(31,56,100); INK=(15,17,22); GREY=(52,58,68); LINE=(220,224,230); GOLD=(201,152,45); SOFT=(246,247,249)
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
    d.text((M,y),f"{ceo} 대표님께",font=F('Bold',58),fill=INK); y+=104
    body=[f"안녕하세요. 네이버 블로그 「낭만 부동산 분석 플랫폼」과 「낭만 인테리어」를 운영하는 김동진입니다.",
          (f"{x['danji'].split(' (')[0]} 입주 2년, 첫 전세 만기 이사철을 맞아 대표님 사무소에 들르는 집주인 · 세입자 손님께 건넬 안내 한 장을 함께 보내 드립니다." if x.get('mode')=='two' else f"{x['danji'].split(' (')[0]} "+'입주가 한창인 지금'+", 대표님 사무소에 들르는 입주 · 이사 손님께 건넬 안내 한 장을 함께 보내 드립니다."),
          "블로그에서 경기 입주 단지의 시세 · 분양 · 전세 분석 글을 꾸준히 씁니다. 이 글을 보고 찾아오는 손님을 대표님 사무소와 함께 맞이하고 싶습니다.",
          ("손님이 뒷장 아래 카드의 QR을 찍으면 저희에게 바로 문자가 옵니다. 나가는 집 수리 · 이사 청소 · 필름 · 줄눈처럼 따로 찾기 번거로운 공사를," if x.get('mode')=='two' else "손님이 뒷장 아래 카드의 QR을 찍으면 저희에게 바로 문자가 옵니다. 중문 · 입주청소 · 줄눈 · 매트처럼 따로 찾기 번거로운 공사를,")+" 저희가 시공 사례 금액과 맞춰 보고 검증한 제휴 시공팀 한두 곳으로 연결합니다."]
    for b in body: y=wrap(b,F('Medium',45),W-2*M,INK,68,y); y+=14
    y+=20
    d.text((M,y),'대표님께 드리는 것',font=F('Bold',46),fill=NAVY); y+=85
    pts=[('소개비','계약되면 저희가 받는 소개 수수료의 절반을 매달 정산해 드립니다'),
         ('번거로움 없음','연락처는 넘기실 필요 없고, 견적 비교와 거절 연락은 저희가 합니다'),
         ('없는 품목만','이미 거래하시는 곳이 있는 품목은 빼고 쓰셔도 됩니다')]
    for a,b in pts:
        y0=y; d.text((M+34,y+4),a,font=F('Bold',42),fill=INK)
        y=wrap(b,F('Medium',40),W-2*M-350,INK,58,y+4,M+350); y=max(y,y0+64); d.rectangle([M,y0+8,M+10,y-6],fill=GOLD); y+=12
    y+=10
    d.text((M,y),'소개비 예시',font=F('Bold',46),fill=NAVY); y+=85
    rows=[('품목','계약 금액','대표님 소개비'),('중문','150만원','7만 5천원'),('필름','300만원','7만 5천원'),('강아지 · 층간소음 매트','건당','7만 5천원')]
    cw=[(W-2*M)*r for r in (0.46,0.27,0.27)]; rh=80
    for i,r in enumerate(rows):
        xx=M
        if i==0: d.rectangle([M,y,W-M,y+rh],fill=SOFT)
        for j,c in enumerate(r):
            d.text((xx+24,y+22),c,font=F('Bold' if i==0 or j==2 else 'Medium',42),fill=NAVY if (j==2 and i) else INK); xx+=cw[j]
        y+=rh; d.line([M,y,W-M,y],fill=LINE,width=3)
    y+=24; d.text((M,y),'품목과 시공팀마다 비율이 다릅니다. 실제 금액은 계약서 금액으로 정산합니다.',font=F('Medium',34),fill=GREY); y+=72
    # 입주 준비 쿠폰 카드 (사용자 10/18 04:53~04:55)
    two=x.get('mode')=='two'; cn=x['code'].replace('-','')+'-0001'
    items='집 수리 · 이사 청소 · 필름 · 줄눈·탄성 · 매트 · 중문' if two else '중문 · 입주청소 · 줄눈 · 매트'
    d.text((M,y),'입주 준비 쿠폰 카드',font=F('Bold',46),fill=NAVY)
    t='소개비와 함께 드립니다'; f=F('Bold',34); d.text((M+d.textlength('입주 준비 쿠폰 카드',font=F('Bold',46))+30,y+12),t,font=f,fill=GOLD); y+=82
    gist=("전세 계약 · 잔금 날 손님께 건네실 쿠폰 카드(" if two else "잔금 날 손님께 건네실 쿠폰 카드(")+items+")를 보내 드립니다. 카드에 대표님 사무소 이름과 QR이 들어가 사무소가 드리는 선물이 됩니다. 손님은 고마워하고, 사무소는 이름이 남습니다."
    y=wrap(gist,F('Medium',40),W-2*M,INK,58,y); y+=12
    cdw,cdh=640,346; cdx=W-M-cdw; ops=[('사무소 이름을 넣은 카드 20장을 보내 드립니다'),(f'쿠폰 번호는 대표님 코드로 시작 · 예 {cn}'),('손님은 두 곳 견적을 받고, 계약 때 번호를 말하면 할인 혜택'),('번호로 대표님 손님인지 바로 확인 · 계약되면 소개비'),('카드가 떨어지면 문자 한 통 주세요. 다시 보내 드립니다')]
    oy=y+6; ow=cdx-M-40-70
    for k,o in enumerate(ops,1):
        d.ellipse([M,oy+4,M+50,oy+54],fill=NAVY); n=str(k); tw=d.textlength(n,font=F('Bold',32)); d.text((M+25-tw/2,oy+5),n,font=F('Bold',32),fill='white')
        oy=wrap(o,F('Medium',38),ow,INK,54,oy,M+70); oy+=10
    # 카드 견본
    cy0=y; d.rounded_rectangle([cdx,cy0,cdx+cdw,cy0+cdh],radius=18,fill='white',outline=NAVY,width=4); d.rectangle([cdx+4,cy0+4,cdx+cdw-4,cy0+16],fill=GOLD)
    on=re.sub(r'\(.*?\)','',x['office']).strip()
    last=on[-1]; jo='이' if (0xAC00<=ord(last)<=0xD7A3 and (ord(last)-0xAC00)%28) else '가'
    lt=on+jo+' 드리는'; fs=30
    while d.textlength(lt,font=F('Bold',fs))>cdw-60 and fs>22: fs-=1
    if d.textlength(lt,font=F('Bold',fs))>cdw-60:
        on=on.replace('공인중개사사무소','공인중개사').replace('부동산중개사무소','부동산'); last=on[-1]; jo='이' if (0xAC00<=ord(last)<=0xD7A3 and (ord(last)-0xAC00)%28) else '가'; lt=on+jo+' 드리는'
    d.text((cdx+30,cy0+36),lt,font=F('Bold',fs),fill=NAVY)
    d.text((cdx+30,cy0+78),'입주 준비 쿠폰',font=F('Black',52),fill=INK)
    iy=wrap(items,F('Medium',26),cdw-230,GREY,34,cy0+152,cdx+30)
    d.text((cdx+30,cy0+cdh-104),f'No. {cn}',font=F('Bold',32),fill=GOLD)
    d.text((cdx+30,cy0+cdh-58),'계약 때 할인 혜택 · 낭만 인테리어',font=F('Medium',24),fill=INK)
    q=qrcode.QRCode(border=0,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_L); q.add_data(f'SMSTO:01028828165:[{cn}] 입주 준비 쿠폰 문의 / 품목: '); q.make(fit=True)
    qs3=150; im.paste(q.make_image(fill_color=NAVY,back_color='white').convert('RGB').resize((qs3,qs3),Image.NEAREST),(cdx+cdw-30-qs3,cy0+cdh-30-qs3))
    t='견본 · 실제 카드는 명함 크기'; f=F('Medium',28); d.text((cdx+cdw-d.textlength(t,font=f),cy0+cdh+12),t,font=f,fill=GREY)
    y=max(oy,cy0+cdh+46)
    # 블로그 QR 두 개
    bh=mm(35); by=H-mm(15)-bh
    qs2=210; yq=by-qs2-40
    assert yq>y-10,(x['code'],y,yq)
    half=(W-2*M)//2
    for i,(nm,sub,url) in enumerate([('낭만 부동산 분석 플랫폼','입주 단지 시세 · 분양 · 전세 분석','https://blog.naver.com/dong_jin_kim'),('낭만 인테리어','시공 사례 · 무료 견적 비교','https://blog.naver.com/champion_chart')]):
        qx=M+i*half; q=qrcode.QRCode(border=0,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make(fit=True)
        im.paste(q.make_image(fill_color=NAVY,back_color='white').convert('RGB').resize((qs2,qs2),Image.NEAREST),(qx,yq))
        tx=qx+qs2+36; d.text((tx,yq+8),"블로그 보기",font=F('Medium',28),fill=GOLD)
        d.text((tx,yq+46),nm,font=F('Bold',38),fill=NAVY); d.text((tx,yq+100),sub,font=F('Medium',30),fill=INK); d.text((tx,yq+146),url.replace('https://',''),font=F('Medium',26),fill=GREY)
    # 연락
    d.rounded_rectangle([M,by,W-M,by+bh],radius=28,fill=SOFT)
    d.text((M+50,by+46),'오른쪽 QR을 찍어 문자 한 통 주세요',font=F('Bold',40),fill=INK)
    d.text((M+50,by+112),'010-2882-8165',font=F('Black',92),fill=NAVY)
    d.text((M+50,by+240),f"사무소 이름이 담긴 문자가 바로 열립니다 · 김동진",font=F('Medium',34),fill=GREY)
    msg=f"[{x['code']}] {x['office']}입니다. 보내 주신 우편 잘 받았습니다. 협업 문의드립니다."
    q=qrcode.QRCode(border=0,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_L); q.add_data('SMSTO:01028828165:'+msg); q.make(fit=True)
    qs=bh-150; qi=q.make_image(fill_color=NAVY,back_color='white').convert('RGB').resize((qs,qs),Image.NEAREST)
    qx=W-M-50-qs; im.paste(qi,(qx,by+50))
    t=f"QR을 찍으면 문자가 열립니다 · {x['code']}"; f=F('Medium',28); d.text((W-M-30-d.textlength(t,font=f),by+60+qs),t,font=f,fill=GREY)
    p=os.path.join(OD,f"letter_{x['code']}.png"); im.save(p,dpi=(DPI,DPI)); return p
if __name__=='__main__':
    L=json.load(open('list.json')); OD=sys.argv[1]; os.makedirs(OD,exist_ok=True)
    for x in L: page(x,OD)
