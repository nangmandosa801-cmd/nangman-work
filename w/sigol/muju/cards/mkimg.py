"""팜 에디터 무주 천마 그림(썸네일 + 정보 카드). python3 mkimg.py — 꿀 공부 카드와 같은 색 · 글꼴"""
import pathlib
from playwright.sync_api import sync_playwright
D = pathlib.Path(__file__).parent
F = "font-family:'Noto Sans CJK KR'"
C = dict(bg='#F6F1E4', ink='#3F4A36', g='#5E7552', lg='#7E9470', gold='#B08A4A', pale='#EFE6D2', line='#E2D8C2', gray='#8A8270', red='#B5523B', root='#E9C9A0')
def img(n): return 'file://' + str(D / n)
def page(inner, h=1080):
    return f'''<meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:{h}px;background:{C["bg"]};{F};color:{C["ink"]}}}b{{color:{C["red"]}}}</style>
<div style="position:relative;width:1080px;height:{h}px;overflow:hidden">{inner}</div>'''
def card(head, body, src=''):
    return page(f'''<div style="position:absolute;inset:0;padding:70px 70px 60px;display:flex;flex-direction:column">
 <div style="display:flex;align-items:center;gap:14px;font-size:30px;color:{C['gold']};font-weight:700"><span style="width:46px;height:4px;background:{C['gold']}"></span>무주 안성 천마</div>
 <div style="font-size:64px;font-weight:700;line-height:1.22;margin-top:22px;letter-spacing:-1px">{head}</div>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:center">{body}</div>
 <div style="display:flex;justify-content:space-between;font-size:24px;color:{C['gray']};border-top:2px solid {C['line']};padding-top:18px"><span>{src}</span><span>팜 에디터</span></div></div>''')
def pill(t, bg, fs=34): return f'<span style="display:inline-block;background:{bg};color:#fff;font-size:{fs}px;font-weight:700;padding:10px 26px;border-radius:40px">{t}</span>'
IM = {}
IM['t01.jpg'] = page(f'''<img src="{img('saeng_clean.jpg')}" style="position:absolute;inset:0;width:1080px;height:1080px;object-fit:cover;filter:brightness(.92)">
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(transparent,rgba(40,46,34,.92) 45%)"></div>
<div style="position:absolute;top:44px;left:50px;font-size:30px;color:#fff;background:rgba(63,74,54,.85);padding:10px 22px;border-radius:30px">팜 에디터</div>
<div style="position:absolute;left:70px;right:70px;bottom:80px;color:#fff">
 <div style="font-size:50px;font-weight:500;color:#F3DDB4">무주 안성천마작목반 · 11월 햇천마</div>
 <div style="font-size:132px;font-weight:700;line-height:1.05;margin-top:12px;letter-spacing:-2px">생천마 가격</div>
 <div style="font-size:70px;font-weight:700;margin-top:18px">5kg <span style="color:#F2C14E">15만 원</span>부터</div></div>''')
IM['t02.jpg'] = card('생천마 · 건천마 가격', ''.join(f'''<div style="display:flex;align-items:center;gap:26px;background:#fff;border-radius:24px;padding:16px 26px;margin:11px 0;border:3px solid {C['line']}">
 <img src="{img(p)}" style="width:150px;height:150px;object-fit:cover;border-radius:16px"><div style="flex:1;font-size:38px;font-weight:700">{n}<div style="font-size:28px;font-weight:400;color:{C['gray']}">{s}</div></div>
 <div style="font-size:48px;font-weight:700;color:{C['g']}">{v}</div></div>''' for p,n,s,v in [
 ('saeng_jung.jpg','생천마 중품','5kg 한 상자','150,000원'),('saeng_sang.jpg','생천마 상품','5kg 한 상자','175,000원'),
 ('geon_sseol.jpg','건천마','1kg · 썰어서 말린 것','160,000원'),('geon_tong.jpg','건천마','1kg · 통째로 말린 것','180,000원')]), '작목반 쇼핑몰 판매가 기준')
mon = ''.join(f'<div style="width:150px;height:118px;margin:8px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700;{("background:"+C["g"]+";color:#fff") if m in (4,11) else ("background:#fff;color:"+C["gray"]+";border:3px solid "+C["line"])}">{m}월</div>' for m in range(1,13))
IM['t03.jpg'] = card('천마 수확시기는<br>봄 4월 · 가을 11월', f'''<div style="display:flex;flex-wrap:wrap;width:1000px;margin-left:-8px">{mon}</div>
 <div style="font-size:36px;line-height:1.5;margin-top:26px">천마는 보통 <b>2년에 한 번</b> 캡니다.<br>작목반은 해마다 봄 · 가을 두 번 캐서 냅니다.</div>''', '무주 안성천마작목반 쇼핑몰 「직접 수확」')
def col(p,t,lines,c): return f'''<div style="flex:1;background:#fff;border-radius:28px;padding:26px;border:4px solid {c}"><img src="{img(p)}" style="width:100%;height:270px;object-fit:cover;border-radius:18px">
 <div style="margin-top:20px">{pill(t,c)}</div><div style="margin-top:16px;font-size:34px;line-height:1.55">{lines}</div></div>'''
IM['t04.jpg'] = card('생천마와 건천마,<br>무엇이 다를까요?', f'''<div style="display:flex;gap:24px">{col('saeng_clean.jpg','생천마','캔 그대로 보냄<br>5kg 상자<br>15만 · 17.5만 원',C['g'])}{col('geon_sseol.jpg','건천마','말려서 보냄<br>1kg · 썬 것 / 통째<br>16만 · 18만 원',C['gold'])}</div>''', '작목반 쇼핑몰 상품 기준')
def bar(lab,v,w,c,n): return f'''<div style="margin:24px 0"><div style="font-size:40px;font-weight:700;margin-bottom:12px">{lab}</div><div style="display:flex;align-items:center;gap:20px"><div style="width:{w}px;height:96px;background:{c};border-radius:14px;display:flex;align-items:center;padding-left:26px;color:#fff;font-size:48px;font-weight:700">{v}</div><span style="font-size:30px;color:{C['gray']}">{n}</span></div></div>'''
IM['t05.jpg'] = card('1년 만에 4분의 1로<br>떨어진 천마 값', bar('1997년','14,500원',800,C['g'],'')+bar('1998년','3,500원',200,C['red'],'')+f'<div style="font-size:36px;line-height:1.5;margin-top:18px">그때 천마는 한약재로만 분류돼 있었습니다.<br>식품으로 바뀐 뒤 즙 · 가루 · 말린 천마가 나왔습니다.</div>', '조규식 대표 「천마 이야기」')
tl=[('1991','농협 견학에서 천마를 처음 만남'),('첫 재배','무주 200평에 심었다가 실패'),('1998','천마 값 3,500원까지 떨어짐'),('2007','첫 무주 천마축제'),('2009','무주천마 향토산업사업단'),('2011','신지식농업인 선정 · 재배 방법 표준화')]
IM['t06.jpg'] = card('조규식 대표의 천마 30여 년', ''.join(f'''<div style="display:flex;align-items:center;gap:26px;margin:10px 0"><div style="width:180px;text-align:right;font-size:40px;font-weight:700;color:{C['gold']}">{y}</div><div style="width:22px;height:22px;border-radius:50%;background:{C['g']}"></div><div style="font-size:36px">{t}</div></div>''' for y,t in tl), '작목반 쇼핑몰 · 2018 전라북도 블로그 인터뷰')
def num(n,u,t): return f'<div style="flex:1;background:#fff;border-radius:28px;padding:34px 20px;text-align:center;border:3px solid {C["line"]}"><div style="font-size:92px;font-weight:700;color:{C["g"]}">{n}<span style="font-size:42px">{u}</span></div><div style="font-size:32px;margin-top:8px;line-height:1.4">{t}</div></div>'
IM['t07.jpg'] = card('숫자로 보는<br>무주 안성천마작목반', f'<div style="display:flex;gap:22px">{num("250","여 명","작목반원")}{num("137","명","돈을 모아<br>가공공장을 세운 농민")}</div><div style="display:flex;gap:22px;margin-top:22px">{num("2","번","한 해 수확<br>4월 · 11월")}{num("1","년","하우스 재배로<br>2년을 1년에")}</div>', '작목반 쇼핑몰 「천마 이야기」')
st=[('1','주문서 작성','팜 에디터 주문서'),('2','입금 안내 문자','택배비 함께 안내'),('3','입금 확인',''),('4','작목반 발송','무주에서 바로')]
IM['t08.jpg'] = card('생천마 주문은 이렇게', ''.join(f'''<div style="display:flex;align-items:center;gap:28px;background:#fff;border-radius:24px;padding:24px 32px;margin:10px 0;border:3px solid {C['line']}"><div style="width:84px;height:84px;border-radius:50%;background:{C['g']};color:#fff;font-size:46px;font-weight:700;display:flex;align-items:center;justify-content:center">{a}</div><div style="font-size:44px;font-weight:700">{b}<div style="font-size:30px;font-weight:400;color:{C['gray']}">{c}</div></div></div>''' for a,b,c in st), '팜 에디터 주문 흐름')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1080})
    for out, html in IM.items():
        t = D / '_t.html'; t.write_text(html, encoding='utf-8'); pg.goto('file://' + str(t)); pg.wait_for_timeout(400)
        pg.screenshot(path=str(D / '_t.png'))
        from PIL import Image
        Image.open(D / '_t.png').convert('RGB').save(D / out, quality=90); print(out)
    b.close()
