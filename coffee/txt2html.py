# 낭만커피 txt 원고 → 블로거 HTML (소넷 몫 UI 입히기를 최소로)
import re, sys, json, os
exec(open("/home/claude/coffee/g_head.py", encoding="utf-8").read().split("def p(")[0].replace("os.makedirs(OUT, exist_ok=True)",""))
B="https://nangmancoffeebean.blogspot.com/2026/10/"; B11="https://nangmancoffeebean.blogspot.com/2026/11/"
U={"b00":B+"coffee-bean-types.html","b01":B+"brazil-coffee-beans.html","b02":B+"colombia-supremo.html","b03":B+"aa.html","b04":B+"mandheling.html","b05":B+"blog-post.html","g02":B+"blog-post_15.html","g01":B+"blog-post_497.html","g03":B+"blog-post_316.html","g04":B+"blog-post_83.html","k05":B+"single-origin-blend.html","k04":B+"coffee-grind-size.html","k02":B+"coffee-bitterness.html","k01":B+"coffee-body.html","k03":B+"coffee-bean-storage.html","m01":B11+"cold-brew.html","m02":B11+"decaf-coffee-beans.html","m03":B11+"coffee-bean-expiration.html"}
T={"b00":"원두 종류 특징, 아라비카와 로부스타부터 나라별 맛까지 한눈에","b01":"브라질 원두 특징, 세계 커피의 3분의 1이 자라는 넓은 고원","b04":"만델링 원두 특징, 수마트라 토바 호숫가의 묵직하고 흙내 나는 커피","g04":"커피 로스팅 단계, 초록 생두가 갈색 원두가 되기까지 12분","k05":"싱글오리진 뜻, 한 땅의 커피와 여러 땅을 섞은 블렌드의 차이","k04":"원두 분쇄도, 같은 원두가 굵기 하나로 시고 쓰게 바뀝니다","k02":"커피 쓴맛 이유, 볶은 시간과 내린 시간이 만드는 맛","k03":"원두 보관법, 봉투를 여는 순간부터 향이 날아갑니다"}
NOTE=('<div style="background:#f6efe6;border-radius:10px;padding:18px 20px;margin:34px 0 10px;font-size:16px;line-height:1.8;color:#4a2c1d;">낭만커피는 직접 볶는 로스터리의 원두를 카페에 이어 드립니다.<br>가게에 맞는 원두를 찾고 계시면 010-2882-8165로 연락 주세요.</div>')
NET=('<p style="font-size:14px;color:#7a6a5c;line-height:1.7;">낭만 네트워크 · <a href="https://nangmanbusinesscards.blogspot.com/">낭만 명함</a> · <a href="https://talk7921.tistory.com/">낭만 부동산 요약</a> · <a href="https://blog.naver.com/champion_chart">낭만 인테리어</a> · <a href="https://nangman-dosa.tistory.com/">낭만도사</a></p>')
def lk(s): return re.sub(r"\[([^\]]+)\]\((\w+)\)", lambda m:f'<a href="{U[m.group(2)]}">{m.group(1)}</a>', s)
def conv(path):
    L=open(path,encoding='utf-8').read().splitlines(); meta={}; out=[]; tb=[]
    def flush():
        if tb:
            h="".join(f"<th {TH}>{c}</th>" for c in tb[0]); r="".join("<tr>"+"".join(f"<td {TD}>{lk(c)}</td>" for c in row)+"</tr>" for row in tb[1:])
            out.append(f'<table {TB}><tr>{h}</tr>{r}</table>'); tb.clear()
    for l in L:
        if not l.strip(): flush(); continue
        if l.startswith('# '): meta['title']=l[2:]; continue
        m=re.match(r'(slug|labels|tail): (.*)',l)
        if m: meta[m.group(1)]=m.group(2); continue
        if l.startswith('|'): tb.append([c.strip() for c in l.strip().strip('|').split('|')]); continue
        flush()
        if l.startswith('> '): out.append(f'<p {LEAD}>{lk(l[2:])}</p>')
        elif l.startswith('## '): out.append(f'<h2 {H2}>{l[3:]}</h2>')
        else: out.append(f'<p {P}>{lk(l)}</p>')
    flush()
    li="".join(f'<li style="margin:0 0 10px;"><a href="{U[k.strip()]}">{T[k.strip()]}</a></li>' for k in meta['tail'].split(','))
    tail=(f'<div style="border:1px solid #e3d3c1;border-radius:10px;padding:18px 20px;margin:24px 0 16px;"><p style="font-size:18px;font-weight:700;color:#4a2c1d;margin:0 0 12px;">원두 이야기 더 읽기</p><ul style="font-size:16px;line-height:1.7;padding-left:20px;margin:0;">{li}</ul></div>')
    meta['h']="\n".join(out)+"\n"+NOTE+"\n"+tail+NET
    return meta
res={}
for i,f in enumerate(sys.argv[1:],1):
    m=conv(f); res[f"m0{i}"]={"t":m['title'],"h":m['h'],"s":m['slug'],"l":m['labels']}
    open(f"/home/claude/coffee/mposts/m0{i}.html","w",encoding="utf-8").write(m['h'])
open("/tmp/claude-0/-home-claude/ab32ed76-1083-5b6b-99db-deb7a9449a69/scratchpad/store_m.js","w").write("localStorage.setItem('nc_m',"+json.dumps(json.dumps(res,ensure_ascii=False),ensure_ascii=False)+");'saved '+localStorage.getItem('nc_m').length")
print({k:(v['t'],len(v['h'])) for k,v in res.items()})
