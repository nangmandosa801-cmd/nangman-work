#!/usr/bin/env python3
"""원고 md → 어사이드가 사람처럼 올릴 txt + 사진 폴더 (11/5 사용자 「도우미 없이 위치만 알려 주면 어사이드가 올림」)
사용: python3 md2txt.py <원고.md> <글이름>  → /home/claude/w/aside_out/<글이름>.txt, /home/claude/w/aside_out/<글이름>/NN.jpg
표시: [사진 NN] · [소제목] … · [표] 칸|칸 … [/표] · [문의] 문장
"""
import sys, os, re, shutil
sys.path.insert(0, '/home/claude/tools/postkit')
md, name = sys.argv[1], sys.argv[2]
O = f'/home/claude/w/aside_out/{name}'; os.makedirs(O, exist_ok=True)
raw = open(md, encoding='utf8').read()
head, body = raw.split('\n---\n', 1) if '\n---\n' in raw else ('', raw)
title = next((l[2:].strip() for l in (head or raw).splitlines() if l.startswith('# ')), name)
tags = next((l.split(':', 1)[1].strip() for l in head.splitlines() if l.startswith('tags:')), '')
out = [f'제목: {title}', '']; k = 0; intable = False
for l in body.splitlines():
    s = l.strip()
    if s.startswith('!'):
        p = s[2:].split(' ')[0] if s.startswith('!=') else s[1:].split(' ')[0]
        if os.path.exists(p):
            k += 1
            if s.startswith('!='): shutil.copy(p, f'{O}/{k:02d}.jpg')
            else:
                from vary import vary
                b, _ = vary(p, s.split(' ', 1)[1] if ' ' in s else '', name + p); open(f'{O}/{k:02d}.jpg', 'wb').write(b)
            out.append(f'[사진 {k:02d}]')
        continue
    if s.startswith('|'):
        if not intable: out.append('[표]'); intable = True
        cells = [c.strip() for c in s.strip('|').split('|')]
        if all(re.fullmatch(r':?-{2,}:?', c) for c in cells): continue
        out.append(' | '.join(cells)); continue
    if intable: out.append('[/표]'); intable = False
    if s.startswith('## '): out += ['', f'[소제목] {s[3:]}']; continue
    if s.startswith('[CALL]'): out.append(f'[문의] {s[6:].strip()} · 문자 · 전화 010-2882-8165'); continue
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s); s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1 (\2)', s)
    out.append(s)
if intable: out.append('[/표]')
if tags: out += ['', f'태그: {tags}']
open(f'/home/claude/w/aside_out/{name}.txt', 'w', encoding='utf8').write(re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip() + '\n')
print(name, k, 'photos')
