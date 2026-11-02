# 10/18 2차 현행화: 1차(링크) 결과 위에 「지금 기준」을 맞춘다 — 사용자 「10-31 12시 중문 단열 글까지 예약했는데 이후 글들이 전체적으로 현행화가 안 됐다」
import json,re,os,sys,collections
sys.path.insert(0,'/home/claude/int'); import links
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
pub=json.load(open('/home/claude/pub/int_live_1018.json')); T={i:t for i,t in pub}
TB=json.load(open('/home/claude/watch/tailboost/tail_boost.json'))
TBI={x['log']:x for x in TB['items']}
norm=lambda s:re.sub(r'[\s,·.›]','',s)
slug=lambda s:os.path.basename(s)[len('nangman_interior_'):-len('_paste.html')]
HEAD='<p style="font-size:16px;color:#444;line-height:1.8;"><span style="background-color:#EEF1F5;">이 글은 낭만 인테리어가 씁니다. 저희는 검증된 제휴 시공업체를 소개합니다. 계약하시면 업체에게서 계약 금액의 일부를 소개 수수료로 받습니다.</span></p>'
LINK=lambda i:f'「<a href="https://blog.naver.com/champion_chart/{i}" style="color:#2E5C8A;">{T[i]}</a>」'
# ── 금지어 · 「업체가/업체는」 주어 · 문의 문장: 그 문장만 고친다 (old, new)
FIX={
'jungmun_brand':[('다루는 업체가 많아 나중에','다루는 곳이 많아 나중에')],
'bangchungmang_cat':[('방충망 종류, 고양이 발톱 기준으로 보면','방충망 종류, 고양이 발톱으로 보면'),
  ('값이 가장 높습니다','가격이 가장 높습니다'),('한 업체는 24·30메시','한 곳은 24·30메시'),
  ('「방묘창 설치, 망보다 먼저 방충망 틀이 빠지지 않는지 봅니다」',LINK('224422997793')),('「단열필름 시공, 겨울에 해 주는 것과 못 하는 것 · 로이유리 집은 먼저 유리부터」',LINK('224444765222'))],
'sash_grade':[('낭만 부동산 분석 플랫폼 · 인테리어','낭만 인테리어 · 샷시 등급'),('국토교통부 「건축물의 에너지절약설계기준」 별표에 조합별 숫자가','국토교통부 고시 별표에 조합별 숫자가'),('국토교통부 「건축물의 에너지절약설계기준」 별표4 · 숫자가','국토교통부 고시 별표4 · 숫자가')],
'sunseo':[('업체가 여럿이면 한 곳이 늦을 때','맡긴 곳이 여럿이면 한 곳이 늦을 때')],
'cheongso_sunseo':[('청소 업체가 출입할 수 있는지 확인하면','청소팀이 출입할 수 있는지 확인하면'),('잔금 전에 청소 업체가 출입할 수 있나요','잔금 전에 청소팀이 출입할 수 있나요')],
'sash_brand':[('LX하우시스 안내 끝에는 이런 문장이 있습니다.','LX하우시스 안내 끝에는 이런 내용이 있습니다.'),
  ('모든 모델이 동일한 1등급 성능 구현이 가능하므로 선택은 디자인과 편의성 기준으로 판단하면 됩니다.','모든 모델이 같은 1등급 성능을 내니 디자인과 편의성을 보고 고르면 된다는 내용입니다.')],
'jungmun_cost':[('직접 오는 업체가 있고, 다른 팀에 넘기는 업체가 있습니다','직접 오는 곳이 있고, 다른 팀에 넘기는 곳이 있습니다')],
'ipju_cheongso':[('업체가 공개한 가격은 37만원입니다','업체 공개 가격은 37만원입니다'),('청소 업체가 들어올 수 있는지','청소팀이 들어올 수 있는지'),('말고 업체가 집을 직접 본 뒤에','말고 청소팀이 집을 직접 본 뒤에')],
'solar1':[('그 업체가 집을 미리 진단한 뒤','그 기업이 집을 미리 진단한 뒤'),('설치한 업체가 없어질 수 있습니다','설치한 회사가 없어질 수 있습니다'),('업체가 와서 난간 · 방향 · 콘센트를','참여기업이 와서 난간 · 방향 · 콘센트를')],
'upche':[('나란히 놓으면 값이 다른 까닭이 보입니다','나란히 놓으면 가격이 다른 이유가 보입니다'),('그래서 업체가 집에 와서 실측해야','그래서 시공팀이 집에 와서 실측해야'),
  ('실측 비용을 받지 않는 업체가 많습니다','실측 비용을 받지 않는 곳이 많습니다'),('브랜드 문인지 업체가 직접 만드는 문인지도','브랜드 문인지 직접 만드는 문인지도'),
  ('업체가 집에 와서 시공하는 일이죠','시공팀이 집에 와서 시공하는 일이죠'),('시공해 본 업체는 고장 났을 때','시공해 본 곳은 고장 났을 때')],
'jungmun_swing':[('3연동 고장 1위와 2위 부품이 달려 있지 않습니다','3연동에서 가장 많이 고장 나는 부품 두 가지가 달려 있지 않습니다')],
'jungmun_mutagong':[('정작 다는 업체가 없습니다','정작 다는 곳이 없습니다'),('나갈 때 원래대로 돌려놔야','이사할 때 원래대로 돌려놔야'),('고장 1위가 상부 레일과 유니트(38%)였던','가장 많은 고장이 상부 레일과 유니트(38%)였던'),
  ('벽이 기울어 있으면 값이 다르게 나옵니다','벽이 기울어 있으면 치수가 다르게 나옵니다'),('그만큼 자리를 먹습니다','그만큼 폭이 줄어듭니다'),
  ('댓글이나 쪽지로 <b>동네 · 현관 사진 · 대략의 폭</b>을 남겨 주세요. 공장에서 직접 제작한 중문으로 시공해 드립니다. 사시는 지역도 같이 남겨 주세요.',
   '<b>사는 지역과 연락처</b>를 비밀댓글로 남겨 주세요. 서울 · 경기 · 인천 · 충청 · 부산 · 경남은 중문 업체를 연결해 드립니다. 현관 사진과 대략의 폭도 같이 남겨 주시면 됩니다.')],
'daejeon_dure':[('대전 중문 설치 업체가 현관을 확인하고','대전 중문 설치 시공팀이 현관을 확인하고')],
'bangmyochang':[('「방묘문, 높이보다 빠져나갈 자리를 봅니다」',LINK('224421379783'))],
'sash_24':[('창호 업체가 블로그에 가격을 공개한','창호 대리점이 블로그에 가격을 공개한')],
'gyeonjeok_bigyo':[('낭만 인테리어도 시공 업체가 아니라 제휴 업체를 연결하는 곳입니다','낭만 인테리어도 직접 시공하는 곳이 아니라 제휴 시공팀을 연결하는 곳입니다')],
'incheon_gompangi':[('업체가 이 집을 살펴보니','시공팀이 이 집을 살펴보니'),('그래서 업체는 창틀과','그래서 시공팀은 창틀과'),('인천 · 부천 · 김포 · 시흥','인천 · 김포 · 시흥')],
'sash_live':[('이 작업은 타일 업체가 따로 합니다','이 작업은 타일 시공팀이 따로 합니다'),('제휴 업체는 특별한 일이 없으면','제휴 시공팀은 특별한 일이 없으면'),('붙어 있는지는 업체가 방문해서 확인합니다','붙어 있는지는 시공팀이 방문해서 확인합니다')],
'villa_sash':[('업체가 방문해서 창을 실측하고','시공팀이 방문해서 창을 실측하고')],
'jeonse_ipju_cheongso':[('서울 · 경기 · 인천은 입주청소 시공팀을 연결해 드립니다','입주청소 시공팀을 연결해 드립니다')],
'seulgaegol_sulhu':[('사는 지역과 연락처를 비밀댓글로 남겨 주세요. 입원한 사이에','사는 지역과 연락처를 비밀댓글로 남겨 주세요. 전국 어디든 매트 시공팀을 연결해 드립니다. 입원한 사이에')],
'changmun_nusu_haegyeol':[('로프를 타고 바깥 창 둘레를 막는 시공팀으로 서울 · 경기 · 인천 어디든 이어 드립니다.','서울 · 경기 · 인천은 로프를 타고 바깥 창 둘레를 막는 코킹 시공팀을 연결해 드립니다.')],
}
# ── 품목(tail_boost 「품목」) · 이웃 품목
NB={'중문':['중문','입주','방묘'],'샷시·창':['샷시·창','누수·코킹','결로·곰팡이'],'누수·코킹':['누수·코킹','샷시·창','결로·곰팡이'],'결로·곰팡이':['결로·곰팡이','누수·코킹','샷시·창'],
    '청소':['청소','입주'],'입주':['입주','청소','중문'],'매트':['매트','입주'],'필름':['필름','샷시·창','중문'],'방묘':['방묘','샷시·창','중문'],'기타':['기타','샷시·창','결로·곰팡이']}
def pummok(sl):
    for k,v in [('cheongso','입주'),('ipju','입주'),('saejip','입주'),('seulgaegol','매트'),('mat','매트'),('film','필름'),('sunseo','필름'),('jeonse_interior','필름'),('bangmyo','방묘'),
                ('bangchungmang','방묘'),('sash','샷시·창'),('incheon_gompangi','결로·곰팡이'),('coking','누수·코킹'),('silicon','누수·코킹'),('nusu','누수·코킹'),('hwajeong','누수·코킹'),('nowon','누수·코킹'),('solar','기타')]:
        if k in sl: return v
    return '중문'
HINT={'입주':['청소'],'청소':['청소'],'매트':['매트'],'필름':['필름'],'샷시·창':['샷시','창'],'중문':['중문'],'누수·코킹':['누수','코킹','실리콘'],'결로·곰팡이':['곰팡이','결로'],'방묘':['방묘'],'기타':['베란다']}
used=collections.Counter()
for i,ds in TB.get('used',{}).items(): used[i]+=len(ds)
log=[];chg=[]
def tail_bounds(h):
    k=h.find('같이 보면 좋은 글')
    if k<0: return None
    a=max(h.rfind('<table',0,k) if 'border-top:3px solid #1F3864' in h[k-400:k] else -1, -1)
    if a<0: a=h.rfind('<p',0,k)
    m=re.search(r'<p style="font-size:1[457]px;color:#(?:8A8578|A8A296);[^"]*">',h[k:])
    b=k+m.start() if m else len(h)
    return a,b
for s in sel:
    sl=slug(s); V1='/home/claude/w/relink1018/v2/v1snap/'; src=V1+s if os.path.exists(V1+s) else B+s; h=open(src).read(); h0=h; ch=[]
    # 1 머리 수수료 고지
    if '이 글은 낭만 인테리어가' not in h:
        m=re.search(r'<p style="font-size:17px;color:#2E5C8A;letter-spacing:1px;">[^<]*</p>\n',h)
        h=h[:m.end()]+'\n'+HEAD+'\n'+h[m.end():]; ch.append('머리 수수료 고지 넣음')
    # 2 문장 고치기
    for a,b in FIX.get(sl,[]):
        if h.count(a)!=1 and not (sl=='upche' and h.count(a)==2): print('!! miss',sl,a[:30],h.count(a)); continue
        h=h.replace(a,b); ch.append('문장: '+a[:24]+' → '+re.sub('<[^>]+>','',b)[:24])
    n=len(re.findall(r'십시오',h))
    if n:
        h=h.replace('물어보십시오','물어보세요').replace('보십시오','보세요').replace('하십시오','하세요'); ch.append(f'「~십시오」→「~세요」 {n}곳')
    # 2b 문의 상자 속 「업체가」 주어 → 시공팀이
    def box(m):
        t=m.group(0)
        if '비밀댓글' not in t: return t
        return re.sub(r'(?<=[는은] )업체가 |(?<=까지 )업체가 |(?<=폭은 )업체가 ','시공팀이 ',t)
    h2=re.sub(r'<p style="background:#F2F4F7;[^>]*>.*?</p>',box,h,flags=re.S)
    if h2!=h: ch.append(f'문의 상자 「업체가」→「시공팀이」 {sum(1 for _ in re.finditer("시공팀이",h2))-sum(1 for _ in re.finditer("시공팀이",h))}곳'); h=h2
    # 3 링크 글자를 발행 제목으로
    def anc(m):
        i,t=m.group(2),m.group(3); suf=' ›' if t.rstrip().endswith('›') else ''
        if i in T and norm(t)!=norm(T[i]) and len(t)>=6:
            ch.append(f'링크 글자→발행 제목 {i}'); return m.group(1)+T[i]+suf+'</a>'
        return m.group(0)
    h=re.sub(r'(<a href="https://blog\.naver\.com/champion_chart/(\d{12})"[^>]*>)([^<]+)</a>',anc,h)
    # 4 다른 블로그(낭만 부동산) 꼬리 목록 빼기 — 샷시 등급
    if sl=='sash_grade':
        m=re.search(r'<p style="font-size:27px;font-weight:700;color:#1F3864;">같이 보면 좋은 글</p>\n<p><br></p>\n(?:<p style="font-size:19px;color:#333;line-height:1.9;">· <a href="https://blog.naver.com/dong_jin_kim/\d+">[^<]*</a></p>\n)+<p><br></p>\n',h)
        h=h[:m.start()]+h[m.end():]; ch.append('낭만 부동산 글 6편 꼬리 목록 뺌(인테리어 꼬리 카드만 남김)')
    # 5 태그 뒤에 붙은 꼬리 → 태그 앞으로
    tags=list(re.finditer(r'<p style="font-size:1[57]px;color:#8A8578;">#[^<]*</p>',h))
    k=h.find('같이 보면 좋은 글')
    if tags and k>tags[-1].end():
        tg=tags[-1]; a=h.rfind('<table',0,k); tail=h[a:].rstrip()+'\n'
        h=h[:tg.start()]+tail+'\n'+tg.group(0)+'\n'+h[tg.end():a]; h=h.rstrip()+'\n'; ch.append('꼬리 묶음을 태그 앞으로 옮김')
    # 6 꼬리 링크: tail_boost 2편(같은 품목 → 이웃 품목) · 5편 이상
    a,b=tail_bounds(h); tail=h[a:b]
    tids=list(dict.fromkeys(re.findall(r'champion_chart/(\d{12})',tail)))
    allids=set(re.findall(r'champion_chart/(\d{12})',h))
    pm=pummok(sl); nb=NB[pm]
    have=[i for i in tids if i in TBI and TBI[i]['품목'] in nb]
    add=[]
    for p in nb:
        if len(have)+len(add)>=2: break
        cands=sorted([x['log'] for x in TB['items'] if x['품목']==p and x['log'] not in tids and x['log'] not in add and used[x['log']]<3],key=lambda i:(not any(w in TBI[i]['kw'] for w in HINT[pm]),i in allids,used[i]))
        for c in cands:
            if len(have)+len(add)>=2: break
            add.append(c); used[c]+=1
    if add:
        style='card' if 'border-top:3px solid #1F3864' in tail else ('dot' if '>· <a href' in tail else ('br' if '›</a><br>' in tail else 'span'))
        if style=='card':
            last=list(re.finditer(r'</td></tr></table>\n',tail))[-1]
            tail=tail[:last.end()]+''.join(links.item(i,T[i]) for i in add)+tail[last.end():]
            tail=re.sub(r'(&nbsp;&nbsp;)(\d+)(편</span>)',lambda m:m.group(1)+str(len(tids)+len(add))+m.group(3),tail,count=1)
        elif style=='dot':
            last=list(re.finditer(r'<p style="font-size:19px;color:#333;line-height:1.9;">· <a [^\n]*</p>\n',tail))[-1]
            st=re.search(r'<a href="[^"]+"( style="[^"]*")?>',last.group(0)).group(1) or ''
            tail=tail[:last.end()]+''.join(f'<p style="font-size:19px;color:#333;line-height:1.9;">· <a href="https://blog.naver.com/champion_chart/{i}"{st}>{T[i]}</a></p>\n' for i in add)+tail[last.end():]
        elif style=='br':
            last=list(re.finditer(r'›</a>\n</p>',tail))[-1]
            tail=tail[:last.start()]+'›</a><br>\n'+'<br>\n'.join(f'<a href="https://blog.naver.com/champion_chart/{i}" style="color:#2E5C8A;">{T[i]} ›</a>' for i in add)+'\n</p>'+tail[last.end():]
        else:
            last=list(re.finditer(r'<p style="font-size:19px;font-weight:700;"><a [^\n]*(?:\n<span[^\n]*)?</p>\n<p><br></p>\n',tail))[-1]
            def sp(i):
                d=links.DESC.get(i,'')
                return (f'<p style="font-size:19px;font-weight:700;"><a href="https://blog.naver.com/champion_chart/{i}" style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #C7D6E6;">{T[i]}</a>'
                        +(f'<br>\n<span style="font-size:17px;font-weight:400;color:#7A8590;">{d}</span>' if d else '')+'</p>\n<p><br></p>\n')
            tail=tail[:last.end()]+''.join(sp(i) for i in add)+tail[last.end():]
        h=h[:a]+tail+h[b:]; ch.append(f'꼬리 첫 화면 밖 글 {len(add)}편 더함({pm}: '+' · '.join(TBI[i]['kw'] for i in add)+')')
    ntail=len(set(re.findall(r'champion_chart/(\d{12})',h[tail_bounds(h)[0]:tail_bounds(h)[1]])))
    if h!=h0:
        os.makedirs(os.path.dirname(O+s),exist_ok=True); open(O+s,'w').write(h)
    log.append(dict(file=s,slug=sl,pummok=pm,changes=ch,tail=ntail,tb_have=have,tb_add=add,changed=h!=h0))
json.dump(log,open('/home/claude/w/relink1018/v2/log2.json','w'),ensure_ascii=False,indent=1)
json.dump(dict(used),open('/home/claude/w/relink1018/v2/tb_used.json','w'),ensure_ascii=False,indent=1)
for l in log: print(l['slug'],l['pummok'],l['tail'],len(l['changes']),l['tb_add'])
print('changed',sum(l['changed'] for l in log))
