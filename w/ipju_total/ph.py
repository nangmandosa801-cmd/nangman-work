import sys,re,json,time,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'}
PH=r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1[5-8]\d{2}[- ]?\d{4}'
def body(b,n):
    rr=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
    so=BeautifulSoup(rr.text,'html.parser'); cc=so.select_one('.se-main-container')
    return (cc.get_text('\n',strip=True).replace('​','') if cc else ''), rr.text
B=sys.argv[1:]
for b in B:
    L=pubsync.fetch(b,maxpage=1)
    phs={}; areas=[]; items=[]; links=set()
    try:
        m=requests.get(f'https://m.blog.naver.com/api/blogs/{b}',headers={**H,'Referer':f'https://m.blog.naver.com/{b}'},timeout=20).text
        intro=re.search(r'"(?:blogDirectoryName|introduce|description)":"([^"]*)"',m)
        name=re.search(r'"blogName":"([^"]*)"',m); nick=re.search(r'"nickName":"([^"]*)"',m); intro2=re.search(r'"introduce":"([^"]*)"',m)
        for p in re.findall(PH,m): phs[p]=phs.get(p,0)+1
        head=f"{name.group(1) if name else ''} / {nick.group(1) if nick else ''} / {intro2.group(1)[:160] if intro2 else ''}"
    except Exception as e: head='ERR '+str(e)
    for n,t,d in L[:6]:
        try: bd,raw=body(b,n)
        except Exception: continue
        for p in re.findall(PH,bd): phs[p]=phs.get(p,0)+1
        for l in bd.split('\n'):
            if re.search(r'시공 ?(가능)? ?지역|출장 ?지역|서비스 ?지역|전 ?지역',l) and len(l)<140: areas.append(l)
            if re.search(r'줄눈',l) and re.search(r'탄성',l) and re.search(r'청소|새집|나노|코팅',l) and len(l)<160: items.append(l)
        time.sleep(0.3)
    print('##',b,'|',head)
    print('   전화',sorted(phs.items(),key=lambda x:-x[1])[:4])
    for l in list(dict.fromkeys(areas))[:3]: print('   지역:',l)
    for l in list(dict.fromkeys(items))[:3]: print('   품목:',l)
    print('   최근:',' / '.join(t[:40] for _,t,_ in L[:4]))
