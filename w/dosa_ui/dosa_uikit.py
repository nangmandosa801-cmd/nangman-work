# -*- coding: utf-8 -*-
# 낭만도사 글 안에 넣는 「한눈에 보이는」 부품 — 낭만 부동산 · 지산드림 · 낭만 인테리어 UI 표준(2026.10.7)을 낭만도사 규칙에 맞춘 판
#   꼴: 흰 바탕 / 맨 위 버건디 가는 줄 하나 / 칸 사이는 옅은 실선 / 큰 글자와 작은 회색 설명 / 왼쪽 맞춤
#   낭만도사 규칙: 모든 글자 19px 이상 · 빈 단락으로 틈을 만들지 않음(틈은 padding으로) · 링크 버건디 · 강조 골드
#   골드는 줄과 막대에만 쓴다. 글자 색으로 쓰면 흰 바탕에서 흐려서 안 읽힌다.
W='<table width="693" style="width:100%;min-width:693px;border-collapse:collapse;table-layout:fixed;">'
INK='#5C1B2A'    # 버건디 — 맨 위 줄 · 큰 글자 · 강조 글자 · 링크
GOLD='#C9A66B'   # 골드 — 강조 칸 위 줄 · 흐름 띠 · 막대
GRAY='#6F6A64'   # 작은 설명 글자
HAIR='#E6DED3'   # 칸 사이 옅은 실선
TINT='#FAF6EE'   # 강조 칸 옅은 바탕(한 부품에서 한 칸만)
SOFT='#E3D3B8'   # 강조하지 않는 막대
MUTE='#8A8580'   # 「아닌 것 · 안 되는 것」 머리 글자와 줄 (버건디와 붉은색은 서로 구분이 안 되어 회색을 씀)

def FIGS(items):
    """숫자 줄. items: [(작은 이름, 큰 글자, 설명)] 두세 칸"""
    n=len(items); s=W+'<tr>'
    for i,(lab,big,note) in enumerate(items):
        bl='' if i==0 else f'border-left:1px solid {HAIR};'
        s+=(f'<td width="{100//n}%" style="border-top:2px solid {INK};border-bottom:1px solid {HAIR};{bl}padding:18px 16px 16px 16px;vertical-align:top;">'
            f'<span style="font-size:19px;color:{GRAY};">{lab}</span><br>'
            f'<span style="font-size:{30 if len(big)<=8 or n<3 else 26}px;font-weight:700;color:{INK};line-height:1.6;">{big}</span><br>'
            f'<span style="font-size:19px;color:#555;line-height:1.6;">{note}</span></td>')
    return s+'</tr></table>\n'

def LIST(items):
    """번호 줄. items: [(번호, 굵은 글자, 설명)] — 실제로 순서가 있는 것만"""
    s=W
    for i,(no,t,note) in enumerate(items):
        bt=f'border-top:2px solid {INK};' if i==0 else ''
        s+=(f'<tr><td width="11%" style="{bt}border-bottom:1px solid {HAIR};padding:16px 0 16px 14px;vertical-align:top;"><span style="font-size:30px;font-weight:700;color:{GOLD};line-height:1.3;">{no}</span></td>'
            f'<td style="{bt}border-bottom:1px solid {HAIR};padding:16px 12px;vertical-align:top;"><span style="font-size:21px;font-weight:700;color:{INK};">{t}</span><br><span style="font-size:19px;color:#555;line-height:1.7;">{note}</span></td></tr>')
    return s+'</table>\n'

def FLOW(items,total=None):
    """흐름 띠. items: [(큰 글자, 설명)] — 대운 · 세운처럼 기간이 이어지는 것 · total: 맨 끝 칸 (큰 글자, 설명)"""
    n=len(items)+(1 if total else 0); s=W+'<tr>'
    for i,(big,note) in enumerate(items):
        col=INK if i==0 else GOLD
        s+=(f'<td width="{100//n}%" style="border-top:6px solid {col};border-right:6px solid #FFFFFF;padding:12px 4px 4px 2px;vertical-align:top;">'
            f'<span style="font-size:24px;font-weight:700;color:{INK};">{big}</span><br><span style="font-size:19px;color:{GRAY};line-height:1.6;">{note}</span></td>')
    if total:
        s+=(f'<td width="{100//n}%" style="border-top:6px solid {HAIR};padding:12px 4px 4px 10px;vertical-align:top;">'
            f'<span style="font-size:24px;font-weight:700;color:{INK};">{total[0]}</span><br><span style="font-size:19px;color:{GRAY};line-height:1.6;">{total[1]}</span></td>')
    return s+'</tr></table>\n'

def VS(heads,rows,hi):
    """나란히 비교. heads: [(이름, 작은 글자)] · rows: [(항목, [값…])] · hi: 강조할 칸 번호"""
    n=len(heads); lw=18; cw=(100-lw)//n
    s=W+f'<tr><td width="{lw}%" style="border-bottom:1px solid {HAIR};padding:0;"></td>'
    for i,(t,sub) in enumerate(heads):
        on=i==hi
        s+=(f'<td width="{cw}%" style="border-top:{"3px solid "+GOLD if on else "3px solid #FFFFFF"};border-bottom:1px solid {HAIR};{"background-color:"+TINT+";" if on else ""}padding:14px 12px 12px 12px;vertical-align:bottom;">'
            f'<span style="font-size:21px;font-weight:700;color:{INK if on else "#444"};">{t}</span><br><span style="font-size:19px;color:{GRAY};">{sub}</span></td>')
    s+='</tr>'
    for lab,vals in rows:
        s+=f'<tr><td style="border-bottom:1px solid {HAIR};padding:13px 4px;"><span style="font-size:19px;color:{GRAY};">{lab}</span></td>'
        for i,v in enumerate(vals):
            on=i==hi
            s+=f'<td style="border-bottom:1px solid {HAIR};{"background-color:"+TINT+";" if on else ""}padding:13px 12px;"><span style="font-size:19px;{"font-weight:700;color:"+INK if on else "color:#444"};">{v}</span></td>'
        s+='</tr>'
    return s+'</table>\n'

def OX(yes,no,ty='해당합니다',tn='해당하지 않습니다'):
    """두 갈래. 흰 바탕 두 칸 — 위 줄 색과 머리 글자 색으로만 구분. 틈은 줄 간격으로(빈 단락 없음)"""
    def col(title,items,fg,pad):
        return (f'<td width="50%" style="border-top:2px solid {fg};{pad}vertical-align:top;">'
                f'<span style="font-size:20px;font-weight:700;color:{fg};line-height:2.2;">{title}</span><br>'
                +'<br>'.join(f'<span style="font-size:19px;color:#333;line-height:2.0;">{x}</span>' for x in items)+'</td>')
    return (W+'<tr>'+col(ty,yes,INK,'padding:12px 20px 12px 2px;border-right:14px solid #FFFFFF;')+col(tn,no,MUTE,'padding:12px 2px 12px 2px;')+'</tr></table>\n')

def BARS(rows,mx,unit='',lw=20,span=44):
    """가는 가로 막대. rows: [(이름, 숫자, 옆 글자, 강조?[, 보여 줄 글자])] — 줄마다 표 하나 · 막대는 칸 배경색"""
    s=''
    for r in rows:
        lab,n,note,hi=r[:4]; txt=r[4] if len(r)>4 else f'{n}{unit}'
        pct=max(4,round(span*n/mx)); col=INK if hi else SOFT
        s+=(W+f'<tr><td width="{lw}%" style="border-top:5px solid #FFFFFF;border-bottom:5px solid #FFFFFF;padding:2px 4px;"><span style="font-size:19px;{"font-weight:700;color:"+INK if hi else "color:#333"};">{lab}</span></td>'
            f'<td width="{pct}%" style="background-color:{col};border-top:12px solid #FFFFFF;border-bottom:12px solid #FFFFFF;font-size:1px;">&nbsp;</td>'
            f'<td width="{100-lw-pct}%" style="border-top:5px solid #FFFFFF;border-bottom:5px solid #FFFFFF;padding:2px 10px;"><span style="font-size:19px;font-weight:700;color:{INK if hi else "#444"};">{txt}</span> <span style="font-size:19px;color:{GRAY};">&nbsp;{note}</span></td></tr></table>\n')
    return s

def CAPTION(t):
    """부품 위나 아래 회색 설명 한 줄"""
    return f'<p style="font-size:19px;color:{GRAY};">{t}</p>\n'

def PAIRS(items,lw=24):
    """이름 · 내용 줄. items: [(이름, 내용)] — 용어와 뜻, 기본 정보"""
    s=W
    for i,(k,v) in enumerate(items):
        bt=f'border-top:2px solid {INK};' if i==0 else ''
        s+=(f'<tr><td width="{lw}%" style="{bt}border-bottom:1px solid {HAIR};padding:13px 4px;vertical-align:top;"><span style="font-size:19px;font-weight:700;color:{INK};">{k}</span></td>'
            f'<td style="{bt}border-bottom:1px solid {HAIR};padding:13px 8px;vertical-align:top;"><span style="font-size:19px;color:#222;line-height:1.7;">{v}</span></td></tr>')
    return s+'</table>\n'

def VERDICT(items):
    """판정 줄. items: [(판정 글자, 'ok'|'cond'|'no', 굵은 글자, 설명)] — 기호 대신 글자로"""
    col={'ok':INK,'cond':'#8A6A2F','no':MUTE}; s=W
    for i,(word,k,t,note) in enumerate(items):
        bt=f'border-top:2px solid {INK};' if i==0 else ''
        s+=(f'<tr><td width="20%" style="{bt}border-bottom:1px solid {HAIR};padding:16px 4px;vertical-align:top;"><span style="font-size:19px;font-weight:700;color:{col[k]};">{word}</span></td>'
            f'<td style="{bt}border-bottom:1px solid {HAIR};padding:16px 8px;vertical-align:top;"><span style="font-size:20px;font-weight:700;color:#222;">{t}</span><br><span style="font-size:19px;color:#555;line-height:1.7;">{note}</span></td></tr>')
    return s+'</table>\n'

def MYEONGSIK(cols,hi=1):
    """명식 판. cols: [(기둥 이름, 천간 글자, 천간 설명, 지지 글자, 지지 설명)] 시주 · 일주 · 월주 · 연주 순서 · hi: 강조할 기둥 번호(일주=1)"""
    n=len(cols); lw=14; cw=(100-lw)//n
    def row(label,idx_big,idx_note,first=False):
        s=f'<tr><td width="{lw}%" style="border-bottom:1px solid {HAIR};padding:12px 4px;"><span style="font-size:19px;color:{GRAY};">{label}</span></td>'
        for i,c in enumerate(cols):
            on=i==hi; bl=f'border-left:1px solid {HAIR};'
            s+=(f'<td width="{cw}%" style="border-bottom:1px solid {HAIR};{bl}{"background-color:"+TINT+";" if on else ""}padding:12px 12px;vertical-align:top;">'
                f'<span style="font-size:32px;font-weight:700;color:{INK if on else "#333"};line-height:1.4;">{c[idx_big]}</span><br><span style="font-size:19px;color:{GRAY};">{c[idx_note]}</span></td>')
        return s+'</tr>'
    s=W+f'<tr><td width="{lw}%" style="border-top:2px solid {INK};border-bottom:1px solid {HAIR};padding:0;"></td>'
    for i,c in enumerate(cols):
        on=i==hi
        s+=(f'<td width="{cw}%" style="border-top:{"3px solid "+GOLD if on else "2px solid "+INK};border-bottom:1px solid {HAIR};border-left:1px solid {HAIR};{"background-color:"+TINT+";" if on else ""}padding:10px 12px;">'
            f'<span style="font-size:19px;font-weight:700;color:{INK if on else "#444"};">{c[0]}</span></td>')
    s+='</tr>'+row('천간',1,2)+row('지지',3,4)
    return s+'</table>\n'
