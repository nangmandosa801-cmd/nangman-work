import requests,re,time,json,sys,urllib.parse,html as H
def G(u,**k):
    for i in range(4):
        try: return requests.get(u,**k)
        except Exception as e: time.sleep(3+i*3)
    raise SystemExit('net fail '+u)
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'}
KW=json.loads(sys.argv[1]); out=[]; seen=set()
st='/home/claude/watch/jisikin_state.json'
try: done=set(json.load(open(st))['done'])
except: done=set()
for kw,post in KW:
    u='https://m.search.naver.com/search.naver?where=m_kin&query='+urllib.parse.quote(kw)+'&nso=so%3Add%2Cp%3A1m'
    h=G(u,headers=UA,timeout=20).text
    ids=[]
    for d,doc in re.findall(r'(?:dirId=|dirs/)(\d+)(?:&amp;docId=|/docs/)(\d+)',h):
        if doc not in ids: ids.append(doc); 
        if len(ids)>8: break
    pairs=list(dict.fromkeys(re.findall(r'(?:dirId=|dirs/)(\d+)(?:&amp;docId=|/docs/)(\d+)',h)))[:8]
    for d,doc in pairs:
        if doc in seen or doc in done: continue
        seen.add(doc)
        q=G(f'https://kin.naver.com/qna/detail.naver?dirId={d}&docId={doc}',headers={'User-Agent':'Mozilla/5.0'},timeout=20).text
        t=re.findall(r'<title>\s*(.*?)\s*: 지식iN',q,re.S); t=H.unescape(t[0].strip()) if t else ''
        dt=re.search(r'작성일</span>\s*<span[^>]*>([\d.]+)',q) or re.search(r'작성일\D{0,40}?(\d{4}\.\d{2}\.\d{2})',re.sub('<[^>]+>','|',q))
        dt=dt.group(1) if dt else ''
        na=re.search(r'(\d+)</em>\s*개 답변',q) or re.search(r'\|(\d+)\|개 답변',re.sub('<[^>]+>','|',q))
        na=int(na.group(1)) if na else -1
        body=re.search(r'작성일.*?\|\s*\|\s*\|(.*?)(?:\|\s*){4}',re.sub(r'\s+',' ',re.sub('<[^>]+>','|',q)))
        out.append(dict(kw=kw,post=post,dir=d,doc=doc,title=t,date=dt,answers=na,url=f'https://kin.naver.com/qna/detail.naver?dirId={d}&docId={doc}',body=(body.group(1)[:400] if body else '')))
        time.sleep(0.6)
    time.sleep(1)
json.dump(out,open('/home/claude/w/jisikin/cand.json','w'),ensure_ascii=False,indent=1)
for o in out:
    if o['date']>='2026.09.10': print(o['date'],o['answers'],o['kw'],'|',o['title'][:60],'|',o['doc'])
