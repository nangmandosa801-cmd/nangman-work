import json,re,sys
SRC=json.load(open('src.json'))
R={r['slug']:r for r in json.load(open('/home/claude/sched/convert_res.json'))}
for s in sys.argv[1:]:
    t=open('/home/claude/int/'+SRC[s]).read()
    names=[a[len('nangman_interior_'+s+'_'):-4] for a,b in R[s]['map'] if a.endswith('.jpg')]
    print('=====',s,SRC[s])
    L=t.split('\n')
    for l in L[:14]:
        if l.startswith('#') and ('출처' in l or '업체' in l or re.search(r'\d{12}',l)): print('  H',l[:420])
    for l in L[:40]:
        if re.match(r'^[A-Za-z_,0-9 ]+=\s*[\'"(\[]',l) and re.search(r'\d{9,}|blog|/home',l): print('  V',l[:300])
    for n in names:
        for l in L:
            if "'"+n+"'" in l and '(' in l: print('  P',l.strip()[:230]); break
        else: print('  P?',n)
