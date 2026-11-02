import sys,json;sys.path.insert(0,'/home/claude/w/sanbon')
from tl import tl
out={}
for b in ['dong_jin_kim','jisandream01','champion_chart','give_me_travel']:
    out[b]=tl(b,8)
    print(b,len(out[b]),out[b][-1][2] if out[b] else '')
json.dump(out,open('pub.json','w'),ensure_ascii=False)
