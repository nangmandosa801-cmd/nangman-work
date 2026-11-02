# -*- coding: utf-8 -*-
import re, urllib.parse, urllib.request, json, time, pickle, os, sys
UA=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
AC='https://ac.search.naver.com/nx/ac?q=%s&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100'
H=pickle.load(open('nam_heads.pkl','rb'))
A=pickle.load(open('nam_ac.pkl','rb')) if os.path.exists('nam_ac.pkl') else {}
def ac(q):
    try:
        with urllib.request.urlopen(urllib.request.Request(AC%urllib.parse.quote(q),headers={'User-Agent':UA}),timeout=10) as x:
            d=json.loads(x.read().decode('utf-8','ignore'))
        return [i[0] for i in d.get('items',[[]])[0]]
    except Exception: return None
for q in H:
    if q in A: continue
    A[q]=ac(q) or []
    time.sleep(0.35)
pickle.dump(A,open('nam_ac.pkl','wb'))
dead=[q for q in H if len(A[q])==0]
live=[q for q in H if len(A[q])>0]
print('앞머리 %d개 · 자동완성 살아있음 %d · 죽음 %d' % (len(H),len(live),len(dead)))
print('\n■ 자동완성 0개 — 제목 앞머리로 쓰면 안 되는 말 (%d개)' % len(dead))
for q in dead: print('   ', q)
