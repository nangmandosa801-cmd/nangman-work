import sys,re,json
BAN=['자리','갈라','갈렸','갈랐','어요','예요','고요','가능성','가정','까닭','견줘','나갈','놓습니다','1위','최고','헷갈','프리미엄','%p','봤습니다','셌습니다','champion_chart','인테리어']
t=open(sys.argv[1]+'/post.txt').read()
body=t.split('함께 보면 좋은 글')[0]
print(json.dumps({'ban':[w for w in BAN if w in t],'chars_body':len(re.sub(r'\s','',body)),'chars_body_sp':len(body),'imgs':t.count('[그림]')},ensure_ascii=False))
