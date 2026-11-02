import json,html,os,re
exec(open('tailbuild.py').read().split("A='style")[0])
res=json.load(open('/tmp/claude-0/tailexist.json'))
import difflib
def norm(x): return re.sub(r'[\s|,·()]','',x)
def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
def match(txt):
    b=max(T,key=lambda no:sim(txt,T[no])); return b if sim(txt,T[b])>=0.72 else None
fixed=[]
A='style="color:#2E5C8A;text-decoration:none;border-bottom:1px solid #B8C6D6;"'
HEAD=('<table width="100%" style="width:100%;border-collapse:collapse;"><tr><td style="border-top:3px solid #2E5C8A;width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid #C8D2DE;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>\n<p><br></p>\n'
      '<p style="font-size:24px;font-weight:700;color:#1F3864;">함께 보면 좋은 글</p>\n<p><br></p>\n')
def item(n,d):
    return (f'<p style="font-size:18px;font-weight:700;"><a href="https://blog.naver.com/dong_jin_kim/{n}" {A}>{html.escape(T[n])}</a>'
            +(f'<br>\n<span style="font-size:15px;color:#7A8590;">{html.escape(d)}</span>' if d else '')+'</p>\n<p><br></p>\n')
base='/mnt/user-data/outputs/tails2'; os.makedirs(base,exist_ok=True)
man=[];stat=[]
for tgt in G:
    seen=set([tgt]); rows=[]
    for n in G[tgt]:
        if n in seen: continue
        seen.add(n); rows.append((n,DESC.get(n,'')))
    old=0
    if tgt!='224377990326':
        for n,d,txt in res.get(tgt,{}).get('items',[]):
            if n and n in T and n!='224377990326' and sim(txt,T[n])<0.5:
                m=match(txt); fixed.append((T[tgt][:15],txt[:25],T[n][:20],T[m][:20] if m else None)); n=m
                if not m: continue
            if not n or n in seen or n not in T: continue
            seen.add(n); rows.append((n,d)); old+=1
    body=(HEAD if tgt!='224377990326' else '')+''.join(item(n,d) for n,d in rows)
    fn=f'{base}/nangman_{tgt}_tail.html'; open(fn,'w').write(body)
    name=T[tgt].replace('|','｜').replace('~','～').replace('/','／').replace(':','：').replace('?','？').replace('"','＂').strip()
    man.append((fn,f'C:\\블로그\\nangman\\[자료] 꼬리링크 - 0930 업어치기\\{name}\\nangman_{tgt}_tail.html'))
    stat.append((len(G[tgt]),old,T[tgt][:30]))
json.dump(man,open('/tmp/claude-0/tailman2.json','w'),ensure_ascii=False)
for s in stat: print(s)

for f in fixed: print('FIX',f)
