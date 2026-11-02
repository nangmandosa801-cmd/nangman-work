# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, json, time, pickle, os, csv, io, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
C=pickle.load(open('jm49.pkl','rb')) if os.path.exists('jm49.pkl') else {}
def ac(q):
    try:
        with urllib.request.urlopen(urllib.request.Request(AC%urllib.parse.quote(q),headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        return [i[0] for i in d.get('items',[[]])[0]]
    except Exception: return []
def ba(q):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(q)
    for _ in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=15) as x:
                h=x.read().decode('utf-8','ignore')
            b=[]
            for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_-]+)/(\d+)', h):
                if m.group(1) not in b: b.append(m.group(1))
            return len(b), len(set(re.findall(r'ader\.naver\.com/v1/\w{20}', h)))
        except Exception: time.sleep(4)
    return -1,-1
Q=[r[0] for r in csv.reader(io.open('/mnt/user-data/outputs/int/중문_남은글감.csv',encoding='utf-8-sig'))][1:]
Q=[q for q in Q if q]
for i,q in enumerate(Q):
    if q in C and C[q][1]>=0: continue
    a=ac(q); time.sleep(0.4); b,ad=ba(q); C[q]=(len(a),b,ad)
    pickle.dump(C,open('jm49.pkl','wb'))
    print('%2d/%d %-20s %2d %3d %3d' % (i+1,len(Q),q,len(a),b,ad)); sys.stdout.flush()
    time.sleep(2.0)
print('완료 %d' % len([q for q in Q if q in C and C[q][1]>=0]))
