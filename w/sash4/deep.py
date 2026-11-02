import sys,re,json,time,collections,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0'}
PH=r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. )]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}'
def deep(b,ids,npost=6):
    ph=collections.Counter(); who=[]; br=collections.Counter(); bodies=0; imgs=0; mp=collections.Counter()
    for n in ids[:npost]:
        try:
            r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={**H,'Referer':f'https://blog.naver.com/{b}'},timeout=30)
            so=BeautifulSoup(r.text,'html.parser'); cc=so.select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
            imgs+=len(cc.select('img')) if cc else 0
            if cc:
                for m in cc.select('.se-map-info'): mp[m.get_text(' ',strip=True)[:70]]+=1
        except Exception: body=''
        if body: bodies+=1
        ph.update(set(re.findall(PH,body)))
        br.update(set(re.findall(r'LX|KCC|현대L&C|홈씨씨|영림|한화|휴그린|이건|윈체|금호|대리점|직영|공장|쇼룸|전시장',body)))
        who+=[l[:90] for l in body.split('\n') if re.search(r'대표가|직접 시공|직접 실측|출장|시공 ?지역|전 ?지역|위치|주소|본사',l) and len(l)<120][:2]
        time.sleep(0.3)
    try:
        j=requests.get(f'https://m.blog.naver.com/api/blogs/{b}',headers={'User-Agent':'Mozilla/5.0 (iPhone)','Referer':f'https://m.blog.naver.com/{b}'},timeout=20).json().get('result',{})
        nm=j.get('blogName',''); day=j.get('dayVisitorCount'); sub=j.get('subscriberCount'); intro=str(j.get('blogIntroduce') or '')
        ph.update(set(re.findall(PH,nm+' '+intro)))
    except Exception: nm=''; day=None; sub=None; intro=''
    return dict(nm=nm,day=day,sub=sub,intro=intro[:160],ph=[p for p,_ in ph.most_common(4)],br=[x for x,_ in br.most_common(8)],who=list(dict.fromkeys(who))[:4],bodies=bodies,imgs=imgs,mp=[m for m,_ in mp.most_common(2)])
if __name__=='__main__':
    src=sys.argv[1]; out=sys.argv[2]; ids=sys.argv[3:]
    prof=json.load(open(src)); res={}
    for b in ids:
        o=prof[b]; i=o.get('ids')
        if not i or len(i)<5:
            try: i=[n for n,_,_ in pubsync.fetch(b,maxpage=1)[:6]]
            except Exception: i=i or []
        d=deep(b,i); res[b]=dict(o,**d); json.dump(res,open(out,'w'),ensure_ascii=False)
        print(f"{b} | {d['nm'][:36]} | 30일 {o['n30']} · 샷시 {o['sash']}/{o['n']} · 오늘 {d['day']} · 이웃 {d['sub']} | {o['reg'][:5]} | {d['ph']} | {d['br']}",flush=True)
        print('    소개:',d['intro'][:120].replace('\n',' '))
        for w in d['who'][:3]: print('    ',w)
        print('    지도:',d['mp'])
        print('    최근:',' / '.join(t[:34] for t in o.get('t3',[])))
