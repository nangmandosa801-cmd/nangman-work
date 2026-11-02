import sys
s=open('/home/claude/w/inq1022/doc.md').read()
row="| 2026-10-22 | 인테리어 | 외풍 차단 — 상가 약국 출입문 2개(바깥 프레임 없는 강화유리 양개문 · 안쪽 자동 미닫이 유리문) · 작년엔 투명 비닐 + 스펀지로 막았다가 벗겨짐 · 유리에 필름은 안 됨(가게가 어두워짐) | 서울 마포 도화동(공덕역 앞) | 외풍 차단 글 검색으로 전화(11:5x 통화) · 사진 6장 받음 | 문수리 임반장(수도권 문 수리) 견적 요청 예정 · 자동문은 따로 확인 | 사진 받음 · 견적 대기 | — | 임반장 |\n"
anchor="\n## 주간 숫자"
s=s.replace(anchor, row.rstrip('\n')+"\n"+anchor,1) if False else s.replace("| 소소리 10% |\n","| 소소리 10% |\n"+row,1)
open('/home/claude/w/inq1022/doc.md','w').write(s)
