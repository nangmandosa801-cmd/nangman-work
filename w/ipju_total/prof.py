import sys,re,json,time,collections,datetime
sys.path.insert(0,'/home/claude'); import pubsync
hits=json.load(open('hits.json'))
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
B=[b for b,v in c if len(set(q for q,_ in v))>=3 and b not in('champion_chart','lyt777')][:150]
print(len(B),flush=True)
ITEMS={'줄눈':r'줄눈','탄성':r'탄성','새집증후군':r'새집증후군|베이크아웃|피톤치드|광촉매','나노코팅':r'나노|코팅(?!.*탄성)|상판 ?연마|엔지니어드','입주청소':r'입주 ?청소|이사 ?청소|준공 ?청소','사전점검':r'사전 ?점검|하자 ?점검','방충망':r'방충망|미세 ?방충','단열필름':r'단열 ?필름|썬팅|열차단','중문':r'중문','필름':r'인테리어 ?필름|시트지','실리콘':r'실리콘|코킹|곰팡이','마루코팅':r'마루 ?코팅|바닥 ?코팅'}
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','검단','청라','고양','일산','파주','운정','김포','남양주','구리','하남','의정부','양주','서울','강남','송파','강동','은평','평택','안산','시흥','광명','오산','대전','청주','세종','천안','아산','부산','창원','김해','양산','대구','광주','울산','전주','원주','춘천']
today=datetime.date(2026,10,7)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d)
    return datetime.date(int(m[1]),int(m[2]),int(m[3])) if m else today
out={}
for b in B:
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception as e: L=[]
    ds=[pd(d) for _,_,d in L]
    n30=sum(1 for d in ds if (today-d).days<=30)
    cov={k:sum(1 for _,t,_ in L if re.search(p,t)) for k,p in ITEMS.items()}
    rc=collections.Counter(r for _,t,_ in L for r in REG if r in t).most_common(6)
    out[b]=dict(n=len(L),n30=n30,last=str(max(ds)) if ds else '',cov=cov,reg=rc,nq=len(set(q for q,_ in hits[b])),t5=[t for _,t,_ in L[:6]])
    time.sleep(0.35)
json.dump(out,open('prof.json','w'),ensure_ascii=False)
r=sorted(out.items(),key=lambda x:(-sum(1 for v in x[1]['cov'].values() if v>=1),-x[1]['n30']))
for b,o in r[:70]:
    cv=' '.join(f'{k}{v}' for k,v in o['cov'].items() if v)
    print(f"{b} | 품목 {sum(1 for v in o['cov'].values() if v)} | 30일 {o['n30']}편 · 마지막 {o['last']} | {cv} | {o['reg'][:4]}")
