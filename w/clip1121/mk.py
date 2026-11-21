# 11/21 클립재료 묶음: 발행된 dong_jin_kim 글(로컬 post.html)에서 제목 · 질문 소제목 · 숫자 문장을 뽑는다. 네이버는 읽지 않는다.
import re,html,json,sys
L=[('NR049','224466613370','helper/s20/songdo_jeonse'),('NR050','224466610775','helper/s20/yeongtong_remodel'),
('NR051','224466608246','helper/s20/gyosan_minbun'),('NR052','224466529359','helper/s20/mokdong_jeonse'),
('NR053','224466588027','helper/s20/sanbon_seondo'),('NR054','224465636084','helper/tj'),
('NR055','224466618342','helper/s20/cheolsan13'),('NR056','224465634845','helper/os'),
('NR057','224465626078','helper/hr'),('NR058','224466476718','helper/bun12'),
('NR059','224465624999','helper/bc'),('NR060','224465623899','helper/gd4')]
BAD=re.compile(r'010-|champion|인테리어|http|blog\.|같이 보면|함께 보면|안녕하세요|낭만 부동산 분석 플랫폼')
out=[]
for nr,no,d in L:
    s=open(f'/home/claude/{d}/post.html').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>|<table.*?</table>','',s,flags=re.S)
    ps=[html.unescape(re.sub('<[^>]+>','',x)).strip() for x in re.findall(r'<p[^>]*>(.*?)</p>',t,re.S)]
    ps=[re.sub(r'\s+',' ',p) for p in ps if p and not BAD.search(p)]
    title=next(p for p in ps if ',' in p and len(p)<60)
    qs=[p for p in ps if p.endswith('?') and len(p)<60][:6]
    sent=[]
    for p in ps:
        for x in re.split(r'(?<=다\.)\s',p):
            if re.search(r'\d',x) and 12<len(x)<120 and x not in sent and not x.endswith('?'): sent.append(x)
    out.append(f'''==================== {nr} ====================
제목: {title}
연결할 글(네이버 클립 「블로그 글 연결」로만, 설명란에 주소 글자 금지): dong_jin_kim 글 번호 {no}
글이 답하는 질문(장면 순서로 써도 됨):
''' + '\n'.join('- '+q for q in qs) + '''
확인된 숫자 문장(이 숫자만 쓴다):
''' + '\n'.join('- '+x for x in sent[:10]) + '\n')
    print(nr,no,len(qs),len(sent[:10]),title[:30])
head='''[클립 재료 묶음 · 낭만 부동산 분석 플랫폼 · 2026-11-21 Claude]
발행이 끝났는데 클립이 없는 글 12편. 숫자는 아래 문장에 있는 것만 쓴다.
공통 금지: 전화번호 글자 · 인테리어 언급 · 설명란 링크 글자 · 위에 없는 숫자 · 「오른다 · 내린다」 단정 · 매수 · 매도 권유 · 「갈-」 표현.
캡션: 해시태그 포함 100자 안 · 해시태그 5개(#낭만부동산 포함). 글자는 크게(작은 글씨 금지).
'''
open('/home/claude/w/clip1121/클립재료_묶음_NR049-060_1121.txt','w').write(head+'\n'+'\n'.join(out))
