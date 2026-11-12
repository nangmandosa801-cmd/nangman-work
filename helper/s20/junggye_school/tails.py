# 낭만 부동산 글 끝 공통 상자 (인터뷰 · 함께 보면 좋은 글 · 꼬리 · 옆 블로그 · 태그)
D='#1F3864'; A='#2E5C8A'
def LK(u,t): return f'<a href="{u}" style="color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a>'
def interview(head,body):
    return f'''<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-left:5px solid {A};background-color:#F4F6F9;padding:20px 22px;"><p style="font-size:21px;font-weight:700;color:{A};">{head}</p>
<p><br></p>
<p style="font-size:20px;color:#333;line-height:1.7;">{body} 원고는 올리기 전에 먼저 보여 드립니다.</p>
<p style="font-size:20px;color:#333;line-height:1.7;">▸ 신청: 문자 010-2882-8165 (사무소 이름 · 편한 요일)</p>
<p style="font-size:19px;font-weight:700;">{LK('https://blog.naver.com/dong_jin_kim/224449575744','부동산 홍보방법, 입주 단지 중개사무소를 찾아가 인터뷰하고 그 단지 글마다 사무소를 무료로 소개합니다 ›')}</p>
</td></tr></table>
<p><br></p>
'''
def related(items):
    o=f'<p style="font-size:27px;font-weight:700;color:{D};">함께 보면 좋은 글</p>\n<p><br></p>\n'
    for t,u,s in items:
        tt=LK(u,t) if u else f'<span style="color:{A};">{t}</span>'
        o+=f'<p style="font-size:19px;font-weight:700;">{tt}<br>\n<span style="font-size:17px;color:#7A8590;">{s}</span></p>\n<p><br></p>\n'
    return o
def platform():
    return f'''<p><br></p>
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
'''
def side(head,items):
    return ''  # 11/10 사용자 「앞으로 인테리어 링크는 올리면 안됨」 — 낭만 인테리어 상자 · 링크 없음
def _side_old(head,items):
    o=f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="background-color:#F4F6F9;border-left:4px solid {A};padding:18px 20px;">\n<span style="font-size:16px;color:#7A8590;letter-spacing:1px;">옆 블로그 · 낭만 인테리어</span><br>\n<span style="font-size:19px;font-weight:700;color:{D};">{head}</span><br><br>\n'
    for t,u,s in items: o+=f'<a href="{u}" style="font-size:19px;font-weight:700;color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a><br>\n<span style="font-size:16px;color:#7A8590;">{s}</span><br><br>\n'
    return o+'</td></tr></table>\n<p><br></p>\n'
def tags(t):
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;">\n<tr><td style="background-color:#F4F6F9;border-left:3px solid {A};padding:16px 18px;">\n<span style="font-size:16px;color:#8A8578;">태그</span><br>\n<span style="font-size:18px;color:#555;line-height:1.9;">{t}</span>\n</td></tr>\n</table>\n'
def save(TITLE,o):
    import re,html as _h
    H_=''.join(o); open('post.html','w').write(H_)
    txt=re.sub(r'<p><br></p>','',H_); txt=re.sub(r'</p>|<br>|</tr>','\n',txt); txt=re.sub(r'<[^>]+>','',txt); txt=_h.unescape(re.sub(r'\n{3,}','\n\n',txt))
    open('post.txt','w').write('[제목]\n'+TITLE+'\n\n'+txt)
