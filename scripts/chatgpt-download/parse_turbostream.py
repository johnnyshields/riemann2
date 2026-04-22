"""Parse a saved ChatGPT page HTML (share page or chat page).

ChatGPT's React Router server-renders the full conversation data into the page HTML
via `window.__reactRouterContext.streamController.enqueue("...")` calls, using the
turbo-stream deduplicated graph format. This script reconstructs the JSON.

Usage:
    python3 parse_turbostream.py /path/to/page.html -o conversation.json

The output is a canonical ChatGPT conversation object with at least:
    { title, create_time, update_time, mapping: {id: {message, parent, children}}, current_node, ... }

Proven on a share-page HTML dump on 2026-04-22 (convo33). If a logged-in
chat page (`chatgpt.com/c/<id>`) uses the same SSR pattern, this same parser
should work; if not, adapt the locator.
"""
import argparse, json, re, sys

def js_unescape(s: str) -> str:
    out = []
    i = 0
    esc_map = {'n':'\n','t':'\t','r':'\r','b':'\b','f':'\f','"':'"',"'":"'",'\\':'\\','/':'/'}
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            n = s[i+1]
            if n == 'u':
                out.append(chr(int(s[i+2:i+6], 16)))
                i += 6
                continue
            if n in esc_map:
                out.append(esc_map[n]); i += 2; continue
            out.append(n); i += 2; continue
        out.append(c); i += 1
    return ''.join(out)

def find_balanced_array(s: str, start: int = 0) -> int:
    depth = 0; in_str = False; esc = False
    for i in range(start, len(s)):
        c = s[i]
        if esc: esc = False; continue
        if c == '\\': esc = True; continue
        if c == '"': in_str = not in_str; continue
        if in_str: continue
        if c == '[': depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return i + 1
    return -1

# turbo-stream negative-index sentinels (Remix/React Router variant).
# -5 is used for null/false in the wild, so treat it as None.
SENTINELS = {-1: None, -2: None, -3: None, -5: None, -6: None, -7: None, -8: None}

def rehydrate(vals):
    L = len(vals)
    memo = {}
    def walk(v, stack):
        if isinstance(v, bool) or v is None:
            return v
        if isinstance(v, int):
            if v < 0 or v >= L:
                return SENTINELS.get(v, v)
            return resolve(v, stack)
        if isinstance(v, (float, str)):
            return v
        if isinstance(v, dict):
            out = {}
            for k, val in v.items():
                if isinstance(k, str) and k.startswith('_'):
                    try:
                        kidx = int(k[1:])
                        key = vals[kidx] if 0 <= kidx < L and isinstance(vals[kidx], str) else k
                    except ValueError:
                        key = k
                else:
                    key = k
                out[key] = walk(val, stack)
            return out
        if isinstance(v, list):
            return [walk(x, stack) for x in v]
        return v
    def resolve(idx, stack=frozenset()):
        if isinstance(idx, int):
            if idx < 0: return SENTINELS.get(idx)
            if idx >= L: return idx
        if idx in stack: return None
        if idx in memo: return memo[idx]
        r = walk(vals[idx], stack | {idx})
        memo[idx] = r
        return r
    return resolve(0)

def extract_conversation(html: str) -> dict:
    chunks = re.findall(r'streamController\.enqueue\("((?:[^"\\]|\\.)*)"\)', html)
    if not chunks:
        raise ValueError("No streamController.enqueue(...) chunks found in HTML.")
    total = ''.join(js_unescape(c) for c in chunks)
    end = find_balanced_array(total)
    if end < 0:
        raise ValueError("Unbalanced top-level array in turbo-stream output.")
    vals = json.loads(total[:end])
    root = rehydrate(vals)
    loader = root.get('loaderData', {})
    # Share page puts data under 'routes/share.$shareId.($action)' → serverResponse.data
    # Logged-in chat page may put it under a different route key; search for one that
    # contains a 'mapping'.
    for key, val in loader.items():
        if not isinstance(val, dict):
            continue
        sr = val.get('serverResponse')
        if isinstance(sr, dict):
            data = sr.get('data')
            if isinstance(data, dict) and 'mapping' in data:
                return data
        if 'mapping' in val:
            return val
    raise ValueError("Could not locate conversation data in loaderData: "
                     f"keys={list(loader.keys())}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html_path')
    ap.add_argument('-o', '--output', required=True)
    args = ap.parse_args()
    html = open(args.html_path, encoding='utf-8').read()
    conv = extract_conversation(html)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(conv, f, indent=2, ensure_ascii=False, default=str)
    print(f'title: {conv.get("title")}')
    print(f'messages: {len(conv.get("mapping", {}))}')
    print(f'wrote {args.output}')

if __name__ == '__main__':
    main()
