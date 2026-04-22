// Download the full conversation JSON for each chat listed in chats_to_fetch.json
// by calling `/backend-api/conversation/<id>` from inside the logged-in browser
// context (same mechanism fetch_index.js uses for `/backend-api/conversations`).
//
// The chat page itself (chatgpt.com/c/<id>) for logged-in sessions renders
// client-side and does NOT include the turbo-stream SSR blob that share pages
// do, so HTML capture doesn't work — but the backend-api endpoint does, when
// called from a page already on chatgpt.com with valid cookies.
//
// Output: one .json file per chat under `out/` (default `./html/<id>.json`).
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
const CDP_URL = process.env.CHROME_CDP_URL || null;
const USER_DATA_DIR = process.env.CHROME_USER_DATA_DIR || null;
const PROFILE = process.env.CHROME_PROFILE || 'Default';

(async () => {
  if (!fs.existsSync(LIST)) { console.error('missing', LIST); process.exit(1); }
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const list = JSON.parse(fs.readFileSync(LIST, 'utf-8'));

  let browser = null;
  let ctx;
  if (CDP_URL) {
    console.log(`Connecting over CDP: ${CDP_URL}`);
    browser = await chromium.connectOverCDP(CDP_URL);
    ctx = browser.contexts()[0] || await browser.newContext();
  } else if (USER_DATA_DIR) {
    console.log(`Using real Chrome profile: ${USER_DATA_DIR} (profile: ${PROFILE})`);
    ctx = await chromium.launchPersistentContext(USER_DATA_DIR, {
      channel: 'chrome',
      headless: false,
      args: [`--profile-directory=${PROFILE}`],
      viewport: null,
    });
  } else {
    browser = await chromium.launch(Object.assign(
      { headless: false },
      EXE ? { executablePath: EXE } : {}
    ));
    ctx = await browser.newContext(fs.existsSync(STATE) ? { storageState: STATE } : {});
  }
  let page = ctx.pages().find(p => /chatgpt\.com|openai\.com/.test(p.url())) || ctx.pages()[0] || await ctx.newPage();
  if (!/chatgpt\.com/.test(page.url())) {
    await page.goto('https://chatgpt.com/', { waitUntil: 'domcontentloaded' });
  }
  console.log('If prompted, complete any verification in the browser, then press Enter here.');

  // Need an accessToken for the backend-api Bearer header.
  let token = null;
  for (let i = 0; i < 60; i++) {
    const r = await page.evaluate(async () => {
      try {
        const s = await fetch('/api/auth/session', { credentials: 'include' });
        if (!s.ok) return { ok: false, status: s.status };
        const j = await s.json();
        return { ok: true, accessToken: j?.accessToken || null };
      } catch (e) { return { ok: false, err: String(e) }; }
    });
    if (r.ok && r.accessToken) { token = r.accessToken; break; }
    await new Promise(r => setTimeout(r, 2000));
  }
  if (!token) { console.error('no accessToken'); process.exit(1); }
  if (!USER_DATA_DIR && !CDP_URL) await ctx.storageState({ path: STATE });

  for (let i = 0; i < list.length; i++) {
    const c = list[i];
    const out = path.join(OUT_DIR, `${c.id}.json`);
    if (fs.existsSync(out)) {
      console.log(`[${i+1}/${list.length}] skip (exists): ${c.title}`);
      continue;
    }
    console.log(`[${i+1}/${list.length}] ${c.title}`);
    try {
      const res = await page.evaluate(async ({ id, token }) => {
        const r = await fetch(`/backend-api/conversation/${id}`, {
          credentials: 'include',
          headers: { 'Authorization': 'Bearer ' + token, 'Accept': 'application/json' }
        });
        const body = await r.text();
        return { ok: r.ok, status: r.status, body };
      }, { id: c.id, token });
      if (!res.ok) {
        console.error(`  FAILED ${c.id}: HTTP ${res.status}`);
        // Don't save — leave it missing so a retry picks it up.
        continue;
      }
      // Sanity: parse to make sure it's valid JSON with a `mapping` field.
      let obj;
      try { obj = JSON.parse(res.body); } catch (e) {
        console.error(`  FAILED ${c.id}: non-JSON response (first 120 ch): ${res.body.slice(0,120)}`);
        continue;
      }
      if (!obj || typeof obj !== 'object' || !obj.mapping) {
        console.error(`  FAILED ${c.id}: missing 'mapping' in response`);
        continue;
      }
      fs.writeFileSync(out, res.body);
      console.log(`  saved ${out} (${res.body.length} bytes)`);
    } catch (e) {
      console.error(`  error on ${c.id}:`, e.message);
    }
    await new Promise(r => setTimeout(r, 300));
  }
  console.log('done');
  if (CDP_URL) { process.exit(0); }
  if (browser) await browser.close(); else await ctx.close();
})().catch(e => { console.error(e); process.exit(1); });
