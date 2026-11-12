"""링크 정리 진행 현황(11/12 사용자 「어디까지 링크 정리하는거 끝냈는지 표시」).
실제 글을 열어 센다 → /tmp/링크정리_현황.txt · --up 이면 드라이브 5_보고에 올림.
부동산 120편: 낭만 인테리어 링크 0이면 끝. 낭만도사 194편: 다른 블로그 링크 0 + 다른 낭만도사 글 링크 3개 이하면 끝."""
import subprocess,re,json,sys,os,datetime,concurrent.futures as cf
D=os.path.dirname(os.path.abspath(__file__))
def get(b,n): return subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0',f'https://blog.naver.com/PostView.naver?blogId={b}&logNo={n}'],capture_output=True).stdout.decode('utf-8','replace')
OUT=['champion_chart','dong_jin_kim','jisandream01','hanam-curator','nangmaninterior']
def bd(n):
    s=get('dong_jin_kim',n); return n,(None if len(s)<5000 else not ('champion_chart' in s or 'nangmaninterior' in s))
def dosa(n):
    s=get('give_me_travel',n)
    if len(s)<5000: return n,None
    body=s.split('se-main-container')[-1] if 'se-main-container' in s else s
    body=body.split('class="post_footer')[0]
    ext=any(k in body for k in OUT)
    inner={m for m in re.findall(r'give_me_travel/(\d{12})',body) if m!=n}
    return n,(not ext and len(inner)<=3)
bdi=open(f'{D}/bd_ids.txt').read().split(); dfx=json.load(open(f'{D}/dosa_fix.json')); dsi=[r['logNo'] for r in dfx]
with cf.ThreadPoolExecutor(8) as ex: B=list(ex.map(bd,bdi)); S=list(ex.map(dosa,dsi))
now=datetime.datetime.utcnow()+datetime.timedelta(hours=9)
def part(name,R,url):
    done=[n for n,v in R if v]; left=[n for n,v in R if v is False]; err=[n for n,v in R if v is None]
    o=[f'■ {name}: 끝 {len(done)} / {len(R)}편 · 남음 {len(left)}편'+(f' · 확인 실패 {len(err)}' if err else ''),
       f'  다음 차례(지시 파일 순서): '+(' · '.join(left[:6]) if left else '없음')]
    return o
L=[f'링크 정리 현황 · {now:%Y-%m-%d %H:%M} 자동 확인(Claude가 실제 글을 열어 셈)','']
L+=part('낭만 부동산 · 인테리어 링크 제거 (지시_부동산_인테리어글링크_제거_발행글_1110 · 하루 6편)',B,'dong_jin_kim')+['']
L+=part('낭만도사 · 다른 블로그 링크 제거 + 같이 보면 좋은 글 3개 (지시_낭만도사_링크정리_194편_1112 · 하루 6편)',S,'give_me_travel')
open('/tmp/링크정리_현황.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
if '--up' in sys.argv: subprocess.run(['python3','/home/claude/helper/gas.py','fput','블로그/협업/5_보고','/tmp/링크정리_현황.txt'],capture_output=True)
