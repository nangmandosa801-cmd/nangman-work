# 낭만커피 원두 이야기 · 썸네일과 시각자료 (모던 다크 에스프레소 톤)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os
OUT = "/home/claude/coffee/imgs"; os.makedirs(OUT, exist_ok=True)
B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
K = "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"
M = "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc"
def F(path, size): return ImageFont.truetype(path, size, index=1)  # KR

BG1, BG2 = (28, 18, 14), (52, 33, 24)
CREAM = (246, 236, 222); CARAMEL = (214, 160, 98); MUTED = (190, 168, 146); LINE = (92, 66, 50)

def gradient(w, h):
    im = Image.new("RGB", (w, h), BG1)
    px = im.load()
    cx, cy = w * 0.78, h * 0.25
    maxd = math.hypot(w, h)
    for y in range(h):
        for x in range(0, w):
            t = min(1, math.hypot(x - cx, y - cy) / (maxd * 0.75))
            px[x, y] = tuple(int(BG2[i] * (1 - t) + BG1[i] * t) for i in range(3))
    return im

def bean(d, cx, cy, r, color, width=10):
    d.ellipse([cx - r * 0.72, cy - r, cx + r * 0.72, cy + r], outline=color, width=width)
    pts = []
    for i in range(41):
        t = i / 40
        y = cy - r * 0.86 + t * r * 1.72
        x = cx + math.sin(t * math.pi * 2) * r * 0.16
        pts.append((x, y))
    d.line(pts, fill=color, width=width, joint="curve")

def chip(d, x, y, text, f):
    w = d.textlength(text, font=f) + 44
    d.rounded_rectangle([x, y, x + w, y + 64], radius=32, outline=CARAMEL, width=3)
    d.text((x + 22, y + 32), text, font=f, fill=CREAM, anchor="lm")
    return x + w + 16

def thumb(key, top, big, sub, chips):
    W, H = 1200, 800
    im = gradient(W, H); d = ImageDraw.Draw(im)
    bean(d, 1030, 300, 200, (110, 78, 56), 14)
    bean(d, 1030, 300, 200, (140, 100, 70), 4)
    d.text((80, 90), "낭만커피 · 원두 이야기", font=F(B, 34), fill=CARAMEL)
    d.line([(80, 145), (180, 145)], fill=CARAMEL, width=5)
    y = 190
    size = 132
    while max(d.textlength(l, font=F(K, size)) for l in big) > 760: size -= 4
    for line in big:
        d.text((76, y), line, font=F(K, size), fill=CREAM); y += int(size * 1.15)
    ss = 44
    while d.textlength(sub, font=F(M, ss)) > 780: ss -= 2
    d.text((80, y + 24), sub, font=F(M, ss), fill=MUTED)
    x = 80
    for c in chips:
        x = chip(d, x, 650, c, F(B, 34))
    im.save(f"{OUT}/coffee_{key}_thumb.jpg", quality=92)

def bar(d, x, y, w, level, label, f, fs):
    d.text((x, y + 18), label, font=f, fill=CREAM, anchor="lm")
    bx = x + 130
    for i in range(5):
        c = CARAMEL if i < level else LINE
        d.rounded_rectangle([bx + i * (w // 5), y, bx + i * (w // 5) + w // 5 - 10, y + 36], radius=8, fill=c)

def profile(key, title, rows, facts, notes):
    W, H = 1200, 900
    im = gradient(W, H); d = ImageDraw.Draw(im)
    d.text((70, 60), "한눈에 보는", font=F(M, 36), fill=CARAMEL)
    d.text((70, 105), title, font=F(K, 72), fill=CREAM)
    d.text((70, 215), "맛 지도  (일반적인 경향)", font=F(B, 32), fill=MUTED)
    y = 275
    for lab, lv in rows:
        bar(d, 70, y, 460, lv, lab, F(B, 38), None); y += 70
    # 오른쪽 사실 카드
    cx = 720
    d.rounded_rectangle([cx, 270, 1130, 590], radius=24, outline=LINE, width=3)
    yy = 300
    for k, v in facts:
        d.text((cx + 30, yy), k, font=F(M, 28), fill=MUTED)
        d.text((cx + 30, yy + 36), v, font=F(B, 36), fill=CREAM)
        yy += 98
    d.text((70, 625), "이런 향이 납니다", font=F(B, 32), fill=MUTED)
    x = 70; yb = 680
    for n in notes:
        w = d.textlength(n, font=F(B, 40)) + 56
        if x + w > 1130: x = 70; yb += 96
        d.rounded_rectangle([x, yb, x + w, yb + 76], radius=38, fill=(74, 50, 37))
        d.text((x + 28, yb + 38), n, font=F(B, 40), fill=CREAM, anchor="lm"); x += w + 18
    d.text((1130, 860), "낭만커피", font=F(B, 28), fill=CARAMEL, anchor="rs")
    im.save(f"{OUT}/coffee_{key}_info.jpg", quality=92)

ORI = {
 "b01": ("브라질", ["브라질 원두"], "세계 커피의 3분의 1이 자라는 넓은 고원", ["고소함", "산미 적음", "블렌드 바탕"],
         [("산미", 1), ("단맛", 3), ("바디", 3), ("쓴맛", 3)], [("해발", "800~1,300m"), ("가공", "내추럴"), ("등급", "No.2 17/18")], ["땅콩", "밀크초콜릿", "캐러멜"]),
 "b02": ("콜롬비아 수프리모", ["콜롬비아", "수프리모"], "안데스 비탈, 한 해 두 번 수확", ["균형", "캐러멜", "부드러운 산미"],
         [("산미", 3), ("단맛", 4), ("바디", 3), ("쓴맛", 2)], [("해발", "1,200~2,000m"), ("가공", "워시드"), ("등급", "수프리모 · 엑셀소")], ["캐러멜", "사과", "견과류"]),
 "b03": ("케냐 AA", ["케냐 AA"], "적도 고원 붉은 흙의 진한 산미", ["자몽", "블랙커런트", "핸드드립"],
         [("산미", 5), ("단맛", 4), ("바디", 3), ("쓴맛", 1)], [("해발", "1,500m 이상"), ("가공", "워시드 (두 번 씻음)"), ("등급", "AA · AB · PB")], ["자몽", "블랙커런트", "토마토 감칠맛"]),
 "b04": ("만델링", ["만델링"], "수마트라 토바 호숫가의 묵직한 커피", ["묵직함", "흙내", "라떼"],
         [("산미", 1), ("단맛", 2), ("바디", 5), ("쓴맛", 4)], [("산지", "수마트라 북부"), ("가공", "길링 바사"), ("등급", "G1")], ["다크초콜릿", "삼나무", "비 온 숲"]),
 "b05": ("과테말라 안티구아", ["과테말라", "안티구아"], "세 화산이 둘러싼 골짜기", ["초콜릿", "스모키", "균형"],
         [("산미", 2), ("단맛", 4), ("바디", 4), ("쓴맛", 3)], [("해발", "약 1,500m"), ("가공", "워시드"), ("등급", "SHB")], ["다크초콜릿", "계피", "은은한 연기"]),
 "g02": ("에티오피아 예가체프", ["예가체프"], "꽃향 나는 커피가 자라는 고원 마을", ["꽃향", "레몬", "핸드드립"],
         [("산미", 4), ("단맛", 3), ("바디", 2), ("쓴맛", 1)], [("해발", "1,700~2,200m"), ("가공", "워시드 · 내추럴"), ("등급", "G1 · G2")], ["재스민", "레몬", "홍차"]),
 "g01": ("게이샤", ["게이샤", "커피 유래"], "에티오피아 숲에서 파나마 산비탈까지", ["재스민", "복숭아", "가장 비싼 한 잔"],
         [("산미", 4), ("단맛", 4), ("바디", 1), ("쓴맛", 1)], [("고향", "에티오피아 게샤"), ("이름난 곳", "파나마 보케테"), ("알려진 해", "2004년")], ["재스민", "복숭아", "베르가못"]),
}
for k, (title, big, sub, chips, rows, facts, notes) in ORI.items():
    thumb(k, None, big, sub, chips)
    profile(k, title, rows, facts, notes)

# b00 허브: 썸네일 + 나라별 맛 지도
thumb("b00", None, ["원두 종류", "특징"], "아라비카와 로부스타, 나라별 맛 한눈에", ["7개 산지", "봉투 읽는 법", "맛 지도"])
W, H = 1200, 1100
im = gradient(W, H); d = ImageDraw.Draw(im)
d.text((70, 60), "한눈에 보는", font=F(M, 36), fill=CARAMEL)
d.text((70, 105), "나라별 원두 맛 지도", font=F(K, 72), fill=CREAM)
d.text((70, 215), "산미 · 바디 (일반적인 경향)", font=F(B, 32), fill=MUTED)
rows = [("브라질", 1, 3), ("콜롬비아", 3, 3), ("과테말라", 2, 4), ("만델링", 1, 5), ("예가체프", 4, 2), ("케냐", 5, 3), ("게이샤", 4, 1)]
d.text((420, 290), "산미", font=F(B, 32), fill=MUTED); d.text((800, 290), "바디", font=F(B, 32), fill=MUTED)
y = 350
for n, a, bd in rows:
    d.text((70, y + 18), n, font=F(B, 42), fill=CREAM, anchor="lm")
    for i in range(5):
        d.rounded_rectangle([420 + i * 70, y, 420 + i * 70 + 58, y + 36], radius=8, fill=CARAMEL if i < a else LINE)
        d.rounded_rectangle([800 + i * 70, y, 800 + i * 70 + 58, y + 36], radius=8, fill=(232, 205, 170) if i < bd else LINE)
    y += 95
d.text((1130, 1060), "낭만커피", font=F(B, 28), fill=CARAMEL, anchor="rs")
im.save(f"{OUT}/coffee_b00_info.jpg", quality=92)

# g03 산미
thumb("g03", None, ["커피 산미", "이유"], "커피콩은 원래 빨간 열매의 씨앗", ["구연산", "사과산", "높은 산지"])
im = gradient(1200, 900); d = ImageDraw.Draw(im)
d.text((70, 60), "한눈에 보는", font=F(M, 36), fill=CARAMEL)
d.text((70, 105), "신맛이 강해지는 조건", font=F(K, 68), fill=CREAM)
cols = [("자란 곳", "높은 산", "낮은 땅"), ("볶은 정도", "연하게", "진하게"), ("가루 굵기", "굵게", "가늘게"), ("물 온도", "낮게", "높게")]
d.text((520, 250), "신맛 ↑", font=F(B, 40), fill=CARAMEL); d.text((860, 250), "신맛 ↓", font=F(B, 40), fill=MUTED)
y = 330
for a, b, c in cols:
    d.rounded_rectangle([70, y, 1130, y + 110], radius=20, outline=LINE, width=3)
    d.text((110, y + 55), a, font=F(B, 42), fill=CREAM, anchor="lm")
    d.text((520, y + 55), b, font=F(B, 44), fill=CARAMEL, anchor="lm")
    d.text((860, y + 55), c, font=F(B, 44), fill=MUTED, anchor="lm")
    y += 135
d.text((1130, 860), "낭만커피", font=F(B, 28), fill=CARAMEL, anchor="rs")
im.save(f"{OUT}/coffee_g03_info.jpg", quality=92)

# g04 로스팅 8단계 색 띠
thumb("g04", None, ["커피 로스팅", "단계"], "초록 생두가 갈색 원두가 되기까지 12분", ["1차 크랙", "8단계", "풀시티"])
im = gradient(1200, 900); d = ImageDraw.Draw(im)
d.text((70, 60), "한눈에 보는", font=F(M, 36), fill=CARAMEL)
d.text((70, 105), "로스팅 8단계", font=F(K, 72), fill=CREAM)
st = [("라이트", (196, 160, 104)), ("시나몬", (176, 124, 72)), ("미디엄", (150, 98, 56)), ("하이", (128, 80, 44)),
      ("시티", (104, 64, 36)), ("풀시티", (82, 50, 30)), ("프렌치", (58, 36, 24)), ("이탈리안", (38, 26, 20))]
x0, wbox = 70, 132
for i, (n, c) in enumerate(st):
    x = x0 + i * wbox
    d.rounded_rectangle([x, 260, x + wbox - 12, 520], radius=18, fill=c, outline=(120, 90, 70), width=2)
    d.text((x + (wbox - 12) / 2, 560), n, font=F(B, 30), fill=CREAM, anchor="mm")
d.line([(70, 640), (1130, 640)], fill=LINE, width=4)
for x, t in [(70, "신맛 · 과일 향"), (1130, "쓴맛 · 그을린 향")]:
    d.text((x, 690), t, font=F(B, 40), fill=CARAMEL if x == 70 else MUTED, anchor="lm" if x == 70 else "rm")
d.text((600, 780), "1차 크랙 무렵 미디엄 · 하이,  2차 크랙부터 풀시티", font=F(M, 34), fill=MUTED, anchor="mm")
d.text((1130, 860), "낭만커피", font=F(B, 28), fill=CARAMEL, anchor="rs")
im.save(f"{OUT}/coffee_g04_info.jpg", quality=92)
print(sorted(os.listdir(OUT)))
