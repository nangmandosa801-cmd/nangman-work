# -*- coding: utf-8 -*-
A_=[]; A=A_.append
DIV='<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:3px solid #1B7A9E;width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid #D6DDE3;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>'
BR='<p><br></p>'
def P(t): return '<p style="font-size:21px;color:#333;">%s</p>'%t
def H(t): return '<p style="font-size:27px;font-weight:700;color:#0D3B5C;">%s</p>'%t
def CAP(t): return '<p style="font-size:17px;color:#8A8578;">%s</p>'%t
def B(t): return '<b style="color:#0D3B5C;">%s</b>'%t
def HL(t): return '<span style="background-color:#FFF3C4;">%s</span>'%t
def FIG(f,d): return '<table width="693" style="width:100%%;min-width:693px;border-collapse:collapse;"><tr><td style="border:1px dashed #9CBBCC;padding:14px;text-align:center;"><span style="font-size:17px;color:#0D3B5C;">%s &#8212; %s</span></td></tr></table>'%(f,d)
def TABLE(ws,hs,rows):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">','<tr>']
    for i,(w,h) in enumerate(zip(ws,hs)):
        bg='#0D3B5C' if i%2==0 else '#1B7A9E'
        o.append('<td width="%s" style="background-color:%s;padding:10px 6px;text-align:center;"><span style="font-size:15px;font-weight:700;color:#FFFFFF;">%s</span></td>'%(w,bg,h))
    o.append('</tr>')
    for cells in rows:
        tr=['<tr>']
        for c in cells:
            al='left'; txt=c
            if isinstance(c,tuple): txt,al=c
            tr.append('<td style="border:1px solid #D6DDE3;padding:8px 6px;text-align:%s;"><span style="font-size:16px;font-weight:700;color:#1B7A9E;">%s</span></td>'%(al,txt))
        tr.append('</tr>'); o.append(''.join(tr))
    o.append('</table>'); return '\n'.join(o)

A('<p style="font-size:17px;color:#1B7A9E;letter-spacing:1px;">지산드림 · 구리 갈매</p>')
A(BR)
A('<p style="font-size:34px;font-weight:700;color:#0D3B5C;">지식산업센터 기숙사, 근로자만 살던 방이 열립니다</p>')
A(BR)
A(P('지식산업센터 기숙사는 오피스텔처럼 생겼는데 오피스텔이 아닙니다. 구리 갈매동 지식산업센터 기숙사가 같은 크기 오피스텔보다 싼 이유가 있습니다. 그래서 월세 수익률이 높게 나왔습니다. 그 이유가 이번 대책으로 바뀝니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('30초 요약'))
A(BR)
for n,t in [('하나','기숙사는 건축물 용도가 지식산업센터 지원시설입니다. 오피스텔이 아닙니다.'),
            ('둘','지금까지는 그 건물 입주기업과 그 종업원만 살 수 있었습니다.'),
            ('셋','2026년 9월 10일 대책에서 지원시설 이용자를 입주업체 근로자로 한정하지 않기로 했습니다.'),
            ('넷','입주 업종도 열거식에서 네거티브로 바뀝니다. 막는 업종만 빼고 다 됩니다.'),
            ('다섯','갈매동 기숙사 한 채가 1억 500만원, 월세가 65~70만원입니다.'),
            ('여섯','아직 법령 개정이 남아 있습니다. 계약 전에 관리기관 확인이 필요합니다.')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(BR); A(DIV); A(BR)

A(H('지식산업센터 기숙사는 오피스텔이 아닙니다'))
A(BR)
A(P('겉보기에는 원룸입니다. 방 하나에 화장실 하나, 주방이 붙어 있습니다. 그런데 건축물대장에 적힌 용도가 다릅니다.'))
A(BR)
A(P('오피스텔은 업무시설입니다. 기숙사는 %s입니다.'%B('지식산업센터 지원시설')))
A(BR)
A(FIG('jisandream_gisuksa_fig1.png','지산 기숙사와 오피스텔 대비'))
A(BR)
A(TABLE(['26%','37%','37%'],['구분','지산 기숙사','오피스텔'],
 [[('건축물 용도','left'),('지식산업센터 지원시설','left'),('업무시설','left')],
  [('주택 수','left'),('안 들어갑니다','left'),('주거용으로 쓰면 들어갑니다','left')],
  [('취득세','left'),('4.6%','left'),('4.6%','left')],
  [('살 수 있는 사람','left'),('제한이 있었습니다','left'),('제한 없음','left')],
  [('값','left'),('같은 크기면 더 쌉니다','left'),('더 비쌉니다','left')]]))
A(CAP('건축물대장 용도 기준 · 주택 수 포함 여부는 실제 사용 형태와 과세 관청 판단에 따라 달라질 수 있습니다'))
A(BR)
A(P('%s 살 수 있는 사람이 좁으면 사려는 사람도 적습니다.'%HL('값이 싼 이유가 네 번째 줄에 있습니다.')))
A(BR); A(BR); A(DIV); A(BR)

A(H('지산 기숙사는 그 건물 직원만 살 수 있었습니다'))
A(BR)
A(P('산업집적활성화 및 공장설립에 관한 법률이 정하고 있습니다.'))
A(BR)
A(P('지원시설은 그 지식산업센터에 입주한 기업의 생산 활동을 돕거나 근로자 복지를 위한 것이어야 합니다. 그래서 기숙사에는 %s만 살 수 있었습니다.'%B('입주기업이나 그 종업원')))
A(BR)
A(P('근거는 제28조의5 제1항 제3호와 제28조의7 제1항 제3호입니다. 자격이 없는 사람에게 넘기거나 빌려주는 것을 막는 조문입니다.'))
A(BR)
A(P('그래서 같은 크기 오피스텔보다 쌌습니다. 실수요로 살 사람이 적으니 값이 안 붙었습니다.'))
A(BR)
A(P('%s'%HL('월세는 오피스텔과 비슷하게 받는데 사는 값이 싸니, 수익률이 높게 나왔습니다.')))
A(BR); A(BR); A(DIV); A(BR)

A(H('지식산업센터 대책, 9월 10일에 이용자 제한을 푼다고 했습니다'))
A(BR)
A(P('산업통상자원부가 2026년 9월 10일 경제관계장관회의에서 지식산업센터 대책을 내놨습니다. 전국 공실률이 높아진 데 따른 것입니다.'))
A(BR)
A(FIG('jisandream_gisuksa_fig2.png','이번 대책에서 풀리는 것과 갈매동 해당 여부'))
A(BR)
A(TABLE(['30%','70%'],['무엇을','어떻게'],
 [[('지원시설 이용자','left'),('입주업체 근로자로 한정하지 않습니다','left')],
  [('입주 업종','left'),('열거식에서 네거티브로 바꿉니다','left')],
  [('막는 업종','left'),('사행·유해시설, 환경부담 업종, 위험물 시설','left')],
  [('새로 되는 것','left'),('AI 앱 개발, 도심형 소형 물류, 드론 촬영 같은 업종','left')],
  [('오피스텔 전환','left'),('일반공업지역에 있는 곳만 한시 허용','left')],
  [('공공임대','left'),('수도권은 LH가 사서 청년·신혼 임대주택으로','left')]]))
A(CAP('산업통상자원부 2026년 9월 10일 발표 기준 · 세부 기준은 법령 개정과 가이드라인으로 정해집니다'))
A(BR)
A(P('첫 줄이 기숙사에 해당합니다. %s'%B('「이용자도 입주업체 근로자에 한정되지 않는다」입니다.')))
A(BR)
A(P('오피스텔 전환은 일반공업지역에 있는 곳만입니다. 갈매동 지식산업센터는 여기 해당하지 않습니다. 이건 따로 정리해 둔 글이 있습니다.'))
A(BR)
A(P('LH가 사들이는 쪽은 구리시가 대상지역에 들어갔습니다.'))
A(BR); A(BR); A(DIV); A(BR)

A(H('구리 갈매동 휴밸나인 기숙사는 한 채 1억 500만원입니다'))
A(BR)
A(P('구리 갈매동 휴밸나인 지식산업센터의 기숙사입니다.'))
A(BR)
A(TABLE(['34%','66%'],['항목','내용'],
 [[('위치','left'),('구리시 갈매동 · 8호선 별내역 도보권','left')],
  [('건축물 용도','left'),('지식산업센터 기숙사','left')],
  [('한 채','left'),('1억 500만원','left')],
  [('월세','left'),('65~70만원','left')],
  [('같은 동네 원룸','left'),('월세 실거래 중간값 62.3만원','left')]]))
A(CAP('갈매동 원룸 월세는 실거래 315건 기준 · 물건마다 다르므로 개별 확인이 필요합니다'))
A(BR)
A(P('갈매동에서 월세 70만원을 받는 원룸을 사려면 얼마가 드는지 따로 세어 둔 글이 있습니다. 그 글과 이어서 보시면 됩니다.'))
A(BR)
A(P('%s 지금까지는 그 방에 들일 수 있는 사람이 좁아서 값이 눌려 있었습니다. 이용자 제한이 풀리면 이 구조가 달라집니다.'%HL('여기서 중요한 건 월세가 아니라 임차인의 범위입니다.')))
A(BR); A(BR); A(DIV); A(BR)

A(H('지산 기숙사 계약 전에 확인하실 것'))
A(BR)
A(P('%s 발표는 나왔고 세부 기준은 법령 개정과 가이드라인으로 정해집니다. 지금 시점에 무엇이 되고 무엇이 아직인지는 건물마다 다릅니다.'%B('대책은 발표 단계입니다.')))
A(BR)
A(P('%s 지식산업센터는 관리기관이 있습니다. 구리시와 관리단에 지금 기준을 확인하셔야 합니다.'%B('관리기관에 물어보셔야 합니다.')))
A(BR)
A(P('%s 법이 허용해도 관리규약이 따로 정해 둔 것이 있을 수 있습니다.'%B('관리규약도 봐야 합니다.')))
A(BR)
A(P('%s 기숙사는 담보인정 조건이 오피스텔과 다릅니다. 은행마다 다르니 미리 확인하시는 게 좋습니다.'%B('대출 조건을 먼저 보십시오.')))
A(BR)
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
A('<tr><td style="background-color:#0D3B5C;padding:10px 14px;"><span style="font-size:16px;color:#FFFFFF;letter-spacing:1px;">지금 다루는 물건</span></td></tr>')
A('<tr><td style="border-left:1px solid #C3D5DF;border-right:1px solid #C3D5DF;border-bottom:1px solid #C3D5DF;padding:20px 22px;background-color:#FBFCFD;">')
A(P('구리 갈매동 휴밸나인 기숙사입니다. 한 채 1억 500만원, 월세 65~70만원입니다.'))
A(BR)
A(P('갈매동 물건은 제가 직접 보고 다룹니다. 지금 기준으로 어디까지 되는지 관리기관에 확인해서 안내해 드리겠습니다.'))
A(BR)
A(P('%s'%B('합리적인 가격으로 안내해 드립니다. 편하게 문의 주세요.')))
A('</td></tr></table>')
A(BR); A(BR); A(DIV); A(BR)

A(H('정리'))
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:3px solid #0D3B5C;background-color:#F4F6F8;padding:20px 22px;">')
for n,t in [('하나','기숙사는 지식산업센터 지원시설입니다. 오피스텔이 아닙니다.'),
            ('둘','지금까지 그 건물 입주기업과 그 종업원만 살 수 있었습니다. 산업집적법 제28조의5와 제28조의7입니다.'),
            ('셋','그래서 값이 쌌고, 월세는 비슷하니 수익률이 높게 나왔습니다.'),
            ('넷','2026년 9월 10일 대책에서 지원시설 이용자를 근로자로 한정하지 않기로 했습니다.'),
            ('다섯','입주 업종도 네거티브로 바뀌어 막는 업종만 빼고 다 됩니다.'),
            ('여섯','갈매동은 오피스텔 전환 대상은 아닙니다. 이용자 제한 쪽이 해당합니다.'),
            ('일곱','법령 개정과 가이드라인이 남아 있습니다. 관리기관 확인이 먼저입니다.')]:
    A(P('%s · %s'%(B(n),t))); A(BR)
A(P('값이 싼 이유가 바뀌면 값도 바뀝니다.'))
A('</td></tr></table>')
A(BR); A(BR); A(DIV); A(BR)

A(H('함께 보면 좋은 글'))
A(BR)
def LK(u,t,d):
    return '<p style="font-size:19px;font-weight:700;"><a href="%s" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">%s</a><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(u,t,d)
for t in [
 LK('https://blog.naver.com/jisandream01/224410106954','별내역 도보 7분 원룸 | 1억 500만원에 연 8% 나옵니다','이 글의 그 물건입니다 · 월세와 수익률을 숫자로 셌습니다'),
 LK('https://blog.naver.com/jisandream01/224409047755','별내자이 더 스타 이그제큐티브 | 주차가 실당 1.3대입니다','같은 생활권 오피스텔 · 별내역 앞 760실'),
 LK('https://blog.naver.com/jisandream01/224402027023','별내자이 더 스타 분양가 | 255개 호실 중 6.09억이 가장 낮습니다','호실별 분양가를 면적군으로 정리했습니다'),
 LK('https://blog.naver.com/jisandream01/224403930372','가산어반워크2 매매 | 이 건물에 나온 매물 중 가장 낮은 값입니다','지식산업센터 매매 물건입니다'),
 LK('https://blog.naver.com/jisandream01/224413070562','지식산업센터 공실 대책 | 갈매동은 오피스텔 전환 대상이 아닙니다','이번 대책에서 갈매동이 어디에 드는지 정리했습니다'),
 LK('https://blog.naver.com/jisandream01/224413366601','지식산업센터 LH 매입 | 구리시가 대상지역에 들어갔습니다','공공이 사들이는 쪽 이야기입니다'),
 LK('https://blog.naver.com/jisandream01/224387502852','구리 갈매동 지식산업센터 | 사기는 쉬운데 팔기가 어렵습니다','되팔 때 무엇이 걸리는지 본 글입니다'),
 LK('https://blog.naver.com/jisandream01/224411815733','별내 오피스텔 전월세 | 실제로 얼마에 나갔는지 1,532건을 셌습니다','옆 동네 오피스텔 월세와 비교하실 때 보십시오'),
 LK('https://blog.naver.com/jisandream01/224387553133','구리 갈매동 오피스텔 수익률 | 작은 게 더 낮았습니다','크기별로 수익률이 어떻게 갈리는지 봤습니다'),
]:
    A(t); A(BR)
A(BR)
A(CAP('지식산업센터 지원시설과 기숙사의 입주 자격은 산업집적활성화 및 공장설립에 관한 법률 제28조의5와 제28조의7에 따른 것으로 국가법령정보센터를 기준으로 정리했습니다. 2026년 9월 10일 산업통상자원부가 경제관계장관회의에서 발표한 지식산업센터 대책의 내용은 발표 자료와 보도를 기준으로 했으며, 세부 기준은 법령 개정과 가이드라인으로 정해지므로 시행 시점과 범위가 달라질 수 있습니다. 오피스텔 전환 허용은 일반공업지역에 있는 미분양·공실 지식산업센터에 한시적으로 적용됩니다. 가격과 월세는 작성 시점 현장 기준이며 물건마다 다릅니다. 갈매동 원룸 월세 중간값은 실거래 315건을 집계한 것입니다. 주택 수 포함 여부, 취득세, 대출 조건은 실제 사용 형태와 개별 판단에 따라 달라지므로 과세 관청과 금융기관에 확인하셔야 합니다. 지난 자료와 발표를 정리한 것으로 앞으로의 가격을 예측하거나 보장하지 않으며 특정 물건의 매수·매도를 권유하지 않습니다. 판단과 결과의 책임은 본인에게 있으며 정확한 검토는 현장 확인과 전문가 상담을 거치시기 바랍니다.'))
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
A('<p style="font-size:21px;font-weight:700;color:#0D3B5C;">구리 갈매동에서 지식산업센터·창고·아파트를 다룹니다</p>')
A(BR)
A('<p style="font-size:17px;color:#333;">현장을 직접 보고 실거래를 열어 확인한 것만 씁니다.</p>')
A('<p style="font-size:17px;color:#333;">되팔 때 걸릴 것까지 미리 말씀드립니다.</p>')
A(BR)
A('<p style="height:1px;background-color:#DDD8CE;margin:6px 0 14px 0;"></p>')
A('<p style="font-size:17px;font-weight:700;"><a href="https://blog.naver.com/jisandream01/224387498556" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">구리 갈매동 공인중개사 | 지산드림 지식산업센터 공장 창고 전문 ›</a><br>')
A('<span style="font-size:15px;color:#7A8590;">구리와 남양주, 마곡에서 다루는 물건들입니다</span></p>')
A('</td></tr></table>')
A(BR)
A('<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">')
A('<tr><td style="border-left:3px solid #1B7A9E;background-color:#F4F6F8;padding:16px 18px;">')
A('<span style="font-size:15px;color:#8A8578;">태그</span><br>')
A('<span style="font-size:17px;color:#555;line-height:1.9;">#지식산업센터기숙사 #지산기숙사 #휴밸나인 #구리갈매휴밸나인 #갈매동지식산업센터 #지식산업센터공실대책 #지원시설 #소액부동산투자 #구리갈매동공인중개사 #지산드림</span>')
A('</td></tr></table>')

x='\n'.join(A_)+'\n'
x=x.replace('%%','%')
open('/mnt/user-data/outputs/재배치/jisandream/gisuksa/jisandream_gisuksa_post.html','w',encoding='utf-8').write(x)
import re
print('bytes',len(x.encode()),'본문',len(re.sub(r'<[^>]+>','',x).replace('\n','')))
