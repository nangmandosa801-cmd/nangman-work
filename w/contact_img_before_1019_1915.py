# 10/19 17:43 사용자 규칙: 네이버 글의 전화번호 · 연락 안내는 글자가 아니라 그림으로 넣는다.
# 연락 안내 상자(배경 #F4F6FA · 왼쪽 남색 띠)를 가로 966px 그림으로 그린다. 글꼴은 기존 연락처 그림과 같은 Noto Sans CJK KR.
# 사용: from contact_img import box_png; box_png(첫줄, out, end=False, line2=None)
import os, sys, re, shutil, datetime
from PIL import Image, ImageDraw, ImageFont

PHONE = '010-2882-8165'
NAVY = (31, 56, 100); BG = (244, 246, 250); BAND = (127, 150, 184)
DARK = (51, 51, 51); RED = (176, 58, 46); GREY = (85, 85, 85)
_FD = '/usr/share/fonts/opentype/noto/'
def _f(w, s):
    return ImageFont.truetype(_FD + {'b': 'NotoSansCJK-Bold.ttc', 'm': 'NotoSansCJK-Medium.ttc', 'k': 'NotoSansCJK-Black.ttc'}[w], s, index=1)

W = 966; BAR = 16; PADL = 44; PADR = 36
LINE2 = '현관 · 창 사진 한 장 문자로 보내 주시면 무료로 봐 드립니다'
SALE = '11월 30일까지 연락한 집은 견적 금액에서 5% 할인'
FOOT = '낭만 인테리어 · 시공은 제휴 시공팀이 맡습니다. 계약이 되면 수수료를 받습니다.'

def _wrap(d, text, font, maxw):
    if d.textlength(text, font=font) <= maxw:
        return [text]
    # 1) 쉼표 · 마침표 뒤에서 끊기(첫 줄이 들어가는 것 중 가장 긴 것)
    best = None
    for sep in (', ', '. '):
        i = 0
        while True:
            j = text.find(sep, i)
            if j < 0: break
            a = text[:j + 1].strip(); b = text[j + 1:].strip()
            if d.textlength(a, font=font) <= maxw and (best is None or len(a) > len(best[0])):
                best = (a, b)
            i = j + 1
    if best:
        return [best[0]] + _wrap(d, best[1], font, maxw)
    # 2) 띄어쓰기에서 두 줄 길이가 가장 비슷하게 끊기(가운뎃점 앞뒤에서는 끊지 않음)
    ws = text.split(' '); cands = []
    for k in range(1, len(ws)):
        if ws[k] == '·' or ws[k - 1] == '·': continue
        a = ' '.join(ws[:k]); b = ' '.join(ws[k:])
        wa = d.textlength(a, font=font)
        if wa <= maxw:
            cands.append((max(wa, d.textlength(b, font=font)), a, b))
    if cands:
        _, a, b = min(cands)
        return [a] + _wrap(d, b, font, maxw)
    return [text]

def _sale_on():
    try:
        sys.path.insert(0, '/home/claude/blogkit'); import discount1130 as _D
        return _D.ON
    except Exception:
        return datetime.date.today() <= datetime.date(2026, 11, 30)

def box_png(head, out, end=False, line2=None, phone=PHONE, foot=None):
    # 10/19 18:01 할인 줄은 discount1130.ON일 때만(12/1부터 저절로 빠짐) · foot: 끝 그림 아래 회색 줄(기본 낭만 인테리어)
    sale = _sale_on()
    spec = [(head, _f('b', 40), NAVY, 14),
            (line2 or LINE2, _f('b', 36), DARK, 12 if sale else 22)]
    if sale:
        spec.append((SALE, _f('b', 36), RED, 22))
    spec.append(('전화 · 문자  ' + phone, _f('k', 64), NAVY, 0))
    if end:
        spec.append((foot or FOOT, _f('m', 34), GREY, 0))
    tmp = Image.new('RGB', (W, 10)); d = ImageDraw.Draw(tmp)
    maxw = W - BAR - PADL - PADR
    rows = []
    for k, (t, f, c, gap) in enumerate(spec):
        ls = _wrap(d, t, f, maxw)
        for i, l in enumerate(ls):
            asc, desc = f.getmetrics()
            h = int(f.size * 1.32)
            rows.append([l, f, c, h, gap if i == len(ls) - 1 else 2, k])
    top = 46; bot = 46; H = top + bot + sum(r[3] + r[4] for r in rows)
    if end: H += 22
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, BAR - 1, H), fill=NAVY)
    d.rectangle((BAR, 0, W, 5), fill=BAND); d.rectangle((BAR, H - 6, W, H), fill=BAND)
    y = top; x0 = BAR + PADL
    for l, f, c, h, gap, k in rows:
        if end and k == len(spec) - 1 and rows[[r[5] for r in rows].index(k)][0] == l:
            y += 10
            d.line((x0, y, W - PADR, y), fill=(200, 208, 222), width=2); y += 12
        b = f.getbbox(l)
        d.text((x0, y + (h - (b[3] - b[1])) / 2 - b[1]), l, font=f, fill=c)
        y += h + gap
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    im.save(out, optimize=True)
    return im


# ───────── 10/19 18:01 사용자 「앞으로 모든 글에 맨위 안내 끝안내 넣자」 ─────────
# 네이버 원고(낭만 인테리어 champion_chart · 낭만 부동산 분석 플랫폼 dong_jin_kim)마다 제목 바로 아래(본문 맨 위) 「맨위 안내」 그림,
# 본문 맨 끝 「끝 안내」 그림. 붙여넣기 사진 폴더 이름은 0-1_맨위안내(0_썸네일 다음) · 9-9_끝안내(9_배너 다음).
# 끝 안내 그림이 예전 「내 템플릿」(공통 연락처 그림 + 수수료 두 문장) 몫을 한다 → 템플릿은 쓰지 않는다.
TOP_NAME, END_NAME = '0-1_맨위안내.png', '9-9_끝안내.png'
NM_FOOT = '낭만 부동산 분석 플랫폼 · 시공 · 이사는 제휴 팀이 맡습니다. 계약이 되면 수수료를 받습니다. 매수 · 매도를 권하지 않습니다.'
# (제목에 든 말, 견적 품목 이름, 사진 보낼 곳)
_ITEMS = [('입주청소', '입주청소', '현관 · 창 · 욕실'), ('청소', '청소', '현관 · 창 · 욕실'),
          ('방묘문', '방묘문', '현관'), ('방묘창', '방묘창', '창'), ('중문', '중문', '현관'), ('현관문', '현관문', '현관'),
          ('코킹', '코킹', '창'), ('실리콘', '실리콘', '창'), ('누수', '누수', '창'), ('결로', '결로', '창'), ('곰팡이', '곰팡이', '창'),
          ('샷시', '샷시', '창'), ('모헤어', '모헤어', '창'), ('방충망', '방충망', '창'), ('단열', '단열', '창'), ('외풍', '외풍차단', '창'),
          ('방풍', '방풍', '창'), ('뽁뽁이', '단열', '창'), ('문풍지', '외풍차단', '창'), ('로이유리', '샷시', '창'), ('창문', '창문', '창'),
          ('창틀', '창틀', '창'), ('줄눈', '줄눈', '욕실'), ('탄성', '탄성코트', '욕실'), ('욕실', '욕실', '욕실'), ('타일', '타일', '욕실'),
          ('필름', '필름', '주방 · 문'), ('싱크대', '싱크대 필름', '주방 · 문'), ('매트', '매트', '거실 바닥'),
          ('에어컨', '에어컨', '거실'), ('보일러', '보일러', '현관 · 창 · 욕실'), ('새집증후군', '새집증후군 시공', '현관 · 창 · 욕실')]
_TAILW = ('설치', '시공', '공사', '교체', '비용', '가격', '추천', '방법', '해결', '업체', '비교', '효과', '뜻', '종류', '두께', '제거', '보수', '셀프', '사이즈', '수리')

def _kw(T):
    return re.split(r'[,|]', T, 1)[0].strip()

def int_texts(T, head=None, line2=None):
    """낭만 인테리어 글 제목 → (첫 줄, 둘째 줄). 넘겨받은 값이 있으면 그대로 쓴다"""
    k = _kw(T); khit = next((x for x in _ITEMS if x[0] in k), None); hit = khit or next((x for x in _ITEMS if x[0] in T), None)
    if head is None:
        w = k.split()
        while len(w) > 1 and w[-1] in _TAILW: w.pop()
        x = ' '.join(w)
        for suf in ('공사', '시공', '설치', '교체'):
            if x.endswith(suf) and len(x) > len(suf) + 1 and x[-len(suf) - 1] != ' ': x = x[:-len(suf)]
        if khit is None: x = '중문 · 창틀 코킹 · 입주청소'   # 앞머리에 품목이 없는 정보 글(예 전세집 수리 범위)
        elif hit[0] not in x and hit[1] not in x: x = x + ' ' + hit[1]
        head = f'{x} 견적, 두 곳을 나란히 보여 드립니다'
    if line2 is None:
        line2 = f'{hit[2] if hit else "현관 · 창 · 욕실"} 사진 한 장 문자로 보내 주시면 무료로 봐 드립니다'
    return head, line2

_NMTAIL = ('아파트', '시세', '매매', '분양가', '이주', '전세', '월세', '거래량', '순위', '줍줍', '무순위', '청약', '본청약', '입주', '입주일', '재건축', '재개발', '집값', '땅값', '보상', '임의공급', '관리처분인가', '부동산', '가격')
def nm_texts(T, place=None, head=None, line2=None):
    """낭만 부동산 글 제목 → (첫 줄, 둘째 줄)"""
    k = _kw(T)
    if place is None:
        w = k.split()
        while len(w) > 1 and (w[-1] in _NMTAIL or re.fullmatch(r'[\d~～.]+(?:월|일|년|차|회)?', w[-1])): w.pop()
        place = ' '.join(w)
        if re.search(r'억|한도|금리|대출|기준|뜻|조건|일정|방법|절차|계산|세금|종부세|수익률|건폐율|용적률', place): place = ''   # 지역 · 단지가 아닌 앞머리
    if head is None:
        what = '이주 · 이사 준비' if '이주' in k else '입주 · 이사 준비'
        head = f'{place} {what}, 중문 · 입주청소 · 이사 견적을 두 곳씩 나란히 보여 드립니다'.strip()
    return head, (line2 or '사진 한 장 문자로 보내 주시면 무료로 봐 드립니다')

def pair_png(head, line2, top_out, end_out, foot=None):
    box_png(head, top_out, end=False, line2=line2)
    box_png(head, end_out, end=True, line2=line2, foot=foot)
    return top_out, end_out

# 붙여넣기 점선 칸 (changgo/simplify.py box와 같은 꼴)
def _pbox(inner):
    return ('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr>'
            '<td style="border:2px dashed #C7D6E6;padding:16px;text-align:center;">' + inner + '</td></tr></table>')
GUIDE = ('<!-- NOTICE_GUIDE -->' + _pbox('<span style="font-size:18px;font-weight:700;color:#B03A2E;">[안내 · 이 칸은 지우세요]</span><br>'
         '<span style="font-size:16px;color:#6B7785;">네이버 「내 템플릿」(연락처 그림 · 수수료 두 문장)은 넣지 않습니다. 맨 끝 「9-9_끝안내」 그림이 그 몫을 합니다.</span>') + '<p><br></p>\n')
TOPBOX = '<!-- NOTICE_TOP -->' + _pbox('<span style="font-size:20px;font-weight:700;color:#1F3864;">[맨위 안내]</span><br><span style="font-size:16px;color:#6B7785;">이 칸을 지우고 사진 폴더 「0-1_맨위안내」를 올리세요</span>') + '<p><br></p>\n'
ENDBOX = '<!-- NOTICE_END -->' + _pbox('<span style="font-size:20px;font-weight:700;color:#1F3864;">[끝 안내]</span><br><span style="font-size:16px;color:#6B7785;">이 칸을 지우고 사진 폴더 「9-9_끝안내」를 올리세요</span>') + '<p><br></p>\n'
_TAGP = re.compile(r'<p style="font-size:17px;color:#8A8578;">\s*#')
_DISCP = re.compile(r'<p style="font-size:14px;color:#A8A296;">\s*시공은 제휴 (?:업체가|시공팀이) 맡습니다\. 계약이 되면 수수료를 받습니다\.\s*</p>\s*(?:<p><br></p>\s*)?')

def _put_end(t, block):
    m = _DISCP.search(t)
    if m: return t[:m.start()] + block + '\n' + t[m.end():]
    m = _TAGP.search(t)
    if m: return t[:m.start()] + block + '\n<p><br></p>\n\n' + t[m.start():]
    return t.rstrip() + '\n<p><br></p>\n' + block

def _put_top(t, block):
    m = re.match(r'\s*<!--[^>]*?-->\s*\n?', t)   # <!-- 제목: … --> 줄 바로 뒤 = 본문 맨 위
    i = m.end() if m else 0
    return t[:i] + block + '\n' + t[i:]

def post_add_int(h, slug, T, d, PH, head=None, line2=None):
    """원고(post.html) 짓기 — 두 그림을 d에 만들고 맨 위 · 맨 끝에 그림 자리를 넣는다(DISC 문장 자리는 끝 그림이 대신)"""
    if f'nangman_interior_{slug}_top.png' in h: return h
    a, b = int_texts(T, head, line2)
    pair_png(a, b, os.path.join(d, f'nangman_interior_{slug}_top.png'), os.path.join(d, f'nangman_interior_{slug}_end.png'))
    h = _put_top(h, PH(f'nangman_interior_{slug}_top.png — 낭만 인테리어 안내 · 맨위 안내 그림(연락 · 할인 · 번호)'))
    return _put_end(h, PH(f'nangman_interior_{slug}_end.png — 낭만 인테리어 안내 · 끝 안내 그림(연락 · 수수료 고지)'))

_PHRE = r'(?:<br>|<p><br></p>)?\s*<table[^>]*>\s*<tr>\s*<td style="border:1px dashed[^"]*"[^>]*>(?:(?!</table>).)*?nangman_interior_[\w\-]+_{k}\.png(?:(?!</table>).)*?</td>\s*</tr>\s*</table>\s*(?:<br>|<p><br></p>)?'
def paste_take(t):
    """simplify 앞단 — 원고의 _top / _end 그림 자리를 표시로 바꿔 사진 묶음에 섞이지 않게 한다"""
    t = re.sub(_PHRE.format(k='top'), '<!-- NOTICE_TOP_AT -->', t, count=1, flags=re.S)
    t = re.sub(_PHRE.format(k='end'), '<!-- NOTICE_END_AT -->', t, count=1, flags=re.S)
    return t

def paste_add_int(t, photo_dir, T=None, src_dir=None, slug=None, head=None, line2=None):
    """붙여넣기 html에 안내 줄 · 맨위 · 끝 칸을 넣고 사진 폴더에 0-1_맨위안내 · 9-9_끝안내를 둔다. 이미 있으면 그대로"""
    os.makedirs(photo_dir, exist_ok=True)
    if T is None:
        m = re.search(r'<!--\s*제목:\s*(.*?)\s*-->', t); T = m.group(1) if m else ''
    src = [os.path.join(src_dir or '', f'nangman_interior_{slug}_{k}.png') for k in ('top', 'end')]
    if src_dir and slug and all(os.path.exists(x) for x in src) and head is None and line2 is None:
        shutil.copy(src[0], os.path.join(photo_dir, TOP_NAME)); shutil.copy(src[1], os.path.join(photo_dir, END_NAME))
    else:
        a, b = int_texts(T, head, line2)
        pair_png(a, b, os.path.join(photo_dir, TOP_NAME), os.path.join(photo_dir, END_NAME))
    if 'NOTICE_TOP -->' not in t:
        t = t.replace('<!-- NOTICE_TOP_AT -->', TOPBOX, 1) if 'NOTICE_TOP_AT' in t else _put_top(t, TOPBOX)
    if 'NOTICE_END -->' not in t:
        t = t.replace('<!-- NOTICE_END_AT -->', ENDBOX, 1) if 'NOTICE_END_AT' in t else _put_end(t, ENDBOX)
    if 'NOTICE_GUIDE' not in t:
        t = _put_top(t, GUIDE)
    return t

def post_add_nm(h, slug, T, d, PH, place=None, head=None, line2=None):
    """낭만 부동산 원고 — nangman_<slug>_top.png · _end.png를 d에 만들고 본문 맨 위 · 태그 상자 앞에 그림 자리를 넣는다"""
    a, b = nm_texts(T, place, head, line2)
    pair_png(a, b, os.path.join(d, f'nangman_{slug}_top.png'), os.path.join(d, f'nangman_{slug}_end.png'), foot=NM_FOOT)
    if f'nangman_{slug}_top.png' in h: return h
    h = PH(f'nangman_{slug}_top.png — 맨위 안내 그림(연락 · 할인 · 번호) · 제목 바로 아래') + h
    m = re.search(r'<table[^>]*>\s*<tr><td[^>]*>\s*<span style="font-size:16px;color:#8A8578;">태그</span>', h)
    blk = PH(f'nangman_{slug}_end.png — 끝 안내 그림(연락 · 수수료 고지) · 본문 맨 끝')
    return (h[:m.start()] + blk + h[m.start():]) if m else (h + blk)

if __name__ == '__main__':
    box_png(sys.argv[1], sys.argv[2], end=len(sys.argv) > 3 and sys.argv[3] == 'end')
