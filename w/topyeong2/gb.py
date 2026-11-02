import sys,subprocess,re,time
from bs4 import BeautifulSoup
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126 Safari/537.36'
for n in sys.argv[1:]:
    u='https://www.guri.go.kr/www/selectBbsNttView.do?bbsNo=42&key=393&nttNo='+n
    t=''
    for i in range(5):
        t=subprocess.run(['curl','-sSL','-m','30','-A',UA,u],capture_output=True).stdout.decode('utf-8','replace')
        if len(t)>2000: break
        time.sleep(5)
    open('g_bodo%s.html'%n,'w').write(t)
    so=BeautifulSoup(t,'html.parser')
    for x in so(['script','style']): x.decompose()
    c=so.select_one('#contents') or so
    x=re.sub(r'\n{2,}','\n',c.get_text('\n',strip=True))
    i=x.find('상세보기'); 
    print('#####',n); print(x[max(i,0):max(i,0)+3500]); time.sleep(2)
