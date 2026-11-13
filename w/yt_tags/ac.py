import json, subprocess, sys, urllib.parse
qs = """평택 입주청소|입주청소 시기|입주청소 언제|창틀 청소
결로 공사|천장 물자국|천장 결로|탑층 결로
군포 곰팡이|곰팡이 재발|곰팡이 계속|벽지 곰팡이
도어락 교체|도어락 안열림|도어락 건전지|현관 도어락
학산 한신더휴|새집증후군 효과|붙박이장 냄새|새집 냄새
퇴실청소|퇴실청소 특약|퇴실청소비 세입자|욕실 물때
장안 디에트르|사전방문|사전점검 일정|욕실 타일
결로방지 페인트|결로 페인트|베란다 결로|결로 페인트 효과
3연동 중문|중문 단열|현관 외풍|중문 난방비
해링턴 마레|입주지정기간|입주기간|욕실 줄눈""".split('\n')
def get(url):
    try:
        r = subprocess.run(['curl','-s','--max-time','8','-A','Mozilla/5.0',url],capture_output=True,text=True)
        return r.stdout
    except Exception as e:
        return ''
out = {}
for i, line in enumerate(qs, 1):
    for q in line.split('|'):
        e = urllib.parse.quote(q)
        nv = get(f'https://ac.search.naver.com/nx/ac?q={e}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
        yt = get(f'https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=ko&q={e}')
        try: n = [x[0] for x in json.loads(nv)['items'][0]][:6]
        except Exception: n = ['ERR ' + nv[:60]]
        try: y = json.loads(yt)[1][:6]
        except Exception: y = ['ERR ' + yt[:60]]
        out[f'{i}:{q}'] = {'naver': n, 'yt': y}
json.dump(out, open('ac.json','w'), ensure_ascii=False, indent=0)
for k, v in out.items():
    print(k, '| N:', ' / '.join(v['naver']), '| Y:', ' / '.join(v['yt']))
