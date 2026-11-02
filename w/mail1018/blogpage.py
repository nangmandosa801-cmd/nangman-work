# 편지 넷째 장: 사무소 블로그 대행 제안 (10/19 00:38 사용자 「블로그 대행도 제안 · 기본형 주3회 30만 · 공격형 주7회 50만」 · 00:39 「매물만 올리면 노출이 안됨 정보성 글」)
import sys, os
sys.path.insert(0, '/home/claude/w/mail1018')
from letter import *
from letter import _wrap, _header, _qr

PLANS = [('기본형', '주 3회', '월 30만 원', '단지 · 동네 정보 글 위주, 매물은 글 속에 자연스럽게'),
         ('공격형', '주 7회', '월 50만 원', '매일 한 편 · 입주 · 전세 · 시세 흐름까지 빠르게')]

def page_blog(x):
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    wr = lambda t, f, w, c, lh, yy, xx=M: _wrap(d, t, f, w, c, lh, yy, xx)
    y = _header(d, '사무소 블로그 대행 안내')
    d.text((M, y), '매물만 올리는 블로그는', font=F('Black', 76), fill=INK); y += 110
    d.text((M, y), '검색에 잘 걸리지 않습니다', font=F('Black', 76), fill=NAVY); y += 140
    for b in ["손님은 매물보다 먼저 「이 단지 언제 입주하지?」 「전세 시세는 어떻게 움직이지?」 「학교 · 교통은?」을 찾습니다.",
              "그 궁금증에 답하는 정보 글을 대표님 사무소 이름으로 꾸준히 올려 드립니다. 글을 읽고 믿음이 생긴 손님이 사무소로 전화합니다."]:
        y = wr(b, F('Medium', 52), W - 2 * M, INK, 80, y); y += 24
    y += 30
    # 요금 두 칸
    gap = 50; bw = (W - 2 * M - gap) // 2; bh = 560
    for i, (nm, freq, price, desc) in enumerate(PLANS):
        bx = M + i * (bw + gap)
        d.rounded_rectangle([bx, y, bx + bw, y + bh], radius=30, fill=SOFT if i == 0 else 'white', outline=NAVY, width=5 if i else 3)
        d.text((bx + 50, y + 44), nm, font=F('Bold', 64), fill=NAVY if i == 0 else GOLD)
        d.text((bx + 50, y + 140), freq, font=F('Black', 96), fill=INK)
        d.text((bx + 50, y + 270), price, font=F('Bold', 64), fill=NAVY)
        _wrap(d, desc, F('Medium', 40), bw - 100, GREY, 58, y + 380, bx + 50)
    y += bh + 70
    d.text((M, y), '이렇게 씁니다', font=F('Bold', 60), fill=NAVY); y += 100
    for a, b in [('정보 글', '입주 일정 · 사전점검 · 전세 시세 흐름 · 학교 · 교통 · 입주 체크리스트'),
                 ('품격 있는 문장', '과장 · 반복 광고 문구 없이, 표 · 사진 · 지도로 깔끔하게'),
                 ('매물은 자연스럽게', '정보 글 끝에 「이 단지 매물 문의」 한 줄과 사무소 연락처'),
                 ('완성본 전달', '제목 · 본문 · 사진 · 태그까지 완성해 보내 드리면 붙여 넣기만')]:
        y0 = y; d.text((M + 36, y + 4), a, font=F('Bold', 50), fill=INK)
        y = wr(b, F('Medium', 46), W - 2 * M - 520, INK, 68, y + 6, M + 520); y = max(y, y0 + 80); d.rectangle([M, y0 + 8, M + 12, y - 10], fill=GOLD); y += 14
    y += 20
    y = wr('꾸준한 정보 글이 쌓이면 검색 노출이 자연스럽게 늘고, 사무소 신뢰도도 함께 올라갑니다. 검색 순위를 돈으로 사는 방식은 쓰지 않습니다.', F('Medium', 42), W - 2 * M, GREY, 62, y)
    # 아래: 견본 QR + 연락
    bh2 = mm(40); by = H - M - bh2
    assert y + 30 < by, ('blog', y, by)
    d.rounded_rectangle([M, by, W - M, by + bh2], radius=30, fill=SOFT)
    d.text((M + 56, by + 44), '견본 글은 오른쪽 QR · 문의는 문자로', font=F('Bold', 46), fill=INK)
    d.text((M + 56, by + 120), '010-2882-8165', font=F('Black', 104), fill=NAVY)
    d.text((M + 56, by + 270), '「낭만 부동산 분석 플랫폼」을 쓰는 김동진이 직접 씁니다', font=F('Medium', 38), fill=GREY)
    qs = bh2 - 150; im.paste(_qr('https://blog.naver.com/dong_jin_kim', qs), (W - M - 56 - qs, by + 46))
    t = '견본: 낭만 부동산 분석 플랫폼'; f = F('Medium', 30); d.text((W - M - 40 - d.textlength(t, font=f), by + 56 + qs), t, font=f, fill=GREY)
    return im

if __name__ == '__main__':
    OD = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(OD, exist_ok=True)
    page_blog({}).save(os.path.join(OD, 'letter_blog.png'), dpi=(DPI, DPI))
