# 청약홈 새 공고 받기 (10/5) — rows(kind) · detail(kind,row) → 공고문 글자
import subprocess,re,os,sys,time,datetime,json
UA='Mozilla/5.0'; D='/home/claude/watch/d/'
URL={'rm':'https://www.applyhome.co.kr/ai/aia/selectAPTRemndrLttotPblancListView.do','apt':'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do'}
DET={'rm':'https://www.applyhome.co.kr/ai/aia/selectAPTRemndrLttotPblancDetailView.do','apt':'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do'}
def post(url,data,out,t=50):
    a=['curl','-sS','-m',str(t),'-A',UA,'-o',out]
    for k,v in data.items(): a+=['--data-urlencode',f'{k}={v}']
    for _ in range(3):
        subprocess.run(a+[url],capture_output=True)
        if os.path.exists(out) and os.path.getsize(out)>500: return True
        time.sleep(2)
    return False
def T(x): return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',x)).strip()
def rows(kind):
    now=datetime.date.today(); b=(now.replace(day=1)-datetime.timedelta(days=1)).strftime('%Y%m'); e=now.strftime('%Y%m'); out=[]
    for pg in (1,2):
        f=D+f'_{kind}{pg}.html'; post(URL[kind],{'beginPd':b,'endPd':e,'pageIndex':pg},f); h=open(f,errors='ignore').read(); i=h.find('<tbody')
        for m in re.finditer(r'<tr data-pbno="(\d+)" data-hmno="(\d+)"(?: data-hsecd="(\d+)")? data-honm="([^"]*)"[^>]*>(.*?)</tr>',h[i:],re.S):
            tds=[T(x) for x in re.findall(r'<td[^>]*>(.*?)</td>',m.group(5),re.S)]; ds=re.findall(r'\d{4}-\d{2}-\d{2}',' '.join(tds))
            out.append(dict(kind=kind,pb=m.group(1),hm=m.group(2),hsecd=m.group(3) or '',name=m.group(4).replace('&amp;','&'),region=tds[0],type=tds[1],dates=ds))
    return out
def detail(r):
    slug=r['kind']+r['pb']; f=D+slug+'.html'
    post(DET[r['kind']],{'houseManageNo':r['hm'],'pblancNo':r['pb'],'houseSecd':r.get('hsecd','')},f)
    h=open(f,errors='ignore').read(); m=re.findall(r'href="(https://static\.applyhome\.co\.kr/ai/aia/getAtchmnfl[^"]+)"',h)
    txt=''
    if m:
        p=D+slug+'.pdf'
        if not os.path.exists(p) or os.path.getsize(p)<10000: subprocess.run(['curl','-sS','-m','150','-A',UA,'-o',p,m[0].replace('&amp;','&')])
        subprocess.run(['pdftotext','-layout',p,D+slug+'.txt'],capture_output=True)
        if os.path.exists(D+slug+'.txt'): txt=open(D+slug+'.txt',errors='ignore').read()
    return T(re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S)),txt,D+slug+'.txt'
if __name__=='__main__':
    R=rows('rm')+rows('apt'); json.dump(R,open(D+'rows.json','w'),ensure_ascii=False,indent=0)
    for r in R: print(r['kind'],r['region'],r['type'],r['name'],r['dates'],r['pb'])
