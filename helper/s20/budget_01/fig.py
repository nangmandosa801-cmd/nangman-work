import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_budget_01_'
J=json.load(open('ana.json')); C=J['calc']; T=J['total']; SD=J['sido']; H=J['hanam']['total']
def uk(v):
    a,b=divmod(int(round(v)),10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
SRC='국토교통부 아파트 매매 실거래 · 2026년 8~10월 계약 · 전용 84㎡ · 59㎡ · 해제 거래 · 직거래 뺌 · 11월 12일 내려받음'
# 1. 숫자 카드 3개
cards3('img/'+S+'1_cards.png','모은 돈 2억 · 월 250만원이면 집값은 '+uk(C['price'])+'까지',
       [(uk(C['price']),'살 수 있는 집값 상한',True,'생애최초 · 집값의 70%까지 대출'),
        (f"{T['all']['pct']}%",'수도권 84㎡ · 59㎡ 거래 중 상한 아래',False,f"{T['all']['n']:,}건 중 {T['all']['k']:,}건"),
        (f"{SD['서울']['allnew']['pct']}%",'서울 2012년 이후 준공만 보면',False,f"{SD['서울']['allnew']['n']:,}건 중 {SD['서울']['allnew']['k']}건")],
       note=SRC)
# 2. 막대 4개 — 상한 아래 거래 비율
it=[('서울',SD['서울']['all']['pct'],f"{SD['서울']['all']['pct']}%",True),
    ('하남',H['all']['pct'],f"{H['all']['pct']}%",False),
    ('경기',SD['경기']['all']['pct'],f"{SD['경기']['all']['pct']}%",False),
    ('인천',SD['인천']['all']['pct'],f"{SD['인천']['all']['pct']}%",False)]
bars('img/'+S+'2_sido.png',f"{uk(C['price'])} 아래 거래, 서울은 100건 중 13건",it,
     note='84㎡ · 59㎡ 매매 실거래 · 2026년 8~10월 계약 · 해제 거래 · 직거래 뺌')
# 썸네일 C형
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 내 조건으로 찾는 집 1편',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,355),'모은 돈 2억',font=kr(ser_,84),fill='#F4F1EA',anchor='mm')
d.text((W/2,475),'한 달 250만원 갚는 부부',font=kr(ser_,58),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),uk(C['price']),font=kr(ser_,108),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'살 수 있는 집값 상한 · 수도권 거래의 '+f"{T['all']['pct']}%"+' · 서울은 '+f"{SD['서울']['all']['pct']}%",font=kr(san,32),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')
