import re,urllib.parse,urllib.request,json,collections,sys
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'}
qs=["다운2지구 우미린 줄눈","다운2지구 우미린 탄성코트","다운2지구 우미린 입주청소","우미린더시그니처 줄눈","울산 줄눈 탄성코트","울산 줄눈 시공","울산 탄성코트","울산 입주청소 새집증후군","울산 입주청소","울산 새집증후군","울산 케라폭시","울산 입주케어","울산 다운동 줄눈","울주 줄눈 탄성코트"]
hit=collections.defaultdict(set);title={}
for q in qs:
  try:
    h=urllib.request.urlopen(urllib.request.Request('https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q),headers=UA),timeout=20).read().decode('utf8','ignore')
  except Exception as e: print('ERR',q,e);continue
  for bid,no in re.findall(r'm\.blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',h):
    hit[bid].add(q)
json.dump({k:sorted(v) for k,v in hit.items()},open('hits.json','w'),ensure_ascii=False)
for k,v in sorted(hit.items(),key=lambda x:-len(x[1]))[:45]: print(len(v),k,'|',' / '.join(sorted(v))[:120])
