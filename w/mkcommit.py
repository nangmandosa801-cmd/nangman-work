import sys,os,json
slug,title=sys.argv[1],sys.argv[2]
d=f'/mnt/user-data/outputs/int/{slug}'
out=[{"stagedPath":f"{d}/{f}","devicePath":f"C:\\블로그\\interior\\[미발행] {title}\\{f}"} for f in sorted(os.listdir(d))]
json.dump(out,open(f'commit_{slug}.json','w',encoding='utf-8'),ensure_ascii=False,indent=0); print(len(out))
