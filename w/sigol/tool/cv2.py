import sys,re,html
t=open(sys.argv[1],encoding='utf-8').read().split('\n')
title=cat=tags=''
body=[]
for l in t:
    if l.startswith('제목:'):title=l[3:].strip();continue
    if l.startswith('카테고리:'):cat=l[5:].strip();continue
    if l.startswith('태그:'):tags=l[3:].strip();continue
    body.append(l)
out=[];i=0
def inl(s):
    s=html.escape(s,quote=False)
    m=re.match(r'^(.*?) \((https?://[^)\s]+)\)$',s)
    if m: return '<a href="%s">%s</a>'%(m.group(2),m.group(1))
    return s
while i<len(body):
    l=body[i].rstrip()
    if not l or l.startswith('[그림'):i+=1;continue
    if l.startswith('## '):out.append('<h2>%s</h2>'%inl(l[3:]));i+=1;continue
    if l.startswith('■ '):out.append('<p><b>%s</b></p>'%inl(l[2:]));i+=1;continue
    if l.startswith('|'):
        rows=[]
        while i<len(body) and body[i].startswith('|'):
            r_=[c.strip() for c in body[i].strip().strip('|').split('|')]
            if not all(re.match(r'^:?-+:?$',c) for c in r_): rows.append(r_)
            i+=1
        h='<table style="width:100%;border-collapse:collapse" border="1"><tbody>'
        for r,row in enumerate(rows):
            tag='th' if r==0 else 'td'
            h+='<tr>'+''.join('<%s style="padding:6px">%s</%s>'%(tag,inl(c),tag) for c in row)+'</tr>'
        out.append(h+'</tbody></table>');continue
    if l.startswith('- ') and '발행 예정' in l:
        i+=1;continue
    if l.startswith('- '):
        its=[]
        while i<len(body) and body[i].startswith('- ') and '발행 예정' not in body[i]:
            its.append('<li>%s</li>'%inl(body[i][2:]));i+=1
        out.append('<ul>'+''.join(its)+'</ul>');continue
    out.append('<p>%s</p>'%inl(l));i+=1
import json
print(json.dumps({'title':title,'cat':cat,'tags':[x.lstrip('#') for x in tags.split()],'html':''.join(out)},ensure_ascii=False))
