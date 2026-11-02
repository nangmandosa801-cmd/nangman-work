import json,re,sys,copy
from bs4 import BeautifulSoup,NavigableString
D=json.load(open('/home/claude/watch/rank/helper_v2_data.json'))
IDX=range(17,25)
def txt(e): return re.sub(r'\s+',' ',e.get_text(' ',strip=True)).strip()
log=[]
def process(i):
    x=D[i-1]; kw=x['kw']
    root=BeautifulSoup('<div>'+x['body']+'</div>','html.parser').div
    ch=[c for c in root.children if getattr(c,'name',None)]
    n=x['n']
    # 1 tag lines / disclaimers / 옆 블로그 / 안전장치 / brand box
    for k,c in enumerate(ch):
        t=txt(c)
        if c.name=='p' and t.startswith('#') and t.count('#')>=3:
            c.decompose(); log.append((i,'태그 줄',t[:30])); continue
        if t.startswith('※ 본 글은'):
            c.decompose(); log.append((i,'※ 안내',t[:30])); continue
        if t.startswith('안전장치 —'):
            for sp in c.find_all('span'):
                for st in list(sp.strings):
                    new=re.sub(r'본 글은 자평진전·연해자평·삼명통회(·궁통보감)?(·적천수)? 등 사주 고전 정설에 근거합니다\. ','',str(st))
                    new=new.replace('자평진전·연해자평·삼명통회 등 사주 고전 정설에 근거하며, 정확한 풀이는','정확한 풀이는')
                    if new!=str(st): st.replace_with(NavigableString(new)); log.append((i,'안전장치 겹치는 문장 뺌',''))
            continue
        if t.startswith('CONCLUSION'):
            trs=c.find_all('tr')
            last=txt(trs[-1]) if trs else ''
            m=re.search(r'^(.*?)\s*(낭만도사 · \S.*)$',last)
            body_line,foot=(m.group(1),m.group(2)) if m else (last,'')
            body_line=body_line.replace('사주는 경향성이지 운명이 아닙니다.','').strip()
            log.append((i,'반복 안내 문장(맺음 줄)','경향성'))
            sp=lambda s,ex='':BeautifulSoup('<p style="text-align:left;"><span style="color:#3b332c;font-size:19px">'+s+'</span></p>','html.parser').p
            repl=[]
            if body_line: repl.append(sp(body_line))
            if foot:
                f=BeautifulSoup('<p style="text-align:center;"><span style="color:#5c1b2a;font-size:19px"><b>'+foot+'</b></span></p>','html.parser').p
                repl.append(f)
            for e in repl: c.insert_before(e)
            c.decompose(); log.append((i,'CONCLUSION 반복 요약 뺌(맺음 줄 남김)',t[:30])); continue
        if t.startswith('오늘 가져갈 것'):
            if c.name=='p':
                nxt=c.find_next_sibling(lambda e:getattr(e,'name',None))
                if nxt is not None and nxt.name=='table': nxt.decompose()
            c.decompose(); log.append((i,'오늘 가져갈 것',t[:30])); continue
        if i==19 and t.startswith('갈매동 원룸 투자'):
            c.decompose(); log.append((i,'옆 블로그(지산드림) 링크',t[:30])); continue
        if t.startswith('NANGMAN DOSA'):
            c.decompose(); log.append((i,'소개 상자',t[:30])); continue
        if t.startswith('응급실 운영 중'):
            # 직전의 URL-only p 도 같이
            prev=c.find_previous_sibling(lambda e:getattr(e,'name',None))
            if prev is not None and txt(prev).startswith('https://blog.naver.com/give_me_travel/224248088697'):
                prev.decompose()
            c.decompose(); log.append((i,'옆 블로그 상자',t[:30])); continue
    # 2 footer
    for p in root.find_all('p'):
        for s in p.find_all(string=re.compile('浪漫道士')):
            s.replace_with(NavigableString('낭만도사 · '+kw)) if txt(p)=='낭만도사 · 浪漫道士' else s.replace_with(NavigableString(str(s).replace('浪漫道士',kw)))
    # 3 repeated sentence
    for sp in root.find_all('span'):
        if txt(sp)=='사주는 경향성이지 운명이 아닙니다.':
            par=sp.parent
            sp.decompose(); log.append((i,'반복 안내 문장','경향성'))
            if par.name=='p' and not txt(par): par.decompose()
    for p in root.find_all('p'):
        if txt(p)=='사주는 경향성이지 운명이 아닙니다.': p.decompose(); log.append((i,'반복 안내 문장 p','경향성'))
    return root
if __name__=='__main__':
    out={}
    for i in IDX:
        r=process(i); out[i]=str(r)[len('<div>'):-len('</div>')]
    json.dump(out,open('/home/claude/watch/rank/day3/stage1.json','w'),ensure_ascii=False)
    for l in log: print(l)
