import sys,re,json,time,datetime,html,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
H=json.load(open('hits.json')); now=datetime.datetime(2026,10,10)
KW={'aircon':r'에어컨','move':r'이사','curtain':r'커튼|블라인드','office':r'사무실|칸막이|상가|인테리어|간판'}
res={}
for c,h in H.items():
    top=sorted(h.items(),key=lambda x:-len(set(x[1])))[:18]; res[c]=[]
    print('==',c)
    for b,v in top:
        s=seo._get(f'https://rss.blog.naver.com/{b}.xml') or ''
        s=html.unescape(s)
        t=re.sub(r'<!\[CDATA\[|\]\]>','',re.search(r'<title>(.*?)</title>',s,re.S).group(1)) if '<title>' in s else ''
        items=re.findall(r'<item>.*?<title>(.*?)</title>.*?<pubDate>(.*?)</pubDate>',s,re.S)
        n30=0;tt=[]
        for ti,pd in items:
            try:
                if (now-datetime.datetime.strptime(pd.strip()[:25],'%a, %d %b %Y %H:%M:%S')).days<=30: n30+=1
            except: pass
            tt.append(re.sub(r'<!\[CDATA\[|\]\]>','',ti).strip())
        rel=sum(1 for x in tt if re.search(KW[c],x))
        ph=[p for p,_ in collections.Counter(re.findall(r'01[0-9][- .]?\d{3,4}[- .]?\d{4}',s)).most_common(2)]
        print(f'  {b} | {t[:28]} | 30일 {n30} | 관련 {rel}/{len(items)} | {ph} | {tt[0][:50] if tt else ""}',flush=True)
        res[c].append(dict(b=b,t=t,n30=n30,rel=rel,n=len(items),ph=ph,first=tt[:3]))
        time.sleep(0.5)
json.dump(res,open('rss.json','w'),ensure_ascii=False)
