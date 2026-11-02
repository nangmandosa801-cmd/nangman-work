import re,subprocess,html,json
from concurrent.futures import ThreadPoolExecutor
L="wjd80000 onedayoneclean erudaup tue2564 banjjakhomecare yamujin_care qjh2003 wjs9828 allinone2406 chobab2joa 82aegis wjdrb1986 1971982 change_clean clean_turn inja0130 goodgoodgood333 njnj5565 ozone_magic bake_dr karsna boss202707 hg_house dahuinhome luluhomecare_".split()
def get(u): return subprocess.run(["curl","-s","-m","15","-A","Mozilla/5.0 (iPhone)",u],capture_output=True,text=True).stdout
def one(i):
  x=get(f"https://rss.blog.naver.com/{i}.xml")
  nos=re.findall(r'<guid>https://blog\.naver\.com/[^/]+/(\d+)',x)
  ph=set();pr=[];eq=0;direct=0;sj_nos=[]
  tits=re.findall(r'<title>(.*?)</title>',x,re.S)[1:]
  for no,t in list(zip(nos,tits))[:12]:
    if re.search('새집|베이크|입주',t): sj_nos.append(no)
  for no in (sj_nos[:3] or nos[:2]):
    t=get(f"https://m.blog.naver.com/PostView.naver?blogId={i}&logNo={no}")
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t)
    ph|=set(re.findall(r'01[016789][-\s.)]?\d{3,4}[-\s.]?\d{4}',t))
    pr+=[m.strip() for m in re.findall(r'[^.]{0,30}(?:평당\s?[\d,.]+\s?(?:천|만)?\s?원|\d{2,3}\s?만\s?원)[^.]{0,20}',t)]
    eq+=len(re.findall('측정|포름알데히드 수치|ppm|측정기',t)); direct+=len(re.findall('직영|하루 한 집|대표가 직접|1일 1|하루 1',t))
  return i,dict(ph=sorted(ph)[:2],price=list(dict.fromkeys(pr))[:3],measure=eq,direct=direct)
out={}
with ThreadPoolExecutor(8) as ex:
  for i,d in ex.map(one,L): out[i]=d; print(i,d)
json.dump(out,open('price.json','w'),ensure_ascii=False)
