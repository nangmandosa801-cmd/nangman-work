import re,json,os
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
pub=json.load(open('/home/claude/pub/int_live_1018.json'))
norm=lambda s:re.sub(r'[\s,·「」.\-~～]','',s)
def find(t):
    n=norm(t)
    for i,pt in pub:
        p=norm(pt)
        if p==n or (len(n)>=10 and (p.startswith(n[:14]) or n.startswith(p[:14]))): return i
for s in sel:
    p=O+s if os.path.exists(O+s) else B+s; h=open(p).read()
    t=re.sub(r'<!--.*?-->','',h,flags=re.S); t=re.sub(r'<a [^>]*>.*?</a>','〔L〕',t,flags=re.S); t=re.sub(r'<[^>]+>','',t)
    for m in re.finditer(r'「([^」]{8,})」(\s?(?:에|을|를|글|도|과|와|편))',t):
        q=m.group(1)
        if '〔L〕' in q: continue
        print(s[9:20],'|',q[:70],'|',find(q))
