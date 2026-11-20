import json,re,subprocess,urllib.parse,time
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
def ac(q):
    e=urllib.parse.quote(q)
    s=subprocess.run(['curl','-s','--max-time','8','-A','Mozilla/5.0',f'https://ac.search.naver.com/nx/ac?q={e}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'],capture_output=True,text=True).stdout
    try: return [x[0] for x in json.loads(s)['items'][0]][:10]
    except Exception: return []
def rank(kw):
    u='https://m.search.naver.com/search.naver?where=m_blog&query='+urllib.parse.quote(kw)
    s=subprocess.run(['curl','-s','-m','20','-A',UA,u],capture_output=True,text=True).stdout
    ids=[]
    for m in re.finditer(r'blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d{9,})',s):
        if m.group(1) not in ids and m.group(1) not in ('PostView','PostList'): ids.append(m.group(1))
    r=lambda b: ids.index(b)+1 if b in ids else 0
    return r('dong_jin_kim'),r('jisandream01'),ids[:3]
seeds=['하남 집값','하남 아파트','하남 전세','미사 집값','미사 아파트','미사 전세','감일 집값','감일 아파트','위례 집값','하남 교산','교산신도시','하남 3호선','하남 9호선','하남 재건축','하남 분양','하남 입주']
kws=[]
for s in seeds:
    for k in ac(s):
        if k not in kws and ('하남' in k or '미사' in k or '감일' in k or '위례' in k or '교산' in k): kws.append(k)
    time.sleep(0.2)
kws=kws[:60]
out=[]
for k in kws:
    a,b,top=rank(k); out.append({'kw':k,'dj':a,'js':b,'top':top}); time.sleep(0.5)
json.dump(out,open('hanam.json','w'),ensure_ascii=False)
t3=sum(1 for o in out if 0<o['dj']<=3); t10=sum(1 for o in out if 0<o['dj']<=10)
print('하남 자동완성',len(out),'| 낭만 3위 안',t3,'| 10위 안',t10,'| 안 보임',sum(1 for o in out if o['dj']==0))
import collections
c=collections.Counter(i for o in out for i in o['top'] if i not in('dong_jin_kim','jisandream01'))
print('상위3 단골',c.most_common(10))
for o in out: print(o['dj'],o['js'],o['kw'],o['top'])
