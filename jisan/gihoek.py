# -*- coding: utf-8 -*-
exec(open('/home/claude/jisan/jkit.py').read())
def TABLE(ws,hs,rows):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">','<tr>']
    for i,(w,h) in enumerate(zip(ws,hs)):
        bg='#0D3B5C' if i%2==0 else '#1B7A9E'
        o.append('<td width="%s" style="background-color:%s;padding:13px 8px;text-align:center;"><span style="font-size:18px;font-weight:700;color:#FFFFFF;">%s</span></td>'%(w,bg,h))
    o.append('</tr>')
    for cells in rows:
        tr=['<tr>']
        for c in cells:
            al='left'; txt=c
            if isinstance(c,tuple): txt,al=c
            tr.append('<td style="border:1px solid #D6DDE3;padding:11px 8px;text-align:%s;"><span style="font-size:19px;font-weight:700;color:#1B7A9E;">%s</span></td>'%(al,txt))
        tr.append('</tr>'); o.append(''.join(tr))
    o.append('</table>'); return '\n'.join(o)
def KV(pairs):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">']
    for k,v in pairs:
        o.append('<tr><td width="28%%" style="background-color:#EEF3F6;border-bottom:1px solid #FFFFFF;padding:13px 12px;"><span style="font-size:19px;font-weight:700;color:#0D3B5C;">%s</span></td><td style="border-bottom:1px solid #D6DDE3;padding:13px 12px;"><span style="font-size:20px;color:#333;">%s</span></td></tr>'%(k,v))
    o.append('</table>'); return '\n'.join(o)

A('<p style="font-size:17px;color:#1B7A9E;letter-spacing:1px;">지산드림 · 토지 매매</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#0D3B5C;">기획부동산, 신도시 옆 그린벨트 임야를 지분으로 쪼개 공시지가 3배에 팔았습니다</p>')
A(BR)
A(P('신도시나 산단이 발표되면 「바로 옆 땅」이라는 전화가 옵니다. 대부분 '+HL('그린벨트 임야를 여러 사람 지분으로 쪼갠 땅')+'입니다. 성남 금토동 그린벨트 임야는 약 4,800명에게 974억원어치가 팔렸습니다. 공시지가의 약 3배였고, 성남시는 개발 가능성이 전혀 없다고 봤습니다.'))
A(BR)
A(P('수용되지 않고 신도시 옆에 남은 땅이 어떻게 팔리는지, 이미 산 땅은 어떻게 해야 하는지 정리했습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('30초 요약'))
A(BR)
for n,t in [('하나','기획부동산은 개발이 어려운 임야를 사서 지분으로 쪼개 비싸게 팝니다.'),
            ('둘','금토동 임야는 공시지가 ㎡당 2만 1,700원 땅을 약 7만원에 팔았습니다.'),
            ('셋','산 사람의 26%는 기획부동산 직원, 62%는 직원 지인이었습니다.'),
            ('넷','경기도 임야 지분 쪼개기는 2018~2020년 10만 5,000건, 2조 7,000억원 규모였습니다.'),
            ('다섯','하남 감북·초이 그린벨트를 해제 1순위라며 판 땅은 10년이 지나도 그린벨트입니다.')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(BR); A(DIV); A(BR)

A(H('기획부동산 뜻, 이렇게 팝니다'))
A(BR)
A(P('기획부동산은 개발이 거의 불가능한 큰 임야를 싸게 산 뒤, 지분으로 잘게 나눠 높은 값에 파는 업체를 말합니다. 신도시·산단·도로 발표가 나오면 「바로 옆」, 「해제 1순위」 같은 말을 붙입니다. 지도에는 신도시 경계와 내 땅을 가깝게 그려 보여 줍니다.'))
A(BR)
A(TABLE(['30%','70%'],['단계','하는 일'],
 [['① 매입','그린벨트·보전산지 임야를 싸게 삼'],
  ['② 쪼개기','필지는 그대로 두고 지분만 수백~수천 명에게 나눔'],
  ['③ 영업','직원과 그 지인에게 먼저 팔고 「신도시 옆」 강조'],
  ['④ 가격',B('공시지가의 몇 배로 팖')]]))
A(CAP('서울신문(2020년 2월 23일) 금토동 사례 · 밸류맵 분석 보도'))
A(BR); A(BR); A(DIV); A(BR)

A(H('기획부동산 사기, 금토동 4,800명 사례'))
A(BR)
A(P('성남 금토동 산73번지는 청계산 능선 그린벨트이고 환경평가 1등급인 공익용 산지입니다. 기획부동산 법인 33곳이 2019년 7월 이 땅을 사서 약 4,800명에게 지분으로 팔았습니다. 판 금액은 974억원입니다.'))
A(BR)
A(P('공시지가는 ㎡당 2만 1,700원이었는데 약 7만원에 팔았습니다. 산 사람의 26%는 기획부동산 직원, 62%는 직원 지인이었습니다. 바로 옆에 판교 제2테크노밸리가 있다는 점을 앞세웠지만, 성남시는 이 땅의 개발 가능성이 전혀 없다는 입장입니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('하남 그린벨트, 해제 1순위라던 땅'))
A(BR)
A(P('2016년 한 업체는 하남 감북·초이동 그린벨트를 「해제 가능성 1순위」라며 평당 59만~80만원에 나눠 팔았습니다. 감북동은 2010년 공공주택지구로 지정됐다가 2015년 풀린 곳입니다. 새 택지 발표 때마다 후보로 거론됐지만 2026년 지금도 그린벨트입니다.'))
A(BR)
A(P('미사섬도 마찬가지입니다. K-스타월드 재추진 뒤 미사섬 그린벨트 땅은 올해 6월까지 19건 거래 중 16건이 지분 거래였습니다. 같은 날 같은 평당 가격으로 5건씩 팔린 날도 있습니다. 개발되더라도 보상은 그린벨트 값으로 받습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('기획부동산 땅 처분, 이미 샀다면'))
A(BR)
A(P('지분 땅은 팔기가 어렵습니다. 사려는 사람이 거의 없고, 다른 공유자 동의 없이는 땅을 나누거나 쓸 수도 없습니다. 이미 샀다면 먼저 세 가지를 확인하세요.'))
A(BR)
for n,t in [('하나','토지이음에서 용도지역·그린벨트·보전산지 여부 확인'),
            ('둘','내 지분이 전체의 몇 분의 몇인지, 공유자가 몇 명인지 등기부로 확인'),
            ('셋','산 가격과 공시지가·주변 실거래를 비교')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(P('공유자가 많으면 공유물 분할 소송으로 내 몫을 나누는 방법이 있지만 시간과 비용이 큽니다. 판매 과정에서 「곧 해제된다」처럼 거짓 설명을 들었다면 계약 취소나 손해배상을 다툴 수 있는지 변호사와 상담하세요.'))
A(BR)
A(P('신도시 옆 땅을 보러 왔다면 지분이 아니라 '+B('통째로 사는 땅, 도로가 붙은 땅, 그린벨트가 아닌 땅')+'부터 보세요. 제가 실거래와 규제를 함께 놓고 합리적인 선에서 안내해 드립니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('함께 보면 좋은 글'))
A(BR)
for t in [
LK('https://blog.naver.com/jisandream01/224409416262','하남 미사섬 땅값, K-스타월드 발표 뒤 아파트는 올랐는데 땅은 왜 달랐나','미사섬 땅과 아파트를 나란히 본 글입니다'),
 LK('https://blog.naver.com/jisandream01/224409114612','하남 감북 신규택지, 2015년 해제된 곳에 다시 넣어달라고 합니다','지구 지정 뒤 해제됐던 감북동입니다'),
 LK('https://blog.naver.com/jisandream01/224394305872','구리 토지 투자, 땅에도 종류가 넷 있습니다','용도지역을 먼저 보는 이유입니다'),
 LK('https://blog.naver.com/jisandream01/224413312449','공장 창고 시세는 도로가 정합니다, 8m 넘으면 1,357만원, 못 미치면 808만원','땅값에서 도로가 차지하는 몫입니다'),
 LK('https://blog.naver.com/dong_jin_kim/224416473291','3기 신도시 비교, 계양 대장 창릉 왕숙 교산, 항목별로 나란히 놓았습니다','보상이 진행된 3기 신도시입니다 · 낭만 부동산 분석 플랫폼'),
 LK('https://blog.naver.com/dong_jin_kim/224404459838','그린벨트 토지 투자 1편, 같은 그린벨트인데 6배 차이입니다','그린벨트 땅값이 무엇으로 정해지는지 봤습니다 · 낭만 부동산 분석 플랫폼'),
]:
    A(t); A(BR)
A(BR)
A(CAP('금토동 사례: 서울신문(2020년 2월 23일) · 경기도 임야 지분 거래: 밸류맵 분석, 서울경제 보도 · 감북·초이 분양: 2016년 언론 보도 · 미사섬 거래: 국토교통부 토지 실거래(하남시 미사동 개발제한구역, 2026년 6월까지). 이 글은 법률 자문이 아니며, 이미 산 땅의 계약 문제는 변호사와 상담하세요.'))
A(BR)
A('<p style="font-size:14px;color:#9AA4AE;">지산드림공인중개사사무소 · 대표 김미호 · 등록번호 41310-2022-00061 · 경기도 구리시 갈매동 540-5, 101호</p>')
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:2px solid #1B7A9E;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>')
A(BR)
A('<p style="font-size:19px;font-weight:700;color:#0D3B5C;text-align:center;">지산드림</p>')
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;"><tr>')
A('<td width="100%" style="border-left:3px solid #0D3B5C;background-color:#F4F6F8;padding:22px 24px;">')
A('<p style="font-size:15px;color:#1B7A9E;letter-spacing:1px;">JISANDREAM</p>')
A(BR)
A('<p style="font-size:21px;font-weight:700;color:#0D3B5C;">구리 갈매동에서 지식산업센터·창고·아파트·토지를 다룹니다</p>')
A(BR)
A('<p style="font-size:17px;color:#333;">현장을 직접 보고 확인한 것만 씁니다.</p>')
A('<p style="font-size:17px;color:#333;">되팔 때 걸릴 것까지 미리 말씀드립니다.</p>')
A(BR)
A('<p style="height:1px;background-color:#DDD8CE;margin:6px 0 14px 0;"></p>')
A('<p style="font-size:17px;font-weight:700;"><a href="https://blog.naver.com/jisandream01/224387498556" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">구리 갈매동 공인중개사 | 지산드림 지식산업센터 공장 창고 전문 ›</a><br>')
A('<span style="font-size:15px;color:#7A8590;">구리와 남양주, 가평에서 다루는 물건들입니다</span></p>')
A('</td></tr></table>')
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
A('<tr><td style="border-left:3px solid #1B7A9E;background-color:#F4F6F8;padding:16px 18px;">')
A('<span style="font-size:15px;color:#8A8578;">태그</span><br>')
A('<span style="font-size:17px;color:#555;line-height:1.9;">#기획부동산 #기획부동산사기 #기획부동산땅처분 #기획부동산뜻 #임야지분 #지분투자 #그린벨트임야 #신도시인근토지 #하남토지 #지산드림</span>')
A('</td></tr></table>')

x='\n'.join(A_)+'\n'
open('/mnt/user-data/outputs/jisandream/jisandream_gihoek_post.html','w',encoding='utf-8').write(x)
import re
t=re.sub(r'<[^>]+>',' ',x)
print('본문',len(re.sub(r'\s','',t)), re.findall(r'\S*(?:갈[라랐렸리]|자리|고요|프리미엄|%p|어요|예요|헷갈|제자리|최고)\S*',t))
