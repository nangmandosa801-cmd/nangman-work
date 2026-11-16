import json,urllib.request,urllib.parse,time,sys
code=sys.argv[1]; uids={}
for p in range(1,200):
    u=f"https://xn--ok0b236bp0a.com/experi_api?code={urllib.parse.quote(code)}&area=&page={p}"
    try: d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read())
    except Exception as e: print('err',p,e); break
    rows=d.get('data') or []
    if not rows: break
    for r in rows: uids[r['uid']]=(r['title'],r['addr'],r.get('summary',''))
    time.sleep(0.3)
json.dump(uids,open(f'list_{code}.json','w'),ensure_ascii=False); print(code,p,len(uids))
