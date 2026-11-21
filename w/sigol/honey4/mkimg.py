"""팜 에디터 꿀 공부 4편 그림 (썸네일 + 정보 카드). python3 mkimg.py
글꼴 Noto Sans CJK KR(팜 에디터 썸네일과 같음) · 색: 크림 #F6F1E4 · 녹색 #3F4A36/#5E7552 · 금색 #B08A4A · 꿀색 #E0A43A"""
import pathlib
from playwright.sync_api import sync_playwright
D = pathlib.Path(__file__).parent
F = "font-family:'Noto Sans CJK KR'"
C = dict(bg='#F6F1E4', ink='#3F4A36', g='#5E7552', lg='#7E9470', gold='#B08A4A', hon='#E0A43A', pale='#EFE6D2', line='#E2D8C2', gray='#8A8270', red='#B5523B')

def hexbg(op=.18):
    cells = ''
    for r in range(9):
        for c in range(9):
            x = c * 150 + (75 if r % 2 else 0) - 40; y = r * 130 - 40
            cells += f'<polygon points="{x+75},{y} {x+150},{y+43} {x+150},{y+130} {x+75},{y+173} {x},{y+130} {x},{y+43}" fill="none" stroke="{C["hon"]}" stroke-width="3"/>'
    return f'<svg style="position:absolute;inset:0;opacity:{op}" width="1080" height="1080">{cells}</svg>'

def jar(w=300, fill=C['hon'], crystals=False):
    dots = ''.join(f'<circle cx="{60+ (i*37)%180}" cy="{170+ (i*53)%150}" r="7" fill="#FFF7E6" opacity=".9"/>' for i in range(22)) if crystals else ''
    return f'''<svg width="{w}" height="{w*1.25}" viewBox="0 0 300 375">
 <rect x="70" y="20" width="160" height="40" rx="10" fill="{C['gold']}"/>
 <rect x="85" y="58" width="130" height="22" fill="{C['pale']}" stroke="{C['gold']}" stroke-width="4"/>
 <path d="M60 80 h180 q30 0 30 40 v190 q0 45 -45 45 h-150 q-45 0 -45 -45 v-190 q0 -40 30 -40z" fill="#fff" stroke="{C['gold']}" stroke-width="6"/>
 <path d="M42 150 h216 v160 q0 40 -40 40 h-136 q-40 0 -40 -40z" fill="{fill}"/>{dots}
 <path d="M70 160 q10 60 0 120" stroke="#fff" stroke-width="10" fill="none" opacity=".5" stroke-linecap="round"/>
</svg>'''

def page(inner, h=1080, hexop=.0):
    return f'''<meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:{h}px;background:{C["bg"]};{F};color:{C["ink"]}}}</style>
<div style="position:relative;width:1080px;height:{h}px;overflow:hidden">{hexbg(hexop) if hexop else ''}{inner}</div>'''

def card(n, head, body, src='', h=1080):
    inner = f'''<div style="position:absolute;inset:0;padding:70px 70px 60px;display:flex;flex-direction:column">
 <div style="display:flex;align-items:center;gap:14px;font-size:30px;color:{C['gold']};font-weight:700"><span style="width:46px;height:4px;background:{C['gold']}"></span>꿀 공부 {n}</div>
 <div style="font-size:64px;font-weight:700;line-height:1.22;margin-top:22px;letter-spacing:-1px">{head}</div>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:center">{body}</div>
 <div style="display:flex;justify-content:space-between;font-size:24px;color:{C['gray']};border-top:2px solid {C['line']};padding-top:18px"><span>{src}</span><span>팜 에디터</span></div>
</div>'''
    return page(inner, h)

def thumb(n, kw, sub, visual):
    inner = f'''<div style="position:absolute;right:-30px;top:120px">{visual}</div>
<div style="position:absolute;top:44px;left:50px;font-size:30px;color:#fff;background:rgba(63,74,54,.85);padding:10px 22px;border-radius:30px">팜 에디터</div>
<div style="position:absolute;left:70px;right:70px;bottom:80px">
 <div style="font-size:52px;font-weight:500;color:{C['lg']}">꿀 공부 {n}</div>
 <div style="font-size:124px;font-weight:700;line-height:1.08;margin-top:10px;letter-spacing:-2px">{kw}</div>
 <div style="font-size:56px;font-weight:700;line-height:1.3;margin-top:22px;color:{C['g']}">{sub}</div>
 <div style="display:flex;align-items:center;gap:16px;margin-top:30px;font-size:34px;color:#6B6455"><span style="width:46px;height:3px;background:#C9A86A"></span>농가가 알려 준 꿀 이야기</div>
</div>'''
    return page(inner, 1080, hexop=.16)

def pill(t, bg, fg='#fff', fs=34):
    return f'<span style="display:inline-block;background:{bg};color:{fg};font-size:{fs}px;font-weight:700;padding:10px 26px;border-radius:40px">{t}</span>'

def row2(a, b, la='벌꿀', lb='사양벌꿀'):
    return f'''<div style="display:flex;gap:24px">
 <div style="flex:1;background:#fff;border-radius:28px;padding:34px;border:4px solid {C['g']}">{pill(la, C['g'])}<div style="margin-top:22px;font-size:38px;line-height:1.55">{a}</div></div>
 <div style="flex:1;background:#fff;border-radius:28px;padding:34px;border:4px solid {C['gold']}">{pill(lb, C['gold'])}<div style="margin-top:22px;font-size:38px;line-height:1.55">{b}</div></div></div>'''

IM = {}
# ---------- 1. 사양꿀 뜻
IM['p1/01.jpg'] = thumb(1, '사양꿀 뜻', '라벨에 이 한 줄이 있으면<br>설탕을 먹은 벌의 꿀', jar(380))
IM['p1/02.jpg'] = card(1, '같은 꿀벌, 먹이가 다릅니다', row2(
    '🌼 꽃에서 모은 꿀<br>이름: 아카시아꿀 · 밤꿀 · 잡화꿀<br>식품 유형: <b>벌꿀</b>',
    '🍚 설탕물을 먹고 채운 꿀<br>이름: 사양벌꿀(사양꿀)<br>식품 유형: <b>사양벌꿀</b>'), '식품의약품안전처 · 2017년부터 구분 표시')
IM['p1/03.jpg'] = card(1, '병 뒷면, 이 칸만 보세요', f'''<div style="background:#fff;border-radius:22px;padding:40px 46px;font-size:34px;line-height:2;border:3px solid {C['line']};color:#555">
 <div>제품명 : ○○ 꿀</div>
 <div style="background:#FFF3D6;margin:6px -20px;padding:4px 20px;border-radius:12px;border:4px solid {C['hon']};color:{C['ink']}"><b>식품 유형 : 사양벌꿀</b></div>
 <div style="color:{C['red']};font-weight:700">꿀벌이 설탕을 먹고 저장해 생산한 꿀</div>
 <div>내용량 : 2.4kg</div><div>원산지 : 국산</div></div>
 <div style="margin-top:28px;font-size:34px;line-height:1.5">빨간 문구는 <b>12포인트</b> 넘는 글자로 적게 되어 있습니다.<br>「식품 유형: 벌꿀」이면 꽃에서 온 꿀입니다.</div>''', '라벨은 예시 · 식품 표시 기준')
def bar(lab, v, w, col, note):
    return f'''<div style="margin:26px 0"><div style="font-size:38px;font-weight:700;margin-bottom:12px">{lab}</div>
 <div style="display:flex;align-items:center;gap:20px"><div style="width:{w}px;height:86px;background:{col};border-radius:14px;display:flex;align-items:center;padding-left:26px;color:#fff;font-size:44px;font-weight:700">{v}</div><span style="font-size:30px;color:{C['gray']}">{note}</span></div></div>'''
IM['p1/04.jpg'] = card(1, '값은 3배쯤 차이 납니다', bar('천연 벌꿀', '4~6만 원', 760, C['g'], '1kg') + bar('사양벌꿀', '1.5~2만 원', 280, C['gold'], '1kg')
    + f'<div style="font-size:34px;line-height:1.5;margin-top:20px">둘 다 합법 식품입니다.<br>문제는 <b>사양꿀을 천연꿀로 속여 팔 때</b>입니다.</div>', '보도 기준(식약처 관계자 · 헤럴드경제)')

# ---------- 2. 꿀 보관방법
IM['p2/01.jpg'] = thumb(2, '꿀 보관방법', '하얗게 굳은 꿀은<br>상한 게 아닙니다', jar(380, crystals=True))
IM['p2/02.jpg'] = card(2, '흰 알갱이는 설탕이 아니라<br>포도당입니다', f'''<div style="display:flex;align-items:center;gap:40px">{jar(260)}<div style="font-size:70px;color:{C['gold']}">→</div>{jar(260, crystals=True)}</div>
 <div style="font-size:36px;line-height:1.55;margin-top:24px">꿀은 물이 녹여 둘 수 있는 양보다 당이 많습니다.<br>서늘해지면 포도당이 먼저 알갱이로 나옵니다.<br><b>먹어도 안전합니다.</b></div>''', '식품의약품안전처 카드뉴스')
def tz(t, lab, sub, col, w):
    return f'<div style="flex:{w};background:{col};color:#fff;padding:30px 22px;text-align:center"><div style="font-size:46px;font-weight:700">{t}</div><div style="font-size:32px;font-weight:700;margin-top:8px">{lab}</div><div style="font-size:26px;margin-top:6px;opacity:.9">{sub}</div></div>'
IM['p2/03.jpg'] = card(2, '10~15도에서 가장 잘 굳습니다', f'''<div style="display:flex;border-radius:26px;overflow:hidden">{tz('4도↓','천천히 굳음','냉장고','#7FA0B5',1)}{tz('10~15도','가장 잘 굳음','겨울 찬장 · 베란다',C['red'],1.3)}{tz('25도↑','거의 안 굳음','따뜻한 실내',C['hon'],1)}</div>
 <div style="font-size:36px;line-height:1.55;margin-top:36px">굳는 게 싫다면 온도가 일정한 실온 그늘에.<br>창가 햇빛 · 가스레인지 옆은 피하고, <b>뚜껑은 꼭 닫기.</b></div>''', '식약처 카드뉴스 · 보도(2026)')
IM['p2/04.jpg'] = card(2, '꽃에 따라 굳는 정도가 다릅니다', row2('유채꿀<br>잡화꿀<br>싸리꿀', '아카시아꿀<br>밤꿀<br>대추꿀', '잘 굳는 꿀', '잘 안 굳는 꿀')
    + '<div style="font-size:34px;line-height:1.5;margin-top:30px">굳는다고 진짜, 안 굳는다고 가짜가 아닙니다.<br>진짜인지는 라벨의 <b>식품 유형</b>으로 봅니다.</div>', '식약처 카드뉴스 · 보도(2026)')
def step(n, t, s):
    return f'<div style="display:flex;gap:28px;align-items:flex-start;margin:22px 0"><div style="flex:none;width:86px;height:86px;border-radius:50%;background:{C["g"]};color:#fff;font-size:46px;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div><div><div style="font-size:42px;font-weight:700">{t}</div><div style="font-size:32px;color:#55594F;margin-top:6px;line-height:1.4">{s}</div></div></div>'
IM['p2/05.jpg'] = card(2, '굳은 꿀 녹이는 법', step(1, '병째 따뜻한 물에', '끓는 물 말고, 손을 넣어 따끈한 정도') + step(2, '미지근한 물부터 천천히', '유리병은 갑자기 뜨거워지면 깨질 수 있음') + step(3, '가끔 숟가락으로 젓기', '굳은 그대로 빵에 발라 먹어도 됩니다')
    + f'<div style="margin-top:20px;background:#FFF3D6;border-radius:18px;padding:22px 28px;font-size:32px">⚠ 돌이 안 된 아기(1세 미만)에게는 꿀을 먹이지 않습니다</div>', '')

# ---------- 3. 천연꿀 추천
IM['p3/01.jpg'] = thumb(3, '천연꿀 추천', '라벨에서<br>-23.5 하나만 보세요', jar(380))
def scale(marks, zones, w=940):
    lo, hi = -26.5, -20.5
    X = lambda v: (v - lo) / (hi - lo) * w
    z = ''.join(f'<div style="position:absolute;left:{X(a)}px;width:{X(b)-X(a)}px;top:0;height:90px;background:{c}"></div>' for a, b, c in zones)
    m = ''.join(f'<div style="position:absolute;left:{X(v)-2}px;top:-16px;width:4px;height:122px;background:{C["ink"]}"></div><div style="position:absolute;left:{X(v)+(-230 if k==0 else 10)}px;width:220px;text-align:{"right" if k==0 else "left"};top:118px;font-size:40px;font-weight:700">{v}</div><div style="position:absolute;left:{X(v)+(-290 if k==0 else 10)}px;width:280px;text-align:{"right" if k==0 else "left"};top:170px;font-size:26px;color:{C["gray"]}">{t}</div>' for k,(v, t) in enumerate(marks))
    return f'<div style="position:relative;width:{w}px;height:220px;margin-top:40px"><div style="position:absolute;inset:0 0 auto 0;height:90px;border-radius:18px;overflow:hidden">{z}</div>{m}</div>'
IM['p3/02.jpg'] = card(3, '숫자가 작을수록<br>꽃꿀에 가깝습니다', f'''<div style="display:flex;justify-content:space-between;font-size:40px;font-weight:700"><span style="color:{C['g']}">🌼 꽃꿀 쪽</span><span style="color:{C['gold']}">설탕을 먹은 꿀 쪽 🍚</span></div>
 <div style="height:26px;margin-top:20px;border-radius:13px;background:linear-gradient(90deg,{C['g']},{C['hon']})"></div>
 <div style="display:flex;justify-content:space-between;font-size:44px;font-weight:700;margin-top:16px"><span>-25</span><span>-20</span><span>-15</span><span>-12</span></div>
 <div style="font-size:34px;line-height:1.55;margin-top:40px">이 숫자가 「탄소동위원소비」입니다.<br>국내 유통 꿀을 잰 연구에서 <b>-25.18 ~ -12.60</b>까지 나왔습니다.</div>''', '「국내 유통되는 벌꿀의 품질특성」 한국식품과학회지')
IM['p3/03.jpg'] = card(3, '-22.5와 -23.5, 두 개의 선', scale([(-23.5, '등급 1+ · 1등급 선'), (-22.5, '천연 벌꿀 선')], [(-26.5, -23.5, C['g']), (-23.5, -22.5, C['hon']), (-22.5, -20.5, '#C9BFA8')])
    + f'''<div style="font-size:33px;line-height:1.75;margin-top:30px"><span style="color:{C['g']};font-weight:700">■</span> -23.5 아래: 1+ · 1등급을 받을 수 있음<br><span style="color:{C['hon']};font-weight:700">■</span> -23.5 ~ -22.5: 벌꿀이지만 2등급까지<br><span style="color:#B3A98F;font-weight:700">■</span> -22.5 넘음: 천연 벌꿀로 팔 수 없음</div>''', '식약처 식품공전 · 축산물품질평가원 등급 기준')
def vbars(vals, ref=-23.5):
    lo = -22; hi = -26
    H = lambda v: (v - lo) / (hi - lo) * 440
    bs = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;width:130px"><div style="font-size:36px;font-weight:700;margin-bottom:10px">{v}</div><div style="width:110px;height:{H(v)}px;background:{C["g"]};border-radius:14px 14px 0 0"></div><div style="font-size:30px;margin-top:12px">농가 {k}</div></div>' for k, v in vals)
    return f'<div style="position:relative;display:flex;justify-content:space-around;align-items:flex-end;height:560px;border-bottom:4px solid {C["ink"]}">{bs}<div style="position:absolute;left:0;right:0;bottom:{H(ref)+58}px;border-top:5px dashed {C["red"]}"></div><div style="position:absolute;right:0;bottom:{H(ref)+66}px;font-size:28px;color:{C["red"]};font-weight:700;background:{C["bg"]};padding:0 8px">-23.5 선</div></div>'
IM['p3/04.jpg'] = card(3, '홍천 아카시아꿀 5곳,<br>모두 -23.5보다 한참 아래', vbars([('A', -25.0), ('B', -25.2), ('C', -25.2), ('D', -25.6), ('E', -25.4)]), '「등급정보 365+」 2016 · 강원 홍천 양봉 농가 5곳')

# ---------- 4. 꿀 고르는법
IM['p4/01.jpg'] = thumb(4, '꿀 고르는법', '등급 QR을 찍으면<br>나오는 다섯 가지', f'''<div style="width:330px;height:330px;margin:60px 60px 0 0;background:#fff;border-radius:30px;border:8px solid {C['ink']};display:grid;grid-template-columns:repeat(5,1fr);gap:10px;padding:26px">{''.join(f'<div style="background:{C["ink"] if (i*7)%3 else "#fff"};border-radius:6px"></div>' for i in range(25))}</div>''')
def badge(t, col, s):
    return f'<div style="text-align:center"><div style="width:230px;height:230px;border-radius:50%;background:{col};color:#fff;font-size:96px;font-weight:700;display:flex;align-items:center;justify-content:center;margin:auto">{t}</div><div style="font-size:30px;margin-top:16px">{s}</div></div>'
IM['p4/02.jpg'] = card(4, '국산 꿀 등급은 세 가지', f'<div style="display:flex;justify-content:space-around">{badge("1+", C["g"], "가장 높은 등급")}{badge("1", C["lg"], "")}{badge("2", C["gold"], "")}</div>'
    + f'<div style="font-size:36px;line-height:1.6;margin-top:46px">대상: <b>아까시꿀 · 밤꿀 · 잡화꿀</b>(국산 천연 꿀)<br>1++ 등급은 없습니다.</div>', '축산물품질평가원 · 2023년 12월 정식 시행')
def box(t, s, col):
    return f'<div style="background:#fff;border:5px solid {col};border-radius:26px;padding:30px 34px"><div style="font-size:42px;font-weight:700;color:{col}">{t}</div><div style="font-size:32px;margin-top:10px;line-height:1.45">{s}</div></div>'
IM['p4/03.jpg'] = card(4, '두 번 검사해서 등급을 매깁니다', box('1차 · 규격 검사', '한국양봉협회 · 한국양봉농협<br>물이 너무 많지 않은지, 천연 꿀이 맞는지', C['gold'])
    + f'<div style="text-align:center;font-size:60px;color:{C["gold"]};margin:10px 0">↓</div>' + box('2차 · 품질 평가', '축산물품질평가원<br>수분 · 당 비율 · 신선도 · 색 · 맛과 향 → 1+ · 1 · 2', C['g']), '경기도 「경기도 토종벌꿀」 2026.3')
def qi(i, t, s):
    return f'<div style="display:flex;align-items:center;gap:24px;background:#fff;border-radius:20px;padding:20px 26px;margin:12px 0"><div style="flex:none;width:64px;height:64px;border-radius:50%;background:{C["hon"]};color:#fff;font-size:36px;font-weight:700;display:flex;align-items:center;justify-content:center">{i}</div><div style="font-size:38px;font-weight:700;width:250px">{t}</div><div style="font-size:30px;color:#55594F">{s}</div></div>'
IM['p4/04.jpg'] = card(4, 'QR을 찍으면 나오는 다섯 가지', qi(1, '꿀의 종류', '아까시 · 밤 · 잡화') + qi(2, '등급', '1+ · 1 · 2') + qi(3, '생산자', '이 꿀을 뜬 양봉 농가') + qi(4, '소분기관', '병에 나눠 담은 곳') + qi(5, '품질검사기관', '검사를 맡은 곳'), '축산물품질평가원 「등급정보 365+」')
IM['p4/05.jpg'] = card(4, '꿀 고르는법, 세 단계', step(1, '등급 QR이 있으면 찍기', '생산자 이름까지 확인') + step(2, '없으면 뒷면 식품 유형', '「벌꿀」인지 「사양벌꿀」인지') + step(3, '탄소동위원소비 -23.5 아래?', '숫자가 없으면 판매자에게 성적서 요청'), '')

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1080})
    for out, html in IM.items():
        t = D / '_t.html'; t.write_text(html, encoding='utf-8'); pg.goto('file://' + str(t)); pg.wait_for_timeout(300)
        pg.screenshot(path=str(D / '_t.png'))
        from PIL import Image
        Image.open(D / '_t.png').convert('RGB').save(D / out, quality=90); print(out)
    b.close()
