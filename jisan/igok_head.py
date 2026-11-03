# -*- coding: utf-8 -*-
exec(open('/home/claude/jisan/jkit.py').read())
def TABLE(ws,hs,rows):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">','<tr>']
    for i,(w,h) in enumerate(zip(ws,hs)):
        bg='#0D3B5C' if i%2==0 else '#1B7A9E'
        o.append('<td width="%s" style="background-color:%s;padding:13px 8px;text-align:center;"><span style="font-size:18px;font-weight:700;color:#FFFFFF;">%s</span></td>'%(w,bg,h))
    o.append('</tr>')
    for cells in rows:
        tr=['<tr>']
        for c in cells:
            al='left'; txt=c
            if isinstance(c,tuple): txt,al=c
            tr.append('<td style="border:1px solid #D6DDE3;padding:11px 8px;text-align:%s;"><span style="font-size:19px;font-weight:700;color:#1B7A9E;">%s</span></td>'%(al,txt))
        tr.append('</tr>'); o.append(''.join(tr))
    o.append('</table>'); return '\n'.join(o)
def KV(pairs):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">']
    for k,v in pairs:
        o.append('<tr><td width="28%%" style="background-color:#EEF3F6;border-bottom:1px solid #FFFFFF;padding:13px 12px;"><span style="font-size:19px;font-weight:700;color:#0D3B5C;">%s</span></td><td style="border-bottom:1px solid #D6DDE3;padding:13px 12px;"><span style="font-size:20px;color:#333;">%s</span></td></tr>'%(k,v))
    o.append('</table>'); return '\n'.join(o)

