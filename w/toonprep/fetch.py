import urllib.request,re,html,json,os,sys
H={'User-Agent':'Mozilla/5.0'};HI={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}
def get(u,h=H): return urllib.request.urlopen(urllib.request.Request(u,headers=h),timeout=30).read()
out={}
for p in sys.argv[1:]:
    b,l=p.split('/'); d=f'/home/claude/w/toonprep/src/{b}_{l}'; os.makedirs(d,exist_ok=True)
    s=get(f'https://blog.naver.com/PostView.naver?blogId={b}&logNo={l}').decode('utf8','ignore')
    m=s.find('se-main-container'); body=s[m:] if m>0 else s
    seq=[];k=0;seen=set()
    for t in re.finditer(r'(https://postfiles\.pstatic\.net/[^"\'\s<>?]+)|<p[^>]*class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>',body,re.S):
        if t.group(1):
            u=t.group(1)
            if u in seen: continue
            seen.add(u);k+=1;f=f'{d}/{k:02d}.jpg'
            if not os.path.exists(f):
                try: open(f,'wb').write(get(u+'?type=w966',HI))
                except Exception as e: print('fail',u,e)
            seq.append(f'[IMG {k:02d}]')
        else:
            x=html.unescape(re.sub(r'<[^>]+>','',t.group(2))).strip()
            if x and x!='​': seq.append(x)
    out[p]=seq; open(f'{b}_{l}.txt','w').write('\n'.join(seq)); print(p,k)
