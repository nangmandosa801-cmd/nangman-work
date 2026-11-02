import sys,re,json,time,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
P=json.load(open('prof.json')); hits=json.load(open('hits.json'))
r=sorted(P.items(),key=lambda x:(-sum(1 for v in x[1]['cov'].values() if v>=1),-x[1]['n30']))
B=[b for b,o in r if sum(1 for v in o['cov'].values() if v)>=4][:46]
H={'User-Agent':'Mozilla/5.0'}
out={}
ITEM=r'줄눈|탄성|새집증후군|나노|입주 ?청소|사전 ?점검|방충망|단열 ?필름|마루 ?코팅|상판|중문|베이크아웃'
for b in B:
    L=pubsync.fetch(b,maxpage=1)
    try:
        rr=requests.get(f'https://blog.naver.com/PostList.naver?blogId={b}',headers=H,timeout=30); bt=re.search(r'<title>([^<]*)</title>',rr.text); bt=bt.group(1).strip() if bt else ''
    except Exception: bt=''
    info=dict(bt=bt,posts=[])
    ns=[(n,t,d) for n,t,d in L[:2]]
    hn=hits[b][0][1]
    if hn not in [n for n,_,_ in ns]: ns.append((hn,'(검색에 걸린 글)',''))
    for n,t,d in ns:
        try:
            rr=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={**H,'Referer':f'https://blog.naver.com/{b}'},timeout=30)
            so=BeautifulSoup(rr.text,'html.parser'); cc=so.select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
            tt=so.select_one('.se-title-text'); t2=tt.get_text(' ',strip=True) if tt else t
        except Exception: body='';t2=t
        ls=body.split('\n')
        info['posts'].append(dict(n=n,t=t2,d=d,ln=len(body),
            ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',body)))[:3],
            pkg=[l[:130] for l in ls if re.search(r'패키지|토탈|올인원|한 ?번에|원스톱|세트',l) and re.search(ITEM,l)][:3],
            pr=[l[:110] for l in ls if re.search(r'\d+\s*만\s*원',l)][:2],
            area=[l[:120] for l in ls if re.search(r'시공 ?(가능)? ?지역|출장|전 ?지역|전국|수도권',l)][:2],
            who=[l[:110] for l in ls if re.search(r'대표|직영|본사|지사|지점|가맹|직접 시공',l)][:3],
            ad=[l[:90] for l in ls if re.search(r'원고료|제공받아|협찬|체험단|소정의',l)][:1]))
        time.sleep(0.4)
    out[b]=info
    o=P[b]
    print('##',b,'|',bt[:50],'|',' '.join(f'{k}{v}' for k,v in o['cov'].items() if v),'|',o['reg'][:4])
    for p in info['posts']:
        print('  -',p['d'],p['t'][:56],'|',p['ln'],'자 | 전화',p['ph'], '| 광고' if p['ad'] else '')
        for k,lab in (('pkg','묶음'),('pr','가격'),('area','지역'),('who','사람')):
            for l in p[k][:2]: print('      ',lab+':',l)
json.dump(out,open('deep.json','w'),ensure_ascii=False)
