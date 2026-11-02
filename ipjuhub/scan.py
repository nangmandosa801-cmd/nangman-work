import subprocess,re,json,concurrent.futures as cf
NAMES=['말끔하게','리담','다원단열','스텔라','stellar','JU인','홈어바웃','몰드케어','moldcare','cleanvip','클린VIP','보일러의모든것','진보일러','대성보일러','뜨끈','모두의보일러','소소리','모던중문','썬중문','크로바','펠리체','인천시흥중문','디자인앤도어','비치움','솜씨종합','청결한사람들','오렌지','드림하우스','줄남청','메가줄눈','아르떼','다정실리콘','플로우홈케어','석천누수','배스코','청년환경','펭귄','진에어','조은클리닝','도하','더빅필름','다온창호','블라썸','펫게이트','이륙통운','포꼼사','토르철거','단디홈케어','홍반장','젊은기술자','가정동열쇠','부산도어락','안전열쇠','게이트맨','설비코리아','경기북부집수리','에코차저']
OUR='champion_chart|dong_jin_kim|jisandream01|give_me_travel|nangman'
def get(u): return subprocess.run(['curl','-s','-m','15','-A','Mozilla/5.0',u],capture_output=True,text=True,errors='ignore').stdout
def chk(u):
    h=get(u)
    m=re.search(r'<div[^>]+(contents_style|tt_article_useless_p_margin|entry-content)[^>]*>(.*)',h,re.S)
    body=m.group(2) if m else h
    body=body.split('another_category')[0]
    t=(re.search(r'<title>([^<]*)',h) or [None,''])[1][:40]
    links=sorted(set(x for x in re.findall(r'blog\.naver\.com/([A-Za-z0-9_\-]+)',body) if not re.match(OUR,x)))
    names=sorted(set(n for n in NAMES if n in body))
    return u,t,links,names
U=[f'https://nangmaninterior.tistory.com/{i}' for i in range(1,55)]+[f'https://talk7921.tistory.com/{i}' for i in range(1,87)]
with cf.ThreadPoolExecutor(8) as ex:
    R=[r for r in ex.map(chk,U) if r[2] or r[3]]
for r in R: print(r[0].replace('https://',''),'|',r[1],'|',r[2][:6],'|',r[3][:8])
json.dump(R,open('scan.json','w'),ensure_ascii=False)
