#!/usr/bin/env python3
# 지산드림 한 번에: python3 make_jisan.py <글스크립트.py> <폴더> <slug> <예약일YYYYMMDD> [--helper]
# 1 원고 빌드(SEO·금지어) 2 html을 폴더로 3 겹침 검사(발행 글 전체) 4 원본 txt 저장 5 (--helper · imgurls 있으면) 도우미 → JSON 한 줄
import sys,subprocess,os,re,json,shutil
scr,folder,slug,date=sys.argv[1:5]; helper='--helper' in sys.argv
J='/home/claude/jisan'; B='/mnt/user-data/outputs/jisandream/'; D=B+folder+'/'; os.makedirs(D,exist_ok=True)
r={'slug':slug}
o=subprocess.run(['python3',J+'/'+scr],capture_output=True,text=True,cwd=J); out=o.stdout+o.stderr
m=re.search(r'금지 (\[.*?\])',out); r['banned']=m.group(1) if m else 'ERR'
r['seo_x']=len(re.findall(r'✘',out)); r['seo_miss']=[l.strip()[:120] for l in out.splitlines() if '✘' in l][:3]
src=B+f'jisandream_{slug}_post.html'
if os.path.exists(src): shutil.move(src,D+f'jisandream_{slug}_post.html')
post=D+f'jisandream_{slug}_post.html'
if not os.path.exists(post): r['error']=out[-400:]; print(json.dumps(r,ensure_ascii=False)); sys.exit(1)
p=subprocess.run(['python3',J+'/master/precheck.py',post],capture_output=True,text=True).stdout.strip().splitlines()
r['overlap']=p[-1] if p else '?'
html=open(post).read(); t=re.search(r'font-size:34px[^>]*>([^<]*)<',html).group(1)
exec(open(J+'/html2txt.py').read())
txt=conv(html,t,[]).replace('\n\n[태그] ','')
T='/mnt/user-data/outputs/text/지산드림/'; os.makedirs(T,exist_ok=True)
fn=T+'%s_지산드림_%s.txt'%(date,re.sub(r'_+','_',re.sub(r'[\\/:*?"<>|,·]','',t.replace('~','-')).replace(' ','_')))
open(fn,'w').write(txt); r['txt']=fn; r['title']=t; r['title_len']=len(t)
if helper:
    if os.path.exists(D+f'jisandream_{slug}_imgurls.json'):
        h=subprocess.run(['python3',J+'/helper_build.py',D,slug,'미발행'],capture_output=True,text=True).stdout.strip()
        r['helper']=h.split()[0] if h else 'ERR'
    else: r['helper']='창고 주소(imgurls.json) 없음 — 그림부터'
print(json.dumps(r,ensure_ascii=False))
