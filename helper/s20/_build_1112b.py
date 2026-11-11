# 11/12 2차: 표 그림 · 카드 추가 뒤 그림 올리기 → mk → 어사이드 html · txt · jpg (로컬만, 업로드는 따로)
import json,glob,subprocess,os,re,sys
D=sys.argv[1:] or ['hakgun_ep1','daechi_price','mokdong_school','banpo_school','junggye_school','bundang_school','pyeongchon_school','gwanggyo_school','songdo_school','mapo_school','gwangjang_school','ilsan_school','dunsan_school','beomeo_school','busan_school','bongseon_school','hakgun_final','detective_01','budget_01']
BAD=re.compile(r'PENDING|pending\.invalid|TEMP|drive-pending')
def up(f):
    r=subprocess.run(['python3','/home/claude/helper/gas.py','image',f],capture_output=True,text=True)
    s=r.stdout
    try: j=json.loads(s)
    except Exception: return 'ERR '+(r.stderr or s)[-300:]
    if isinstance(j,str): return j
    return j.get('url') or next((v for v in j.values() if isinstance(v,str) and v.startswith('http')),'')
out={}
for d in D:
    os.chdir(f'/home/claude/helper/s20/{d}')
    try:
        for f in glob.glob('*_helper.html'): os.remove(f)
        subprocess.run(['python3','mk.py'],check=True,capture_output=True)
        u=json.load(open('urls.json')) if os.path.exists('urls.json') else {}
        n_up=0
        for f in sorted(glob.glob('img/*.png')):
            k=re.sub(rf'^nangman_{d}_','',os.path.basename(f))[:-4]
            if not u.get(k,'').startswith('http') or BAD.search(u.get(k,'')) or k.startswith(('3_t','3_pay','4_','5_')):
                url=up(f)
                if not url.startswith('http'): raise Exception('image fail '+f+' '+url)
                u[k]=url; n_up+=1
                json.dump(u,open('urls.json','w'),ensure_ascii=False,indent=1)
        subprocess.run(['python3','mk.py'],check=True,capture_output=True)
        a=subprocess.run(['python3','/home/claude/tools/postkit/html2aside.py','.',f'nangman_{d}'],capture_output=True,text=True)
        b=subprocess.run(['python3','/home/claude/tools/postkit/html2aside_html.py','.',f'nangman_{d}'],capture_output=True,text=True)
        h=open(f'/home/claude/w/aside_out/nangman_{d}.html',encoding='utf-8').read()
        jpg=len(glob.glob(f'/home/claude/w/aside_out/nangman_{d}/*.jpg'))
        marks=h.count('▼ 사진')
        txt=open('post.txt',encoding='utf8').read()+open(f'/home/claude/w/aside_out/nangman_{d}.txt',encoding='utf8').read()
        bad=sorted(set(re.findall(r'고요|갈렸|갈랐|갈라|최고|champion_chart|낭만 인테리어|PENDING|pending\.invalid|TEMP_',txt+h)))
        out[d]={'up':n_up,'jpg':jpg,'marks':marks,'bad':bad,'aside':json.loads(a.stdout.strip().split('\n')[0]).get('bad') if a.stdout else a.stderr[-200:]}
    except Exception as e:
        out[d]={'err':str(e)[:300]}
    print(d,json.dumps(out[d],ensure_ascii=False),flush=True)
json.dump(out,open('/home/claude/helper/s20/_build_1112b.json','w'),ensure_ascii=False,indent=0)
