# 낭만커피 구글 블로그 (서정형) 5편
import os, json
OUT = "/home/claude/coffee/gposts"
os.makedirs(OUT, exist_ok=True)

P = 'style="font-size:17px;line-height:1.95;color:#2b2420;margin:0 0 18px;"'
LEAD = 'style="font-size:19px;line-height:1.9;color:#5a3a26;font-style:italic;border-left:3px solid #c9a27a;padding:6px 0 6px 16px;margin:6px 0 28px;"'
H2 = 'style="font-size:21px;font-weight:700;color:#4a2c1d;margin:40px 0 14px;padding-bottom:8px;border-bottom:1px solid #e3d3c1;"'
TB = 'style="width:100%;border-collapse:collapse;font-size:16px;margin:8px 0 24px;"'
TH = 'style="background:#5a3a26;color:#fff;padding:11px 8px;border:1px solid #e3d3c1;text-align:center;"'
TD = 'style="padding:11px 8px;border:1px solid #e3d3c1;text-align:center;background:#fffaf4;"'

def p(t): return f'<p {P}>{t}</p>'
def lead(t): return f'<p {LEAD}>{t}</p>'
def h2(t): return f'<h2 {H2}>{t}</h2>'
def table(head, rows):
    h = "".join(f"<th {TH}>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<table {TB}><tr>{h}</tr>{r}</table>'

