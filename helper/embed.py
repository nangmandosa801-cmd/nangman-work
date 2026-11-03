import json,re,sys
src,urls,prefix,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
heads=json.loads(sys.argv[5])  # {key: heading}
U=json.load(open(urls)); s=open(src).read()
def img(k): return f'<p style="text-align:center;"><img src="{U[k]}" width="693" style="width:100%;max-width:693px;" alt="{k}"></p>\n'
for k in U:
    if k in heads or k=='thumb': continue
    fn=f'{prefix}_{k}.png'
    pat=re.compile(r'<table[^>]*>(?:(?!</table>).)*?'+re.escape(fn)+r'(?:(?!</table>).)*?</table>',re.S)
    s,n=pat.subn(img(k),s,count=1); print(k,n)
s=img('thumb')+'<p><br></p>\n'+s
for k,h in heads.items():
    key=f'>{h}</p>\n<p><br></p>\n'; assert key in s,h
    s=s.replace(key,key+img(k)+'<p><br></p>\n',1)
open(out,'w').write(s); print('imgs',s.count('<img'))
