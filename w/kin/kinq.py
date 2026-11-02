# 지식인 질문 찾기 — python3 kinq.py <기간 1w|1m|all> <검색어…> → 제목 · 날짜 · 답변수 · 주소
import sys,re,html,subprocess,urllib.parse,json
def cl(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',x))).strip()
def search(q,period='1w',page=1):
    u='https://kin.naver.com/search/list.naver?query='+urllib.parse.quote(q)+'&sort=date&section=qna&page=%d'%page+('' if period=='all' else '&period='+period)
    s=subprocess.run(['curl','-sS','-m','25','-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf-8','replace')
    out=[]
    for li in re.findall(r'<li data-nlog-imp-params=.*?</li>',s,re.S):
        m=re.search(r'<a href="(https://kin\.naver\.com/qna/detail\.naver\?[^"]+)"[^>]*>(.*?)</a>',li,re.S)
        if not m: continue
        d=re.search(r'<dd class="txt_inline">(.*?)</dd>\s*<dd>(.*?)</dd>',li,re.S); n=re.search(r'답변수 (\d+)',li); c=re.findall(r'class="txt_g1 _nclicks:qna\.cat\d">(.*?)</a>',li)
        out.append(dict(url=html.unescape(m.group(1)),title=cl(m.group(2)),date=cl(d.group(1)) if d else '',body=cl(d.group(2)) if d else '',ans=int(n.group(1)) if n else 0,cat=cl(c[-1]) if c else ''))
    return out
if __name__=='__main__':
    seen={}
    for q in sys.argv[2:]:
        for r in search(q,sys.argv[1]):
            k=re.search(r'docId=(\d+)',r['url']).group(1)
            if k in seen: continue
            seen[k]=r; print(f"[{q}] {r['date']} 답{r['ans']} {r['cat']} | {r['title']}\n    {r['body'][:150]}\n    docId={k} dirId={re.search(r'dirId=(\d+)',r['url']).group(1)}")
    json.dump(seen,open('last.json','w'),ensure_ascii=False)
