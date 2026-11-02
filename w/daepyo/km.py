import json,subprocess,sys,urllib.parse
out=[]
for q in sys.argv[1:]:
  for p in (1,2,3):
    r=subprocess.run(['curl','-s','-m','15','-G','https://search.map.kakao.com/mapsearch/map.daum','--data-urlencode','q='+q,'--data-urlencode','msFlag=A','--data-urlencode','sort=0','--data-urlencode','page=%d'%p,'-H','Referer: https://map.kakao.com/','-A','Mozilla/5.0'],capture_output=True,text=True).stdout
    try: d=json.loads(r)
    except: break
    pl=d.get('place') or []
    for x in pl: out.append({'q':q,'name':x.get('name'),'tel':x.get('tel'),'addr':x.get('new_address') or x.get('address'),'cate':x.get('last_cate_name')})
    if not pl: break
seen=set();res=[]
for o in out:
  k=o['name']
  if k in seen: continue
  seen.add(k);res.append(o)
json.dump(res,open('dongjak_km.json','w'),ensure_ascii=False,indent=1)
print(len(res))
for o in res:
  if o['tel'] and o['tel'].startswith('010'): print(o['name'],o['tel'],o['addr'])
