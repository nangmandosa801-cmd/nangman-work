import re,sys,os
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
import json; sel=json.load(open('/home/claude/w/relink1018_files.json'))
for k in sys.argv[1:]:
    s=next(x for x in sel if k in x); p=O+s if os.path.exists(O+s) else B+s
    h=open(p).read(); print('#####',p)
    t=re.sub(r'<table[^>]*>','\n[TABLE]',h); t=re.sub(r'<(?!/?a\b)[^>]+>','',t); t=re.sub(r'<a href="https://blog.naver.com/champion_chart/(\d+)"[^>]*>',r'[A \1]',t); t=re.sub(r'\n{3,}','\n\n',t)
    print(t)
