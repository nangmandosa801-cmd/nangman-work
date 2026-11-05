"""post.html 안 HTML로 그린 시각화(숫자 카드 FIGS · 막대 BARS · 비교 상자 VS)를 그림으로 바꾼다.
prep(폴더) → (바뀐 html 문자열, {가짜주소: png경로}). html2aside*.py 가 부른다."""
import re, os, subprocess
from bs4 import BeautifulSoup
def kind(t):
    s = str(t)
    if t.find('table') and 'height:18px' in s: return 'bars'
    tds = t.find_all('td', recursive=False) or [td for tr in t.find_all('tr', recursive=False) for td in tr.find_all('td', recursive=False)]
    if tds and all('border-top:4px' in (td.get('style') or '') for td in tds): return 'card'
    return None
def prep(d):
    soup = BeautifulSoup(open(f'{d}/post.html', encoding='utf8').read(), 'html.parser')
    os.makedirs(f'{d}/img/vis', exist_ok=True); m = {}; n = 0
    for t in soup.find_all('table'):
        if t.find_parent('table') or not kind(t): continue
        n += 1; png = f'{d}/img/vis/vis_{n:02d}.png'
        page = f'<html><head><meta charset="utf-8"></head><body style="margin:0;padding:20px;background:#fff;font-family:\'Noto Sans CJK KR\',\'NanumGothic\',sans-serif;width:693px;">{t}</body></html>'
        open(png[:-4] + '.html', 'w', encoding='utf8').write(page)
        subprocess.run(['wkhtmltoimage', '-q', '--width', '733', '--enable-local-file-access', png[:-4] + '.html', png], check=True)
        u = f'vis://{n}'; m[u] = png
        t.replace_with(BeautifulSoup(f'<img src="{u}" alt="시각화 {n}">', 'html.parser'))
    return str(soup), m
