# 꼬리 링크 일부를 「첫 화면 밖」 발행 글로 보내기 — 사용자 10/17 17:52 「이것도 하고」
import re,json,datetime
pub=[]
sec=open('/home/claude/proj/발행글_목록_부동산_인테리어.md').read().split('## 낭만 인테리어')[1]
for m in re.finditer(r'\| (\d{4}\.\d\d\.\d\d) \| (\d{12}) \| (.+?) \|',sec): pub.append({'date':m[1],'log':m[2],'title':m[3].strip()})
rank=open('/home/claude/proj/낭만인테리어_검색순위_1016.md').read()
out=[]
for m in re.finditer(r'\| 첫 화면 밖 \| [^|]+\| (.+?) \|',rank):
    kw=m[1].strip(); n=lambda s:re.sub(r'\s','',s)
    hit=[p for p in pub if n(p['title']).startswith(n(kw)+',') or n(p['title']).split(',')[0]==n(kw)]
    if hit: out.append({'kw':kw,'log':hit[0]['log'],'url':'https://blog.naver.com/champion_chart/'+hit[0]['log'],'title':hit[0]['title']})
G={'입주':['입주','사전점검'],'청소':['청소'],'매트':['매트'],'방묘':['방묘','고양이','캣'],'누수·코킹':['누수','코킹','실리콘'],'결로·곰팡이':['결로','곰팡이'],'필름':['필름'],'샷시·창':['샷시','방충망','뽁뽁','외풍','단열','창'],'중문':['중문','도어','현관','가벽','파티션'],'기타':['']}
for o in out: o['품목']=next(k for k,v in G.items() if any(w in o['kw'] for w in v)) if any(w in o['kw'] for v in G.values() for w in v if w) else next(k for k,v in G.items() if any(w in o['title'] for w in v))
json.dump({'made':str(datetime.date.today()),'src':'검색순위_1016 「첫 화면 밖」 × 발행 목록','rule':'새 인테리어 글 꼬리 링크 5개 이상 중 2개는 여기서 같은 품목(없으면 이웃 품목) 글 · 같은 글을 한 주에 세 번 넘게 쓰지 않음 · 쓴 날을 used에 적음','items':out,'used':{}},open('tail_boost.json','w'),ensure_ascii=False,indent=1)
import collections;print(len(out),collections.Counter(o['품목'] for o in out))
