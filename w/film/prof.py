import sys,re,json,time,collections,subprocess,requests,datetime
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
hits=json.load(open('hits.json'))
c=sorted(hits.items(),key=lambda x:-len(set(q for q,_ in x[1])))
B=[b for b,v in c if len(set(q for q,_ in v))>=3 and b not in('champion_chart','hanssem_sinbundang')][:75]
REG=['수원','용인','성남','분당','화성','동탄','안양','부천','인천','송도','고양','일산','파주','김포','남양주','구리','하남','의정부','서울','강남','송파','노원','마포','평택','안산','시흥','광명','대전','청주','세종','천안','부산','창원','김해','대구','광주','울산','양주','오산','군포','의왕','과천','검단','청라','강동','강서','은평','성북','위례','광교','판교','별내','다산']
out={}
today=datetime.date(2026,10,6)
def pd(d):
    m=re.match(r'(\d{4})\. ?(\d+)\. ?(\d+)',d)
    if m: return datetime.date(int(m[1]),int(m[2]),int(m[3]))
    return today
for b in B:
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception as e: L=[]
    ds=[pd(d) for _,_,d in L]
    n30=sum(1 for d in ds if (today-d).days<=30); span=(today-min(ds)).days if ds else None
    film=sum(1 for _,t,_ in L if '필름' in t)
    rc=collections.Counter(r for _,t,_ in L for r in REG if r in t).most_common(6)
    n=hits[b][0][1]; ph=[]; title=''; nimg=0; ln=0; pr=[]
    try:
        r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
        so=BeautifulSoup(r.text,'html.parser'); tt=so.select_one('.se-title-text'); cc=so.select_one('.se-main-container')
        title=tt.get_text(' ',strip=True) if tt else ''; body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
        ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',body)))[:3]
        pr=[l for l in body.split('\n') if re.search(r'\d+\s*만\s*원',l)][:3]; nimg=len(cc.select('.se-image')) if cc else 0; ln=len(body)
        nick=re.search(r"nickName\s*=\s*'([^']*)'|\"nickName\":\"([^\"]*)\"",r.text); bn=re.search(r'<title>([^<]*)</title>',r.text)
    except Exception as e: nick=bn=None
    out[b]=dict(n_list=len(L),n30=n30,span=span,film=film,reg=rc,title=title,ph=ph,pr=pr,nimg=nimg,ln=ln,qs=sorted(set(q for q,_ in hits[b])),bn=bn.group(1) if bn else '',t5=[t for _,t,_ in L[:5]])
    print(f'{b} | 최근30개가 {span}일치 · 30일 안 {n30}편 · 필름 제목 {film}/{len(L)} | {rc} | 전화 {ph} | 사진 {nimg} · {ln}자 | {title[:50]}',flush=True)
    time.sleep(0.5)
json.dump(out,open('prof.json','w'),ensure_ascii=False,default=str)
