import re,html,subprocess,urllib.parse,sys
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'
def search(w):
    s=subprocess.run(['curl','-sS','-m','30','-A',UA,'https://m.search.naver.com/search.naver?where=m_kin&query='+urllib.parse.quote(w)+'&nso=so:dd,p:1m'],capture_output=True,text=True).stdout
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    res={}
    for m in re.finditer(r'<a[^>]*href="([^"]*?/docs/(\d+)[^"]*)"[^>]*>(.*?)</a>',s,re.S):
        t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(3)))).strip()
        d=m.group(2); dr=re.search(r'dirs/(\d+)',m.group(1))
        if t and len(t)>6: res.setdefault(d,{'dir':dr.group(1) if dr else '','t':[]})['t'].append(t)
    return res
if __name__=='__main__':
    for w in sys.argv[1:]:
        print('##',w)
        for d,v in search(w).items(): print(d,v['dir'],'|',' || '.join(x[:200] for x in v['t'][:3]))
