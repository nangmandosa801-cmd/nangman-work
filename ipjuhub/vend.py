import pickle,collections,html as H,json
from build import datestr,vendors,cplace
items,by=pickle.load(open('data.pkl','rb'))
S='!important'
def region(x):
    prov,toks=cplace(x['지역'] or '')
    m={'서울':'서울','인천':'인천','경기':'경기','부산':'부산 · 경남','경남':'부산 · 경남','울산':'울산','대구':'대구 · 경북','경북':'대구 · 경북','대전':'대전 · 세종 · 충청','세종':'대전 · 세종 · 충청','충북':'대전 · 세종 · 충청','충남':'대전 · 세종 · 충청','광주':'광주 · 전남','전남':'광주 · 전남','전북':'전북','강원':'강원 · 제주','제주':'강원 · 제주'}
    return m.get(prov,'그 밖')
RID={'서울':'seoul','인천':'incheon','경기':'gyeonggi','부산 · 경남':'busan','울산':'ulsan','대구 · 경북':'daegu','대전 · 세종 · 충청':'daejeon','광주 · 전남':'gwangju','전북':'jeonbuk','강원 · 제주':'gangwon','그 밖':'etc'}
import build as Bm
def vendorsB(reg):
    prov,toks=Bm.cplace(reg);out=[]
    for c in Bm.ORDER:
        L=sorted([(Bm.covers(p['area'],prov,toks),p) for p in Bm.PART if c in p['cats'] and 'blogspot' in p['u']],key=lambda x:-x[0])
        L=[p for s2,p in L if s2>0][:2]
        if L: out.append((c,L))
    return out
up=[x for x in items if x['입주시작']>='2026-11']
G=collections.OrderedDict((k,[]) for k in RID)
for x in up: G[region(x)].append(x)
def p(t,sz=19): return f'<p style="font-size:{sz}px {S};line-height:1.8 {S};margin:0 0 8px {S};">{t}</p>'
out=[f'<div style="font-family:\'Noto Sans KR\',sans-serif {S};color:#222 {S};max-width:760px {S};margin:0 auto {S};">']
out.append(p('<b style="color:#2f5d8a">낭만 인테리어 · 입주 시공팀</b>'))
out.append(f'<h2 style="font-size:28px {S};color:#1d3d5c {S};line-height:1.45 {S};margin:6px 0 16px {S};">입주청소 업체 추천,<br>입주 아파트 지역별 시공팀 리스트</h2>')
out.append(p('2026년 11월부터 2027년 6월까지 입주하는 아파트를 지역으로 묶고, 그 지역에 가는 시공팀을 품목별로 이었습니다. 사전점검 · 입주청소 · 새집증후군 · 줄눈 · 중문 · 결로단열 · 보일러 · 이사입니다.'))
out.append(p('소개만 하고 공사는 시공팀이 직접 합니다. 소개비는 시공팀이 냅니다. 손님이 내는 금액은 시공팀에 직접 물을 때와 같습니다. 단지별 입주 날짜는 <a href="https://nangmaninterior.tistory.com/53" target="_blank">2027년 입주 아파트 월별 리스트</a>에 있습니다.'))
nav=' · '.join(f'<a href="#r-{RID[k]}">{k} {len(v)}곳</a>' for k,v in G.items() if v)
out.append(f'<div style="background:#fff8e8 {S};border:1px solid #f0d9a0 {S};padding:14px 18px {S};margin:14px 0 24px {S};border-radius:6px {S};">'+p('<b>지역 바로 가기</b><br>'+nav)+'</div>')
for k,L in G.items():
    if not L: continue
    out.append(f'<h3 id="r-{RID[k]}" style="font-size:24px {S};color:#1d3d5c {S};margin:36px 0 10px {S};border-bottom:3px solid #1d3d5c {S};padding-bottom:6px {S};">{k} 입주 아파트 시공팀 · {len(L)}곳</h3>')
    # 품목별 시공팀(지역 안 단지들이 쓰는 팀을 모음)
    cnt=collections.OrderedDict()
    for x in L:
        for c,V in vendorsB(x['지역'] or ''):
            for v in V: cnt.setdefault(c,collections.Counter())[v['u']]+=1
    rows=''.join(f'<tr><td style="padding:9px {S};border:1px solid #c9d4df {S};font-size:18px {S};font-weight:700 {S};width:24% {S};">{c}</td><td style="padding:9px {S};border:1px solid #c9d4df {S};font-size:18px {S};">'+' · '.join(f'<a href="{u}" target="_blank">시공팀 소개 {"①②③"[i]}</a>' for i,(u,_) in enumerate(C.most_common(3)))+'</td></tr>' for c,C in cnt.items())
    if rows: out.append(f'<table style="width:100% {S};border-collapse:collapse {S};margin:8px 0 14px {S};">{rows}</table>')
    def clink(x):
        nm=H.escape(x["단지"].split("(")[0]);d=datestr(x)[0].split(" (")[0].split(" · ")[0]
        order={'낭만 부동산 분석 플랫폼':0,'낭만 인테리어':1,'낭만 부동산 입주 노트':2,'낭만 인테리어 티스토리':3}
        ps=sorted([q for q in x['_p'] if q['b'] in order],key=lambda q:order[q['b']])
        if not ps: return f'{nm}({d} · <span style="color:#8a94a0;">글 준비 중</span>)'
        more=''.join(f' <a href="{q["u"]}" target="_blank">{"②③④"[k]}</a>' for k,q in enumerate(ps[1:4]))
        return f'<a href="{ps[0]["u"]}" target="_blank"><b>{nm}</b></a>{more}({d})'
    names=' · '.join(clink(x) for x in L)
    out.append(p('<b>이 지역 입주 단지</b> · '+names,18))
out.append(f'<h2 style="font-size:24px {S};color:#1d3d5c {S};margin:40px 0 12px {S};">시공팀은 어떻게 부르나요?</h2>')
out.append(p('단지 이름과 동 · 타입, 열쇠 받는 날을 문자로 보내 주세요. 그 단지에 가는 시공팀을 이어 드립니다. 받은 견적서가 있으면 사진을 같이 보내 주세요. 같은 범위로 한 곳 더 맞춰 보여 드립니다.'))
out.append(f'<div style="background:#f3f6fa {S};border-left:5px solid #2f5d8a {S};padding:14px 18px {S};margin:14px 0 24px {S};">'+p('<b style="font-size:22px">문자 · 전화 010-2882-8165</b>')+p('첫 줄에 「단지 이름 / 동 · 타입 / 열쇠 받는 날」')+'</div>')
T=[('2027년 입주 아파트, 월별 입주 날짜와 단지 리스트','https://nangmaninterior.tistory.com/53'),('입주청소 새집증후군 비용, 20평부터 50평까지','https://nangmaninterior.tistory.com/47'),('입주청소 업체 고르는 법, 전화로 먼저 물을 네 가지','https://nangmaninterior.tistory.com/6'),('입주청소 추가금 요구, 청소 피해 5건 중 1건은 더 달라는 돈','https://nangmaninterior.tistory.com/7'),('곰팡이 제거 업체, 지역별 결로 단열 시공팀 연결','https://nangmaninterior.tistory.com/50'),('제휴 시공팀 모아 보기 · 하는 일 · 지역별','https://nangmanbusinesscards.blogspot.com/2026/10/blog-post_889.html')]
out.append(f'<h3 style="font-size:20px {S};color:#1d3d5c {S};margin:30px 0 10px {S};">같이 보면 좋은 글</h3><ul style="padding-left:22px {S};">'+''.join(f'<li style="font-size:19px {S};margin-bottom:6px {S};"><a href="{u}" target="_blank">{t}</a></li>' for t,u in T)+'</ul>')
out.append(p('#입주청소업체추천 #입주청소업체 #사전점검업체 #입주아파트 #낭만인테리어'))
out.append('</div>')
h=''.join(out);open('vend.html','w').write(h);print(len(h.encode())//1024,'KB',{k:len(v) for k,v in G.items()})
json.dump({x['단지']:RID[region(x)] for x in items},open('rid.json','w'),ensure_ascii=False)
