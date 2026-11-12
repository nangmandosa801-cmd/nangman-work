import subprocess,re,html,json,os
NR=['224464143654','224464143205','224464142679','224464142056','224464141540','224464141062','224464140561','224464036910','224464036028','224464139141','224464035147','224464138305','224464034261','224464137103','224464033367','224462895487','224462895038','224464031660','224462894471','224462893483','224464030876','224462888236','224462887153','224461117554','224453529026','224461008155','224461589974']
BAD=re.compile(r'010-|champion_chart|nangmaninterior|낭만 인테리어|김수아')
for i,n in enumerate(NR,1):
    u=f'https://blog.naver.com/PostView.naver?blogId=dong_jin_kim&logNo={n}'
    s=subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf-8','replace')
    ps=[html.unescape(re.sub('<[^>]+>','',x)).replace('​','').strip() for x in re.findall(r'se-text-paragraph[^>]*>(.*?)</p>',s,re.S)]
    ps=[p for p in ps if p and not BAD.search(p)]
    title=ps[0] if ps else ''
    cut=next((k for k,p in enumerate(ps) if p.startswith(('같이 보면','함께 보면','#'))),len(ps))
    body=ps[1:cut]
    heads=[p for p in body if p.endswith('?') and len(p)<45][:6]
    nums=[]
    for p in body:
        if re.search(r'\d',p) and 15<len(p)<160 and p not in nums: nums.append(p)
    first=' '.join(body[:6])[:500]
    d=f'NR{i:03d}_{n}'; os.makedirs(d,exist_ok=True)
    t=f'''[클립재료 · 낭만 부동산 분석 플랫폼 · {d}]
제목: {title}
원문: https://blog.naver.com/dong_jin_kim/{n}
(클립 「연결할 글」 = 이 원문)

[글의 첫머리 · 무슨 이야기인가]
{first}

[글 속 질문 소제목]
''' + '\n'.join('- '+h for h in heads) + '''

[확인된 숫자가 든 문장 · 숫자는 여기 있는 것만 쓰기]
''' + '\n'.join('- '+x for x in nums[:14]) + '''

[금지]
- 여기 없는 숫자 · 날짜 · 단지 이름 만들기
- 전화번호 글자 · 낭만 인테리어 언급 · 링크 글자
- 매수 · 매도 권유(「지금 사세요」 등)
'''
    open(f'{d}/재료.txt','w').write(t); print(d,len(nums),title[:30])
