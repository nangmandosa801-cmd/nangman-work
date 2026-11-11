import json,glob,subprocess,os,re,sys
D=['hakgun_ep1','daechi_price','mokdong_school','banpo_school','junggye_school','bundang_school','pyeongchon_school','gwanggyo_school','songdo_school','mapo_school','gwangjang_school','ilsan_school','dunsan_school','beomeo_school','busan_school','bongseon_school','hakgun_final','detective_01','budget_01']
BAD=re.compile(r'PENDING|pending\.invalid|TEMP_|drive-pending')
def up(f):
    r=subprocess.run(['python3','/home/claude/helper/gas.py','image',f],capture_output=True,text=True)
    s=r.stdout; j=json.loads(s[s.index('{'):]) if '{' in s else {}
    return j.get('url','')
out={}
for d in D:
    os.chdir(f'/home/claude/helper/s20/{d}')
    try:
        u=json.load(open('urls.json')) if os.path.exists('urls.json') else {}
        imgs=sorted(glob.glob('img/*.png'))
        for f in imgs:
            k=re.sub(r'^.*?_(\d_[^.]+|thumb)\.png$',r'\1',os.path.basename(f))
            if k not in u or BAD.search(u.get(k,'')) or not u.get(k,'').startswith('http'):
                url=up(f)
                if not url.startswith('http'): raise Exception('image fail '+f)
                u[k]=url
        json.dump(u,open('urls.json','w'),ensure_ascii=False,indent=1)
        subprocess.run(['python3','mk.py'],capture_output=True)
        a=subprocess.run(['python3','/home/claude/tools/postkit/html2aside.py','.',f'nangman_{d}','--up'],capture_output=True,text=True).stdout[-120:]
        b=subprocess.run(['python3','/home/claude/tools/postkit/html2aside_html.py','.',f'nangman_{d}','--up'],capture_output=True,text=True).stdout[-120:]
        n=len(glob.glob(f'/home/claude/w/aside_out/nangman_{d}/*.jpg'))
        h=open(f'/home/claude/w/aside_out/nangman_{d}.html',encoding='utf-8').read()
        out[d]={'ok':True,'photos':n,'bad':bool(BAD.search(h)),'interior':h.count('champion_chart')}
    except Exception as e:
        out[d]={'ok':False,'err':str(e)[:100]}
    for f in glob.glob('*_helper.html'): os.remove(f)
print(json.dumps(out,ensure_ascii=False,indent=0))
