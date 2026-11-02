# 3차 결과 점검 + PC에 넣을 목록 만들기
import json,os,re,subprocess,sys,glob
from PIL import Image
OUT='/mnt/user-data/outputs/int/'
m=json.load(open('/home/claude/w/phase2_map.json')); pc=json.load(open('/home/claude/w/pc_interior.json'))
F={it['slug']:it['folder'] for it in m}
N=['slim3_onam','wood3_daeyeon','auto3_okjeong','dress_gimhae','jubang_jinhae','pocket_gimhae','gabyeok_tongyeong','six_seoul','changwon_gamgye','door_film','room_film','frame_film','sash_film','changteul_nusu','lowe','villa_sash']
O=['pocket_jinju','arch_pocheon','bronze_gimhae','living_suwon','dress_cheonan','busan_sasang','busan_danggam','changwon_daewon','daejeon_dure','cheongju_jiwell','sejong_surubae','suwon_narrow','suwon_gansal','donam_hansin','house_macheon','moru_yangsan','swing_onam','veranda_masan','sash_live','sink_film','sash_nusu','suwon_cheongso','bangmyo_jejak','ipju_centerfine','ipju_deungchon','ipju_dongnae','ipju_gwanjeo','ipju_hoecheon','ipju_hwayang_dongmun','ipju_icheon_yemizi','ipju_janghang_jeil','ipju_medialle','ipju_osan_geumgang','ipju_seongdong_xi','ipju_yeonhui_hoban']
def gray(p):
    try:
        im=Image.open(p).convert('RGB').resize((16,16)); px=list(im.getdata())
        return all(abs(r-176)<6 and abs(g-176)<6 and abs(b-176)<6 for r,g,b in px)
    except Exception: return True
def chk(p):
    r=subprocess.run(['python3','/home/claude/int/chk.py',p],capture_output=True,text=True).stdout
    bad=re.search(r'금지어: (.*)',r).group(1); q=re.search(r'인용투 (\d+)',r).group(1); old=re.search(r'옛 말: (.*)',r).group(1)
    x=r.count('✘'); cta='비밀댓글) 있음' in r; hl=None
    return bad,q,old,x,cta,[l.strip() for l in r.splitlines() if '✘' in l]
commit={}; rows=[]
for s in N+O:
    folder=F.get(s); d=OUT+s+'/'
    if not folder or folder not in pc: rows.append((s,'PC 폴더 없음')); continue
    pcf=set(pc[folder]); files=[]
    for f in sorted(os.listdir(d)):
        if f not in pcf: continue
        if f.endswith('.jpg') and (s in O) and gray(d+f): continue
        files.append(f)
    posts=[f for f in files if f.endswith('.html')]
    for p in posts:
        bad,q,old,x,cta,xl=chk(d+p)
        h=open(d+p).read(); refs=set(re.findall(r'(nangman_interior_'+s+r'_[A-Za-z0-9_]+\.(?:jpg|png))',h))
        miss=[r for r in refs if r not in pcf]
        rows.append((s,p.replace('nangman_interior_','').replace(s+'_',''),bad,q,old,x,'문의O' if cta else '문의X',xl,'없는 그림 '+str(miss) if miss else ''))
    commit[s]=[dict(stagedPath=d+f,devicePath='C:\\블로그\\interior\\'+folder+'\\'+f) for f in files]
for r in rows: print(*r,sep=' | ')
json.dump(commit,open('/home/claude/w/commit_v3.json','w'),ensure_ascii=False,indent=0)
print('글',len(commit),'파일',sum(len(v) for v in commit.values()),'jpg',sum(f['stagedPath'].endswith('.jpg') for v in commit.values() for f in v))
