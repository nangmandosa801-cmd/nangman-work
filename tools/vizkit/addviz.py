import json,re
U=json.load(open('viz/urls.json'))
A={'busan_danyeol':[('v_busan_1','그 물을 먹고 곰팡이가 자랍니다.'),('v_busan_2','그 안에서 다시 핍니다.')],
 'daegu_gompang':[('v_daegu_2','석고보드 · 도배 마감'),('v_daegu_1','50mm로 붙였습니다.')],
 'veranda_hwakjang':[('v_veranda_1','거기서 물이 맺힙니다.'),('v_veranda_2','이음새 · 코너')],
 'cheonjang_gyeolro':[('v_cheon_1','단열을 해야 멈춥니다.'),('v_cheon_2','폼으로 채웁니다.')],
 'gompang_biyong':[('v_biyong_2','다시 안 피게 하려면 뒤쪽입니다.'),('v_biyong_1','약 127만원이었습니다.')],
 'gyeolro_seipja':[('v_seip_1','60% 아래인데도 맺히면 단열 문제'),('v_seip_2','환기와 제습부터 봅니다.')]}
for s,L in A.items():
    fn=f'nangman_interior_{s}.json';d=json.load(open(fn));h=d['html']
    h=re.sub(r'<p data-viz[^>]*>.*?</p>','',h)
    for n,a in L:
        i=h.index(a); m=re.compile(r'</(p|table)>').search(h,i); j=m.end()
        h=h[:j]+f'<p data-viz style="text-align:center"><img src="{U[n]}" data-v="{n}" style="width:100%;max-width:720px"></p>'+h[j:]
    d['html']=h;json.dump(d,open(fn,'w'),ensure_ascii=False);print(s,h.count('data-viz'))
