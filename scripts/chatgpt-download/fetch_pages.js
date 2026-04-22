// Download the full page HTML for each chat listed in chats_to_fetch.json
// by navigating to https://chatgpt.com/c/<id> in the logged-in browser and
// saving the rendered HTML. The HTML contains the full conversation data
// in a React-Router turbo-stream blob that parse_turbostream.py can decode.
//
// Why not the backend-api/conversation/<id> endpoint directly? That endpoint
// returns a Cloudflare challenge (HTML) instead of JSON in WSL-hosted Chromium
// sessions, while the chat page itself renders normally. Using the page HTML
// is equivalent and bypasses the challenge.
//
// Output: one .html file per chat under `out/` (default `./html/<id>.html`).
//
// Usage:
//   node fetch_pages.js [--list chats_to_fetch.json] [--out html] [--state state.json]

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const args = Object.fromEntries(process.argv.slice(2).reduce((acc, x, i, a) => {
  if (x.startsWith('--')) {
    const key = x.slice(2);
    const val = (i + 1 < a.length && !a[i + 1].startsWith('--')) ? a[i + 1] : true;
    acc.push([key, val]);
  }
  return acc;
}, []));

const LIST = args.list || path.join(__dirname, 'chats_to_fetch.json');
const OUT_DIR = args.out || path.join(__dirname, 'html');
const STATE = args.state || path.join(__dirname, 'state.json');
const EXE = process.env.CHROME_PATH || null;

function hasTurboStream(html) {
  return /streamController\.enqueue\("/.test(html) &&
         /"mapping"/.test(html);
}

(async () => {
  if (!fs.existsSync(LIST)) { console.error('missing', LIST); process.exit(1); }
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const list = JSON.parse(fs.readFileSync(LIST, 'utf-8'));

  const browser = await chromium.launch(Object.assign(
    { headless: false },
    EXE ? { executablePath: EXE } : {}
  ));
  const ctx = await browser.newContext(fs.existsSync(STATE) ? { storageState: STATE } : {});
  const page = await ctx.newPage();
  await page.goto('https://chatgpt.com/', { waitUntil: 'domcontentloaded' });
  console.log('If prompted, complete any verification in the browser, then press Enter here.');

  // Quick sanity check: try to reach an authenticated endpoint.
  for (let i = 0; i < 60; i++) {
    const ok = await page.evaluate(async () => {
      try {
        const r = await fetch('/api/auth/session', { credentials: 'include' });
        if (!r.ok) return false;
        const j = await r.json();
        return !!j?.accessToken;
      } catch { return false; }
    });
    if (ok) break;
    await new Promise(r => setTimeout(r, 2000));
  }
  await ctx.storageState({ path: STATE });

  for (let i = 0; i < list.length; i++) {
    const c = list[i];
    const out = path.join(OUT_DIR, `${c.id}.html`);
    if (fs.existsSync(out)) {
      console.log(`[${i+1}/${list.length}] skip (exists): ${c.title}`);
      continue;
    }
    const url = c.url || `https://chatgpt.com/c/${c.id}`;
    console.log(`[${i+1}/${list.length}] ${c.title}`);
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      // Wait for the SSR blob to arrive. Give up to 30s; retry once.
      let html = null;
      for (let t = 0; t < 60; t++) {
        const cand = await page.content();
        if (hasTurboStream(cand)) { html = cand; break; }
        await new Promise(r => setTimeout(r, 500));
      }
      if (!html) {
        console.error(`  no turbo-stream found for ${c.id} — retrying once`);
        await page.reload({ waitUntil: 'domcontentloaded' });
        for (let t = 0; t < 60; t++) {
          const cand = await page.content();
          if (hasTurboStream(cand)) { html = cand; break; }
          await new Promise(r => setTimeout(r, 500));
        }
      }
      if (!html) { console.error(`  FAILED: ${c.id}`); continue; }
      fs.writeFileSync(out, html);
      console.log(`  saved ${out} (${html.length} bytes)`);
    } catch (e) {
      console.error(`  error on ${c.id}:`, e.message);
    }
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('done');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
