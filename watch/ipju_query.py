#!/usr/bin/env python3
"""입주 단지 통합 장부 조회 · 갱신 (낭만 인테리어)

  python3 ipju_query.py 다음 [N일] [최소세대] [전부]
                                     앞으로 N일(기본 21) 안에 오는 시점의 써야 할 글 · 추천 상품
                                     (전부 = 글이 있는 칸도 보임 · 최소세대 예: 다음 21 300)
  python3 ipju_query.py 단지 <이름>    한 단지 전부 (이름 일부 · 옛 이름도 됨)
  python3 ipju_query.py 상태           글 상태 집계(미작성 · 미발행 · 예약 · 발행)
  python3 ipju_query.py 갱신           mix_schedule에서 글 상태를 다시 읽어 장부 갱신(백업 먼저)
  python3 ipju_query.py 문서           프로젝트 문서(md)를 장부에서 다시 만듦

장부  : /home/claude/watch/ipju_master.json
상품표: /home/claude/watch/ipju_stage_products.json
mix_schedule_1017c.json 은 읽기만 한다(「예약 …」 줄은 절대 고치지 않음).
"""
import json, os, re, sys, shutil, signal, datetime as dt

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

W = "/home/claude/watch"
MASTER = f"{W}/ipju_master.json"
PRODUCTS = f"{W}/ipju_stage_products.json"
MIX = f"{W}/mix_schedule_1017c.json"
PUB = f"{W}/ipju_pub_plan.json"
PUBLIST = "/home/claude/proj/발행글_목록_부동산_인테리어.md"
DOC = "/home/claude/proj/낭만_입주단지_통합장부.md"
STAGES = ["D60", "D30", "직전", "직후", "2년차"]
RANK = {"직전": 0, "D30": 1, "직후": 2, "D60": 3, "2년차": 4}


# ---------------------------------------------------------------- 공통
def today():
    return dt.date.today()


def norm(s):
    s = (s or "").lower()
    for a, b in (("Ⅰ", "1"), ("Ⅱ", "2"), ("Ⅲ", "3"), ("Ⅳ", "4"), ("ⅲ", "3"), ("ⅳ", "4"),
                 ("이편한세상", "e편한세상"), ("s-class", "s클래스"), ("에스클래스", "s클래스")):
        s = s.replace(a, b)
    s = s.replace("아파트", "")
    return re.sub(r"[\s\-·・,.'\"「」『』()\[\]&/~～]", "", s)


def D(s):
    if not s:
        return None
    if isinstance(s, dt.date):
        return s
    try:
        return dt.date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def post_date(md):
    """'10/24' → 2026-10-24 · '1/2' → 2027-01-02"""
    m = re.match(r"(\d{1,2})/(\d{1,2})", md or "")
    if not m:
        return None
    mo, dd = int(m.group(1)), int(m.group(2))
    return dt.date(2026 if mo >= 7 else 2027, mo, dd)


def load(p, default=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save(p, obj):
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)


def month_end(d):
    nxt = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    return nxt - dt.timedelta(days=1)


def add_months(d, n):
    y, m = divmod(d.month - 1 + n, 12)
    return dt.date(d.year + y, m + 1, 1)


# ---------------------------------------------------------------- 시점
def calc_stages(r):
    """r: 단지 줄 → 시점 dict (문자열 날짜)"""
    st = {k: None for k in STAGES}
    S = D(r.get("입주시작"))
    if r.get("구분") == "입주예정" and S:
        st["D60"] = (S - dt.timedelta(days=60)).isoformat()
        st["D30"] = (S - dt.timedelta(days=30)).isoformat()
        st["직전"] = {"시작": (S - dt.timedelta(days=7)).isoformat(), "끝": S.isoformat()}
        st["직후"] = {"시작": S.isoformat(), "끝": (S + dt.timedelta(days=30)).isoformat()}
    two = r.get("2년되는달")
    if two and re.match(r"\d{4}-\d{2}$", two):
        m0 = dt.date(int(two[:4]), int(two[5:7]), 1)
        st["2년차"] = {"시작": (m0 - dt.timedelta(days=60)).isoformat(),
                      "끝": month_end(m0).isoformat(), "달": two}
    elif two and "~" in two:  # '2026-11~2027-01'
        a, b = [x.strip()[:7] for x in two.split("~")[:2]]
        m0 = dt.date(int(a[:4]), int(a[5:7]), 1)
        m1 = dt.date(int(b[:4]), int(b[5:7]), 1)
        st["2년차"] = {"시작": (m0 - dt.timedelta(days=30)).isoformat(),
                      "끝": month_end(m1).isoformat(), "달": two}
    return st


def stage_of_post(r, d, title=""):
    """글이 나가는 날(d)이 그 단지의 어느 시점인지"""
    if r.get("구분") == "2년차":
        return "2년차"
    S = D(r.get("입주시작"))
    if S and d:
        # 칸을 쓸 수 있는 기간과 같은 경계(D30 칸은 D30 7일 전부터)
        if d < S - dt.timedelta(days=37):
            base = "D60"
        elif d < S - dt.timedelta(days=7):
            base = "D30"
        elif d < S:
            base = "직전"
        elif S + dt.timedelta(days=700) <= d:
            base = "2년차"
        else:
            base = "직후"
        # 2편 · 입주청소 글은 D30 몫(입주 한 달 전 예약하는 때) — 일찍 나가도 D30 칸을 채움
        if base == "D60" and ("2편" in title or "입주청소" in title):
            base = "D30"
        # 중문 1편(옵션 · 고르기)은 D60 몫 — 입주 달만 아는 단지에서 D30 칸 첫 주에 걸려도 D60으로 셈
        elif base == "D30" and ("1편" in title or ("중문" in title and "입주청소" not in title and "2편" not in title)) \
                and d < S - dt.timedelta(days=30):
            base = "D60"
        return base
    if "1편" in title:
        return "D60"
    if "2편" in title:
        return "D30"
    return None


def stage_window(r, stg):
    """그 시점 칸을 쓸 수 있는 기간(시작, 끝)"""
    st = r.get("시점") or {}
    v = st.get(stg)
    if not v:
        return None
    if stg == "D60":
        a = D(v) - dt.timedelta(days=7)
        b = D(st.get("D30")) - dt.timedelta(days=1)
        return a, b
    if stg == "D30":
        a = D(v) - dt.timedelta(days=7)
        b = D(st["직전"]["시작"]) - dt.timedelta(days=1)
        return a, b
    return D(v["시작"]), D(v["끝"])


# ---------------------------------------------------------------- 글
ITEM_KW = [("입주청소", ["입주청소", "퇴실 청소", "퇴실청소"]), ("중문", ["중문"]),
           ("줄눈", ["줄눈"]), ("탄성코트", ["탄성코트"]), ("매트", ["매트"]),
           ("인테리어 필름", ["필름"]), ("단열", ["단열"]), ("창호", ["샷시", "창호"]),
           ("코킹/실리콘", ["코킹", "실리콘"]), ("결로·곰팡이", ["결로", "곰팡이"]),
           ("누수", ["누수"]), ("하자보수", ["하자"]), ("사전점검", ["사전점검"]),
           ("이사", ["이사 "]), ("입주 준비", ["입주"])]


def items_of(title):
    out = []
    for name, kws in ITEM_KW:
        if any(k in title for k in kws):
            out.append(name)
    if "입주 준비" in out and len(out) > 1:
        out.remove("입주 준비")
    return " · ".join(out[:3]) or "기타"


def status_of(raw, title):
    s = (raw or "").strip()
    if s.startswith("예약") or s.startswith("발행") or s.startswith("미발행") or s.startswith("삭제"):
        return s
    if title.startswith("[쓸 글]") or title.startswith("(아직 안 씀") or s == "안 씀":
        return "미작성"
    return "미작성" if not s else s


def kind_of(status):
    for k in ("미작성", "미발행", "예약", "발행", "삭제"):
        if status.startswith(k):
            return k
    return "미작성"


def alias_keys(r):
    keys = set()
    for a in [r["단지"]] + r.get("별칭", []):
        n = norm(a)
        n2 = norm(re.sub(r"\([^)]*\)", "", a))
        for x in (n, n2):
            if len(x) >= 5:
                keys.add(x)
    return keys


def build_matcher(master):
    pairs = []
    for i, r in enumerate(master["단지목록"]):
        for k in alias_keys(r):
            pairs.append((k, i))
    pairs.sort(key=lambda x: -len(x[0]))

    def match(title):
        """제목 앞쪽에 나오는 단지가 이김 · 같은 자리면 긴 별칭"""
        nt = norm(title)
        best = None
        for k, i in pairs:
            p = nt.find(k)
            if p >= 0 and (best is None or (p, -len(k)) < best[0]):
                best = ((p, -len(k)), i)
        return best[1] if best else None
    return match


def read_publist():
    out = []
    try:
        lines = open(PUBLIST, encoding="utf-8").read().splitlines()
    except OSError:
        return out
    on = False
    for ln in lines:
        if ln.startswith("## "):
            on = "인테리어" in ln
            continue
        if on and ln.startswith("| 20"):
            c = [x.strip() for x in ln.strip("|").split("|")]
            if len(c) >= 3 and c[1].isdigit():
                out.append({"날": c[0], "logNo": c[1], "제목": c[2]})
    return out


def collect_posts(master):
    """mix_schedule(우선) · 입주 글 계획표 · 발행 목록에서 단지 이름이 든 글을 모은다."""
    match = build_matcher(master)
    rows = master["단지목록"]
    got = {i: [] for i in range(len(rows))}
    seen_log, seen_title, seen_head = set(), set(), set()

    def head(i, t):
        return (i, norm(t.split(",")[0]))

    def put(i, post):
        got[i].append(post)

    mix = load(MIX, [])
    for p in mix:
        t = p.get("제목", "")
        i = match(t)
        if i is None:
            continue
        st = status_of(p.get("상태"), t)
        m = re.search(r"발행 (\d{12})", st)
        if m:
            seen_log.add(m.group(1))
        seen_title.add(norm(t))
        seen_head.add(head(i, t))
        d = D(p.get("_d")) or post_date(p.get("날"))
        put(i, {"제목": t, "품목": items_of(t), "날": d.isoformat() if d else None,
                "시각": p.get("시각"), "시점": stage_of_post(rows[i], d, t), "상태": st,
                "PC폴더": p.get("PC폴더") or "", "출처": "mix_schedule"})

    pub = load(PUB, {}).get("plan", [])
    for p in pub:
        t = p.get("제목", "")
        st = status_of(p.get("상태"), t)
        if kind_of(st) in ("미작성", "삭제"):
            continue  # 안 쓴 칸은 mix_schedule의 [쓸 글]이 맡음
        log = str(p.get("logNo") or "")
        if log.isdigit() and log in seen_log or norm(t) in seen_title:
            continue
        i = match(t)
        if i is None:
            continue
        if not log.isdigit() and head(i, t) in seen_head:
            continue  # 같은 앞머리 글이 mix_schedule에 있음(제목만 바뀐 것)
        if log.isdigit():
            st = f"발행 {log}"
            seen_log.add(log)
        seen_title.add(norm(t))
        d = post_date(p.get("날"))
        put(i, {"제목": t, "품목": items_of(t), "날": d.isoformat() if d else None, "시각": None,
                "시점": stage_of_post(rows[i], d, t + (p.get("편") or "")), "상태": st,
                "PC폴더": p.get("PC") or "", "출처": "ipju_pub_plan"})

    for p in read_publist():
        if p["logNo"] in seen_log:
            continue
        i = match(p["제목"])
        if i is None:
            continue
        seen_log.add(p["logNo"])
        d = D(p["날"].replace(".", "-"))
        put(i, {"제목": p["제목"], "품목": items_of(p["제목"]), "날": d.isoformat() if d else None,
                "시각": None, "시점": stage_of_post(rows[i], d, p["제목"]),
                "상태": f"발행 {p['logNo']}", "PC폴더": "", "출처": "발행글_목록"})
    return got


def refresh_posts(master):
    got = collect_posts(master)
    auto = {"mix_schedule", "ipju_pub_plan", "발행글_목록"}
    for i, r in enumerate(master["단지목록"]):
        new = got[i]
        titles = {norm(p["제목"]) for p in new}
        keep = [p for p in r.get("글", []) if p.get("출처") not in auto and norm(p["제목"]) not in titles]
        r["글"] = sorted(new + keep, key=lambda p: (p.get("날") or "9999", p.get("시각") or ""))
    return master


# ---------------------------------------------------------------- 상품
def winter(d):
    return d and d.month in (11, 12, 1, 2)


def products_for(r, stg, d, prod):
    sp = prod["시점"][stg]
    main, side = list(sp["주력"]), list(sp["곁들임"])
    if winter(d) and sp.get("겨울"):
        main, side = list(sp["겨울"]["주력"]), list(sp["겨울"]["곁들임"])
    feats = set(r.get("특성", []))
    typ = r.get("유형")
    notes = []
    for rule in prod.get("단지_특성_조정", []):
        hit = (rule.get("유형") and rule["유형"] == typ) or (rule.get("특성") and rule["특성"] in feats)
        if not hit or (rule.get("시점") and stg not in rule["시점"]):
            continue
        for a, b in rule.get("바꿈", {}).items():
            main = [b if x == a else x for x in main]
            side = [b if x == a else x for x in side]
        notes.append(rule["메모"])
    return main[:2], side[:3], notes


# ---------------------------------------------------------------- 명령
def upcoming(master, days=21):
    prod = load(PRODUCTS)
    t0 = today()
    t1 = t0 + dt.timedelta(days=days)
    out = []
    for r in master["단지목록"]:
        for stg in STAGES:
            w = stage_window(r, stg)
            if not w:
                continue
            a, b = w
            if b < t0 or a > t1:
                continue
            posts = [p for p in r.get("글", []) if p.get("시점") == stg]
            written = [p for p in posts if kind_of(p["상태"]) in ("미발행", "예약", "발행")]
            planned = [p for p in posts if kind_of(p["상태"]) == "미작성"]
            eff = max(a, t0)
            main, side, notes = products_for(r, stg, eff, prod)
            out.append({"단지": r["단지"], "지역": r.get("지역"), "세대": r.get("세대"), "구분": r["구분"],
                        "시점": stg, "기간": f"{a.isoformat()}~{b.isoformat()}", "날": eff.isoformat(),
                        "써야함": not written, "잡힌칸": [f"{p['날']} {p['제목']}" for p in planned],
                        "있는글": [f"{p['상태']} · {p['제목']}" for p in written],
                        "주력": main, "곁들임": side, "메모": notes,
                        "확인정도": r.get("확인정도")})
    out.sort(key=lambda x: (x["날"], RANK[x["시점"]], -(x["세대"] or 0)))
    return out


CAP = ["서울", "경기", "인천", "수원", "성남", "용인", "고양", "화성", "부천", "남양주", "안산", "평택", "안양", "시흥",
       "파주", "김포", "의정부", "광주시", "하남", "광명", "군포", "양주", "오산", "이천", "구리", "안성", "포천", "의왕",
       "양평", "여주", "동두천", "과천", "연천", "검단", "송도", "동탄", "위례", "운정", "영종", "청라"]
MID = ["대전", "충남", "충북", "청주", "천안", "아산", "세종", "공주", "서산", "보령", "당진", "청양", "계룡", "부여",
       "예산", "진천", "음성", "충주", "부산", "경남", "창원", "김해", "양산", "거제", "진주", "밀양", "기장"]


def region_tier(r):
    """1 = 수도권(중문 · 청소 · 줄눈 · 매트 다 됨) · 2 = 충청 · 부산경남(중문 업체만) · 3 = 그 밖"""
    reg = (r.get("지역") or "").strip()
    t = reg + " " + r["단지"]
    far = ("대구", "부산", "울산", "광주 ", "광주광역", "대전", "전남", "전북", "경북", "경남", "강원", "충남", "충북", "제주", "세종")
    if reg.startswith(far):
        return 2 if any(k in reg for k in MID) else 3
    if any(k in t for k in CAP):
        return 1
    if any(k in t for k in MID):
        return 2
    return 3


def todo_list(master, days=21, min_units=0):
    """써야 할 글만 · 순서: 제휴 권역(수도권 먼저) → 날짜가 확인된 단지 → 칸이 닫히는 날 → 세대 큰 순"""
    idx = {r["단지"]: r for r in master["단지목록"]}
    out = []
    for x in upcoming(master, days):
        if not x["써야함"] or (x["세대"] or 0) < min_units:
            continue
        r = idx[x["단지"]]
        x["권역"] = region_tier(r)
        x["정확"] = 0 if "월만" not in (x.get("확인정도") or "월만") else 1
        out.append(x)
    out.sort(key=lambda x: (x["권역"], x["정확"], x["기간"][11:], RANK[x["시점"]], -(x["세대"] or 0)))
    return out


def cmd_next(days, show_all=False, min_units=0):
    m = load(MASTER)
    rows = upcoming(m, days)
    need = todo_list(m, days, min_units)
    print(f"# 앞으로 {days}일({today()} ~ {today() + dt.timedelta(days=days)}) · 시점 {len(rows)}칸 · 써야 할 글 {len([x for x in rows if x['써야함']])}칸"
          + (f" · {min_units}세대 이상 {len(need)}칸" if min_units else ""))
    print("# 순서: 수도권 → 충청 · 부산경남 → 그 밖, 날짜 확인된 단지 먼저, 칸이 닫히는 날 가까운 순 (전부 보기: 다음 21 전부)\n")
    for x in (rows if show_all else need):
        mark = "■ 써야 함" if x["써야함"] else "□ 글 있음"
        print(f"{mark} | {x['날']} | {x['단지']} ({x['지역'] or '-'} · {x['세대'] or '?'}세대 · {x['구분']}) | {x['시점']} {x['기간']}")
        print(f"    주력: {' · '.join(x['주력'])} / 곁들임: {' · '.join(x['곁들임'])}")
        for n in x["메모"]:
            print(f"    조정: {n}")
        for p in x["있는글"]:
            print(f"    글: {p}")
        for p in x["잡힌칸"]:
            print(f"    잡힌 칸(미작성): {p}")
        if x["확인정도"]:
            print(f"    날짜 확인: {x['확인정도']}")


def find(m, name):
    q = norm(name)
    hits = [r for r in m["단지목록"] if any(q in norm(a) for a in [r["단지"]] + r.get("별칭", []))]
    return hits


def cmd_danji(name):
    m = load(MASTER)
    hits = find(m, name)
    if not hits:
        print("없음:", name)
        return
    for r in hits:
        print(json.dumps(r, ensure_ascii=False, indent=1))


def counts(m):
    c = {"미작성": 0, "미발행": 0, "예약": 0, "발행": 0, "삭제": 0}
    by = {"입주예정": dict(c), "2년차": dict(c)}
    for r in m["단지목록"]:
        for p in r.get("글", []):
            k = kind_of(p["상태"])
            c[k] += 1
            by[r["구분"]][k] += 1
    return c, by


def cmd_status():
    m = load(MASTER)
    c, by = counts(m)
    n_in = sum(1 for r in m["단지목록"] if r["구분"] == "입주예정")
    n_two = sum(1 for r in m["단지목록"] if r["구분"] == "2년차")
    has = sum(1 for r in m["단지목록"] if r.get("글"))
    print(f"단지 {len(m['단지목록'])} (입주예정 {n_in} · 2년차 {n_two}) · 글이 있는 단지 {has}")
    print("글 상태:", " · ".join(f"{k} {v}" for k, v in c.items() if k != "삭제" or v))
    for g, cc in by.items():
        print(f"  {g}:", " · ".join(f"{k} {v}" for k, v in cc.items() if k != "삭제" or v))


def cmd_refresh():
    m = load(MASTER)
    stamp = dt.datetime.now().strftime("%m%d_%H%M")
    bak = f"{W}/ipju_master.bak{stamp}.json"
    shutil.copy2(MASTER, bak)
    before = counts(m)[0]
    for r in m["단지목록"]:
        r["시점"] = calc_stages(r)
    refresh_posts(m)
    m["갱신"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    save(MASTER, m)
    after = counts(m)[0]
    print("백업:", bak)
    print("전:", before)
    print("후:", after)


# ---------------------------------------------------------------- 문서
def fmt_stage(v):
    if not v:
        return "-"
    if isinstance(v, dict):
        return f"{v['시작'][5:]}~{v['끝'][5:]}"
    return v[5:]


def post_brief(r):
    c = {}
    for p in r.get("글", []):
        k = kind_of(p["상태"])
        c[k] = c.get(k, 0) + 1
    return " ".join(f"{k}{v}" for k, v in c.items()) or "없음"


def cmd_doc(path=DOC):
    m = load(MASTER)
    prod = load(PRODUCTS)
    c, by = counts(m)
    rows = m["단지목록"]
    inn = sorted([r for r in rows if r["구분"] == "입주예정"],
                 key=lambda r: (r.get("입주시작") or "9999", -(r.get("세대") or 0)))
    two = sorted([r for r in rows if r["구분"] == "2년차"],
                 key=lambda r: ((r.get("2년되는달") or "9999")[:7], -(r.get("세대") or 0)))
    L = []
    L.append("# 낭만 입주 단지 통합 장부")
    L.append("")
    L.append(f"만든 때: {m.get('갱신') or m.get('만든때')} · 장부 `/home/claude/watch/ipju_master.json` · 상품표 `/home/claude/watch/ipju_stage_products.json` · 조회 `python3 /home/claude/watch/ipju_query.py`")
    L.append("")
    L.append(f"- 단지 {len(rows)}곳: 입주예정 {len(inn)} · 2년차 {len(two)}. 이름이 다른 같은 단지는 한 줄로 합침(옛 이름은 「별칭」).")
    L.append(f"- 글 상태(단지 이름이 든 글): 미작성 {c['미작성']} · 미발행 {c['미발행']} · 예약 {c['예약']} · 발행 {c['발행']}")
    L.append("- 시점: D60 = 입주 시작 60일 전(사전점검 전후) · D30 = 30일 전 · 직전 = 7일 전~당일 · 직후 = 당일~30일 · 2년차 = 2년 되는 달 60일 전~그 달 말.")
    L.append("- 입주 시작이 「달」만 알려진 단지는 그 달 1일로 셈(확인정도에 「월만」).")
    L.append("")
    L.append("## 앞으로 3주 써야 할 글")
    L.append("")
    td = todo_list(m, 21, 300)
    L.append(f"300세대 이상 {len(td)}칸 가운데 앞 40칸 · 순서: 수도권 → 충청 · 부산경남 → 그 밖, 날짜 확인된 단지 먼저, 칸이 닫히는 날 가까운 순. 전체는 `다음 21`.")
    L.append("")
    L.append("| 날 | 단지 | 시점(쓸 수 있는 기간) | 주력 상품 | 곁들임 | 잡힌 칸 |")
    L.append("|---|---|---|---|---|---|")
    for x in td[:40]:
        L.append(f"| {x['날'][5:]} | {x['단지']} ({x['지역'] or '-'}) | {x['시점']} ({x['기간'][5:10]}~{x['기간'][16:]}) | {' · '.join(x['주력'])} | {' · '.join(x['곁들임'])} | {'<br>'.join(x['잡힌칸']) or '-'} |")
    L.append("")
    L.append("## 시점별 팔 상품 (제휴 품목만)")
    L.append("")
    L.append("| 시점 | 언제 | 주력 2 | 곁들임 | 겨울(11~2월) |")
    L.append("|---|---|---|---|---|")
    for s in STAGES:
        sp = prod["시점"][s]
        w = sp.get("겨울")
        L.append(f"| {s} | {sp['때']} | {' · '.join(sp['주력'])} | {' · '.join(sp['곁들임'])} | {(' · '.join(w['주력']) + ' / ' + ' · '.join(w['곁들임'])) if w else '같음'} |")
    L.append("")
    L.append("단지 특성 조정: " + " · ".join(f"{(x.get('유형') or x.get('특성'))} → {x['메모']}" for x in prod["단지_특성_조정"]))
    L.append("")
    L.append(f"## 입주예정 {len(inn)}곳 (입주 시작 가까운 순)")
    L.append("")
    L.append("| 입주 시작 | 단지 | 지역 | 세대 | 유형 | 사전점검 | D60 | D30 | 직전 | 직후 | 글 | 확인 |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in inn:
        st = r["시점"]
        L.append(f"| {r.get('입주시작') or '-'} | {r['단지']} | {r.get('지역') or '-'} | {r.get('세대') or '-'} | {r.get('유형') or '-'} | {r.get('사전점검일') or '-'} | {fmt_stage(st['D60'])} | {fmt_stage(st['D30'])} | {fmt_stage(st['직전'])} | {fmt_stage(st['직후'])} | {post_brief(r)} | {r.get('확인정도') or '-'} |")
    L.append("")
    L.append(f"## 2년차 {len(two)}곳 (2년 되는 달 순)")
    L.append("")
    L.append("| 2년 되는 달 | 단지 | 지역 | 세대 | 입주 | 글 | 우편 | 확인 |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in two:
        L.append(f"| {r.get('2년되는달') or '-'} | {r['단지']} | {r.get('지역') or '-'} | {r.get('세대') or '-'} | {r.get('입주시작') or '-'} | {post_brief(r)} | {r.get('우편') or '-'} | {r.get('확인정도') or '-'} |")
    L.append("")
    L.append("## 갱신 방법")
    L.append("")
    L.append("- 글 상태: `python3 /home/claude/watch/ipju_query.py 갱신` — mix_schedule_1017c.json(우선) · ipju_pub_plan.json · 발행글_목록에서 단지 이름이 든 글을 다시 읽음. 장부는 `ipju_master.bak<MMDD_HHMM>.json`으로 먼저 백업. mix_schedule은 읽기만 함(「예약 …」 줄 안 고침).")
    L.append("- 새 글을 쓰면: 그 단지 「글」에 `{제목, 품목, 날, 시점, 상태: 미발행, PC폴더, 출처: 수동}`으로 더함. mix_schedule에 같은 제목이 생기면 갱신 때 mix 쪽 줄로 바뀜.")
    L.append("- 새 단지 · 날짜가 바뀐 단지: 그 줄의 입주시작 · 입주지정기간 · 사전점검일 · 출처 · 확인정도를 고친 뒤 `갱신`(시점을 다시 셈). 이름이 다르면 「별칭」에 더함.")
    L.append("- 조회: `다음 21` · `단지 <이름>` · `상태` · 이 문서 다시 만들기 `문서`.")
    L.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print("문서:", path)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    c = argv[1]
    if c in ("다음", "next"):
        nums = [int(re.sub(r"\D", "", a)) for a in argv[2:] if re.sub(r"\D", "", a)]
        cmd_next(nums[0] if nums else 21, "전부" in argv[2:], nums[1] if len(nums) > 1 else 0)
    elif c in ("단지", "danji"):
        cmd_danji(" ".join(argv[2:]))
    elif c in ("상태", "status"):
        cmd_status()
    elif c in ("갱신", "refresh"):
        cmd_refresh()
    elif c in ("문서", "doc"):
        cmd_doc()
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
