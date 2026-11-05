#!/usr/bin/env python3
"""네이버 낭만 인테리어 글 → 티스토리(nangmaninterior) 요약 글 만들기 (11/5 사용자 「안 쓴 글 찾아서 티스토리로 확장」)
사용: python3 ts_expand.py <logNo> [<logNo> ...]
  1) 네이버 글 본문 · 표 · 사진을 읽는다
  2) ChatGPT(블로그 우체통 gpt)에게 같은 사실로 다른 문장의 짧은 요약 글(JSON)을 받는다 — 지어내기 · 업체 이름 금지
  3) 시공 사진 한 장을 낭만 창고(구글)에 올려 맨 위 대표 사진으로
  4) /home/claude/w/ts_expand/ts_<logNo>.html + list.json(제목 · 태그 · 원문)
나온 html 은 드라이브 「블로그/협업/4_어사이드」로 올려 어사이드가 발행한다.
"""
import sys, os, re, json, html, urllib.request, urllib.parse
sys.path.insert(0, '/home/claude/helper'); sys.path.insert(0, '/home/claude/tools/followup')
from gas import call
from post_followup import is_banner
OUT = '/home/claude/w/ts_expand'; os.makedirs(OUT, exist_ok=True)
N = 'https://blog.naver.com/champion_chart/'
H = {'User-Agent': 'Mozilla/5.0'}; HI = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://blog.naver.com/'}
def get(u, h=H): return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25).read()
BAN = ['갈렸', '갈랐', '고요.', '최고', '프리미엄', '놓치면 손해', '이번 달만']
SYS = """너는 한국어 블로그 편집자다. 네이버 원문을 티스토리용 짧은 요약 글로 다시 쓴다.
규칙: 원문에 있는 사실 · 숫자만 쓴다(새 정보 · 후기 · 과장 금지). 원문 문장을 그대로 베끼지 말고 다른 문장으로 쓴다.
아주 쉬운 일상어, 짧은 문장, 「~습니다」체. 「~고요」 금지, 「갈렸다 · 갈랐다」 금지, 할인율 숫자 · 기한 압박 금지, 업체 이름 · 업체 전화 금지.
제목은 원제목의 검색어(쉼표 앞)를 맨 앞에 그대로 두고 35자 안. 소제목은 검색어를 넣은 질문형.
JSON만: {"title":"","lead":"2문장","sections":[{"h":"소제목","p":"2~3문장"}],"tags":["5개"]} sections는 4~5개."""
td = 'style="border:1px solid #ccc;padding:8px"'
def T(rows):
    if not rows: return ''
    h = ''.join(f'<th {td}>{x}</th>' for x in rows[0])
    r = ''.join('<tr>' + ''.join(f'<td {td}>{c}</td>' for c in row) + '</tr>' for row in rows[1:])
    return f'<table style="width:100%;border-collapse:collapse"><tbody><tr>{h}</tr>{r}</tbody></table>'
ASK = ('<div style="background:#FFF8EC;border:1px solid #E8D9B5;border-radius:10px;padding:14px 16px;margin:14px 0"><b>사진 한 장이면 됩니다</b><br>'
       '문제 생긴 곳 사진 한 장과 사는 동네를 문자로 보내 주세요. 가까운 시공팀을 이어 드립니다.<br>문자 · 전화 <b>010-2882-8165</b></div>')
def titles():
    f = f'{OUT}/naver_titles.json'
    if os.path.exists(f): return json.load(open(f))
    D = {}
    for p in range(1, 12):
        s = get(f'https://blog.naver.com/PostTitleListAsync.naver?blogId=champion_chart&currentPage={p}&countPerPage=30').decode('utf8', 'ignore')
        r = re.findall(r'"logNo":"(\d+)","title":"(.*?)"', s)
        if not r: break
        for n, t in r: D[n] = html.unescape(urllib.parse.unquote_plus(t))
    json.dump(D, open(f, 'w'), ensure_ascii=False); return D
def related(no, title, D, k=5):
    words = [w for w in re.split(r'[\s,·]+', re.split(r'[,，]', title)[0]) if len(w) >= 2]
    sc = []
    for n, t in D.items():
        if n == no: continue
        s = sum(2 if w in t else 0 for w in words) + sum(1 for w in ['중문', '줄눈', '입주청소', '사전점검', '도어락', '결로', '누수', '코킹', '곰팡이', '동파'] if w in t and w in title)
        if s: sc.append((s, n, t))
    sc.sort(reverse=True); L = [(n, t) for _, n, t in sc[:k]]
    for n, t in D.items():
        if len(L) >= k: break
        if n != no and (n, t) not in L: L.append((n, t))
    return L
def one(no, D):
    v = get(f'https://blog.naver.com/PostView.naver?blogId=champion_chart&logNo={no}').decode('utf8', 'ignore')
    title = D.get(no) or re.search(r'<title>(.*?)</title>', v).group(1).replace(' : 네이버 블로그', '')
    b = v[v.find('se-main-container'):]
    b = b[:b.find('같이 보면 좋은 글')] if '같이 보면 좋은 글' in b else b
    txt = re.sub(r'\s+', ' ', re.sub(r'\{[^{}]*\}', '', re.sub('<[^>]+>', ' ', html.unescape(b)))).replace('​', '').strip()
    tables = []
    for tb in re.findall(r'<table.*?</table>', b, re.S)[:2]:
        rows = [[re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', c))).replace('​', '').strip() for c in re.findall(r'<td.*?</td>', tr, re.S)] for tr in re.findall(r'<tr.*?</tr>', tb, re.S)]
        rows = [r for r in rows if any(r)]
        if len(rows) >= 2 and all(len(r) == len(rows[0]) for r in rows): tables.append(rows)
    j = json.loads(call('gpt', system=SYS, user=f'원제목: {title}\n원문:\n{txt[:6000]}'))
    # 사진: 첫 장(표지) 빼고 배너 아닌 첫 사진
    img = ''
    for u in [x.split('?')[0] for x in re.findall(r'(https://postfiles\.pstatic\.net/[^"\'\s<>]+)', b)][1:8]:
        try:
            p = f'{OUT}/_img_{no}.jpg'; open(p, 'wb').write(get(u + '?type=w966', HI))
            if is_banner(p): continue
            r = call('image', name=f'ts_{no}.jpg', b64=__import__('base64').b64encode(open(p, 'rb').read()).decode())
            img = r.get('url') if isinstance(r, dict) else r; break
        except Exception: continue
    secs = j.get('sections', [])
    h = (f'<p><img src="{img}" alt="{j["title"]}" style="width:100%"><br><span style="font-size:13px;color:#666">제휴 시공팀 현장 사진</span></p>' if img else '')
    h += f'<p><b>{j.get("lead", "")}</b></p>' + ASK
    for i, s in enumerate(secs):
        h += f'<h2>{s["h"]}</h2><p>{s["p"]}</p>'
        if i < len(tables): h += T(tables[i])
    h += ASK + f'<p>사진이 더 많은 원문: <a href="{N}{no}">{title}</a></p>'
    h += '<h2>같이 보면 좋은 글</h2><ul>' + ''.join(f'<li><a href="{N}{n}">{t}</a></li>' for n, t in related(no, title, D)) + '</ul>'
    bad = [w for w in BAN if w in h]
    open(f'{OUT}/ts_{no}.html', 'w').write(h)
    return {'no': no, 'title': j['title'], 'tags': ','.join(j.get('tags', [])[:5]), 'orig': title, 'img': bool(img), 'tables': len(tables), 'bad': bad, 'chars': len(re.sub('<[^>]+>', '', h))}
if __name__ == '__main__':
    D = titles(); lf = f'{OUT}/list.json'; L = json.load(open(lf)) if os.path.exists(lf) else []
    done = {x['no'] for x in L}
    for no in sys.argv[1:]:
        if no in done: continue
        try: r = one(no, D); L.append(r); print(json.dumps(r, ensure_ascii=False), flush=True)
        except Exception as e: print(json.dumps({'no': no, 'error': str(e)[:150]}, ensure_ascii=False), flush=True)
        json.dump(L, open(lf, 'w'), ensure_ascii=False, indent=1)
