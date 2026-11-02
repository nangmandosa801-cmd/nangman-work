import json
R=json.load(open('day1_data.json'))
NOTE={'224426338443':'맨 아래 연락 그림은 새 번호 그림으로 바꿔 두었습니다.','224444765222':'맨 위에 수수료 안내가 없던 글이라 새로 넣었습니다. 본문에 있던 「동영상 넣을 곳」 안내 줄은 뺐습니다.'}
for r in R: r['note']=NOTE.get(r['n'],'')
data=json.dumps(R,ensure_ascii=False).replace('</','<\\/')
T=open('tpl.html',encoding='utf8').read().replace('__DATA__',data)
open('nangman_interior_fix_day1.html','w',encoding='utf8').write(T)
print(len(T))
