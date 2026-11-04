#!/usr/bin/env python3
"""구글 드라이브 커넥터로 읽은 우체통_conf.json 글자를 받아 /home/claude/gas/conf.json 으로 저장(11/5).
커넥터는 밑줄 앞에 \\ 를 붙여 돌려주므로 지운다. 사용: python3 conf_fix.py '<읽은 글자>'   (출력: ok · url 앞부분만)"""
import sys, json, os
t = sys.argv[1].replace('\\_', '_').strip()
j = json.loads(t); assert j.get('url') and j.get('key')
os.makedirs('/home/claude/gas', exist_ok=True); json.dump(j, open('/home/claude/gas/conf.json', 'w'))
print('ok', j['url'][:45])
