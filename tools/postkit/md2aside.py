#!/usr/bin/env python3
"""낭만 인테리어 원고 md → 어사이드 작업 폴더 (도우미 없이 · 사진은 어사이드가 네이버에 직접 올림 · 11/5 사용자)
사용: python3 md2aside.py <원고.md> [--up]
  원고 머리말에 thumb: 꼬리표 | 이름1 | 이름2 | 앞말 | 핵심 | 설명  (썸네일 = 01.jpg 대표)
결과: /home/claude/w/aside_pkg/<이름>/
  01.jpg 썸네일(대표) · 02.jpg~ 본문 사진과 표 그림을 나오는 순서대로 · <이름>.html(모양 그대로 · 「▼ 사진 NN.jpg」 표시)
--up : 드라이브 「블로그/협업/4_어사이드/원고/<이름>/」에 폴더째 올림(같은 이름은 바꿔 끼움)"""
import sys, os, re, shutil, subprocess, base64, html as H, json
md = sys.argv[1]; name = os.path.splitext(os.path.basename(md))[0]
OUT = f'/home/claude/w/aside_pkg/{name}'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
raw = open(md, encoding='utf8').read(); head, body = raw.split('\n---\n', 1); m = {}
for ln in head.splitlines():
    if ln.startswith('# '): m['title'] = ln[2:].strip()
    elif ':' in ln: k, v = ln.split(':', 1); m[k.strip()] = v.strip()
T = m['title']; n = [1]; parts = []
def b64(p, mime='image/jpeg'): return f'data:{mime};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def mark(k, note=''): return f'<p style="font-size:15px;color:#c00;font-weight:700;margin:18px 0 4px">▼ 사진 {k:02d}.jpg{note}</p>'
# 01 썸네일
t = [a.strip() for a in m.get('thumb', '').split('|')]
th = f'{OUT}/01.jpg'
cmd = ['python3', '/home/claude/tools/ipju_thumb.py', '--tag', t[0], '--name', t[1] + '|' + t[2], '--lead', t[3], '--key', t[4], '--out', th]
if len(t) > 5 and t[5]: cmd += ['--sub', t[5]]
subprocess.run(cmd, check=True, capture_output=True)
parts.append(f'<p style="font-size:15px;color:#c00;font-weight:700">제목 칸: {H.escape(T)}</p>' + mark(1, ' (대표 · 썸네일)') + f'<img src="{b64(th)}" width="420"><hr>')
def inline(x):
    x = H.escape(x); return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', x)
BAN = ('<div style="width:872px;background:#eaf2fb;border-left:10px solid #1f5fa8;padding:30px 34px 34px;font-family:\'Noto Sans CJK KR\',sans-serif">'
       '<div style="font-size:40px;font-weight:900;color:#123d6b;line-height:1.35">{}</div>'
       '<div style="font-size:27px;color:#2b3a4a;margin-top:16px;line-height:1.5">사는 동네와 함께 문자로 보내 주세요. 가까운 시공팀을 이어 드립니다.</div>'
       '<div style="display:inline-block;margin-top:24px;background:#1f6fd1;color:#fff;font-size:30px;font-weight:800;padding:16px 38px;border-radius:999px">문자 · 전화 010-2882-8165</div></div>')
def banner(fname, text):
    hp = f'{OUT}/_b.html'
    open(hp, 'w', encoding='utf8').write(f'<html><head><meta charset="utf-8"></head><body style="margin:0;padding:0;background:#fff;width:920px">{BAN.format(H.escape(text))}</body></html>')
    subprocess.run(['wkhtmltoimage', '-q', '--width', '920', '--enable-local-file-access', hp, f'{OUT}/{fname}'], check=True); os.remove(hp)
    return (f'<p style="font-size:15px;color:#c00;font-weight:700;margin:18px 0 4px">▼ 배너 {fname}</p>'
            f'<img src="{b64(f"{OUT}/{fname}", "image/png")}" style="max-width:100%">')
GAP = '<p><br></p>'
ncall = [0]
TS = 'width:100%;border-collapse:collapse;font-size:23px;'
def table_img(rows):
    n[0] += 1; k = n[0]
    h = f'<table style="{TS}font-family:\'Noto Sans CJK KR\',sans-serif">'
    for i, r in enumerate(rows):
        tg = 'th' if i == 0 else 'td'; st = 'background:#1d3d5c;color:#fff;' if i == 0 else ('background:#f6f8fb;' if i % 2 == 0 else '')
        h += '<tr>' + ''.join(f'<{tg} style="{st}padding:12px 10px;border:1px solid #c9d4df;text-align:left;line-height:1.5">{inline(c)}</{tg}>' for c in r) + '</tr>'
    h += '</table>'
    page = f'<html><head><meta charset="utf-8"></head><body style="margin:0;padding:16px;background:#fff;width:808px">{h}</body></html>'
    hp = f'{OUT}/_t{k}.html'; open(hp, 'w', encoding='utf8').write(page)
    png = f'{OUT}/_t{k}.png'
    subprocess.run(['wkhtmltoimage', '-q', '--width', '840', '--enable-local-file-access', hp, png], check=True)
    from PIL import Image
    Image.open(png).convert('RGB').save(f'{OUT}/{k:02d}.jpg', quality=92); os.remove(png); os.remove(hp)
    # 표 그림 + 같은 내용 표(글자로도 남김 · 어사이드가 그림을 넣고 아래 표는 지우거나 둘 다 둠)
    return mark(k, ' (표 그림)') + f'<img src="{b64(f"{OUT}/{k:02d}.jpg")}" style="max-width:100%">'
# 11/12 배너 빠짐 방지: [CALL] 줄이 없으면 자동으로 넣는다(중간 = 둘째 소제목 위 · 끝 = 같이 보면 좋은 글 위)
if not re.search(r'^\[CALL\] ', body, re.M):
    hs = [mm.start() for mm in re.finditer(r'^## (?!같이 보면)', body, re.M)]
    at = hs[1] if len(hs) > 1 else (hs[0] if hs else len(body))
    body = body[:at] + '[CALL] ' + (m.get('call') or '사진 한 장 보내 주시면 어디부터 볼지 알려 드려요') + '\n\n' + body[at:]
if not re.search(r'^\[CALL\]\s*$', body, re.M):
    mm = re.search(r'^## 같이 보면', body, re.M)
    at = mm.start() if mm else len(body)
    body = body[:at] + '\n[CALL]\n\n' + body[at:]
tbl = []
def flush():
    if tbl: parts.append(table_img(tbl)); tbl.clear()
for blk in re.split(r'\n\s*\n', body.strip()):
    for ln in blk.splitlines():
        ln = ln.strip()
        if ln.startswith('|'):
            cs = [c.strip() for c in ln.strip('|').split('|')]
            if not all(re.fullmatch(r':?-{2,}:?', c) for c in cs): tbl.append(cs)
            continue
        flush()
        if ln.startswith('## '): parts.append(f'<h2 style="font-size:22px;color:#1d3d5c;margin:30px 0 10px">{inline(ln[3:])}</h2>')
        elif ln.startswith('!='):
            n[0] += 1; shutil.copy(ln[2:].strip(), f'{OUT}/{n[0]:02d}.jpg')
            parts.append(mark(n[0]) + f'<img src="{b64(f"{OUT}/{n[0]:02d}.jpg")}" style="max-width:100%">')
        elif ln == '[CALL]': parts.append(banner('banner_end.png', '사진 한 장이면 됩니다'))
        elif ln.startswith('[CALL] '):
            ncall[0] += 1; parts.append(banner('banner_mid.png' if ncall[0] == 1 else f'banner_mid{ncall[0]}.png', ln[7:].strip()))
        elif ln.startswith('- '):
            mm = re.match(r'(.+?) · (https?://\S+)$', ln[2:])
            parts.append(f'<p>· <a href="{mm.group(2)}">{H.escape(mm.group(1))}</a></p>' if mm else f'<p>· {inline(ln[2:])}</p>')
        elif ln: parts.append(f'<p>{inline(ln)}</p>')
    flush()
    if parts and parts[-1].startswith('<p') and '▼' not in parts[-1][:80]: parts.append(GAP)
tags = [x.strip() for x in m.get('tags', '').split(',') if x.strip()]
parts.append('<p style="color:#2f5d8a">' + ' '.join('#' + x.replace(' ', '') for x in tags) + '</p>')
doc = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{H.escape(T)}</title></head>'
       f'<body style="max-width:760px;margin:20px auto;padding:0 16px;font-size:18px;line-height:1.85;color:#222;font-family:sans-serif">' + '\n'.join(parts) + '</body></html>')
open(f'{OUT}/{name}.html', 'w', encoding='utf8').write(doc)
res = {'name': name, 'photos': n[0], 'dir': OUT}
if '--up' in sys.argv:
    sys.path.insert(0, '/home/claude/helper'); from gas import call
    for f in sorted(os.listdir(OUT)):
        p = f'{OUT}/{f}'; mime = 'text/html' if f.endswith('.html') else ('image/png' if f.endswith('.png') else 'image/jpeg')
        call('fput', path=f'블로그/협업/4_어사이드/원고/{name}', name=f, b64=base64.b64encode(open(p, 'rb').read()).decode(), mime=mime)
    res['uploaded'] = len(os.listdir(OUT))
print(json.dumps(res, ensure_ascii=False))
