import sys,re,json,time,collections,datetime,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
hits=json.load(open('hits.json')); prof=json.load(open('prof.json'))
old=open('/home/claude/proj/낭만인테리어_제휴후보.md').read()
today=datetime.date(2026,10,6)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d); return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else today
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','검단','고양','일산','파주','김포','남양주','구리','하남','의정부','양주','서울','강남','송파','강동','노원','은평','강서','마포','평택','안산','시흥','광명','군포','오산','양평','가평','포천','과천','의왕','이천','여주','안성','청라','위례','광교','판교','별내','다산','미사','영등포','구로','관악','동작','성북','중랑','도봉','강북','서초','양천','금천','동대문','성동','광진','용산','종로','서대문']
cand=[b for b,v in sorted(hits.items(),key=lambda x:-len(x[1])) if b not in prof and b not in old and b!='champion_chart']
print('새로 볼 곳',len(cand),flush=True)
for i,b in enumerate(cand[:260]):
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception: L=[]
    if not L: prof[b]=dict(n=0); continue
    ds=[pd(d) for _,_,d in L]
    prof[b]=dict(n=len(L),n30=sum(1 for d in ds if (today-d).days<=30),span=(today-min(ds)).days,sash=sum(1 for _,t,_ in L if re.search('샷시|샤시|창호|새시',t)),
                 reg=collections.Counter(r for _,t,_ in L for r in REG if r in t).most_common(6),ids=[n for n,_,_ in L[:3]],t3=[t for _,t,_ in L[:3]])
    time.sleep(0.2)
    if i%20==0: json.dump(prof,open('prof.json','w'),ensure_ascii=False); print('..',i,flush=True)
json.dump(prof,open('prof.json','w'),ensure_ascii=False)
keep=[b for b,o in prof.items() if o.get('n',0)>=10 and o['sash']/o['n']>=0.5 and 1<=o['n30']<=15 and b not in old]
print('조건에 맞는 곳',len(keep),flush=True)
res={}
H={'User-Agent':'Mozilla/5.0'}
for b in keep:
    o=prof[b]; ids=o.get('ids') or [hits[b][0][1]]
    ph=set(); who=[]; br=set()
    for n in ids[:3]:
        try:
            r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={**H,'Referer':f'https://blog.naver.com/{b}'},timeout=30)
            cc=BeautifulSoup(r.text,'html.parser').select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
        except Exception: body=''
        ph|=set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',body))
        br|=set(re.findall(r'LX|KCC|현대L&C|홈씨씨|영림|한화|휴그린|이건|윈체|금호|대리점|직영|공장',body))
        who+=[l[:80] for l in body.split('\n') if re.search(r'대표가|직접 시공|출장|시공 ?지역|전 ?지역',l)][:1]
        time.sleep(0.3)
    try:
        j=requests.get(f'https://m.blog.naver.com/api/blogs/{b}',headers={'User-Agent':'Mozilla/5.0 (iPhone)','Referer':f'https://m.blog.naver.com/{b}'},timeout=20).json().get('result',{})
        nm=j.get('blogName',''); day=j.get('dayVisitorCount'); ph|=set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',nm+' '+str(j.get('blogIntroduce',''))))
    except Exception: nm=''; day=None
    res[b]=dict(o,nm=nm,day=day,ph=sorted(ph)[:3],br=sorted(br),who=who[:2])
    json.dump(res,open('keep2.json','w'),ensure_ascii=False)
    print(f"{b} | {nm[:34]} | 30일 {o['n30']}편 · 샷시 {o['sash']}/{o['n']} · 오늘 {day} | {o['reg'][:5]} | {res[b]['ph']} | {res[b]['br']}",flush=True)
json.dump(res,open('keep2.json','w'),ensure_ascii=False)
