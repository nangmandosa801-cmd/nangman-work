import json,re,html,sys
from bs4 import BeautifulSoup,NavigableString
sys.path.insert(0,'.'); import scan
OLD=json.load(open('helper_old_data.json'))
BY={x['logNo']:x for x in OLD}
TMAP={x['old_title']:x['new_title'] for x in OLD if x['new_title'] and x['new_title']!=x['old_title']}
CONTACT='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgggmSoEvzH-ndWSJIX7GiNBY90C8MVnLS8SPDI8C1oPXOwYX1KWTQuRQHmEoKUSmmAzaW9Uo7I2DlsgR0Ep4pWLeT9AexrpsR72LXNfr1WUVRLzbnroevYUeSKBDItq9-BYU1xtWnlkR8ZAPMqs9EZZkPrsYpr0XXiehmwTSBAk3ET1mrBovwxRUp-MnnD/s1600/nangman_interior_contact_966x330.png'
NOTICE={
'224426338443':'중문까지 필요한 집이라면 낭만 인테리어가 제휴 중문 시공팀을 이어 드립니다. 계약이 되면 시공팀에게서 소개 수수료를 받습니다.',
'224444765222':'필름 시공은 낭만 인테리어가 제휴 시공팀을 소개합니다. 소개한 집이 계약하면 시공팀에게서 소개 수수료가 들어옵니다.',
'224438517059':'곰팡이 원인을 보러 가는 업체는 낭만 인테리어가 이어 드립니다. 계약이 되면 그 업체에게서 수수료를 받습니다.',
'224436506476':'이천과 광명 두 집을 시공한 제휴 시공팀을 낭만 인테리어가 소개합니다. 계약이 되면 그 팀에게서 소개 수수료를 받습니다.',
'224435596372':'청라 · 김포 · 인천 세 집을 시공한 제휴팀과 계약이 되면 낭만 인테리어가 소개 수수료를 받습니다. 사진과 순서는 그 팀의 작업 기록입니다.',
'224439589802':'코킹 업체를 이어 드리는 일로 낭만 인테리어가 수수료를 받습니다. 계약이 되지 않으면 받는 돈은 없습니다.',
'224432194148':'군포 아파트를 시공한 제휴 코킹팀과 계약이 되면 낭만 인테리어가 소개 수수료를 받습니다.',
'224435830476':'컨테이너 농막은 제휴 제작 업체가 짓습니다. 낭만 인테리어는 계약이 되면 그 업체에게서 소개 수수료를 받습니다.',
}
# post-specific edits: (op, startswith, new)
OPS={
'224426338443':[('delp','정리'),('delp','현관 외풍 차단은 문풍지를 사는 것부터'),('delp','손잡이 쪽에서 새면 문 닫힘 상태')],
'224444765222':[('delp','답부터 적습니다'),('delp','[동영상')],
'224438517059':[('repp','둘은 고치는 곳이 다릅니다','원인을 모르고 곰팡이 제거제만 뿌리면 같은 일이 되풀이됩니다.')],
'224436506476':[('delp','그런데 벽 자체가 차가운 집은 덮은 것 뒤에서 다시 젖습니다')],
'224435596372':[('repp','베란다와 세탁실 곰팡이는 락스로','베란다와 세탁실 곰팡이는 락스로 닦으면 잠깐 없어집니다. 그런데 겨울이 오면 같은 곳에 다시 핍니다.')],
'224439589802':[('repp','창틀 누수가 있던 두 집을 밖에서','창틀 누수가 있던 두 집을 밖에서 찍은 사진입니다. 원인이 다르면 작업도 달라집니다.')],
'224432194148':[('repp','군포의 아파트에서 베란다 실리콘 코킹을 했습니다','걷어 내기 전과 새로 쏜 뒤를 사진으로 봅니다.')],
'224435830476':[('delp','시공은 제휴 업체가 맡습니다')],
}
INTRO_INSERT={'224435830476'}
def esc(s): return html.escape(s,quote=False)
def spanstyle(sp):
    st=[]
    m=[re.match(r'se-fs-fs(\d+)$',c) for c in sp.get('class',[])]
    m=[x for x in m if x]
    if m: st.append(f'font-size:{m[0].group(1)}px')
    s=sp.get('style','') or ''
    for k in s.split(';'):
        k=k.strip()
        if k.startswith(('color:','background-color:')): st.append(k)
    return ';'.join(st)
def inner(node):
    o=''
    for ch in node.children:
        if isinstance(ch,NavigableString): o+=esc(str(ch).replace('​',''))
        elif ch.name=='b': o+='<b>'+inner(ch)+'</b>'
        elif ch.name=='u': o+='<u>'+inner(ch)+'</u>'
        elif ch.name=='br': o+='<br>'
        elif ch.name=='a': o+=f'<a href="{html.escape(ch.get("href",""))}" style="color:inherit;text-decoration:none;border-bottom:1px solid #C7D6E6;">'+inner(ch)+'</a>'
        elif ch.name=='span': o+=inner(ch)
        else: o+=inner(ch)
    return o
def ptext(p): return p.get_text('').replace('​','').strip()
def emit_p(p):
    t=ptext(p)
    if not t and not p.find('img'): return '<p><br></p>'
    st=[]
    if 'se-text-paragraph-align-center' in p.get('class',[]): st.append('text-align:center')
    lh=re.search(r'line-height:[\d.]+',p.get('style','') or '')
    if lh: st.append(lh.group(0))
    o=''
    for sp in p.find_all('span',recursive=False):
        if '__se-hash-tag' in sp.get('class',[]): continue
        ss=spanstyle(sp); body=inner(sp)
        o+=f'<span style="{ss}">{body}</span>' if ss else f'<span>{body}</span>'
    return f'<p style="{";".join(st)};">{o}</p>' if st else f'<p>{o}</p>'
def mk(text,fs,color,bg=None,bold=False,lh=None,align=None):
    s=f'font-size:{fs}px;color:{color}'+(f';background-color:{bg}' if bg else '')
    t=f'<b>{esc(text)}</b>' if bold else esc(text)
    ps=(f'text-align:{align};' if align else '')+(f'line-height:{lh};' if lh else '')
    return f'<p style="{ps}"><span style="{s}">{t}</span></p>'
def emit_table(t):
    o='<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">'
    for tr in t.select('tr'):
        o+='<tr>'
        for td in tr.find_all('td',recursive=False):
            stl=re.sub(r'height:[^;]*;?','',td.get('style','')).strip()
            o+=f'<td colspan="{td.get("colspan","1")}" rowspan="{td.get("rowspan","1")}" style="{stl}">'
            for p in td.select('p.se-text-paragraph'): o+=emit_p(p)
            o+='</td>'
        o+='</tr>'
    return o+'</table>'
def imgsrc(x):
    im=x.select_one('img'); u=im.get('data-lazy-src') or im.get('src')
    u=re.sub(r'\?type=.*','',u)
    if 'logo_c_banner_navy_tel_1' in u: return CONTACT,'swap'
    if 'pstatic.net' in u: u+='?type=w966'
    return u,''
def build(n):
    sp=BY[n]; s=BeautifulSoup(open(f'src/{n}.html').read(),'html.parser'); c=s.select_one('.se-main-container')
    for sc in c.find_all('script'): sc.decompose()
    log=[]
    # global text edits
    for tn in list(c.find_all(string=True)):
        t=str(tn); t2=t
        for o,nw in TMAP.items():
            if o in t2: t2=t2.replace(o,nw); log.append('제목참조')
        if t2!=t: tn.replace_with(t2)
    # tag paragraphs
    for p in c.select('p.se-text-paragraph'):
        if len(p.select('.__se-hash-tag'))>=3: p.decompose(); log.append('태그줄 뺌')
    # old-helper card descriptions / bottom notice
    for b in sp['boilerplate']:
        if b['act']=='del' and b['note'].startswith('카드'):
            key=b['old'].rstrip('…')[:16]
            for p in c.select('p.se-text-paragraph'):
                if ptext(p).startswith(key): p.decompose(); log.append('카드설명 뺌')
    for op in OPS.get(n,[]):
        hit=0
        for p in c.select('p.se-text-paragraph'):
            t=ptext(p)
            if t.startswith(op[1]) and (op[0]!='delp' or True):
                if op[0]=='delp': p.decompose()
                else:
                    first=p.find('span'); 
                    for o in p.find_all('span',recursive=False)[1:]: o.decompose()
                    first.clear(); first.append(op[2])
                hit+=1; break
        log.append(f'{op[0]}:{op[1][:12]}:{hit}')
    comps=c.find_all('div',class_='se-component',recursive=False)
    # comp0 header
    c0=comps[0]; hdr=ptext(c0.select_one('p.se-text-paragraph'))
    ttl=sp['new_title']; i=ttl.index(', '); l1=ttl[:i+1]; l2=ttl[i+2:]
    out=[mk(hdr,16,'#2e5c8a'),mk(NOTICE[n],13,'#2e5c8a','#f5faff'),'<p><br></p>',
         mk(l1,34,'#1f3864',bold=True,lh='1.5'),mk(l2,34,'#1f3864',bold=True,lh='1.5'),'<p><br></p>']
    imgs=[]
    for k,x in enumerate(comps[1:],1):
        cl=x['class'][1]
        if cl=='se-text':
            blanks=0
            for p in x.select('p.se-text-paragraph'):
                h=emit_p(p)
                if h=='<p><br></p>':
                    blanks+=1
                    if blanks>2: continue
                else: blanks=0
                out.append(h)
        elif cl=='se-table': out.append(emit_table(x)); out.append('<p><br></p>')
        elif cl=='se-image':
            u,sw=imgsrc(x); imgs.append(u)
            if sw: log.append('배너를 2882 연락 그림으로 바꿈')
            out.append(f'<p style="text-align:center;"><img src="{u}" width="693" style="width:100%;max-width:693px;" alt=""></p>')
            cap=x.select_one('.se-caption')
            if cap and ptext(cap): out.append(mk(ptext(cap),13,'#8a8578',align='center'))
            if k==1 and n in INTRO_INSERT:
                out.append('<p><br></p>'); out.append(mk(sp['intro'],19,'#333333',lh='1.9')); out.append('<p><br></p>'); log.append('첫 문단 넣음')
        elif cl=='se-oglink': out.append(f'<p>{esc(x.get_text(" ",strip=True))}</p>')
    # drop trailing blanks
    while out and out[-1]=='<p><br></p>': out.pop()
    B='\n'.join(out)
    return dict(n=n,old=sp['old_title'],T=sp['new_title'],G=sp['tags'],B=B,log=sorted(set(log)),imgs=len(imgs))
if __name__=='__main__':
    ids=[x['logNo'] for x in OLD if x['day']=='1일차']
    R=[build(n) for n in ids]
    json.dump(R,open('day1_data.json','w'),ensure_ascii=False)
    for r in R:
        txt=BeautifulSoup(r['B'],'html.parser').get_text('\n')
        print(r['n'],len(r['B']),'img',r['imgs'],r['log'],scan.scan(txt+r['T']+NOTICE[r['n']]))
