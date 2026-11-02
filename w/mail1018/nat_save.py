# usage: python3 nat_save.py <textfile>  lines: ID|qn,qn|errs|row;;row   row: id~name~tel~jibun~road~qi
import json,sys,os,datetime
B='/home/claude/w/mail1018/'
D={d['id']:d for d in json.load(open(B+'nat_danji.json'))}
Q={d['id']:d['qs'] for d in json.load(open('/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad/qs.json'))} if os.path.exists('/tmp/claude-0/-home-claude/4ad5379a-a2ca-5eaf-8c64-af30ad194588/scratchpad/qs.json') else {}
out=json.load(open(B+'brokers_010_nat.json')) if os.path.exists(B+'brokers_010_nat.json') else []
pg=json.load(open(B+'nat_progress.json')) if os.path.exists(B+'nat_progress.json') else {'done':{},'note':'nat_danji.json id별 진행. done[id]={qn:검색어별 결과수, errs, found}'}
ex={x['mobile'].replace('-','') for x in json.load(open(B+'brokers_010.json'))}
bym={x['mobile'].replace('-',''):x for x in out}
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.strip()
    if not line: continue
    i,qn,errs,rows=(line.split('|',3)+[''])[:4]
    d=D[i]; found=0
    for r in [r for r in rows.split(';;') if r]:
        kid,name,tel,jibun,road,qi=r.split('~')
        m=''.join(c for c in tel if c.isdigit())
        if m in ex: continue
        if m in bym:
            if bym[m]['danji']!=d['danji'] and d['danji'] not in bym[m]['also_danji']: bym[m]['also_danji'].append(d['danji'])
            continue
        rec=dict(danji=d['danji'],kind='입주' if d['kind']=='입주' else '2년차',office=name,mobile=tel,addr=road,
                 kakao_q=Q.get(i,['?']*9)[int(qi)],kakao_id=kid,jibun=jibun,also_danji=[],src='kakaomap 10/18',
                 sido=d['sido'],ipju_month=d['ipju_month'])
        out.append(rec); bym[m]=rec; found+=1
    pg['done'][i]={'qn':[int(x) for x in qn.split(',') if x],'errs':int(errs),'found':found}
pg['updated']=datetime.datetime.now().isoformat(timespec='minutes')
json.dump(out,open(B+'brokers_010_nat.json','w'),ensure_ascii=False,indent=1)
json.dump(pg,open(B+'nat_progress.json','w'),ensure_ascii=False,indent=1)
print(len(out),'records;',len(pg['done']),'danji done')
