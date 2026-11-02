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
    o.append('</tr>'); o+=rows; o.append('</table>')
    return '\n'.join(o)
def HL(t): return '<span style="background-color:#FFF3C4;">%s</span>'%t
def B(t): return '<b style="color:#2E5C8A;">%s</b>'%t
def BOX(inner): return '<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F2F4F7;border-left:3px solid #2E5C8A;padding:20px 22px;">\n'+inner+'\n</td></tr></table>'

O=[];A=O.append
A('<p style="font-size:17px;color:#2E5C8A;letter-spacing:1px;">낭만 부동산 분석 플랫폼 · 경기 토지</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#1F3864;">그린벨트 토지 투자 2편, 지분 거래가 5.9%에서 65%로 늘었습니다</p>')
A(BR)
A(P('1편에서 같은 그린벨트라도 대지가 산의 6배라는 걸 셌습니다. 팔리는 건 대개 산이었고 열 평도 안 되는 조각이 28%였습니다.'))
A(BR)
A(P('그럼 그 조각들은 언제부터, 어디에 몰렸을까요. 경기도 토지 실거래 213만 건에서 용도지역이 개발제한구역인 16만 96건을 따로 뽑았습니다. 2010년 1월부터 2026년 8월까지입니다.'))
A(BR); A(BR)

inner=[]
inner.append('<p style="font-size:23px;font-weight:700;color:#1F3864;">먼저 결론</p>'); inner.append(BR)
inner.append(P('%s · 경기 그린벨트 지분 거래 비율은 2010년 5.9%%%%에서 %s. 2019년에 79.2%%%%로 정점을 찍었습니다.'%(B('하나'),HL('2026년 66.8%가 됐습니다'))))
inner.append(BR)
inner.append(P('%s · 최근 3년만 보면 개발제한구역이 65.4%%%%입니다. 같은 기간 경기 토지 전체는 48.7%%%%입니다.'%B('둘')))
inner.append(BR)
inner.append(P('%s · 성남 85%%%%, 광명 83%%%%, 과천 83%%%%, 하남 79%%%%입니다. 서울에 붙은 도시가 위에 있습니다.'%B('셋')))
inner.append(BR)
inner.append(P('%s · 성남 금토동은 2019년 한 해에만 1,721건이 거래됐고 그중 98%%%%가 지분이었습니다. 그해 평당 23만 9천원이었습니다.'%B('넷')))
inner.append(BR)
inner.append(P('%s · 거리만으로는 설명되지 않습니다. 용인이 31km에서 63.7%%%%, 평택이 58km에서 54.5%%%%, 이천이 40km에서 34.4%%%%입니다.'%B('다섯')))
A(BOX('\n'.join(inner)))
A(BR); A(BR); A(DIV); A(BR)

# 1
A(H('2010년에는 스무 건에 한 건이었습니다'))
A(BR)
A(P('지분 거래는 필지 하나를 통째로 사는 게 아니라 그 땅의 몇 분의 몇을 사는 거래입니다. 신고서에 지분으로 표시됩니다.'))
A(BR)
A(P('계약 연도별로 그 비율을 셌습니다.'))
A(BR)
A(FIG('nangman_land2_fig1.png','경기 개발제한구역과 토지 전체의 연도별 지분 거래 비율'))
A(BR)
rows=[]
for y,n,gb,al in [(2010,'4,042','5.9%','24.5%'),(2013,'6,426','35.7%','31.7%'),(2016,'15,101','63.3%','41.9%'),
                  (2018,'15,416','72.6%','49.7%'),(2019,'17,514','79.2%','53.2%'),(2021,'10,407','47.2%','43.6%'),
                  (2023,'5,770','59.0%','48.6%'),(2024,'4,793','69.2%','47.5%'),(2026,'4,019','66.8%','51.4%')]:
    hot = y in (2010,2019)
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,td('%d년'%y,'left',hot),
        td(gb,'right',hot,'#B5654E' if hot else '#333'),td(al,'right',hot),td(n,'right',hot)))
A(TABLE(['계약 연도','개발제한구역','토지 전체','개발제한구역 거래'],rows))
A(CAP('국토교통부 실거래가 · 경기도 토지 · 2026년은 8월까지'))
A(BR)
A(P('%s 2019년에 79.2%%%%까지 올랐습니다.'%HL('2010년에는 5.9%였습니다.')))
A(BR)
A(P('같은 기간 경기 토지 전체는 24.5%%%%에서 53.2%%%%로 올랐습니다. %s'%B('개발제한구역이 훨씬 가파릅니다.')))
A(BR)
A(P('2021년에 47.2%로 한 번 꺾입니다. 그해 개발제한구역 거래 자체가 1만 407건으로 전년의 6할로 줄었습니다. 2020년 2월부터 수도권 주요 지역이 토지거래허가구역으로 묶였고, 2021년 3월에 LH 직원 땅 투기가 드러나면서 단속이 붙은 시기입니다.'))
A(BR)
A(P('그리고 2024년에 69.2%%로 다시 올라옵니다. 지금은 %s입니다.'%B('셋 중 둘이 지분 거래')))
A(BR); A(BR); A(DIV); A(BR)

# 2
A(H('성남 85%, 광명 83%, 과천 83%입니다'))
A(BR)
A(P('최근 3년만 따로 봤습니다. 2024년 1월부터 2026년 8월까지 개발제한구역 거래 1만 4,778건입니다. 이 기간 지분 비율은 65.4%이고, 같은 기간 경기 토지 전체는 48.7%입니다.'))
A(BR)
A(FIG('nangman_land2_fig2.png','경기 시군별 개발제한구역 지분 거래 비율'))
A(BR)
rows=[]
for nm,n,r,p in [('성남시','915','85%','150만원'),('광명시','299','83%','148만원'),('과천시','546','83%','20만원'),
                 ('수원시','630','82%','49만원'),('하남시','2,180','79%','136만원'),('부천시','299','78%','113만원'),
                 ('화성시','1,460','71%','67만원'),('의왕시','429','68%','87만원'),('의정부시','304','61%','115만원'),
                 ('남양주시','2,748','59%','97만원'),('고양시','1,172','55%','130만원'),('김포시','294','53%','105만원'),
                 ('안산시','703','48%','83만원'),('시흥시','1,444','48%','83만원'),('양주시','302','41%','56만원'),
                 ('광주시','380','39%','38만원')]:
    hot = nm in ('성남시','광주시')
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,td(nm,'left',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333'),td(p,'right',hot),td(n,'right',hot)))
A(TABLE(['시군','지분 거래','평당가','거래'],rows))
A(CAP('용도지역이 개발제한구역인 토지 · 2024년 1월~2026년 8월 · 거래 200건 이상 시군 · 평당가는 중간값, 지분 거래는 지분 면적 기준'))
A(BR)
A(P('맨 위가 성남 85%, 맨 아래가 광주 39%입니다.'))
A(BR)
A(P('성남, 광명, 과천, 하남은 서울과 맞닿아 있습니다. 광주, 양주, 시흥, 안산은 한 겹 바깥입니다.'))
A(BR)
A(P('다만 %s 과천은 평당 20만원인데 83%%이고, 고양은 평당 130만원인데 55%%입니다.'%B('평당가와는 따로 움직입니다.')))
A(BR); A(BR); A(DIV); A(BR)

# 3
A(H('동으로 내려가면 90%를 넘습니다'))
A(BR)
A(P('시군은 넓습니다. 읍면동 단위로 내려가 봤습니다. 거래 30건 이상인 동만 실었습니다.'))
A(BR)
rows=[]
for nm,n,r,p in [('남양주 지금동','201','99%','138만원'),('하남 감이동','251','97%','119만원'),
                 ('성남 금토동','478','96%','138만원'),('하남 광암동','381','96%','40만원'),
                 ('광명 소하동','194','94%','149만원'),('수원 파장동','155','94%','43만원'),
                 ('성남 복정동','102','93%','203만원'),('과천 문원동','366','92%','20만원'),
                 ('하남 감북동','444','91%','304만원'),('하남 교산동','164','87%','37만원'),
                 ('하남 초이동','217','65%','408만원'),('남양주 금곡동','184','46%','96만원')]:
    hot = nm in ('남양주 지금동','하남 초이동')
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s%s</tr>'%(bg,td(nm,'left',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333'),td(p,'right',hot),td(n,'right',hot)))
A(TABLE(['동','지분 거래','평당가','거래'],rows))
A(CAP('개발제한구역 토지 · 2024년 1월~2026년 8월 · 거래 30건 이상인 동'))
A(BR)
A(P('%s 201건 중 온전한 필지로 팔린 게 두 건뿐이라는 뜻입니다.'%HL('남양주 지금동이 99%입니다.')))
A(BR)
A(P('평당가를 같이 보시면 두 종류가 보입니다.'))
A(BR)
A(P('과천 문원동은 평당 20만원인데 지분이 92%%입니다. 하남 광암동은 평당 40만원에 96%%입니다. 반대로 하남 초이동은 %s입니다.'%B('평당 408만원인데 지분이 65%')))
A(BR)
A(P('싼 땅일수록 잘게 나뉘어 팔립니다. 평당 20만원짜리 땅은 100평을 사도 2천만원이라, 그걸 다시 열 조각으로 나누면 200만원짜리 상품이 됩니다. 소액으로 들어오라는 권유가 그래서 나옵니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 4
A(H('성남 금토동은 2019년 한 해에만 1,721건이 거래됐습니다'))
A(BR)
A(P('가장 극단적인 동네를 하나 열어 봤습니다. 성남 금토동입니다.'))
A(BR)
A(FIG('nangman_land2_fig3.png','성남 금토동 개발제한구역 연도별 거래 건수와 지분 비율'))
A(BR)
A(P('2011년에 17건, 2013년에 12건이었습니다. 지분은 0%%%%였습니다. %s'%B('그때는 땅이 통째로 팔렸습니다.')))
A(BR)
A(P('2018년에 279건으로 늘고 지분이 88%가 됩니다.'))
A(BR)
A(P('%s 그중 98%%가 지분이었습니다. 그해 평당가는 23만 9천원입니다.'%HL('그리고 2019년, 한 해에 1,721건이 거래됩니다.')))
A(BR)
A(P('금토동은 2019년 5월에 성남 금토 공공주택지구로 지정된 곳입니다. 지정 발표 전후로 거래가 몰렸습니다.'))
A(BR)
A(P('2020년에 7건으로 끊깁니다. 토지거래허가구역으로 묶인 뒤입니다. 그리고 2024년에 286건으로 돌아왔고 지분은 97%입니다.'))
A(BR)
A(P('같은 모양이 하남 교산동에도 있습니다. 2018년 30건에 73%%였다가 2019년부터 2024년까지 거래가 사실상 끊겼고, 2025년 65건, %s 교산은 2018년 12월에 3기 신도시로 발표된 곳입니다.'%B('2026년 99건에 지분 99%입니다.')))
A(BR); A(BR); A(DIV); A(BR)

# 5
A(H('거리만으로는 설명이 안 됩니다'))
A(BR)
A(P('서울에 가까울수록 지분이 많다고 하면 깔끔합니다. 그런데 맞지 않습니다. 이번엔 개발제한구역이 아닌 거래까지 포함한 토지 전체로 봤습니다.'))
A(BR)
rows=[]
for nm,km,r in [('하남시','10.5km','72.8%'),('성남시','10.6km','78.8%'),('과천시','13.6km','69.2%'),
                ('남양주시','17.1km','51.2%'),('용인시','31.0km','63.7%'),('이천시','39.9km','34.4%'),
                ('평택시','58.0km','54.5%'),('연천군','64.9km','30.4%')]:
    hot = nm in ('용인시','이천시')
    bg=' style="background-color:#FBF3F0;"' if hot else ''
    rows.append('<tr%s>%s%s%s</tr>'%(bg,td(nm,'left',hot),td(km,'right',hot),
        td(r,'right',hot,'#B5654E' if hot else '#333')))
A(TABLE(['시군','잠실역까지','지분 거래'],rows))
A(CAP('시군 중심점에서 잠실역까지 직선거리 · 토지 전체 거래 기준 · 2024년 1월~2026년 8월'))
A(BR)
A(P('가까운 세 곳이 높은 건 맞습니다. 그런데 %s 이천은 40km인데 34.4%%입니다.'%HL('용인이 31km에서 63.7%, 평택이 58km에서 54.5%입니다.')))
A(BR)
A(P('용인은 호동 92.7%, 죽전동 91.0%, 삼계리 88.3%입니다. 평택은 내리 96.4%, 후사리 94.0%, 대반리 88.6%입니다.'))
A(BR)
A(P('용인에는 반도체 클러스터가 있고 평택에는 산업단지가 있습니다. %s'%B('개발 얘기가 도는 곳이면 서울에서 멀어도 지분이 붙습니다.')))
A(BR)
A(P('지분율이 높다는 건 서울에 가깝다는 뜻이 아니라, 그 땅에 무언가 기대가 붙어 있다는 뜻입니다.'))
A(BR); A(BR); A(DIV); A(BR)

# 한계
A(H('자료의 한계'))
A(BR)
A(P('%s 전국 토지 자료가 없어 다른 시도와 비교하지 못했습니다.'%B('경기도만 봤습니다.')))
A(BR)
A(P('%s 상속으로 나뉜 땅, 가족이나 동업자가 함께 산 땅도 지분으로 잡힙니다. 비율만으로 투기라고 단정할 수 없습니다.'%B('지분 거래가 전부 쪼개 팔기는 아닙니다.')))
A(BR)
A(P('%s 거래 뒤 바뀐 곳이 있을 수 있습니다. 특히 개발제한구역에서 해제된 땅은 해제 이후 거래가 다른 용도지역으로 잡힙니다.'%B('용도지역은 신고 당시 기준입니다.')))
A(BR)
A(P('%s 필지 전체 가격과 직접 비교하기 어렵습니다. 같은 땅이라도 지분으로 쪼개 팔면 평당가가 더 높게 찍히는 경향이 있습니다.'%B('평당가는 지분 면적 기준입니다.')))
A(BR)
A(P('%s 같은 시 안에서도 동마다 거리가 크게 다릅니다.'%B('거리는 시군 중심점 기준입니다.')))
A(BR); A(BR); A(DIV); A(BR)

# 정리
A(H('정리'))
A(BR)
inner=[]
inner.append(P('%s · 경기 그린벨트 지분 거래는 2010년 5.9%%%%에서 2019년 79.2%%%%까지 올랐고, 지금은 66.8%%%%입니다.'%B('하나')))
inner.append(BR)
inner.append(P('%s · 최근 3년 개발제한구역은 65.4%%%%, 경기 토지 전체는 48.7%%%%입니다.'%B('둘')))
inner.append(BR)
inner.append(P('%s · 성남 85%%%%, 광명 83%%%%, 과천 83%%%%, 하남 79%%%%. 동으로 내려가면 남양주 지금동 99%%%%, 하남 감이동 97%%%%입니다.'%B('셋')))
inner.append(BR)
inner.append(P('%s · 과천 문원동은 평당 20만원에 92%%%%, 하남 초이동은 평당 408만원에 65%%%%입니다. 싼 땅일수록 잘게 나뉩니다.'%B('넷')))
inner.append(BR)
inner.append(P('%s · 성남 금토동은 공공주택지구 지정이 있던 2019년 한 해에 1,721건이 거래됐고 98%%%%가 지분이었습니다.'%B('다섯')))
A(BOX('\n'.join(inner)))
A(BR); A(BR); A(DIV); A(BR)

# 꼬리
A(H('함께 보면 좋은 글'))
A(BR)
def LK(u,t,d):
    return '<p style="font-size:19px;font-weight:700;"><a href="%s" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">%s</a><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(u,t,d)
def SOON(t,d):
    return '<p style="font-size:19px;font-weight:700;"><span style="color:#2E5C8A;border-bottom:1px solid #C7D6E6;">%s</span> <span style="font-size:16px;color:#B5654E;">(발행 예정)</span><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(t,d)
for t in [
 LK('https://blog.naver.com/jisandream01/224409047755','별내자이 더 스타 이그제큐티브 | 주차가 실당 1.3대입니다','별내역 앞 760실 · 샘플하우스 열려 있습니다'),
 LK('https://blog.naver.com/jisandream01/224405117181','여주 산북면 토지 956평 | 개발행위허가가 이미 나 있습니다','온전한 필지 하나를 실제로 열어 본 글입니다'),
 LK('https://blog.naver.com/dong_jin_kim/224394543980','그린벨트 토지 투자 1편 | 같은 그린벨트인데 6배 차이입니다','지목별로 얼마나 벌어지는지 센 1편입니다'),
 LK('https://blog.naver.com/jisandream01/224394277226','갈매동 그린벨트 | 694건 중 529건이 한 필지입니다','한 동네에서 쪼개기가 어떻게 도는지 본 글입니다'),
 LK('https://blog.naver.com/jisandream01/224409416262','하남 미사섬 땅값 | K-스타월드 발표 뒤 아파트는 올랐는데 땅은 왜 달랐나','발표가 땅값에 닿는 방식을 본 글입니다'),
 LK('https://blog.naver.com/dong_jin_kim/224403269485','용인 처인구 땅값 | 부지 옆은 2~5배, 밖은 그대로입니다','기대가 붙은 땅이 어디까지 오르는지 봅니다'),
 SOON('그린벨트 해제 신도시, 후보지 발표 전에 503㎢가 먼저 묶였습니다','해제와 지정이 어떤 순서로 도는지 봅니다'),
 SOON('하남 교산 황산 토지, 179건의 정체는 임야 지분이었습니다','교산에서 실제로 팔린 조각들을 열어 봅니다'),
]:
    A(t); A(BR)
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
A('<tr><td style="background-color:#F2F4F7;border-left:3px solid #2E5C8A;padding:16px 18px;">')
A('<span style="font-size:16px;color:#8A8578;">태그</span><br>')
A('<span style="font-size:18px;color:#555;line-height:1.9;">#그린벨트토지투자 #개발제한구역 #토지지분거래 #땅쪼개기 #성남금토동 #하남교산 #과천문원동 #토지실거래 #부동산데이터 #낭만부동산</span>')
A('</td></tr></table>')

x='\n'.join(O)+'\n'
x=x.replace('%%','%')
open('/mnt/user-data/outputs/재배치/nangman/land2/nangman_land2_post.html','w',encoding='utf-8').write(x)
import re
print('bytes',len(x.encode()),'본문',len(re.sub(r'<[^>]+>','',x).replace('\n','')))
