import urllib.request,urllib.parse,json,re,time,sys,pickle
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
def ac(q):
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    for _ in range(3):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf-8','ignore'))
            return [i[0] for i in j.get('items',[[]])[0]]
        except Exception: time.sleep(3)
    return []
def blog(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for _ in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
            ids=[]
            for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
                if b not in ids: ids.append(b)
            return len(ids),len(set(re.findall(r'ader\.naver\.com/v1/\w{20}',h))),('dong_jin_kim' in ids and ids.index('dong_jin_kim')+1 or 0)
        except Exception: time.sleep(4)
    return -1,-1,0
Q=[l.strip() for l in open(sys.argv[1]) if l.strip()]
rows=[]
for q in Q:
    it=ac(q); time.sleep(0.9); b,ad,me=blog(q); time.sleep(2.6)
    rows.append((q,len(it),b,ad,me,it))
    print('%-16s 제안%3d 경쟁%3d 광고%3d 내글%2d | %s'%(q,len(it),b,ad,me,' / '.join(it[:5])),flush=True)
pickle.dump(rows,open(sys.argv[2],'wb'))
