import sys,re,html,json,urllib.request,time
out=json.load(open('dg.json')) if __import__('os').path.exists('dg.json') else {}
for s in sys.argv[1:]:
    if s in out: continue
    try:
        x=urllib.request.urlopen(urllib.request.Request('https://www.daangn.com/kr/local-profile/'+s+'/',headers={'User-Agent':'Mozilla/5.0'}),timeout=10).read().decode('utf-8','ignore')
    except Exception as e: out[s]={'err':str(e)}; continue
    t=re.search(r'<title>(.*?)</title>',x); m=re.search(r'<meta name="description" content="(.*?)"',x)
    txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x)))
    prices=[k.group(0).strip() for k in re.finditer(r'[^ ]{0,30}\s?[0-9,]{5,}원~?',txt)][:10]
    ph=sorted(set(re.sub(r'\D','',p) for p in re.findall(r'01[016]-?\d{3,4}-?\d{4}|0507-?\d{4}-?\d{4}',txt)))
    out[s]=dict(title=html.unescape(t.group(1)) if t else '',desc=html.unescape(m.group(1))[:200] if m else '',prices=prices,ph=ph)
    time.sleep(0.7)
json.dump(out,open('dg.json','w'),ensure_ascii=False,indent=0)
for s in sys.argv[1:]: v=out[s]; print(v.get('title','')[:50],'|',v.get('ph'),'|',' / '.join(v.get('prices',[]))[:200])
