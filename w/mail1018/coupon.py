# 사무소별 온라인 쿠폰 이미지 (카톡으로 보내는 용 · 1080×1350) — python3 coupon.py <코드> [mode]
import sys,json,re
from PIL import Image,ImageDraw
from letter import F,NAVY,INK,GREY,GOLD,SOFT,_qr,_wrap
import qrcode
import sys as _sy; _sy.path.insert(0,'/home/claude/blogkit'); import discount1130 as _D1130   # DISCOUNT1130
def make(x,out):
    two=x.get('mode')=='two'; W,H=1080,1350; im=Image.new('RGB',(W,H),(246,247,249)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([50,50,W-50,H-50],radius=40,fill='white',outline=NAVY,width=6); d.rectangle([56,56,W-56,90],fill=GOLD)
    on=re.sub(r'\(.*?\)','',x['office']).strip(); last=on[-1]; jo='이' if (0xAC00<=ord(last)<=0xD7A3 and (ord(last)-0xAC00)%28) else '가'
    lt=on+jo+' 드리는'; fs=50
    while d.textlength(lt,font=F('Bold',fs))>W-200 and fs>34: fs-=1
    d.text((100,140),lt,font=F('Bold',fs),fill=NAVY)
    d.text((100,215),'입주 준비 쿠폰',font=F('Black',104),fill=INK)
    items=['집 수리','이사 청소','필름','줄눈 · 탄성','매트','중문','포장이사'] if two else ['중문','입주청소','줄눈 · 탄성','매트','포장이사 · 보관이사']
    y=380
    if _D1130.ON:   # DISCOUNT1130 — 할인 줄이 들어가 품목을 두 칸으로 나눠 아래 쿠폰 코드와 겹치지 않게(11/30 뒤에는 원래 한 칸)
        rows=(len(items)+1)//2
        for i,it in enumerate(items):
            xx=100+(i//rows)*450; yy=y+(i%rows)*74
            d.rounded_rectangle([xx,yy+12,xx+44,yy+56],radius=8,fill=NAVY); d.line([(xx+10,yy+35),(xx+20,yy+46),(xx+36,yy+22)],fill='white',width=7)
            d.text((xx+62,yy+2),it,font=F('Bold',46),fill=INK)
        y+=rows*74
    else:
      for it in items:
        d.rounded_rectangle([100,y+12,146,y+58],radius=8,fill=NAVY); d.line([(110,y+36),(121,y+48),(138,y+22)],fill='white',width=7)
        d.text((168,y),it,font=F('Bold',52),fill=INK); y+=78
    y+=24
    LN=['두 곳 견적을 무료로 비교해 드립니다','계약할 때 이 쿠폰을 보여 주시면','할인 혜택을 드립니다']
    if _D1130.ON: LN=['두 곳 견적을 무료로 비교해 드립니다',_D1130.L1,_D1130.L2]   # DISCOUNT1130 (10/19 사용자 · 11/30까지)
    for ln in LN:
        d.text((100,y),ln,font=F('Bold',46),fill=INK); y+=64
    cn=x['code'] if x.get('keep_dash') else x['code'].replace('-','')
    qs=300; im.paste(_qr(f"SMSTO:01028828165:[{cn}] 입주 준비 쿠폰 문의 / 단지: / 품목: ",qs,qrcode.constants.ERROR_CORRECT_L),(W-100-qs,H-120-qs))
    d.text((100,H-420),f'쿠폰 코드 {cn}',font=F('Bold',56),fill=GOLD)
    d.text((100,H-330),'QR을 찍으면 문자가 열립니다',font=F('Medium',38),fill=INK)
    d.text((100,H-270),'010-2882-8165',font=F('Black',72),fill=NAVY)
    d.text((100,H-175),'낭만 인테리어 · 김동진',font=F('Medium',36),fill=GREY)
    im.save(out,quality=92); return out
if __name__=='__main__':
    L=json.load(open('list.json'))+json.load(open('list_two.json'))
    x=next(v for v in L if v['code']==sys.argv[1]); print(make(x,f"/mnt/user-data/outputs/mail1018/coupon/nangman_coupon_{x['code'].replace('-','')}.jpg"))
