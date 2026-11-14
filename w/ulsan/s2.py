import re,urllib.parse,urllib.request,json,collections
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'}
qs=["서사우미린더시그니처 입주청소","서사우미린더시그니처 새집증후군","서사 우미린 입주청소","다운2지구 우미린 새집증후군","울산 입주청소 업체","울산 입주청소 추천","울산 신축 입주청소","울산 새집증후군 시공","울산 베이크아웃","울산 새집증후군 업체","울산 입주청소 새집증후군 패키지","울산 중구 입주청소","울주 입주청소","울산 피톤치드 시공","울산 이사청소","울산 에피트스타시티 입주청소","울산 한양립스 더퍼스트하임 입주청소"]
hit=collections.defaultdict(set)
for q in qs:
  try: h=urllib.request.urlopen(urllib.request.Request('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q),headers=UA),timeout=20).read().decode('utf8','ignore')
  except Exception as e: print('ERR',q);continue
  for bid,no in re.findall(r'm\.blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h): hit[bid].add(q)
for k,v in sorted(hit.items(),key=lambda x:-len(x[1])): 
  if len(v)>=2: print(len(v),k)
json.dump({k:sorted(v) for k,v in hit.items()},open('hits2.json','w'),ensure_ascii=False)
