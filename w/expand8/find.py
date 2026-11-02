import sys,re,json,time,urllib.parse,collections
sys.path.insert(0,'/home/claude/blogkit'); import seo
REG=['서울','강남','송파','노원','수원','용인','성남','화성','동탄','인천','부천','고양','남양주','하남','김포','평택','안양','의정부']
CAT={'hood':['주방후드 교체','렌지후드 교체'],'aircon2':['벽걸이 에어컨 설치','에어컨 이전설치']}
out={}
for c,ks in CAT.items():
    hits=collections.defaultdict(list)
    regs=REG
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
