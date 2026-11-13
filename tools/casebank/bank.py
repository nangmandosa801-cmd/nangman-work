#!/usr/bin/env python3
"""시공 사례 은행 — 제휴팀 블로그 글을 사례 폴더(사진 + 사례.txt)로 쌓는다. ChatGPT · 어사이드가 꺼내 쓰는 곳.
사용: python3 bank.py [--per 5] [--blog door-diy777 ...] [--up]
결과: /home/claude/w/casebank/<분야>/<사례ID>/{사진 NN.jpg, sheet.jpg, 사례.txt} + 목록.json · 목록.txt
--up 이면 드라이브 「블로그/협업/시공사례_은행/」로 올림(이미 올린 사례는 건너뜀 · bank_state.json).
원칙: 사진 사용 조건(pool.json photo_rule)을 사례.txt 맨 위에 적고, 「가공해서만 · 쓰던 대로(가공)」는 가공본만 둔다.
이야기 뼈대는 원문 문장에서 자동으로 뽑은 것(확인 필요). 원문에 없는 말 · 숫자는 쓰지 않는다.
"""
import json, os, re, html, sys, subprocess, argparse, glob
from PIL import Image, ImageDraw, ImageEnhance
POOL = '/home/claude/w/partners/pool.json'; OUT = '/home/claude/w/casebank'
FIELD = {'door-diy777': '중문_설치', 'flowhc': '중문_무타공·설비', 'doors9774': '중문_수리', 'febric_cleaning': '결로·단열·곰팡이',
         'specialcoking': '코킹·창틀누수', 'lmg4455': '줄눈', 'amrita2580': '입주청소·줄눈·탄성', 'dd2homecare': '사전점검'}
KW = {'불편': r'고민|불편|문의|소음|삐걱|고장|곰팡|누수|들뜨|냄새|춥|외풍|결로|새는|깨진|파손|오래',
      '단서': r'원인|확인해|보니|발견|측정|열화상|점검|살펴|알고 보니|상태',
      '방법': r'교체|철거|제거|충진|설치|도포|시공합|작업합|진행했|바꿔|실측|부착',
      '결과': r'완료|마무리|깔끔|해결|사라|부드럽|새것|만족|확인했'}
def clean(t):
    t = html.unescape(t.replace('se-main-container">', '')); t = re.sub(r'[\u200b\s]+', ' ', t)
    t = re.split(r'태그 취소|공감 0|Previous image', t)[0] if '태그 취소' in t or '공감 0' in t else t
    t = re.sub(r'0\d{1,2}[ .\-]?\d{3,4}[ .\-]?\d{4}', '[번호 지움]', t)
    t = re.sub(r'#\S+', '', t); t = re.sub(r'https?://\S+|www\.\S+', '', t)
    return t.replace('Previous image', '').replace('Next image', '').strip()
def sents(t): return [s.strip() for s in re.split(r'(?<=[.!?요다])\s+', t) if 12 <= len(s.strip()) <= 160]
def skeleton(t):
    ss = sents(t); out = {}
    for k, pat in KW.items():
        hit = [s for s in ss if re.search(pat, s) and not re.search(r'문의|톡톡|상담|전문 ?업체|자격', s) or (k == '불편' and re.search(pat, s) and '문의로 시작' in s)]
        out[k] = hit[:3]
    return out
def proc(src, dst, rule):
    im = Image.open(src).convert('RGB')
    if '가공' in rule:
        w, h = im.size; c = int(min(w, h) * 0.04); im = im.crop((c, c, w - c, h - c))
        im = ImageEnhance.Brightness(im).enhance(1.04); im = ImageEnhance.Contrast(im).enhance(1.03)
    im.save(dst, quality=92)
def sheet(files, out):
    c = 6; S = 220; r = (len(files) + c - 1) // c; sh = Image.new('RGB', (c * S, r * S), 'white'); d = ImageDraw.Draw(sh)
    for n, f in enumerate(files):
        im = Image.open(f).convert('RGB'); im.thumbnail((S - 6, S - 20)); sh.paste(im, ((n % c) * S, (n // c) * S + 16))
        d.text(((n % c) * S + 3, (n // c) * S + 2), os.path.basename(f), fill='red')
    sh.save(out, quality=85)
def slug(t): return re.sub(r'[^\w가-힣]+', '_', html.unescape(t))[:28].strip('_')
def build(i):
    fld = FIELD.get(i['blog'], i['kind']); cid = f"{i['logNo']}_{slug(i['title'])}"; d = f'{OUT}/{fld}/{cid}'
    if os.path.exists(f'{d}/사례.txt'): return fld, cid, None
    os.makedirs(d + '/_raw', exist_ok=True); keep = []
    for j, u in enumerate(i['imgs'], 1):
        if not re.search(r'\.(jpe?g)$', u.split('?')[0], re.I): continue   # PNG = 배너 · 홍보 카드가 대부분 → 뺌
        raw = f'{d}/_raw/{j:02d}.jpg'
        subprocess.run(['curl', '-s', '-e', 'https://blog.naver.com/', '-o', raw, u.split('?')[0] + '?type=w966'])
        try:
            w, h = Image.open(raw).size
            if min(w, h) < 400: continue
        except Exception: continue
        dst = f'{d}/{len(keep) + 1:02d}.jpg'; proc(raw, dst, i['photo_rule']); keep.append(dst)
    subprocess.run(['rm', '-rf', d + '/_raw'])
    if len(keep) < 3: subprocess.run(['rm', '-rf', d]); return fld, cid, 'too_few'
    sheet(keep, f'{d}/sheet.jpg')
    t = clean(i['text']); sk = skeleton(t); rule = i['photo_rule']
    use = ('가공본만 들어 있음 · 원본 요청 금지 · 업체명 · 연락처 본문 노출 금지' if '가공' in rule else
           '사진 안에 작게 업체 이름 표기하고 사용' if '이름 표기' in rule else '사용 허락 받음 · 업체명 · 연락처 본문 노출 금지')
    card = [f"[시공 사례 카드] {fld} · {cid}", f"출처: https://blog.naver.com/{i['blog']}/{i['logNo']} ({i['date']}) · 제휴 {i['abbr']}",
            f"원제목: {html.unescape(i['title'])}", f"사진 조건: {rule} → {use}",
            f"사진: {len(keep)}장 (01~{len(keep):02d}, 원글 순서 · 홍보 그림 · 작은 그림 뺌) · 한눈에 보기 sheet.jpg",
            "전후 짝: 미정 — 쓰기 전에 sheet.jpg 로 같은 부위 · 같은 방향인지 확인. 확정되면 이 줄을 「전 NN ↔ 후 NN」으로 고친다.", '',
            '[이야기 뼈대 · 원문에서 자동으로 뽑음 · 확인 필요]']
    for k, v in sk.items(): card.append(f'- {k}: ' + (' / '.join(v) if v else '미확인'))
    card += ['', '[고객 말 · 비용 · 기간 · 재발 여부] 원문에 없으면 미확인. 지어 내지 않는다. 업체 문장 그대로 베끼지 않는다.', '', '[원문 정리본 · 번호 · 해시태그 지움]', t[:4000]]
    open(f'{d}/사례.txt', 'w', encoding='utf8').write('\n'.join(card))
    return fld, cid, len(keep)
def index():
    rows = []
    for f in sorted(glob.glob(f'{OUT}/*/*/사례.txt')):
        L = open(f, encoding='utf8').read().split('\n'); fld, cid = f.split('/')[-3:-1]
        rows.append({'분야': fld, '사례': cid, '출처': L[1].split(' ')[1], '조건': L[3][7:], '사진': L[4].split('장')[0][4:],
                     '전후짝': L[5].split(': ',1)[1][:24], '사용': (lambda u: (u.get(f.split('/')[-2].split('_')[0],{}).get('상태','') + ' ' + u.get(f.split('/')[-2].split('_')[0],{}).get('글','')).strip() or '안 씀')(json.load(open(f'{OUT}/used.json')) if os.path.exists(f'{OUT}/used.json') else {}), '이야기': '정리됨' if os.path.exists(f.replace('사례.txt', '이야기.txt')) else '뼈대만'})
    json.dump(rows, open(f'{OUT}/목록.json', 'w'), ensure_ascii=False, indent=1)
    txt = ['시공 사례 은행 목록 — 분야 · 사례 폴더 · 사진 수 · 전후 짝 · 이야기(정리됨 = Claude가 원문 대조해 쓴 이야기.txt 있음)', '']
    for r in rows: txt.append(f"{r['분야']} | {r['사례']} | 사진 {r['사진']} | {r['전후짝']} | {r['이야기']} | 사용: {r['사용']} | {r['출처']}")
    open(f'{OUT}/목록.txt', 'w', encoding='utf8').write('\n'.join(txt)); return len(rows)
def upload():
    st_p = f'{OUT}/bank_state.json'; st = json.load(open(st_p)) if os.path.exists(st_p) else {}
    jobs = []
    for f in sorted(glob.glob(f'{OUT}/*/*/*')):
        rel = os.path.relpath(f, OUT); key = rel + ':' + str(int(os.path.getmtime(f)))
        if st.get(rel) == key: continue
        jobs.append((os.path.dirname(rel), f, rel, key))
    with open('/tmp/bank_jobs.txt', 'w') as fp:
        for dr, f, rel, key in jobs: fp.write(f'블로그/협업/시공사례_은행/{dr}\t{f}\n')
    subprocess.run("cat /tmp/bank_jobs.txt | xargs -P 8 -d '\\n' -I{} bash -c 'IFS=$\"\\t\" read d f <<< \"{}\"; timeout 120 python3 /home/claude/helper/gas.py fput \"$d\" \"$f\" >/dev/null'", shell=True)
    for dr, f, rel, key in jobs: st[rel] = key
    for f in ['목록.json', '목록.txt', '쓰는법.txt', '배정표.txt']:
        if os.path.exists(f'{OUT}/{f}'): subprocess.run(['timeout', '100', 'python3', '/home/claude/helper/gas.py', 'fput', '블로그/협업/시공사례_은행', f'{OUT}/{f}'], capture_output=True)
    json.dump(st, open(st_p, 'w'), ensure_ascii=False); return len(jobs)
if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('--per', type=int, default=5); a.add_argument('--blog', nargs='*'); a.add_argument('--up', action='store_true'); a.add_argument('--ids', nargs='*')
    v = a.parse_args(); p = json.load(open(POOL)); items = list(p.values()); res = []
    if v.ids: pick = [i for i in items if i['logNo'] in v.ids]
    else:
        pick = []
        for b in (v.blog or FIELD):
            mine = sorted([i for i in items if i['blog'] == b], key=lambda i: i['logNo'], reverse=True)
            n = 0
            for i in mine:
                if n >= v.per: break
                fld, cid, r = build(i)
                if r != 'too_few': n += 1; res.append((cid, r))
    for i in pick: res.append(build(i)[1:])
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import guard; guard.check(); guard.queue(7)
    n = index(); up = upload() if v.up else 0
    print(json.dumps({'built': [r for r in res if r[1] not in (None,)], 'cases': n, 'uploaded_files': up}, ensure_ascii=False)[:1500])
