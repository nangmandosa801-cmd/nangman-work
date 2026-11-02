# 공부 채팅이 낭만 부동산 · 낭만 인테리어 글에 링크를 걸 수 있게 발행 글 전체 목록을 프로젝트 문서로 만든다 (10/15 사용자 「공부창에서 링크를 부동산 인테리어 쪽으로 걸어야 하니깐」)
import subprocess,re,urllib.parse,json,datetime,os
def get(b,p):
    return subprocess.run(['curl','-sS','-m','30','-A','Mozilla/5.0','-H','Referer: https://blog.naver.com/'+b,
      f'https://blog.naver.com/PostTitleListAsync.naver?blogId={b}&currentPage={p}&countPerPage=30&categoryNo=0&viewdate=&parentCategoryNo=0'],capture_output=True,text=True).stdout
def pubs(b):
    out=[];seen=set()
    for p in range(1,30):
        t=get(b,p); items=re.findall(r'"logNo":"(\d+)","title":"([^"]*)".*?"addDate":"([^"]*)"',t)
        new=[(l,urllib.parse.unquote_plus(ti),d) for l,ti,d in items if l not in seen]
        if not new: break
        for x in new: seen.add(x[0]); out.append(x)
    return out
now=(datetime.datetime.utcnow()+datetime.timedelta(hours=9))
def day(d):
    m=re.match(r'(\d+)시간 전',d)
    if m: return (now-datetime.timedelta(hours=int(m.group(1)))).strftime('%Y.%m.%d')
    m=re.match(r'(\d{4})\. (\d+)\. (\d+)',d)
    return f'{m.group(1)}.{int(m.group(2)):02d}.{int(m.group(3)):02d}' if m else d
L=['# 낭만 부동산 · 낭만 인테리어 발행 글 목록 (공부 블로그 링크용)','',
 f'만든 때: {now:%Y-%m-%d %H:%M} · 매일 아침 정기 작업 「발행 글 목록 새로 고침」이 다시 만든다. 공부 채팅은 개념과 맞는 글을 이 목록에서 골라 주소(https://blog.naver.com/<블로그>/<번호>)로 건다. 쓴 짝은 `claude/공부블로그_링크장부.md` 아래쪽 목록에 더한다.','']
for b,name in (('dong_jin_kim','낭만 부동산 분석 플랫폼'),('champion_chart','낭만 인테리어')):
    P=pubs(b); L+=[f'## {name} ({b}) · {len(P)}편','','| 날 | 번호 | 제목 |','|---|---|---|']
    for l,t,d in P: L.append(f'| {day(d)} | {l} | {t.replace("|","/")} |')
    L.append('')
open('/home/claude/proj/발행글_목록_부동산_인테리어.md','w').write('\n'.join(L)); print(len(L))
