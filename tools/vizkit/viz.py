from PIL import Image, ImageDraw, ImageFont
import os
B = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
K = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
NAVY, BLUE, ORG, RED, GRN, GRY, BG = '#1d3d5c', '#2f5d8a', '#f08a24', '#d9534f', '#2e9e6a', '#6b7785', '#f4f7fb'
W = 1080
os.makedirs('viz', exist_ok=True)
def f(s, k=B): return ImageFont.truetype(k, s, index=1)
def tw(d, t, ft): return d.textlength(t, font=ft)

def frame(h, kicker, title):
    im = Image.new('RGB', (W, h), 'white'); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 170), fill=NAVY)
    d.text((60, 30), kicker, font=f(34), fill='#9fc3e6')
    d.text((60, 78), title, font=f(58, K), fill='white')
    d.rectangle((0, h-70, W, h), fill=BG)
    d.text((60, h-55), '낭만 인테리어', font=f(32), fill=GRY)
    return im, d

def center(d, cx, y, t, ft, fill):
    d.text((cx - tw(d, t, ft)/2, y), t, font=ft, fill=fill)

def cols(name, kicker, title, items, h=820):
    """items: [(head, [lines], verdict, color)]"""
    im, d = frame(h, kicker, title)
    n = len(items); gap = 30; cw = (W - 120 - gap*(n-1)) / n
    for i, (hd, lines, vd, c) in enumerate(items):
        x = 60 + i*(cw+gap); y0 = 220
        d.rounded_rectangle((x, y0, x+cw, h-110), 22, fill=BG, outline=c, width=5)
        d.rounded_rectangle((x, y0, x+cw, y0+100), 22, fill=c)
        d.rectangle((x, y0+70, x+cw, y0+100), fill=c)
        center(d, x+cw/2, y0+18, hd, f(50 if n < 3 else 44, K), 'white')
        y = y0+140
        for L in lines:
            center(d, x+cw/2, y, L, f(40 if n < 3 else 36), '#222'); y += 66
        center(d, x+cw/2, h-215, vd, f(46 if n < 3 else 40, K), c)
    im.save(f'viz/{name}.png'); return name

def steps(name, kicker, title, items):
    h = 230 + 120*len(items) + 90
    im, d = frame(h, kicker, title)
    y = 220
    for i, (a, b) in enumerate(items):
        d.ellipse((60, y, 150, y+90), fill=ORG if i == len(items)-1 else BLUE)
        center(d, 105, y+8, str(i+1), f(56, K), 'white')
        d.text((180, y+4), a, font=f(48, K), fill=NAVY)
        if b: d.text((180 + tw(d, a, f(48, K)) + 24, y+14), b, font=f(38), fill=GRY)
        if i < len(items)-1: d.line((105, y+92, 105, y+118), fill='#c9d4df', width=6)
        y += 120
    im.save(f'viz/{name}.png'); return name

def bars(name, kicker, title, items, unit, note):
    """items: [(label, value, color, valtext)]"""
    h = 260 + 150*len(items) + 120
    im, d = frame(h, kicker, title)
    mx = max(v for _, v, _, _ in items); y = 230; x0 = 400; L = W - x0 - 80
    for lb, v, c, vt in items:
        d.text((60, y+18), lb, font=f(44, K), fill=NAVY)
        d.rounded_rectangle((x0, y, x0 + L*v/mx, y+96), 16, fill=c)
        t = vt; ft = f(46, K)
        if tw(d, t, ft) + 40 < L*v/mx: d.text((x0+24, y+18), t, font=ft, fill='white')
        else: d.text((x0 + L*v/mx + 20, y+18), t, font=ft, fill=c)
        y += 150
    d.text((60, y+10), note, font=f(38), fill=GRY)
    im.save(f'viz/{name}.png'); return name

def layers(name, kicker, title, before, after, h=900):
    """before/after: (label, [(layer, width, color)], verdict, vcolor) — drawn left=outside"""
    im, d = frame(h, kicker, title)
    for k, (lb, ls, vd, vc) in enumerate((before, after)):
        x = 60 + k*510; y0 = 220
        center(d, x+225, y0, lb, f(46, K), vc)
        center(d, x+225, y0+64, '바깥  →  방 안', f(30), GRY)
        xx = x; top = y0+120; bot = h-260
        for nm, wd, c in ls:
            d.rectangle((xx, top, xx+wd, bot), fill=c)
            # vertical label
            ft = f(34); ty = top + 20
            for ch in nm:
                if ch == ' ': ty += 20; continue
                d.text((xx + wd/2 - 17, ty), ch, font=ft, fill='white' if c not in ('#ffffff', '#f2e6c9', '#e8eef5', '#fde2e1') else '#333'); ty += 40
            xx += wd
        center(d, x+225, h-230, vd, f(42, K), vc)
    im.save(f'viz/{name}.png'); return name

def card(name, kicker, title, big, lines, h=840):
    im, d = frame(h, kicker, title)
    d.rounded_rectangle((60, 220, W-60, 470), 26, fill=BG, outline=ORG, width=6)
    center(d, W/2, 262, big, f(96, K), ORG)
    center(d, W/2, 392, '가로 1m × 세로 1m = 1헤베', f(40), GRY)
    y = 520
    for a, b in lines:
        d.text((80, y), a, font=f(44, K), fill=NAVY)
        d.text((W - 80 - tw(d, b, f(44, K)), y), b, font=f(44, K), fill=BLUE); y += 74
    im.save(f'viz/{name}.png'); return name

CONC, GAP, MOLD, BEAD, XPS, FOAM, GYP, PAPER = '#8a8f96', '#ffffff', '#3a3a3a', '#f2e6c9', '#ef8fb4', '#f5c242', '#d7dde4', '#e8eef5'
OUT = {
 'busan_danyeol': [
  cols('v_busan_1', '부산 단열시공 · 북향 방', '왜 북향 방만 젖을까?',
       [('남향 방', ['해가 들어 벽이 데워짐', '방 안 공기와', '벽 온도 차이 작음'], '물 거의 안 맺힘', GRN),
        ('북향 방', ['해가 안 들어 벽이 참', '따뜻한 공기가 닿으면', '물방울이 맺힘'], '모서리 곰팡이', RED)]),
  layers('v_busan_2', '부산 단열시공 · 벽 속 단면', '단열벽지 vs 벽 열고 단열',
         ('단열벽지만 덧댐', [('콘크리트', 150, CONC), ('곰팡이', 80, MOLD), ('벽지', 70, PAPER), ('단열벽지', 150, BEAD)], '뒤에서 곰팡이', RED),
         ('벽 열고 단열', [('콘크리트', 150, CONC), ('압출법 단열재', 160, XPS), ('석고보드', 80, GYP), ('벽지', 60, PAPER)], '틈 없이 붙임', GRN))],
 'daegu_gompang': [
  bars('v_daegu_1', '대구 곰팡이 제거 · 아이 방', '단열재 두께 20mm → 50mm',
       [('전에 넣은 것', 20, GRY, '20mm'), ('이번에 붙인 것', 50, BLUE, '50mm 아이소핑크')], '', '두께와 함께 이음새를 폼으로 채워야 찬 기운이 안 샙니다'),
  steps('v_daegu_2', '대구 곰팡이 제거 업체', '시공 순서 5단계',
        [('철거', '벽지 · 석고보드 · 옛 단열재'), ('곰팡이 약품', '→ 중화 → 건조'), ('항균 코팅', '곰팡이 자리와 둘레'),
         ('단열재 붙이기', '이음새는 폼으로'), ('마감', '석고보드 · 도배')])],
 'veranda_hwakjang': [
  layers('v_veranda_1', '베란다 확장 단열 · 벽 속 단면', '대구 남구 집 벽을 열어 보니',
         ('뜯기 전', [('콘크리트', 150, CONC), ('빈 공간 물', 90, '#7fb2e5'), ('비드법', 110, BEAD), ('석고보드', 100, GYP)], '틈에서 물이 맺힘', RED),
         ('시공 뒤', [('콘크리트', 150, CONC), ('압출법 단열재', 150, XPS), ('폼', 50, FOAM), ('석고보드', 100, GYP)], '벽에 꽉 붙임', GRN)),
  cols('v_veranda_2', '베란다 확장 단열재 종류', '세 가지 무엇이 다를까?',
       [('비드법', ['스티로폼 계열', '값이 쌈', '물을 먹음'], '틈이 잘 생김', GRY),
        ('압출법', ['아이소핑크 등', '단단함', '물 거의 안 먹음'], '벽에 붙이는 판', BLUE),
        ('우레탄 폼', ['뿜어서 채움', '판 사이 · 코너', '틈을 막음'], '이음새 담당', ORG)])],
 'cheonjang_gyeolro': [
  cols('v_cheon_1', '천장 결로 누수 차이', '비 온 뒤에만? 겨울마다?',
       [('결로', ['겨울 · 추운 아침', '천장 넓게 · 모서리', '까만 곰팡이 점점이'], '단열 시공팀', BLUE),
        ('누수', ['비 온 뒤 · 윗집 물', '한 점에서 번짐', '누런 물자국 테두리'], '누수 탐지', RED)]),
  steps('v_cheon_2', '천장 결로 공사', '창원 베란다 천장 순서',
        [('열풍기로 말리기', '젖은 천장부터'), ('곰팡이 약품', '→ 중화'), ('항균 코팅', ''),
         ('단열재 붙이기', '물 안 먹는 판'), ('틈 채우기', '판 사이를 폼으로')])],
 'gompang_biyong': [
  card('v_biyong_1', '결로 곰팡이 제거 비용', '1헤베에 얼마?', '1헤베 10만원 선',
       [('작은 방 바깥 벽 두 면', '10~13헤베'), ('그러면', '100만원대 초반'), ('대구 작은 방 두 면 사례', '약 127만원')]),
  cols('v_biyong_2', '결로 곰팡이 제거 비용', '방법별 다음 겨울',
       [('약품 청소', ['곰팡이 닦기', '항균 코팅', '수십만원'], '다시 핌', RED),
        ('단열벽지', ['벽지 위에', '단열 시트 덧대기', '싸고 빠름'], '뒤에서 자람', ORG),
        ('벽 열고 단열', ['철거 → 제거', '→ 단열재 → 마감', '1헤베 10만원 선'], '거의 안 핌', GRN)])],
 'gyeolro_seipja': [
  steps('v_seip_1', '결로 곰팡이 세입자', '먼저 할 세 가지',
        [('사진 · 영상', '날짜가 보이게'), ('집주인에게 문자', '말로만 하면 기록 없음'), ('습도계 기록', '실내 습도를 적어 둠')]),
  cols('v_seip_2', '아파트 결로 책임', '습도로 먼저 봅니다',
       [('습도 60% 아래', ['그래도 창가 · 모서리에', '물이 맺히면', '벽이 차가운 것'], '집 문제 → 집주인', BLUE),
        ('습도 70~80%', ['집 안 여기저기', '곰팡이가 핌', '환기 · 제습 부족'], '사는 방식 점검', ORG)])],
}
if __name__ == '__main__':
    print(OUT)
