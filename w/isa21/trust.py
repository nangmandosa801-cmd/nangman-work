import re,sys,urllib.request
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=8).read().decode('utf-8','ignore')
    except Exception: return ''
P=r'허가|주선|적재물|배상|보험|\d{1,2}\s?년\s?(?:차|경력|째|이상|동안)|19\d\d년|20[012]\d년\s?(?:창업|설립|부터)|사업자|유니폼|단체복|입주청소|정리수납|정리 ?서비스'
def run(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml')
    nos=re.findall(r'blog\.naver\.com/'+re.escape(b)+r'/(\d{9,})',x)[:8]
    hits={}
    for no in nos:
        h=get(f'https://m.blog.naver.com/{b}/{no}')
        m=re.search(r'<div class="se-main-container">(.*?)<div class="(?:post_footer|comment)',h,re.S)
        body=re.sub(r'<[^>]+>',' ',m.group(1) if m else h); body=re.sub(r'\s+',' ',body)
        for s in re.findall(r'[^.!?]{0,40}(?:'+P+r')[^.!?]{0,40}',body):
            s=s.strip()
            if s and s not in hits: hits[s]=no
    return b,list(hits.items())[:14]
B=sys.argv[1].split(',')
with ThreadPoolExecutor(6) as ex:
    for b,h in ex.map(run,B):
        print('##',b)
        for s,no in h: print('   ',no,s[:120])
