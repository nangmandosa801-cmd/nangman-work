import requests,re,html,json,time,sys
def fetch(no):
    for k in range(4):
        r=requests.get('https://blog.naver.com/PostView.naver',params=dict(blogId='dong_jin_kim',logNo=no),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124'})
        if 'se-main-container' in r.text: return r.text
        time.sleep(15)
    return ''
def paras(t):
    i=t.find('se-main-container'); t=t[i:]
    j=t.find('post_footer'); t=t[:j] if j>0 else t
    out=[]
    for m in re.finditer(r'<p class="se-text-paragraph[^>]*>(.*?)</p>',t,re.S):
        inner=m.group(1)
        txt=html.unescape(re.sub(r'<[^>]+>','',inner)).replace('​','').strip()
        lk=re.findall(r'href="https://blog\.naver\.com/dong_jin_kim/(\d{12})"',inner)
        col=re.findall(r'color:(#[0-9a-fA-F]{6})',inner)
        big='fs2' in inner or 'fs24' in inner or 'fs22' in inner
        fs=re.findall(r'se-fs-fs(\d+)',inner)
        out.append(dict(t=txt,l=lk,c=col[0].lower() if col else '',fs=fs[0] if fs else ''))
    return out
if __name__=='__main__':
    no=sys.argv[1]; P=paras(fetch(no))
    k=max([i for i,p in enumerate(P) if '함께 보면' in p['t']] or [len(P)-40])
    for p in P[max(0,k-15):]:
        if p['t'] or p['l']: print(p['fs'],p['c'],p['l'],p['t'][:60])
