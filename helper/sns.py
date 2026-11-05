#!/usr/bin/env python3
"""낭만 SNS 예약 장부 (11/6~ · Upload-Post 대신)
블로그 우체통(gas/Sns.gs)이 드라이브 「블로그/SNS예약/대기」의 json을 예약 시각에 인스타 · 스레드 공식 API로 올린다.
유튜브 · 틱톡은 공식 API가 심사 전 비공개라 어사이드 지시 파일(블로그/협업/4_어사이드)로 보낸다.

  python3 sns.py add --account kimdongjin24 --platforms instagram,threads --when "2026-11-10 21:10" \
      --caption-file cap.txt [--threads-file th.txt] [--first-comment "…"] [--threads-reply "…"] [--topic 인테리어] \
      [--id 이름] [--drive-id <드라이브 id> …] [로컬 파일 …]
  python3 sns.py yt --channel "낭만 인테리어" --when "2026-11-10 21:10" --title "…" --desc-file d.txt --drive-id <영상 id> [--thumb-id <id>]
  python3 sns.py tiktok --account hidjkim2000 --when "…" --caption-file c.txt --drive-id <영상 id>
  python3 sns.py status            → 블로그/SNS예약/상태.json (토큰 만료일 · 최근 결과 · DRY_RUN)
  python3 sns.py check <이름.json>  → 대기 글 하나 지금 검사
  python3 sns.py find <파일 이름>   → 드라이브에서 id 찾기
  python3 sns.py from-uploadpost <list_scheduled 결과 파일> --after "2026-11-27 00:00" [--write]
      → Upload-Post 예약을 이 장부(인스타 · 스레드)와 어사이드 지시(유튜브 · 틱톡)로 옮긴다. --write 없으면 미리보기만.
      끝에 나오는 cancel_job_ids 는 Upload-Post cancel_scheduled 로 지운다(두 번 올라가지 않게).
계정 이름 = 스크립트 속성 TOK_IG_<계정> · TOK_TH_<계정> 의 <계정>.
"""
import argparse, base64, datetime as dt, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

QUEUE = '블로그/SNS예약/대기'
MEDIA = '블로그/SNS예약/미디어'
ASIDE = '블로그/협업/4_어사이드'
# Upload-Post 프로필 → 새 장부 계정 (11/6 기준 연결 상태)
PROFILE = {
    'default': {'instagram': 'kimdongjin24', 'threads': 'kimdongjin24', 'youtube': '낭만 인테리어 (@nangman_interior)'},
    'nangman_budongsan': {'instagram': 'dong.jin.kim.nangman', 'threads': 'dong.jin.kim.nangman', 'youtube': '낭만 부동산 (@nangman.budongsan)'},
    'life_webtoon': {'instagram': 'nowand1969', 'threads': 'nowand1969'},
    'nangman_dosa': {'threads': 'nangman.group', 'youtube': '도사낭만 (@도사낭만)', 'tiktok': 'hidjkim2000'},  # 인스타 nangman.group 은 11/5 포기
    'nangman_sigol': {'threads': 'nangman.sigol'},
}
BLOG = {'default': 'champion_chart', 'nangman_budongsan': 'dong_jin_kim', 'nangman_dosa': 'give_me_travel'}


def gas(action, **kw):
    from gas import call
    return call(action, **kw)


def has_gas():
    return os.path.exists(os.environ.get('GAS_CONF', '/home/claude/gas/conf.json'))


def put_text(path, name, text):
    return gas('fput', path=path, name=name, text=text)


def put_file(path, local):
    return gas('fput', path=path, name=os.path.basename(local), b64=base64.b64encode(open(local, 'rb').read()).decode())


def when_ok(s):
    return dt.datetime.strptime(s.strip()[:16].replace('T', ' '), '%Y-%m-%d %H:%M')


def item_name(when, account, tag):
    w = when_ok(when)
    return f"{w:%m%d_%H%M}_{account}_{re.sub(r'[^0-9A-Za-z가-힣_.-]', '', tag)[:24]}.json"


def read(path):
    return open(path, encoding='utf-8').read().strip() if path else None


def cmd_add(a):
    media = [{'drive': i} for i in (a.drive_id or [])]
    for f in a.files:
        media.append({'drive': put_file(MEDIA, f)['id']})
    item = {'id': a.id or os.path.splitext(os.path.basename(a.files[0]))[0] if a.files else (a.id or a.account),
            'when': when_ok(a.when).strftime('%Y-%m-%d %H:%M'), 'account': a.account,
            'platforms': a.platforms.split(','), 'media': media, 'caption': read(a.caption_file) or ''}
    if a.threads_file: item['threads_text'] = read(a.threads_file)
    if a.first_comment: item['first_comment'] = a.first_comment
    if a.threads_reply: item['threads_reply'] = a.threads_reply
    if a.topic: item['topic_tag'] = a.topic
    name = item_name(item['when'], a.account, item['id'])
    r = put_text(QUEUE, name, json.dumps(item, ensure_ascii=False, indent=1))
    return {'queued': name, 'file_id': r.get('id'), 'media': len(media)}


def aside_line(kind, target, when, title, desc, vid, thumb=None):
    s = [f"■ {when} · {kind} {target}", f"  영상: 드라이브 파일 id {vid}" + (f" · 썸네일 id {thumb}" if thumb else ''),
         f"  제목: {title}"]
    if desc: s.append('  설명:\n' + '\n'.join('    ' + x for x in desc.splitlines()))
    return '\n'.join(s)


def aside_file(lines, tag):
    head = ("[어사이드 지시] 유튜브 · 틱톡 예약 — 규칙: 블로그/협업/0_지시/어사이드_유튜브틱톡예약_1106.txt\n"
            "아래 줄마다: 드라이브에서 영상을 받아 → 해당 채널에 올리고 → 공개 범위 「예약」 → 적힌 날짜 · 시각(한국 시간).\n"
            "제목 · 설명은 그대로 붙여 넣는다. 끝나면 5_보고 에 「유튜브틱톡예약_" + tag + "_보고」(줄마다 예약 시각 · 막힌 곳).\n\n")
    name = f"지시_유튜브틱톡예약_{tag}.txt"
    put_text(ASIDE, name, head + '\n\n'.join(lines) + '\n')
    return name


def cmd_yt(a, kind='유튜브'):
    target = a.channel if kind == '유튜브' else a.account
    line = aside_line(kind, target, when_ok(a.when).strftime('%Y-%m-%d %H:%M'), a.title or '', read(a.desc_file) or read(getattr(a, 'caption_file', None)) or '', a.drive_id[0], a.thumb_id)
    return {'aside': aside_file([line], when_ok(a.when).strftime('%m%d_%H%M') + ('_yt' if kind == '유튜브' else '_tt'))}


def find_drive(name, cache):
    if not name: return None
    if name in cache: return cache[name]
    hit = None
    if has_gas():
        try:
            r = gas('sns_find', name=name)
            r.sort(key=lambda x: (x.get('folder') not in ('shorts', '미디어'), -x.get('size', 0)))
            hit = r[0]['id'] if r else None
        except Exception as e:
            hit = None
    cache[name] = hit
    return hit


def kst(p):
    if p.get('original_timezone') == 'Asia/Seoul' and p.get('original_scheduled_str'):
        return dt.datetime.fromisoformat(p['original_scheduled_str'][:19])
    return dt.datetime.fromisoformat(p['scheduled_date'][:19]) + dt.timedelta(hours=9)


def cmd_from_up(a):
    s = open(a.file, encoding='utf-8').read()
    posts = json.loads(s[s.find('{'):])['scheduled_posts']
    after = when_ok(a.after)
    out = {'queue': [], 'aside': [], 'skipped': [], 'cancel_job_ids': [], 'needs_check': []}
    cache, aside_lines = {}, []
    for p in sorted(posts, key=kst):
        w = kst(p)
        if w < after: continue
        if a.only and p['job_id'] not in a.only: continue
        prof, acc = p['profile_username'], PROFILE.get(p['profile_username'], {})
        pc = p.get('platform_content') or {}
        txt = lambda pl: ((pc.get(pl) or {}).get('title') or p.get('title') or '').strip()
        when = w.strftime('%Y-%m-%d %H:%M')
        media_id = find_drive(p.get('source_filename'), cache) if p['post_type'] in ('photo', 'video') else None
        if p['post_type'] in ('photo', 'video') and not media_id:
            out['needs_check'].append({'job': p['job_id'], 'when': when, 'why': '드라이브에서 원본 못 찾음: ' + str(p.get('source_filename'))})
        logno = re.search(r'(22\d{10})', (p.get('source_filename') or '') + ' ' + p.get('title', ''))
        link = f"https://blog.naver.com/{BLOG.get(prof, '')}/{logno.group(1)}" if logno and BLOG.get(prof) else None
        sns = [pl for pl in p['platforms'] if pl in ('instagram', 'threads') and acc.get(pl)]
        groups = {}
        for pl in sns: groups.setdefault(acc[pl], []).append(pl)
        moved_all = True
        for account, pls in groups.items():
            item = {'id': p['job_id'][:8], 'when': when, 'account': account, 'platforms': pls,
                    'media': [{'drive': media_id}] if media_id else [], 'from_uploadpost': p['job_id']}
            if 'instagram' in pls: item['caption'] = txt('instagram')
            if 'threads' in pls:
                item['threads_text'] = txt('threads')
                if (p.get('fields') or {}).get('threads_topic_tag'): item['topic_tag'] = p['fields']['threads_topic_tag']
                if link: item['threads_reply'] = '자세한 글 ' + link
            if 'instagram' in pls and link: item['first_comment'] = '자세한 글 ' + link
            if '답글' in txt('threads') and not link:
                out['needs_check'].append({'job': p['job_id'], 'when': when, 'why': '본문에 「답글에 링크」가 있는데 글 주소를 못 찾음'})
            if p['post_type'] in ('photo', 'video') and not media_id:
                moved_all = False; continue
            if a.aside_sns:   # 프로그램이 아직 안 될 때: 어사이드가 인스타 · 스레드 자체 예약으로
                for pl in pls:
                    body = item.get('caption') if pl == 'instagram' else item.get('threads_text')
                    extra = item.get('first_comment') if pl == 'instagram' else item.get('threads_reply')
                    aside_lines.append(aside_line('인스타' if pl == 'instagram' else '스레드', account, when, body,
                                                  ('첫 댓글: ' + extra) if extra else '', media_id or '(사진 · 영상 없음)'))
                continue
            name = item_name(when, account, p['job_id'][:8])
            if a.write: put_text(QUEUE, name, json.dumps(item, ensure_ascii=False, indent=1))
            out['queue'].append(name)
        for pl in p['platforms']:
            if pl == 'youtube' and acc.get('youtube'):
                yt = pc.get('youtube') or {}
                aside_lines.append(aside_line('유튜브', acc['youtube'], when, yt.get('title') or txt('youtube'), yt.get('caption') or p.get('description') or txt('instagram'), media_id or ('(원본 못 찾음: ' + str(p.get('source_filename')) + ')')))
            elif pl == 'tiktok' and acc.get('tiktok'):
                aside_lines.append(aside_line('틱톡', acc['tiktok'], when, txt('tiktok'), '', media_id or '(원본 못 찾음)'))
            elif pl not in sns:
                out['skipped'].append({'job': p['job_id'], 'when': when, 'platform': pl, 'why': '옮길 곳 없음(틱톡 중단 · 끊긴 계정)'})
        if moved_all: out['cancel_job_ids'].append(p['job_id'])
    if aside_lines:
        out['aside'] = [aside_file(aside_lines, after.strftime('%m%d') + '_이관')] if a.write else [f'{len(aside_lines)}줄(미리보기)']
    out['count'] = {k: len(v) for k, v in out.items() if isinstance(v, list)}
    return out


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    x = sp.add_parser('add'); x.add_argument('--account', required=True); x.add_argument('--platforms', default='instagram,threads')
    x.add_argument('--when', required=True); x.add_argument('--caption-file'); x.add_argument('--threads-file')
    x.add_argument('--first-comment'); x.add_argument('--threads-reply'); x.add_argument('--topic'); x.add_argument('--id')
    x.add_argument('--drive-id', action='append'); x.add_argument('files', nargs='*')
    y = sp.add_parser('yt'); y.add_argument('--channel', required=True); y.add_argument('--when', required=True)
    y.add_argument('--title', required=True); y.add_argument('--desc-file'); y.add_argument('--drive-id', action='append', required=True); y.add_argument('--thumb-id')
    t = sp.add_parser('tiktok'); t.add_argument('--account', required=True); t.add_argument('--when', required=True)
    t.add_argument('--caption-file'); t.add_argument('--drive-id', action='append', required=True)
    sp.add_parser('status'); c = sp.add_parser('check'); c.add_argument('name'); f = sp.add_parser('find'); f.add_argument('name')
    u = sp.add_parser('from-uploadpost'); u.add_argument('file'); u.add_argument('--after', required=True); u.add_argument('--write', action='store_true')
    u.add_argument('--only', nargs='*', help='이 job_id만'); u.add_argument('--aside-sns', action='store_true', help='인스타 · 스레드도 어사이드 지시로')
    d = sp.add_parser('dry'); d.add_argument('onoff', choices=['on', 'off'])
    a = ap.parse_args()
    if a.cmd == 'add': r = cmd_add(a)
    elif a.cmd == 'yt': r = cmd_yt(a)
    elif a.cmd == 'tiktok': a.title = read(a.caption_file); a.desc_file = None; a.thumb_id = None; r = cmd_yt(a, '틱톡')
    elif a.cmd == 'status': r = gas('sns_status')
    elif a.cmd == 'check': r = gas('sns_check', name=a.name)
    elif a.cmd == 'find': r = gas('sns_find', name=a.name)
    elif a.cmd == 'dry': r = gas('sns_dry', on=a.onoff == 'on')
    else: r = cmd_from_up(a)
    print(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
