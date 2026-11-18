"""티스토리(talk7921 · 낭만 부동산 노트) 표준 썸네일 — 11/18 사용자 「티스토리 표준 썸네일 만들고 그런 형태로 다 통일」
모든 티스토리 글은 이 한 가지 모양만 쓴다(tsthumb.py 는 옛 판 · 쓰지 않음).

  python3 tsstd.py one "<검색어>" "<큰 숫자>" "<숫자 뜻>" "<카테고리>" "<기준>" out.png
  python3 tsstd.py all spec.json outdir/      # spec = [{no, kw, num, lab, cat, base}, …] → outdir/ts<no>_thumb.png

모양(1200x690 · 목록 카드 비율 그대로라 잘리지 않음)
  맨 위 파란 띠 · 왼쪽 위 카테고리 칩 · 오른쪽 위 「낭만 부동산 노트」
  검색어(검정 · 굵게 · 2줄까지) → 큰 숫자 하나(파랑) → 숫자 뜻 한 줄(회색)
  맨 아래 가는 줄 + 왼쪽 기준(자료 · 기간) · 오른쪽 「낭만 부동산 분석 플랫폼」
규칙: 숫자는 글 본문에 있는 것 하나만 · 그림 · 사진 · 그래프 없음 · 글자 크기 고정(작게 줄이지 않음 · 넘치면 검색어를 줄인다)."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
F = '/home/claude/tools/tistory/fonts/Pretendard-'
INK, GRAY, ACC, BG, LINE, CHIP = '#191F28', '#6B7684', '#3182F6', '#FFFFFF', '#E5E8EB', '#E8F3FF'
W, H, L = 1200, 690, 80


def font(w, s):
    if not os.path.exists(F + w + '.otf'):   # 글꼴은 저장소에 없음 → npm 에서 받아 둔다
        os.system('mkdir -p /tmp/pt /home/claude/tools/tistory/fonts && cd /tmp/pt && npm pack pretendard@1.3.9 -q >/dev/null 2>&1 '
                  '&& tar xzf pretendard-1.3.9.tgz && cp package/dist/public/static/Pretendard-*.otf /home/claude/tools/tistory/fonts/')
    return ImageFont.truetype(F + w + '.otf', s)


def wrap(d, t, f, maxw):
    out, cur = [], ''
    for w in t.split(' '):
        nx = (cur + ' ' + w).strip()
        if d.textlength(nx, font=f) <= maxw or not cur: cur = nx
        else: out.append(cur); cur = w
    out.append(cur); return out


def make(kw, num, lab, cat, base, out):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=ACC)
    # 카테고리 칩
    fc = font('Bold', 28); cw = d.textlength(cat, font=fc)
    d.rounded_rectangle([L, 58, L + cw + 40, 58 + 52], radius=26, fill=CHIP)
    d.text((L + 20, 58 + 9), cat, font=fc, fill=ACC)
    fb = font('SemiBold', 28); bt = '낭만 부동산 노트'
    d.text((W - L - d.textlength(bt, font=fb), 68), bt, font=fb, fill=GRAY)
    # 검색어
    fk = font('ExtraBold', 84); ls = wrap(d, kw, fk, W - 2 * L)
    if len(ls) > 2: raise SystemExit(f'검색어가 2줄을 넘음: {kw}')
    blk = len(ls) * 100 + 18 + 150 + 46
    y = 130 + max(0, ((H - 95) - 130 - blk) // 2)
    for ln in ls:
        d.text((L, y), ln, font=fk, fill=INK); y += 100
    # 큰 숫자
    y += 18
    fn = font('ExtraBold', 128)
    if d.textlength(num, font=fn) > W - 2 * L: raise SystemExit(f'숫자가 너무 김: {num}')
    d.text((L, y), num, font=fn, fill=ACC); y += 150
    fl = font('SemiBold', 38)
    if d.textlength(lab, font=fl) > W - 2 * L: raise SystemExit(f'숫자 뜻이 너무 김: {lab}')
    d.text((L, y), lab, font=fl, fill=GRAY)
    # 아래 줄
    d.line([L, H - 78, W - L, H - 78], fill=LINE, width=2)
    fs = font('Medium', 26)
    d.text((L, H - 60), base, font=fs, fill=GRAY)
    br = '낭만 부동산 분석 플랫폼'
    d.text((W - L - d.textlength(br, font=font('Bold', 26)), H - 60), br, font=font('Bold', 26), fill=INK)
    if y + 50 > H - 90: raise SystemExit(f'세로 넘침: {kw}')
    im.save(out); return out


if __name__ == '__main__':
    if sys.argv[1] == 'one':
        print(make(*sys.argv[2:8]))
    else:
        spec = json.load(open(sys.argv[2], encoding='utf8')); od = sys.argv[3]; os.makedirs(od, exist_ok=True)
        bad = []
        for s in spec:
            try: make(s['kw'], s['num'], s['lab'], s['cat'], s['base'], os.path.join(od, f"ts{s['no']}_thumb.png"))
            except SystemExit as e: bad.append((s['no'], str(e)))
        print(json.dumps({'ok': not bad, 'n': len(spec), 'bad': bad}, ensure_ascii=False))
