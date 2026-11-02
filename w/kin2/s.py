import re,html,subprocess,urllib.parse,json,sys
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
kws=sys.argv[1].split(',')
out={}
for k in kws:
  for p in (1,2):
    u=f"https://kin.naver.com/search/list.naver?query={urllib.parse.quote(k)}&sort=date&section=qna&page={p}"
    x=subprocess.run(['curl','-s','-A',UA,u],capture_output=True).stdout.decode('utf-8','ignore')
    for m in re.finditer(r'<dt>.*?href="([^"]*dirId=(\d+)[^"]*docId=(\d+)[^"]*)"[^>]*>(.*?)</a>.*?<dd class="txt_inline">(.*?)</dd>(.*?)</dd>',x,re.S):
      d=int(m.group(3))
      if d<495600000: continue
      t=html.unescape(re.sub('<[^>]+>','',m.group(4))).strip()
      out[d]={'kw':k,'dir':m.group(2),'doc':d,'title':t,'date':html.unescape(re.sub('<[^>]+>','',m.group(5))).strip()}
json.dump(out,open('found.json','w'),ensure_ascii=False,indent=1)
for d in sorted(out,reverse=True): print(d,out[d]['kw'],'|',out[d]['title'][:60])
