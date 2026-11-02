import sys,re,json,time,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
B='smmall0320 ceomoon_ jitaepung radical119 house_star zubell the1_hut saeumhousing namdo3639 sowoldesign bdh7361 acsystem seum164 kwonss0224 samwoohappycamp kmih7181 ynj7293 ahj1327 sbiado coldfire_yw hangang_housing k-8900 depoul vg_hom suduk1004 fen5581 einshill75 jbjm77 mmjd0712 koreafo hangyul6125 aa392 cjdeka770 newhousinghome huangtoman kjyy11333 raonhousing_ housingshop4u cspark99 tingthe1 yuyu9446 clayart-'.split()
H={'User-Agent':'Mozilla/5.0'}
PH=r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1[5-8]\d{2}[- ]\d{4}'
CALLED={'01033106729','01066182451','01042582811','01082696444','0543383638','01038155116','15660158','01038124872','15515157','01024404545','01028226571','01026214576'}
out={}
for b in B:
    try: L=pubsync.fetch(b,maxpage=1)
    except Exception: L=[]
    try:
        rr=requests.get(f'https://blog.naver.com/PostList.naver?blogId={b}',headers=H,timeout=30); bt=re.search(r'<title>([^<]*)</title>',rr.text); bt=bt.group(1).replace(': 네이버 블로그','').strip() if bt else ''
    except Exception: bt=''
    phs={}; price=[]; addr=[]; kind=[]; ad=0; called=False
    for p in re.findall(PH,bt): phs[p]=phs.get(p,0)+3
    for n,t,d in L[:4]:
        try:
            rr=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={**H,'Referer':f'https://blog.naver.com/{b}'},timeout=30)
            so=BeautifulSoup(rr.text,'html.parser'); cc=so.select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
        except Exception: body=''
        for p in re.findall(PH,body): phs[p]=phs.get(p,0)+1
        for l in body.split('\n'):
            if re.search(r'\d[\d,]*\s*만\s*원|\d,\d{3}만',l) and len(l)<110: price.append(l)
            if re.search(r'전시장|공장|본사|주소',l) and re.search(r'[가-힣]+(시|군|구) ',l) and len(l)<110: addr.append(l)
            if re.search(r'원고료|제공받아|협찬|체험단|소정의',l): ad+=1
        time.sleep(0.3)
    for p in phs:
        if re.sub(r'\D','',p) in CALLED: called=True
    if re.search(r'퓨전|바른하우징',bt): called=True
    out[b]=dict(bt=bt,phs=sorted(phs.items(),key=lambda x:-x[1])[:3],price=list(dict.fromkeys(price))[:3],addr=list(dict.fromkeys(addr))[:2],ad=ad,called=called,t=[t for _,t,_ in L[:3]])
    print('##',b,'|',bt[:46],'| 전화',out[b]['phs'],'| 이미 전화함' if called else '','| 광고글' if ad else '')
    for l in out[b]['addr'][:2]: print('    주소:',l[:100])
    for l in out[b]['price'][:2]: print('    가격:',l[:100])
    for t in out[b]['t'][:2]: print('    글:',t[:70])
json.dump(out,open('deep.json','w'),ensure_ascii=False)
