import re, subprocess, html, json
def get(u, ua='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'):
    return subprocess.run(['curl','-sL','--max-time','20','-A',ua,u],capture_output=True,text=True).stdout
x = get('https://rss.blog.naver.com/champion_chart.xml')
items = re.findall(r'<item>(.*?)</item>', x, re.S)
rows = []
for it in items:
    t = html.unescape(re.sub(r'<!\[CDATA\[|\]\]>','', re.search(r'<title>(.*?)</title>', it, re.S).group(1))).strip()
    l = re.sub(r'<!\[CDATA\[|\]\]>','', re.search(r'<link>(.*?)</link>', it, re.S).group(1)).strip()
    d = re.search(r'<pubDate>(.*?)</pubDate>', it).group(1)[5:16]
    no = re.search(r'(\d{9,})', l).group(1)
    rows.append((d, no, t))
BUY = r'가격|비용|견적|얼마|업체|만원|시공|설치|교체|수리|공사'
INFO = r'언제|일정|시기|뜻|방법|차이|순서|체크|기간|이유|원인|누가|책임|보험|입주일|사전점검|사전방문'
b = [r for r in rows if re.search(BUY, r[2])]; i = [r for r in rows if re.search(INFO, r[2]) and not re.search(r'가격|비용|견적|얼마|업체|만원', r[2])]
price = [r for r in rows if re.search(r'가격|비용|견적|얼마|만원', r[2])]
print('RSS', len(rows), '편 | 가격·비용·만원이 제목에:', len(price), '| 정보형(언제·일정·책임 등 · 가격 말 없음):', len(i))
for d, no, t in rows: print(d, no, ('₩' if (d,no,t) in price else ' '), t[:58])
json.dump(rows, open('rss.json','w'), ensure_ascii=False)
# 연락 수단: 최신 글 2편 + 블로그 첫 화면
for no in [rows[0][1], rows[5][1]]:
    h = get(f'https://m.blog.naver.com/PostView.naver?blogId=champion_chart&logNo={no}')
    keys = {k: len(re.findall(k, h)) for k in ['tel:', 'open\\.kakao', 'pf\\.kakao', 'talk\\.naver', 'forms\\.gle', 'form\\.naver', 'naver\\.me', 'instagram\\.com', '010-2882', '2882']}
    print('POST', no, 'len', len(h), keys, '| img', len(re.findall(r'se-image-resource|<img ', h)))
h = get('https://m.blog.naver.com/champion_chart')
print('HOME len', len(h), {k: len(re.findall(k, h)) for k in ['talk\\.naver', '톡톡', 'open\\.kakao', 'tel:', 'instagram']})
