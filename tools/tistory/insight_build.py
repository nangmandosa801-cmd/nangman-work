#!/usr/bin/env python3
"""티스토리 talk7921 「공법 · 용어 + 실제 사례」 인사이트 글 꾸러미 (11/10)
python3 insight_build.py [--up]   → /home/claude/w/ts_pages/<slug>/index.html · /home/claude/nangman-work/ts_pkg/<slug>.json
그림은 insight_viz.py(viz2d · 평평한 2D)가 만든다. 글마다 대표 + 2장. --up 이면 gas.py image 로 올리고 urls.json 에 적는다."""
import json, os, re, sys, subprocess, datetime as D
R = '/home/claude/w/ts_pages'; PKG = '/home/claude/nangman-work/ts_pkg'
P = lambda t: f'<p style="font-size:17px;line-height:1.85;color:#22324A;margin:10px 0">{t}</p>'
H2 = lambda t: f'<h2 style="font-size:24px;color:#1F3864;border-left:6px solid #2E5C8A;padding-left:12px;margin:38px 0 12px">{t}</h2>'
H3 = lambda t: f'<h3 style="font-size:19px;color:#1F3864;margin:24px 0 6px">{t}</h3>'
IMG = lambda n: '<p style="margin:16px 0;text-align:center">{{IMG:%d}}</p>' % n
TOP = lambda t: f'<p style="font-size:14px;color:#6B7A90;margin:0 0 6px">{t}</p>'
def NOTE(lines): return '<div style="background:#F4F7FB;border:1px solid #D5DDE8;border-radius:8px;padding:14px 16px;margin:26px 0;font-size:14px;line-height:1.8;color:#4A5A72"><b>NOTE</b><br>' + '<br>'.join('· ' + l for l in lines) + '</div>'
def BOX(t): return f'<div style="background:#FFF6EC;border-left:6px solid #E8833A;border-radius:6px;padding:14px 18px;margin:18px 0;font-size:18px;line-height:1.8;color:#22324A">{t}</div>'
def TABLE(head, rows):
    th = ''.join(f'<th style="border:1px solid #1F3864;padding:10px 6px;background:#1F3864;color:#fff;font-size:15px;text-align:center">{h}</th>' for h in head)
    tr = ''
    for i, r in enumerate(rows):
        bg = '#FFFFFF' if i % 2 == 0 else '#F4F7FB'
        tr += '<tr>' + ''.join(f'<td style="border:1px solid #D5DDE8;padding:9px 8px;text-align:{"left" if j else "center"};font-size:15px;line-height:1.6;background:{bg}{";font-weight:bold" if j == 0 else ""}">{c}</td>' for j, c in enumerate(r)) + '</tr>'
    return f'<table style="width:100%;border-collapse:collapse;table-layout:auto;margin:14px 0"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

SMALL = lambda lines: '<p style="font-size:13px;line-height:1.7;color:#8B95A1;margin:34px 0 0;border-top:1px solid #E5E8EB;padding-top:14px"><b>근거</b> · ' + ' / '.join(lines) + '</p>'

# ================================================================ 글 1 · 환지처분 (11/10 다시 씀: 질문 하나 + 답 하나 · 쉬운 말 · 조문은 맨 끝 「근거」에만)
def hwanji():
    B = []
    B.append(TOP('2026.11.11 · 낭만 부동산 분석 플랫폼'))
    B.append(P('<b>입주 16년째인데 내 집 땅은 아직 내 이름이 아닙니다.</b> 고양 덕이지구 5,159세대 이야기입니다.'))
    B.append(P('이유는 하나입니다. 「환지처분」이라는 마지막 절차가 안 끝났습니다. 이 절차가 끝나야 아파트 땅 등기가 나옵니다.'))
    B.append(IMG(1))
    B.append(H2('땅 등기가 없으면 무슨 일이 생기나요?'))
    B.append(P('등기부에 건물만 있고 땅이 없습니다. 은행은 이런 집을 담보로 잡기 어려워합니다.'))
    B.append(P('팔 때도 사려는 사람이 꺼립니다. 덕이지구 주민들은 집을 팔 때, 대출받을 때, 물려줄 때마다 어려움을 겪었습니다.'))
    B.append(P('땅 주인으로 확정되지도 않았는데 땅 세금은 해마다 냈습니다. 아파트는 2011년 3월부터 사람이 살았습니다.'))
    B.append(H2('환지처분이 왜 16년이나 걸리나요?'))
    B.append(P('① 이 동네는 땅 주인에게 돈 대신 새 땅을 돌려주는 방식으로 개발했습니다. 「환지 방식」이라고 부릅니다.'))
    B.append(P('② 새 땅의 주인을 한날에 확정하는 절차가 환지처분입니다. 그날이 지나야 땅 등기를 할 수 있습니다.'))
    B.append(P('③ 환지처분은 동네 전체 공사가 끝나고 검사를 통과해야 할 수 있습니다. 아파트 한 단지가 기준이 아닙니다.'))
    B.append(P('④ 아파트는 그 전에 다 지어집니다. 사람도 들어와 삽니다. 땅 등기만 뒤에 남습니다.'))
    B.append(P('⑤ 그래서 동네 끝의 도로 하나, 도랑 하나가 정리되지 않으면 모든 집의 땅 등기가 멈춥니다.'))
    B.append(P('덕이지구를 막은 것은 358㎡짜리 도랑 땅이었습니다. 1982년에 도면 정리가 빠져 주인이 둘로 겹쳐 있었습니다. 5,159세대가 이 땅 하나에 걸렸습니다.'))
    B.append(P('2026년 11월 3일 국민권익위원회 조정으로 합의가 났습니다. 보상금을 고양시가 70%, 조합이 30% 냅니다.'))
    B.append(IMG(2))
    B.append(P('등기가 바로 나오지는 않습니다. 검사, 환지처분, 등기 신청이 차례로 남았습니다. 조합장은 절차가 계획대로 가면 2027년 중반으로 내다봤습니다.'))
    B.append(P('막힌 곳은 아파트 담장 밖입니다. 집을 산 사람이 풀 수 있는 문제가 아닙니다.'))
    B.append(H2('분양 받기 전에 무엇을 보면 되나요?'))
    B.append(P('입주자모집공고 뒤쪽 「유의사항」에서 낱말 세 개를 찾습니다. 수십 쪽짜리 공고도 낱말 찾기로 1분이면 됩니다.'))
    B.append(TABLE(['찾을 낱말', '나오면 무슨 뜻인가'], [
        ['환지', '땅 등기가 동네 전체 공사가 끝난 뒤에 나오는 곳입니다.'],
        ['체비지', '아파트가 선 땅이 공사비를 대려고 떼어 둔 땅입니다. 환지처분 다음 날에야 주인이 확정됩니다.'],
        ['대지권', '「입주 후 상당 기간 지연될 수 있음」 같은 말이 붙었는지 봅니다.'],
    ]))
    B.append(P('실제로 있는 문장입니다. 2026년 11월 청약을 받은 평택 한화포레나 지제역(1,098가구) 공고에는 「등기 이전 불가 등의 문제가 발생할 수 있다」는 말이 들어갔습니다. 지하차도 공사비를 조합이 낼지 다투는 중입니다.'))
    B.append(P('낱말이 나왔다고 그 단지가 꼭 늦어지는 것은 아닙니다. 대신 물어볼 것이 하나 생깁니다. 분양 사무실과 시청에 <b>「지구 준공 예정일이 언제입니까」</b>라고 물으세요. 땅 등기는 그 날짜보다 먼저 나오지 않습니다.'))
    B.append(SMALL([
        '도시개발법 제34조 · 제36조 · 제40조 · 제42조 · 제43조 · 제51조(국가법령정보센터 2026.11.10 확인)',
        '고양 덕이지구: 서울신문 2025.10.3, 경기일보 2026.3.17, 이투데이 2026.11.3, 노컷뉴스 2026.11.3',
        '평택 영신지구: 뉴스필드 2026.11.4, 비즈워치 2026.11.6',
        '제도를 설명한 글입니다. 특정 단지의 청약 · 계약을 권하거나 말리지 않습니다.',
    ]))
    return dict(slug='hwanji-cheobun', title='새 아파트인데 등기가 안 나온다, 왜 그럴까요?',
                tags='환지처분,환지처분이란,환지 방식,대지권 미등기,체비지,입주자모집공고 유의사항,도시개발사업 등기',
                alts=['환지처분이란', '환지처분 지연 고양 덕이지구 5,159세대 입주 16년째 대지권 미등기', '환지처분 남은 단계 · 준공검사 환지처분 등기'],
                at=D.datetime(2026, 11, 11, 13, tzinfo=D.timezone(D.timedelta(hours=9))), body=B, nimg=3)

# ================================================================ 글 2 · 토지거래허가구역 (11/10 다시 씀)
def toheo():
    B = []
    B.append(TOP('2026.11.12 · 낭만 부동산 분석 플랫폼'))
    B.append(P('<b>토지거래허가구역 아파트를 사면 2년 동안 직접 살아야 합니다.</b> 전세를 주면 해마다 집값의 7%를 냅니다.'))
    B.append(P('10억원에 산 집이면 한 해 7,000만원입니다. 「전세 끼고 사 두기」가 안 되는 이유입니다.'))
    B.append(IMG(1))
    B.append(H2('전세를 주면 실제로 어떻게 되나요?'))
    B.append(P('구청이 먼저 문서를 보냅니다. 3개월 안에 들어가 살라는 내용입니다.'))
    B.append(P('그래도 안 들어가면 집값의 7%가 나옵니다. 「이행강제금」이라는 돈입니다. 고칠 때까지 1년에 한 번씩 다시 나옵니다.'))
    B.append(P('사 놓고 비워 두면 더 큽니다. 10%입니다. 산 날부터 2년이 지나면 더는 나오지 않습니다.'))
    B.append(P('세입자가 이미 사는 집은 길이 하나 있습니다. 집 없는 사람이 사면 세입자 계약이 끝날 때까지 입주를 미룰 수 있습니다. 신청은 2027년 12월 31일까지입니다. 미룬 뒤에는 들어가서 2년을 살아야 합니다.'))
    B.append(TABLE(['이런 경우', '2년 살아야 하나요'], [
        ['법원 경매로 산 집', '아닙니다. 허가를 받지 않는 거래입니다.'],
        ['새 아파트 분양', '이 제도로는 아닙니다. 분양에는 다른 법의 거주 의무가 따로 붙을 수 있습니다.'],
        ['해외 이주 · 군 복무 · 재해', '의무가 풀립니다.'],
        ['직장 이동 · 자녀 학교', '정해진 사유가 아닙니다. 구청 심사를 받아야 합니다.'],
    ]))
    B.append(H2('묶인 뒤 서울 거래는 어떻게 됐나요?'))
    B.append(P('지정 뒤 8일 동안 서울 4개 구 계약은 41건이었습니다. 그 앞 23일은 2,642건입니다.'))
    B.append(IMG(2))
    B.append(P('강남 · 서초 · 송파 · 용산이 2025년 3월 24일에 묶였습니다. 사람들은 그 전날까지 계약서를 서둘러 썼습니다.'))
    B.append(P('거래가 사라진 것은 아닙니다. 서울 나머지 21개 구는 2025년 10월에 묶였습니다. 묶이기 직전 달 계약이 7,306건, 일곱 달 뒤인 2026년 5월이 7,376건입니다.'))
    B.append(P('21개 구 거래는 돌아왔습니다. 다만 2년 살 사람만 사는 시장이 됐습니다.'))
    B.append(H2('하남은 지금 어떤가요?'))
    B.append(P('하남 아파트는 시 전체가 허가구역입니다. 기한은 2026년 12월 31일입니다. 경기도가 연장을 검토하고 있습니다.'))
    B.append(P('땅은 따로입니다. 2026년 11월 3일부터 감북 · 감일 · 미사동 일원 7.17㎢만 남았습니다. 그 전에는 70.14㎢였습니다. 남은 곳은 2029년 11월 2일까지입니다.'))
    B.append(P('이 구역에서 밭을 사면 2년 동안 직접 농사를 지어야 합니다.'))
    B.append(P('계약 전에 날짜 하나만 확인하세요. <b>세입자 계약이 끝나는 날</b>입니다. 원칙은 허가를 받고 4개월 안에 들어가 사는 것입니다. 그 안에 집이 비지 않으면 입주 유예를 받을 수 있는지 구청 토지거래허가 담당에게 먼저 물어야 합니다.'))
    B.append(SMALL([
        '부동산 거래신고 등에 관한 법률 제11조 · 제14조 · 제17조 · 제18조, 같은 법 시행령 제11조 · 제14조 · 제16조(국가법령정보센터 2026.11.10 확인)',
        '입주 유예: SBS Biz 2026.9.17 · 서울신문 2025.10.16',
        '하남 · 경기: 산업일보 2026.11.4, SBS Biz 2026.11.3',
        '서울 지정: 뉴시스 2025.3.19, 서울신문 2025.10.16',
        '거래 건수는 국토교통부 아파트 매매 실거래 자료를 직접 셌습니다(계약일 기준 · 취소된 거래 뺌). 건수에는 대출 규제 같은 다른 정책의 영향도 섞여 있습니다.',
        '유예 요건과 허가 기준은 구역 공고와 구청 안내가 우선입니다.',
    ]))
    return dict(slug='toheo-silgeoju', title='토지거래허가구역 실거주 2년, 안 지키면 어떻게 되나요?',
                tags='토지거래허가구역 실거주,토지거래허가구역 실거주 의무,토지거래허가구역 전세,토지거래허가 이행강제금,하남 토지거래허가구역,서울 토지거래허가구역 거래량,토허제 실거주',
                alts=['토지거래허가구역 실거주 의무', '토지거래허가구역 실거주 의무 기간 2년 · 전세 주면 7% · 비워 두면 10%', '서울 토지거래허가구역 지정 전 23일 2,642건 · 지정 뒤 8일 41건'],
                at=D.datetime(2026, 11, 12, 13, tzinfo=D.timezone(D.timedelta(hours=9))), body=B, nimg=3)

BAN = ['고요', '최고', '갈라', '갈렸', '갈랐', '갈리', '적혀 있습니다', '이라고 적습니다', '먼저 하나', '링크', '010-', '낭만 인테리어', '낭만부동산']
def build(a, up):
    d = f"{R}/{a['slug']}"; uj = f'{d}/urls.json'
    urls = json.load(open(uj)) if os.path.exists(uj) else []
    if up or len(urls) != a['nimg']:
        urls = []
        for i in range(1, a['nimg'] + 1):
            o = subprocess.run(['python3', '/home/claude/helper/gas.py', 'image', f'{d}/{i:02d}.jpg'], capture_output=True, text=True).stdout
            urls.append(json.loads(o)['url'])
        json.dump(urls, open(uj, 'w'))
    html = '\n'.join(a['body'])
    txt = re.sub(r'<[^>]+>|\{\{IMG:\d\}\}', '', html)
    ban = [b for b in BAN if b in txt] + [m for m in re.findall(r'(?<![가-힣])갈[가-힣]', txt)]
    local = html
    for i in range(1, a['nimg']): local = local.replace('{{IMG:%d}}' % i, f'<img src="{i+1:02d}.jpg" alt="{a["alts"][i]}" style="max-width:100%">')
    open(f'{d}/index.html', 'w').write(f'<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>{a["title"]}</title></head><body style="max-width:860px;margin:0 auto;padding:16px">\n<!-- 제목: {a["title"]} -->\n<!-- 태그: {a["tags"]} -->\n<!-- 대표 이미지: 01.jpg -->\n<h1>{a["title"]}</h1>\n{local}\n</body></html>')
    pk = dict(slug=a['slug'], title=a['title'], html=html, tags=a['tags'], category=1373246, imgs=urls, thumb=0, at=int(a['at'].timestamp()), alts=a['alts'])
    json.dump(pk, open(f"{PKG}/{a['slug']}.json", 'w'), ensure_ascii=False)
    return dict(slug=a['slug'], title=a['title'], chars=len(re.sub(r'\s', '', txt)), chars_sp=len(txt), imgs=len(urls), ph=len(re.findall(r'\{\{IMG:\d\}\}', html)), at=pk['at'], ban=ban)
DRIVE = '블로그/협업/4_어사이드/티스토리/원고'
def aside(a):
    """어사이드용: 드라이브 「…/티스토리/원고/<slug>/」 에 index.html(빨간 「▼ 사진 NN.jpg」 표시) + 01.jpg~ 를 올린다."""
    import base64; sys.path.insert(0, '/home/claude/helper'); from gas import call
    d = f"{R}/{a['slug']}"; html = '\n'.join(a['body'])
    for i in range(1, a['nimg']):
        html = html.replace('<p style="margin:16px 0;text-align:center">{{IMG:%d}}</p>' % i,
                            f'<p style="color:#E03131;font-weight:bold;font-size:17px;margin:16px 0">▼ 사진 {i+1:02d}.jpg</p>')
    when = a['at'].strftime('%Y-%m-%d %H:%M')
    top = ''.join(f'<p style="color:#E03131;font-size:15px;margin:2px 0">{t}</p>' for t in
                  [f'제목 칸: {a["title"]}', f'태그: {a["tags"]}', '카테고리: 부동산 시세', f'예약: {when}', '대표 이미지: 01.jpg'])
    out = f'<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>{a["title"]}</title></head><body style="max-width:860px;margin:0 auto;padding:16px">\n{top}\n<hr>\n{html}\n</body></html>'
    open(f'{d}/aside.html', 'w').write(out)
    call('fput', path=f"{DRIVE}/{a['slug']}", name='index.html', mime='text/html', b64=base64.b64encode(out.encode()).decode())
    for i in range(1, a['nimg'] + 1):
        call('fput', path=f"{DRIVE}/{a['slug']}", name=f'{i:02d}.jpg', mime='image/jpeg', b64=base64.b64encode(open(f'{d}/{i:02d}.jpg', 'rb').read()).decode())
    return dict(drive=f"{DRIVE}/{a['slug']}", files=1 + a['nimg'])
if __name__ == '__main__':
    for f in (hwanji, toheo):
        a = f(); r = build(a, '--up' in sys.argv)
        if '--aside' in sys.argv: r.update(aside(a))
        print(json.dumps(r, ensure_ascii=False))
