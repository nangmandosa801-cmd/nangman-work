import subprocess,re,html,os,sys,time
def get(s,j,br='00'):
    f=f'/home/claude/w/law/gb/{s}_{j}_{br}.txt'
    if os.path.exists(f) and os.path.getsize(f)>50: return open(f).read()
    for i in range(4):
        r=subprocess.run(['curl','-sS','-m','40','-A','Mozilla/5.0',f'https://www.law.go.kr/LSW/lsSideInfoP.do?lsiSeq={s}&joNo={j}&joBrNo={br}&docCls=jo&urlMode=lsScJoRltInfoR&chrClsCd=010202'],capture_output=True)
        h=r.stdout.decode('utf-8','ignore')
        t=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S))))
        m=re.search(r'(제\d+조(의\d+)?\(.*?) 위로 아래로',t)
        if m:
            open(f,'w').write(m.group(1)); return m.group(1)
        time.sleep(3)
    return ''
if __name__=='__main__':
    s=sys.argv[1]
    for a in sys.argv[2:]:
        j,_,br=a.partition('-'); t=get(s,j.zfill(4),br.zfill(2) if br else '00'); print(s,a,len(t),t[:150])
