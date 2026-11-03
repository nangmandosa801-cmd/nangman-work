# 새 원고와 발행 글이 얼마나 겹치는지 — 문장 단위 같은 문장 수 + 25자 조각 겹침 비율
import re,html,sys,os,subprocess
C='/home/claude/jisan/master/cache/'
def fetch(n):
    p=C+n+'.txt'
    if not os.path.exists(p):
        s=subprocess.run(['curl','-s',f'https://m.blog.naver.com/PostView.naver?blogId=jisandream01&logNo={n}','-H','User-Agent: Mozilla/5.0'],capture_output=True,text=True).stdout
        s=s[s.find('se-main-container'):]; s=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S)
        t=html.unescape(re.sub('<[^>]+>','\n',s)); open(p,'w').write(t)
    return open(p).read()
def clean(t):
    t=re.sub(r'\s+',' ',t); return t
def sents(t): return set(x.strip() for x in re.split(r'(?<=[다요])\.\s|\n',t) if len(x.strip())>=15)
def shingles(t,k=25):
    t=re.sub(r'\s+','',t); return set(t[i:i+k] for i in range(0,max(0,len(t)-k),5))
def plain_post(path):
    s=open(path).read(); return html.unescape(re.sub('<[^>]+>','\n',s))
if __name__=='__main__':
    new=plain_post(sys.argv[1]); ns=sents(new); nsh=shingles(new)
    for n in sys.argv[2:]:
        o=fetch(n); os_=sents(o); osh=shingles(o)
        same=ns&os_; r=len(nsh&osh)/max(1,len(nsh))
        print(f'{n}  같은 문장 {len(same)}개 · 조각 겹침 {r:.0%}')
