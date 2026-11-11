# 11/12 2차: 어사이드 원고를 글마다 한 폴더로 (학군지연재/NN화_<slug> · 새코너/<slug>)
import subprocess,glob,os,shutil,json
L=['hakgun_ep1','daechi_price','mokdong_school','banpo_school','junggye_school','bundang_school','pyeongchon_school','gwanggyo_school','songdo_school','mapo_school','gwangjang_school','ilsan_school','dunsan_school','beomeo_school','busan_school','bongseon_school','hakgun_final']
B='블로그/협업/4_어사이드/원고'
J=[(d,f'{B}/학군지연재/{i+1:02d}화_{d}') for i,d in enumerate(L)]+[(d,f'{B}/새코너/{d}') for d in ('detective_01','budget_01')]
out={}
for d,folder in J:
    S=f'/tmp/stg/{d}'; shutil.rmtree(S,ignore_errors=True); os.makedirs(S)
    A='/home/claude/w/aside_out'
    shutil.copy(f'{A}/nangman_{d}.html',f'{S}/{d}.html'); shutil.copy(f'{A}/nangman_{d}.txt',f'{S}/{d}.txt')
    fs=[f'{S}/{d}.html',f'{S}/{d}.txt']+sorted(glob.glob(f'{A}/nangman_{d}/*.jpg'))
    ok=0
    for f in fs:
        r=subprocess.run(['python3','/home/claude/helper/gas.py','fput',folder,f],capture_output=True,text=True)
        if r.returncode==0 and '"id"' in r.stdout: ok+=1
        else: print('FAIL',d,f,r.stderr[-200:],flush=True)
    out[d]={'folder':folder,'files':len(fs),'ok':ok}
    print(d,out[d],flush=True)
json.dump(out,open('/home/claude/helper/s20/_drive_1112b.json','w'),ensure_ascii=False,indent=0)
