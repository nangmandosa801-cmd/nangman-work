# 전국 입주 단지 잡기: 네이버 블로그 검색에서 「사전점검 · 입주지정기간 · 입주 전세」 글을 모아 단지 이름과 날짜를 뽑는다
import re,html,json,sys,time,urllib.parse,subprocess
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'
def get(q,start=1):
    u='https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q)+f'&start={start}'
    r=subprocess.run(['curl','-s','-m','20','-A',UA,u],capture_output=True)
    t=r.stdout.decode('utf8','ignore')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'</?(mark|b|strong|em|span|i)[^>]*>','',t)
    t=html.unescape(re.sub(r'<[^>]+>','\n',t))
    return [s.strip() for s in t.split('\n') if s.strip()]
MON=[(2026,m) for m in range(10,13)]+[(2027,m) for m in range(1,7)]
Q=[]
for y,m in MON:
    for k in ['사전점검','입주지정기간','입주 시작']:
        Q.append(f'{y}년 {m}월 {k} 아파트')
REG=['서울','경기','인천','부산','대구','광주','대전','울산','세종','강원','충북','충남','전북','전남','경북','경남','제주']
for r in REG: Q+= [f'{r} 사전점검 아파트 2026', f'{r} 입주지정기간 아파트']
NAME=re.compile(r'([가-힣A-Za-z0-9]{2,}(?:\s?[가-힣A-Za-z0-9]+){0,3}?(?:자이|푸르지오|힐스테이트|래미안|e편한세상|이편한세상|아이파크|롯데캐슬|더샵|SK뷰|sk뷰|센트레빌|호반써밋|위브|한신더휴|데시앙|어울림|포레나|자연앤|엘리프|더플래티넘|두산위브|해링턴플레이스|디에이치|아크로|오티에르|르엘|베르디움|시그니처|스카이|파크|센트럴|리버뷰|캐슬)[가-힣A-Za-z0-9]*(?:\s[가-힣0-9]{1,6}(?:단지|차|블록|시그니처|센트럴|리버뷰|파크))?)')
DATE=re.compile(r'(20\d\d)\s*[년.\-/]\s*(\d{1,2})\s*[월.\-/]\s*(\d{1,2})?')
def run(q):
    out=[]
    for st in (1,16):
        for line in get(q,st):
            if not re.search('사전점검|입주지정|입주 시작|입주예정|첫 입주|입주 기간',line): continue
            ns=set(NAME.findall(line))|set(re.findall(r'([가-힣A-Za-z0-9]{3,}(?:\s[가-힣A-Za-z0-9]{2,}){0,2})\s?(?:사전점검|입주지정기간)',line))
            for n in ns:
                ds=['%s-%02d%s'%(a,int(b),('-%02d'%int(c)) if c else '') for a,b,c in DATE.findall(line) if 2026<=int(a)<=2027 and 1<=int(b)<=12]
                out.append({'name':n.strip(),'dates':ds,'line':line[:200],'q':q})
        time.sleep(1.2)
    return out
if __name__=='__main__':
    qs=Q if len(sys.argv)<2 else sys.argv[1:]
    res=[]
    with ThreadPoolExecutor(3) as ex:
        for o in ex.map(run,qs): res+=o
    json.dump(res,open('raw.json','w'),ensure_ascii=False,indent=0)
    print(len(qs),'queries',len(res),'hits')
