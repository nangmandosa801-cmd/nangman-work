import re,subprocess,json,sys,concurrent.futures as cf
def get(u):
    r=subprocess.run(['curl','-s','-m','15',u],capture_output=True)
    return r.stdout.decode('utf8','ignore')
urls=[]
for y in range(2019,2027):
    for m in range(1,13):
        for s in ['sub1-%d','sub2-%d','sub3-%d','sub4-%d','sub_%d']:
            for k in range(1,12):
                if s=='sub_%d': urls.append(f'https://rda.go.kr/webzine/{y}/{m:02d}/sub_{k+30}.html'); continue
                urls.append(f'https://rda.go.kr/webzine/{y}/{m:02d}/'+(s%k)+'.html')
out={}
def job(u):
    h=get(u)
    if '010-' not in h: return u,None
    t=re.sub(r'<[^>]+>','\n',h); t=re.sub(r'&nbsp;',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return u,t
with cf.ThreadPoolExecutor(16) as ex:
    for u,t in ex.map(job,urls):
        if t: out[u]=t
json.dump(out,open('rda_pages.json','w'),ensure_ascii=False)
print(len(urls),len(out))
