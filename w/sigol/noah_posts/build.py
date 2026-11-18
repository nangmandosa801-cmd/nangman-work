import sys,json,html
sys.path.insert(0,'.'); from posts import P,I
B='<div class="post-geo" style="font-size:16px;line-height:1.85;color:#3f4a3a">'
def mk(p):
    h=[B,f'<p><img src="{I[p["img"]]}" alt="{html.escape(p["kw"].split(" · ")[0])} 노아의숲" style="width:100%;border-radius:12px"></p>',
       f'<p><b>{p["intro"]}</b></p>']
    for q,ps in p['sec']:
        h.append(f'<h2 style="font-size:20px;color:#3d5a3a;margin-top:32px">{q}</h2>'); h+= [f'<p>{x}</p>' for x in ps]
    if p.get('faq'):
        h.append('<h2 style="font-size:20px;color:#3d5a3a;margin-top:32px">자주 묻는 질문</h2>')
        for q,a in p['faq']: h.append(f'<p><b>Q. {q}</b><br>{a}</p>')
    h.append('<p style="font-size:13px;color:#888;margin-top:32px">그림은 노아의숲을 바탕으로 그린 그림입니다.<br>참고: '+' · '.join(p['src'])+'</p></div>')
    # FAQPage 구조화 데이터(GEO)
    if p.get('faq'):
        ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]}
        h.append('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>')
    return '\n'.join(h)
out={}
txt=['[노아의숲 홈페이지 글 원고 검수본 · 클로드 1119 · 13편]','']
for p in P:
    out[p['slug']]=dict(title=p['title'],label=p['label'],html=mk(p))
    txt+=[f'■ {p["slug"]} | 라벨 {p["label"]} | 자동완성 확인 검색어: {p["kw"]}',f'제목: {p["title"]}','',p['intro'],'']
    for q,ps in p['sec']: txt+=['[소제목] '+q]+ps+['']
    if p.get('faq'):
        txt.append('[자주 묻는 질문]'); txt+=[f'Q. {q}\nA. {a}' for q,a in p['faq']]; txt.append('')
    txt+=['출처: '+' · '.join(p['src']),'','─'*30,'']
json.dump(out,open('posts.json','w'),ensure_ascii=False,indent=1)
open('노아의숲_홈페이지글_검수본_1119.txt','w').write('\n'.join(txt))
print(len(out), sum(len(v['html']) for v in out.values()))
