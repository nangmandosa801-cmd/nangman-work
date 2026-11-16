import re,html,json,sys,subprocess,urllib.parse,time,os
qs=sys.argv[1:]; out='nb_hits.json'
H=json.load(open(out)) if os.path.exists(out) else {}
for q in qs:
    tot=0
    for start in (1,16):
        u='https://m.search.naver.com/search.naver?where=m_blog&start=%d&query='%start+urllib.parse.quote(q)
        h=subprocess.run(['curl','-s','-m','15','-A','Mozilla/5.0 (iPhone)',u],capture_output=True).stdout.decode('utf8','ignore')
        h=re.sub(r'<script.*?</script>','',h,flags=re.S); h=re.sub(r'<style.*?</style>','',h,flags=re.S)
        # split per result card by blog link
        parts=re.split(r'(?=href="https://m\.blog\.naver\.com/[A-Za-z0-9_]+/\d+)',h)
        for p in parts:
            bm=re.match(r'href="(https://m\.blog\.naver\.com/[A-Za-z0-9_]+/\d+)',p)
            t=html.unescape(re.sub(r'<[^>]+>',' ',p[:6000])); t=re.sub(r'\s+',' ',t)
            for m in re.finditer(r'01[016789][-. )]?\d{3,4}[-. ]?\d{4}',t):
                k=re.sub(r'\D','',m.group())
                if k not in H: H[k]=dict(q=q,url=bm.group(1) if bm else '',txt=t[max(0,m.start()-120):m.end()+40]); tot+=1
        time.sleep(0.4)
    print(q,tot,flush=True)
json.dump(H,open(out,'w'),ensure_ascii=False); print('total',len(H))
