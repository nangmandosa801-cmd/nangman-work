import sys,re,json,time,urllib.parse,collections,datetime,requests
sys.path.insert(0,'/home/claude/blogkit'); sys.path.insert(0,'/home/claude'); import seo,pubsync
from bs4 import BeautifulSoup
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','검단','고양','일산','파주','김포','남양주','구리','하남','의정부','양주','서울','강남','송파','강동','노원','은평','강서','마포','평택','안산','시흥','광명','군포','오산','광주 경기']
QS=[r+' 샷시 교체' for r in REG]+[r+' 샷시 시공' for r in ['수원','용인','성남','인천','고양','남양주','하남','의정부','부천','안양','서울','김포','화성']]+['살면서 샷시 교체 후기','거실 샷시 교체 후기','베란다 샷시 교체','구축 아파트 샷시 교체']
hits=collections.defaultdict(list)
for q in QS:
    s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    for b,n in dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)): hits[b].append((q,n))
    time.sleep(0.9)
json.dump(hits,open('hits.json','w'),ensure_ascii=False)
old=open('/home/claude/proj/낭만인테리어_제휴후보.md').read()
c=[(b,v) for b,v in sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1]))) if len(set(q for q,_ in v))>=2 and b not in old and b!='champion_chart']
print(len(hits),'곳 · 두 검색어 넘게',len(c),flush=True)
today=datetime.date(2026,10,6)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d); return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else today
R2=REG+['양평','가평','포천','동두천','과천','의왕','이천','여주','안성','청라','위례','광교','판교','별내','다산','미사','영등포','구로','관악','동작','성북','중랑','도봉','강북','서초','양천','금천','동대문','성동','광진','용산','종로','서대문']
out={}
for b,v in c[:110]:
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception: L=[]
    if not L: continue
    ds=[pd(d) for _,_,d in L]; n30=sum(1 for d in ds if (today-d).days<=30); span=(today-min(ds)).days
    sash=sum(1 for _,t,_ in L if re.search('샷시|샤시|창호|새시',t))
    rc=collections.Counter(r for _,t,_ in L for r in R2 if r in t).most_common(6)
    out[b]=dict(n=len(L),n30=n30,span=span,sash=sash,reg=rc,t3=[t for _,t,_ in L[:3]],n0=v[0][1],nq=len(set(q for q,_ in v)))
    time.sleep(0.3)
json.dump(out,open('prof.json','w'),ensure_ascii=False)
keep=[(b,o) for b,o in out.items() if o['n']>=10 and o['sash']/o['n']>=0.5 and 1<=o['n30']<=12]
print('남긴 곳',len(keep),flush=True)
res={}
for b,o in keep:
    try:
        r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':o['n0']},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
        so=BeautifulSoup(r.text,'html.parser'); cc=so.select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
        bt=re.search(r'<title>([^<]*)</title>',requests.get(f'https://blog.naver.com/PostList.naver?blogId={b}',headers={'User-Agent':'Mozilla/5.0'},timeout=30).text)
    except Exception: body=''; bt=None
    ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',body)))[:3]
    br=sorted(set(re.findall(r'LX|KCC|현대L&C|홈씨씨|영림|한화|휴그린|이건|윈체|금호|대리점|직영|공장',body)))
    who=[l[:90] for l in body.split('\n') if re.search(r'대표가|직접 시공|직영|공장|대리점|지역',l)][:3]
    res[b]=dict(o,bt=(bt.group(1).replace(' : 네이버 블로그','') if bt else ''),ph=ph,br=br,who=who)
    print(f"{b} | {res[b]['bt'][:36]} | 30일 {o['n30']}편 · 30편이 {o['span']}일치 · 샷시 {o['sash']}/{o['n']} | {o['reg']} | {ph} | {br}",flush=True)
    for w in who[:2]: print('     ',w)
    time.sleep(0.4)
json.dump(res,open('keep.json','w'),ensure_ascii=False)
