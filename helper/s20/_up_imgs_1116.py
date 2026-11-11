# 11/12 새 코너 3편 그림 → 낭만 창고(gas.py image) → urls.json
import subprocess, json, glob, os, re, sys
for s in sys.argv[1:]:
    d = f'/home/claude/helper/s20/{s}'; U = {}
    if os.path.exists(f'{d}/urls.json'): U = json.load(open(f'{d}/urls.json'))
    for f in sorted(glob.glob(f'{d}/img/nangman_{s}_*.png')):
        k = os.path.basename(f).replace(f'nangman_{s}_', '').replace('.png', '')
        r = subprocess.run(['python3', '/home/claude/helper/gas.py', 'image', f], capture_output=True, text=True)
        m = re.search(r'https://\S+', r.stdout)
        if m: U[k] = m.group(0).strip('"\',')
        else: print('FAIL', f, r.stdout[-200:], r.stderr[-300:])
    json.dump(U, open(f'{d}/urls.json', 'w'), indent=1); print(s, len(U))
