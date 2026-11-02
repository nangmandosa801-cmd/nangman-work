import re,subprocess,urllib.parse,html,json
from concurrent.futures import ThreadPoolExecutor
def get(u): return subprocess.run(["curl","-s","-m","20","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130",u],capture_output=True,text=True).stdout
qs=["입주청소 새집증후군","새집증후군 비용","새집증후군 업체","새집증후군 시공 효과","새집증후군 시공","입주청소 새집증후군 같이","입주청소 비용","입주청소 업체 추천","입주청소 업체","베이크아웃 업체","베이크아웃","신축 아파트 입주청소","새아파트 새집증후군","입주청소 30평","입주청소 34평"]
seen={}
def lst(q):
  out=[]
  for pg in (1,2):
    t=get(f"https://kin.naver.com/search/list.naver?query={urllib.parse.quote(q)}&period=1m&sort=date&page={pg}")
    for m in re.finditer(r'<dt>\s*<a href="(https://kin\.naver\.com/qna/detail\.naver\?dirId=(\d+)&docId=(\d+)[^"]*)"[^>]*>(.*?)</a>.*?<dd class="txt_inline">([^<]*)</dd>',t,re.S):
      out.append((m.group(3),m.group(2),html.unescape(re.sub('<[^>]+>','',m.group(4))).strip(),m.group(5).strip(),q))
  return out
with ThreadPoolExecutor(6) as ex:
  for r in ex.map(lst,qs):
    for d,dir_,ti,dt,q in r: seen.setdefault(d,dict(doc=d,dir=dir_,title=ti,date=dt,q=q))
print(len(seen))
json.dump(list(seen.values()),open('list.json','w'),ensure_ascii=False)
for v in sorted(seen.values(),key=lambda x:x['date'],reverse=True)[:60]: print(v['date'],v['doc'],v['title'][:50])
