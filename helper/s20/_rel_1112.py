import subprocess,shutil,os
L=['hakgun_ep1','daechi_price','mokdong_school','banpo_school','junggye_school','bundang_school','pyeongchon_school','gwanggyo_school','songdo_school','mapo_school','gwangjang_school','ilsan_school','dunsan_school','beomeo_school','busan_school','bongseon_school','hakgun_final']
B='블로그/협업/4_어사이드/원고'
J=[(d,f'{B}/학군지연재/{i+1:02d}화_{d}') for i,d in enumerate(L)]+[(d,f'{B}/새코너/{d}') for d in ('detective_01','budget_01','hanam_cancel','hanam_monthly200','hanam_renewal')]
A='/home/claude/w/aside_out'; P='/home/claude/tools/postkit'
for d,folder in J:
    W=f'/home/claude/helper/s20/{d}'; shutil.copy('/home/claude/helper/pg/tails.py',W)
    r=subprocess.run(['python3','mk.py'],cwd=W,capture_output=True,text=True,timeout=300)
    if r.returncode: print('MKFAIL',d,r.stderr[-300:],flush=True); continue
    for t in ('html2aside.py','html2aside_html.py'): subprocess.run(['python3',f'{P}/{t}','.',f'nangman_{d}'],cwd=W,capture_output=True)
    s=open(f'{A}/nangman_{d}.txt').read(); ok=s.count('[같이 보면 좋은 글]')==1 and s.rstrip().split('\n')[-1].startswith('▶')
    S=f'/tmp/stg/{d}'; shutil.rmtree(S,ignore_errors=True); os.makedirs(S)
    shutil.copy(f'{A}/nangman_{d}.html',f'{S}/{d}.html'); shutil.copy(f'{A}/nangman_{d}.txt',f'{S}/{d}.txt')
    up=sum('"id"' in subprocess.run(['python3','/home/claude/helper/gas.py','fput',folder,f'{S}/{d}.{x}'],capture_output=True,text=True).stdout for x in ('html','txt'))
    print(d,'block_ok' if ok else 'BLOCK?','up',up,flush=True)
