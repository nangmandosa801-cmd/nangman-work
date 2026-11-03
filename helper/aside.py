#!/usr/bin/env python3
"""도우미 html에 Aside용 id를 붙인다: when(예약 줄) · t0(제목) · h0(본문 html, 창고 주소 그대로).
사용: python3 aside.py <작업폴더> "2026-11-04 08:00 | 카테고리"
"""
import sys,os,glob,re
d=os.path.abspath(sys.argv[1]); when=sys.argv[2]
f=glob.glob(os.path.join(d,'*_helper.html'))[0]
t=open(f).read()
title=open(os.path.join(d,'post.txt')).read().split('\n')[1].strip()
body=open(os.path.join(d,'post.html')).read()
t=re.sub(r'<div class="when"[^>]*>.*?</div>',f'<div class="when" id="when">{when}</div>',t,count=1,flags=re.S)
t=re.sub(r'<div id="t0"[^>]*>.*?</div>\n?','',t,flags=re.S)
t=re.sub(r'<div id="h0"[^>]*>.*?<!--/h0--></div>\n?','',t,flags=re.S)
blk=(f'<div class="step"><div class="meta">제목</div><div id="t0" style="font-size:20px;font-weight:700">{title}</div></div>\n'
     f'<div id="h0" hidden>{body}<!--/h0--></div>\n')
i=t.find('<div class="step"><div class="meta">예약 시각')
t=t[:i]+blk+t[i:]
open(f,'w').write(t)
print(f, title, when, 'imgs', body.count('<img'))
