import json,sys
slug=sys.argv[1]; pairs=sys.argv[2:]
d={x['stagedPath'].rsplit('/',1)[1]:x['devicePath'] for x in json.load(open(f'commit_{slug}.json'))}
out=[];
for p in pairs:
    f,u=p.split('=')
    out.append({'fileUuid':u,'devicePath':d[f]})
miss=set(d)-{p.split('=')[0] for p in pairs}
print(json.dumps(out,ensure_ascii=False)); print('MISSING',miss,file=sys.stderr)
