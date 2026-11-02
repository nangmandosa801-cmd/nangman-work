import re,subprocess,html,urllib.parse,json,sys
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"
get=lambda u:subprocess.run(["curl","-s","-m","15","-A",UA,u],capture_output=True,text=True).stdout
Q={'울산':["울산 입주청소 가격","울산 새집증후군 비용","울산 입주청소 34평"],'부산':["부산 새집증후군 비용","에코델타 입주청소","부산 입주청소 34평 가격"],'전주':["전주 입주청소 가격","전주 새집증후군 비용","전주 입주청소 34평"]}
out={}
def post(i,n):
  t=get(f"https://m.blog.naver.com/PostView.naver?blogId={i}&logNo={n}")
  t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t)
  ti=re.search(r'<title>(.*?)</title>',t) 
  hits=re.findall(r'[^.!?]{0,40}(?:평당\s?[\d,.]+\s?(?:천|만)?\s?원|\d{2,3}\s?평[^.]{0,15}?\d{2,3}\s?만\s?원|\d{2,3}\s?만\s?원)[^.!?]{0,30}',t)
  return i,n,hits[:6]
for reg,qs in Q.items():
  ids=[]
  for q in qs:
    h=get("https://m.search.naver.com/search.naver?where=m_blog&query="+urllib.parse.quote(q))
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h):
      if (m.group(1),m.group(2)) not in ids: ids.append((m.group(1),m.group(2)))
  with ThreadPoolExecutor(8) as ex: res=list(ex.map(lambda x:post(*x),ids[:18]))
  out[reg]=[r for r in res if r[2]]
  print('##',reg)
  for i,n,h in out[reg][:10]: print(' ',i,n,'|',' // '.join(x.strip()[:90] for x in h[:3]))
json.dump(out,open('px.json','w'),ensure_ascii=False)
