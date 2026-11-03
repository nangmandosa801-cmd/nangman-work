import json,requests,time,re,sys
S=requests.Session(); S.verify='/root/.ccr/ca-bundle.crt'
UA_PC='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
UA_M='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'
d=json.load(open('/home/claude/narrow/nm_posts.json'))
items=sorted(d.items(),reverse=True)[:int(sys.argv[1]) if len(sys.argv)>1 else 90]
def ranks(h):
    seen=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h):
        k=(m.group(1),m.group(2))
        if k not in seen: seen.append(k)
    return seen
out=[]
for n,t in items:
    kw=t.split(',')[0]
    r={}
    for nm,url,ua,q in [('pc_full','https://search.naver.com/search.naver',UA_PC,t[:60]),('m_full','https://m.search.naver.com/search.naver',UA_M,t[:60]),('m_kw','https://m.search.naver.com/search.naver',UA_M,kw)]:
        h=S.get(url,params=dict(where='m_blog' if nm.startswith('m') else 'blog',query=q),headers={'User-Agent':ua}).text
        L=ranks(h); pos=next((i+1 for i,(b,l) in enumerate(L) if l==n),None); r[nm]=pos; time.sleep(0.5)
    out.append(dict(logNo=n,title=t,kw=kw,**r)); print(n,r,t[:30],flush=True)
json.dump(out,open('nm_rank_1025.json','w'),ensure_ascii=False)
