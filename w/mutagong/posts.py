import json,re,time,requests
from bs4 import BeautifulSoup
hits=json.load(open('hits.json'))
B=['door-diy777','danu111','ing_eng','homedoorworld','247door','joadoor-','poieqw1234','won6343337','luminadoor','fishhong012','home_repair_man','osg1','edenhome29','ckhomecare','fixmyhome','daetong32','epiekia55','1z10bau7f7enyc','design022','designwishow','cenacledesign','bebigo8272','dwcwao15257','ssgvdu','hykyhtih']
out={}
for b in B:
    ns=list(dict.fromkeys(n for _,n in hits.get(b,[])))[:3]
    for n in ns:
        try:
            r=requests.get('https://blog.naver.com/PostView.naver',params={'blogId':b,'logNo':n},headers={'User-Agent':'Mozilla/5.0','Referer':f'https://blog.naver.com/{b}'},timeout=30)
        except Exception as e: print(b,n,'ERR'); continue
        so=BeautifulSoup(r.text,'html.parser'); tt=so.select_one('.se-title-text'); c=so.select_one('.se-main-container')
        title=tt.get_text(' ',strip=True) if tt else ''; body=c.get_text('\n',strip=True).replace('​','') if c else ''
        m=re.search(r'se_publishDate[^>]*>([^<]+)',r.text); dt=m.group(1) if m else ''
        ph=sorted(set(re.findall(r'0\d{1,2}[-. ]?\d{3,4}[-. ]?\d{4}|1\d{3}[- ]?\d{4}',body)))
        mu=[l for l in body.split('\n') if '무타공' in l][:6]
        pr=[l for l in body.split('\n') if re.search(r'\d+\s*만\s*원|\d{2,3},000원',l)][:5]
        nimg=len(c.select('.se-image')) if c else 0
        out[f'{b}/{n}']=dict(title=title,dt=dt,len=len(body),ph=ph,mu=mu,pr=pr,nimg=nimg,body=body)
        print(f'## {b}/{n} | {dt} | {title[:70]} | {len(body)}자 · 사진 {nimg} | 전화 {ph[:3]}')
        for l in mu[:4]: print('   무타공:',l[:150])
        for l in pr[:3]: print('   가격:',l[:150])
        time.sleep(0.8)
json.dump(out,open('posts.json','w'),ensure_ascii=False)
