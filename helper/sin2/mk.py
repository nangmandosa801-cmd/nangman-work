from kit import *
TITLE='신축아파트 2년후, 2024년 입주 아파트 올해 계약 절반은 새 세입자였습니다'
o=[]
o.append(f'<p style="font-size:17px;color:{A};letter-spacing:1px;">낭만 부동산 분석 플랫폼 · 신축 2년 차 · 전세</p>\n<p><br></p>\n')
o.append(f'<p style="font-size:34px;font-weight:700;color:{D};">{TITLE}</p>\n<p><br></p>\n')
o.append(P('신축아파트 2년후에는 무슨 일이 생길까요. 입주장에 들어온 세입자의 전세 계약이 끝나는 해입니다.'))
o.append(P(f'2024년에 지은 전국 아파트 635개 단지에서 올해 전월세 계약이 36,820건 신고됐습니다. {B("이 가운데 52%가 새 세입자와 맺은 신규 계약입니다.")} 다시 계약한 갱신은 46%입니다.'))
o.append(P(f'새 세입자는 2년 전 입주장 금액보다 평균 26% 높게 들어왔습니다. 그대로 남은 세입자는 4.6% 올렸습니다. 평균 금액으로는 남은 세입자가 3억 3,400만원, 새 세입자가 {HL("4억 300만원")}입니다.'))
o.append(FIGS([('52%','2024년 입주 아파트<br>올해 신규 계약',D),('+26%','새 세입자 전세<br>2년 전 입주장보다',A),('2년','도배 · 타일<br>하자보수 기간',D)]))

o.append(H('신축아파트 2년후, 올해 계약 두 건 중 한 건은 새 세입자입니다'))
o.append(IMG('nangman_sinchuk2_1_split.png','신축아파트 2년후 · 2024년에 지은 아파트 2026년 전월세 계약 구분'))
o.append(P('올해 1월부터 9월까지 매달 1,600~2,400건씩 새 세입자 계약이 나왔습니다. 2024년에 입주한 단지는 올해 한 해 동안 차례로 첫 전세 만기를 맞습니다.'))
o.append(P('새 세입자가 들어오는 집은 앞 세입자가 이사를 나간 집입니다. 이사 나간 날과 새 세입자가 들어오는 날 사이에 빈집이 생깁니다.'))

o.append(H('신축 전세 2년 뒤, 다시 계약하면 4.6% 새로 들어오면 26%'))
o.append(IMG('nangman_sinchuk2_2_money.png','신축 전세 2년 뒤 · 2024년 입주 단지 갱신 전세와 신규 전세'))
o.append(P('2024년에 지은 아파트 가운데 갱신과 신규가 모두 5건 넘게 나온 단지·면적 259개를 비교했습니다. 2년 전 입주장 금액은 갱신 계약서에 적힌 종전 보증금입니다.'))
o.append(P(f'갱신은 평균 4.6% 올랐습니다. 갱신요구권을 쓰면 5% 넘게 올릴 수 없습니다. 갱신 계약의 63%가 갱신요구권을 쓴 계약입니다.'))
o.append(P(f'신규는 평균 26% 올랐습니다. 259개 가운데 89%는 신규가 갱신보다 높았습니다. {B("입주장에 싸게 들어온 세입자가 남으면 4년 동안 싸게 삽니다.")} 세입자가 바뀌면 집주인은 2년 전보다 전세를 크게 올려 받습니다.'))
o.append(P('오산 사례는 「'+LK('https://blog.naver.com/dong_jin_kim/224457240998','오산역 금강펜테리움 전세, 2년 전 오산 입주장 신규 24%·갱신 5% 상승')+'」에, 입주장 첫 석 달 금액은 「'+LK('https://blog.naver.com/dong_jin_kim/224457234936','입주장 전세, 새 아파트 50곳은 첫 석 달 그대로였고 넷째 달부터 올랐습니다')+'」에, 입주장 급매가 몰리는 달은 「'+LK('https://blog.naver.com/dong_jin_kim/224457266231','입주장 전세급매 잡는법, 큰 단지는 둘째 달 급매가 평소의 1.6배였습니다')+'」에 정리했습니다.'))

o.append(H('신축 전세 저렴한 이유가 끝나는 해, 지역마다 달랐습니다'))
o.append(IMG('nangman_sinchuk2_3_sido.png','신축아파트 2년후 · 시도별 2024년 입주 아파트 신규 계약 비중'))
o.append(P(f'새 세입자 비중은 대구가 {HL("82%")}로 가장 높았습니다. 강원 77%, 경북 75%입니다. 서울은 40%, 경기는 44%로 낮았습니다.'))
o.append(P('서울은 갱신 세입자와 신규 세입자의 전세 차이가 평균 1억 6,230만원으로 가장 큽니다. 새로 들어가면 1억 6천만원을 더 내야 하는 동네에서 신규 계약은 10건 중 4건뿐이었습니다.'))
o.append(P('대구는 같은 차이가 4,290만원입니다. 대구 2024년 입주 단지는 계약 10건 중 8건이 신규였습니다. 새 세입자를 받는 집은 그 사이 집을 손볼 기회가 생깁니다.'))

o.append(H('아파트 하자보수 기간 몇년, 도배와 타일은 2년입니다'))
o.append(IMG('nangman_sinchuk2_4_haja.png','아파트 하자보수 기간 · 공동주택관리법 하자담보책임기간'))
o.append(P(f'세대 안 하자보수 기간은 열쇠를 받은 날부터 셉니다. 도배 · 타일 · 도장 · 주방기구 같은 마감공사는 {B("2년")}입니다. 창호 · 단열 · 급배수는 3년, 방수는 5년입니다.'))
o.append(P('입주 2년 차는 전세 만기와 마감공사 하자보수 기간 끝이 겹칩니다. 세입자가 나간 빈집에서 들뜬 타일, 벌어진 줄눈, 벽지 곰팡이가 보이면 2년 안에 하자로 접수할 수 있습니다. 기간이 지나면 집주인 돈으로 고칩니다.'))
o.append(P('하자 접수 순서는 「'+LK('https://blog.naver.com/champion_chart/224444779647','아파트 하자보수 기간, 타일과 도배 같은 마감공사는 2년이라 입주 2년 차 전세 만기 전에 봅니다')+'」에 있습니다. 창틀 누수는 3년이라 「'+LK('https://blog.naver.com/champion_chart/224444953177','창틀 누수 보수, 새 아파트는 3년 안이면 하자보수부터 청구합니다')+'」를 보면 됩니다.'))

o.append(H('전세 원상복구 범위, 2년 만에 나가는 세입자가 떼는 것'))
o.append(P('입주장 세입자는 새 집에 중문, 필름, 선반을 직접 단 경우가 많습니다. 이사할 때는 내가 단 것을 떼고 처음 상태로 되돌립니다. 살면서 자연스럽게 낡은 것은 세입자가 고치지 않습니다.'))
o.append(P('어디까지가 세입자 몫인지는 「'+LK('https://blog.naver.com/champion_chart/224435839462','전세 원상복구, 살면서 자연스럽게 낡은 건 세입자 몫이 아니고 내가 단 중문 · 필름 · 선반은 떼고 나갑니다')+'」에 정리했습니다. 중문 철거 비용은 10만~30만원입니다.'))
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:1px solid #C7D6E6;border-bottom:1px solid #C7D6E6;padding:14px 18px;"><span style="font-size:19px;color:{D};">새 세입자를 받기 전 빈집일 때 줄눈은 34평 욕실 2곳과 현관 기준 {B("경제형 23만원")}부터입니다 → '+LK('https://blog.naver.com/champion_chart/224453266232','줄눈 시공 가격 34평')+'</span></td></tr></table>\n<p><br></p>\n')
o.append(NOTE('자료: 국토교통부 아파트 전월세 실거래(2026년 1월~10월 23일 계약 · 2026년 10월 24일 받은 자료) · 2024년에 지은 아파트 · 계약구분 신규 · 갱신 · 갱신요구권 사용 여부 · 종전계약 보증금 · 공동주택관리법 시행령 별표 4(하자담보책임기간) · 단지·면적 비교는 월세 없는 전세만, 갱신 · 신규 모두 5건 넘는 곳의 중앙값'))
o.append(f'''<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:5px solid {A};background-color:#F4F6F9;padding:20px 22px;"><p style="font-size:21px;font-weight:700;color:{A};">입주 2년 차 단지 앞 중개사무소 인터뷰를 받습니다</p>
<p><br></p>
<p style="font-size:20px;color:#333;line-height:1.7;">첫 전세 만기 때 집주인과 세입자가 묻는 것 같은 현장 이야기를 들려주시면 블로그에 무료로 소개합니다. 원고는 올리기 전에 먼저 보여 드립니다.</p>
<p style="font-size:20px;color:#333;line-height:1.7;">▸ 신청: 문자 010-2882-8165 (사무소 이름 · 편한 요일)</p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224449575744','부동산 홍보방법, 입주 단지 중개사무소를 찾아가 인터뷰하고 그 단지 글마다 사무소를 무료로 소개합니다 ›')}</p>
</td></tr></table>
<p><br></p>
''')
o.append(f'<p style="font-size:27px;font-weight:700;color:{D};">함께 보면 좋은 글</p>\n<p><br></p>\n')
for t,u,s in [('상도동 아파트 전세, 새 아파트 입주 때는 옆 단지보다 1억 낮았습니다','https://blog.naver.com/dong_jin_kim/224451832221','2024년 입주 상도 푸르지오 클라베뉴의 2년 뒤 갱신과 신규'),
 ('신검단중앙역 센트레빌 전세, 같은 역 새 아파트 입주 때 84㎡는 3억이었습니다','https://blog.naver.com/dong_jin_kim/224451824958','검단 입주장 전세와 2년 뒤 갱신 금액'),
 ('서울 전세가율, 7~9월 단지 486곳 가운데 80%를 넘은 곳은 1곳이고 금천 · 도봉이 61%로 가장 높습니다','https://blog.naver.com/dong_jin_kim/224441368891','서울 단지별 전세가율'),
 ('경기도 전세, 31개 시군 전세가율과 갭투자 필요 금액을 세웠습니다','https://blog.naver.com/dong_jin_kim/224401817897','경기도 시군별 전세가율'),
 ('신축아파트 입주비용, 6억 집은 취득세 660만원에 청소 · 새집증후군 71만원','https://blog.naver.com/dong_jin_kim/224451684611','입주 때 함께 나가는 돈'),
 ('입주장 전세급매 잡는법, 큰 단지는 둘째 달 급매가 평소의 1.6배였습니다','https://blog.naver.com/dong_jin_kim/224457266231','큰 단지 급매가 몰리는 달'),
 ('입주장 전세, 새 아파트 50곳은 첫 석 달 그대로였고 넷째 달부터 올랐습니다','https://blog.naver.com/dong_jin_kim/224457234936','입주장 첫 석 달과 넷째 달 전세'),
 ('오산역 금강펜테리움 전세, 2년 전 오산 입주장 신규 24%·갱신 5% 상승','https://blog.naver.com/dong_jin_kim/224457240998','오산 2024년 입주 단지 갱신과 신규')]:
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
<span style="font-size:19px;font-weight:700;color:{D};">입주 2년 차 집을 손본다면</span><br><br>
''')
for t,u,s in [('창문 결로 하자, 신축 첫 겨울에 접수되는 결로와 생활 결로를 나누는 법','https://blog.naver.com/champion_chart/224444582153','2년 차 겨울 전에 결로 하자부터'),
 ('전세집 수리 범위, 보일러 고장과 비 새는 벽은 집주인이 고치고 별 비용 없이 손쉽게 고칠 사소한 것은 세입자가 고칩니다','https://blog.naver.com/champion_chart/224444749412','집주인과 세입자가 고치는 것'),
 ('전세집 중문, 집주인 동의 받고 달거나 무타공으로 달 수 있고 철거 비용은 10만~30만원입니다','https://blog.naver.com/champion_chart/224431136138','새 세입자로 들어가는 집의 중문')]:
    o.append(f'<a href="{u}" style="font-size:19px;font-weight:700;color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n<span style="font-size:16px;color:#7A8590;">{s}</span><br><br>\n')
o.append('</td></tr></table>\n<p><br></p>\n')
tags='#신축아파트2년후 #신축전세 #신축전세저렴한이유 #아파트하자보수기간 #아파트하자보수기간몇년 #하자보수기간 #전세원상복구 #전세원상복구범위 #전세갱신요구권 #입주장전세 #전세만기이사 #낭만부동산'
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">\n<tr><td style="background-color:#F4F6F9;border-left:3px solid {A};padding:16px 18px;">\n<span style="font-size:16px;color:#8A8578;">태그</span><br>\n<span style="font-size:18px;color:#555;line-height:1.9;">{tags}</span>\n</td></tr>\n</table>\n')
H_=''.join(o); open('post.html','w').write(H_)
import re,html as _h
txt=re.sub(r'<p><br></p>','',H_); txt=re.sub(r'</p>|<br>|</tr>','\n',txt); txt=re.sub(r'<[^>]+>','',txt); txt=_h.unescape(re.sub(r'\n{3,}','\n\n',txt))
open('post.txt','w').write('[제목]\n'+TITLE+'\n\n'+txt)
print(len(H_))
