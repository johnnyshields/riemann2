# ChatGPT bulk download

Tools for downloading RH-related ChatGPT conversations into
`paper/chats/` as markdown archives.

## Pipeline

1. **`fetch_index.js`** — open a logged-in Chromium, list conversations in
   the last N days via `/backend-api/conversations` (works — that endpoint
   responds with JSON when a real browser session is attached). Writes
   `recent.json`.
2. **Filter `recent.json`** down to the chats you want to archive and save
   as `chats_to_fetch.json` (same schema, plus a `url` field). For this
   session that list is already curated — see `chats_to_fetch.json`.
3. **`fetch_pages.js`** — navigate to `chatgpt.com/c/<id>` for each chat
   and save the rendered HTML to `html/<id>.html`. The HTML contains the
   full conversation data embedded in a React-Router turbo-stream blob.
   (The `/backend-api/conversation/<id>` endpoint returns a Cloudflare
   challenge in the current WSL browser session, so we use the page HTML
   instead. A real browser on Windows may not hit that challenge; if so,
   an API fetch would also work.)
4. **`parse_turbostream.py`** — decode the turbo-stream blob from a saved
   `.html` into a canonical ChatGPT conversation JSON.
5. **`render_md.py`** — render one conversation JSON to markdown.
6. **`render_all.py`** — glue: for every chat in `chats_to_fetch.json`,
   parse its saved HTML and write `paper/chats/YYYYMMDD-HHMM-<slug>.md`.
   Also writes `paper/chats/_index.md` (chat-id ↔ filename) and
   `paper/chats/_convo_mapping.md` (best-effort mapping from existing
   `paper/convoNN.*` files to the new filenames, by matching the first
   user message).

## Output conventions

- Filename: `YYYYMMDD-HHMM-<slug>.md` where the timestamp is the chat's
  `create_time` (UTC) and the slug is derived from the title (or the first
  user message when the title is empty/"New chat").
- Format: markdown with LaTeX-native math delimiters `\(...\)` / `\[...\]`.
  Do not convert to `$...$` — see `CLAUDE.md` "LaTeX conventions".
- Role headers: `## User (2026-04-22 08:23)` / `## Assistant (...)`.
- Skipped: system messages, tool messages (redacted), internal tool-call
  JSON (`code` / `thoughts` / `model_editable_context`).
- Kept: user text, assistant text, assistant `reasoning_recap`
  ("Thought for Xs") as short italicized notes.
- ChatGPT internal `filecite…turn#file#…` citation markers (wrapped in
  U+E200..U+E202 PUA chars) are stripped.

## Installation

Playwright Node module is required for `fetch_*.js`:

```bash
cd scripts/chatgpt-download
npm init -y
npm install playwright
# On a fresh machine:
npx playwright install chromium
```

On WSL the bundled Chromium (`~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`)
works; point `CHROME_PATH` at it if needed. On Windows, omit `CHROME_PATH`
and Playwright will find its bundled browser automatically.

## Running end-to-end

```bash
cd scripts/chatgpt-download

# 1. Login + pull the last 14 days of conversation metadata.
#    A browser window opens; log in and complete any CF checks.
node fetch_index.js --days 14 --out recent.json

# 2. (Manual or scripted) filter recent.json → chats_to_fetch.json.
#    For this session the list is already committed.

# 3. Download the HTML for every chat in the list.
node fetch_pages.js

# 4. Render to markdown + build the indexes.
python3 render_all.py
```

## Proven on

- 2026-04-22: share-page turbo-stream decode (convo33 in `paper/`). The
  chat-page SSR is expected to use the same turbo-stream format; if the
  `loaderData` route key differs, `parse_turbostream.extract_conversation`
  already loops over loaderData to find the entry with a `mapping` field.
