import json,urllib.request,urllib.parse,time,sys
codes=sys.argv[1:]; uids={}
for code in codes:
  for area in ['02','031','032','033','041','042','043','044','051','052','053','054','055','061','062','063','064']:
    n0=len(uids)
    for p in range(1,60):
        u=f"https://xn--ok0b236bp0a.com/experi_api?code={urllib.parse.quote(code)}&area={area}&page={p}"
        try: d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read())
        except Exception as e: break
        rows=d.get('data') or []
        if not rows: break
        for r in rows: uids[r['uid']]=(r['title'],r['addr'],code)
        time.sleep(0.05)
    print(code,area,len(uids)-n0,flush=True)
json.dump(uids,open('list_area_'+'_'.join(c.replace('/','') for c in codes)+'.json','w'),ensure_ascii=False); print(len(uids))
