import sys,re,json,time,urllib.parse
sys.path.insert(0,'/home/claude/blogkit'); import seo
def place(q):
    s=seo._get('https://m.search.naver.com/search.naver?query='+urllib.parse.quote(q))
    tel=list(dict.fromkeys(re.findall(r'tel:([0-9\-]{9,14})',s)))
    addr=list(dict.fromkeys(re.findall(r'"(?:roadAddress|address)":"([^"]{6,60})"',s)))[:3]
    nm=list(dict.fromkeys(re.findall(r'"name":"([^"]{2,30})"',s)))[:4]
    return tel[:3],addr,nm
if __name__=='__main__':
    for q in sys.argv[1:]:
        try: print(q,'|',place(q))
        except Exception as e: print(q,'x',e)
        time.sleep(0.8)
