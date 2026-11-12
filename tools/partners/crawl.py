#!/usr/bin/env python3
"""제휴 업체 네이버 블로그 새 글 · 사진 모으기 (11/5 사용자 「제휴 업체 블로그 새로운 그림 내용을 충분히 가지고 와서 그걸 활용해」)
사용: python3 crawl.py [글 수=15]   → 업체마다 최근 글 중 아직 안 받은 것만
결과: /home/claude/w/partners/pool.json (글마다 업체 · 종목 · 제목 · 날짜 · 본문 앞 2,500자 · 사진 주소 · 사진 규칙)
      사진: /home/claude/v2src/partners/<업체>/<logNo>/NN.jpg (저장소에 안 올라감 → 새 창은 pool.json 주소로 다시 받음)
비치움(lnr0724) · 다정실리콘(s0097s, 사진 광고 불가)은 넣지 않는다. 사진 규칙은 마스터현황 문서 기준.
"""
import urllib.request, urllib.parse, re, html, json, os, sys, time
P = {  # 블로그 id: (약자, 종목, 사진 규칙)
 'amrita2580':      ('ㄷㄹㅎㅇㅅ', '입주청소 · 줄눈 · 탄성 · 새집증후군', '허락'),
 'lmg4455':         ('ㅁㄱ 줄눈', '줄눈 · 케라폭시', '쓰던 대로(가공)'),
 'door-diy777':     ('ㅍㄹㅊ 중문', '중문 · 무타공', '허락'),
 'flowhc':          ('ㅍㄹㅇ 홈케어', '무타공 중문 · 설비 · 도기', '허락'),
 'specialcoking':   ('ㅅㅍㅅ 코킹', '외벽 · 창틀 코킹', '허락'),
 'febric_cleaning': ('ㅁㄲㅎㄱ 단열', '결로 · 단열 · 곰팡이', '가공해서만'),
 'dd2homecare':     ('ㄷㄷ 홈케어', '사전점검', '허락 · 사진에 작게 이름 표기'),
 'doors9774':       ('ㅁㅅㄹ ㅇㅂㅈ', '중문 수리', '허락(10/21 사진 받음)'),
}
H = {'User-Agent': 'Mozilla/5.0'}; HI = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://blog.naver.com/'}
POOL = '/home/claude/w/partners/pool.json'; IMG = '/home/claude/v2src/partners'
def get(u, h=H): return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=20).read()
def main(n=15, noimg=False):
    pool = json.load(open(POOL)) if os.path.exists(POOL) else {}
    new = []
    for bid, (ab, kind, rule) in P.items():
        s = ''
        for pg in range(1, (n + 29) // 30 + 1):
            try: s += get(f'https://blog.naver.com/PostTitleListAsync.naver?blogId={bid}&currentPage={pg}&countPerPage={min(n, 30)}').decode('utf8', 'ignore')
            except Exception as e: print(bid, 'list_err', e); break
        for no, t, d in re.findall(r'"logNo":"(\d+)","title":"(.*?)".*?"addDate":"(.*?)"', s):
            k = f'{bid}/{no}'
            if k in pool: continue
            try:
                v = get(f'https://blog.naver.com/PostView.naver?blogId={bid}&logNo={no}').decode('utf8', 'ignore')
            except Exception: continue
            b = v[v.find('se-main-container'):] if 'se-main-container' in v else v
            txt = re.sub(r'\s+', ' ', re.sub(r'\{[^{}]*\}', '', re.sub('<[^>]+>', ' ', html.unescape(b)))).strip()
            imgs = []
            for x in re.findall(r'(https://postfiles\.pstatic\.net/[^"\'\s<>?]+)', b):
                if x not in imgs: imgs.append(x)
            d0 = f'{IMG}/{bid}/{no}'; os.makedirs(d0, exist_ok=True); got = 0
            for i, u in enumerate([] if noimg else imgs[:30]):
                f = f'{d0}/{i:02d}.jpg'
                if os.path.exists(f): got += 1; continue
                try: open(f, 'wb').write(get(u + '?type=w966', HI)); got += 1
                except Exception: pass
            pool[k] = {'blog': bid, 'abbr': ab, 'kind': kind, 'photo_rule': rule, 'logNo': no,
                       'title': urllib.parse.unquote_plus(t), 'date': d, 'text': txt[:4000], 'imgs': imgs[:30], 'got': got}
            new.append(k); time.sleep(0.3)
            os.makedirs(os.path.dirname(POOL), exist_ok=True); json.dump(pool, open(POOL, 'w'), ensure_ascii=False, indent=0)
    os.makedirs(os.path.dirname(POOL), exist_ok=True)
    json.dump(pool, open(POOL, 'w'), ensure_ascii=False, indent=0)
    print(json.dumps({'new': len(new), 'total': len(pool), 'by_blog': {b: sum(1 for k in new if k.startswith(b + '/')) for b in P}}, ensure_ascii=False))
if __name__ == '__main__': main(int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 15, '--noimg' in sys.argv)
