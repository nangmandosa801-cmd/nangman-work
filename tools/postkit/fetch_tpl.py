import urllib.request,re,html,json,sys,os
def get(no):
    u=f'https://blog.naver.com/PostView.naver?blogId=febric_cleaning&logNo={no}'
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf8','ignore')
    t=html.unescape(re.search(r'<title>(.*?) : 네이버',x,re.S).group(1)).strip()
    ps=[html.unescape(re.sub(r'<[^>]+>','',a)).strip() for a in re.findall(r'<p class="se-text-paragraph[^>]*>(.*?)</p>',x,re.S)]
    ps=[p for p in ps if p and p!='​']
    imgs=[]
    for s in re.findall(r'data-lazy-src="([^"]+)"',x):
        s=s.split('?')[0]
        if s not in imgs: imgs.append(s)
    os.makedirs(no,exist_ok=True)
    out=[]
    for i,s in enumerate(imgs):
        ext=s.rsplit('.',1)[-1].lower()
        fn=f'{no}/{i:02d}.{ext}'
        if not os.path.exists(fn):
            d=urllib.request.urlopen(urllib.request.Request(s+'?type=w966',headers={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}),timeout=20).read()
            open(fn,'wb').write(d)
        out.append(fn)
    json.dump(dict(no=no,title=t,ps=ps,imgs=out),open(f'{no}/post.json','w'),ensure_ascii=False)
    return t,len(ps),out
for no in sys.argv[1:]:
    try: print(no,get(no)[0],len(get(no)[2]))
    except Exception as e: print('ERR',no,e)
