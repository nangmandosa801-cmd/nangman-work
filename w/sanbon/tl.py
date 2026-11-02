import subprocess,json,urllib.parse,re,sys
def tl(b,pages=3):
    out=[]
    for pg in range(1,pages+1):
        u=f'https://blog.naver.com/PostTitleListAsync.naver?blogId={b}&currentPage={pg}&countPerPage=30&categoryNo=0&viewdate=&parentCategoryNo=0'
        r=subprocess.run(['curl','-s',u,'-A','Mozilla/5.0','-e',f'https://blog.naver.com/{b}'],capture_output=True,text=True).stdout
        r=r.replace("\\'","'")
        try: j=json.loads(r)
        except Exception as e: print('fail',b,pg,r[:100]); break
        for p in j['postList']: out.append((p['logNo'],urllib.parse.unquote_plus(p['title']),p['addDate']))
    return out
if __name__=='__main__':
    used=json.load(open('/home/claude/pub/used_cases.json'))
    for b in sys.argv[1:]:
        for n,t,d in tl(b,4):
            if re.search(sys.argv[0] and '군포|산본|금정|당정|궁내|재궁|수리산|대야미|부곡',t):
                print(b,n,d,'USED' if n in used else '',t)
