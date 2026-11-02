# -*- coding: utf-8 -*-
DIV='<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:3px solid #2E5C8A;width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid #C8D2DE;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>'
BR='<p><br></p>'
def P(t): return '<p style="font-size:21px;color:#333;">%s</p>'%t
def H(t): return '<p style="font-size:27px;font-weight:700;color:#1F3864;">%s</p>'%t
def CAP(t): return '<p style="font-size:18px;color:#8A8578;">%s</p>'%t
def FIG(f,d): return '<table width="693" style="width:100%%;min-width:693px;border-collapse:collapse;"><tr><td style="border:1px dashed #C7D6E6;padding:14px;text-align:center;"><span style="font-size:18px;color:#1F3864;">%s — %s</span></td></tr></table>'%(f,d)
TH='padding:13px 8px;font-size:19px;font-weight:700;color:#1F3864;text-align:center;border:1px solid #D8DFE8;'
def td(v,al='right',bold=False,col='#333'):
    return '<td style="padding:11px 8px;font-size:19px;color:%s;%stext-align:%s;border:1px solid #D8DFE8;">%s</td>'%(col,'font-weight:700;' if bold else '',al,v)
def TABLE(head,rows):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;border:1px solid #D8DFE8;">','<tr style="background-color:#F2F4F7;">']
    for h in head: o.append('<td style="%s">%s</td>'%(TH,h))
    o.append('</tr>')
    for r in rows: o.append(r)
    o.append('</table>')
    return '\n'.join(o)
def HL(t): return '<span style="background-color:#FFF3C4;">%s</span>'%t
def B(t): return '<b style="color:#2E5C8A;">%s</b>'%t

O=[]
A=O.append
A('<p style="font-size:17px;color:#2E5C8A;letter-spacing:1px;">낭만 부동산 분석 플랫폼 · 아파트</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#1F3864;">경기도 아파트 실거래, 2022년에 산 사람 77.6%가 손해 보고 팔았습니다</p>')
A(BR)
A(P('경기도 아파트 실거래에서 같은 집이 두 번 팔린 기록만 뽑았습니다. 109만 4,695쌍이 나왔습니다. 같은 단지, 같은 번지, 같은 전용면적, 같은 층입니다. 말 그대로 같은 집이 다시 팔린 경우입니다.'))
A(BR); A(BR)

# 먼저 결론
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F2F4F7;border-left:3px solid #2E5C8A;padding:20px 22px;">')
A('<p style="font-size:23px;font-weight:700;color:#1F3864;">먼저 결론</p>')
A(BR)
A(P('%s · 2022년에 산 사람은 %s. 2021년은 61.3%%, 2020년은 9.2%%였습니다.'%(B('하나'),HL('77.6%가 손해를 보고 팔았습니다'))))
A(BR)
A(P('%s · 손해 본 사람의 중간 손해액은 2021년 매수 8,000만원, 2022년 매수 7,000만원입니다.'%B('둘')))
A(BR)
A(P('%s · 같은 경기도인데 광명이 80.6%%, 이천이 43.7%%입니다. 서울에 가까울수록 손해율이 높았습니다.'%B('셋')))
A(BR)
A(P('%s · 비싼 집일수록 더 많이 잃었습니다. 8~12억이 80.8%%, 3억 미만이 43.4%%입니다.'%B('넷')))
A(BR)
A(P('%s · 4년을 들고 있다가 판 사람도 70.0%%가 손해였습니다. 기다린다고 해결되지 않았습니다.'%B('다섯')))
A('</td></tr></table>')
A(BR); A(BR); A(DIV); A(BR)

# 1
A(H('2020년에 산 사람은 9.2%, 2021년은 61.3%입니다'))
A(BR)
A(P('산 해로만 나눠 봤습니다. 판 시점은 따지지 않았습니다. 사서 6개월 넘게 들고 있다가 판 경우만 셌습니다.'))
A(BR)
A(FIG('nangman_loss_fig1.png','매수 연도별로 손해 보고 판 비율'))
A(BR)
rows=[]
for y,n,r,m in [(2015,'99,418','22.9%','+5.2%'),(2016,'89,183','28.1%','+4.0%'),(2017,'80,904','34.8%','+3.5%'),
                (2018,'85,779','29.6%','+5.8%'),(2019,'67,947','13.1%','+19.3%'),(2020,'102,224','9.2%','+22.2%'),
                (2021,'73,253','61.3%','−6.6%'),(2022,'27,762','77.6%','−13.4%'),(2023,'50,850','34.6%','+3.2%'),
                (2024,'49,121','38.1%','+1.9%'),(2025,'31,236','30.6%','+3.7%')]:
    hot = y in (2021,2022)
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,
        td('%d년'%y,'left',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333'),
        td(m,'right',hot,'#B5654E' if hot else '#333'),
        td(n,'right',hot)))
A(TABLE(['산 해','손해 비율','가격 변화 중간값','쌍'],rows))
A(CAP('국토교통부 실거래가 · 같은 단지 같은 번지 같은 전용면적 같은 층이 두 번 팔린 경우 · 보유 6개월 이상 · 2026년 8월까지'))
A(BR)
A(P('%s 2021년에 산 사람은 61.3%%입니다.'%HL('2020년에 산 사람은 9.2%가 손해였습니다.')))
A(BR)
A(P('1년 차이로 %s가 됐습니다.'%B('여섯 배 이상')))
A(BR)
A(P('그리고 2022년이 77.6%로 더 높습니다. 최악의 해는 2021년이 아니라 2022년이었습니다.'))
A(BR)
A(P('가격 변화 중간값을 보면 더 분명합니다. 2020년에 산 사람은 +22.2%, 2022년에 산 사람은 −13.4%입니다.'))
A(BR)
A(P('2022년 쌍이 2만 7,762개로 다른 해보다 적습니다. 그해에 거래 자체가 적었기 때문입니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 2
A(H('광명 80.6%, 이천 43.7%, 같은 경기도입니다'))
A(BR)
A(P('2021년과 2022년에 산 쌍 10만 1,015개를 시군별로 나눴습니다. 쌍이 500개 넘는 27개 시군입니다.'))
A(BR)
A(FIG('nangman_loss_fig2.png','2021~2022년 매수, 시군별 손해 비율'))
A(BR)
data=[('광명시','1,740','80.6%','−9,000','6.80'),('김포시','3,760','79.3%','−7,700','5.00'),
      ('고양시','7,309','76.0%','−7,000','4.69'),('의정부시','3,805','73.1%','−4,300','3.30'),
      ('남양주시','5,547','72.8%','−5,500','4.48'),('광주시','2,096','72.8%','−4,500','4.19'),
      ('의왕시','982','71.4%','−7,000','6.35'),('용인시','8,999','71.1%','−5,300','6.15'),
      ('하남시','1,868','70.3%','−8,800','9.20'),('안양시','3,411','69.6%','−5,200','6.12'),
      ('구리시','1,112','68.5%','−4,500','6.55'),('양주시','2,077','68.4%','−3,500','2.78'),
      ('화성시','7,986','67.3%','−4,500','5.48'),('수원시','9,323','65.7%','−4,000','5.15'),
      ('성남시','3,559','64.3%','−6,000','10.30'),('파주시','3,775','64.2%','−2,600','3.19'),
      ('군포시','2,206','64.1%','−4,000','4.80'),('오산시','2,375','63.3%','−2,500','3.28'),
      ('시흥시','4,828','62.5%','−3,000','3.40'),('부천시','4,521','61.6%','−2,300','4.55'),
      ('안산시','3,669','57.0%','−1,700','4.00'),('평택시','7,196','52.3%','−500','2.65'),
      ('안성시','2,357','50.0%','0','1.79'),('여주시','1,073','46.0%','+100','1.65'),
      ('포천시','995','43.7%','+200','1.60'),('이천시','2,308','43.7%','+400','1.90')]
rows=[]
for nm,n,r,g,amt in data:
    hot = nm in ('광명시','이천시')
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,
        td(nm,'left',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333'),
        td(g+('만원' if g!='0' else ''),'right',hot),
        td(amt+'억','right',hot)))
A(TABLE(['시군','손해 비율','중간 손해액','산 가격 중간값'],rows))
A(CAP('2021~2022년에 산 쌍 · 쌍 500개 이상인 시군 · 중간 손해액은 손해 본 쌍만 모은 중간값'))
A(BR)
A(P('맨 위가 광명 80.6%%, 맨 아래가 이천 43.7%%입니다. 같은 도 안에서 %s가 납니다.'%B('37%포인트')))
A(BR)
A(P('위쪽은 광명, 김포, 고양, 의정부, 남양주입니다. 서울로 출퇴근하는 동네들입니다.'))
A(BR)
A(P('아래쪽은 이천, 포천, 여주, 안성, 평택입니다. 서울과 멀고, 산 가격 중간값이 1억 6천만원에서 2억 6천만원 사이입니다.'))
A(BR)
A(P('%s 이천에서 산 사람은 손해를 봤어도 중간이 +400만원이었습니다.'%HL('하남에서 산 사람은 손해 보고 팔 때 중간이 8,800만원이었습니다.')))
A(BR)
A(P('많이 오른 동네가 많이 떨어졌습니다. 2021년까지 서울 가까운 곳이 크게 올랐고, 그 값에 산 사람들이 이 표 위쪽에 있습니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 3
A(H('비싼 집을 산 사람이 더 많이 잃었습니다'))
A(BR)
A(P('이번에는 산 가격으로 나눠 봤습니다. 역시 2021년과 2022년에 산 쌍입니다.'))
A(BR)
A(FIG('nangman_loss_fig3.png','2021~2022년 매수 가격대별 손해 비율'))
A(BR)
rows=[]
for nm,n,r,g in [('3억 미만','29,975','43.4%','+400만원'),('3~5억','29,581','69.6%','−4,300만원'),
                 ('5~8억','28,859','79.7%','−8,500만원'),('8~12억','9,719','80.8%','−11,600만원'),
                 ('12억 이상','2,881','70.1%','−11,000만원')]:
    hot = nm in ('3억 미만','8~12억')
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,
        td(nm,'left',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333'),
        td(g,'right',hot),
        td(n,'right',hot)))
A(TABLE(['산 가격','손해 비율','중간 손해액','쌍'],rows))
A(CAP('2021~2022년에 산 쌍 10만 1,015개 · 중간 손해액은 손해 본 쌍만 모은 중간값'))
A(BR)
A(P('3억 미만은 43.4%입니다. 8~12억은 80.8%입니다.'))
A(BR)
A(P('중간 손해액은 %s입니다. 8~12억에 산 사람은 1억 1,600만원입니다.'%B('3억 미만이 +400만원')))
A(BR)
A(P('12억 이상만 70.1%로 조금 낮습니다. 쌍이 2,881개로 적고, 대부분 성남과 과천처럼 이후 다시 오른 동네입니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 4
A(H('4년을 들고 있어도 70.0%였습니다'))
A(BR)
A(P('오래 들고 있으면 달라질까요. 2021년과 2022년에 산 쌍을 보유 기간으로 나눴습니다.'))
A(BR)
rows=[]
for nm,n,r in [('6~12개월','23,665','42.1%'),('1~2년','28,685','75.1%'),('2~3년','22,897','75.7%'),
               ('3~5년','24,177','70.0%')]:
    rows.append('<tr>%s%s%s</tr>'%(td(nm,'left'),td(r,'right',False,'#B5654E'),td(n,'right')))
A(TABLE(['보유 기간','손해 비율','쌍'],rows))
A(CAP('2021~2022년에 산 쌍 · 5년 넘게 들고 있다가 판 쌍은 1,591개뿐이라 뺐습니다'))
A(BR)
A(P('6~12개월 만에 판 사람이 42.1%로 가장 낮습니다. 이 사람들은 대부분 2022년 상반기에 팔았습니다. 아직 가격이 남아 있을 때입니다.'))
A(BR)
A(P('1~2년은 75.1%, 2~3년은 75.7%입니다. 2023년과 2024년에 팔린 것들입니다.'))
A(BR)
A(P('%s 4년을 기다린 사람도 열 명 중 일곱이 손해였습니다.'%HL('3~5년이 70.0%입니다.')))
A(BR)
A(P('판 해로 나눠 보면 2023년에 판 사람이 79.8%로 가장 높고, 2026년에 판 사람이 64.9%입니다. 조금씩 낮아지고는 있습니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 자료의 한계
A(H('판 사람만 세어진 숫자입니다'))
A(BR)
A(P('이 숫자는 %s입니다. 2021년에 사서 아직 들고 있는 사람은 여기 없습니다.'%B('사고 나서 실제로 판 사람만')))
A(BR)
A(P('손해를 보게 된 사람 중에는 팔지 않고 버티는 쪽이 많습니다. 그래서 실제로 손해 상태인 집의 비율과는 다릅니다. 이 표는 「팔았을 때 어땠나」를 보여 줍니다.'))
A(BR)
A(P('세금과 중개수수료, 이사비는 넣지 않았습니다. 산 가격과 판 가격만 비교했습니다. 실제로 손에 쥔 돈은 이보다 적습니다.'))
A(BR)
A(P('취소된 거래는 국토교통부 자료에서 이미 빠져 있습니다. 다만 같은 층 같은 면적이라도 동이 다르면 다른 집인데, 번지까지 같으면 같은 단지로 봤습니다. 대단지에서는 서로 다른 동의 같은 층이 섞일 수 있습니다.'))
A(BR)
A(P('보유 6개월 미만은 뺐습니다. 분양권 전매나 같은 집이 짧게 두 번 도는 경우를 걸러 내기 위해서입니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 정리
A(H('정리'))
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F2F4F7;border-left:3px solid #2E5C8A;padding:20px 22px;">')
A(P('%s · 같은 집이 두 번 팔린 109만 4,695쌍에서, 2022년에 산 사람은 77.6%%, 2021년은 61.3%%, 2020년은 9.2%%가 손해였습니다.'%B('하나')))
A(BR)
A(P('%s · 손해 본 사람의 중간 손해액은 2021년 매수 8,000만원, 2022년 매수 7,000만원입니다.'%B('둘')))
A(BR)
A(P('%s · 광명 80.6%%, 김포 79.3%%, 고양 76.0%%입니다. 이천 43.7%%, 포천 43.7%%, 여주 46.0%%입니다.'%B('셋')))
A(BR)
A(P('%s · 8~12억에 산 사람이 80.8%%로 가장 높고, 3억 미만이 43.4%%로 가장 낮습니다.'%B('넷')))
A(BR)
A(P('%s · 3~5년을 들고 있다가 판 사람도 70.0%%가 손해였습니다.'%B('다섯')))
A('</td></tr></table>')
A(BR); A(BR); A(DIV); A(BR)

# 꼬리
A(H('함께 보면 좋은 글'))
A(BR)
def LK(u,t,d):
    return '<p style="font-size:19px;font-weight:700;"><a href="%s" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">%s</a><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(u,t,d)
def SOON(t,d):
    return '<p style="font-size:19px;font-weight:700;"><span style="color:#2E5C8A;border-bottom:1px solid #C7D6E6;">%s</span> <span style="font-size:16px;color:#B5654E;">(발행 예정)</span><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(t,d)
tail=[
 LK('https://blog.naver.com/jisandream01/224409047755','별내자이 더 스타 이그제큐티브 | 주차가 실당 1.3대입니다','별내역 앞 760실 · 샘플하우스 열려 있습니다'),
 LK('https://blog.naver.com/jisandream01/224402027023','별내자이 더 스타 분양가 | 255개 호실 중 6.09억이 가장 낮습니다','호실별 분양가를 면적군으로 정리했습니다'),
 LK('https://blog.naver.com/dong_jin_kim/224401854235','경기도 아파트 시세 지도 | 31개 시군 84㎡ 가격을 한 줄로 세웠습니다','지금 가격이 어디쯤인지 한눈에 봅니다'),
 LK('https://blog.naver.com/dong_jin_kim/224401277281','서울 아파트 수익률 | 2017년 도봉구가 2021년 강남구보다 나았습니다','서울에서도 산 해가 결과를 갈랐습니다'),
 LK('https://blog.naver.com/dong_jin_kim/224401817897','경기도 전세가율 | 31개 시군 갭투자 필요 금액을 세웠습니다','지금 사려면 얼마가 드는지 봅니다'),
 LK('https://blog.naver.com/dong_jin_kim/224397832357','오를까요 내릴까요 | 예측을 그만두기로 했습니다','이 블로그가 숫자만 세는 이유입니다'),
 SOON('화성 아파트 시세, 거래 45%가 동탄2인데 회복률은 꼴찌입니다','손해가 몰린 동네를 한 시군 안에서 봅니다'),
 SOON('양주 아파트 시세, GTX-C 오는 덕정동이 2021년보다 28.9% 낮습니다','아직 2021년 가격을 못 넘은 동네입니다'),
]
for i,t in enumerate(tail):
    A(t)
    A(BR)
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
A('<tr><td style="background-color:#F2F4F7;border-left:3px solid #2E5C8A;padding:16px 18px;">')
A('<span style="font-size:16px;color:#8A8578;">태그</span><br>')
A('<span style="font-size:18px;color:#555;line-height:1.9;">#경기도아파트실거래 #경기도아파트시세 #아파트손해 #실거래가분석 #광명아파트 #김포아파트 #고양아파트 #하남아파트 #부동산데이터 #낭만부동산</span>')
A('</td></tr></table>')

open('/mnt/user-data/outputs/재배치/nangman/loss/nangman_loss_post.html','w',encoding='utf-8').write('\n'.join(O)+'\n')
import re
x='\n'.join(O)
print('bytes',len(x.encode()))
print('본문 글자수', len(re.sub(r'<[^>]+>','',x).replace('\n','')))
