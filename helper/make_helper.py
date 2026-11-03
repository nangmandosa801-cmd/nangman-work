#!/usr/bin/env python3
"""낭만 부동산 발행 도우미 한 번에 만들기.
사용: python3 make_helper.py <작업폴더> [--skip-fig]
작업폴더에 mk.py(본문 · TITLE) · fig.py(그림) · img/*_thumb.png · urls.json(창고 주소, 있으면) 이 있어야 한다.
하는 일: 그림 → 본문 → 금지어 · 창고 주소 확인 → 도우미 html → txt를 텍스트 폴더와 outputs에 복사. 화면 캡처 없음."""
import sys,os,subprocess,json,re,glob,shutil,urllib.request
d=os.path.abspath(sys.argv[1]); os.chdir(d)
BAN=['자리','갈라','갈렸','갈랐','어요','예요','고요','가능성','가정','까닭','견줘','나갈','놓습니다','1위','최고','헷갈','프리미엄','%p','봤습니다','셌습니다']
if '--skip-fig' not in sys.argv and os.path.exists('fig.py'): subprocess.run(['python3','fig.py'],check=True,capture_output=True)
subprocess.run(['python3','mk.py'],check=True,capture_output=True)
title=open('post.txt').read().split('\n')[1].strip()
txt=open('post.txt').read(); bad=[w for w in BAN if w in txt]
html=open('post.html').read()
ph=re.findall(r'\[그림\] (\S+)',html)
urls=re.findall(r'src="(https://blogger\.googleusercontent[^"]+)"',html)
dead=[]
for u in urls:
    try: urllib.request.urlopen(urllib.request.Request(u,method='HEAD'),timeout=15)
    except Exception: dead.append(u[-40:])
thumb=(glob.glob('img/*_thumb.png') or [''])[0]
slug=os.path.basename(thumb).replace('_thumb.png','') if thumb else os.path.basename(d)
out=f'{slug}_helper.html'
subprocess.run(['python3',os.path.join(os.path.dirname(__file__),'build.py'),'post.html',title,'예약 시각은 정해서 넣으세요','낭만 부동산 분석 플랫폼 (dong_jin_kim)','',out,title.split(',')[0]+' 발행 도우미','',thumb],check=True)
t=open(out).read()
s=t.index('<div class="step"><h2><span class="n">3</span>'); e=t.index('<div class="step"><h2><span class="n">4</span>')
msg=f'본문 그림 {len(urls)}장' if urls else '본문 그림 없음'
t=t[:s]+f'<div class="step"><h2><span class="n">3</span>{msg}</h2><div class="meta">2번 「본문 복사」에 그림이 이미 들어 있습니다(낭만 창고 주소). 붙여 넣은 뒤 그림이 다 보이는지만 확인하세요.</div></div>\n'+t[e:]
import re as _re
t=t.replace("document.getElementById('bt').onclick=","(document.getElementById('bt')||{}).onclick=")
t=_re.sub(r'<div class="step"><h2><span class="n">1</span>제목</h2>.*?</div></div>\n?','',t,count=1,flags=_re.S)
t=t.replace('<span class="n">0</span>대표 사진(썸네일) — 맨 먼저 올리고 「대표」로 지정','<span class="n">0</span>썸네일 — 따로 복사해서 맨 위에 붙이고 「대표」로 지정')
ts=t.find('<div class="step"><h2><span class="n">0</span>썸네일'); te=t.find('<div class="step"><h2><span class="n">3</span>')
if ts>0 and te>ts:
    blk=t[ts:te].replace('<span class="n">0</span>','<span class="n">1</span>'); t=t[:ts]+t[te:]
    bs=t.find('<div class="step"><h2><span class="n">2</span>본문'); t=t[:bs]+blk+t[bs:]
open(out,'w').write(t)
from datetime import date
old=glob.glob(f"/home/claude/텍스트/낭만부동산/*_낭만부동산_{title}.txt"); fn=old[0] if old else f"/home/claude/텍스트/낭만부동산/{date.today():%Y%m%d}_낭만부동산_{title}.txt"
os.makedirs(os.path.dirname(fn),exist_ok=True); shutil.copy('post.txt',fn)
od=f'/mnt/user-data/outputs/{slug}'; os.makedirs(od,exist_ok=True)
for f in glob.glob('img/*.png')+['post.html','post.txt']: shutil.copy(f,od)
print(json.dumps({'title':title,'helper':os.path.join(d,out),'금지어':bad,'남은_점선자리':ph,'창고그림':len(urls),'안열리는그림':dead,'outputs':od},ensure_ascii=False,indent=0))
