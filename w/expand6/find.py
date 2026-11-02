import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['서울','강남','송파','노원','수원','용인','성남','화성','동탄','인천','부천','고양','남양주','하남','김포','평택','안양','의정부']
CAT={'aircon':['시스템에어컨 설치','시스템에어컨 신축 아파트','시스템에어컨 설치비용'],
     'move':['포장이사','이사업체 후기'],
     'curtain':['커튼 블라인드 시공','블라인드 설치 아파트'],
     'office':['사무실 인테리어','사무실 칸막이 공사','상가 인테리어','지식산업센터 인테리어','간판 제작']}
out={}
for c,ks in CAT.items():
    hits=collections.defaultdict(list)
    regs=REG if c!='office' else ['서울','강남','성수','구로','가산','금천','송파','문정','수원','화성','동탄','용인','성남','하남','인천','부천','고양','안양']
    for r in regs:
        for k in ks[:2] if c!='office' else ks[:3]:
            q=r+' '+k
            s=seo._get('https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&where=m_blog&sm=mtb_jum&query='+urllib.parse.quote(q)) or ''
            for b,n in dict.fromkeys(re.findall(r'https://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s)): hits[b].append(q)
            time.sleep(0.8)
    out[c]=hits
    top=sorted(hits.items(),key=lambda x:-len(set(x[1])))[:25]
    print('==',c,len(hits)); 
    for b,v in top: print(' ',b,len(set(v)),'|',' · '.join(sorted(set(v)))[:90])
json.dump(out,open('hits.json','w'),ensure_ascii=False)
