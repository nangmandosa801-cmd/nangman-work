import re,json,sys,urllib.request,email.utils,datetime
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
def get(u,t=8):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=t) as r: return r.read().decode('utf-8','ignore')
    except Exception: return ''
KW={'보양':'보양','유니폼':'유니폼|단체복|근무복|조끼','이중포장':'이중\s?포장|에어캡|뽁뽁이|완충','정리':'정리\s?정돈|제자리|수납 정리|정리까지','허가':'허가|주선사업|운송사업|국토','보험':'적재물|배상\s?보험|보증보험|책임보험|보험 가입','연수':r'\d{1,2}\s?년\s?(?:차|경력|째|이상)|since|19\d\d년|20[01]\d년|창업|설립','사다리':'사다리','청소':'입주청소|이사청소','보관':'보관'}
def chk(b):
    x=get('https://rss.blog.naver.com/'+b+'.xml')
    items=re.findall(r'<item>(.*?)</item>',x,re.S)
    rows=[]
    for it in items[:40]:
        l=re.search(r'<link>(.*?)</link>',it); d=re.search(r'<pubDate>(.*?)</pubDate>',it); t=re.search(r'<title><!\[CDATA\[(.*?)\]\]>',it,re.S)
        try: dt=email.utils.parsedate_to_datetime(d.group(1)).date().isoformat()
        except Exception: dt=''
        rows.append((dt,t.group(1) if t else '',l.group(1) if l else ''))
    desc=re.search(r'<description><!\[CDATA\[(.*?)\]\]>',x,re.S); desc=desc.group(1) if desc else ''
    agg={k:0 for k in KW}; imgs=[]; sample=[]
    posts=[r for r in rows if re.search('이사|포장|이삿짐',r[1])][:4]
    for dt,t,l in posts:
        m=re.search(r'/(\d{9,})',l)
        if not m: continue
        h=get(f'https://m.blog.naver.com/{b}/{m.group(1)}')
        body=re.sub(r'<[^>]+>',' ',h)
        for k,p in KW.items():
            if re.search(p,body): agg[k]+=1
        im=re.findall(r'(https://mblogthumb-phinf\.pstatic\.net/[^"\'\s?]+)',h)
        im=list(dict.fromkeys(im)); imgs.append(len(im)); sample.append((m.group(1),im[:12]))
        if k=='연수': pass
        yrs=re.findall(r'[^.]{0,25}(?:\d{1,2}\s?년\s?(?:차|경력|째)|19\d\d년|since \d{4})[^.]{0,15}',body)[:2]
        sample[-1]=sample[-1]+(yrs,)
    hk={k:bool(re.search(p,desc)) for k,p in KW.items()}
    return dict(b=b,latest=rows[0][0] if rows else '',n=len(rows),recent=[r[:2] for r in rows[:3]],posts=len(posts),imgs=imgs,kw=agg,desc_kw=[k for k,v in hk.items() if v],desc=desc[:400].replace('\n',' '),sample=sample)
if __name__=='__main__':
    B=sys.argv[1].split(',')
    with ThreadPoolExecutor(6) as ex: R=list(ex.map(chk,B))
    json.dump(R,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
    for r in R:
        print('==',r['b'],r['latest'],'n',r['n'],'imgs',r['imgs'],r['kw'],'desc:',r['desc_kw'])
        print('   ',r['recent'][:3]); print('   ',r['desc'][:250])
        for s in r['sample']:
            if len(s)>2 and s[2]: print('    yrs',s[2])
