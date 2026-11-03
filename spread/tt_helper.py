#!/usr/bin/env python3
"""티스토리 원고 json(title, body, tags) → Aside용 도우미 html (id: when, t0, h0, tags).
사용: python3 tt_helper.py out/tt_<logNo>.json "블로그 주소 | 카테고리" 출력.html"""
import sys,json,html
d=json.load(open(sys.argv[1])); when=sys.argv[2]; out=sys.argv[3]
t=d['title']; b=d['body']; tg=d.get('tags','')
page=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t[:30])} 티스토리 도우미</title>
<style>:root{{--bg:#f4f6f9;--fg:#1b2433;--line:#d5dce6;--card:#fff;--ac:#1F3864}}@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#11151c;--fg:#e4e9f0;--line:#2a3340;--card:#181e27;--ac:#8fb2e6;color-scheme:dark}}}}:root[data-theme="dark"]{{--bg:#11151c;--fg:#e4e9f0;--line:#2a3340;--card:#181e27;--ac:#8fb2e6;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 system-ui,"Noto Sans KR",sans-serif;padding:24px 16px}}.w{{max-width:760px;margin:0 auto;display:grid;gap:14px}}.c{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;overflow-wrap:anywhere}}#when{{font-size:22px;font-weight:700;color:var(--ac)}}#t0{{font-size:20px;font-weight:700}}#h0{{background:#fff;color:#222;max-height:480px;overflow:auto}}</style></head><body><div class="w">
<div class="c"><div>예약 · 블로그 · 카테고리</div><div id="when">{html.escape(when)}</div></div>
<div class="c"><div>제목</div><div id="t0">{html.escape(t)}</div></div>
<div class="c"><div>태그 (쉼표)</div><div id="tags">{html.escape(tg)}</div></div>
<div class="c"><div>본문 (HTML 그대로 · 그림 없음)</div><div id="h0">{b}</div></div>
</div></body></html>'''
open(out,'w').write(page); print(out,len(b))
