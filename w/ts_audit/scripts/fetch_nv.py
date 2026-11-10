import json,os,subprocess,re,hashlib
P=json.load(open('/home/claude/w/ts_audit/raw/parsed.json'))
seen=set()
for p in P:
    for bid,no,_ in p['naver_links'][:12]:
        k=f'{bid}_{no}'
        if k in seen: continue
        seen.add(k); f=f'/home/claude/w/ts_audit/nv/{k}.html'
        if os.path.exists(f) and os.path.getsize(f)>10000: continue
        subprocess.run(['curl','-sS','-m','30','-A','Mozilla/5.0','-o',f,f'https://blog.naver.com/PostView.naver?blogId={bid}&logNo={no}'])
print(len(seen))
