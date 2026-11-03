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

A('<p style="font-size:17px;color:#1B7A9E;letter-spacing:1px;">지산드림 · 토지보상과 택지</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#0D3B5C;">협의자택지 뜻, 1,000㎡ 넘는 땅을 협의로 넘기면 받는 택지이고 미사 이주자택지는 평당 720만원이었습니다</p>')
A(BR)
A(P('땅이 수용될 때 보상금 말고 '+HL('택지')+'를 받을 수 있는 사람이 있습니다. 그 땅에 살던 사람은 이주자택지, 땅을 협의로 넘긴 사람은 협의자택지입니다. 협의자택지의 정식 이름은 협의양도인택지입니다.'))
A(BR)
A(P('하남 미사지구 이주자택지는 '+HL('301필지')+'가 평당 720만원, 필지당 5억 1,000만~5억 8,000만원에 공급됐습니다. 택지를 받으면 무엇을 얼마에 받는지, 협의자택지 추첨방법까지 정리했습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('30초 요약'))
A(BR)
for n,t in [('하나','협의자택지는 수도권 1,000㎡ 이상 땅을 주민공람 1년 전부터 갖고 협의로 넘긴 사람이 받습니다.'),
            ('둘','그린벨트 지구에서는 그린벨트 지정 전부터 땅을 가진 사람이 1순위입니다.'),
            ('셋','이주자택지는 그 집에 고시일 1년 전부터 산 사람이 받습니다.'),
            ('넷','이주자택지 값은 조성원가에서 기반시설비를 뺀 값, 협의자택지는 수도권에서 감정가 수준입니다.'),
            ('다섯','두 택지 모두 공급계약 전 권리를 사고팔면 무효이고 처벌받습니다.')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(BR); A(DIV); A(BR)

A(H('협의자택지 뜻, 협의양도인택지와 같은 말입니다'))
A(BR)
A(TABLE(['30%','35%','35%'],['구분','이주자택지','협의자택지 (협의양도인택지)'],
 [['누가','그 지구 안 집에 산 사람','그 지구 안 땅을 협의로 넘긴 사람'],
  ['조건','고시일 1년 전부터 계속 거주','수도권 1,000㎡ 이상 · 주민공람 1년 전부터 소유'],
  ['가격',B('조성원가 − 기반시설비'),B('수도권은 감정가 수준')],
  ['넘기는 방식','수용재결로 가도 대상','수용재결이 아니라 협의로 넘겨야 함']]))
A(CAP('LH 이주 및 생활대책 수립지침 요약 · 경향신문(2021년 5월 26일) · 사업마다 공고 기준이 다릅니다'))
A(BR)
A(P('협의자택지는 「다투지 않고 협의로 땅을 넘긴 사람」에게 주는 혜택입니다. 보상금이 마음에 들지 않아 수용재결로 가면 협의자택지는 받을 수 없습니다. 보상금을 더 다툴지, 택지를 받을지 먼저 계산해야 하는 이유입니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('협의자택지 추첨방법, 순위를 먼저 나눕니다'))
A(BR)
A(P('신청자가 공급 필지보다 많으면 순위를 나누고 같은 순위 안에서 추첨합니다. 그린벨트를 풀어 만드는 지구에서는 '+B('그린벨트 지정 전부터 땅을 가진 사람')+'이 1순위입니다. 오래 가진 원래 땅 주인을 먼저 챙기는 방식입니다. 세부 순위와 추첨 방식은 사업마다 공급 공고문에 나옵니다.'))
A(BR)
A(P('당첨되면 공급계약을 맺습니다. 계약 전에 협의자택지 권리를 사고팔면 무효이고 3년 이하 징역 또는 1억원 이하 벌금입니다. 계약 뒤에는 사업시행자 동의를 받아 한 번만 팔 수 있습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('이주자택지 가격, 미사와 파주 사례'))
A(BR)
A(TABLE(['30%','35%','35%'],['사례','면적','공급가'],
 [['하남 미사 이주자택지 301필지','필지당 71~80평',(B('평당 720만원 · 5.1억~5.8억원'),'right')],
  ['파주 동패동 이주자택지 (점포겸용)','234~384㎡',('3억 3,121만~6억 6,069만원','right')]]))
A(CAP('미사: 이코노믹리뷰 · 파주: LH 2024년 2월 공급공고'))
A(BR)
A(P('미사 이주자택지는 건폐율 60%, 용적률 200%, 4층까지 6가구를 지을 수 있는 땅이었습니다. 1층에 상가를 넣을 수 있는 점포겸용 택지는 265㎡ 이하, 주거전용은 330㎡ 이하입니다.'))
A(BR)
A(P('값만 보고 고르면 안 됩니다. 택지를 받아도 건물을 지을 돈이 따로 듭니다. 하남 교산은 원주민 단체가 이주자택지에 땅값과 건축비를 합쳐 25억원 안팎이 든다고 추정했고, 기존 점포형 이주자택지의 재정착률은 10% 안팎이었습니다. 단체 추정치라 사업마다 다를 수 있습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('택지와 보상금, 어느 쪽이 나은가'))
A(BR)
A(P('협의자택지를 받으려면 협의로 땅을 넘겨야 합니다. 보상금을 다투면 택지를 놓칩니다. 대토보상도 보상금에 이의를 제기하지 않아야 받습니다. 그래서 순서가 중요합니다. 감정평가 금액을 먼저 보고, 다툴 근거가 있으면 이의신청을 하고, 근거가 약하면 협의와 택지를 고르는 방식입니다.'))
A(BR)
A(P('하남·구리·남양주처럼 보상이 이어지는 동네라면 택지 공고와 주변 땅값을 함께 놓고 계산해 봐야 합니다. 토지보상 서류와 이의신청은 보상 경험이 많은 행정사와, 받은 택지나 주변 땅을 사고팔 때는 제가 합리적인 선에서 함께 봐 드립니다.'))
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
A(CAP('이주자택지·협의양도인택지 기준: LH 이주 및 생활대책 수립지침(한국건설기술연구원 CODIL 연구 인용), 경향신문(2021년 5월 26일) · 전매 제한: 택지개발촉진법 제19조의2, 2020년 12월 개정 · 미사 이주자택지: 이코노믹리뷰 · 파주 동패동: LH 2024년 2월 공급공고 · 교산 추정: 경기일보(2024년 7월 15일, 원주민 단체 인용). 공급 기준과 순위는 사업마다 공고문을 확인하세요. 이 글은 법률 자문이 아닙니다.'))
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
A('<span style="font-size:17px;color:#555;line-height:1.9;">#협의자택지 #협의자택지뜻 #협의자택지추첨방법 #협의양도인택지 #이주자택지 #이주자택지가격 #점포겸용택지 #하남토지보상 #토지보상 #지산드림</span>')
A('</td></tr></table>')

x='\n'.join(A_)+'\n'
open('/mnt/user-data/outputs/jisandream/jisandream_hyj_post.html','w',encoding='utf-8').write(x)
import re
t=re.sub(r'<[^>]+>',' ',x)
print('본문',len(re.sub(r'\s','',t)), re.findall(r'\S*(?:갈[라랐렸리]|자리|고요|프리미엄|%p|어요|예요|헷갈|제자리|최고)\S*',t))
