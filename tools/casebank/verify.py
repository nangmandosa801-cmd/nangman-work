#!/usr/bin/env python3
"""드라이브 사례 폴더에 파일이 다 있는지 확인하고 빠진 것만 다시 올림(11/13 · 병렬로 올릴 때 같은 폴더가 동시에 두 번 만들어져 일부 파일이 다른 폴더로 간 문제 보완)."""
import os, glob, json, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bank import OUT, ok_case
G = '/home/claude/helper/gas.py'; R = '블로그/협업/시공사례_은행'
def ls(p):
    r = subprocess.run(['timeout', '60', 'python3', G, 'ls', p], capture_output=True, text=True)
    try: return {f['name'] for f in json.loads(r.stdout)}
    except Exception: return set()
def fix(d):
    rel = os.path.relpath(d, OUT); out = []
    for sub in ['', '보정본']:
        loc = os.path.join(d, sub)
        if not os.path.isdir(loc): continue
        want = {f for f in os.listdir(loc) if os.path.isfile(os.path.join(loc, f))}
        have = ls(f'{R}/{rel}' + (f'/{sub}' if sub else ''))
        for f in sorted(want - have):   # 한 폴더 안은 순서대로(폴더 중복 생성 방지)
            r = subprocess.run(['timeout', '150', 'python3', G, 'fput', f'{R}/{rel}' + (f'/{sub}' if sub else ''), os.path.join(loc, f)], capture_output=True, text=True)
            out.append((f, r.returncode == 0))
    return rel, out
ds = [d for d in sorted(glob.glob(f'{OUT}/*/*/')) if ok_case(d.rstrip('/'))]
with ThreadPoolExecutor(6) as ex:   # 사례끼리는 병렬(서로 다른 폴더라 안전)
    res = list(ex.map(fix, [d.rstrip('/') for d in ds]))
miss = sum(len(o) for _, o in res); bad = sum(1 for _, o in res for f, k in o if not k)
print(json.dumps({'cases': len(res), 'reuploaded': miss, 'failed': bad}, ensure_ascii=False))
