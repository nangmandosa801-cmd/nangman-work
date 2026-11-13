#!/usr/bin/env python3
"""다시 만든 원고 꾸러미를 드라이브에 올린다: 원고/새코너/salary_map/(html · txt · 01~06.jpg). --end 를 주면 검수 끝 폴더에도 txt."""
import subprocess, glob, os, shutil, sys, json
B = '블로그/협업/4_어사이드/원고/새코너'; A = '/home/claude/w/aside_out'; d = 'salary_map'
S = f'/tmp/stg/{d}'; shutil.rmtree(S, ignore_errors=True); os.makedirs(S)
shutil.copy(f'{A}/nangman_{d}.html', f'{S}/{d}.html'); shutil.copy(f'{A}/nangman_{d}.txt', f'{S}/{d}.txt')
fs = [f'{S}/{d}.html', f'{S}/{d}.txt'] + ([] if '--text' in sys.argv else sorted(glob.glob(f'{A}/nangman_{d}/*.jpg'))); ok = 0
for f in fs:
    r = subprocess.run(['python3', '/home/claude/helper/gas.py', 'fput', f'{B}/{d}', f], capture_output=True, text=True)
    ok += r.returncode == 0 and '"id"' in r.stdout
if '--end' in sys.argv:
    r = subprocess.run(['python3', '/home/claude/helper/gas.py', 'fput', '블로그/협업/검수_자연스러움/끝', f'{A}/nangman_{d}.txt'], capture_output=True, text=True); ok += '"id"' in r.stdout; fs.append('끝')
print(json.dumps({'files': len(fs), 'ok': int(ok)}, ensure_ascii=False))
