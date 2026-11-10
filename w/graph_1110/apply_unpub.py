#!/usr/bin/env python3
"""발행 전 원고에 v2 그림 반영: gas image → urls.json → mk.py IMG 이름 _v2 → mk.py 다시 → html2aside(txt·사진) + html2aside_html --up
  python3 apply_unpub.py <folder> <nangman_name> [--noup]"""
import sys, os, re, json, glob, subprocess, shutil
sys.path.insert(0, '/home/claude/helper'); import gas
H = '/home/claude/helper/'
folder, name = sys.argv[1], sys.argv[2]; up = '--noup' not in sys.argv
d = H + folder; os.chdir(d)
slug = name.replace('nangman_', '')
U = json.load(open('urls.json')); log = {'folder': folder, 'new': []}
mk = open('mk.py').read()
for f in sorted(glob.glob('img/*_v2.png')):
    base = os.path.basename(f); old = base.replace('_v2.png', '.png')
    k = base.replace(f'nangman_{slug}_', '').replace('.png', '')
    if k not in U or os.path.getmtime(f) > os.path.getmtime('urls.json'):
        r = gas.image(os.path.abspath(f)); U[k] = r if isinstance(r, str) else (r.get('url') or r.get('src') or list(r.values())[0])
        log['new'].append(k)
    mk = mk.replace(f"IMG('{old}'", f"IMG('{base}'")
json.dump(U, open('urls.json', 'w'), ensure_ascii=False, indent=1)
open('mk.py', 'w').write(mk)
if not os.path.samefile('tails.py', H + 'pg/tails.py') and open('tails.py').read() != open(H + 'pg/tails.py').read(): shutil.copy(H + 'pg/tails.py', 'tails.py')
r = subprocess.run([sys.executable, 'mk.py'], capture_output=True, text=True); log['mk'] = (r.stdout.strip()[-20:] or r.stderr.strip()[-200:])
p = open('post.html').read()
log['v2_in_post'] = sum(1 for k in U if k.endswith('_v2') and U[k] in p); log['interior'] = len(re.findall('champion_chart|낭만 인테리어', p))
log['placeholder'] = p.count('[그림]')
if up and r.returncode == 0:
    for tool in ('html2aside.py', 'html2aside_html.py'):
        q = subprocess.run([sys.executable, '/home/claude/tools/postkit/' + tool, d, name, '--up'], capture_output=True, text=True)
        log[tool] = 'ok' if q.returncode == 0 else (q.stderr.strip()[-300:] or q.stdout.strip()[-300:])
print(json.dumps(log, ensure_ascii=False))
