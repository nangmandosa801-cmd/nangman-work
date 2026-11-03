import re,glob,html
files=["산양삼재배"]
def inl(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'\((https://\S+?)\)',r'(<a href="\1">\1</a>)',s)
    return s
out=['<meta charset=utf-8><style>body{font:16px/1.8 sans-serif;max-width:720px;margin:auto;padding:16px}h1{font-size:22px}h2{font-size:18px;margin-top:28px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:4px 8px}hr{margin:48px 0}.m{color:#888;font-size:13px}</style>']
for f in files:
    L=open(f"/mnt/user-data/outputs/sigol/txt/20261101_낭만시골_{f}.txt",encoding="utf-8").read().split("\n")
    out.append(f'<h1>{html.escape(L[0][4:])}</h1><p class=m>{html.escape(L[1])} · {html.escape(L[2])}</p>')
    i=3;ul=False
    while i<len(L):
        l=L[i]
        if l.startswith("|"):
            rows=[]
            while i<len(L) and L[i].startswith("|"):
                if not re.match(r'^\|[-| ]+\|$',L[i]): rows.append([c.strip() for c in L[i].strip("|").split("|")])
                i+=1
            out.append("<table>"+"".join("<tr>"+"".join(f"<{'th' if r is rows[0] else 'td'}>{inl(c)}</{'th' if r is rows[0] else 'td'}>" for c in r)+"</tr>" for r in rows)+"</table>");continue
        if l.startswith("- "):
            if not ul: out.append("<ul>");ul=True
            out.append(f"<li>{inl(l[2:])}</li>")
        else:
            if ul: out.append("</ul>");ul=False
            if l.startswith("## "): out.append(f"<h2>{inl(l[3:])}</h2>")
            elif l.strip(): out.append(f"<p>{inl(l)}</p>")
        i+=1
    if ul: out.append("</ul>")
    out.append("<hr>")
open("/mnt/user-data/outputs/sigol/preview_sanyang.html","w",encoding="utf-8").write("\n".join(out))
