import re,urllib.request,html,sys
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=25).read().decode('utf8','ignore')
def one(b):
  x=get(f'https://rss.blog.naver.com/{b}.xml')
  links=re.findall(r'(https://blog.naver.com/[A-Za-z0-9_-]+/\d+)',x)[:5]
  ph={};kk=set()
  for l in links:
    m=re.search(r'/(\d{9,})',l)
    if not m: continue
    try: t=get(f'https://m.blog.naver.com/PostView.naver?blogId={b}&logNo={m.group(1)}')
    except Exception: continue
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    for p in re.findall(r'(?<!\d)(01[016789][-. )]*\d{3,4}[-. ]*\d{4}|0507[-. ]*\d{4}[-. ]*\d{4}|05[0-9][-. )]*\d{3,4}[-. ]*\d{4}|1[5-6]\d\d[-. ]\d{4})(?!\d)',t):
      p=re.sub(r'[^\d]','',p); ph[p]=ph.get(p,0)+1
    for k in ['카톡','카카오','톡톡','오픈채팅','새집증후군','입주청소','탄성','줄눈','케라폭시','폴리우레아','직영','대표']:
      if k in t: kk.add(k)
  return b,ph,sorted(kk)
with ThreadPoolExecutor(8) as ex:
  for b,ph,kk in ex.map(one,sys.argv[1:]): print(b,dict(sorted(ph.items(),key=lambda x:-x[1])[:4]),kk)
