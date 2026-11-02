import re,sys
BAN=[('갈-','갈[가-힣]'),('견주','견주'),('자리','자리'),('고요','고요'),('프리미엄','프리미엄'),('최고','최고'),('헷갈','헷갈'),('가능성','가능성'),('놓습니다','놓습니다'),('어요','어요'),('예요','예요'),('트렌드','트렌드'),('퀄리티','퀄리티'),('가정','가정'),('기준','기준'),('까닭','까닭'),('차례로','차례로'),('%p','%p'),('7678','7678|9967')]
def scan(t):
    out=[]
    for name,rx in BAN:
        for m in re.finditer(rx,t):
            a=max(0,m.start()-14); out.append((name,t[a:m.end()+14].replace('\n',' ')))
    return out
if __name__=='__main__':
    for l in open(sys.argv[1],encoding='utf8'):
        for n,c in scan(l): print(n,'|',c)
