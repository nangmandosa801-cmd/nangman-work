import sys,re,json,time,requests
sys.path.insert(0,'/home/claude'); import pubsync
from bs4 import BeautifulSoup
B=['pakpro_','doha_film','filmlab_','akrus33','hs6563','uniha0213','thebigfilm','film-gamsung','filmkoo527','gounfilm0913','matefilm_thousand','siotfilm','intefilm','gonggam_f','yminterior_96','ghkwns3411','moogyul96','zionew486','golf19park','himchan_interior','engelsoo','saebomfilm','wjdghks13258','moonf_ilm1']
H={'User-Agent':'Mozilla/5.0'}
out={}
for b in B:
    L=pubsync.fetch(b,maxpage=1)
    try:
        r=requests.get(f'https://blog.naver.com/PostList.naver?blogId={b}',headers=H,timeout=30); bt=re.search(r'<title>([^<]*)</title>',r.text); bt=bt.group(1).strip() if bt else ''
        nick=re.search(r'class="nick"[^>]*>(?:<[^>]+>)*([^<]+)',r.text); 
    except Exception: bt=''
    info=dict(bt=bt,posts=[])
    for n,t,d in L[:2]:
        try:
            r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={**H,'Referer':f'https://blog.naver.com/{b}'},timeout=30)
            so=BeautifulSoup(r.text,'html.parser'); cc=so.select_one('.se-main-container'); body=cc.get_text('\n',strip=True).replace('​','') if cc else ''
        except Exception: body=''; cc=None
        ls=body.split('\n')
        info['posts'].append(dict(n=n,t=t,d=d,ln=len(body),nimg=len(cc.select('.se-image')) if cc else 0,
            ph=sorted(set(re.findall(r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. ]\d{3,4}[-. ]\d{4}|1\d{3}[- ]\d{4}',body)))[:3],
            pr=[l[:110] for l in ls if re.search(r'\d+\s*만\s*원',l)][:3],
            asl=[l[:110] for l in ls if re.search(r'A/?S|보증|하자|무상',l)][:3],
            area=[l[:120] for l in ls if re.search(r'시공 ?(가능)? ?지역|출장|전 ?지역|전국',l)][:3],
            who=[l[:110] for l in ls if re.search(r'대표|직접 시공|1인|팀|기능사|경력|\d+년 ?차',l)][:3]))
        time.sleep(0.5)
    out[b]=info
    print('##',b,'|',bt[:60])
    for p in info['posts']:
        print('  -',p['d'],p['t'][:60],'|',p['ln'],'자 · 사진',p['nimg'],'| 전화',p['ph'])
        for k,lab in (('pr','가격'),('asl','A/S'),('area','지역'),('who','사람')):
            for l in p[k][:2]: print('      ',lab+':',l)
json.dump(out,open('deep.json','w'),ensure_ascii=False)
