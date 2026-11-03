import json,sys
src,prefix,out=sys.argv[1],sys.argv[2],sys.argv[3]; heads=json.loads(sys.argv[4])  # {key:[heading,caption]}
s=open(src).read()
def box(fn,cap): return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border:1px dashed #9FB3C8;padding:14px;text-align:center;"><span style="font-size:17px;color:#1F3864;">[그림] {fn} — {cap}</span></td></tr></table>\n<p><br></p>\n'
for k,(h,cap) in heads.items():
    key=f'>{h}</p>\n<p><br></p>\n'; assert key in s,h
    s=s.replace(key,key+box(f'{prefix}_{k}.png',cap),1)
open(out,'w').write(s); print('boxes',s.count('[그림]'))
