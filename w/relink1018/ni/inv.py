import json,re,os,glob
L="suwon_gansal busan_danggam donam_hansin daejeon_dure changwon_daewon cheongju_jiwell sejong_surubae incheon_gompangi arch_pocheon pocket_jinju busan_sasang changwon_gamgye living_suwon dress_cheonan suwon_narrow bronze_gimhae moru_yangsan six_seoul auto3_okjeong gabyeok_tongyeong jubang_jinhae anbang_saha wood3_daeyeon pocket_gimhae auto_okjeong slim3_onam asym_wolgye swing_onam house_macheon veranda_masan dress_gimhae villa_sash sash_live sink_film door_film room_film frame_film".split()
files=json.load(open('/home/claude/w/relink1018_files.json'))
S=json.load(open('/home/claude/int/serial.json'))['rows']
out={}
for s in L:
    rel=[f for f in files if f.endswith(f'nangman_interior_{s}_paste.html')]
    rel=rel[0] if rel else None
    p='/mnt/user-data/outputs/relink1018/'+rel if rel and os.path.exists('/mnt/user-data/outputs/relink1018/'+rel) else ('/mnt/user-data/uploads/블로그/interior/'+rel if rel else None)
    h=open(p).read() if p else ''
    grp=re.findall(r'\[사진 (\d+)번 · (\d+)장\]',h)
    rows=[c for c,v in S.items() if v['slug']==s]
    d='/mnt/user-data/outputs/int/'+s
    imgs=sorted(os.listdir(d)) if os.path.isdir(d) else None
    py=os.path.exists(f'/home/claude/int/{s}.py')
    out[s]=dict(rel=rel,cur=p,grp=grp,rows=rows,imgs=imgs,py=py)
    print(s,'| rel',bool(rel),'out' if p and 'outputs' in p else 'up','| grp',grp,'| serial',len(rows),rows[:1],'| imgs',None if imgs is None else [i for i in imgs if i.endswith('.jpg')][:3], len(imgs or []),'| py',py)
json.dump(out,open('/home/claude/w/relink1018/ni/inv.json','w'),ensure_ascii=False,indent=1)
