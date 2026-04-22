# ChatGPT bulk download — handoff to Windows Claude session

Date: 2026-04-22

## Goal

Download the 39 RH-related ChatGPT conversations from the last 14 days into
`paper/chats/` as markdown archives, then build a mapping from the existing
`paper/convo*.{txt,md}` manual dumps to the new files so the dumps can be
deleted after verification.

## Output conventions (already agreed with user)

- **Location**: `paper/chats/`
- **Filename**: `YYYYMMDD-HHMM-<slug>.md` — UTC create time of the chat, slug
  derived from the title (or the first user message if the title is empty /
  "New chat"). Slug: lowercase, hyphen-separated, max ~60 chars.
- **Format**: markdown. LaTeX-native math delimiters `\(...\)` / `\[...\]`.
  Do NOT convert to `$...$`. (See `CLAUDE.md` → "LaTeX conventions".)
- **Role headers**: `## User (2026-04-22 08:23)` / `## Assistant (...)` with
  the per-message UTC timestamp embedded.
- **Skip**: system messages (empty), tool messages (output redacted),
  internal tool-call JSON (`code` / `thoughts` / `model_editable_context`).
- **Keep**: user text, assistant text, assistant `reasoning_recap`
  ("Thought for Xs") as short italics.
- **Strip**: ChatGPT internal `filecite…turn#file#…` citation markers (they
  leak through wrapped in U+E200..U+E202 Private-Use-Area chars).

## What has already been done

- **`paper/convo33-rh-proof-summary-review.md`** — the first chat, extracted
  from its share URL using the turbo-stream parser (proven pipeline). This is
  one of the 39 chats and will be re-downloaded into the new filename format;
  keep it for now as a sanity reference and a cross-check target.
- **`CLAUDE.md`** — added a `## LaTeX conventions` section codifying the
  math-delimiter rule.
- **`scripts/chatgpt-download/`** — the working scripts, committed:
  - `fetch_index.js` — opens browser, waits for login/CF, enumerates the last
    N days from `/backend-api/conversations`. **Proven working** in WSL
    (pulled 2100 summaries in ~2 min).
  - `fetch_pages.js` — navigates to `chatgpt.com/c/<id>` for each listed
    chat and saves the HTML (which contains the SSR turbo-stream blob).
  - `parse_turbostream.py` — decodes the turbo-stream blob to a canonical
    ChatGPT conversation JSON. Proven on a share page; chat page should use
    the same format (the script already searches loaderData for a route key
    with a `mapping` field).
  - `render_md.py` — single-conversation JSON → markdown, with the
    conventions above.
  - `render_all.py` — glues the pipeline: parses every saved `.html`, writes
    `paper/chats/YYYYMMDD-HHMM-<slug>.md`, builds `_index.md`, and builds
    `_convo_mapping.md` by matching the first user message of each downloaded
    chat against `paper/convo*.{txt,md}`.
  - `chats_to_fetch.json` — the 39 chats to download (id + title + ISO
    timestamps + URL). Curated from a 14-day window; 11 non-RH chats
    (medical/dental/legal/Ruby/generic) and 1 generic "Model Inquiry" were
    excluded from the 50 hits. Item "Discrete vs Continuous Series" was kept
    by the user.
  - `README.md` — pipeline overview.

## What is NOT done and why

- Individual chat content has NOT been downloaded yet. The direct
  `/backend-api/conversation/<id>` endpoint returns a Cloudflare challenge
  HTML page (HTTP 403) in the WSL Chromium session even with a valid Bearer
  token — so the approach switched to navigating to the chat page and
  capturing its SSR blob (`fetch_pages.js`). That script exists but has not
  been run to completion in this session. The user also mentioned they may
  need to complete a human-verification challenge.

## Safety / account risk

Small data-collection run (39 reads of the user's own chats). Ban risk is
near zero with any approach. Ranking from safest to least safe:

1. **Official data export** (Settings → Data Controls → Export data).
   Sanctioned path, delivers a zip with `conversations.json` in minutes.
   No scraping, no CF issues, no new public artifacts. If the chat-page
   path hits trouble, fall back here — ask the user to trigger the export
   and then point `render_all.py` at the `conversations.json` inside the
   zip (each entry already has the same `mapping` structure).
2. **Chat-page HTML capture** (current `fetch_pages.js`). Traffic pattern is
   indistinguishable from a human clicking through their chat list. No new
   public artifacts created on ChatGPT's servers.
3. **Share-link creation then public download**. `POST /backend-api/share/
   create_or_update` publishes each chat to a public URL. Works, but
   creates 39 public artifacts that must be revoked afterward. Not
   recommended for private research drafts.

## Why Windows may work better

- Native Windows Chrome (not WSL Chromium) presents a browser fingerprint
  that is less likely to trip Cloudflare's per-endpoint checks.
- No WSLg display routing, so the browser window is more stable and
  responsive for completing human-verification challenges.
- If the `/backend-api/conversation/<id>` endpoint works directly from
  Windows, it's faster than the page-navigation fallback; if it still
  challenges, the page-navigation path already handles it.

## Handoff prompt for the Windows Claude session

Paste this verbatim (adjust paths if the repo isn't at `C:\workspace\riemann2`):

```
We're resuming a task to bulk-download 39 RH-related ChatGPT conversations
into paper/chats/. Previous session documented the plan and scripts at
C:\workspace\riemann2\lore\20260422-chatgpt-bulk-download-handoff.md and
C:\workspace\riemann2\scripts\chatgpt-download\. Read both and follow the
conventions exactly.

Pipeline in four steps:

1. cd C:\workspace\riemann2\scripts\chatgpt-download
2. npm init -y && npm install playwright
3. node fetch_pages.js     # opens a Chrome window; I'll log in and pass any
                           # Cloudflare challenge. Requires state.json OR
                           # an initial run of fetch_index.js to establish
                           # login state.
4. python render_all.py    # decodes each saved HTML, writes markdown files
                           # into paper\chats\YYYYMMDD-HHMM-slug.md, builds
                           # _index.md and _convo_mapping.md.

If fetch_pages.js cannot find the turbo-stream blob in the chat-page HTML,
the SSR structure for logged-in pages may differ from share pages. In that
case, try the alternative: use page.evaluate() to call
`/backend-api/conversation/<id>` directly from within the logged-in page
context (same approach fetch_index.js already uses for the list endpoint).
Playwright code to try:

  const data = await page.evaluate(async (id) => {
    const r = await fetch(`/backend-api/conversation/${id}`, {
      credentials: 'include',
      headers: { Accept: 'application/json' }
    });
    if (!r.ok) return { ok: false, status: r.status };
    return { ok: true, body: await r.json() };
  }, id);

If that returns JSON directly, write it to html/<id>.json instead and
adapt render_all.py to read JSON (conversations from backend-api already
look like the canonical form — no turbo-stream decode needed).

Before calling the task done:
- Confirm every chat in chats_to_fetch.json has a corresponding file in
  paper\chats\.
- Review paper\chats\_convo_mapping.md and confirm it's safe to delete the
  existing paper\convo*.{txt,md} dumps (do NOT delete without user sign-off).
- Commit in logical units: (a) new paper\chats\ content, (b) mapping/index,
  (c) any script changes. Follow git workflow from CLAUDE.md. Do not push.
```

## Chats to download (39, chronological by create_time UTC)

Authoritative source: `scripts/chatgpt-download/chats_to_fetch.json`. Table
inlined here for convenience.

| # | Create time (UTC) | Title | URL |
|---|---|---|---|
|  1 | 2026-04-10 04:36 | Riemann Hypothesis Insight | https://chatgpt.com/c/69d87e03-a5c8-83a5-9f21-1062e8b6d064 |
|  2 | 2026-04-15 07:37 | Discrete vs Continuous Series | https://chatgpt.com/c/69df401b-c1e4-83e8-a4be-b2333dd9e409 |
|  3 | 2026-04-16 10:38 | Riemann Hypothesis Proof Review | https://chatgpt.com/c/69e0bc07-7b34-83e8-847a-5c6a5cd45407 |
|  4 | 2026-04-16 18:17 | Proof of Riemann Hypothesis | https://chatgpt.com/c/69e1279e-22a4-83e8-8ef0-5d10fce5686c |
|  5 | 2026-04-18 09:07 | Proof review feedback | https://chatgpt.com/c/69e349d2-3f10-83e8-ab98-4d35cd0a90ce |
|  6 | 2026-04-18 10:41 | Pointwise vs Generic Residual | https://chatgpt.com/c/69e35fb3-8478-83e8-abe9-ca18f91230be |
|  7 | 2026-04-18 20:22 | Clean parallel prompts | https://chatgpt.com/c/69e3e7fd-3d28-83e8-b51c-dcdf2957ee1a |
|  8 | 2026-04-18 20:25 | Audit ECT Geometry | https://chatgpt.com/c/69e3e88a-d72c-83e8-ba45-8d05d3fc7917 |
|  9 | 2026-04-18 20:26 | Quintic septic algebra audit | https://chatgpt.com/c/69e3e881-5460-83e8-a0d1-997d0851a3d9 |
| 10 | 2026-04-18 20:26 | TeX draft audit | https://chatgpt.com/c/69e3e881-13f4-83e8-8804-ce366fbab3d3 |
| 11 | 2026-04-19 05:26 | Affine Normal Form Audit | https://chatgpt.com/c/69e46785-73e0-83e8-b0d7-a9231e9e7889 |
| 12 | 2026-04-19 10:02 | Proof of RH Assessment | https://chatgpt.com/c/69e4a803-6c74-83e8-91c9-e051c87bb3b2 |
| 13 | 2026-04-19 14:47 | Proof of RH Approach | https://chatgpt.com/c/69e4eae6-96f0-83e8-8184-fe6e31d2ddc9 |
| 14 | 2026-04-20 06:21 | Riemann Hypothesis Strategy | https://chatgpt.com/c/69e5c5cd-b3c0-83e8-8b43-586291570ff7 |
| 15 | 2026-04-20 06:22 | Riemann Hypothesis Proof | https://chatgpt.com/c/69e5c618-f070-83e8-8869-1b19f757855f |
| 16 | 2026-04-20 12:47 | Two-Point Theorem Proof | https://chatgpt.com/c/69e62051-7a90-83e8-8ac2-1a76ba3bc1e8 |
| 17 | 2026-04-20 12:47 | Global Three-Point Continuation | https://chatgpt.com/c/69e62016-4e34-83e8-a7fd-4df98f66b5d4 |
| 18 | 2026-04-20 12:48 | Nonmixed 4-Point Theorem | https://chatgpt.com/c/69e62038-ec70-83e8-8ecb-25e49ba74ce2 |
| 19 | 2026-04-20 14:50 | Riemann Hypothesis Analysis | https://chatgpt.com/c/69e63c9f-8e64-83e8-8f60-bc190180db4c |
| 20 | 2026-04-20 18:27 | Source-coupling and Odd-zero Exclusion | https://chatgpt.com/c/69e66fe2-81ec-83e8-9f83-9299237ddcc7 |
| 21 | 2026-04-20 18:28 | Shear-Transfer Theorem | https://chatgpt.com/c/69e67027-7cf8-83e8-a681-9f4037202891 |
| 22 | 2026-04-20 18:28 | Riemann Hypothesis Strategy | https://chatgpt.com/c/69e6703e-4c50-83e8-a1a2-61a7e158e8a2 |
| 23 | 2026-04-21 01:41 | Left Pincer Strategy | https://chatgpt.com/c/69e6d58d-44b0-83e8-a999-070700fac3fc |
| 24 | 2026-04-21 01:41 | Riemann Hypothesis Proof | https://chatgpt.com/c/69e6d5db-fb54-83e8-9ed8-0d220552d09f |
| 25 | 2026-04-21 03:17 | Riemann Hypothesis Derivatives | https://chatgpt.com/c/69e6ebf5-c3cc-83e8-86a6-62d412fb642e |
| 26 | 2026-04-21 03:17 | Riemann Hypothesis Derivative Geometry | https://chatgpt.com/c/69e6ec0c-c148-83e8-9e0a-62686c0027f5 |
| 27 | 2026-04-21 03:17 | Riemann Hypothesis Derivatives | https://chatgpt.com/c/69e6ebeb-7ea0-83e8-a035-b7411d9185b6 |
| 28 | 2026-04-21 04:26 | Continuation of Chat Work | https://chatgpt.com/c/69e6fc40-31dc-83e8-a5d0-6924ad55f533 |
| 29 | 2026-04-21 11:56 | Global Topological Theorem Search | https://chatgpt.com/c/69e765cf-ea88-83e8-b12e-ea7416fd9ccc |
| 30 | 2026-04-21 11:56 | Global Bad Core Proof | https://chatgpt.com/c/69e765d2-adf4-83e8-94bb-ffcfbeb71fbe |
| 31 | 2026-04-21 11:56 | New-Generator Audit RH | https://chatgpt.com/c/69e765d7-5d6c-83e8-9e3d-06ba5b7b418a |
| 32 | 2026-04-21 15:10 | Mathematical Argument Audit | https://chatgpt.com/c/69e79361-809c-83e8-979d-bc4f7102b786 |
| 33 | 2026-04-21 15:53 | RH Proof Discussion | https://chatgpt.com/c/69e79d64-0130-83e8-87bc-1bb77f7dc371 |
| 34 | 2026-04-21 16:23 | RH Proof Attack Strategy | https://chatgpt.com/c/69e7a480-ec5c-83e8-b81c-8e27b397c73e |
| 35 | 2026-04-21 19:36 | RH Proof Audit | https://chatgpt.com/c/69e7d1b3-bc78-83e8-ae00-6d5f87d4910b |
| 36 | 2026-04-21 22:00 | RH Proof Paper Review | https://chatgpt.com/c/69e7f339-555c-83e8-a257-2f35e2292c4d |
| 37 | 2026-04-22 00:29 | RH Proof Summary Review | https://chatgpt.com/c/69e815af-00cc-83e8-8873-cc8f92d10d93 |
| 38 | 2026-04-22 00:29 | RH Proof Paper Review | https://chatgpt.com/c/69e8163e-c9ac-83e8-9cf1-13041a52472f |
| 39 | 2026-04-22 01:11 | RH Attack Continuation | https://chatgpt.com/c/69e82031-f058-83e8-98cf-1a44101c5a14 |

Note: chat #37 is the one already captured as `paper/convo33-rh-proof-summary-review.md`
— useful as a cross-check target for the new-format output.

## Things the Windows Claude should NOT do

- Do NOT convert LaTeX math to `$...$` / `$$...$$` — see `CLAUDE.md`.
- Do NOT delete existing `paper/convo*.{txt,md}` dumps without user sign-off
  after the mapping file has been reviewed.
- Do NOT push commits — the project's git workflow is commit-only.
- Do NOT edit `paper/proof_of_rh.tex` or `paper/unverified.tex` as part of
  this task — this is an archival/ETL task, not a proof edit.

## Success criteria

- All 39 files present in `paper/chats/` with the correct naming convention.
- `paper/chats/_index.md` lists all 39.
- `paper/chats/_convo_mapping.md` attempts a match for every
  `paper/convo*.{txt,md}` (even if some have no match).
- A spot-check comparison of `convo33-rh-proof-summary-review.md` against
  its new-format counterpart shows equivalent content (same first user
  message, same number of user+assistant turns).
