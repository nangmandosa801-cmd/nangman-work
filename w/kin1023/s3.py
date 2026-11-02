import re,subprocess,urllib.parse,html,json
from concurrent.futures import ThreadPoolExecutor
def get(u): return subprocess.run(["curl","-s","-m","20","-A","Mozilla/5.0 (Windows NT 10.0) Chrome/130",u],capture_output=True,text=True).stdout
qs=["입주청소 견적","입주청소 업체 추천 경기","신축 입주청소 비용","새집증후군 시공 업체 추천","새집증후군 시공 비용","피톤치드 시공","입주 줄눈 청소 순서","입주청소 몇평","새아파트 입주청소","입주청소 서울","입주청소 인천","입주청소 수원","입주청소 고양","입주청소 김포","입주청소 화성","입주청소 평택","신축 새집냄새","베이크아웃 업체 비용","새집증후군 측정","포름알데히드 측정"]
old=set(x['doc'] for x in json.load(open('detail2.json')))
seen={}
def lst(a):
  q,pg=a
  t=get(f"https://kin.naver.com/search/list.naver?query={urllib.parse.quote(q)}&period=1m&sort=date&page={pg}")
  return [(m.group(2),m.group(1),html.unescape(re.sub('<[^>]+>','',m.group(3))).strip()) for m in re.finditer(r'<dt>\s*<a href="https://kin\.naver\.com/qna/detail\.naver\?dirId=(\d+)&docId=(\d+)[^"]*"[^>]*>(.*?)</a>',t,re.S)]
with ThreadPoolExecutor(8) as ex:
  for r in ex.map(lst,[(q,p) for q in qs for p in range(1,4)]):
    for d,di,ti in r:
      if int(d)>=495000000 and d not in old: seen.setdefault(d,dict(doc=d,dir=di,title=ti))
KEEP=re.compile('입주|새집|베이크|포름|피톤|줄눈')
C=[v for v in seen.values() if KEEP.search(v['title'])]
print(len(seen),len(C))
def one(x):
  u=f"https://kin.naver.com/qna/detail.naver?dirId={x['dir']}&docId={x['doc']}"; t=get(u)
  if len(t)<5000: return None
  s=re.sub(r'<script.*?</script>','',t,flags=re.S)
  ac=re.search(r'<span class="_answerCount">\s*(\d+)\s*</span>',t)
  og=re.search(r'<meta property="og:description"\s+content="([^"]*)"',t,re.S)
  ti=re.search(r'<meta property="og:title"\s+content="([^"]*)"',t)
  qd=re.search(r'작성일\s*(?:</span>)?\s*(?:<span[^>]*>)?\s*([0-9.]+|[0-9]+(?:시간|분|일) 전)',t)
  m=re.search(r'class="questionDetail"[^>]*>(.*?)</div>',s,re.S)
  b=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',m.group(1))).strip() if m else ''
  x.update(url=u,ans=int(ac.group(1)) if ac else 0,adopt='질문자가 채택한 답변' in s,full_title=html.unescape(ti.group(1)) if ti else x['title'],body=html.unescape(b or (og.group(1) if og else '')),qdate=qd.group(1) if qd else '')
  return x
with ThreadPoolExecutor(8) as ex: R=[r for r in ex.map(one,C) if r]
json.dump(R,open('more.json','w'),ensure_ascii=False)
for r in sorted(R,key=lambda r:-int(r['doc'])): print(r['doc'],r['qdate'],'답',r['ans'],'채택' if r['adopt'] else '-',r['full_title'][:45],'|',r['body'][:200])
