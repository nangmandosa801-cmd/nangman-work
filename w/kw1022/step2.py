from ac import many
import json
rows=json.load(open('step1.json'))
best=[r for r in rows if r['n']>=4 and not r['q'].startswith('아파트')]
best.sort(key=lambda r:(-r['n'],-r['com']))
print('== 아파트 밖 살아있는 조합(제안 4개 이상):',len(best))
for r in best: print(f"{r['q']} ({r['n']}/{r['com']}): "+' | '.join(r['sug'][:6]))
