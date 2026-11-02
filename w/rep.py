import urllib.request,urllib.parse,json,re,time,pickle,os
UA={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}
CF='rep.pkl'; C=pickle.load(open(CF,'rb')) if os.path.exists(CF) else {}
def sv(): pickle.dump(C,open(CF,'wb'))
def ac(q):
    k=('a',q)
    if k in C: return C[k]
    u=('https://ac.search.naver.com/nx/ac?q='+urllib.parse.quote(q)+'&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
    for _ in range(3):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf-8','ignore'))
            C[k]=[i[0] for i in j.get('items',[[]])[0]]; sv(); return C[k]
        except Exception: time.sleep(3)
    return []
def blog(q):
    k=('b',q)
    if k in C: return C[k]
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for _ in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode('utf-8','ignore')
            ids=[]
            for b,n in re.findall(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)',h):
                if b not in ids: ids.append(b)
            C[k]=(len(ids),len(set(re.findall(r'ader\.naver\.com/v1/\w{20}',h)))); sv(); return C[k]
        except Exception: time.sleep(4)
    return (-1,-1)
Q=[('A1','현관문 안닫힘'),('A1','중문 설치 후 현관문'),('A1','현관 도어클로저'),
   ('A2','중문 소음'),('A2','중문 드르륵'),('A2','중문 소리'),
   ('A3','중문 레일 구리스'),('A3','중문 윤활'),
   ('A4','중문 유리 깨짐'),('A4','강화유리 자파'),('A4','중문 유리 교체'),
   ('A5','스윙 중문 처짐'),('A6','중문 흔들림'),('A7','중문 뻑뻑'),
   ('A8','중문 모헤어'),('A8','중문 틈새'),('A9','현관문 결로'),('A9','현관 결로'),
   ('A10','현관 담배냄새'),('A11','중문 청소'),('A11','중문 레일 청소'),
   ('A12','중문 필름'),('A12','중문 리폼'),
   ('B1','모루유리 중문'),('B1','사틴유리 중문'),('B3','입주박람회 중문'),('B4','옵션 중문'),
   ('B6','중문 없이'),('B7','복도식 아파트 중문'),('B8','무타공 중문'),
   ('C1','전세 중문'),('C2','세입자 중문'),('C3','중문 이전 설치'),('C4','강아지 현관 탈출'),('C4','강아지 중문'),
   ('C5','중문 손끼임'),('C6','유모차 중문'),('C7','1층 중문'),('C8','좁은 현관 중문'),('C9','현관 말발굽'),
   ('C10','빌라 중문'),('C10','오피스텔 중문'),('D1','겨울 중문'),('D3','사전점검 중문'),('D3','입주 전 중문')]
rows=[]
for code,q in Q:
    it=ac(q); time.sleep(0.8); b,ad=blog(q); time.sleep(2.5)
    rows.append((code,q,len(it),b,ad,it))
pickle.dump(rows,open('rep_rows.pkl','wb'))
for code,q,n,b,ad,it in rows:
    ok='●' if (n>0 and 0<b<=20) else ' '
    print('%s %-4s %-14s 제안%3d 경쟁%3d 광고%3d | %s'%(ok,code,q,n,b,ad,' / '.join(it[:4])))
