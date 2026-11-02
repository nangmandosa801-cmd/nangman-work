import re,subprocess,html,json
from concurrent.futures import ThreadPoolExecutor
L=json.load(open('list.json'))
KEEP=re.compile('새집|베이크|입주청소|입주 청소|포름|신축')
DROP=re.compile('에어컨|포장이사|원룸|6평|태백|마산|창원|대구|청도|순천|천안|고성|빌라 계단|창업|누수|방화|월세|신차|냉장고|소이캔들|사업자|담배')
L=[x for x in L if KEEP.search(x['title']) and not DROP.search(x['title'])]
def get(u): return subprocess.run(["curl","-s","-m","20","-A","Mozilla/5.0 (Windows NT 10.0) Chrome/130",u],capture_output=True,text=True).stdout
def one(x):
  u=f"https://kin.naver.com/qna/detail.naver?dirId={x['dir']}&docId={x['doc']}"
  t=get(u)
  if '삭제되어' in t[:3000]: return None
  s=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
  qd=re.search(r'class="c-userinfo__info">\s*<span[^>]*>([^<]*)',t)
  dates=re.findall(r'(20\d\d\.\d{1,2}\.\d{1,2}\.)',s)
  body=re.search(r'<div class="questionDetail"[^>]*>(.*?)</div>',t,re.S) or re.search(r'class="c-heading__content"[^>]*>(.*?)</div>',t,re.S)
  bt=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',body.group(1)))).strip() if body else ''
  ac=re.search(r'답변\s*<em[^>]*>\s*(\d+)',t) or re.search(r'"answerCount"\s*:\s*(\d+)',t)
  adopt=('질문자 채택' in s) or ('질문자채택' in s)
  x.update(url=u,qdate=dates[0] if dates else '',body=bt[:500],ans=int(ac.group(1)) if ac else None,adopt=adopt)
  return x
with ThreadPoolExecutor(6) as ex: R=[r for r in ex.map(one,L) if r]
json.dump(R,open('detail.json','w'),ensure_ascii=False)
for r in sorted(R,key=lambda r:r['qdate'],reverse=True): print(r['qdate'],r['doc'],'ans',r['ans'],'채택' if r['adopt'] else '-',r['title'][:40],'|',r['body'][:120])
