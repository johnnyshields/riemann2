"""Convert every saved .html in html/ into a markdown file under paper/chats/
with the naming convention `YYYYMMDD-HHMM-<slug>.md`.

Also emits `paper/chats/_index.md` with chat-id ↔ filename mapping, and
appends to `paper/chats/_convo_mapping.md` any existing `paper/convoNN.*`
file whose first user message matches one of the downloaded chats.

Usage:
    python3 render_all.py \
        [--html-dir html] \
        [--list chats_to_fetch.json] \
        [--out-dir ../../paper/chats] \
        [--repo-root ../..]
"""
import argparse, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from parse_turbostream import extract_conversation  # type: ignore
from render_md import render, slugify, fmt_ts  # type: ignore

def iso_to_yyyymmdd_hhmmss(iso_or_epoch):
    if iso_or_epoch is None:
        return '00000000-000000'
    if isinstance(iso_or_epoch, (int, float)):
        dt = datetime.fromtimestamp(float(iso_or_epoch), tz=timezone.utc)
    else:
        s = str(iso_or_epoch).rstrip('Z')
        try:
            dt = datetime.fromisoformat(s)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        except Exception:
            return '00000000-000000'
    return dt.strftime('%Y%m%d-%H%M%S')

def content_based_slug(conv, max_len=60):
    """Prefer the conversation title; fall back to first user message."""
    title = (conv.get('title') or '').strip()
    if title and title.lower() != 'new chat':
        return slugify(title, max_len)
    mp = conv.get('mapping') or {}
    # Walk in order and find first user text message
    for nid, n in mp.items():
        m = (n or {}).get('message') or {}
        if ((m.get('author') or {}).get('role')) != 'user':
            continue
        parts = (m.get('content') or {}).get('parts') or []
        for p in parts:
            if isinstance(p, str) and p.strip():
                return slugify(p, max_len)
    return 'untitled'

def first_user_message(conv):
    mp = conv.get('mapping') or {}
    for nid, n in mp.items():
        m = (n or {}).get('message') or {}
        if ((m.get('author') or {}).get('role')) != 'user':
            continue
        parts = (m.get('content') or {}).get('parts') or []
        for p in parts:
            if isinstance(p, str) and p.strip():
                return p.strip()
    return ''

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--html-dir', default=str(HERE / 'html'))
    ap.add_argument('--list', default=str(HERE / 'chats_to_fetch.json'))
    ap.add_argument('--out-dir', default=str(HERE.parent.parent / 'paper' / 'chats'))
    ap.add_argument('--repo-root', default=str(HERE.parent.parent))
    args = ap.parse_args()

    list_path = Path(args.list)
    html_dir = Path(args.html_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    chats = json.loads(list_path.read_text()) if list_path.exists() else []
    index_rows = []  # for _index.md
    first_user_by_id = {}  # id -> first user text (for convo## matching)

    for c in chats:
        cid = c['id']
        json_path = html_dir / f'{cid}.json'
        html_path = html_dir / f'{cid}.html'
        if json_path.exists():
            try:
                conv = json.loads(json_path.read_text(encoding='utf-8'))
            except Exception as e:
                print(f'PARSE FAILED {cid}: {e}', file=sys.stderr)
                continue
        elif html_path.exists():
            try:
                conv = extract_conversation(html_path.read_text(encoding='utf-8'))
            except Exception as e:
                print(f'PARSE FAILED {cid}: {e}', file=sys.stderr)
                continue
        else:
            print(f'MISSING: {json_path} (and no .html)', file=sys.stderr)
            continue
        stamp = iso_to_yyyymmdd_hhmmss(c.get('create_time') or conv.get('create_time'))
        slug = content_based_slug(conv)
        out_path = out_dir / f'{stamp}-{cid}-{slug}.md'
        md = render(conv, source_url=c.get('url') or f'https://chatgpt.com/c/{cid}')
        out_path.write_text(md, encoding='utf-8')
        print(f'wrote {out_path}')
        index_rows.append((out_path.name, cid, conv.get('title') or ''))
        first_user_by_id[cid] = first_user_message(conv)

    # Write _index.md
    idx_path = out_dir / '_index.md'
    lines = ['# Chat index', '',
             f'_{len(index_rows)} chats rendered at {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}_',
             '', '| File | Chat ID | Title |', '|---|---|---|']
    for fname, cid, title in sorted(index_rows):
        safe_title = (title or '').replace('|', '\\|')
        lines.append(f'| [{fname}]({fname}) | `{cid}` | {safe_title} |')
    idx_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {idx_path}')

    # Build convo## → new-file mapping by matching first-user-message bytes
    repo_root = Path(args.repo_root)
    paper = repo_root / 'paper'
    convo_files = sorted([p for p in paper.glob('convo*.*') if p.is_file()])
    mapping_lines = ['# convo## ↔ downloaded chat mapping', '',
                     '_Generated by render_all.py — check before deleting `paper/convo*.{txt,md}`._',
                     '',
                     '| convo file | matched new file | chat id | confidence |', '|---|---|---|---|']
    def tail_score(fu, text):
        """Longest suffix window of fu found in text (the distinguishing tail)."""
        for n in (1500, 800, 500, 300, 200):
            if len(fu) >= n and fu[-n:] in text:
                return n
        return 0

    def prefix_score(fu, text):
        """Longest prefix window of fu found in text (may match shared boilerplate)."""
        for n in (1500, 800, 500, 300, 200):
            if len(fu) >= n and fu[:n] in text:
                return n
        return 0

    for cf in convo_files:
        try:
            text = cf.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        # Prefer a chat whose distinguishing tail appears in the convo.
        best_tail = (None, 0)
        for cid, fu in first_user_by_id.items():
            if not fu:
                continue
            s = tail_score(fu, text)
            if s > best_tail[1]:
                best_tail = (cid, s)
        if best_tail[0]:
            new_file = next((fn for fn, cid, _ in index_rows if cid == best_tail[0]), '?')
            mapping_lines.append(f'| {cf.name} | {new_file} | `{best_tail[0]}` | tail ({best_tail[1]} ch) |')
            continue
        # Fallback: match on shared boilerplate prefix (ambiguous — mark as such).
        best_pre = (None, 0)
        for cid, fu in first_user_by_id.items():
            if not fu:
                continue
            s = prefix_score(fu, text)
            if s > best_pre[1]:
                best_pre = (cid, s)
        if best_pre[0]:
            new_file = next((fn for fn, cid, _ in index_rows if cid == best_pre[0]), '?')
            mapping_lines.append(f'| {cf.name} | {new_file} | `{best_pre[0]}` | prefix-only ({best_pre[1]} ch) |')
        else:
            mapping_lines.append(f'| {cf.name} | _no match_ | — | — |')

    mapping_lines += [
        '',
        '## Known gaps (data not recoverable from the downloaded JSON)',
        '',
        '- **`convo01.txt`** — source chat is "Discrete vs Continuous Series" (`69df401b-c1e4-83e8-a4be-b2333dd9e409`). The `/backend-api/conversation/<id>` endpoint returns HTTP 500 (`"Can\'t load conversation"`) for this chat — the conversation is too large for the server to assemble in one call. The UI loads it incrementally. Recovery path: official ChatGPT data export (Settings → Data controls → Export data); the resulting `conversations.json` includes this chat. Until then, `convo01.txt` is the only local copy of the content.',
        '- **`convo11.txt`** — source chat is "Proof of RH Approach" (`69e4eae6-96f0-83e8-8184-fe6e31d2ddc9`), captured as `20260419-144723-proof-of-rh-approach.md`. The downloaded chat is linear (1971 nodes, 0 branch points) — ChatGPT pruned the regenerated-away branches from the mapping tree. `convo11.txt` preserves earlier assistant responses that were later regenerated and are no longer in the JSON. The downloaded render is the current active branch only.',
        '- **`convo11b-rh-deriv-geometry.txt`** — same source chat as `convo11.txt`. Content is redundant with the downloaded render; differences are encoding artifacts from pasting the UI-rendered (KaTeX) LaTeX back as Unicode rather than `\\(...\\)` source. Safe to treat as a duplicate of `20260419-144723-proof-of-rh-approach.md`.',
        '',
    ]
    (out_dir / '_convo_mapping.md').write_text('\n'.join(mapping_lines) + '\n', encoding='utf-8')
    print(f'wrote {out_dir / "_convo_mapping.md"}')

if __name__ == '__main__':
    main()
