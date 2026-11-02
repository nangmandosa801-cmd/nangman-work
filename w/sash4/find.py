import sys,re,json,time,urllib.parse,collections,datetime,requests
sys.path.insert(0,'/home/claude/blogkit'); sys.path.insert(0,'/home/claude'); import seo,pubsync
from bs4 import BeautifulSoup
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','검단','고양','일산','파주','김포','남양주','구리','하남','의정부','양주','서울','강남','송파','강동','노원','은평','강서','마포','평택','안산','시흥','광명','군포','오산','경기 광주']
SUB=['위례','미사','별내','다산','광교','판교','청라','운정','삼송','옥정','영통','수지','기흥','죽전','평촌','산본','중동','상동','부평','계양','목동','상계','잠실','둔촌','고덕','덕소','호평','진접','민락','행신','화정','탄현','봉담','향남','병점','세교','배곧','정왕','철산','하안','금천','관악','동작','성북','중랑','도봉','강북','서초','양천','동대문','성동','광진','영등포','구로','과천','의왕','이천','여주','안성','포천','동두천','양평','가평']
QS=[r+' 샷시 업체' for r in REG]+[r+' 창호 교체' for r in REG]+[r+' 샷시 교체' for r in SUB]+[r+' 샷시 견적' for r in ['수원','용인','성남','인천','고양','남양주','부천','안양','서울','화성','김포','의정부','하남','평택','안산']]+['아파트 샷시 교체 업체','샷시 교체 업체 추천','KCC 샷시 대리점','LX 샷시 대리점','영림 샷시 대리점','빌라 샷시 교체','주택 샷시 교체','이중창 교체 후기','발코니 샷시 교체','확장부 샷시 교체']
if 'search' in sys.argv:
    hits=collections.defaultdict(list)
    for i,q in enumerate(QS):
        try: s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
        except Exception as e: print('x',q,e,flush=True); continue
        for b,n in dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)): hits[b].append((q,n))
        time.sleep(0.8)
        if i%20==0: print('..',i,len(hits),flush=True); json.dump(hits,open('hits.json','w'),ensure_ascii=False)
    json.dump(hits,open('hits.json','w'),ensure_ascii=False); print('검색 끝',len(QS),len(hits),flush=True)
hits=json.load(open('hits.json'))
old=open('/home/claude/proj/낭만인테리어_제휴후보.md').read()
p2=json.load(open('/home/claude/w/sash2/prof.json')); h2=json.load(open('/home/claude/w/sash2/hits.json'))
today=datetime.date(2026,10,6)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d); return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else today
R2=REG+SUB
try: prof=json.load(open('prof.json'))
except Exception: prof={}
cand=[b for b,v in sorted(hits.items(),key=lambda x:-len(x[1])) if b not in p2 and b not in h2 and b not in old and b not in prof and b!='champion_chart']
print('새 블로그',len(cand),flush=True)
for i,b in enumerate(cand[:420]):
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception: L=[]
    if not L: prof[b]=dict(n=0); continue
    ds=[pd(d) for _,_,d in L]
    prof[b]=dict(n=len(L),n30=sum(1 for d in ds if (today-d).days<=30),span=(today-min(ds)).days,sash=sum(1 for _,t,_ in L if re.search('샷시|샤시|창호|새시',t)),
                 reg=collections.Counter(r for _,t,_ in L for r in R2 if r in t).most_common(6),ids=[n for n,_,_ in L[:5]],t3=[t for _,t,_ in L[:3]],nq=len(hits[b]))
    time.sleep(0.2)
    if i%20==0: json.dump(prof,open('prof.json','w'),ensure_ascii=False); print('..p',i,flush=True)
json.dump(prof,open('prof.json','w'),ensure_ascii=False); print('프로필 끝',len(prof),flush=True)
