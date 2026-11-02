# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, time, json
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def blogsearch(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    r=urllib.request.Request(u,headers=UA)
    h=urllib.request.urlopen(r,timeout=20).read().decode('utf-8','ignore')
    hits=re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h)
    seen=[];  order=[]
    for bid,no in hits:
        if bid not in seen:
            seen.append(bid); order.append(bid)
    return order
def ac(q):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+
       '&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    r=urllib.request.Request(u,headers=UA)
    j=json.loads(urllib.request.urlopen(r,timeout=20).read().decode('utf-8','ignore'))
    it=j.get('items',[[]])[0]
    return [x[0] for x in it]

qs=['현관중문 종류','주방 중문','중문 종류','중문 잠금장치','중문']
for q in qs:
    try:
        o=blogsearch(q)
        pos=o.index('champion_chart')+1 if 'champion_chart' in o else 0
        print('%-12s 노출블로그 %2d개  champion_chart 순위: %s' % (q, len(o), pos if pos else '없음'))
    except Exception as e:
        print(q,'ERR',e)
    time.sleep(2.6)
