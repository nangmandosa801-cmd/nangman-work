import json,sys,subprocess
m=json.load(open(sys.argv[1])); bad=0
for k,u in m.items():
    r=subprocess.run(['curl','-sI','-m','30',u],capture_output=True,text=True).stdout
    ok=(' 200' in r.split('\n')[0]) and 'image/' in r.lower()
    if not ok: bad+=1; print('BAD',k,r.split('\n')[0])
print(len(m),'bad',bad)
