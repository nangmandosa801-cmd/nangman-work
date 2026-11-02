import json,re,os,sys
R={r['slug']:r for r in json.load(open('/home/claude/sched/convert_res.json'))}
SRC={'suwon_gansal':'sun_suwon.py','suwon_narrow':'sun_suwon.py','busan_danggam':'modern.py','changwon_daewon':'modern.py','busan_sasang':'modern.py',
'donam_hansin':'sg_donam_hansin.py','daejeon_dure':'clover.py','cheongju_jiwell':'clover.py','sejong_surubae':'clover.py','incheon_gompangi':'n1008/p27_incheon_gompangi.py',
'arch_pocheon':'sg_arch.py','pocket_jinju':'sg_pocket.py','changwon_gamgye':'n1007/p10_changwon.py','living_suwon':'sg_living.py','dress_cheonan':'sg_dress.py','bronze_gimhae':'sg_bronze.py',
'moru_yangsan':'sg_moru_yangsan.py','six_seoul':'n1007/p09_six.py','auto3_okjeong':'n1007/p03_auto3.py','gabyeok_tongyeong':'n1007/p08_gabyeok.py','jubang_jinhae':'n1007/p06_jubang.py',
'anbang_saha':'n1007/p05_anbang.py','wood3_daeyeon':'n1007/p02_wood3.py','pocket_gimhae':'n1007/p07_pocket.py','auto_okjeong':'sg_auto_okjeong.py','slim3_onam':'n1007/p01_slim3.py',
'asym_wolgye':'sg_asym_wolgye.py','swing_onam':'sg_swing_onam.py','house_macheon':'sg_house_macheon.py','veranda_masan':'sg_veranda_masan.py','dress_gimhae':'n1007/p04_dress.py',
'villa_sash':'n1007/p17_villa.py','sash_live':'sg_sash_live.py','sink_film':'sg_sink_film.py','door_film':'n1007/p11_door_film.py','room_film':'n1007/p12_room_film.py','frame_film':'n1007/p13_frame_film.py'}
json.dump(SRC,open('src.json','w'),ensure_ascii=False)
for s in sys.argv[1:]:
    t=open('/home/claude/int/'+SRC[s]).read()
    names=[a[len('nangman_interior_'+s+'_'):-4] for a,b in R[s]['map'] if a.endswith('.jpg')]
    print('=====',s,SRC[s],names)
    for l in t.split('\n')[:6]:
        if '출처' in l: print('  H',l[:500])
    if SRC[s] in('modern.py','clover.py','sun_suwon.py'):
        i=t.find("'"+s+"'"); print('  CTX',t[max(0,i-300):i+1500].replace('\n','\n    ')[:2500]); continue
    for n in names:
        for l in t.split('\n'):
            if "'"+n+"'" in l and ('(' in l): print('  P',l.strip()[:260]); break
        else: print('  P?',n)
