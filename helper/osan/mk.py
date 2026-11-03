from kit import *
TITLE='오산역 금강펜테리움 전세, 2년 전 오산 입주장은 갱신 5% 신규 24% 올랐습니다'
o=[]
o.append(f'<p style="font-size:17px;color:{A};letter-spacing:1px;">낭만 부동산 분석 플랫폼 · 오산 입주 단지 · 전세</p>\n<p><br></p>\n')
o.append(f'<p style="font-size:34px;font-weight:700;color:{D};">{TITLE}</p>\n<p><br></p>\n')
o.append(P('오산역 금강펜테리움 센트럴파크가 10월부터 열쇠를 줍니다. 730세대가 모두 84㎡입니다. 같은 면적 전세가 한 단지에서 한꺼번에 나옵니다.'))
o.append(P(f'입주장에 정한 전세 금액은 2년으로 끝나지 않습니다. {B("2024년에 입주한 오산 새 아파트 5곳을 보면 입주장 세입자는 2년 뒤 4.5%만 올려 다시 계약했습니다.")} 같은 해 새로 들어온 세입자는 2년 전 금액보다 24% 높게 계약했습니다.'))
o.append(P(f'두 세입자의 전세 차이는 평균 {HL("4,750만원")}입니다. 입주장 금액이 4년 동안 그 집 전세의 기준이 됩니다.'))
o.append(FIGS([('4.5% 올림','입주장 세입자<br>2년 뒤 갱신',D),('24% 올림','같은 집에<br>새로 들어온 세입자',A),('4,750만원','갱신과 신규<br>전세 차이 평균',D)]))

o.append(H('오산 아파트 전세, 2년 전 입주장 세입자는 5%만 올려 다시 계약했습니다'))
o.append(P('2024년에 지은 오산 아파트 5곳에서 올해 전세 갱신이 이어졌습니다. 종전 보증금은 2년 전 입주장 때 계약한 금액입니다.'))
o.append(IMG('nangman_osan_jeonse_1_osan.png','오산 아파트 전세 · 2024년 입주 단지 2년 전 금액과 올해 갱신 · 신규 전세'))
rows=[('힐스테이트 오산 더퍼스트 59㎡','2억 1천만원','2억 2,050만원','2억 8천만원'),
('힐스테이트 오산 더퍼스트 84㎡','2억 5천만원','2억 6,250만원','3억 3천만원'),
('오산 세교 한양수자인 59㎡','2억원','2억 1,500만원','2억 7천만원'),
('오산 세교 한양수자인 64㎡','2억 5천만원','2억 6,050만원','3억원'),
('중흥S-클래스 에듀파크 59㎡','2억 3천만원','2억 4,150만원','2억 8천만원'),
('중흥S-클래스 에듀파크 72㎡','2억 6,500만원','2억 6,775만원','3억 3천만원'),
('중흥S-클래스 에듀파크 84㎡','2억 9천만원','3억 450만원','3억 5천만원'),
('오산 롯데캐슬 스카이파크 84㎡','2억 8천만원','2억 8,500만원','3억 2천만원'),
('오산 라온프라이빗스위트 84㎡','2억 6천만원','2억 7,500만원','3억원')]
o.append(TABLE(['오산 2024년 입주 단지','2년 전 입주장','올해 갱신','올해 신규'],rows,["37%","21%","21%","21%"]))
o.append(NOTE('국토교통부 아파트 전월세 실거래 · 2024년에 지은 경기 오산시 아파트 · 2026년 1월~10월 23일 계약 · 월세 없는 전세만 · 「2년 전 입주장」은 갱신 계약에 적힌 종전 보증금 · 갱신과 신규 모두 5건 이상인 단지·면적만 · 중앙값'))
o.append(P(f'아홉 줄 모두 신규가 갱신보다 높습니다. 차이는 작은 곳이 2,500만원, 큰 곳이 6,750만원입니다. 힐스테이트 오산 더퍼스트 84㎡는 같은 단지 같은 면적인데 {B("갱신 세입자가 2억 6,250만원, 새 세입자가 3억 3천만원")}입니다.'))
o.append(P('오산 2024년 입주 단지 갱신 계약 182건 가운데 82%가 갱신요구권을 썼습니다. 갱신요구권을 쓰면 보증금을 5% 넘게 올릴 수 없습니다. 입주장 금액에서 5%를 더한 값이 2년 뒤 금액의 상한이 됩니다.'))

o.append(H('전세 갱신요구권, 전국 2024년 입주 단지에서도 같았습니다'))
o.append(P(f'2024년에 지은 전국 아파트에서 갱신과 신규가 모두 5건 넘게 나온 단지·면적은 259개입니다. 갱신 세입자는 평균 4.6% 올렸습니다. 신규 세입자는 2년 전 금액보다 평균 26% 높았습니다.'))
o.append(P(f'259개 가운데 {HL("89%")}는 신규가 갱신보다 높았습니다. 신규 전세가 2년 전 입주장 금액보다 낮은 곳은 2%뿐입니다. 갱신 계약의 63%는 갱신요구권을 쓴 계약입니다.'))
o.append(IMG('nangman_osan_jeonse_2_sido.png','전세 갱신요구권 · 2024년 입주 단지 갱신 세입자와 신규 세입자 전세 차이 · 시도별'))
o.append(P('차이는 서울이 1억 6,230만원으로 가장 컸습니다. 부산 9,160만원, 경기 7,400만원, 인천 5,210만원입니다. 서울과 부산처럼 전세 금액이 큰 곳에서 차이가 컸습니다.'))

o.append(H('오산역 금강펜테리움 전세, 먼저 입주한 세교파라곤은 넉 달 만에 6천만원 올랐습니다'))
o.append(P('올봄 입주한 세교파라곤 84㎡ 신규 전세는 2~4월 27건의 중앙값이 3억 2천만원입니다. 6~8월 22건의 중앙값은 3억 8천만원입니다.'))
o.append(IMG('nangman_osan_jeonse_3_segyo.png','오산 세교파라곤 84㎡ 전세 · 입주 첫 달부터 달별 금액'))
o.append(P(f'4월 한 달에만 같은 84㎡가 2억 8천만원부터 4억 5천만원까지 계약됐습니다. 입주장 한가운데에서는 {B("같은 집이 1억 7천만원 차이로 계약")}됩니다.'))
o.append(P('전국 새 아파트 50곳도 같았습니다. 첫 석 달 전세는 그대로였고 넷째 달부터 올랐습니다. 이 내용은 「입주장 전세, 새 아파트 50곳은 첫 석 달 그대로였고 넷째 달부터 올랐습니다」에 정리했습니다.'))

o.append(H('입주장 전세, 언제 계약했느냐가 4년 금액을 정합니다'))
o.append(P('세교파라곤 숫자로 4년을 이어 보면 이렇습니다.'))
o.append(VS(('2~4월에 계약한 세입자','세교파라곤 84㎡ · 입주 첫 석 달',['처음 2년 3억 2천만원','갱신요구권을 쓰면 2년 뒤 3억 3,600만원','4년 동안 3억 3,600만원 넘지 않음'],D),
            ('6~8월에 계약한 세입자','같은 단지 같은 면적 · 넉 달 뒤',['처음 2년 3억 8천만원','갱신요구권을 쓰면 2년 뒤 3억 9,900만원','두 세입자 차이 6천만원 넘게 이어짐'],A)))
o.append(P(f'세입자 쪽에서 보면 입주장 첫 석 달 계약은 4년 동안 이어지는 싼 전세입니다. 집주인 쪽에서 보면 같은 6천만원을 4년 동안 덜 받는 계약입니다.'))
o.append(P(f'집주인이 6천만원을 보증금으로 더 받으면 그만큼 잔금 대출을 덜 받게 됩니다. 연 4% 대출이라면 {HL("한 해 240만원")}, 4년이면 960만원 이자 차이입니다. 반대로 넉 달을 비워 두면 그동안 관리비와 대출 이자를 집주인이 냅니다.'))
o.append(P('오산역 금강펜테리움은 730세대가 같은 84㎡라 세교파라곤처럼 첫 석 달 금액이 비슷하게 모일 수 있습니다. 첫 신고가 나오면 이 글에 숫자를 더하겠습니다.'))

o.append(H('오산역 금강펜테리움 매매, 옆 새 아파트는 2년 된 단지보다 8,750만원 낮았습니다'))
o.append(P('세교파라곤 84㎡ 매매는 6~9월 17건, 중앙값 4억 9천만원입니다. 2024년에 지은 중흥S-클래스 에듀파크 84㎡는 10건, 5억 7,750만원입니다.'))
o.append(P(f'전세는 넉 달 만에 옆 단지를 넘었는데 매매는 아직 {B("8,750만원")} 낮습니다. 세교파라곤 6~8월 전세 3억 8천만원은 매매 중앙값의 78%입니다.'))

o.append(H('오산역 금강펜테리움 입주, 전세를 내놓기 전에 현관부터'))
o.append(P('730세대가 모두 84㎡이면 세입자 눈에는 집이 다 비슷해 보입니다. 현관을 열었을 때 중문이 달려 있는지, 줄눈과 입주청소가 끝나 있는지가 먼저 보입니다.'))
o.append(P('옵션 여닫이를 넣지 않은 집이 옆으로 미는 3연동을 다는 방법은 「'+LK('https://blog.naver.com/champion_chart/224442889901','오산역 금강펜테리움 센트럴파크 입주, 옵션 중문은 여닫이 126만원이었고 옆으로 미는 3연동은 입주 뒤에 따로 답니다')+'」에 있습니다. 줄눈 · 입주청소 · 매트 순서는 「'+LK('https://blog.naver.com/champion_chart/224436127312','오산역 금강펜테리움 입주일, 730세대가 모두 84㎡라 줄눈과 매트도 순서만 지키면 이삿날 전에 끝납니다')+'」에 정리했습니다.'))
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:1px solid #C7D6E6;border-bottom:1px solid #C7D6E6;padding:14px 18px;"><span style="font-size:19px;color:{D};">직접 들어가 사는 집은 입주청소와 새집증후군을 하루 차이로 묶으면 34평(84㎡) {B("71만 4천원")}입니다 → '+LK('https://blog.naver.com/champion_chart/224451151010','입주청소 새집증후군 묶음')+'</span></td></tr></table>\n<p><br></p>\n')
o.append(NOTE('자료: 오산역 금강펜테리움 센트럴파크 입주자모집공고(오산시 가수동 · 세교2지구 A8블록 · 730세대 · 모두 84㎡ · 입주 예정 2026년 10월) · 국토교통부 아파트 매매 · 전월세 실거래(2026년 10월 24일 받은 자료 · 해제 거래 뺌) · 단지 이름은 실거래 자료에 적힌 이름을 띄어 씀 · 대출 이자는 연 4% 단순 계산'))
o.append(f'''<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:5px solid {A};background-color:#F4F6F9;padding:20px 22px;"><p style="font-size:21px;font-weight:700;color:{A};">오산역 금강펜테리움 센트럴파크 앞 중개사무소 인터뷰를 받습니다</p>
<p><br></p>
<p style="font-size:20px;color:#333;line-height:1.7;">입주장 전세 분위기, 잔금 날 손님들이 묻는 것 같은 현장 이야기를 들려주시면 블로그에 무료로 소개합니다. 원고는 올리기 전에 먼저 보여 드립니다.</p>
<p style="font-size:20px;color:#333;line-height:1.7;">▸ 신청: 문자 010-2882-8165 (사무소 이름 · 편한 요일)</p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224449575744','부동산 홍보방법, 입주 단지 중개사무소를 찾아가 인터뷰하고 그 단지 글마다 사무소를 무료로 소개합니다 ›')}</p>
</td></tr></table>
<p><br></p>
''')
o.append(f'<p style="font-size:27px;font-weight:700;color:{D};">함께 보면 좋은 글</p>\n<p><br></p>\n')
for t,u,s in [('신검단중앙역 센트레빌 전세, 같은 역 새 아파트 입주 때 84㎡는 3억이었습니다','https://blog.naver.com/dong_jin_kim/224451824958','검단 새 아파트 입주장 전세와 2년 뒤 갱신 금액'),
 ('상도동 아파트 전세, 새 아파트 입주 때는 옆 단지보다 1억 낮았습니다','https://blog.naver.com/dong_jin_kim/224451832221','서울 새 아파트 입주장 전세를 옆 구축과 비교'),
 ('향남역 그로브 스위첸 분양가, 84㎡ 5억 1,340만~5억 5,970만원은 올해 향남에서 가장 비싸게 팔린 5억 500만원보다 높습니다','https://blog.naver.com/dong_jin_kim/224434613491','오산과 붙은 화성 서남부 5억대 새 아파트'),
 ('화성 아파트 시세, 거래 45%가 동탄2인데 회복률은 꼴찌입니다','https://blog.naver.com/dong_jin_kim/224417170873','오산 옆 화성 아파트 가격 흐름'),
 ('경기도 전세, 31개 시군 전세가율과 갭투자 필요 금액을 세웠습니다','https://blog.naver.com/dong_jin_kim/224401817897','오산을 포함한 경기도 시군별 전세가율'),
 ('입주장 전세, 새 아파트 50곳은 첫 석 달 그대로였고 넷째 달부터 올랐습니다 (발행 예정)','','전국 새 아파트 50곳 입주장 전세 흐름')]:
    o.append(TAIL(t,u,s))
o.append(f'''<p><br></p>
<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr>
<td style="border-left:3px solid {D};background-color:#F4F6F9;padding:22px 24px;">
<p style="font-size:17px;color:{A};letter-spacing:1px;">NANGMAN REAL ESTATE PLATFORM</p>
<p><br></p>
<p style="font-size:23px;font-weight:700;color:{D};">답이 아니라 방법을 씁니다</p>
<p><br></p>
<p style="font-size:19px;color:#333;">실거래를 직접 열어 차이가 얼마인지 세고, 그중 얼마가 무엇 때문인지 분석합니다.</p>
<p style="font-size:19px;color:#333;">모르는 건 모른다고 씁니다.</p>
<p><br></p>
<p><br></p>
<p style="height:3px;background-color:{D};margin:0;"></p>
<p style="font-size:16px;color:{A};letter-spacing:1px;">블로그 대행 · 데이터 분석</p>
<p style="font-size:21px;font-weight:700;color:{D};">부동산 블로그 작성에 도움이 필요하시거나</p>
<p style="font-size:21px;font-weight:700;color:{D};">부동산 데이터 분석 자료가 필요하시면 요청해 주세요</p>
<p style="height:3px;background-color:{D};margin:0;"></p>
<p><br></p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224448347577','부동산 블로그 대행, 맡기기 전에 글 한 편으로 확인할 다섯 가지 ›')}</p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224377990326','부동산을 데이터로 읽고, 공부한 것을 기록합니다 ›')}</p>
</td></tr></table>
<p><br></p>
<p style="font-size:19px;text-align:center;">▶ <a href="https://blog.naver.com/champion_chart" style="font-weight:700;color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">낭만 인테리어 바로 가기 blog.naver.com/champion_chart</a></p>
<p><br></p>
<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F4F6F9;border-left:4px solid {A};padding:18px 20px;">
<span style="font-size:16px;color:#7A8590;letter-spacing:1px;">옆 블로그 · 낭만 인테리어</span><br>
<span style="font-size:19px;font-weight:700;color:{D};">오산에서 집을 고친다면</span><br><br>
''')
for t,u,s in [('전세집 중문, 집주인 동의 받고 달거나 무타공으로 달 수 있고 철거 비용은 10만~30만원입니다','https://blog.naver.com/champion_chart/224431136138','전세로 들어가는 집의 중문'),
 ('입주청소 추가금 요구 244건, 계약 전 확인 6가지와 현장 대처 순서','https://blog.naver.com/champion_chart/224455976621','입주장에 몰리는 청소 예약에서 추가금 피하기'),
 ('중문 옵션 사제 차이, 입주 단지 19곳 옵션 중문은 110만원에서 365만원입니다','https://blog.naver.com/champion_chart/224430190408','옵션으로 넣을지 입주 뒤에 달지')]:
    o.append(f'<a href="{u}" style="font-size:19px;font-weight:700;color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n<span style="font-size:16px;color:#7A8590;">{s}</span><br><br>\n')
o.append('</td></tr></table>\n<p><br></p>\n')
tags='#오산역금강펜테리움전세 #오산역금강펜테리움 #오산역금강펜테리움센트럴파크 #오산역금강펜테리움입주 #오산아파트전세 #오산아파트전세시세 #전세갱신요구권 #계약갱신요구권5% #입주장전세 #세교파라곤전세 #힐스테이트오산더퍼스트 #중흥S클래스에듀파크 #낭만부동산'
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">\n<tr><td style="background-color:#F4F6F9;border-left:3px solid {A};padding:16px 18px;">\n<span style="font-size:16px;color:#8A8578;">태그</span><br>\n<span style="font-size:18px;color:#555;line-height:1.9;">{tags}</span>\n</td></tr>\n</table>\n')
H_=''.join(o); open('post.html','w').write(H_)
import re,html as _h
txt=re.sub(r'<p><br></p>','',H_); txt=re.sub(r'</p>|<br>|</tr>','\n',txt); txt=re.sub(r'<[^>]+>','',txt); txt=_h.unescape(re.sub(r'\n{3,}','\n\n',txt))
open('post.txt','w').write('[제목]\n'+TITLE+'\n\n'+txt)
print(len(H_))
