import re,sys,urllib.request
from concurrent.futures import ThreadPoolExecutor
exec(open('scan.py').read().split('REG=')[0])
def v(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml',ua='Mozilla/5.0')
    items=re.findall(r'<item>(.*?)</item>',x,re.S)[:2]
    out=[]
    for it in items:
        link=re.search(r'<link>(.*?)</link>',it).group(1)
        no=re.search(r'(\d{9,})',link).group(1)
        d=re.search(r'<pubDate>(.*?)</pubDate>',it).group(1)[5:16]
        t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',it,re.S).group(1)[:45]
        h=get(f'https://m.blog.naver.com/PostView.naver?blogId={b}&logNo={no}')
        imgs=len(set(re.findall(r'(?:postfiles|blogfiles|mblogthumb-phinf)\.pstatic\.net/[^"\'?\s]+',h)))
        body=re.sub(r'<[^>]+>',' ',h)
        ph=sorted(set(re.sub(r'\D','',p) for p in re.findall(r'01[016][-. )]*\d{3,4}[-. ]*\d{4}',body)))
        rep=sorted(set(re.findall(r'1[5-6]\d{2}-\d{4}',body)))
        addr=re.findall(r'(?:서울|경기|인천)[^ ]{0,4} ?[가-힣]{1,4}[시구] [가-힣0-9]{1,8}(?:로|길|동)[ 0-9\-]{0,8}',body)[:2]
        out.append(f'{d} 사진{imgs} ph{ph[:3]} 대표{rep[:2]} 주소{addr} | {t}')
    return b,out
B=sys.argv[1:]
with ThreadPoolExecutor(8) as ex:
    for b,o in ex.map(v,B):
        print('==',b); [print('  ',l) for l in o]
