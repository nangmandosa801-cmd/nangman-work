"""입주청소+새집증후군 묶음 손님 접수 → 오렌지(ㅇㄹㅈ ㅎㅋㅇ)에 넘길 문자 + 장부 한 줄.
쓰기: python3 intake.py 단지 평형 청소날 시공날 [손님번호] [메모]
예:   python3 intake.py 한강풍경채어바니티 34 11/28 11/29 010-0000-0000 "84A · 1904호 아님"
"""
import sys,json,os,datetime
P=11000; SJ={30:300000,34:340000}
a=sys.argv[1:]
if len(a)<4: print(__doc__); sys.exit()
danji,py,cd,sd=a[0],int(a[1]),a[2],a[3]; ph=a[4] if len(a)>4 else '(손님 동의 뒤)'; memo=a[5] if len(a)>5 else ''
cl=P*py; sj=SJ.get(py); tot=cl+sj if sj else None
won=lambda n:f'{n//10000}만'+(f' {n%10000//1000}천' if n%10000 else '')+'원'
msg=f"""사장님, 낭만 인테리어 소개 손님입니다.
단지: {danji} · {py}평
청소: {cd} · 새집증후군: {sd}(청소 다음 날)
손님 번호: {ph}
안내한 금액: 청소 {won(cl)}{' + 새집증후군 '+won(sj)+' = '+won(tot) if sj else ' + 새집증후군(평형 확인 뒤 안내)'}{' · 현금영수증 부가세 10% 별도'}
{memo}
일정 되시는지 답 주세요. 낭만 소개 건으로 적어 두겠습니다."""
print(msg)
L='/home/claude/w/orange/intake_ledger.json'
d=json.load(open(L)) if os.path.exists(L) else []
d.append(dict(접수=datetime.datetime.now().strftime('%m/%d %H:%M'),단지=danji,평=py,청소=cd,시공=sd,손님=ph,안내금액=tot,메모=memo,오렌지답='',계약='',수수료=''))
json.dump(d,open(L,'w'),ensure_ascii=False,indent=1)
print(f'\n장부 {len(d)}번째 줄 적음 → {L}')
