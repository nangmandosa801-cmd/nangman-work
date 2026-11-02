import json,re,sys
inv=json.load(open('inv.json'))
R={r['slug']:r for r in json.load(open('/home/claude/sched/convert_res.json'))}
for s in sys.argv[1:]:
    h=open(inv[s]['cur']).read()
    m={b.split('.')[0]:a[len('nangman_interior_'+s+'_'):] for a,b in R[s]['map']}
    print('=====',s)
    for x in re.finditer(r'<p style="font-size:2[67]px;font-weight:700[^"]*">(.*?)</p>|\[사진 (\d+)번 · (\d+)장\]|<b style="color:#[0-9A-F]+;font-size:21px;">(.*?)</b>|\[배너\]|같이 보면 좋은 글|비밀댓글',h):
        if x.group(1): print('  H',re.sub('<[^>]+>','',x.group(1))[:60],x.start())
        elif x.group(2): g=x.group(2); print('    PH',g,[m.get(f'{g}-{k}') for k in range(1,int(x.group(3))+1)],x.start())
        elif x.group(4): print('    BOX',x.group(4)[:40],x.start())
        else: print('    ',x.group(0),x.start())
