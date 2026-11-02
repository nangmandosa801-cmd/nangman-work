import re,sys,json,urllib.parse,subprocess
qs=["입주청소 평당 9000원","입주청소 평당 1만원","입주청소 평당 만원 경기","입주청소 34평 30만원","입주청소 30평 27만원","고양 입주청소 평당","일산 입주청소 가격","인천 입주청소 평당","서울 입주청소 평당 1만원","입주청소 새집증후군 같이 업체"]
out={}
for q in qs:
  u="https://m.search.naver.com/search.naver?where=m_blog&query="+urllib.parse.quote(q)
  h=subprocess.run(["curl","-s","-A","Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148",u],capture_output=True,text=True).stdout
  rows=[]
  for m in re.finditer(r'href="https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d+)"[^>]*>(.*?)</a>',h,re.S):
    t=re.sub('<[^>]+>','',m.group(3)).strip()
    if len(t)>8: rows.append((m.group(1),m.group(2),t[:70]))
  seen=set();r2=[]
  for x in rows:
    if x[1] in seen: continue
    seen.add(x[1]);r2.append(x)
  out[q]=r2[:10]
  print("##",q)
  for x in r2[:10]: print("  ",x)
json.dump(out,open('serp.json','w'),ensure_ascii=False)
