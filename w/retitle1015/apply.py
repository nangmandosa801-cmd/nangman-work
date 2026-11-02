import re,shutil,os,subprocess,sys
from titles import NEW
for old,f,t in NEW:
    bak=f.replace('_post.html','_post_before_retitle.html')
    if not os.path.exists(bak): shutil.copy(f,bak)
    h=open(bak).read()
    m=re.search(r'(<p style="font-size:3[0-9]px;font-weight:700[^"]*">)(.*?)(</p>)',h,re.S)
    h=h[:m.start(2)]+t+h[m.end(2):]
    h=re.sub(r'<title>.*?</title>',f'<title>{t}</title>',h,flags=re.S)
    open(f,'w').write(h)
    r=subprocess.run(['python3','/home/claude/blogkit/seo.py',f],capture_output=True,text=True).stdout
    x=[l.strip() for l in r.splitlines() if '✘' in l]
    print(len(x),t.split(',')[0]); [print('    ',l[:150]) for l in x]
