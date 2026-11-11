"""mk.py 의 TABLE 호출 가운데 고른 것을 표 그림(IMG)으로 바꾼다 (11/12).
mk.py: import tabimg; TABLE=tabimg.wrap(TABLE,IMG,'<slug>')
고르기: 폴더의 tabpick.json {"호출번호": {"head": 결론 한 줄, "cap": 그림 아래 설명, "note": 그림 안 출처}}
TABDUMP=1 이면 표 자리에 @@T번호@@ 를 남겨 tabdump.json 에 머리 · 행을 적는다."""
import os, json, sys
sys.path.insert(0, '/home/claude/helper/pg')
def wrap(TABLE, IMG, slug):
    pick = json.load(open('tabpick.json', encoding='utf8')) if os.path.exists('tabpick.json') else {}
    dump = os.environ.get('TABDUMP'); log = []; n = [0]
    def T(head, rows, widths, hl=None):
        n[0] += 1; k = str(n[0])
        if dump:
            log.append({'n': n[0], 'head': head, 'rows': [list(r) for r in rows]})
            json.dump(log, open('tabdump.json', 'w', encoding='utf8'), ensure_ascii=False)
            return f'<p>@@T{k}@@</p>\n' + TABLE(head, rows, widths, hl)
        if k in pick:
            p = pick[k]; fn = f'nangman_{slug}_3_t{k}.png'
            from fig2d import table
            os.makedirs('img', exist_ok=True)
            table('img/' + fn, p['head'], head, rows, hl=p.get('hl', hl), note=p.get('note'), widths=widths)
            return IMG(fn, p['cap'])
        return TABLE(head, rows, widths, hl)
    return T


def fig(IMG, slug, key, kind, cap, *a, **kw):
    """본문 숫자로 그림 한 장(bars · cards3 · one)을 그리고 IMG 를 돌려준다. key 예: '4_one'"""
    import fig2d
    fn = f'nangman_{slug}_{key}.png'; os.makedirs('img', exist_ok=True)
    getattr(fig2d, kind)('img/' + fn, *a, **kw)
    return IMG(fn, cap)
