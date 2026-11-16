import re,html,json,subprocess,time,sys,os
def get(u): return subprocess.run(['curl','-s','-m','15',u],capture_output=True).stdout.decode('utf8','ignore')
ids=json.load(open('fs_ids.json')) if os.path.exists('fs_ids.json') else []
if not ids:
    s=set()
    for p in range(1,60):
        h=get(f'https://www.farmstay.co.kr/search?page={p}')
        f=set(re.findall(r'village/(A\d+)',h))
        if not f-s: break
        s|=f; time.sleep(0.2)
    ids=sorted(s); json.dump(ids,open('fs_ids.json','w')); print('ids',len(ids),'pages',p)
R=json.load(open('fs_v.json')) if os.path.exists('fs_v.json') else {}
t0=time.time()
for i in ids:
    if i in R: continue
    if time.time()-t0>100: break
    h=get(f'https://www.farmstay.co.kr/village/{i}')
    t=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',h,flags=re.S))); t=re.sub(r'\s+',' ',t)
    m=re.search(r'마을 기본정보 주소 (.*?) 대표자 (.*?) 전화문의 (\S+)',t)
    nm=re.search(r'"og:title" content="([^"]*)"',h) or re.search(r'<h2[^>]*>(.*?)</h2>',h)
    sp=re.search(r'재배하는|특산물(.{0,0})',t)
    R[i]=dict(name=(nm.group(1) if nm else ''),addr=m.group(1) if m else '',ceo=m.group(2) if m else '',tel=m.group(3) if m else '',intro=t[t.find('마을소개 '):t.find('마을소개 ')+250] if '마을소개 ' in t else '')
    time.sleep(0.15)
json.dump(R,open('fs_v.json','w'),ensure_ascii=False)
mob=[k for k,v in R.items() if v['tel'].startswith('01')]
print('done',len(R),'/',len(ids),'mobile',len(mob))
