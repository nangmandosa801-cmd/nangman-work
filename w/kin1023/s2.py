import re,subprocess,urllib.parse,html,json
from concurrent.futures import ThreadPoolExecutor
def get(u): return subprocess.run(["curl","-s","-m","20","-A","Mozilla/5.0 (Windows NT 10.0) Chrome/130",u],capture_output=True,text=True).stdout
qs=["입주청소 새집증후군","새집증후군","새집증후군 비용","새집증후군 업체","새집증후군 시공","새집증후군 효과","베이크아웃","베이크아웃 업체","새집냄새","포름알데히드 새아파트","입주청소","입주청소 비용","입주청소 업체","입주청소 추천","신축 입주청소","아파트 입주청소","입주청소 평당","줄눈 입주청소 순서","입주 전 청소","새아파트 냄새"]
seen={}
def lst(a):
  q,pg=a
  t=get(f"https://kin.naver.com/search/list.naver?query={urllib.parse.quote(q)}&period=1m&sort=date&page={pg}")
  return [(m.group(3),m.group(2),html.unescape(re.sub('<[^>]+>','',m.group(4))).strip()) for m in re.finditer(r'<dt>\s*<a href="(https://kin\.naver\.com/qna/detail\.naver\?dirId=(\d+)&docId=(\d+)[^"]*)"[^>]*>(.*?)</a>',t,re.S)]
with ThreadPoolExecutor(8) as ex:
  for r in ex.map(lst,[(q,p) for q in qs for p in range(1,6)]):
    for d,di,ti in r: seen.setdefault(d,dict(doc=d,dir=di,title=ti))
C=[v for v in seen.values() if int(v['doc'])>=494300000]
print(len(seen),len(C))
def one(x):
  u=f"https://kin.naver.com/qna/detail.naver?dirId={x['dir']}&docId={x['doc']}"; t=get(u)
  if '삭제되어' in t[:3000] or len(t)<5000: return None
  s=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
  ac=re.search(r'<span class="_answerCount">\s*(\d+)\s*</span>',t)
  qa=re.search(r'<div class="questionDetail"[^>]*>(.*?)</div>',t,re.S)
  body=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',qa.group(1)))).strip() if qa else ''
  dates=re.findall(r'(?:작성일|class="date"[^>]*>)\s*([^<]{6,20})',t)
  d1=re.search(r'<span class="c-userinfo__info">\s*(?:<span[^>]*>[^<]*</span>)?\s*작성일\s*([^<]+)',t)
  dd=re.findall(r'(20\d\d\.\d{1,2}\.\d{1,2}\.|\d+(?:분|시간|일) 전)',s)
  x.update(url=u,ans=int(ac.group(1)) if ac else 0,adopt=bool(re.search('질문자 ?채택',s) and 'adopt' in t),body=body[:600],date=dd[0] if dd else '')
  return x
with ThreadPoolExecutor(8) as ex: R=[r for r in ex.map(one,C) if r]
json.dump(R,open('detail2.json','w'),ensure_ascii=False)
for r in sorted(R,key=lambda r:-int(r['doc'])): print(r['doc'],r['date'],'답',r['ans'],'채택' if r['adopt'] else '',r['title'][:38],'|',r['body'][:150])
