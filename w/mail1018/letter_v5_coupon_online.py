# 우편 편지 두 쪽 (10/18 05:06 사용자 「글씨가 너무 작아 3장으로 만들까?」 → 편지 2쪽 + 손님 전단 1쪽 = 3장, 글씨 크게)
# 이전 판: letter_v3_pre_3page.py (1쪽 · 쿠폰 포함) · letter_v2_pre_coupon.py
import sys, json, os, re, qrcode
from PIL import Image, ImageDraw, ImageFont
DPI=300; mm=lambda v:int(round(v/25.4*DPI)); W,H=mm(210),mm(297)
NAVY=(31,56,100); INK=(15,17,22); GREY=(52,58,68); LINE=(220,224,230); GOLD=(190,140,30); SOFT=(246,247,249)
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/opentype/noto/NotoSansCJK-{w}.ttc',s,index=1)
M=mm(18)

def _wrap(d,t,f,width,col,lh,yy,xx):
    line=''
    for wd in t.split(' '):
        if line and d.textlength(line+wd,font=f)>width: d.text((xx,yy),line.rstrip(),font=f,fill=col); yy+=lh; line=''
        line+=wd+' '
    d.text((xx,yy),line.rstrip(),font=f,fill=col); return yy+lh

def _header(d,sub):
    y=M
    d.text((M,y),'낭만 인테리어',font=F('Bold',56),fill=NAVY); f=F('Medium',38); d.text((W-M-d.textlength(sub,font=f),y+14),sub,font=f,fill=GREY)
    y+=100; d.line([M,y,W-M,y],fill=NAVY,width=6); return y+70

def _qr(data,size,ec=qrcode.constants.ERROR_CORRECT_M):
    q=qrcode.QRCode(border=0,box_size=10,error_correction=ec); q.add_data(data); q.make(fit=True)
    return q.make_image(fill_color=NAVY,back_color='white').convert('RGB').resize((size,size),Image.NEAREST)

def page1(x):
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); wr=lambda t,f,w,c,lh,yy,xx=M:_wrap(d,t,f,w,c,lh,yy,xx)
    two=x.get('mode')=='two'
    y=_header(d,'입주 · 이사 손님 소개 제휴 안내  1/2')
    d.text((M,y),x['office'],font=F('Bold',54),fill=INK); y+=86
    d.text((M,y),f"{x['ceo']} 대표님께",font=F('Black',76),fill=INK); y+=130
    dj=x['danji'].split(' (')[0]
    body=["안녕하세요. 네이버 블로그 「낭만 부동산 분석 플랫폼」과 「낭만 인테리어」를 운영하는 김동진입니다.",
          (f"{dj} 입주 2년, 첫 전세 만기 이사철을 맞아 사무소에 들르는 집주인 · 세입자 손님께 건넬 안내를 함께 보내 드립니다." if two else f"{dj} 입주가 한창인 지금, 사무소에 들르는 입주 · 이사 손님께 건넬 안내를 함께 보내 드립니다."),
          "블로그에서 경기 입주 단지의 시세 · 분양 · 전세 분석 글을 꾸준히 씁니다. 이 글을 보고 찾아오는 손님을 대표님 사무소와 함께 맞이하고 싶습니다.",
          ("손님이 셋째 장 카드의 QR을 찍으면 저희에게 바로 문자가 옵니다. 집 수리 · 이사 청소 · 필름 · 줄눈처럼 따로 찾기 번거로운 공사를" if two else "손님이 셋째 장 카드의 QR을 찍으면 저희에게 바로 문자가 옵니다. 중문 · 입주청소 · 줄눈 · 매트처럼 따로 찾기 번거로운 공사를")+" 시공 사례 금액과 맞춰 보고, 검증한 제휴 시공팀 한두 곳에 연결합니다."]
    for b in body: y=wr(b,F('Medium',58),W-2*M,INK,90,y); y+=26
    y+=30
    d.text((M,y),'대표님께 드리는 것',font=F('Bold',60),fill=NAVY); y+=105
    pts=[('소개비','계약되면 저희가 받는 소개 수수료의 절반을 매달 정산해 드립니다'),
         ('온라인 쿠폰','잔금 날 손님께 카톡으로 보내실 사무소 이름이 든 쿠폰을 드립니다'),
         ('번거로움 없음','연락처는 넘기실 필요 없고, 견적 비교와 거절 연락은 저희가 합니다'),
         ('없는 품목만','이미 거래하시는 곳이 있는 품목은 빼고 쓰셔도 됩니다')]
    for a,b in pts:
        y0=y; d.text((M+36,y+4),a,font=F('Bold',56),fill=INK)
        y=wr(b,F('Medium',54),W-2*M-460,INK,78,y+6,M+460); y=max(y,y0+86); d.rectangle([M,y0+8,M+12,y-10],fill=GOLD); y+=18
    # 블로그 QR 두 개 (아래)
    qs=300; yq=H-M-qs-20
    assert yq>y+20,('p1',x['code'],y,yq)
    d.text((M,yq-90),'블로그에서 먼저 보세요',font=F('Bold',52),fill=NAVY)
    half=(W-2*M)//2
    for i,(nm,sub,url) in enumerate([('낭만 부동산 분석 플랫폼','시세 · 분양 · 전세 분석','https://blog.naver.com/dong_jin_kim'),('낭만 인테리어','시공 사례 · 견적 비교','https://blog.naver.com/champion_chart')]):
        qx=M+i*half; im.paste(_qr(url,qs),(qx,yq))
        tx=qx+qs+34; d.text((tx,yq+10),nm.replace(' 분석 플랫폼',''),font=F('Bold',44),fill=NAVY)
        if '분석' in nm: d.text((tx,yq+66),'분석 플랫폼',font=F('Bold',44),fill=NAVY); oy=yq+130
        else: oy=yq+70
        d.text((tx,oy),sub,font=F('Medium',36),fill=INK); d.text((tx,oy+54),url.replace('https://blog.naver.com/',''),font=F('Medium',34),fill=GREY)
    return im

def page2(x):
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); wr=lambda t,f,w,c,lh,yy,xx=M:_wrap(d,t,f,w,c,lh,yy,xx)
    two=x.get('mode')=='two'
    y=_header(d,'소개비 · 온라인 쿠폰 안내  2/2')
    d.text((M,y),'소개비 예시',font=F('Bold',60),fill=NAVY); y+=105
    rows=[('품목','계약 금액','소개비'),('중문','150만원','7만 5천원'),('필름','300만원','7만 5천원'),('창틀 코킹','80만원','4만원'),('강아지 · 층간소음 매트','건당','7만 5천원')]
    cw=[(W-2*M)*r for r in (0.48,0.26,0.26)]; rh=100
    for i,r in enumerate(rows):
        xx=M
        if i==0: d.rectangle([M,y,W-M,y+rh],fill=SOFT)
        for j,c in enumerate(r):
            d.text((xx+26,y+24),c,font=F('Bold' if i==0 or j==2 else 'Medium',50),fill=NAVY if (j==2 and i) else INK); xx+=cw[j]
        y+=rh; d.line([M,y,W-M,y],fill=LINE,width=3)
    y+=26; y=wr('품목과 시공팀마다 비율이 다릅니다. 실제 금액은 계약서 금액으로 정산합니다.',F('Medium',42),W-2*M,GREY,60,y); y+=50
    cn=x['code'].replace('-','')
    items='집 수리 · 이사 청소 · 필름 · 줄눈·탄성 · 매트 · 중문' if two else '중문 · 입주청소 · 줄눈 · 매트'
    d.text((M,y),'입주 준비 온라인 쿠폰',font=F('Bold',60),fill=NAVY); y+=100
    gist=("전세 계약 · 잔금 날 손님께 카톡으로 보내실 쿠폰을 드립니다." if two else "잔금 날 손님께 카톡으로 보내실 쿠폰을 드립니다.")+" 쿠폰에 대표님 사무소 이름이 크게 들어가 사무소가 드리는 선물이 됩니다. 인쇄할 것도, 챙겨 둘 카드도 없습니다."
    y=wr(gist,F('Medium',50),W-2*M,INK,74,y); y+=24
    ops=['문자 한 통 주시면 사무소 이름이 든 쿠폰을 카톡으로 보내 드립니다','잔금 날 손님께 그 쿠폰을 카톡으로 전달만 하시면 됩니다',f'손님이 쿠폰 QR을 찍으면 대표님 코드({cn})가 담긴 문자가 저희에게 옵니다','손님은 두 곳 견적을 먼저 받고, 계약 때 쿠폰을 보여 주면 할인 혜택을 받습니다','코드로 대표님 손님인지 바로 확인하고, 계약되면 소개비를 드립니다']
    for k,o in enumerate(ops,1):
        d.ellipse([M,y+6,M+64,y+70],fill=NAVY); n=str(k); f=F('Bold',42); d.text((M+32-d.textlength(n,font=f)/2,y+6),n,font=f,fill='white')
        y=wr(o,F('Medium',48),W-2*M-96,INK,70,y,M+96); y+=14
    y+=20
    # 카드 견본 (가운데 · 크게) + 연락 상자
    bh=mm(44); by=H-M-bh
    cdw,cdh=1100,560; cdx=(W-cdw)//2; cy0=y
    assert cy0+cdh+60<by-30,('p2',x['code'],cy0,by)
    d.rounded_rectangle([cdx,cy0,cdx+cdw,cy0+cdh],radius=24,fill='white',outline=NAVY,width=5); d.rectangle([cdx+5,cy0+5,cdx+cdw-5,cy0+22],fill=GOLD)
    on=re.sub(r'\(.*?\)','',x['office']).strip(); last=on[-1]; jo='이' if (0xAC00<=ord(last)<=0xD7A3 and (ord(last)-0xAC00)%28) else '가'
    lt=on+jo+' 드리는'; fs=44
    while d.textlength(lt,font=F('Bold',fs))>cdw-80 and fs>30: fs-=1
    if d.textlength(lt,font=F('Bold',fs))>cdw-80:
        on=on.replace('공인중개사사무소','공인중개사').replace('부동산중개사무소','부동산'); last=on[-1]; jo='이' if (0xAC00<=ord(last)<=0xD7A3 and (ord(last)-0xAC00)%28) else '가'; lt=on+jo+' 드리는'
    d.text((cdx+44,cy0+50),lt,font=F('Bold',fs),fill=NAVY)
    d.text((cdx+44,cy0+112),'입주 준비 쿠폰',font=F('Black',80),fill=INK)
    _wrap(d,items,F('Medium',38),cdw-380,GREY,52,cy0+232,cdx+44)
    d.text((cdx+44,cy0+cdh-150),f'쿠폰 코드 {cn}',font=F('Bold',48),fill=GOLD)
    d.text((cdx+44,cy0+cdh-82),'계약 때 할인 혜택 · 낭만 인테리어',font=F('Medium',36),fill=INK)
    qs3=250; im.paste(_qr(f'SMSTO:01028828165:[{cn}] 입주 준비 쿠폰 문의 / 단지: / 품목: ',qs3,qrcode.constants.ERROR_CORRECT_L),(cdx+cdw-44-qs3,cy0+cdh-44-qs3))
    t='견본 · 카톡으로 보내는 쿠폰 이미지'; f=F('Medium',36); d.text((cdx+cdw-d.textlength(t,font=f),cy0+cdh+14),t,font=f,fill=GREY)
    # 연락
    d.rounded_rectangle([M,by,W-M,by+bh],radius=30,fill=SOFT)
    d.text((M+56,by+52),'오른쪽 QR을 찍어 문자 한 통 주세요',font=F('Bold',50),fill=INK)
    d.text((M+56,by+132),'010-2882-8165',font=F('Black',112),fill=NAVY)
    d.text((M+56,by+290),'사무소 이름이 담긴 문자가 바로 열립니다 · 김동진',font=F('Medium',40),fill=GREY)
    msg=f"[{x['code']}] {x['office']}입니다. 보내 주신 우편 잘 받았습니다. 협업 문의드립니다."
    qs=bh-170; im.paste(_qr('SMSTO:01028828165:'+msg,qs,qrcode.constants.ERROR_CORRECT_L),(W-M-56-qs,by+50))
    t=f"QR을 찍으면 문자가 열립니다 · {x['code']}"; f=F('Medium',32); d.text((W-M-36-d.textlength(t,font=f),by+66+qs),t,font=f,fill=GREY)
    return im

def page(x,OD):
    """두 쪽을 그려 경로 두 개를 돌려준다."""
    out=[]
    for k,fn in ((1,page1),(2,page2)):
        p=os.path.join(OD,f"letter_{x['code']}_p{k}.png"); fn(x).save(p,dpi=(DPI,DPI)); out.append(p)
    return out

if __name__=='__main__':
    L=json.load(open('list.json')); OD=sys.argv[1]; os.makedirs(OD,exist_ok=True)
    for x in L: page(x,OD)
