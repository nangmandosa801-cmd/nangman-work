import json
p='/mnt/user-data/outputs/sigol/txt/20261031_낭만시골_산주학교1일차.txt'
s=open(p,encoding='utf-8').read()
R2=[("1차 첫 시간은 임찬성 센터장님이 맡았습니다. 이 글은 그 첫 시간에 들은 이야기입니다. 이어서 이기원 산채마을 대표님이 산채 재배 수업을 했습니다.","이 글은 1차 첫 시간에 들은 이야기입니다. 이어서 산채 재배 수업이 있었습니다."),
("센터장님이 산림청에 낸 제안은 세 가지입니다.","산림청에 이미 들어간 제안은 세 가지입니다."),
(" 센터장님이 3년째 요구하고 있는 일입니다.",""),
("그런데 두 번째 시간, 이기원 산채마을 대표님 수업에서는","그런데 두 번째 시간 산채 수업에서는")]
for a,b in R2:
    assert a in s,a[:20]; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
R=json.load(open('/mnt/user-data/outputs/sigol/upload/hugi_fix.json'))
# chain: apply R2 on the "new" sides so the editor (already has R applied) gets R2
json.dump(R2,open('/mnt/user-data/outputs/sigol/upload/hugi_fix2.json','w'),ensure_ascii=False)
import re
print(re.findall(r'.{0,20}(?:대표님|센터장님).{0,20}',s))
