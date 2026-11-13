#!/usr/bin/env python3
"""구글 블로그 「낭만 부동산」 표 페이지 — 연봉별 주택담보대출 한도표 (찾아보는 곳 · 매달 갱신)
사용: python3 gblog.py            → gblog.html · gblog.txt 만 만든다
      python3 gblog.py --pub "2026-11-16T09:00:00+09:00"   → 새 글 예약(이미 올린 글이면 같은 글을 patch)
      python3 gblog.py --pub      → 이미 올린 글 본문만 고침(매달 갱신 · 네이버 글 주소가 생기면 NAVER 에 넣고 다시)
기록: /home/claude/tools/tistory/gblog_pages.json 의 'salary_table'
금리 · 스트레스 금리가 바뀌면 ana.py 의 BASE · STRESS 와 아래 RATE_NOTE 를 고치고 다시 돌린다."""
import sys, os, json, math, html as H, datetime, re
sys.path.insert(0, '/home/claude/helper')
D = os.path.dirname(os.path.abspath(__file__))
J = json.load(open(os.path.join(D, 'ana.json'))); R = {r['inc']: r for r in J['rows']}
BASE, STRESS, DSR, CAP, N = J['base'], J['stress'], J['dsr'], J['cap'], J['years'] * 12
NAVER = 'https://blog.naver.com/dong_jin_kim'          # 네이버 원문이 발행되면 글 주소로 바꾼다
NAVER_T = '낭만 부동산 분석 플랫폼 네이버 블로그'
TITLE = '연봉별 주택담보대출 한도표, 2026년 11월 수도권 기준'
RATE_NOTE = '5대 은행 주택담보대출 금리는 2026년 11월 10일 기준 고정형 연 4.41~6.39%, 변동형 연 4.42~6.48%입니다.'
def pv(pm, rate):
    r = rate / 100 / 12; return pm * (1 - (1 + r) ** -N) / r
def pay(loan, rate):
    r = rate / 100 / 12; return loan * r / (1 - (1 + r) ** -N)
def loan(inc, ratio, base=BASE):
    return min(math.floor(pv(inc * DSR / 12, base + STRESS * ratio) / 10) * 10, CAP)
def uk(v):
    a, b = divmod(int(round(v)), 10000)
    return f'{a}억' if b == 0 else (f'{b:,}만' if a == 0 else f'{a}억 {b:,}만')
c = lambda v: uk(v) + ('(한도)' if v >= CAP else '')
TH = 'background:#1F3864;color:#fff;padding:9px 8px;font-size:15px;border:1px solid #1F3864;text-align:center'
TD = 'padding:8px;font-size:15px;border:1px solid #D5DDE8;text-align:center;color:#22324A'
def table(head, rows, hl=()):
    h = ''.join(f'<th style="{TH}">{H.escape(x)}</th>' for x in head); body = ''
    for i, r in enumerate(rows):
        bg = '#EAF1FB' if i in hl else ('#F7F9FC' if i % 2 else '#FFFFFF')
        body += '<tr>' + ''.join(f'<td style="{TD};background:{bg}' + (';font-weight:bold' if j == 0 or i in hl else '') + f'">{H.escape(str(x))}</td>' for j, x in enumerate(r)) + '</tr>'
    return f'<table style="width:100%;border-collapse:collapse;margin:14px 0"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'
P = lambda t: f'<p style="font-size:17px;line-height:1.85;color:#22324A;margin:10px 0">{t}</p>'
H2 = lambda t: f'<h2 style="font-size:24px;color:#1F3864;border-left:6px solid #2E5C8A;padding-left:12px;margin:38px 0 12px">{H.escape(t)}</h2>'
NOTE = lambda t: f'<div style="background:#F4F7FB;border:1px solid #D5DDE8;border-radius:8px;padding:14px 16px;margin:26px 0;font-size:14px;line-height:1.8;color:#4A5A72">{t}</div>'
today = datetime.datetime.now()
B = []; T = [f'제목: {TITLE}', '']   # B = html · T = 검수용 글자
def p(t): B.append(P(t)); T.append(re.sub(r'<[^>]+>', '', t.replace('<br>', '\n'))); T.append('')
def h2(t): B.append(H2(t)); T.append('[소제목] ' + t); T.append('')
def tb(head, rows, hl=()):
    B.append(table(head, rows, hl)); T.append('[표]'); T.append(' | '.join(head)); T.extend(' | '.join(map(str, r)) for r in rows); T.append('[/표]'); T.append('')
B.append(f'<p style="font-size:14px;color:#6B7A90;margin:0 0 6px">갱신 {today.year}.{today.month:02d}.{today.day:02d} · 수도권 · 은행 · 연 {BASE}% · 30년 · 다른 대출 없음</p>')
p(f'연봉만 알면 은행에서 빌릴 수 있는 돈을 바로 찾는 표입니다. <b>세전 연봉 6천만원이면 5년 주기형으로 {uk(R[6000]["주기형"])}원, 변동형으로 {uk(R[6000]["변동형"])}원까지 나옵니다.</b> 수도권 한도 6억원을 다 빌리려면 연봉이 {uk(J["cap_income"]["주기형"])}원을 넘어야 합니다.')
p('표의 값은 은행 DSR 40%와 수도권 스트레스 금리 3.0%포인트를 넣어 계산했습니다. 금리 유형에 따라 한도가 달라지니 세 칸을 같이 보세요.')

h2('연봉별 주택담보대출 한도는 얼마인가요?')
p(f'연 {BASE}% · 30년 기준으로 세전 연봉에 5년 주기형은 {J["mult"]["주기형"]:.1f}, 혼합형은 {J["mult"]["혼합형"]:.1f}, 변동형은 {J["mult"]["변동형"]:.1f}을 곱한 값이 한도입니다. 아래 표에서 내 연봉 줄을 찾으면 됩니다.')
incs = list(range(3000, 15001, 500)); rows = []
for i in incs: rows.append((uk(i), c(loan(i, 1.0)), c(loan(i, 0.8)), c(loan(i, 0.4))))
tb(['세전 연봉', '변동형', '혼합형', '5년 주기형'], rows, hl=[incs.index(6000), incs.index(10000)])
assert loan(6000, 0.4) == R[6000]['주기형'] and loan(10000, 1.0) == R[10000]['변동형']

h2('금리가 다르면 한도는 얼마나 달라지나요?')
l45, l55 = loan(6000, 0.4, 4.5), loan(6000, 0.4, 5.5)
p(f'금리가 1%포인트 오르면 한도는 10%쯤 줄어듭니다. 연봉 6천만원의 5년 주기형 한도는 연 4.5%에서 {uk(l45)}원, 연 5.5%에서 {uk(l55)}원입니다.')
rs = (4.5, 5.0, 5.5, 6.0); rows = [(uk(i), *[c(loan(i, 0.4, b)) for b in rs]) for i in (4000, 5000, 6000, 7000, 8000, 10000)]
tb(['세전 연봉', *[f'연 {b}%' for b in rs]], rows, hl=[2])
p(RATE_NOTE)

h2('그 대출로 살 수 있는 집값은 얼마인가요?')
p(f'집값의 70%를 빌린다면 연봉 6천만원은 {uk(R[6000]["price"])}원짜리 집까지 닿습니다. 2026년 8~10월 수도권 84㎡ 실거래 {J["n84"]:,}건 가운데 {R[6000]["s84"]}%가 이 값 아래로 팔렸습니다.')
rows = [(uk(i), uk(R[i]['price']), uk(R[i]['own']), f"{R[i]['pay']:.0f}만", f"{R[i]['s84']}%", f"{R[i]['s59']}%") for i in (3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)]
tb(['세전 연봉', '닿는 집값', '필요한 내 돈', '한 달 갚는 돈', '84㎡ 닿는 거래', '59㎡ 닿는 거래'], rows, hl=[3])
p('닿는 집값은 5년 주기형 한도를 0.7로 나눈 값입니다. 생애최초 구입자와 규제지역 밖에서 집을 사는 무주택자가 집값의 70%까지 빌릴 수 있습니다. 서울 전체와 경기 15곳 같은 규제지역에서는 생애최초가 아니면 40%까지만 나옵니다.')

h2('연봉 6천만원으로 닿는 84㎡는 어느 지역에 많나요?')
t = R[6000]['top84']
p(f'{t[0]["sgg"]}가 {t[0]["k"]}건으로 가장 많고, {t[1]["sgg"]} {t[1]["k"]}건, {t[2]["sgg"]} {t[2]["k"]}건 순서입니다. {uk(R[6000]["price"])}원 아래로 팔린 84㎡ {R[6000]["k84"]:,}건을 지역별로 센 결과입니다.')
tb(['지역', '닿는 84㎡ 거래', '그 지역 84㎡ 전체', '닿는 비율'], [(x['sgg'], f"{x['k']}건", f"{x['n']}건", f"{x['share']}%") for x in t], hl=[0])

h2('한도는 어떻게 계산했나요?')
p('연봉의 40%를 한 해에 갚을 수 있는 돈으로 보고, 그 돈으로 30년 동안 갚을 수 있는 원금을 거꾸로 구했습니다. 이때 실제 금리에 스트레스 금리를 얹습니다. 변동형은 3.0%포인트, 혼합형은 2.4%포인트, 5년 주기형은 1.2%포인트입니다.')
p(f'연 {BASE}%로 빌리면 변동형은 {J["rate_dsr"]["변동형"]}%, 혼합형은 {J["rate_dsr"]["혼합형"]}%, 주기형은 {J["rate_dsr"]["주기형"]}%로 계산됩니다. 신용대출이나 카드론이 있으면 한도가 더 줄어듭니다.')

h2('자주 묻는 질문')
p(f'<b>연봉 1억이면 주택담보대출은 얼마까지 되나요?</b><br>변동형 {uk(R[10000]["변동형"])}원, 혼합형 {uk(R[10000]["혼합형"])}원, 5년 주기형 {uk(R[10000]["주기형"])}원입니다. 한도 6억원에는 셋 다 못 미칩니다.')
p(f'<b>6억원을 빌리면 한 달에 얼마를 갚나요?</b><br>연 {BASE}% · 30년 · 매달 같은 돈을 갚는 방식이면 한 달 {J["pay_6eok"]:.0f}만원입니다.')
p('<b>이 표는 언제 바뀌나요?</b><br>은행 금리가 크게 움직이거나 스트레스 금리가 바뀌면 다시 계산합니다. 지금 스트레스 금리 3.0%는 2026년 12월 31일까지 정해진 값입니다.')
p(f'이 표를 이야기로 풀어 쓴 글은 <a href="{NAVER}" style="color:#2E5C8A;font-weight:bold">{NAVER_T}</a>에 있습니다.')
src = ('출처: 금융위원회 2026년 8월 14일 「부동산 시장 안정을 위한 금융 종합대책 ②」(DSR 40% · 수도권 한도 6억원 · 규제지역 LTV 40% · 비규제지역 70%) · 은행연합회 2026년 6월 30일(수도권 스트레스 금리 3.0% · 12월 31일까지) · '
       '금융위원회 2025년 5월 20일(혼합형 80% · 5년 주기형 40% 적용) · 금리: 파이낸셜포스트 2026년 11월 10일 · 실거래: 국토교통부 아파트 매매(서울 · 경기 · 인천 · 2026년 8~10월 계약 · 해제 · 직거래 뺌 · 84㎡ '
       f'{J["n84"]:,}건 · 59㎡ {J["n59"]:,}건) · 10만원 아래 버림 · 실제 한도는 은행 심사에서 정해집니다.')
B.append(NOTE(src)); T.append(src)
html_ = '\n'.join(B)
open(os.path.join(D, 'gblog.html'), 'w', encoding='utf8').write(html_)
open(os.path.join(D, 'gblog.txt'), 'w', encoding='utf8').write('\n'.join(T) + '\n')
print(json.dumps({'title': TITLE, 'html': len(html_), 'rows': len(incs)}, ensure_ascii=False))
if '--pub' in sys.argv:
    from gas import call, BLOG
    BOOK = '/home/claude/tools/tistory/gblog_pages.json'; book = json.load(open(BOOK)) if os.path.exists(BOOK) else {}
    when = next((a for a in sys.argv[2:] if a.startswith('20')), None)
    if 'salary_table' in book:
        r = call('patch', blogId=BLOG['budongsan'], postId=book['salary_table']['postId'], title=TITLE, html=html_); mode = 'patch'
    else:
        kw = dict(blogId=BLOG['budongsan'], title=TITLE, html=html_, labels=['대출', '연봉별 대출한도', '한도표'])
        if when: kw['publishAt'] = when
        r = call('post', **kw); mode = 'post'
    book['salary_table'] = dict(book.get('salary_table', {}), postId=r['id'], url=r.get('url'), title=r.get('title'), status=r.get('status'),
                                published=r.get('published'), updated=today.strftime('%Y-%m-%d %H:%M'))
    json.dump(book, open(BOOK, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(dict(mode=mode, **{k: book['salary_table'].get(k) for k in ('postId', 'url', 'status', 'published')}), ensure_ascii=False))
