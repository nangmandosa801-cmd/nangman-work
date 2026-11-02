import re,html,sys
def txt(p):
    s=open(p).read(); s=s.split('같이 보면 좋은 글')[0]
    t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S); t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t=re.sub(r'</td>|</th>',' | ',t); t=re.sub(r'<br\s*/?>|</p>|</h\d>|</div>|</li>|</tr>','\n',t)
    return re.sub(r'\n\s*\n+','\n',html.unescape(re.sub(r'<[^>]+>','',t)))
for a in sys.argv[1:]:
    p=a if a.endswith('.html') else f'/mnt/user-data/outputs/int/{a}/nangman_interior_{a}_post.html'
    print('=====',a); print(txt(p))
