import re,json,os
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
for s in sel:
    p=O+s if os.path.exists(O+s) else B+s; h=open(p).read()
    t=re.sub(r'<[^>]+>','',h)
    for m in re.finditer(r'[^.。\n]*비밀댓글[^\n]*',t): print(s[9:20],'|',m.group(0)[:260])
