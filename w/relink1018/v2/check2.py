# 2차 현행화 점검 — 75편 최종본(2차 결과 → 1차 결과 → 원본 순)
import json,re,os,sys
sys.path.insert(0,'/home/claude/w/relink1018/v2'); import forb
B='/mnt/user-data/uploads/블로그/interior/'; O='/mnt/user-data/outputs/relink1018/'
sel=json.load(open('/home/claude/w/relink1018_files.json'))
pub=dict((i,t) for i,t in json.load(open('/home/claude/pub/int_live_1018.json')))
TBI={x['log']:x for x in json.load(open('/home/claude/watch/tailboost/tail_boost.json'))['items']}
rows=[]
for s in sel:
    p=O+s if os.path.exists(O+s) else B+s; h=open(p).read()
    k=h.find('같이 보면 좋은 글'); tg=[m.start() for m in re.finditer(r'<p style="font-size:1[57]px;color:#8A8578;">#',h)]
    tail=h[k:(tg[-1] if tg and tg[-1]>k else len(h))] if k>0 else ''
    ids=re.findall(r'champion_chart/(\d{12})',h); tids=re.findall(r'champion_chart/(\d{12})',tail); utids=list(dict.fromkeys(tids))
    # 카드 한 장에 같은 주소가 두 번(제목 · 화살표) 들어가므로 카드형은 짝으로 센다
    dup=[i for i in utids if tids.count(i)>(2 if 'border-top:3px solid #1F3864' in h[max(0,k-400):k] else 1)]
    t=re.sub(r'<[^>]+>','',h)
    phones=sorted(set(re.findall(r'01[016789]-?\d{3,4}-?\d{4}',t)))
    ask=re.search(r'사는 지역과 연락처를? 비밀댓글로 남겨 주세요\.\s*([^.<]*연결해 드립니다)',t)
    r=dict(file=s,folder=s.split('/')[0][5:16].strip(),slug=os.path.basename(s)[17:-11],
      dead=[i for i in ids if i not in pub],ph=len(re.findall(r'발행 예정|\(예정\)|준비 중',t)),tail=len(utids),tb=sum(1 for i in utids if i in TBI),dup=dup,
      forb=[w for w,_ in forb.hits(h)],phones=phones,phone_ok=all(x.replace('-','')=='01076789967' for x in phones),
      ask=bool(ask),ireo=len(re.findall(r'이어 드립니다',re.sub(r'<a [^>]*>.*?</a>','',h))),head='이 글은 낭만 인테리어가' in h,
      tail_before_tags=bool(k>0 and tg and k<tg[-1]),heads=h.count('같이 보면 좋은 글'),other=len(re.findall(r'blog\.naver\.com/(?!champion_chart)',tail)))
    rows.append(r)
json.dump(rows,open('/home/claude/w/relink1018/v2/check2.json','w'),ensure_ascii=False,indent=1)
bad=lambda r: r['dead'] or r['ph'] or r['tail']<5 or r['tb']<2 or r['dup'] or r['forb'] or not r['phone_ok'] or not r['ask'] or r['ireo'] or not r['head'] or not r['tail_before_tags'] or r['heads']!=1 or r['other']
for r in rows:
    if bad(r): print(r['folder'],r['slug'],{k:v for k,v in r.items() if k not in('file','folder','slug')})
print('총',len(rows),'· 문제',sum(1 for r in rows if bad(r)),'· 죽은 링크',sum(len(r['dead']) for r in rows),'· 발행 예정',sum(r['ph'] for r in rows),
      '· 꼬리<5',sum(r['tail']<5 for r in rows),'· 첫화면밖<2',sum(r['tb']<2 for r in rows),'· 금지어',sum(len(r['forb']) for r in rows),'· 번호 이상',sum(not r['phone_ok'] for r in rows),
      '· 문의문장 없음',sum(not r['ask'] for r in rows),'· 이어 드립니다',sum(r['ireo'] for r in rows))
