import re,json,datetime,sys
M='/home/claude/proj/입주이주_단지_마스터_1026.md'
PUB='/home/claude/proj/발행글_목록_부동산_인테리어.md'
SCH='/home/claude/watch/mix_schedule_1017c.json'
today=datetime.date(2026,10,26)
def norm(s): return re.sub(r'[\s\(\)\[\]·,\-]|\(.*?\)','',re.sub(r'\(.*?\)','',s))
_t=open(PUB,encoding='utf-8').read()
_a,_b=_t.split('## 낭만 인테리어 (champion_chart)')
rx=r'^\| [^|]+\| (\d{12}) \| (.+?) \|$'
nb=[(m.group(1),m.group(2)) for m in re.finditer(rx,_a,re.M)]
ic=[(m.group(1),m.group(2)) for m in re.finditer(rx,_b,re.M)]
pub=nb+ic
ALIAS={'성남수진1구역':'수진1구역','영통벽적골':'벽적골','여의도대교아파트':'대교아파트','개포주공':'개포주공'}
pairs=[]
d=json.load(open(SCH));rows=d if isinstance(d,list) else d['rows']
sch=[]
for r in rows:
    st=(r.get('상태') or '');t=r['제목']
    kind='발행' if st.startswith('발행') else '예약' if st.startswith('예약') else '원고' if '원고' in st or st.startswith('미발행') else '쓸글' if '[쓸 글]' in t else None
    if kind and not st.startswith('보류'): sch.append((kind,r['날'],r['시각'],t,st))
txt=open(M,encoding='utf-8').read()
tab=txt.split('## 표 1.')[1].split('\n## ')[0]
out=[];summ={}
for line in tab.splitlines():
    c=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(c)<12 or c[0] not in('이주','입주'): continue
    name=c[1];n=norm(name)
    key=next((v for k,v in ALIAS.items() if n.startswith(k[:5])),None) or (n[:6] if len(n)>=6 else n)
    kn=[no for no,t in nb if key in norm(t)]; ki=[no for no,t in ic if key in norm(t)]
    p=[no for no,t in pub if key in norm(t)]
    s=[x for x in sch if key in norm(x[3]) and x[0]!='발행']
    sp=[x for x in sch if key in norm(x[3]) and x[0]=='발행']
    p=sorted(set(p+[re.search(r'\d{12}',x[4]).group(0) for x in sp if re.search(r'\d{12}',x[4])]))
    res=[x for x in s if x[0]=='예약'];wr=[x for x in s if x[0]=='원고'];tw=[x for x in s if x[0]=='쓸글']
    m=re.search(r'(\d\d)-(\d\d)',c[8]); due=None
    if m:
        mo,dy=int(m.group(1)),int(m.group(2));due=datetime.date(2027 if mo<6 and today.month>6 else 2026,mo,dy)
    own=c[10].startswith('글 있음') or c[10].startswith('있음')
    if p or res or own: stat='올라감' if (p or own) else '예약만'
    elif wr: stat='원고만(미예약)'
    elif tw: stat='일정표에 쓸 글'
    else: stat='없음'
    need=''
    mm=re.match(r'(\d{4})-(\d\d)(?:-(\d\d))?',c[5]); st_date=datetime.date(int(mm.group(1)),int(mm.group(2)),int(mm.group(3) or 1)) if mm else None
    if stat=='없음':
        if due is None: need='날짜 확인 뒤'
        elif c[0]=='입주' and (lambda g:g<300)(int(re.sub(r'\D','',c[3].split('→')[0]) or 0) if re.sub(r'\D','',c[3]) else 999): need='제외(300세대 미만)'
        elif c[0]=='입주' and st_date and (today-st_date).days>30: need='시기 지남(직후·2년차로)'
        elif c[0]=='이주' and st_date and st_date>=today-datetime.timedelta(days=3): need='이번 주 써야 함(이주 시작 임박)'
        elif c[0]=='이주' and re.match(r'\d{4}-\d\d-\d\d',c[6]) and datetime.date.fromisoformat(c[6][:10])>today: need='이주 진행 중: 이사·전세집 글로 쓰면 의미 있음'
        elif c[0]=='이주': need='이주 끝났거나 종료일 미확인: 후순위'
        elif due<today: need='지금 써야 함(글 날 지남)'
        elif (due-today).days<=21: need='3주 안에 써야 함'
        else: need='아직 여유'
    elif stat in('원고만(미예약)','일정표에 쓸 글'): need='예약·작성 이어서'
    pairs.append((c[0],name,c[5],kn,ki))
    out.append((c[0],name,c[5],c[8],stat,len(p),'; '.join(f'{x[1]} {x[2]}' for x in res+tw),need))
    summ[stat]=summ.get(stat,0)+1
pri={'이번 주 써야 함(이주 시작 임박)':0,'이주 진행 중: 이사·전세집 글로 쓰면 의미 있음':1,'이주 끝났거나 종료일 미확인: 후순위':5,'시기 지남(직후·2년차로)':6,'제외(300세대 미만)':7,'지금 써야 함(글 날 지남)':0,'3주 안에 써야 함':1,'예약·작성 이어서':2,'날짜 확인 뒤':3,'아직 여유':4,'':5}
todo=[o for o in out if o[7] in('이번 주 써야 함(이주 시작 임박)','이주 진행 중: 이사·전세집 글로 쓰면 의미 있음','이주 끝났거나 종료일 미확인: 후순위','지금 써야 함(글 날 지남)','3주 안에 써야 함','예약·작성 이어서')]
todo.sort(key=lambda o:(o[0]!='이주',pri[o[7]]))
doc=f'\n## 발행·예약 대조 ({today:%m/%d} 기준 · 자동: watch/master_match.py)\n\n상태: '+' · '.join(f'{k} {v}' for k,v in summ.items())+'\n\n- 올라감 = 발행 글 목록에 단지 이름이 든 글이 있음 · 예약만 = 일정표 예약 칸에만 있음 · 원고만 = 원고는 있으나 예약 안 됨 · 없음 = 글 없음.\n- 이름 일치는 단지 이름 앞 여섯 글자로 어림 대조. 틀린 곳은 표 1 글 상태 칸을 손으로 고친다.\n\n### 더 써야 할 단지 (이주 먼저)\n\n| 구분 | 단지 | 시작 | 부동산 글 날 | 상태 | 할 일 |\n|---|---|---|---|---|---|\n'+'\n'.join(f'| {o[0]} | {o[1]} | {o[2]} | {o[3]} | {o[4]}{" · "+o[6] if o[6] else ""} | {o[7]} |' for o in todo[:60])
doc+='\n\n### 이주 단지 전체 대조\n\n| 단지 | 시작 | 상태 | 발행 글 수 | 예약·쓸 글 | 할 일 |\n|---|---|---|---|---|---|\n'+'\n'.join(f'| {o[1]} | {o[2]} | {o[4]} | {o[5]} | {o[6]} | {o[7]} |' for o in out if o[0]=='이주')
def link(kn,ki):
    if kn=='MAN': return '부동산 원고만(gaepo67_iju · 10/21 올림 기록, 목록엔 없음 → 발행 확인) · 인테리어 11/3 예약 → 둘 다 나오면 서로 링크'
    if kn and ki: return '둘 다 있음 → 서로 링크 확인'
    if kn: return '부동산만 → 인테리어 짝 글 쓰고 링크'
    if ki: return '인테리어만 → 부동산 짝 글 쓰고 링크'
    return '둘 다 없음'
lk='\n### 낭만 부동산 ↔ 낭만 인테리어 상호 링크 (발행 글 기준)\n\n규칙: 입주·이주 단지 글은 부동산(시세·일정·전세)과 인테리어(상품) 짝으로 쓰고, 글 끝 「옆 블로그」 칸에 서로의 주소를 넣는다. 한쪽이 먼저 나오면 다음 글에 링크를 채운다. 발행된 글 본문은 직접 고치지 않고 새 글·고침 글에서 채운다. 링크가 실제 걸렸는지는 본문 확인이 필요하다(미확인).\n\n| 구분 | 단지 | 시작 | 부동산 글 | 인테리어 글 | 해야 할 일 |\n|---|---|---|---|---|---|\n'+'\n'.join(f'| {a} | {b} | {c_} | {('gaepo67_iju' if kn=='MAN' else "/".join(kn) or "-")} | {('gaepo67_ijoo_allinone(예약 11/3)' if kn=='MAN' else "/".join(ki) or "-")} | {link(kn,ki)} |' for a,b,c_,kn,ki in [(a,b,c_,('MAN' if b.startswith('개포주공6') else kn),ki) for a,b,c_,kn,ki in pairs] if (kn or ki) or a=='이주')
base=re.sub(r'\n## 발행·예약 대조.*?(?=\n## 표 1\.|\n## 시점별|\Z)','',txt,flags=re.S)
base=base.replace('\n## 표 1.',doc+lk+'\n\n## 표 1.',1)
open(M,'w',encoding='utf-8').write(base)
print(summ,len(todo))
