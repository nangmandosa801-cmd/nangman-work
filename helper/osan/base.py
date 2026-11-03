import html
D='#1F3864'; A='#2E5C8A'; BR='#B5533C'; L='#C8D2DE'
def P(t): return f'<p style="font-size:21px;color:#333;">{t}</p>\n<p><br></p>\n'
def HL(t): return f'<b style="color:{D};border-bottom:6px solid #D4E6F7;background:linear-gradient(to top,#D4E6F7 40%,transparent 40%);">{t}</b>'
def B(t): return f'<b style="color:{D};">{t}</b>'
def LK(url,t): return f'<a href="{url}" style="color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a>'
def H(t): return (f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:3px solid {A};width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid {L};font-size:1px;line-height:1px;">&nbsp;</td></tr></table>\n<p><br></p>\n'
                  f'<p style="font-size:27px;font-weight:700;color:{D};">{t}</p>\n<p><br></p>\n')
import json as _j
_U=_j.load(open('urls.json'))
def IMG(fn,cap):
    k=fn.replace('nangman_ipjujang_jeonse_','').replace('.png','')
    return f'<p style="text-align:center;"><img src="{_U[k]}" alt="{cap}" width="693" style="width:100%;max-width:693px;"></p>\n<p style="font-size:17px;color:#7A8590;text-align:center;">{cap}</p>\n<p><br></p>\n'
def NOTE(t): return f'<p style="font-size:18px;color:#8A8578;">{t}</p>\n<p><br></p>\n'
def FIGS(items):
    tds=[]
    for i,(big,sub,col) in enumerate(items):
        br='' if i==len(items)-1 else 'border-right:8px solid #FFFFFF;'
        tds.append(f'<td width="33%" style="background-color:#F4F6F9;border-top:4px solid {col};{br}padding:20px 10px;text-align:center;vertical-align:top;"><span style="font-size:24px;font-weight:700;color:{col};">{big}</span><br><span style="font-size:18px;color:#555;line-height:1.6;">{sub}</span></td>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr>{"".join(tds)}</tr></table>\n<p><br></p>\n'
def TABLE(head,rows,widths,hl=None):
    h=''.join(f'<td width="{w}" style="background-color:{D};padding:13px 8px;text-align:center;"><span style="font-size:18px;font-weight:700;color:#FFFFFF;">{c}</span></td>' for i,(c,w) in enumerate(zip(head,widths)))
    out=[f'<tr>{h}</tr>']
    for r,row in enumerate(rows):
        bg=' style="background-color:#F0F4F8;"' if r%2 else ''
        if hl is not None and r in hl: bg=' style="background-color:#F1F6FB;"'
        cells=[]
        for j,c in enumerate(row):
            al='left' if j==0 else 'right'
            st=f'font-size:19px;font-weight:700;color:{D};' if j==0 else 'font-size:19px;color:#333;'
            cells.append(f'<td style="border:1px solid {L};padding:11px 8px;text-align:{al};"><span style="{st}">{c}</span></td>')
        out.append(f'<tr{bg}>{"".join(cells)}</tr>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">\n'+'\n'.join(out)+'\n</table>\n<p><br></p>\n'
def BARS(cap,items,lo,hi):
    rows=[]
    for lab,v,n,strong in items:
        w=max(4,round((v-lo)/(hi-lo)*100)); col=A if strong else '#9FB3C8'
        rows.append(f'<tr><td width="24%" style="padding:9px 6px;border-bottom:1px solid {L};"><span style="font-size:19px;color:{D};font-weight:700;">{lab}</span></td>'
                    f'<td width="56%" style="padding:9px 6px;border-bottom:1px solid {L};"><table width="100%" style="border-collapse:collapse;"><tr><td width="{w}%" style="background-color:{col};height:18px;font-size:1px;line-height:1px;">&nbsp;</td><td style="font-size:1px;">&nbsp;</td></tr></table></td>'
                    f'<td width="20%" style="padding:9px 6px;border-bottom:1px solid {L};text-align:right;"><span style="font-size:20px;font-weight:700;color:{A if strong else "#555"};">{v}</span><span style="font-size:16px;color:#7A8590;"> ({n}곳)</span></td></tr>')
    return (f'<p style="font-size:18px;color:#555;">{cap}</p>\n<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;border-top:2px solid {D};">\n'+'\n'.join(rows)+'\n</table>\n<p><br></p>\n')
def VS(a,b):
    def cell(t,sub,lines,col,br):
        return (f'<td width="50%" style="border-top:4px solid {col};{br}background-color:#F4F6F9;padding:18px 16px;vertical-align:top;"><span style="font-size:20px;font-weight:700;color:{col};">{t}</span><br><span style="font-size:17px;color:#7A8590;">{sub}</span><br><br>'
                + '<br>'.join(f'<span style="font-size:19px;color:#333;line-height:1.8;">{x}</span>' for x in lines)+'</td>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;"><tr>{cell(*a,"border-right:8px solid #FFFFFF;")}{cell(*b,"")}</tr></table>\n<p><br></p>\n'
def TAIL(title,url,sub):
    t=LK(url,title) if url else f'<span style="color:{A};">{title}</span>'
    return f'<p style="font-size:19px;font-weight:700;">{t}<br>\n<span style="font-size:17px;color:#7A8590;">{sub}</span></p>\n<p><br></p>\n'

TITLE='입주장 전세, 새 아파트 50곳은 첫 석 달 그대로였고 넷째 달부터 올랐습니다'
o=[]
o.append(f'<p style="font-size:17px;color:{A};letter-spacing:1px;">낭만 부동산 분석 플랫폼 · 입주장 · 전세</p>\n<p><br></p>\n')
o.append(f'<p style="font-size:34px;font-weight:700;color:{D};">{TITLE}</p>\n<p><br></p>\n')
o.append(P('새 아파트 입주장 전세는 언제가 가장 쌀까요. 입주 첫 달이 가장 싸다는 말이 많습니다. 실거래는 조금 다릅니다.'))
o.append(P(f'올해 2~7월에 첫 전월세 계약이 신고된 전국 새 아파트 50곳, 계약 4,533건입니다. 같은 단지 같은 면적 전세끼리 첫 두 달 금액과 비교했습니다.'))
o.append(P(f'{B("입주장 전세는 첫 석 달 동안 그대로였습니다.")} 넷째 달부터 오르기 시작했습니다. 일곱째 달에는 첫 두 달보다 평균 {HL("7.9%")} 높았습니다.'))
o.append(FIGS([('그대로','입주장 첫 석 달 전세<br>첫 두 달 금액과 같음',D),('7.9% 올랐습니다','일곱째 달 전세<br>첫 두 달보다 (평균)',A),('1억 7천만원','세교파라곤 84㎡ 전세<br>4월 한 달 안 금액 차이',D)]))

o.append(H('입주장 시기, 계약은 첫 넉 달에 10건 중 6건이 몰립니다'))
o.append(P(f'입주지정기간은 보통 두 달 안팎입니다. 계약도 그 무렵에 몰립니다. 50곳 계약 4,533건 가운데 {HL("64%")}가 첫 넉 달에 나왔습니다. 셋째 달과 넷째 달이 각각 19%로 가장 많습니다.'))
o.append(P('첫 달은 12%뿐입니다. 입주 전에 미리 계약하는 세입자가 적기 때문입니다. 열쇠를 받는 둘째 달부터 계약이 늘어납니다.'))
o.append(P('일곱째 달이 넘으면 계약이 거의 없습니다. 비어 있던 집이 다 찼다는 뜻입니다.'))
o.append(IMG('nangman_ipjujang_jeonse_2_sigi.png','입주장 시기 · 첫 계약 달부터 달마다 나온 계약 비중'))

o.append(H('입주장 전세, 첫 석 달은 오르지 않았습니다'))
o.append(IMG('nangman_ipjujang_jeonse_1_month.png','입주장 전세 · 첫 석 달은 그대로, 넷째 달부터 오름'))
o.append(TABLE(['첫 계약 달부터','입주장 전세 (첫 두 달 = 100)','단지·면적 수'],
  [('첫 달','101','24곳'),('둘째 달','100','35곳'),('셋째 달','100','28곳'),('넷째 달','<b style="color:#1F3864;">103</b>','32곳'),('다섯째 달','<b style="color:#1F3864;">104</b>','22곳'),('여섯째 달','<b style="color:#1F3864;">106</b>','14곳'),('일곱째 달','<b style="color:#1F3864;">108</b>','10곳')],["34%","38%","28%"]))
o.append(NOTE('국토교통부 아파트 전월세 실거래 · 2024년 이후 지은 아파트 가운데 2026년 2~7월에 첫 전월세 계약이 신고된 단지 · 계약 40건 이상 · 임대 단지 뺌 · 같은 단지 같은 전용면적 전세(월세 없는 계약)의 달별 중앙값을 그 단지 첫 두 달 중앙값으로 나눈 뒤 평균 · 그달 전세가 3건 넘는 단지·면적만 · 2026년 10월은 23일 계약까지'))
o.append(P('첫 석 달 전세는 100 근처에서 움직이지 않았습니다. 집이 한꺼번에 쏟아지는 때라 집주인끼리 금액을 비슷하게 맞춥니다.'))
o.append(P(f'넷째 달 103, 일곱째 달 108로 올랐습니다. 빈집이 줄면서 금액이 올라갑니다. {B("입주장 끝 무렵에 계약한 세입자는 첫 석 달에 계약한 세입자보다 전세를 더 냈습니다.")}'))
o.append(P('넉 달 넘게 계약이 이어진 단지·면적 33개 가운데 21개는 2% 넘게 올랐습니다. 7개는 그대로였습니다. 5개는 내렸습니다.'))

o.append(H('신축 입주장 전세, 단지마다 이렇게 움직였습니다'))
rows=[('오산 세교파라곤 (84㎡)','2월','3월 3억 2천만원','7월 3억 9천만원'),
('포항 학산 한신더휴 엘리트파크 (84㎡)','6월','6월 2억 3천만원','10월 2억 7,500만원'),
('오산 호반써밋 라프리미어 (59㎡)','4월','5월 2억 4,800만원','9월 3억원'),
('서울 청량리 롯데캐슬 하이루체 (59㎡)','2월','3월 6억원','6월 6억 6천만원'),
('인천 신검단중앙역 디에트르 더에듀 (59㎡)','2월','3월 2억 5,500만원','7월 3억원'),
('인천 신검단중앙역 칸타빌 더스위트 (84㎡)','3월','4~8월 3억원','9월 3억 3천만원'),
('대구 힐스테이트 동대구센트럴 (84㎡)','3월','3월 3억 2천만원','10월 3억 5천만원'),
('인천 롯데캐슬 넥스티엘 (84㎡)','3월','3월 4억 5천만원','6월 4억 500만원'),
('이천 힐스테이트 이천역 1단지 (84㎡)','7월','8월 3억 6,500만원','9월 3억 2천만원')]
o.append(IMG('nangman_ipjujang_jeonse_6_danji.png','신축 입주장 전세 · 단지별 처음 전세와 최근 전세'))
o.append(NOTE('국토교통부 아파트 전월세 실거래 · 2026년 · 전세(월세 없는 계약) 달별 중앙값 · 59㎡는 전용 59.9㎡ 안팎, 84㎡는 84.9㎡ 안팎'))
o.append(P(f'오산 세교파라곤은 넉 달 만에 {HL("7천만원")} 올랐습니다. 포항 학산 한신더휴는 넉 달 만에 4,500만원 올랐습니다. 같은 검단에서도 칸타빌 더스위트는 다섯 달 동안 3억원에 머물렀습니다.'))
o.append(P('대구 힐스테이트 동대구센트럴은 셋째 달과 넷째 달에 2억 9천만원으로 3천만원 내렸습니다. 그 뒤 다시 올라 10월에는 처음보다 3천만원 높아졌습니다. 입주장 한가운데에서 잠깐 싸졌던 단지입니다.'))

o.append(H('입주장 전세급매, 첫 달보다 넷째 달에 더 많이 나옵니다'))
o.append(P('입주장 전세급매는 첫 달에 나온다고 보기 쉽습니다. 실거래는 반대입니다.'))
o.append(P(f'같은 단지, 같은 면적, 같은 달 전세 가운데 낮은 계약과 높은 계약의 차이는 첫 달 평균 2,500만원이었습니다. 넷째 달에는 5,000만원, 다섯째 달에는 {HL("7,100만원")}으로 벌어졌습니다.'))
o.append(IMG('nangman_ipjujang_jeonse_3_geupmae.png','입주장 전세급매 · 같은 달 싼 전세와 비싼 전세의 차이'))
o.append(P(f'오산 세교파라곤 84㎡는 4월 한 달에 2억 8천만원짜리 전세와 4억 5천만원짜리 전세가 같이 계약됐습니다. {B("1억 7천만원 차이")}입니다.'))
o.append(IMG('nangman_ipjujang_jeonse_5_segyo.png','오산 세교파라곤 84㎡ 입주장 전세 · 달별 중앙값과 가장 낮은 · 높은 계약'))
o.append(P('첫 달에는 집주인 모두가 비슷한 금액을 부릅니다. 석 달쯤 지나면 집주인마다 사정이 다릅니다. 잔금 날짜가 급한 집은 금액을 낮춥니다. 급하지 않은 집은 높게 부릅니다. 평균은 오르는데 싼 전세도 같이 나오는 것은 이 때문입니다.'))
o.append(NOTE('금액 차이는 같은 단지 같은 면적 같은 달 전세가 5건 이상일 때 아래위 10%씩을 빼고 낮은 계약과 높은 계약의 차이를 구해 평균'))

o.append(H('신축아파트 전세 들어갈때, 입주장 끝 무렵에는 월세가 늘어납니다'))
o.append(P(f'첫 달 계약은 83%가 전세였습니다. 넷째 달에는 68%, 여섯째 달에는 {HL("56%")}로 줄었습니다. 나머지는 월세와 반전세입니다.'))
o.append(IMG('nangman_ipjujang_jeonse_4_wolse.png','신축아파트 전세 · 계약 가운데 전세와 월세 비중'))
o.append(P(f'전세 세입자를 못 구한 집주인은 보증금을 낮추고 월세를 받습니다. 그래서 입주장 끝 무렵에는 월세 계약이 많아집니다. {B("전세로 들어갈 집을 찾는다면 첫 석 달에 고를 수 있는 집이 가장 많습니다.")}'))

o.append(H('입주장 전세가율, 매매가 있는 11곳은 49~73%였습니다'))
o.append(P('올해 같은 면적 매매가 3건 이상 나온 곳은 11곳입니다. 같은 단지 같은 면적 매매 중앙값과 전세 중앙값을 나눈 값입니다.'))
o.append(P(f'김해 대청천 에피트 59㎡가 {HL("73%")}로 가장 높았습니다. 파주 운정중앙역 우미린 더센텀 84㎡가 72%, 오산 세교파라곤 84㎡가 71%입니다. 부산 초읍 하늘채 포레스원 59㎡는 49%로 가장 낮았습니다.'))
o.append(P('초읍 하늘채 포레스원 59㎡는 매매 5억 1천만원, 전세 2억 5,200만원입니다. 집주인이 전세를 놓아도 2억 6천만원 가까이를 직접 마련해야 했습니다. 세교파라곤 84㎡는 매매 4억 9천만원, 전세 3억 5천만원으로 그 차이가 1억 4천만원입니다.'))

o.append(H('입주 아파트 전세놓는방법, 내린 단지는 처음 금액이 높았습니다'))
o.append(VS(('롯데캐슬 넥스티엘 84㎡','인천 검단 · 첫 계약 3월',['3월 4억 5천만원','6월 4억 500만원','석 달 만에 4,500만원 내림'],D),
            ('칸타빌 더스위트 84㎡','인천 검단 · 첫 계약 3월',['3~4월 3억원 안팎','6월 3억원','9월 3억 3천만원으로 오름'],A)))
o.append(P('두 단지는 처음에 1억 5천만원 차이였습니다. 석 달 뒤에는 1억 500만원으로 줄었습니다. 이천 힐스테이트 이천역 1단지도 둘째 달 3억 6,500만원에서 셋째 달 3억 2천만원으로 내렸습니다.'))
o.append(P(f'{B("입주장 첫 금액이 옆 단지보다 크게 높으면 석 달 안에 옆 단지 쪽으로 내려왔습니다.")} 낮게 시작한 단지는 넷째 달부터 올랐습니다.'))

o.append(H('신축 입주장, 계약이 몰리는 석 달은 집 고치는 일정도 몰립니다'))
o.append(P(f'첫 석 달에 50곳 계약의 {HL("45%")}가 몰렸습니다. 이 석 달은 이삿짐, 입주청소, 줄눈, 중문 시공 날짜도 같이 몰립니다.'))
o.append(P('전세를 놓는 집주인은 세입자가 들어오기 전 빈집일 때 공사를 끝내는 편이 일정 잡기가 쉽습니다. 세입자가 들어온 뒤에는 날짜를 세입자와 맞춰야 합니다. 공정 순서는 「'+LK('https://blog.naver.com/champion_chart/224437487580','신축 입주 순서, 먼지 나는 일을 먼저 하고 청소는 그다음, 이삿짐은 맨 마지막입니다')+'」에 있습니다.'))
o.append(P('입주장 전세로 들어가는 세입자는 중문을 직접 다는 경우가 많습니다. 벽에 구멍을 내지 않는 무타공 중문도 있습니다. 「'+LK('https://blog.naver.com/champion_chart/224431136138','전세집 중문, 집주인 동의 받고 달거나 무타공으로 달 수 있고 철거 비용은 10만~30만원입니다')+'」에 정리했습니다.'))
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:1px solid #C7D6E6;border-bottom:1px solid #C7D6E6;padding:14px 18px;"><span style="font-size:19px;color:{D};">열쇠를 받는 날 입주청소와 새집증후군을 하루 차이로 묶으면 34평(84㎡) {B("71만 4천원")}입니다 → '+LK('https://blog.naver.com/champion_chart/224451151010','입주청소 새집증후군 묶음')+'</span></td></tr></table>\n<p><br></p>\n')
o.append(NOTE('자료: 국토교통부 아파트 매매·전월세 실거래(2026년 10월 24일 받은 자료) · 단지 이름은 실거래 자료에 적힌 이름을 띄어 씀 · 첫 계약 달은 그 단지 첫 전월세 계약이 신고된 달이라 실제 입주 시작보다 한두 달 이를 수 있음 · 공공·민간 임대 단지와 계약이 한 달에 몰려 금액이 한 가지인 단지는 뺌'))
o.append(f'''<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:5px solid {A};background-color:#F4F6F9;padding:20px 22px;"><p style="font-size:21px;font-weight:700;color:{A};">입주장 단지 앞 중개사무소 인터뷰를 받습니다</p>
<p><br></p>
<p style="font-size:20px;color:#333;line-height:1.7;">입주장 전세 분위기, 잔금 날 집주인과 세입자가 묻는 것 같은 현장 이야기를 들려주시면 블로그에 무료로 소개합니다. 원고는 올리기 전에 먼저 보여 드립니다.</p>
<p style="font-size:20px;color:#333;line-height:1.7;">▸ 신청: 문자 010-2882-8165 (사무소 이름 · 편한 요일)</p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224449575744','부동산 홍보방법, 입주 단지 중개사무소를 찾아가 인터뷰하고 그 단지 글마다 사무소를 무료로 소개합니다 ›')}</p>
</td></tr></table>
<p><br></p>
''')
o.append(f'<p style="font-size:27px;font-weight:700;color:{D};">함께 보면 좋은 글</p>\n<p><br></p>\n')
for t,u,s in [('신검단중앙역 센트레빌 전세, 같은 역 새 아파트 입주 때 84㎡는 3억이었습니다','https://blog.naver.com/dong_jin_kim/224451824958','검단 새 아파트 입주장 전세와 2년 뒤 갱신 금액'),
 ('상도동 아파트 전세, 새 아파트 입주 때는 옆 단지보다 1억 낮았습니다','https://blog.naver.com/dong_jin_kim/224451832221','서울 새 아파트 입주장 전세를 옆 구축과 비교'),
 ('대치동 전세, 개포 입주 때는 내렸는데 은마 이주는 반대입니다','https://blog.naver.com/dong_jin_kim/224413536755','큰 입주장이 옆 동네 전세에 준 영향'),
 ('신축아파트 입주비용, 6억 집은 취득세 660만원에 청소 · 새집증후군 71만원','https://blog.naver.com/dong_jin_kim/224451684611','잔금 날 함께 나가는 돈'),
 ('경기도 전세, 31개 시군 전세가율과 갭투자 필요 금액을 세웠습니다','https://blog.naver.com/dong_jin_kim/224401817897','경기도 시군별 전세가율'),
 ('오산역 금강펜테리움 전세, 먼저 입주한 세교파라곤 84㎡는 3억 2천에서 넉 달 뒤 3억 8천이 됐습니다 (발행 예정)','','10월 입주하는 오산 730세대 단지의 전세')]:
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
<span style="font-size:19px;font-weight:700;color:{D};">입주장에 들어간다면</span><br><br>
''')
for t,u,s in [('학산 한신더휴 입주, 청소 다음 날 새집증후군을 하고 전후 수치를 보여 드립니다','https://blog.naver.com/champion_chart/224452055989','포항 학산 한신더휴 입주 집 청소 · 새집증후군 순서'),
 ('신검단중앙역 센트레빌 입주지정기간, 언제 들어가도 줄눈 다음에 입주청소','https://blog.naver.com/champion_chart/224448364385','검단 입주지정기간 안에 끝낼 일'),
 ('입주청소 추가금 요구 244건, 계약 전 확인 6가지와 현장 대처 순서','https://blog.naver.com/champion_chart/224455976621','입주장에 몰리는 청소 예약에서 추가금 피하기')]:
    o.append(f'<a href="{u}" style="font-size:19px;font-weight:700;color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n<span style="font-size:16px;color:#7A8590;">{s}</span><br><br>\n')
o.append('</td></tr></table>\n<p><br></p>\n')
tags='#입주장전세 #입주장 #신축입주장전세 #입주장시기 #입주장전세가율 #입주장전세급매 #신축아파트전세 #입주아파트전세 #새아파트전세 #세교파라곤전세 #학산한신더휴 #신검단전세 #낭만부동산'
o.append(f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">\n<tr><td style="background-color:#F4F6F9;border-left:3px solid {A};padding:16px 18px;">\n<span style="font-size:16px;color:#8A8578;">태그</span><br>\n<span style="font-size:18px;color:#555;line-height:1.9;">{tags}</span>\n</td></tr>\n</table>\n')
open('post.html','w').write(''.join(o)); print(len(''.join(o)))
