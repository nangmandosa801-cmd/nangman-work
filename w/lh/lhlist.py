import subprocess,re,html,json,sys
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36'
U='https://www.lh.or.kr/board.es?mid=a10601020000&bid=0060'
def curl(*a): return subprocess.run(['curl','-sS','-m','40','-A',UA,'-b','ck.txt','-c','ck.txt',*a],capture_output=True).stdout.decode('utf-8','replace')
s=curl(U); print('첫 화면',len(s))
m=re.search(r'name="_csrf"[^>]*value="([^"]+)"',s) or re.search(r'value="([^"]+)"[^>]*name="_csrf"',s)
csrf=m.group(1) if m else ''
rows=[]
for pg in range(1,5):
    t=curl('-e',U,'--data-urlencode','act=list','--data-urlencode',f'nPage={pg}','--data-urlencode','_csrf='+csrf,U) if pg>1 else s
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>',t,flags=re.S):
        a=re.search(r'list_no=(\d+)[^>]*>(.*?)</a>',tr,flags=re.S)
        if not a: 
            a=re.search(r"goView\('?(\d+)'?[^>]*>(.*?)</a>",tr,flags=re.S)
        if a:
            tds=[re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',x))).strip() for x in re.findall(r'<td[^>]*>(.*?)</td>',tr,flags=re.S)]
            rows.append((a.group(1),re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',a.group(2)))).strip(),tds[-3:] if tds else []))
json.dump(rows,open('lhrows.json','w'),ensure_ascii=False)
print(len(rows))
for r in rows[:45]: print(r[0],'|',r[1][:70],'|',r[2])
