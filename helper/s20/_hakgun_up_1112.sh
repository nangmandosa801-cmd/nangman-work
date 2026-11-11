#!/bin/bash
# 학군지 1~8화 — 11/12 블로그 우체통 권한 오류(DriveApp 권한 없음)로 못 올린 그림 · 원고를 올린다. 우체통 권한을 다시 승인한 뒤 한 번 실행.
# 하는 일: urls.json 의 PENDING 그림을 gas.py image 로 올려 주소 교체 → mk.py → html2aside(--up) · html2aside_html(--up)
cd /home/claude/helper/s20 || exit 1
for d in hakgun_ep1 daechi_price mokdong_school banpo_school junggye_school bundang_school pyeongchon_school gwanggyo_school; do
  ( cd $d && python3 - <<'P' && python3 mk.py >/dev/null && python3 /home/claude/tools/postkit/html2aside.py . nangman_$d --up 2>&1 | grep name && python3 /home/claude/tools/postkit/html2aside_html.py . nangman_$d --up 2>&1 | grep photos )
import json,glob,subprocess,sys
u=json.load(open('urls.json'))
for k,v in u.items():
    if 'PENDING' in v:
        f=glob.glob(f'img/*_{k}.png')[0]
        r=subprocess.run(['python3','/home/claude/helper/gas.py','image',f],capture_output=True,text=True)
        try:
            j=json.loads(r.stdout); url=j if isinstance(j,str) else (j.get('url') or j.get('lh3') or next((x for x in j.values() if isinstance(x,str) and x.startswith('http')),''))
        except Exception: url=''
        if not url.startswith('http'): sys.exit('gas image 실패: '+r.stderr[-200:])
        u[k]=url
json.dump(u,open('urls.json','w'),ensure_ascii=False,indent=1)
P
done
