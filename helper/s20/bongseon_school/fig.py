import sys, json
sys.path.insert(0,'/home/claude/helper/pg')
from fig2d import bars, cards3
S='nangman_bongseon_school_'
J=json.load(open('ana.json'))
def uk(v):
    v=int(round(v)); a,b=divmod(v,10000)
    return f'{a}억' if b==0 else f'{a}억 {b:,}만'
def ch(k): return (J[k]['2026']['med']/J[k]['2021']['med']-1)*100
# 1. 2021년 = 100 으로 본 2026년 84㎡ (봉선동 둘 · 수완 · 첨단 · 효천)
L=[('제일풍경채엘리트파크','봉선 제일풍경채|봉선동 2016',True),('봉선3차한국아델리움','봉선3차 아델리움|봉선동 2014',False),('수완호반베르디움1차','호반베르디움1차|수완 2012',False),('힐스테이트리버파크','힐스테이트리버파크|첨단 2019',False),('효천시티프라디움','효천시티프라디움|효천 2019',False)]
bars('img/'+S+'1_vs2021.png','2021년보다 봉선동 −9%, 효천 −28%',
     [(n,J[k]['2026']['med']/J[k]['2021']['med']*100,f'{ch(k):+.1f}%',h) for k,n,h in L],
     note='2021년 매매 중앙값을 100으로 둔 2026년 1~10월 매매 중앙값 · 전용 84㎡ · 국토교통부 실거래')
# 2. 2026년 새 세입자 전세
L=[('포스코더샵','포스코더샵|봉선동 2004',True),('제일풍경채엘리트파크','봉선 제일풍경채|봉선동 2016',False),('수완호반베르디움1차','호반베르디움1차|수완 2012',False),('힐스테이트리버파크','힐스테이트리버파크|첨단 2019',False),('효천시티프라디움','효천시티프라디움|효천 2019',False)]
bars('img/'+S+'2_jeonse.png','봉선동 2004년 집 전세가 수완보다 1억 4천 높습니다',
     [(n,J[k]['jn26']['med']/10000,uk(J[k]['jn26']['med']),h) for k,n,h in L],
     note='2026년 1~10월 새 세입자 전세 보증금 중앙값 · 전용 84㎡ · 국토교통부 전월세 실거래')
from PIL import Image,ImageDraw,ImageFont
def kr(p,s):
    for i in range(10):
        f=ImageFont.truetype(p,s,index=i)
        if 'KR' in ' '.join(f.getname()): return f
ser_='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; san='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
W=1000; im=Image.new('RGB',(W,W),'#203864'); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,14],fill='#D4B04C'); d.rectangle([0,W-14,W,W],fill='#D4B04C')
d.text((70,95),'낭만 부동산 · 학군지 아파트 16화 · 광주 봉선동',font=kr(san,28),fill='#AFC0D8',anchor='lm')
d.line([70,248,930,248],fill='#3A5A8A',width=3); d.line([70,782,930,782],fill='#3A5A8A',width=3)
d.text((W/2,360),'봉선동 아파트 시세',font=kr(ser_,88),fill='#F4F1EA',anchor='mm')
d.text((W/2,485),'2021년 값 넘은 단지',font=kr(ser_,60),fill='#F4F1EA',anchor='mm')
d.text((W/2,605),'11곳 중 1곳',font=kr(ser_,104),fill='#D4B04C',anchor='mm')
d.text((W/2,715),'제일풍경채 84㎡ 8억 5,000만 · 2021년보다 8.6% 아래 · 2026년 1~10월',font=kr(san,30),fill='#AFC0D8',anchor='mm')
im.save('img/'+S+'thumb.png')
print('fig ok')
