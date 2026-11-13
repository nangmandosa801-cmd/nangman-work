#!/usr/bin/env python3
"""낭만 부동산 요일 코너 원고 한 편이 지나가는 길을 한 도구로 (11/14 · 정기 작업 「낭만 부동산 요일 코너 원고」가 씀)
원고 폴더 = /home/claude/helper/s20/<slug>/  (ana.py → ana.json · fig.py → img/nangman_<slug>_*.png · mk.py → post.html · urls.json)
꼴은 helper/s20/salary_map(킬러 1호)과 salary_5000 을 본뜬다.

  python3 corner.py new <slug>                 폴더 · kit.py · tails.py 만들기
  python3 corner.py thumb <slug> "위 작은 줄" "큰 줄 1" "큰 줄 2" "숫자 하나" "아래 설명"     대표 사진(01 · 남색 정사각 카드)
  python3 corner.py build <slug> [--fig]       (그림 없으면 fig.py · 그래도 없으면 urls.json 주소에서 받기) → 새 그림 올리기 → mk.py → 금지어 · 1차 QA → 어사이드용 html · txt · NN.jpg
  python3 corner.py up <slug> [--text] [--end] 드라이브 「4_어사이드/원고/새코너/<slug>/」에 올리기(--text 글자만 · --end 검수 끝 폴더에도 txt)
  python3 corner.py submit <slug>              ChatGPT 자연스러움 검수 대기 폴더에 nangman_<slug>.txt
  python3 corner.py block <slug> --when "2026-11-25(수) 17:00" [--cat "부동산 분석"]    어사이드 지시 파일(상태: 검수중) 만들어 올리기
  python3 corner.py result <slug>              검수 결과가 왔나(없으면 exit 3) → 폴더에 gpt.json 저장
  python3 corner.py fix <slug>                 gpt.json 의 고침을 mk.py 문장에 반영(숫자 · 제목 · 소제목 · 근거 줄은 그대로)
  python3 corner.py ready <slug> [--when "..."] 지시 블록을 「상태: 대기」로 + 어사이드 교신 한 통(예약 부탁)
  python3 corner.py clip <slug>                ChatGPT 클립 재료(원고의 30초 요약 · 질문 소제목 · 그림 02~04) 올리기 + 교신 한 통
  python3 corner.py reedit <slug>              이미 예약 지시가 나간 글(장부 mode: reedit)의 글자만 고쳤을 때 — html · txt 만 올리고 어사이드에 본문 다시 채우기 교신
  python3 corner.py status                     corner_plan.json 을 표로
한 편의 순서: new → (ana · fig · mk 쓰기) → thumb → build → up → submit → block  …검수…  result → fix → build → up --end → ready
계획 · 상태 장부: helper/s20/corner_plan.json (date · time · corner · slug · title · state: todo | 검수중 | 대기 | 완료)"""
import sys, os, json, re, glob, shutil, subprocess, time, datetime

S20 = os.path.dirname(os.path.abspath(__file__))
GAS = '/home/claude/helper/gas.py'; PK = '/home/claude/tools/postkit'; OUT = '/home/claude/w/aside_out'
DRV = '블로그/협업/4_어사이드'; REV = '블로그/협업/검수_자연스러움'; WORK = '/home/claude/w/corner'
PLAN = os.path.join(S20, 'corner_plan.json')
BAN = ['까닭', '갈라', '갈렸', '갈랐', '고요.', '가능성', '뿐만 아니라', '여러분', '살펴보겠', '알아보겠', '정리해 보겠', '이 글에서는']
os.environ.setdefault('TZ', 'Asia/Seoul'); time.tzset()


def sh(*a, cwd=None):
    r = subprocess.run(list(a), capture_output=True, text=True, cwd=cwd)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def gas(*a):
    rc, o = sh('python3', GAS, *a)
    return rc == 0 and '"id"' in o, o


def J(x): print(json.dumps(x, ensure_ascii=False))


def plan_load(): return json.load(open(PLAN, encoding='utf8')) if os.path.exists(PLAN) else {'posts': []}
def plan_save(p): json.dump(p, open(PLAN, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
def plan_set(slug, **kw):
    p = plan_load(); e = next((x for x in p['posts'] if x.get('slug') == slug), None)
    if e is None: e = {'slug': slug}; p['posts'].append(e)
    e.update(kw); plan_save(p); return e


def folder(slug):
    d = os.path.join(S20, slug)
    if not os.path.isdir(d): raise SystemExit('폴더 없음: ' + d)
    return d


def title_of(d):
    m = re.search(r"^TITLE\s*=\s*['\"](.+?)['\"]\s*$", open(os.path.join(d, 'mk.py'), encoding='utf8').read(), re.M)
    return m.group(1) if m else ''


def font(size, serif=True):
    from PIL import ImageFont
    for q in (('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc',) if serif else ()) + ('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'):
        if not os.path.exists(q): continue
        for i in range(10):
            try: f = ImageFont.truetype(q, size, index=i)
            except Exception: break
            if 'KR' in ' '.join(f.getname()): return f
    pre = '/home/claude/tools/tistory/fonts/Pretendard-Bold.otf'
    return ImageFont.truetype(pre, size) if os.path.exists(pre) else ImageFont.load_default()


def cmd_new(slug):
    d = os.path.join(S20, slug); os.makedirs(os.path.join(d, 'img'), exist_ok=True)
    k = open(os.path.join(S20, 'salary_map', 'kit.py'), encoding='utf8').read().replace('nangman_salary_map_', f'nangman_{slug}_')
    open(os.path.join(d, 'kit.py'), 'w', encoding='utf8').write(k)
    shutil.copy('/home/claude/helper/pg/tails.py', os.path.join(d, 'tails.py'))
    if not os.path.exists(os.path.join(d, 'urls.json')): open(os.path.join(d, 'urls.json'), 'w').write('{}')
    J({'ok': True, 'dir': d, 'img_prefix': f'img/nangman_{slug}_<키>.png', '본뜰 글': 'helper/s20/salary_5000 (ana.py · fig.py · mk.py)'})


def cmd_thumb(slug, top, l1, l2, big, sub):
    from PIL import Image, ImageDraw
    d = folder(slug); os.makedirs(os.path.join(d, 'img'), exist_ok=True)
    W = 1000; im = Image.new('RGB', (W, W), '#203864'); dr = ImageDraw.Draw(im)
    dr.rectangle([0, 0, W, 14], fill='#D4B04C'); dr.rectangle([0, W - 14, W, W], fill='#D4B04C')
    dr.text((70, 95), top, font=font(28, False), fill='#AFC0D8', anchor='lm')
    dr.line([70, 248, 930, 248], fill='#3A5A8A', width=3); dr.line([70, 782, 930, 782], fill='#3A5A8A', width=3)
    for txt, y, sz, col in ((l1, 360, 80, '#F4F1EA'), (l2, 485, 60, '#F4F1EA'), (big, 605, 100, '#D4B04C')):
        f = font(sz)
        while dr.textlength(txt, font=f) > 880 and sz > 36: sz -= 4; f = font(sz)     # 길면 줄여서 한 줄에
        dr.text((W / 2, y), txt, font=f, fill=col, anchor='mm')
    dr.text((W / 2, 715), sub, font=font(32, False), fill='#AFC0D8', anchor='mm')
    out = os.path.join(d, 'img', f'nangman_{slug}_thumb.png'); im.save(out); J({'ok': True, 'thumb': out})


def ensure_imgs(slug, d, refig):
    pre = f'nangman_{slug}_'; img = os.path.join(d, 'img'); os.makedirs(img, exist_ok=True)
    up = os.path.join(d, 'urls.json'); U = json.load(open(up)) if os.path.exists(up) else {}
    have = lambda: {os.path.basename(f)[len(pre):-4] for f in glob.glob(os.path.join(img, pre + '*.png'))}
    note = []
    if os.path.exists(os.path.join(d, 'fig.py')) and (refig or not (have() - {'thumb'})):
        rc, o = sh('python3', 'fig.py', cwd=d)
        if rc: note.append('fig.py 실패: ' + o[-200:])
    miss = [k for k in U if k not in have()]
    if miss:                                    # 그림 파일은 저장소에 없다 → 이미 올려 둔 주소에서 받는다(글자만 고치는 새 창)
        import requests
        ca = os.path.expanduser('~/.ccr/ca-bundle.crt')
        for k in miss:
            try:
                r = requests.get(U[k], timeout=60, verify=ca if os.path.exists(ca) else True)
                if r.status_code == 200 and len(r.content) > 2000: open(os.path.join(img, pre + k + '.png'), 'wb').write(r.content)
            except Exception as e: note.append(f'{k} 받기 실패')
    new = [k for k in sorted(have()) if k not in U]
    for k in new:                               # 새 그림은 낭만 창고에 올려 주소를 urls.json 에
        rc, o = sh('python3', GAS, 'image', os.path.join(img, pre + k + '.png'))
        m = re.search(r'https?://[^\s"]+', o)
        if m: U[k] = m.group(0)
        else: note.append(f'{k} 올리기 실패')
    json.dump(U, open(up, 'w'), ensure_ascii=False, indent=0)
    if 'thumb' not in have(): note.append('대표 사진 없음 → corner.py thumb 먼저')
    return sorted(have()), note


def cmd_build(slug, refig=False):
    d = folder(slug); res = {'slug': slug}
    imgs, note = ensure_imgs(slug, d, refig); res['imgs'] = imgs
    rc, o = sh('python3', 'mk.py', cwd=d)
    if rc: J({'ok': False, 'why': 'mk.py 멈춤(숫자가 계산과 다르면 assert)', 'tail': o[-500:]}); sys.exit(1)
    t = open(os.path.join(d, 'post.txt'), encoding='utf8').read()
    res['ban'] = sorted({w for w in BAN if w in t})
    rc, o = sh('python3', os.path.join(S20, '_ban_check.py'), slug, cwd=S20)      # 부동산 글 금지어 목록(갈- · 까닭 · 견줘 · 봤습니다 …)
    try: res['ban'] = sorted(set(res['ban']) | set(json.loads(o.strip().split('\n')[-1]).get('ban', [])))
    except Exception: pass
    for links in [re.findall(r'https?://[^\s|]+', t)]:
        if any('champion_chart' in l or 'nangmaninterior' in l for l in links): res['ban'].append('인테리어 링크')
    rel = t.split('[같이 보면 좋은 글]')[-1] if '[같이 보면 좋은 글]' in t else ''
    res['related'] = rel.count('▶')
    for tool in ('html2aside.py', 'html2aside_html.py'):
        rc, o = sh('python3', os.path.join(PK, tool), d, f'nangman_{slug}')
        if rc: J({'ok': False, 'why': tool + ' 실패', 'tail': o[-400:]}); sys.exit(1)
    a = os.path.join(OUT, f'nangman_{slug}.txt'); at = open(a, encoding='utf8').read()
    res['chars'] = len(re.sub(r'\s', '', at)); res['photos'] = len(glob.glob(os.path.join(OUT, f'nangman_{slug}', '*.jpg')))
    q = '/home/claude/kit_dasi/selfqa.py'
    if os.path.exists(q):
        rc, o = sh('python3', q, a)
        try: res['selfqa_fail'] = [f for f in json.loads(o)['fail'] if '생일' not in f]
        except Exception: res['selfqa_fail'] = ['selfqa 읽기 실패']
    else: res['selfqa_fail'] = ['selfqa 없음(드라이브 블로그/dosa/_tools/dasi/dasi_kit.tgz 를 /home/claude/kit_dasi 에 풀기)']
    res['title'] = title_of(d); res['note'] = note
    res['ok'] = not res['ban'] and res['related'] == 3 and res['photos'] >= 2 and 'thumb' in imgs
    J(res)


def cmd_up(slug, text=False, end=False):
    folder(slug); st = f'/tmp/stg/{slug}'; shutil.rmtree(st, ignore_errors=True); os.makedirs(st)
    shutil.copy(f'{OUT}/nangman_{slug}.html', f'{st}/{slug}.html'); shutil.copy(f'{OUT}/nangman_{slug}.txt', f'{st}/{slug}.txt')
    fs = [f'{st}/{slug}.html', f'{st}/{slug}.txt'] + ([] if text else sorted(glob.glob(f'{OUT}/nangman_{slug}/*.jpg'))); ok = 0
    for f in fs:                                # 한 폴더 안은 순서대로(동시에 올리면 폴더가 둘로 갈라진다)
        ok += gas('fput', f'{DRV}/원고/새코너/{slug}', f)[0]
    if end: ok += gas('fput', f'{REV}/끝', f'{OUT}/nangman_{slug}.txt')[0]; fs.append('끝')
    J({'ok': ok == len(fs), 'files': len(fs), 'uploaded': ok, 'folder': f'{DRV}/원고/새코너/{slug}'})


def cmd_submit(slug):
    ok, o = gas('fput', f'{REV}/대기', f'{OUT}/nangman_{slug}.txt')
    if ok: plan_set(slug, state='검수중', submitted=time.strftime('%Y-%m-%d %H:%M'))
    J({'ok': ok, 'file': f'{REV}/대기/nangman_{slug}.txt'})


def jisi_path(slug):
    os.makedirs(WORK, exist_ok=True)
    e = next((x for x in plan_load()['posts'] if x.get('slug') == slug), {})
    return os.path.join(WORK, e.get('jisi') or f'지시_부동산_코너_{slug}.txt')


def cmd_block(slug, when, cat='부동산 분석'):
    d = folder(slug); t = title_of(d)
    body = f"""[네이버 낭만 부동산 분석 플랫폼(dong_jin_kim) · 요일 코너 글 1편 · {slug}]
작성: {time.strftime('%Y-%m-%d %H:%M')} 한국시간 · Claude(정기 작업 「낭만 부동산 요일 코너 원고」)

흐름: Claude 원고 → ChatGPT 자연스러움 검수 → Claude 반영 → 아래 블록이 「상태: 대기」가 되면 어사이드가 예약한다. 「상태: 검수중」이면 손대지 않는다.
방법: 0_지시 「어사이드_발행방식_1105.txt」대로 에디터에서 직접 작성. html 모양 그대로, 빨간 「▼ 사진 NN.jpg」 자리에 같은 폴더 NN.jpg. 글자 복사는 txt.
대표 사진: 01.jpg(남색 썸네일 카드)를 직접 대표로 지정한다. 예약 뒤 미리보기에서 대표가 01 인지 확인한다. 02.jpg 부터 본문 순서대로.
표와 맨 위 「30초 요약」 상자는 글자(표) 그대로 넣는다. 그림으로 바꾸지 않는다.
발행 뒤 확인: 본문에 ##, **, [CALL], <div, [사진, [소제목], [표] 같은 기호가 글자로 보이면 지우기.
연락처 · 홍보 상자 · 인테리어 링크 없음. 글 끝은 「같이 보면 좋은 글」 3줄뿐.

=== 블록 ===
[종류: 새 글]
제목: {t}
카테고리: {cat}
예약: {when}
  · 그 시각에 다른 예약 글이 이미 있으면 그 글은 그대로 두고 이 글을 다음 날 같은 시각으로(하루 2편 · 3시간 간격). 옮겼으면 보고에 적는다.
html: {DRV}/원고/새코너/{slug}/{slug}.html · 사진: 같은 폴더 01.jpg~ · 글자: {slug}.txt
태그: 원고 맨 아래 「태그」 줄 그대로
상태: 검수중
보고: 5_보고 「부동산_코너_보고.txt」 맨 아래에 한 줄 — {slug} · 실제 예약 날짜 시각 · 발행 뒤 글 주소.
"""
    p = jisi_path(slug); open(p, 'w', encoding='utf8').write(body)
    ok, o = gas('fput', DRV, p); plan_set(slug, when=when, title=t, jisi=os.path.basename(p))
    J({'ok': ok, 'jisi': os.path.basename(p), 'state': '검수중'})


def cmd_result(slug):
    d = folder(slug); name = f'nangman_{slug}.gpt.json'; out = os.path.join(d, 'gpt.json')
    # 「결과」에 없으면 「결과/반영완료」도 본다(다른 정기 작업이 먼저 옮겨 놓았을 때 놓치지 않게)
    where = None
    for sub in ('결과', '결과/반영완료'):
        if os.path.exists(out): os.remove(out)
        rc, o = sh('python3', GAS, 'fget', f'{REV}/{sub}', name, out)
        if not rc and os.path.exists(out) and os.path.getsize(out) >= 20: where = sub; break
    if not where:
        if os.path.exists(out): os.remove(out)
        J({'ok': False, 'why': '결과 아직 없음', 'submitted': next((x.get('submitted') for x in plan_load()['posts'] if x.get('slug') == slug), None)}); sys.exit(3)
    try: j = json.load(open(out, encoding='utf8'))
    except Exception: J({'ok': False, 'why': '결과 파일이 JSON 이 아님'}); sys.exit(2)
    J({'ok': True, 'checklist': j.get('checklist'), 'verdict': j.get('verdict'), 'fixes': len(j.get('fixes', [])), 'file': out, 'where': where})


def cmd_fix(slug):
    d = folder(slug); j = json.load(open(os.path.join(d, 'gpt.json'), encoding='utf8'))
    if j.get('checklist') != '자연스러움_1112': J({'ok': False, 'why': '다른 점검표 결과 — 쓰지 않음(다시 요청)'}); sys.exit(2)
    mp = os.path.join(d, 'mk.py'); s = open(mp, encoding='utf8').read()
    nums = lambda t: sorted(re.findall(r'\d[\d,.]*', t)); done, skip = 0, []
    for f in j.get('fixes', []):
        q, to = (f.get('quote') or '').strip(), (f.get('to') or '').strip()
        if not q: continue
        if s.count(q) != 1: skip.append({'quote': q, 'to': to, 'why': 'mk.py 에 없거나 여러 번 — 손으로'}); continue
        line = next(l for l in s.split('\n') if q in l).lstrip()
        if line.startswith(('o.append(H(', 'o.append(NOTE(', 'TITLE', 'o.append(related', 'o.append(tags', '(')): skip.append({'quote': q, 'why': '제목 · 소제목 · 근거 줄 — 그대로'}); continue
        if to and nums(q) != nums(to): skip.append({'quote': q, 'to': to, 'why': '숫자가 달라짐 — 그대로'}); continue
        if not to and nums(q): skip.append({'quote': q, 'why': '숫자가 든 문장은 지우지 않음'}); continue
        if any(w in to for w in BAN): skip.append({'quote': q, 'to': to, 'why': '금지어가 든 고침'}); continue
        s = s.replace(q + ' ', '') if (not to and q + ' ' in s) else s.replace(q, to); done += 1
    open(mp, 'w', encoding='utf8').write(s)
    J({'ok': True, 'verdict': j.get('verdict'), 'done': done, 'skip': skip})


def cmd_ready(slug, when=None):
    p = jisi_path(slug)
    if not os.path.exists(p):
        rc, o = sh('python3', GAS, 'fget', DRV, os.path.basename(p), p)
        if not os.path.exists(p): J({'ok': False, 'why': '지시 파일 없음 → block 먼저'}); sys.exit(1)
    s = open(p, encoding='utf8').read()
    if when: s = re.sub(r'^예약: .*$', '예약: ' + when, s, count=1, flags=re.M)
    if '상태: 대기' in s or '상태: 완료' in s: J({'ok': True, 'state': '이미 대기 · 완료 — 아무것도 안 함'}); return
    s = s.replace('상태: 검수중', '상태: 대기', 1); open(p, 'w', encoding='utf8').write(s)
    ok, o = gas('fput', DRV, p)
    w = re.search(r'^예약: (.*)$', s, re.M).group(1); t = re.search(r'^제목: (.*)$', s, re.M).group(1)
    g = os.path.join(WORK, f"교신_어사이드_클로드_{time.strftime('%Y%m%d-%H%M')}_부동산 코너 글 예약 {slug}.txt")
    open(g, 'w', encoding='utf8').write(f"""용건: 낭만 부동산 요일 코너 글 「{t}」 네이버 예약.
해야 할 일: 4_어사이드 「{os.path.basename(p)}」 블록이 「상태: 대기」가 됐다. 그 지시대로 dong_jin_kim 에 예약한다. 대표 사진은 01.jpg 를 직접 지정. 표와 「30초 요약」은 글자 그대로.
기한: 이 교신을 읽은 실행. 예약 시각 {w}.
쓸 재료·주소: {DRV}/원고/새코너/{slug}/ ({slug}.html · {slug}.txt · 01.jpg~)
끝났다는 증거: 5_보고 「부동산_코너_보고.txt」 맨 아래 한 줄({slug} · 예약 날짜 시각 · 발행 뒤 글 주소). 블록 「상태: 완료」.
막히면: 로그인 · 인증은 「사용자_확인필요」 한 줄 뒤 멈춤. 그 시각에 다른 예약 글이 있으면 그 글은 그대로 두고 이 글을 다음 날 같은 시각으로.
""")
    ok2, o = gas('fput', DRV, g); plan_set(slug, state='대기', ready=time.strftime('%Y-%m-%d %H:%M'), when=w)
    J({'ok': ok and ok2, 'state': '대기', 'when': w})


def cmd_reedit(slug):
    """이미 예약 · 발행 지시가 나간 글의 글자만 고쳤을 때: html · txt 만 다시 올리고 어사이드에게 본문 다시 채우기를 부탁한다(사진 · 예약 시각 그대로)."""
    d = folder(slug); t = title_of(d); cmd_up(slug, text=True, end=True)
    g = os.path.join(WORK, f"교신_어사이드_클로드_{time.strftime('%Y%m%d-%H%M')}_부동산 예약 글 본문 다시 채우기 {slug}.txt"); os.makedirs(WORK, exist_ok=True)
    open(g, 'w', encoding='utf8').write(f"""용건: 낭만 부동산 글 「{t}」 — ChatGPT 검수로 문장 몇 곳을 고쳤다. 예약(또는 발행)된 글의 본문을 새 html 로 다시 채운다.
해야 할 일: dong_jin_kim 예약 글 「{t}」를 「수정」으로 열어 {DRV}/원고/새코너/{slug}/{slug}.html 대로 본문 글자를 다시 채운다. 사진 · 대표 사진(01.jpg) · 제목 · 태그 · 예약 시각은 그대로 둔다. 아직 예약 전이면 새 html 로 예약한다.
기한: 그 글 예약 시각 4시간 전까지. 그 뒤라면 손대지 않는다(원래 글이 나간다).
쓸 재료·주소: {DRV}/원고/새코너/{slug}/ ({slug}.html · {slug}.txt 가 새 판 · 사진은 그대로)
끝났다는 증거: 5_보고 「부동산_코너_보고.txt」 맨 아래 한 줄({slug} · 본문 다시 채움 · 시각).
막히면: 예약 글을 못 찾으면 고치지 말고 보고에 「못 찾음」 한 줄. 로그인 · 인증은 「사용자_확인필요」.
""")
    ok, o = gas('fput', DRV, g); plan_set(slug, state='대기', ready=time.strftime('%Y-%m-%d %H:%M'))
    J({'ok': ok, 'state': '대기(본문 다시 채우기 부탁)'})


def cmd_clip(slug):
    """ChatGPT 가 클립 · 인스타 · 스레드를 만들 재료(확인된 숫자만)를 올리고 교신 한 통. 숫자는 원고의 「30초 요약」과 질문 소제목에서만 뽑는다."""
    d = folder(slug); t = open(f'{OUT}/nangman_{slug}.txt', encoding='utf8').read().split('\n'); p = plan_load(); nr = p.get('next_nr', 43)
    e = next((x for x in p['posts'] if x.get('slug') == slug), {})
    if e.get('clip'): J({'ok': True, 'clip': e['clip'], 'note': '이미 올림'}); return
    title = title_of(d); summ = [l[1:].strip() for l in t if l.startswith('·')][:3]; heads = [l.replace('[소제목]', '').strip() for l in t if l.startswith('[소제목]')]
    cond = next((l for l in t if l.startswith('기준일')), '')
    name = f'NR{nr:03d}_{slug}'; wd = os.path.join(WORK, name); os.makedirs(wd, exist_ok=True)
    body = (f"[클립 재료 · {name[:5]} · 낭만 부동산 분석 플랫폼 · {time.strftime('%Y-%m-%d')} Claude]\n제목: {title}\n"
            f"원문: 네이버 예약 {e.get('when', '')} 예정. 발행 주소는 5_보고 「부동산_코너_보고.txt」에 적힌다 — 주소가 나온 뒤에 클립을 올린다(연결할 글 = 그 주소).\n\n"
            "확인된 숫자와 뜻 (이 숫자만 쓴다)\n" + ''.join(f'- {x}\n' for x in summ) + f"조건: {cond}\n\n"
            "글이 답하는 질문(장면 순서로 써도 된다)\n" + ''.join(f'- {x}\n' for x in heads if x != '자주 묻는 질문') +
            "\n금지: 전화번호 글자 · 인테리어 링크 · 위에 없는 숫자 · 「오른다 · 내린다」 단정 · 특정 대출이나 단지를 고르라는 권유 · 「갈-」 표현\n"
            "그림: 같은 폴더 02.jpg~04.jpg (원고 본문 그림)\n")
    open(os.path.join(wd, '재료.txt'), 'w', encoding='utf8').write(body)
    ok = gas('fput', f'{DRV}/클립재료/{name}', os.path.join(wd, '재료.txt'))[0]
    for n in ('02', '03', '04'):
        f = f'{OUT}/nangman_{slug}/{n}.jpg'
        if os.path.exists(f): ok &= gas('fput', f'{DRV}/클립재료/{name}', f)[0]
    g = os.path.join(WORK, f"교신_챗지피티_클로드_{time.strftime('%Y%m%d-%H%M')}_부동산 클립 재료 {name}.txt")
    open(g, 'w', encoding='utf8').write(f"""용건: 부동산 새 글 「{title}」 클립 1편 기획 · 제작({name[:5]}) + 같은 재료로 real.estate.nangman 인스타 · 스레드 1편씩.
해야 할 일: 클립재료/{name}/재료.txt 와 그림으로 세로 클립 1편 + cover.jpg + caption.txt 를 같은 폴더에(클립_기획기준_1112 그대로). 숫자는 재료에 있는 것만.
기한: 글 예약 시각({e.get('when', '')}) 전날 18:00.
쓸 재료·주소: {DRV}/클립재료/{name}/
끝났다는 증거: 같은 폴더의 clip.mp4 · cover.jpg · caption.txt.
막히면: 숫자가 더 필요하면 교신으로 요청한다(없는 숫자는 쓰지 않는다).
""")
    ok &= gas('fput', DRV, g)[0]; p = plan_load(); p['next_nr'] = nr + 1; plan_save(p); plan_set(slug, clip=name)
    J({'ok': bool(ok), 'clip': name})


def cmd_status():
    for e in sorted(plan_load()['posts'], key=lambda x: (x.get('date', ''), x.get('time', ''))):
        print(f"{e.get('date', '')} {e.get('time', '')} | {e.get('corner', ''):<8} | {e.get('state', 'todo'):<4} | {e.get('slug', '-'):<18} | {e.get('title') or e.get('topic', '')}")


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    c, r = a[0], a[1:]
    opt = lambda k: (r[r.index(k) + 1] if k in r and r.index(k) + 1 < len(r) else None)
    if c == 'new': cmd_new(r[0])
    elif c == 'thumb': cmd_thumb(*r[:6])
    elif c == 'build': cmd_build(r[0], '--fig' in r)
    elif c == 'up': cmd_up(r[0], '--text' in r, '--end' in r)
    elif c == 'submit': cmd_submit(r[0])
    elif c == 'block': cmd_block(r[0], opt('--when') or '', opt('--cat') or '부동산 분석')
    elif c == 'result': cmd_result(r[0])
    elif c == 'fix': cmd_fix(r[0])
    elif c == 'ready': cmd_ready(r[0], opt('--when'))
    elif c == 'reedit': cmd_reedit(r[0])
    elif c == 'clip': cmd_clip(r[0])
    elif c == 'status': cmd_status()
    else: print(__doc__)
