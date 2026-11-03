import re,sys
from fetch import body
BAN=['자리','갈라','갈렸','갈랐','엇갈','어요','예요','고요','최고','프리미엄','가능성','헷갈','놓습니다','가정','까닭','견줘','%p','나갈','1위']
def sents(t): return [s.strip() for s in re.split(r'(?<=[.?!다])\s+',re.sub(r'<[^>]+>',' ',t)) if len(s.strip())>=12]
def check(text,logNo):
    ps,_=body(logNo); src=set(); 
    for p in ps: src|=set(s.replace(' ','') for s in sents(p))
    bad=[w for w in BAN if w in text]
    ov=[s for s in sents(text) if s.replace(' ','') in src]
    return bad,ov
if __name__=='__main__':
    t=open(sys.argv[1]).read(); b,o=check(t,sys.argv[2]); print('금지어',b); print('겹침',len(o)); [print(' ',x) for x in o]
