import re,json,os,sys
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
FORB=r'자리|갈[라렸리린랐아]|어요|예요|고요|최고|프리미엄|가능성|헷갈|놓습니다|가정|까닭|견줘|%p|나갈|값|기준|부천|차례로|1위|업체[는가](?=\s)|이어 드립|십시오'
def strip_main(h):
    h=re.sub(r'<!--.*?-->','',h,flags=re.S)
    k=h.find('같이 보면 좋은 글'); h=h[:k] if k>0 else h
    h=re.sub(r'<p style="font-size:1[45]px;color:#8A8578;[^"]*">자료 ·.*?</p>','',h,flags=re.S)
    h=re.sub(r'<span style="background-color:#EEF1F5;">이 글은 낭만 인테리어가.*?</span>','',h)
    h=re.sub(r'<a [^>]*>.*?</a>','',h,flags=re.S)
    return h
def hits(h):
    t=re.sub(r'<[^>]+>','',strip_main(h))
    return [(m.group(0),t[max(0,m.start()-40):m.end()+25].replace('\n',' ')) for m in re.finditer(FORB,t)]
if __name__=='__main__':
    for s in sel:
        p=O+s if os.path.exists(O+s) else B+s
        for w,c in hits(open(p).read()): print(os.path.basename(s)[17:-11],'|',w,'|',c)
