import json,html
P=json.load(open('/tmp/claude-0/pub_now.json')); Lk=json.load(open('/tmp/claude-0/links.json'))
T={no:t for no,t,d in P}
DESC={'224426423870':'2차 선정 5곳과 빠진 효자촌의 가격입니다',
'224422463981':'초이동에서 확정된 것과 건의 단계인 것을 나눴습니다',
'224425144688':'서울 5억대 3,974건, 같은 돈으로 사는 넓이입니다',
'224425288775':'토지거래허가 지정 직전과 직후 거래를 셌습니다',
'224422009186':'GTX-A가 열린 뒤 운정 가격입니다',
'224422338298':'공원과 놀이터가 법에서 어떻게 다른지입니다',
'224422140276':'평촌 선도지구와 2차 신청 단지의 가격입니다',
'224422066734':'일산 선도지구와 나머지 단지의 가격입니다',
'224422350601':'소유자 동의를 누구로 세는지입니다',
'224416484050':'3기 신도시 중 입주가 가장 늦은 이유입니다',
'224416473291':'3기 신도시 다섯 곳을 항목별로 비교했습니다',
'224423406304':'같은 단지 안 임대동 옆 동 가격입니다',
'224422958913':'계양 청약 가격을 주변 새 아파트와 비교했습니다',
'224422778105':'동탄과 광교가 19억까지 간 시간입니다',
'224423295333':'구축을 고칠 때 순서입니다',
'224417236360':'용적률을 깎는 구역입니다',
'224417206389':'개발행위허가를 묶는 기간입니다',
'224415184061':'화성국제테마파크 일정이 늦어진 과정입니다',
'224415206586':'동북권 구축과 신축 가격입니다',
'224413658396':'성장관리계획구역에서 풀어주는 건폐율·용적률입니다',
'224421990760':'1차에 빠진 단지들이 따라잡은 과정입니다',
'224422187601':'재건축과 재개발 조합원이 되는 방법입니다',
'224414230923':'노원·도봉·강북 전세가율과 가격입니다'}
M={'224426423870':['224421990760','224411802216','224422140276','224422066734'],
'224422463981':['224416465303','224386383560','224409413552'],
'224425144688':['224414230923','224415206586','224401277281','224414054216'],
'224425288775':['224383649942','224387479639','224394543980','224386181571'],
'224422009186':['224417043722','224401854235','224409663188'],
'224422338298':['224422187601','224422350601','224409353359'],
'224422140276':['224421990760','224411802216','224422066734'],
'224422066734':['224421990760','224411802216','224422140276'],
'224422350601':['224422187601','224412341795','224409575947'],
'224416484050':['224416473291','224381460159','224383525900','224422958913'],
'224416473291':['224390827296','224422958913'],
'224423406304':['224409734321','224410297285'],
'224422958913':['224416473291'],
'224422778105':['224409663188','224387820020'],
'224423295333':['224381189036'],
'224417236360':['224413658396','224413642108'],
'224417206389':['224413642108','224410258088'],
'224415184061':['224417170873'],
'224415206586':['224411589685','224414230923'],
'224413658396':['224407725817']}
G={}
for new,targets in M.items():
    for t in targets:
        if new in Lk.get(t,[]): continue
        G.setdefault(t,[]).append(new)
hubmiss=[no for no in T if no not in Lk['224377990326'] and no!='224377990326']
G.setdefault('224377990326',[]).extend(hubmiss)
for k in G: DESC.setdefault(k,'')
A='style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #B8C6D6;"'
def block(nos):
    s=''
    for n in nos:
        d=DESC.get(n,'')
        s+=f'<p style="font-size:18px;font-weight:700;"><a href="https://blog.naver.com/dong_jin_kim/{n}" {A}>{html.escape(T[n])}</a>'+(f'<br>\n<span style="font-size:15px;color:#7A8590;">{d}</span>' if d else '')+'</p>\n<p><br></p>\n'
    return s
order=sorted(G,key=lambda t:(t!='224377990326',-len(G[t])))
out=['<!doctype html><html><head><meta charset="utf-8"><title>꼬리링크 추가 작업 0930</title></head><body style="font-family:sans-serif;max-width:860px;margin:auto;padding:20px;">',
f'<h1 style="color:#1F3864;">꼬리링크 추가 작업 · 2026-09-30</h1><p>수정할 글 {len(G)}편 · 제목을 복사해 블로그에서 검색 → 각 글 꼬리 맨 아래에 아래 링크 블록을 붙여넣기</p><hr>']
for i,t in enumerate(order,1):
    out.append(f'<h2 style="font-size:17px;background:#F4F6F9;padding:10px;border-left:4px solid #B5533C;">{i}. 수정할 글 (검색용 정확한 제목)<br><span style="font-size:19px;color:#1F3864;user-select:all;">{html.escape(T[t])}</span><br><span style="font-size:13px;color:#888;">https://blog.naver.com/dong_jin_kim/{t} · 추가 {len(G[t])}개</span></h2>')
    out.append('<div style="border:1px dashed #C8D2DE;padding:14px;margin-bottom:30px;">'+block(G[t])+'</div>')
out.append('</body></html>')
open('/mnt/user-data/outputs/nangman_tail_0930.html','w').write('\n'.join(out))
print(len(G), sum(len(v) for v in G.values()))
for t in order: print(len(G[t]), T[t])

import os
os.makedirs('/mnt/user-data/outputs/tails',exist_ok=True)
man=[]
for t in order:
    body=block(G[t]).rstrip()
    fn=f'/mnt/user-data/outputs/tails/nangman_{t}_tail.html'
    open(fn,'w').write(body+'\n')
    name=T[t].replace('|','｜').replace('~','～').replace('/','／').replace(':','：').replace('?','？').replace('"','＂').strip()
    name=' '.join(name.split())
    man.append((fn,'C:\\블로그\\nangman\\[자료] 꼬리링크 - '+name+'\\'+os.path.basename(fn)))
json.dump(man,open('/tmp/claude-0/tailman.json','w'),ensure_ascii=False)
print(len(man)); print(man[0][1])
