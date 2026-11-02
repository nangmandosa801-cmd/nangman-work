import sys,subprocess,re,html,time,os
from bs4 import BeautifulSoup
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
def raw(u,tries=5):
    for i in range(tries):
        s=subprocess.run(['curl','-sSL','-m','40','-A',UA,u],capture_output=True).stdout
        if len(s)>800: break
        time.sleep(5)
    for enc in ('utf-8','euc-kr','cp949'):
        try: return s.decode(enc)
        except Exception: pass
    return s.decode('utf-8','replace')
def text(u,sel=None,save=None):
    t=raw(u)
    if save: open(save,'w').write(t)
    so=BeautifulSoup(t,'html.parser')
    for x in so(['script','style','noscript']): x.decompose()
    el=None
    for s in ([sel] if sel else [])+['#article-view-content-div','#articleBody','.article_view','#news_body_area','.article-body','#articeBody','article','.view_con','.bbs_view','.bbs--view','#contents','.news_view','#content']:
        el=so.select_one(s)
        if el and len(el.get_text(strip=True))>200: break
        el=None
    tt=so.select_one('title')
    return ('TITLE: '+(tt.get_text(strip=True) if tt else '')+'\n'+re.sub(r'\n{2,}','\n',(el or so).get_text('\n',strip=True)))
if __name__=='__main__':
    for u in sys.argv[1:]:
        print('#####',u); print(text(u)[:7000]); time.sleep(1)
