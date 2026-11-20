import json,re,subprocess,urllib.parse,time,collections
rss=json.load(open('rss.json'))
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
res=[]
for o in rss:
    kw=o['t'].split(',')[0].strip()
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(kw)
    s=subprocess.run(['curl','-s','-m','20','-A',UA,u],capture_output=True,text=True).stdout
    ids=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if m.group(1) not in ids and m.group(1) not in ('PostView','PostList'): ids.append(m.group(1))
    rank=ids.index('dong_jin_kim')+1 if 'dong_jin_kim' in ids else 0
    res.append({'kw':kw,'d':o['d'],'rank':rank,'n':len(ids),'top':ids[:5]})
    time.sleep(0.6)
json.dump(res,open('rank.json','w'),ensure_ascii=False)
ok=[r for r in res if r['n']>0]
print('잰 것',len(ok),'/',len(res))
b=collections.Counter()
for r in ok:
    k='1위' if r['rank']==1 else '2~3위' if 1<r['rank']<=3 else '4~10위' if 3<r['rank']<=10 else '11위 밖' if r['rank']>10 else '안 보임'
    b[k]+=1
print(dict(b))
c=collections.Counter()
for r in ok:
    for i in r['top'][:3]:
        if i!='dong_jin_kim': c[i]+=1
print('상위3 자주 나오는 블로그',c.most_common(12))
for r in res: print(r['d'][:6],r['rank'],r['n'],r['kw'][:28],r['top'][:3])
