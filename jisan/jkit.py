# -*- coding: utf-8 -*-
A_=[]; A=A_.append
DIV='<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;"><tr><td style="border-top:3px solid #1B7A9E;width:60px;font-size:1px;line-height:1px;">&nbsp;</td><td style="border-top:1px solid #D6DDE3;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>'
BR='<p><br></p>'
def P(t): return '<p style="font-size:21px;color:#333;">%s</p>'%t
def H(t): return '<p style="font-size:27px;font-weight:700;color:#0D3B5C;">%s</p>'%t
def CAP(t): return '<p style="font-size:17px;color:#8A8578;">%s</p>'%t
def B(t): return '<b style="color:#0D3B5C;">%s</b>'%t
def HL(t): return '<span style="background-color:#FFF3C4;">%s</span>'%t
def FIG(f,d): return '<table width="693" style="width:100%%;min-width:693px;border-collapse:collapse;"><tr><td style="border:1px dashed #9CBBCC;padding:14px;text-align:center;"><span style="font-size:17px;color:#0D3B5C;">%s &#8212; %s</span></td></tr></table>'%(f,d)
def TABLE(ws,hs,rows):
    o=['<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">','<tr>']
    for i,(w,h) in enumerate(zip(ws,hs)):
        bg='#0D3B5C' if i%2==0 else '#1B7A9E'
        o.append('<td width="%s" style="background-color:%s;padding:10px 6px;text-align:center;"><span style="font-size:15px;font-weight:700;color:#FFFFFF;">%s</span></td>'%(w,bg,h))
    o.append('</tr>')
    for cells in rows:
        tr=['<tr>']
        for c in cells:
            al='left'; txt=c
            if isinstance(c,tuple): txt,al=c
            tr.append('<td style="border:1px solid #D6DDE3;padding:8px 6px;text-align:%s;"><span style="font-size:16px;font-weight:700;color:#1B7A9E;">%s</span></td>'%(al,txt))
        tr.append('</tr>'); o.append(''.join(tr))
    o.append('</table>'); return '\n'.join(o)

def LK(u,t,d):
    return '<p style="font-size:19px;font-weight:700;"><a href="%s" style="color:#1B7A9E;text-decoration:none;border-bottom:1px solid #9CBBCC;">%s</a><br>\n<span style="font-size:17px;color:#7A8590;">%s</span></p>'%(u,t,d)
