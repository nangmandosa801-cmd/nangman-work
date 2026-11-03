#!/usr/bin/env python3
"""새 글 있나만 빠르게 본다. 사용: python3 rss_new.py <블로그id,...> [시간=30] [handled.json]
환경변수 GREP="문구1|문구2" 를 주면 본문에 그 문구가 있는 글만 남긴다. 출력: JSON 한 줄."""
import sys, json, re, os, urllib.request, email.utils, datetime as dt
ids = sys.argv[1].split(','); hrs = float(sys.argv[2]) if len(sys.argv) > 2 else 30
handled = set()
if len(sys.argv) > 3:
    try: handled = set(map(str, json.load(open(sys.argv[3])).get('handled', [])))
    except Exception: pass
now = dt.datetime.now(dt.timezone.utc); out = []; err = []
for b in ids:
    try:
        x = urllib.request.urlopen(urllib.request.Request(f'https://rss.blog.naver.com/{b}.xml', headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read().decode('utf-8', 'ignore')
    except Exception as e:
        err.append(f'{b}:{e.__class__.__name__}'); continue
    for it in re.findall(r'<item>(.*?)</item>', x, re.S):
        g = lambda t: (re.search(rf'<{t}>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{t}>', it, re.S) or [None, ''])[1].strip()
        d = email.utils.parsedate_to_datetime(g('pubDate'))
        m = re.search(r'/(\d{9,})', g('link')); no = m.group(1) if m else g('link')
        if (now - d).total_seconds() <= hrs * 3600 and no not in handled and f'{b}/{no}' not in handled:
            out.append({'blog': b, 'no': no, 'title': g('title')[:40], 'date': d.isoformat()})
kw = [k for k in os.environ.get('GREP', '').split('|') if k]
if kw:
    keep = []
    for o in out:
        try:
            h = urllib.request.urlopen(urllib.request.Request(f"https://m.blog.naver.com/{o['blog']}/{o['no']}", headers={'User-Agent': 'Mozilla/5.0 (iPhone)'}), timeout=20).read().decode('utf-8', 'ignore')
            o['hit'] = [k for k in kw if k in h]
        except Exception as e:
            o['hit'] = []; err.append(f"{o['no']}:{e.__class__.__name__}")
        if o['hit']: keep.append(o)
    out = keep
print(json.dumps({'new': out, 'err': err}, ensure_ascii=False))
