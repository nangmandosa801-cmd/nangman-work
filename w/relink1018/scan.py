import json,re,glob,collections
pub=json.load(open('/home/claude/pub/int_live_1018.json'))
ids={i for i,_ in pub}
norm=lambda s:re.sub(r'[\s,·「」.\-~～]','',s)
def find(t):
    n=norm(t)
    for i,pt in pub:
        p=norm(pt)
        if p==n or p.startswith(n[:16]) or n.startswith(p[:16]): return i,pt
    return None
files=[f for f in glob.glob('/mnt/user-data/uploads/블로그/interior/*/*_paste.html')]
sel=json.load(open('/home/claude/w/relink1018_files.json'))
files=['/mnt/user-data/uploads/블로그/interior/'+s for s in sel]
PH=re.compile(r'<span style="color:#1F3864;">([^<]+)</span> <span style="font-size:16px;color:#A8A296;">발행 예정</span>')
tot=collections.Counter(); rows=[]
for f in files:
    h=open(f).read()
    ph=PH.findall(h); links=re.findall(r'champion_chart/(\d{12})',h)
    bad=[i for i in links if i not in ids]
    hit=[(t,find(t)) for t in ph]
    tot['ph']+=len(ph); tot['ph_hit']+=sum(1 for _,x in hit if x); tot['badlink']+=len(bad); tot['other_ph']+=h.count('발행 예정')-len(ph)
    rows.append((f.split('/')[-2][:40],len(ph),sum(1 for _,x in hit if x),len(bad),len(set(links))))
print(tot)
for r in rows[:80]: print(r)
