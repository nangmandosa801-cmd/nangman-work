import re,subprocess,html,json
from concurrent.futures import ThreadPoolExecutor
L="cleans-man best_2671 cleaninging cheongcham theclean_company arecorde10 clean-people majestymedia jclean_ kind_k-clean yokohm1436 seonghwan12345 duck2664 terry0245".split()
def get(u): return subprocess.run(["curl","-s","-m","15","-A","Mozilla/5.0 (iPhone)",u],capture_output=True,text=True).stdout
def one(i):
  x=get(f"https://rss.blog.naver.com/{i}.xml")
  links=[(0,n) for n in re.findall(r'<guid>https://blog\.naver\.com/[^/]+/(\d+)',x)[:3]]
  ph=set();pr=set();sj=0
  for _,no in links:
    t=get(f"https://m.blog.naver.com/PostView.naver?blogId={i}&logNo={no}")
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t)
    ph|=set(re.findall(r'0(?:10|50\d{1,2}|70|31|32|2)[-\s.)]?\d{3,4}[-\s.]?\d{4}',t))
    pr|=set(m.strip() for m in re.findall(r'[^.]{0,25}(?:평당\s?[\d,.]+\s?(?:천|만)?\s?원|\d{2,3}\s?만\s?원)[^.]{0,15}',t))
    sj+=len(re.findall('새집증후군|베이크아웃',t))
  return i,sorted(ph)[:3],list(pr)[:3],sj
with ThreadPoolExecutor(7) as ex:
  for i,ph,pr,sj in ex.map(one,L): print(i,'|',ph,'| 새집',sj,'|',pr)
