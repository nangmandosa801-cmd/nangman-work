# 문의 장치 벤치마킹 (2026.10.6 22:22 사용자: 「리서치만 하지 말고 벤치마킹도 해」) — 품목별 검색 첫 화면 블로그 글을 열어 형태를 센다. 남의 글 문장은 옮기지 않고 숫자만 센다.
import subprocess,re,json,time,urllib.parse,sys,os,collections
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1'
def g(u,ref=None,tries=3):
    for _ in range(tries):
        s=subprocess.run(['curl','-sS','-m','25','-A',UA]+(['-H','Referer: '+ref] if ref else [])+[u],capture_output=True).stdout.decode('utf-8','replace')
        if len(s)>300: return s
        time.sleep(1.2)
    return ''
QS={'중문':['중문 가격','중문 시공 후기','3연동 중문 설치','아파트 중문 설치 비용','수원 중문'],
    '샷시':['샷시 교체 비용','샷시 교체 후기','아파트 샷시 교체','살면서 샷시 교체'],
    '필름':['인테리어 필름 시공','싱크대 필름 시공 가격','인테리어필름 업체','현관문 필름 시공'],
    '입주청소':['입주청소 업체','입주청소 가격','입주청소 후기','수원 입주청소'],
    '코킹':['외벽 코킹 비용','창틀 코킹 업체','외부 코킹 업체','창틀 누수'],
    '방묘문':['방묘문 설치','방묘문 제작','방묘문 가격'],
    '문수리':['방문 수리','중문 수리','현관문 수리 업체','문 수리 업체']}
PHONE=r'01[016][-. ]?\d{3,4}[-. ]?\d{4}|0\d{1,2}[-. )]\d{3,4}[-. ]\d{4}|1[5-9]\d{2}[- ]?\d{4}'
def kind(h):
    h=h.lower()
    for k,p in [('톡톡','talk.naver.com'),('예약','booking.naver.com'),('스토어','smartstore.naver.com'),('스토어','brand.naver.com'),('스토어','shopping.naver.com'),('오픈채팅','open.kakao.com'),('카카오채널','pf.kakao.com'),('폼','form.naver.com'),('폼','forms.gle'),('폼','docs.google.com/forms'),
                ('플레이스','place.naver.com'),('플레이스','map.naver.com'),('전화링크','tel:'),('줄임링크','naver.me'),('줄임링크','bit.ly'),('쿠팡','coupang'),('인스타','instagram.com'),('유튜브','youtu'),('내부글','blog.naver.com'),('카페','cafe.naver.com')]:
        if p in h: return k
    return '외부' if h.startswith('http') else ''
def search(q,n=8):
    s=g('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q))
    return list(dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)))[:n]
def post(b,n):
    s=g(f'https://m.blog.naver.com/PostView.naver?blogId={b}&logNo={n}',f'https://m.blog.naver.com/{b}')
    so=BeautifulSoup(s,'html.parser'); cc=so.select_one('.se-main-container')
    if not cc: return None
    bno=(re.findall(r'blogNo["\']?\s*[:=]\s*["\']?(\d+)',s) or [''])[0]
    tt=so.select_one('.se-title-text') or so.select_one('title'); title=tt.get_text(' ',strip=True) if tt else ''
    comps=[c for c in cc.find_all('div',recursive=False) if 'se-component' in (c.get('class') or [])]
    N=len(comps) or 1; seq=[]; dev=[]; chars=0; imgs=0; txt=[]
    for i,c in enumerate(comps):
        cl=' '.join(c.get('class')); m=re.search(r'se-component se-(\w+)',cl); t=m.group(1) if m else '?'
        tx=c.get_text(' ',strip=True).replace('​',''); pos=round(i/N,3)
        if t in('text','table','quotation','sectionTitle'): chars+=len(re.sub(r'\s','',tx)); txt.append((pos,tx))
        if t in('image','imageGroup','imageStrip'): imgs+=len(c.select('img')) or 1
        seq.append(t)
        for a in c.select('a[href]'):
            k=kind(a['href'])
            d=(pos,k,'그림' if t.startswith('image') else ('카드' if t=='oglink' else '글자'),a['href'][:90])
            if k and d not in dev: dev.append(d)
        if t in('placesMap','map'): dev.append((pos,'지도','지도',''))
        if t in('text','table','quotation'):
            for _ in re.findall(PHONE,tx): dev.append((pos,'전화글자','글자',''))
    full=' '.join(x for _,x in txt)
    cta=[(p,w) for p,x in txt for w in re.findall(r'문의|상담|견적|비밀댓글|댓글|톡톡|카톡|전화',x)]
    r=dict(b=b,n=n,bno=bno,title=title,ncomp=N,chars=chars,imgs=imgs,video=seq.count('video'),table=seq.count('table'),head=seq.count('sectionTitle')+seq.count('quotation'),line=seq.count('horizontalLine'),sticker=seq.count('sticker'),
           dev=dev,cta=cta,price=len(re.findall(r'\d[\d,\.]*\s*만\s*원|\d{1,3}(?:,\d{3})+\s*원',full)),
           w={k:len(re.findall(p,full)) for k,p in dict(견적='견적',문의='문의',상담='상담',무료='무료',실측='실측',후기='후기',전후='전후|비포|애프터|before|after|Before|After',AS='A/S|AS|에이에스|하자보수|보증',평='\\d{2}\\s*평',고지='소정의|원고료|수수료|협찬|제공받|광고',내돈='내돈내산|직접 결제|솔직 ?후기',저희='저희|우리 ?업체|시공해 ?드',비밀댓글='비밀 ?댓글',질문='\\?').items()},
           first=full[:160],last=full[-200:],seq=''.join({'text':'t','image':'i','imageGroup':'I','imageStrip':'I','oglink':'L','video':'v','table':'T','placesMap':'M','sticker':'s','quotation':'q','sectionTitle':'h','horizontalLine':'-'}.get(x,'?') for x in seq))
    # 댓글
    if bno:
        u='https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?'+urllib.parse.urlencode(dict(ticket='blog',templateId='default',pool='blogid',lang='ko',country='',objectId=f'{bno}_201_{n}',groupId=bno,pageSize=100,indexSize=10,page=1,initialize='true',useAltSort='true',replyPageSize=10,showReply='true'))
        c=g(u,f'https://m.blog.naver.com/CommentList.naver?blogId={b}&logNo={n}')
        try:
            j=json.loads(c)['result']; L=j.get('commentList') or []
            r['cmt']=dict(total=(j.get('count') or {}).get('total'),top=sum(1 for x in L if x.get('replyLevel')==1),secret=sum(1 for x in L if x.get('secret')),secret_top=sum(1 for x in L if x.get('secret') and x.get('replyLevel')==1),
                          ask=sum(1 for x in L if x.get('replyLevel')==1 and not x.get('secret') and re.search(r'견적|문의|가격|얼마|비용|연락|상담|가능한가|가능할까',x.get('contents') or '')),keys=sorted(L[0].keys())[:0] if L else [])
        except Exception as e: r['cmt']=dict(err=str(e)[:60])
    return r
if __name__=='__main__':
    hits=collections.OrderedDict()
    for it,qs in QS.items():
        for q in qs:
            for rank,(b,n) in enumerate(search(q),1): hits.setdefault((b,n),[]).append((it,q,rank))
            time.sleep(0.7)
    print('글',len(hits),flush=True); json.dump([[b,n,v] for (b,n),v in hits.items()],open('hits.json','w'),ensure_ascii=False)
    res=[]
    def one(k):
        try: r=post(*k)
        except Exception as e: r=None; print('x',k,e,flush=True)
        if r: r['hit']=hits[k]
        return r
    with ThreadPoolExecutor(5) as ex:
        for i,r in enumerate(ex.map(one,list(hits))):
            if r: res.append(r)
            if i%20==0: print('..',i,len(res),flush=True); json.dump(res,open('posts.json','w'),ensure_ascii=False)
    json.dump(res,open('posts.json','w'),ensure_ascii=False); print('끝',len(res),flush=True)
