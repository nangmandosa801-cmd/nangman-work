import subprocess,time,re,sys,urllib.parse,html
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
def get(u,tries=6,data=None):
    for i in range(tries):
        cmd=['curl','-sS','-A',UA,'-m','60','-L',u]
        if data: cmd+=['-X','POST','-d',data,'-H','Referer: https://www.law.go.kr/']
        r=subprocess.run(cmd,capture_output=True)
        if r.returncode==0 and len(r.stdout)>500: return r.stdout.decode('utf-8','ignore')
        time.sleep(8)
    return ''
def seq(name):
    s=get('https://www.law.go.kr/%EB%B2%95%EB%A0%B9/'+urllib.parse.quote(name))
    m=re.search(r'lsiSeq=(\d+)&amp;chrClsCd=\d+&amp;urlMode=lsInfoP&amp;efYd=(\d+)',s)
    return m.groups() if m else None
def body(name):
    sq=seq(name); print(name,sq,file=sys.stderr)
    if not sq: return ''
    s=get(f'https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq={sq[0]}&chrClsCd=010202&urlMode=lsInfoP&efYd={sq[1]}&ancYnChk=0',data=f'lsiSeq={sq[0]}&chrClsCd=010202&efYd={sq[1]}&ancYnChk=0')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>','\n',t)); t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
    for n in sys.argv[1:]:
        t=body(n); open(n+'.txt','w').write(t); print(n,len(t))
