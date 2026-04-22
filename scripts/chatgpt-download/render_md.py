"""Render a ChatGPT conversation JSON (from parse_turbostream.py or backend-api)
as a markdown file matching the project's conventions.

Conventions:
- LaTeX-native math delimiters: `\\(...\\)` inline, `\\[...\\]` display. Do NOT convert.
- Per-message timestamp in role header: `## User (2026-04-22 08:23)`.
- Skip system and tool messages (system is usually empty; tool output is redacted).
- Skip `code`, `thoughts`, and `model_editable_context` content types
  (tool-call JSON and internal-only).
- Keep `text` and `reasoning_recap` content types.
- Strip ChatGPT internal file-citation markers wrapped in PUA chars U+E200..U+E202.

Usage:
    python3 render_md.py conversation.json -o out.md [--source-url URL]
"""
import argparse, json, re
from datetime import datetime, timezone

def fmt_ts(ts):
    if ts is None:
        return ''
    try:
        ts = float(ts)
    except (TypeError, ValueError):
        return ''
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

def fmt_day(ts):
    try:
        ts = float(ts)
    except (TypeError, ValueError):
        return ''
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def slugify(s, limit=60):
    s = (s or '').lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:limit].rstrip('-') or 'untitled'

def linearize(conv):
    mp = conv.get('mapping') or {}
    node = conv.get('current_node')
    chain, seen = [], set()
    while node and node not in seen:
        seen.add(node)
        n = mp.get(node)
        if not n:
            break
        chain.append(node)
        node = n.get('parent')
    chain.reverse()
    return chain

def extract_text(msg):
    c = msg.get('content') or {}
    ct = c.get('content_type')
    if ct == 'text':
        parts = c.get('parts') or []
        out = []
        for p in parts:
            if isinstance(p, str) and p.strip():
                out.append(p)
            elif isinstance(p, dict):
                out.append(f'_[attachment: {p.get("content_type","unknown")}]_')
        return '\n\n'.join(out) if out else None
    if ct == 'reasoning_recap':
        return f'_{c.get("content","")}_'
    return None

def clean_citation_markers(text):
    # Strip ChatGPT's internal file-citation tokens wrapped in U+E200..U+E202
    text = re.sub(r'\s?filecite[-][^-]*[-]', '', text)
    text = re.sub(r'[-]', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def render(conv, source_url=None):
    title = conv.get('title') or 'Untitled'
    create_time = conv.get('create_time')
    # backend-api returns floats; share-page sometimes returns ISO strings.
    out = [f'# {title}', '']
    if source_url:
        out.append(f'- Source: {source_url}')
    if create_time:
        out.append(f'- Created: {fmt_day(create_time)}')
    if conv.get('default_model_slug'):
        out.append(f'- Default model: {conv["default_model_slug"]}')
    out += ['', '---', '']

    last_role = None
    for nid in linearize(conv):
        m = ((conv.get('mapping') or {}).get(nid) or {}).get('message') or {}
        role = ((m.get('author') or {}).get('role')) or ''
        if role in ('system', 'tool'):
            continue
        txt = extract_text(m)
        if not txt:
            continue
        ts = fmt_ts(m.get('create_time'))
        heading = {'user': 'User', 'assistant': 'Assistant'}.get(role, role.capitalize())
        if role == last_role == 'assistant':
            out.append('')
            out.append(txt)
        else:
            out.append(f'## {heading}' + (f' ({ts})' if ts else ''))
            out.append('')
            out.append(txt)
            out.append('')
        last_role = role

    return clean_citation_markers('\n'.join(out).rstrip() + '\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('json_path')
    ap.add_argument('-o', '--output', required=True)
    ap.add_argument('--source-url', default=None)
    args = ap.parse_args()
    conv = json.load(open(args.json_path, encoding='utf-8'))
    md = render(conv, args.source_url)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'wrote {args.output} ({len(md)} chars)')

if __name__ == '__main__':
    main()
