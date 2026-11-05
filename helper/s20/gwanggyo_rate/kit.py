import html
D='#1F3864'; A='#2E5C8A'; BR='#B5533C'; L='#C8D2DE'
def P(t): return f'<p style="font-size:21px;color:#333;">{t}</p>\n<p><br></p>\n'
def HL(t): return f'<b style="color:{D};border-bottom:6px solid #D4E6F7;background:linear-gradient(to top,#D4E6F7 40%,transparent 40%);">{t}</b>'
def B(t): return f'<b style="color:{D};">{t}</b>'
def LK(url,t): return f'<a href="{url}" style="color:{A};text-decoration:none;border-bottom:1px solid #C7D6E6;">{t}</a>'
def H(t): return (f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:3px solid {A};width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid {L};font-size:1px;line-height:1px;">&nbsp;</td></tr></table>\n<p><br></p>\n'
                  f'<p style="font-size:27px;font-weight:700;color:{D};">{t}</p>\n<p><br></p>\n')
import json as _j
_U=_j.load(open('urls.json')) if __import__('os').path.exists('urls.json') else {}
def IMG(fn,cap):
    k=fn.replace('nangman_gwanggyo_rate_','').replace('.png','')
    if k not in _U: return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border:1px dashed #9FB3C8;padding:14px;text-align:center;"><span style="font-size:17px;color:#1F3864;">[그림] {fn} — {cap}</span></td></tr></table>\n<p><br></p>\n'
    return f'<p style="text-align:center;"><img src="{_U[k]}" alt="{cap}" width="693" style="width:100%;max-width:693px;"></p>\n<p style="font-size:17px;color:#7A8590;text-align:center;">{cap}</p>\n<p><br></p>\n'
def NOTE(t): return f'<p style="font-size:18px;color:#8A8578;">{t}</p>\n<p><br></p>\n'
def FIGS(items):
    tds=[]
    for i,(big,sub,col) in enumerate(items):
        br='' if i==len(items)-1 else 'border-right:8px solid #FFFFFF;'
        tds.append(f'<td width="33%" style="background-color:#F4F6F9;border-top:4px solid {col};{br}padding:20px 10px;text-align:center;vertical-align:top;"><span style="font-size:24px;font-weight:700;color:{col};">{big}</span><br><span style="font-size:18px;color:#555;line-height:1.6;">{sub}</span></td>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr>{"".join(tds)}</tr></table>\n<p><br></p>\n'
def TABLE(head,rows,widths,hl=None):
    h=''.join(f'<td width="{w}" style="background-color:{D};padding:13px 8px;text-align:center;"><span style="font-size:18px;font-weight:700;color:#FFFFFF;">{c}</span></td>' for i,(c,w) in enumerate(zip(head,widths)))
    out=[f'<tr>{h}</tr>']
    for r,row in enumerate(rows):
        bg=' style="background-color:#F0F4F8;"' if r%2 else ''
        if hl is not None and r in hl: bg=' style="background-color:#F1F6FB;"'
        cells=[]
        for j,c in enumerate(row):
            al='left' if j==0 else 'right'
            st=f'font-size:19px;font-weight:700;color:{D};' if j==0 else 'font-size:19px;color:#333;'
            cells.append(f'<td style="border:1px solid {L};padding:11px 8px;text-align:{al};"><span style="{st}">{c}</span></td>')
        out.append(f'<tr{bg}>{"".join(cells)}</tr>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">\n'+'\n'.join(out)+'\n</table>\n<p><br></p>\n'
def BARS(cap,items,lo,hi):
    rows=[]
    for lab,v,n,strong in items:
        w=max(4,round((v-lo)/(hi-lo)*100)); col=A if strong else '#9FB3C8'
        rows.append(f'<tr><td width="24%" style="padding:9px 6px;border-bottom:1px solid {L};"><span style="font-size:19px;color:{D};font-weight:700;">{lab}</span></td>'
                    f'<td width="56%" style="padding:9px 6px;border-bottom:1px solid {L};"><table width="100%" style="border-collapse:collapse;"><tr><td width="{w}%" style="background-color:{col};height:18px;font-size:1px;line-height:1px;">&nbsp;</td><td style="font-size:1px;">&nbsp;</td></tr></table></td>'
                    f'<td width="20%" style="padding:9px 6px;border-bottom:1px solid {L};text-align:right;"><span style="font-size:20px;font-weight:700;color:{A if strong else "#555"};">{v}</span><span style="font-size:16px;color:#7A8590;"> ({n}곳)</span></td></tr>')
    return (f'<p style="font-size:18px;color:#555;">{cap}</p>\n<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;border-top:2px solid {D};">\n'+'\n'.join(rows)+'\n</table>\n<p><br></p>\n')
def VS(a,b):
    def cell(t,sub,lines,col,br):
        return (f'<td width="50%" style="border-top:4px solid {col};{br}background-color:#F4F6F9;padding:18px 16px;vertical-align:top;"><span style="font-size:20px;font-weight:700;color:{col};">{t}</span><br><span style="font-size:17px;color:#7A8590;">{sub}</span><br><br>'
                + '<br>'.join(f'<span style="font-size:19px;color:#333;line-height:1.8;">{x}</span>' for x in lines)+'</td>')
    return f'<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;"><tr>{cell(*a,"border-right:8px solid #FFFFFF;")}{cell(*b,"")}</tr></table>\n<p><br></p>\n'
def TAIL(title,url,sub):
    t=LK(url,title) if url else f'<span style="color:{A};">{title}</span>'
    return f'<p style="font-size:19px;font-weight:700;">{t}<br>\n<span style="font-size:17px;color:#7A8590;">{sub}</span></p>\n<p><br></p>\n'

