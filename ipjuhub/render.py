import pickle,re,json,html as H
items,by=pickle.load(open('data.pkl','rb'))
RID=json.load(open('rid.json'));VURL='https://nangmaninterior.tistory.com/54'
S='!important'
def p(t,sz=19,extra=''): return f'<p style="font-size:{sz}px {S};line-height:1.8 {S};margin:0 0 6px {S};{extra}">{t}</p>'
def a(u,t): return f'<a href="{u}" target="_blank" style="color:#2f5d8a {S};">{H.escape(t)}</a>'
def short(t):
    h=t.split(',')[0].strip()
    rest=t.split(',')[1].strip() if ',' in t else ''
    return (h if len(h)<=22 else h[:22]+'…')
NOW='2026-11';M4=['2026-11','2026-12','2027-01','2027-02']
def ymd(k): y,m=k.split('-');return f'{y}년 {int(m)}월'
def block(x):
    from build import datestr
    d,ex=datestr(x)
    seb=f'{x["세대"]:,}세대' if x.get('세대') else ''
    L=[f'<b style="font-size:20px">{H.escape(x["단지"])}</b>',
       f'<span style="color:{"#c0392b" if ex else "#555"};font-weight:{"700" if ex else "400"}">입주 {d}</span>',
       '<span style="color:#555">'+' · '.join(v for v in [H.escape(x.get("지역") or ""),seb] if v)+'</span>']
    NB='낭만 부동산 입주 노트'; ps=[q for q in x['_p'] if q['b']!=NB]; ns=[q for q in x['_p'] if q['b']==NB]
    if ps: L.append('블로그 글 · '+' / '.join(f'<a href="{q["u"]}" target="_blank">{H.escape(q["b"]+": "+short(q["t"]))}</a>' for q in ps[:6]))
    if ns: L.append('<b>입주 노트</b> · '+' / '.join(f'<a href="{q["u"]}" target="_blank">{H.escape(short(q["t"]))}</a>' for q in ns[:3]))
    if not x['_p']: L.append('<span style="color:#8a94a0;">블로그 글 · 준비 중</span>')
    rid=RID.get(x['단지'])
    if rid: L.append(f'<a href="{VURL}#r-{rid}" target="_blank">이 지역 시공팀 보기 (사전점검 · 입주청소 · 줄눈 · 중문 · 결로단열 · 보일러)</a>')
    return f'<p style="font-size:19px {S};line-height:1.75 {S};border-left:4px solid {"#f08a24" if ex else "#c9d4df"} {S};padding:8px 14px {S};margin:0 0 14px {S};background:#fafbfc {S};">'+'<br>'.join(L)+'</p>'
out=[f'<div style="font-family:\'Noto Sans KR\',sans-serif {S};color:#222 {S};max-width:760px {S};margin:0 auto {S};">']
out.append(p('낭만 인테리어 · 입주 아파트 현황',19,f'color:#2f5d8a {S};font-weight:700 {S};'))
out.append(f'<h2 style="font-size:28px {S};color:#1d3d5c {S};line-height:1.45 {S};margin:6px 0 16px {S};">2027년 입주 아파트,<br>월별 입주 날짜와 단지 리스트</h2>')
n=len(items)
out.append(p(f'2026년 7월부터 2027년 6월까지 입주하는 아파트 {n}곳을 달마다 모았습니다. 단지마다 정확한 입주 날짜, 지역 · 세대 수, 낭만 블로그에 쓴 글, 그 지역 시공팀 리스트를 이었습니다.'))
out.append(p(f'<b style="color:#c0392b {S};">빨간 날짜</b>는 입주 안내문 · 공지로 확인한 날입니다. 「○월 중」은 아직 날짜 공지 전이라 달만 적었습니다. 날짜가 나오면 이 글을 고칩니다. (2026년 11월 1일 기준)'))
box=''.join(f'<li style="font-size:19px {S};margin-bottom:6px {S};"><a href="#m{k}" style="color:#1d3d5c {S};font-weight:700 {S};">{ymd(k)} 입주 · {len(by[k])}곳 · {sum(x["세대"] or 0 for x in by[k]):,}세대</a></li>' for k in M4)
out.append(f'<div style="background:#fff8e8 {S};border:1px solid #f0d9a0 {S};padding:14px 18px {S};margin:16px 0 24px {S};border-radius:6px {S};">'+p('<b>앞으로 4개월 입주 아파트</b>')+f'<ul style="padding-left:22px {S};margin:6px 0 0 {S};">{box}</ul></div>')
for y in ('2026','2027'):
    ks=[k for k in by if k.startswith(y) and k>=NOW]
    if not ks: continue
    lab='2026 입주물량 · 남은 달' if y=='2026' else '2027년 입주 아파트'
    out.append(f'<h2 style="font-size:25px {S};color:#1d3d5c {S};margin:40px 0 8px {S};border-bottom:3px solid #1d3d5c {S};padding-bottom:6px {S};">{lab}</h2>')
    for k in ks:
        out.append(f'<h3 id="m{k}" style="font-size:22px {S};color:#1d3d5c {S};margin:28px 0 10px {S};">{ymd(k)} 입주 아파트 · {len(by[k])}곳</h3>')
        out+= [block(x) for x in by[k]]
out.append(f'<h2 style="font-size:25px {S};color:#1d3d5c {S};margin:40px 0 8px {S};border-bottom:3px solid #1d3d5c {S};padding-bottom:6px {S};">입주가 이미 시작된 단지 (2026년 7~10월)</h2>')
for k in [k for k in by if k<NOW]:
    out.append(f'<h3 id="m{k}" style="font-size:22px {S};color:#1d3d5c {S};margin:28px 0 10px {S};">{ymd(k)} 입주 · {len(by[k])}곳</h3>')
    out+= [block(x) for x in by[k]]
out.append(f'<h2 style="font-size:24px {S};color:#1d3d5c {S};margin:40px 0 12px {S};">시공팀은 어떻게 부르나요?</h2>')
out.append(p('단지 이름과 동 · 타입, 열쇠 받는 날을 문자로 보내 주세요. 그 단지에 가는 시공팀을 이어 드립니다. 입주박람회 · 단지 카페에서 받은 견적서가 있으면 사진을 같이 보내 주세요. 같은 범위로 한 곳 더 맞춰 보여 드립니다.'))
out.append(p('소개만 하고 공사는 시공팀이 직접 합니다. 소개비는 시공팀이 냅니다. 손님이 내는 금액은 시공팀에 직접 물을 때와 같습니다.'))
out.append(f'<div style="background:#f3f6fa {S};border-left:5px solid #2f5d8a {S};padding:14px 18px {S};margin:14px 0 24px {S};">'+p('<b style="font-size:22px">문자 · 전화 010-2882-8165</b>')+p('첫 줄에 「단지 이름 / 동 · 타입 / 열쇠 받는 날」')+'</div>')
L=[('입주청소 새집증후군 비용, 20평부터 50평까지','https://nangmaninterior.tistory.com/47'),('곰팡이 제거 업체, 지역별 결로 단열 시공팀 연결','https://nangmaninterior.tistory.com/50'),('입주청소 업체 고르는 법, 전화로 먼저 물을 네 가지','https://nangmaninterior.tistory.com/6'),('입주청소 추가금 요구, 청소 피해 5건 중 1건은 더 달라는 돈','https://nangmaninterior.tistory.com/7'),('아파트 하자보수 기간, 입주 2년이면 청구가 끝납니다','https://nangmaninterior.tistory.com/14'),('결로 단열 협력업체 모집, 겨울 동파 · 보일러 시공팀','https://nangmaninterior.tistory.com/48'),('제휴 시공팀 모아 보기 · 하는 일 · 지역별','https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_889.html')]
out.append(f'<h3 style="font-size:20px {S};color:#1d3d5c {S};margin:30px 0 10px {S};">같이 보면 좋은 글</h3><ul style="padding-left:22px {S};">'+''.join(f'<li style="font-size:19px {S};margin-bottom:6px {S};">{a(u,t)}</li>' for t,u in L)+'</ul>')
out.append(p('#2027년입주아파트 #입주예정아파트 #2026입주물량 #서울입주아파트2026 #부산입주예정아파트'))
out.append('</div>')
h=''.join(out);open('body.html','w').write(h);print(len(h.encode())//1024,'KB')
