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

A('<p style="font-size:17px;color:#1B7A9E;letter-spacing:1px;">지산드림 · 하남 토지</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#0D3B5C;">하남 토지 매매, 미사섬처럼 수용 얘기가 나온 땅은 보상 기준부터 계산하고 사야 합니다</p>')
A(BR)
A(P('하남 그린벨트 땅은 개발 소식이 붙으면 값이 먼저 뜁니다. 미사섬(K-스타월드), 감북·초이(신규택지 후보)가 그렇습니다. 그런데 이런 땅이 실제로 수용되면 보상금은 '+HL('개발 소식이 붙기 전 그린벨트 값')+'으로 정해집니다.'))
A(BR)
A(P('미사섬 그린벨트 밭·논은 2022년 평당 299만원까지 거래됐고, 2023~2024년에는 230만~240만원대였습니다. 이 값에 사서 그린벨트 기준으로 보상받으면 손해가 날 수 있습니다. 사기 전에 계산해 볼 다섯 가지를 정리했습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('하남 토지 매매 전 확인할 다섯 가지'))
A(BR)
for n,t in [('하나','공시지가 · 보상은 사업 발표 직전 공시지가에서 출발합니다'),
            ('둘','용도지역 · 그린벨트는 그린벨트 상태 그대로 평가합니다'),
            ('셋','취득 시기 · 사업인정고시일 2년 전에 산 땅이어야 양도세 감면을 받습니다'),
            ('넷','사는 곳 · 땅 근처에 살지 않으면 1억원 넘는 보상금은 채권으로 받습니다'),
            ('다섯','묶인 규제 · 개발행위허가 제한과 토지거래허가가 걸려 있는지 봅니다')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(BR); A(DIV); A(BR)

A(H('하남 그린벨트 토지보상, 왜 그린벨트 값인가'))
A(BR)
A(P('대법원은 그린벨트를 「일반적인 계획 제한」으로 봅니다. 그래서 수용할 때 그린벨트인 상태 그대로 평가합니다(대법원 93누12527). 사업 때문에 그린벨트가 풀려도 풀리기 전 상태로 평가합니다. 사업 때문에 오른 땅값도 빼고 계산합니다.'))
A(BR)
A(P('하남 교산 춘궁동 평균 보상가는 평당 620만~630만원이었습니다. 대지·창고·농지를 다 합친 평균입니다. 토지주 단체는 대로변 시세의 3분의 1이라고 반발했습니다. 바로 옆 미사지구는 2010년 보상이 네 번 미뤄졌습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('하남 토지 실거래, 도로가 붙은 땅이 두 배입니다'))
A(BR)
A(TABLE(['40%','30%','30%'],['미사섬 그린벨트 땅 (2019년 이후)','평당 중간값','거래'],
 [['12m 미만 도로에 붙은 땅',(B('439만원'),'right'),('15건','right')],
  ['8m 미만 도로에 붙은 땅',('226만원','right'),('164건','right')],
  ['도로 없는 땅',('219만원','right'),('114건','right')]]))
A(CAP('국토교통부 토지 실거래 · 하남시 미사동 개발제한구역 · 해제 거래 제외 · 2019년~2026년 6월'))
A(BR)
A(P('같은 미사섬 그린벨트라도 큰 도로에 붙은 땅은 평당 439만원, 도로 없는 땅은 219만원이었습니다. 수용되면 보상 감정평가에서도 도로 조건은 값을 매기는 요소입니다. 개발 소식만 보고 도로 없는 땅을 도로 붙은 값에 사면 보상금과의 차이가 커집니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('하남 토지거래허가, 지금 묶인 것'))
A(BR)
A(P('미사동을 포함한 하남 24개 동 자연녹지 70.14㎢는 2026년 8월 18일부터 12월 31일까지 토지거래허가구역입니다. 미사섬은 2025년 2월부터 개발행위허가가 제한돼 건물을 짓거나 땅을 나눌 수 없습니다. 사업이 무산되면 구리 월드디자인시티처럼 보상 없이 그린벨트로 남습니다.'))
A(BR)
A(P('수용이 확실해 보이는 땅은 오히려 실제로 쓰고 있는 사람이 유리합니다. 사업 고시일 1년 전부터 그 집에 살아야 이주자택지를 받을 수 있습니다. 땅을 오래 가진 사람은 양도세 감면도 받습니다.'))
A(BR)
A(P('이미 하남 그린벨트 땅을 가진 분이라면 지금부터 거주 기록, 실제 이용 기록, 비닐하우스·창고 같은 지장물 목록을 정리해 두세요. 보상이 시작되면 감정평가와 이의신청은 토지보상 경험이 많은 행정사와 함께 보는 편이 좋습니다. 사고팔 땅이라면 보상 기준으로 계산한 값을 놓고 제가 합리적인 선에서 안내해 드립니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('함께 보면 좋은 글'))
A(BR)
for t in [
 LK('https://blog.naver.com/jisandream01/224409416262','하남 미사섬 땅값, K-스타월드 발표 뒤 아파트는 올랐는데 땅은 왜 달랐나','미사섬 땅과 아파트를 나란히 본 글입니다'),
 LK('https://blog.naver.com/jisandream01/224409114612','하남 감북 신규택지, 2015년 해제된 곳에 다시 넣어달라고 합니다','지구 지정 뒤 해제됐던 감북동입니다'),
 LK('https://blog.naver.com/jisandream01/224394305872','구리 토지 투자, 땅에도 종류가 넷 있습니다','용도지역을 먼저 보는 이유입니다'),
 LK('https://blog.naver.com/jisandream01/224413312449','공장 창고 시세는 도로가 정합니다, 8m 넘으면 1,357만원, 못 미치면 808만원','땅값에서 도로가 차지하는 몫입니다'),
 LK('https://blog.naver.com/dong_jin_kim/224425288775','하남 토지거래허가, 지정 직전 5일 44건, 지정 뒤 12일은 0건입니다','하남 녹지 토지거래허가입니다 · 낭만 부동산 분석 플랫폼'),
 LK('https://blog.naver.com/dong_jin_kim/224404459838','그린벨트 토지 투자 1편, 같은 그린벨트인데 6배 차이입니다','그린벨트 땅값이 무엇으로 정해지는지 봤습니다 · 낭만 부동산 분석 플랫폼'),
]:
    A(t); A(BR)
A(BR)
A(CAP('실거래: 국토교통부 토지 매매 · 하남시 미사동 개발제한구역 · 해제 거래 제외. 보상 원칙: 대법원 93누12527, 토지보상법 제67조, 같은 법 시행규칙 제23조. 교산·미사지구: 경기일보(2020년 12월), 머니투데이(2021년 1월), 시티뉴스(2010년). 토지거래허가: 아시아경제(2026년 8월 18일). 개발행위허가 제한: 하남Times(2025년 2월). 양도세 감면: 조세특례제한법 제77조. 이 글은 법률·세무 자문이 아닙니다.'))
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
A('<span style="font-size:17px;color:#555;line-height:1.9;">#하남토지 #하남토지매매 #하남토지거래허가 #하남그린벨트 #미사섬 #미사섬개발 #그린벨트토지보상 #토지수용보상 #하남토지보상 #지산드림</span>')
A('</td></tr></table>')

x='\n'.join(A_)+'\n'
open('/mnt/user-data/outputs/jisandream/jisandream_hnsy_post.html','w',encoding='utf-8').write(x)
import re
t=re.sub(r'<[^>]+>',' ',x)
print('본문',len(re.sub(r'\s','',t)), re.findall(r'\S*(?:갈[라랐렸리]|자리|고요|프리미엄|%p|어요|예요|헷갈|제자리|최고)\S*',t))
