# 지산드림 마스터 점검 — 새 원고를 내기 전에 (1) 제목 앞머리가 이미 쓰였는지 (2) 같은 매물 글과 본문 문장이 겹치는지 본다
# 사용: python3 precheck.py <원고.html> <같은매물 logNo ...>
import re,sys,html
from overlap import fetch,plain_post,sents
L=open('/home/claude/jisan_move/jisan_list.md').read()
rows=re.findall(r'^\| [^|]+ \| (\d+) \| (.+?) \|$',L,re.M)
titles={n:t for n,t in rows}
BOIL=set(titles.values())|{'구리 갈매동 공인중개사 | 지산드림 지식산업센터 전문','구리 갈매동에서 지식산업센터·창고·아파트·토지를 다룹니다','구리와 남양주, 하남에서 다루는 물건들입니다','되팔 때 걸릴 것까지 미리 말씀드립니다','현장을 직접 보고 확인한 것만 씁니다','가격은 제가 합리적인 가격으로 안내해 드립니다','지산드림이 지금 내놓은 매물 전체입니다'}
def head(t): return re.split(r'[,/|]',t)[0].strip()
src=open(sys.argv[1]).read()
T=html.unescape(re.sub('<[^>]+>','',re.search(r'font-size:34px;font-weight:700;color:#0D3B5C;">(.*?)</p>',src).group(1)))
h=head(T); bad=0
same=[(n,t) for n,t in titles.items() if head(t)==h or head(t).startswith(h+' ') and False]
print('제목 앞머리:',h)
for n,t in titles.items():
    if head(t)==h: print('  ✘ 같은 앞머리 이미 있음:',n,t); bad+=1
    elif h in head(t) or head(t) in h: print('  · 비슷한 앞머리:',n,t)
new=plain_post(sys.argv[1]); ns={s for s in sents(new) if s not in BOIL and not s.startswith('▸') and 'JA(' not in s}
ns={s for s in ns if not any(s in b or b in s for b in BOIL)}
targets=sys.argv[2:] or list(titles.keys())
for n in targets:
    sh=sorted(ns&sents(fetch(n)))
    flag='✘' if len(sh)>=5 else ('·' if sh else '✔')
    if len(sh)>=5: bad+=1
    if sh or sys.argv[2:]: print(f'  {flag} {n} 본문 같은 문장 {len(sh)}개', ('· 예: '+sh[0][:50]) if sh else '')
print('▶', '✘ %d곳 — 각도를 바꾸거나 내지 않음'%bad if bad else '✔ 겹침 없음')
