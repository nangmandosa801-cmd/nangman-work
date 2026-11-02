INT=[('224419299693','현관중문 종류, 우리 집 현관엔 뭐가 맞을까요','중문을 처음 알아볼 때 보는 글'),
     ('224420365390','아파트 중문 가격, 32평이라고 정해지지 않습니다','중문 가격이 어디서 달라지는지'),
     ('224422155844','창문 단열필름, 붙이기 전에 우리 집 유리부터 봅니다','겨울 전에 창문 손볼 때')]
def box(c1,c2,c3,bg,line,title_sz=19,link_sz=19,w=None):
    tw=f'width="{w}" style="width:{w}px;' if w else 'width="693" style="width:100%;min-width:693px;'
    s=(f'<table {tw}border-collapse:collapse;"><tr><td style="background-color:{bg};border-left:4px solid {c1};padding:18px 20px;">\n'
       f'<span style="font-size:16px;color:{c3};letter-spacing:1px;">옆 블로그 · 낭만 인테리어</span><br>\n'
       f'<span style="font-size:{title_sz}px;font-weight:700;color:{c2};">이사나 집수리를 앞두고 있다면</span><br><br>\n')
    for n,t,d in INT:
        s+=(f'<a href="https://blog.naver.com/champion_chart/{n}" style="font-size:{link_sz}px;font-weight:700;color:{c1};text-decoration:none;border-bottom:1px solid {line};">{t}</a><br>\n'
            f'<span style="font-size:16px;color:{c3};">{d}</span><br><br>\n')
    return s+'</td></tr></table>\n<p><br></p>\n'
NANGMAN=box('#2E5C8A','#1F3864','#7A8590','#F4F6F9','#C7D6E6')
DOSA=box('#6B5B4C','#3B332C','#8E857A','#FAF8F4','#CFC4B6',link_sz=20,w=740)

BRAND='<p><br></p>\n<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr>\n<td style="border-left:3px solid #1F3864;background-color:#F4F6F9;padding:22px 24px;">\n<p style="font-size:17px;color:#2E5C8A;letter-spacing:1px;">NANGMAN REAL ESTATE PLATFORM</p>\n<p><br></p>\n<p style="font-size:23px;font-weight:700;color:#1F3864;">답이 아니라 방법을 씁니다</p>\n<p><br></p>\n<p style="font-size:19px;color:#333;">실거래를 직접 열어 차이가 얼마인지 세고, 그중 얼마가 무엇 때문인지 분석합니다.</p>\n<p style="font-size:19px;color:#333;">모르는 건 모른다고 씁니다.</p>\n<p><br></p>\n<p><br></p>\n<p style="height:3px;background-color:#1F3864;margin:0;"></p>\n<p style="font-size:16px;color:#2E5C8A;letter-spacing:1px;">블로그 대행 · 데이터 분석</p>\n<p style="font-size:21px;font-weight:700;color:#1F3864;">부동산 블로그 작성에 도움이 필요하시거나</p>\n<p style="font-size:21px;font-weight:700;color:#1F3864;">부동산 데이터 분석 자료가 필요하시면 요청해 주세요</p>\n<p style="height:3px;background-color:#1F3864;margin:0;"></p>\n<p><br></p>\n<p style="font-size:19px;font-weight:700;"><a href="https://blog.naver.com/dong_jin_kim/224377990326" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">부동산을 데이터로 읽고, 공부한 것을 기록합니다 ›</a></p>\n</td></tr></table>\n<p><br></p>\n'
