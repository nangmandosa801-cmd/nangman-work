#!/usr/bin/env python3
"""티스토리 발행 꾸러미 (11/10): python3 tspub.py <slug> <title> <html파일> <tags> <category_id> <img_url>... [--id 글번호] [--at "2026-11-11 09:00"](KST 예약)
html 안 그림 자리는 {{IMG:0}} {{IMG:1}} … (0 = 대표). 꾸러미를 nangman-work/ts_pkg/<slug>.json 에 쓰고 sync 뒤
크롬에서 실행할 한 줄 JS 를 출력한다. 카테고리: 1373246 부동산 시세 · 1373248 지식산업센터 · 토지."""
import sys, json, subprocess
a = sys.argv[1:]; pid = None; at = None
if '--id' in a: i = a.index('--id'); pid = a[i+1]; del a[i:i+2]
if '--at' in a:
    i = a.index('--at'); import datetime as D; at = int(D.datetime.strptime(a[i+1], '%Y-%m-%d %H:%M').replace(tzinfo=D.timezone(D.timedelta(hours=9))).timestamp()); del a[i:i+2]
slug, title, hf, tags, cat, *imgs = a
P = {'slug': slug, 'title': title, 'html': open(hf, encoding='utf-8').read(), 'tags': tags, 'category': int(cat), 'imgs': imgs, 'thumb': 0}
if pid: P['id'] = pid
if at: P['at'] = at  # 예약 발행(초) · 없으면 바로 공개
json.dump(P, open(f'/home/claude/nangman-work/ts_pkg/{slug}.json', 'w', encoding='utf-8'), ensure_ascii=False)
subprocess.run(['bash', '/home/claude/nangman-work/sync.sh'], capture_output=True)
sha = subprocess.run(['git', '-C', '/home/claude/nangman-work', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
raw = f'https://raw.githubusercontent.com/nangmandosa801-cmd/nangman-work/{sha}/ts_pkg/'
print(f"const R='{raw}';(new Function('return '+await (await fetch(R+'pub.js')).text()))()(R+'{slug}.json')")
