import subprocess,re,html,json,sys,os
O='/home/claude/watch/fanout_run/doorlock2/src/'
L=[('safety-key','224439844001'),('safety-key','224423609456'),('safety-key','224414511187'),('safety-key','224352810735'),('safety-key','224441056489'),
('wnsdn15tp','224452128599'),('wnsdn15tp','224446323300'),('wnsdn15tp','224433860964'),('wnsdn15tp','224438761044'),('wnsdn15tp','224432709290'),
('youilgate','224405408616'),('youilgate','224415498584'),('youilgate','224436005396')]
res={}
for b,n in L:
    f=O+f'{b}_{n}.html'
    subprocess.run(['curl','-sS','-A','Mozilla/5.0','-o',f,f'https://blog.naver.com/PostView.naver?blogId={b}&logNo={n}'])
    h=open(f,errors='ignore').read(); i=h.find('se-main-container'); j=h.find('post_footer_contents') ; body=h[i:j if j>i else None]
    imgs=re.findall(r'data-lazy-src="([^"]+)"',body)
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',body,flags=re.S); t=re.sub(r'</p>|<br>','\n',t); t=html.unescape(re.sub('<[^>]+>','',t)); t=re.sub(r'[ \t​]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    t=t.split('태그')[0]
    res[f'{b}_{n}']={'imgs':imgs,'text':t[:3000]}
json.dump(res,open(O+'src.json','w'),ensure_ascii=False,indent=1)
for k,v in res.items(): print('=====',k,len(v['imgs'])); print(v['text'][:1400])
