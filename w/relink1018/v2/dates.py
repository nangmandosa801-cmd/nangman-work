import re,json,os
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
for s in sel:
    p=O+s if os.path.exists(O+s) else B+s; h=open(p).read()
    t=re.sub(r'<!--.*?-->','',h,flags=re.S); t=re.sub(r'<a [^>]*>.*?</a>','〔링크〕',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
    for m in re.finditer(r'(\d{1,2})월(?: (\d{1,2})일)?|올해|이번 달|다음 달|곧 올|다음 글|올릴 |올리겠|따로 쓰|정리할 |다룰 |예정|준비 중|이번 주|다음 주',t):
        print(s[9:20],'|',t[max(0,m.start()-60):m.end()+50])
