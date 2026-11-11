# 11/12 새 코너 3편(11/16~11/20) → 드라이브 「원고/새코너/<slug>/」 (견본 _drive_1112b.py 와 같은 규칙: <slug>.html · <slug>.txt · NN.jpg)
import subprocess, glob, os, shutil, json
B = '블로그/협업/4_어사이드/원고/새코너'; A = '/home/claude/w/aside_out'; out = {}
for d in ('hanam_cancel', 'hanam_monthly200', 'hanam_renewal'):
    S = f'/tmp/stg/{d}'; shutil.rmtree(S, ignore_errors=True); os.makedirs(S)
    shutil.copy(f'{A}/nangman_{d}.html', f'{S}/{d}.html'); shutil.copy(f'{A}/nangman_{d}.txt', f'{S}/{d}.txt')
    fs = [f'{S}/{d}.html', f'{S}/{d}.txt'] + sorted(glob.glob(f'{A}/nangman_{d}/*.jpg')); ok = 0
    for f in fs:
        r = subprocess.run(['python3', '/home/claude/helper/gas.py', 'fput', f'{B}/{d}', f], capture_output=True, text=True)
        if r.returncode == 0 and '"id"' in r.stdout: ok += 1
        else: print('FAIL', d, f, r.stderr[-200:], flush=True)
    out[d] = {'folder': f'{B}/{d}', 'files': len(fs), 'ok': ok}; print(d, out[d], flush=True)
json.dump(out, open('/home/claude/helper/s20/_drive_1116.json', 'w'), ensure_ascii=False, indent=0)
