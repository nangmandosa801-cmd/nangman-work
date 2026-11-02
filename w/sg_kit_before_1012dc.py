# 시공 글 공통 (2026.10.4 밤~) — sigong_v2.build_new 위에 새 규칙 검사를 얹음
# 새 규칙: 「가격 · 이유 · 비교 · 순서」(값 · 까닭 · 견줘 · 차례 안 씀) · 놓습니다/가정/기준 꼬리표 · 본문에 업체 이름과 번호 없음 · 3 스트라이크 없음 · 카드 링크 번호 없음
exec(open('/home/claude/int/sigong_v2.py').read())
sys.path.insert(0,'/home/claude/pjh')
try: import mark2
except ModuleNotFoundError: mark2=None   # 10/6: /home/claude/pjh(모던중문 원본 사진과 mark2.py)가 작업 공간에서 사라짐 — 업체 표시를 덮는 crop_badge · mark2.badge를 쓰는 글은 mark2.py를 다시 만들어야 돈다
def crop_badge(path,box,marks,bw=300,bh=108):
    """큰 합성 사진에서 한 칸을 잘라 내고 업체 표시를 낭만 인테리어 표시로 덮는다. box와 marks는 원본 좌표"""
    im=Image.open(path).convert('RGB')
    for m in marks:
        if len(m)==4: mark2.badge(im,*m)
        else: mark2.badge(im,m[0],m[1],bw,bh)
    return im.crop(box) if box else im
def build_s(slug,T,kick,thumb,photos,o,keys,tags):
    build_new(slug,T,kick,thumb,photos,o,keys,tags)
    if slug in _GUIDE: sys.path.insert(0,'/home/claude/int'); __import__('guide_card').render(_GUIDE[slug],OUT+slug+f'/nangman_interior_{slug}_guide.png')
    if slug in _BANNER:   # 글 내용을 담는 끝 배너 — 같은 그림을 글마다 되풀이하지 않는다 (10/6 22:28 사용자)
        kd,q,items,names,ex=_BANNER[slug]; P={nm:im for im,nm,cap in photos}; nm3=names or [photos[i][1] for i in sorted({0,len(photos)//2,len(photos)-1})]
        sys.path.insert(0,'/home/claude/int'); __import__('post_banner').render(OUT+slug+f'/nangman_interior_{slug}_banner.png',kd,T,q,items,[P.get(x,x) if isinstance(x,str) else x for x in nm3],ex=ex,crop=1,two=_TWO.get(slug,True))
    if slug in _APPEAL: sys.path.insert(0,'/home/claude/int'); __import__('appeal_card').render(T,OUT+slug+f'/nangman_interior_{slug}_appeal.png',_APPEAL[slug])   # 10/10 23:23 사용자 — 손님 어필 그림 · 글 제목을 옅게 넣어 글마다 다름
    if slug in _STRIP: sys.path.insert(0,'/home/claude/int'); __import__('guide_card').strip(*_STRIP[slug][:1],OUT+slug+f'/nangman_interior_{slug}_ask.png',_STRIP[slug][1],ex=(_BANNER.get(slug) or [None]*5)[4])
    h=open(OUT+slug+f'/nangman_interior_{slug}_post.html').read()
    t=re.sub('<[^>]+>',' ',re.sub('<!--.*?-->','',h)).split('같이 보면 좋은 글')[0]
    bad=re.findall(r'\S*(?:어요|예요|값|까닭|견줘|견주|차례|놓습니다|가정|기준|가운데 하나|모던중문|소소리|썬중문|크로바)\S*',t)
    print('  새 규칙 검사',bad)
    # 10/9 10:04 사용자 「인테리어 글 쓸때 좀 쉽게 이해하기 쉽게 써」 — 어려운 말 · 긴 문장 검사 (프로젝트 문서 낭만인테리어_글쓰기_지적사항.md 0-2)
    EASY={'단차':'높이 차이','하부장':'싱크대 아래 수납장','상부장':'싱크대 위 수납장','몰딩':'벽 아래 · 천장 둘레 띠','재단':'자르기','탈거':'빼내기','분진':'먼지','도장':'페인트칠','내구성':'오래 버티는지','완충':'충격을 받아 줌','생활방수':'물을 흘려도 닦임','고밀도':'단단하게 꽉 찬','마감재':'겉면 재료','하자':'잘못된 곳','시공 완성도':'마무리 상태','논슬립':'미끄럼 방지','전실':'현관 앞 작은 공간','공정':'작업 단계','실측':'치수 재기','타공':'구멍 뚫기','우레탄':'(설명 붙이기)','2.2T':'2.2cm'}
    hard=sorted({w for w in EASY if w in t}); longs=[x.strip()[:40]+'…' for x in re.split(r'(?<=[.?!])\s+',re.sub(r'\s+',' ',t)) if len(x.strip())>40 and x.strip().endswith(('다.','?')) and 'nangman_' not in x and '▸' not in x and ' · ' not in x[:30]]
    # 10/9 10:24 사용자 「너무 다 다로 끝나 다양하게 표현 인간처럼」 — 본문 문장 끝 가운데 「~다.」 비율 · 같은 끝 세 번 연달아
    ends=[x.strip() for x in re.split(r'(?<=[.?!])\s+',re.sub(r'\s+',' ',t)) if x.strip().endswith(('다.','죠.','요.','?','.')) and 'nangman_' not in x and '▸' not in x and len(x.strip())>8]
    da=[x.endswith('다.') for x in ends]; run=max((len(m.group()) for m in re.finditer('1+',''.join('1' if d else '0' for d in da))),default=0)
    print('  문장 끝 검사 · 「~다.」',f'{sum(da)}/{len(ends)}',f'({round(100*sum(da)/max(1,len(ends)))}% · 65% 아래로)','· 「~다.」 가장 길게 연달아',run,'(4 아래로)')
    print('  쉬운 말 검사 · 어려운 말',[f'{w}→{EASY[w]}' for w in hard],'· 40자 넘는 문장',len(longs),longs[:5])
    # 문의가 오게 쓰는 법 검사 (10/6 22:11 사용자: 「글 적을 때 문의가 잘 오게 만들어」) — 프로젝트 문서 낭만인테리어_견적정책.md 「문의가 오게 쓰는 법」
    # 10/9 20:41 사용자 「넣고 일련번호까지 포함하라니깐」 — 사진 번호(NI-)가 있는 글은 「이 사진처럼 하고 싶다면」 상자(nk.LIKE)가 있어야 한다
    if '(사진 NI-' in t and '이 사진처럼' not in t: print('  ✘ 「이 사진처럼 하고 싶다면」 상자(LIKE) 없음 — 사진 번호를 넣은 글은 꼭 넣을 것')
    miss=[n for n,ok in [('문의 띠(STRIP) — 글 가운데',slug in _STRIP),('문의 상자(WHO)','연락처를 비밀댓글로' in t),('사진 10장',len(photos)>=10)] if not ok]
    nq=len(re.findall('견적',t)); first=re.sub(r'\s+',' ',t)[:400]
    if '수수료' not in re.sub(r'\s+',' ',t)[:400]: miss.append('글 첫머리 소개 수수료 고지')
    if slug not in _BANNER: miss.append('내용 배너(BANNER)')
    fake=re.findall(r'이번 ?달만|이번 ?주만|오늘만|놓치면|마감 ?임박|선착순|한정 ?수량|서두르',t)
    if fake: print('  기한 · 손실 표현',fake,'← 실제 기한이 없으면 뺄 것')
    # 장점 원칙 (10/8 21:26 · 21:34 사용자: 「장점을 꼭 넣어 원칙으로 해」) — 프로젝트 문서 낭만인테리어_글쓰기_지적사항.md 0-1
    tt=re.sub(r'\s+',' ',t); cut=len(tt)//3
    good=[n for n,ok in [('앞쪽 「달라지는 것 · 좋은 점」 상자',bool(re.search(r'달라지는 것|좋은 점|장점',tt[:cut]))),
        ('자재 · 제품 장점',bool(re.search(r'장점',tt))),('「시공팀이 … 지키는 것」 상자',bool(re.search(r'(?:업체가|시공팀이|팀이)[^。]{0,30}지키는 것',tt)))] if not ok]
    print('  장점 검사 · 빠진 것',good,'← 채울 것' if good else '')
    print('  문의 검사 · 빠진 것',miss,'· 본문 「견적」',nq,'번'+(' ← 5번 넘음, 줄일 것' if nq>5 else ''))

# 10/6 18:15 사용자: 「복수 비교 견적도 가능하다고 얘기하고」 — 제휴 업체가 두 곳 넘게 겹치는 품목 · 지역에서만 쓴다(사실일 때만). 업체가 늘면 여기에 품목을 더한다.
#   중문: 경기 · 서울 · 인천 = 인천 시흥 중문 + 썬중문(+ 남양주 인근 소소리) / 충청 = 크로바 + 썬중문 / 부산 · 경남은 모던 한 곳이라 해당 없음
#   필름: 서울 · 경기 = 도하인테리어필름 + 더빅필름 / 샷시 · 코킹 · 문 수리 · 방묘문 · 입주 청소는 한 곳씩이라 쓰지 않음(샷시는 답을 기다리는 곳이 붙으면 더함)
CMP={'중문':'글에 나온 중문을 그대로 고르셔도 됩니다. 서울 · 경기 · 인천 · 충청은 다른 제품, 다른 업체의 견적도 같이 받아 비교하실 수 있습니다.',
     '필름':'글에 나온 필름을 그대로 고르셔도 됩니다. 서울과 경기는 다른 필름, 다른 업체의 견적도 같이 받아 비교하실 수 있습니다.',
     # 업체가 한 곳인 품목: 「다른 업체」는 쓰지 않고 「다른 제품」까지만 (10/6 19:06 사용자: 「블로그 글 모델을 선택하셔도 되고 다른 모델 · 업체 복수 견적도 가능하다는 취지로」)
     '샷시':'글에 나온 창을 그대로 고르셔도 되고, 다른 제품의 견적도 같이 받아 보실 수 있습니다.',
     '방묘문':'글에 나온 문을 그대로 고르셔도 되고, 다른 모양의 견적도 같이 받아 보실 수 있습니다.'}
def cmp_line(kind): return CMP.get(kind,'')
# 10/6 19:03 사용자: 「글 쓸 때 하라고」 — 견적서 봐 주기 · 거절 대행 약속을 새 글의 문의 문장에 넣는다(모든 품목)
PROMISE='다른 곳에서 받은 견적서가 있으면 같은 공사인지 봐 드립니다. 소개받은 시공팀이 마음에 안 들면 거절 연락은 저희가 대신 드립니다.'
def ASK(kind,region,last=''):
    """글 끝 문의 문장 — 「사는 지역만 비밀댓글로」(10/5 규칙) + 견적을 잇는 지역 + 그 글에만 붙는 말.
    10/6 20:57 사용자: 「견적 이런 말이나 판매 영업 관련 문구는 본문에서 반복되면 저품질 판정 받을 수 있으니 시각화해서」
    → 두 곳 비교(CMP) · 견적서 봐 주기 · 거절 대행(PROMISE)은 본문 글자로 쓰지 않고 GUIDE 그림에 넣는다. kind는 그대로 받되 문장에는 쓰지 않는다."""
    # 10/6 22:53 사용자: 「사는 지역하고 연락처도 남겨야지」
    return ' '.join(x for x in ['사는 지역과 연락처를 비밀댓글로 남겨 주세요.',region,last] if x)
_GUIDE={}
def GUIDE(slug,kind):
    """견적 안내 그림 자리 — 문의 상자(WHO) 바로 아래에 둔다. kind: 중문 · 필름 · 샷시 · 방묘문 · 코킹 · 문수리 · 청소. 그림은 build_s가 만든다(guide_card.py)."""
    _GUIDE[slug]=kind
    return PH(f'nangman_interior_{slug}_guide.png — 견적 안내 그림')
_APPEAL={}
def APPEAL(slug,kind='일반'):
    """「낭만 인테리어에 물어보시면」 어필 그림 자리 — 문의 상자 바로 위에 한 번. kind: 입주 · 일반. 그림 아래에 글 제목이 아주 옅게 들어간다(appeal_card.py)."""
    _APPEAL[slug]=kind
    return PH(f'nangman_interior_{slug}_appeal.png — 낭만 인테리어에 물어보시면')
# 10/10 23:45 사용자 「앞으로 블로그 쓸 때 전세 복구 들 아직 안 들어갔어」 — 전세 · 입주 · 이사 글에 반려견 집 → 매트로 넘어가는 한 줄 상자
MAT_URL='https://blog.naver.com/champion_chart/224435609606'
def PETLINE(what='이사 들어가기 전'):
    return ('<p style="background:#F7F5F0;border-left:4px solid #B5761A;padding:16px 20px;font-size:19px;color:#333;line-height:1.9;">'
            f'<b style="color:#1F3864;">강아지 · 고양이와 사는 집이라면</b><br>{what}에 거실과 복도에 매트를 깔면 미끄러지지 않고, 이사할 때 걷어 낼 수 있습니다. '
            f'평수와 깔 곳만 남기시면 몇 장 드는지 알려 드립니다. <a href="{MAT_URL}">강아지 매트 시공 사례 보기 →</a></p>')
MATGOOD_HTML='<table width="100%" style="width:100%;border-collapse:collapse;margin:24px 0;"><tr><td style="background:#F2F4F7;border-left:5px solid #2E5C8A;padding:20px 22px;font-size:19px;color:#333;line-height:1.95;"><b style="color:#1F3864;font-size:22px;">좋은 강아지 매트는 이렇게 고릅니다</b><br><br>▸ <b style="color:#1F3864;">세 겹을 봅니다</b> · 겉면 TPU 막이 미끄럼 · 긁힘 · 물을 막고, 가운데 우레탄 폼이 충격과 소리를 받아 줍니다. 바닥 방수층이 있어 스팀청소도 됩니다.<br>▸ <b style="color:#1F3864;">같은 2.2cm라도 다릅니다</b> · 우레탄이 많이 든 논슬립 매트가 더 단단히 받쳐 줘서 강아지 발이 휘청거리지 않습니다.<br>▸ <b style="color:#1F3864;">소리와 미끄럼</b> · 시공팀이 잰 송도 집은 70dB에서 21.5dB로 줄었습니다. 겉면 미끄럼 저항은 일반 PVC 바닥재의 세 배가 넘는다고 합니다.<br>▸ <b style="color:#1F3864;">샘플부터</b> · 손으로 눌러 보고 고르세요. 비밀댓글에 「샘플」이라고만 남기면 요청해 보내 드립니다.<br><br><a href="https://blog.naver.com/champion_chart/224437536765" target="_blank" style="color:#2E5C8A;font-weight:700;text-decoration:underline;">→ 자세한 비교 보기 : 강아지 매트 추천, 같은 2.2cm라도 겉면 TPU와 속 우레탄 양이 달라서 샘플을 눌러 보고 고릅니다</a></td></tr></table>'
def MATGOOD():
    """10/11 00:14 사용자 — 강아지 · 고양이 매트 글에 넣는 「좋은 강아지 매트는 이렇게 고릅니다」 장점 상자 + 매트 추천 글(224437536765) 링크. 문의 상자 위에 한 번."""
    return MATGOOD_HTML
_STRIP={}
def STRIP(slug,kind,q,kw=''):
    """글 가운데 「문의 띠」 그림 자리 — 그 글에서 손님이 혼자 정하기 어려운 것을 다룬 문단 바로 아래에 한 번. q는 그것을 묻는 말(「우리 집 현관에도 3연동이 들어갈까요?」). 그림은 build_s가 만든다."""
    _STRIP[slug]=(kind,q)
    return PH(f'nangman_interior_{slug}_ask.png — {kw} 문의 안내 그림'.replace('—  ','— '))
_BANNER={}; _TWO={}
def BANNER(slug,kind,q,items,photos=None,ex=None,two=True):
    """끝 배너에 그 글의 내용을 담는다 — q: 그 글만의 질문 · items: 「이런 집이라면」 세 줄(WHO 상자의 줄을 그대로) · photos: 쓸 사진 이름 셋(없으면 처음 · 가운데 · 끝) · ex: 댓글 예시(그 글의 지역으로). build_s 앞에서 한 번 부른다."""
    _BANNER[slug]=(kind,q,items,photos,ex); _TWO[slug]=two
