import json,re,os,collections
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
pub=dict((i,t) for i,t in json.load(open('/home/claude/pub/int_live_1018.json')))
FORB=r'자리|갈[라렸리린랐아]|어요|예요|고요|최고|프리미엄|가능성|헷갈|놓습니다|가정|까닭|견줘|%p|나갈|값|기준|부천|차례로|1위|업체[는가](?=\s)'
def base(s): return O+s if os.path.exists(O+s) else B+s
def body(h):
    h=re.sub(r'<!--.*?-->','',h,flags=re.S)
    k=h.find('같이 보면 좋은 글'); 
    main=h[:k] if k>0 else h
    main=re.sub(r'<a [^>]*>.*?</a>','',main,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',main)
    return t
rows=[]
for s in sel:
    h=open(base(s)).read()
    t=body(h)
    ids=re.findall(r'champion_chart/(\d{12})',h)
    k=h.find('같이 보면 좋은 글'); tail=h[k:] if k>0 else ''
    style='card' if 'border-top:3px solid #1F3864' in tail[:400] or '같이 보면 좋은 글</span>' in tail[:300] else ('list21' if k>0 and 'font-size:21px' in h[k-80:k] else ('list27' if k>0 else 'none'))
    tids=list(dict.fromkeys(re.findall(r'champion_chart/(\d{12})',tail)))
    phones=re.findall(r'01[0-9]-\d{3,4}-\d{4}',h)
    r=dict(s=s[9:40],style=style,tail=len(tids),all=len(set(ids)),dead=[i for i in ids if i not in pub],
      phones=sorted(set(phones)),head='이 글은 낭만 인테리어가' in h, ireo=len(re.findall(r'이어 드립니다|이어 드리',t)),
      bimil='비밀댓글' in h, forb=re.findall(r'\S*(?:'+FORB+r')\S*',t), ni=len(re.findall(r'NI-\d{4}',h)), like='이 사진처럼 하고 싶다면' in h,
      ph=len(re.findall(r'발행 예정|\(예정\)|준비 중',h)), src=('자료 ·' in h))
    rows.append(r)
for r in rows: print(r)
print('=====')
for s in sel:
    t=re.sub(r'\s+',' ',body(open(base(s)).read()))
    for m in re.finditer(FORB,t):
        print(s[9:22],'|',t[max(0,m.start()-50):m.end()+30])
