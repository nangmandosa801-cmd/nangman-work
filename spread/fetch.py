import subprocess,json,urllib.parse,sys,html
def page(n):
    u=f"https://blog.naver.com/PostTitleListAsync.naver?blogId=dong_jin_kim&viewdate=&currentPage={n}&categoryNo=&parentCategoryNo=&countPerPage=30"
    o=subprocess.run(['curl','-s','-A','Mozilla/5.0','-e','https://blog.naver.com/dong_jin_kim',u],capture_output=True).stdout.decode('utf-8','replace')
    o=o.replace("\\'","'")
    d=json.loads(o)
    return [dict(logNo=p['logNo'],title=html.unescape(urllib.parse.unquote_plus(p['title'])),date=p.get('addDate','')) for p in d['postList']]
if __name__=='__main__':
    L=page(1); print(json.dumps(L[:12],ensure_ascii=False,indent=0))
import re
def body(logNo):
    u=f"https://blog.naver.com/PostView.naver?blogId=dong_jin_kim&logNo={logNo}&redirect=Dlog&widgetTypeCall=true&directAccess=false"
    o=subprocess.run(['curl','-s','-A','Mozilla/5.0','-e','https://blog.naver.com/dong_jin_kim',u],capture_output=True).stdout.decode('utf-8','replace')
    m=re.search(r'<div class="se-main-container">(.*?)<div class="comment_area|<div class="se-main-container">(.*)',o,re.S)
    h=o[o.find('se-main-container'):]
    ps=[html.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in re.findall(r'<p[^>]*class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>',h,re.S)]
    links=re.findall(r'href="(https://blog\.naver\.com/[a-z_]+/\d+)"',h)
    return [p.replace('​','') for p in ps if p.strip('​ ')],sorted(set(links))
