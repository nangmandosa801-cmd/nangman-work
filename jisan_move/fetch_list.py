import json, sys, urllib.parse, requests, time, re
bid=sys.argv[1]; out=[]
for p in range(1,30):
    r=requests.get(f"https://blog.naver.com/PostTitleListAsync.naver?blogId={bid}&viewdate=&currentPage={p}&categoryNo=0&parentCategoryNo=0&countPerPage=30",headers={"Referer":f"https://blog.naver.com/{bid}"},timeout=20)
    t=r.text.replace("\\'","'")
    d=json.loads(t)
    pl=d.get("postList",[])
    if not pl: break
    for x in pl:
        out.append((urllib.parse.unquote_plus(x["addDate"]),x["logNo"],urllib.parse.unquote_plus(x["title"]).replace("|","/")))
    if len(pl)<30: break
    time.sleep(0.3)
json.dump(out,open(f"/home/claude/jisan_move/{bid}.json","w"),ensure_ascii=False)
print(len(out)); [print(*o,sep=" | ") for o in out[:40]]

import datetime
L=["# 지산드림 발행 글 목록 (다른 블로그 링크용)","",
"만든 때: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+" · 지산드림 채팅이 새로 받을 때마다 다시 만든다. 낭만 부동산 · 낭만 인테리어 · 티스토리 · 구글 블로그 채팅은 지역 · 매물이 맞는 글을 여기서 골라 주소(https://blog.naver.com/jisandream01/<번호>)로 건다.","",
f"## 지산드림 (jisandream01) · {len(out)}편","","| 날 | 번호 | 제목 |","|---|---|---|"]
for a,n,t in out: L.append(f"| {a.strip().rstrip('.')} | {n} | {t} |")
open("/home/claude/jisan_move/jisan_list.md","w").write("\n".join(L)+"\n")
