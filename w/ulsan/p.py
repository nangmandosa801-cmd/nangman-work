import re,urllib.request,json,html,sys
from concurrent.futures import ThreadPoolExecutor
ids=sys.argv[1:]
H={'User-Agent':'Mozilla/5.0','Referer':'https://blog.naver.com/'}
def get(u):
  return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf8','ignore')
def one(b):
  try:
    x=get(f'https://rss.blog.naver.com/{b}.xml')
  except Exception as e: return b,{'err':str(e)}
  name=html.unescape((re.findall(r'<title><!\[CDATA\[(.*?)\]\]>',x) or re.findall(r'<title>(.*?)</title>',x) or [''])[0])
  items=re.findall(r'<item>(.*?)</item>',x,re.S)
  ts=[];phones={};dates=[]
  for it in items[:20]:
    t=html.unescape((re.findall(r'<title><!\[CDATA\[(.*?)\]\]>',it) or re.findall(r'<title>(.*?)</title>',it) or [''])[0])
    d=(re.findall(r'<pubDate>(.*?)</pubDate>',it) or [''])[0][5:16]
    ts.append(d+' '+t[:60])
    for p in re.findall(r'0\d{1,2}[-. ]?\d{3,4}[-. ]?\d{4}|1[5-6]\d\d[-. ]?\d{4}',it):
      p=re.sub(r'[ .]','-',p); phones[p]=phones.get(p,0)+1
  return b,{'name':name,'n':len(items),'phones':phones,'titles':ts[:8]}
with ThreadPoolExecutor(8) as ex:
  for b,r in ex.map(one,ids):
    print('==',b,r.get('name',''),r.get('err',''),'| 글',r.get('n'),'| 번호',r.get('phones'))
    for t in r.get('titles',[]): print('   ',t)
