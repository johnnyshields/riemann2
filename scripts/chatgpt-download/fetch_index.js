// Open a headed Chromium, wait for login, and enumerate conversations from the
// /backend-api/conversations list endpoint (which is reachable with the Bearer
// token from /api/auth/session and does NOT hit the same CF challenge that the
// per-conversation endpoint does).
//
// Output: recent.json — array of conversation summaries {id, title,
// create_time, update_time, ...}, ordered by update_time descending.
//
// Stops early once crossing the date cutoff (default 14 days).
//
// Usage:
//   node fetch_index.js [--days 14] [--all] [--state state.json] [--out recent.json]

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

const DAYS = args.days ? parseInt(args.days) : 14;
const FETCH_ALL = !!args.all;
const STATE = args.state || path.join(__dirname, 'state.json');
const OUT = args.out || path.join(__dirname, 'recent.json');

// On WSL, use the installed Playwright chromium directly.
// On Windows, omit executablePath to use Playwright's bundled chromium, or
// point at your Chrome install.
const EXE = process.env.CHROME_PATH || null;

// Attach modes:
//   1. CDP attach (preferred when user launched Chrome with
//      --remote-debugging-port=9222 --user-data-dir="<non-default-path>").
//      Set CHROME_CDP_URL=http://localhost:9222 to use.
//   2. launchPersistentContext against CHROME_USER_DATA_DIR (requires Chrome
//      fully closed beforehand). Less reliable on real profiles.
//   3. Plain chromium.launch (Playwright's bundled browser) — default.
const CDP_URL = process.env.CHROME_CDP_URL || null;
const USER_DATA_DIR = process.env.CHROME_USER_DATA_DIR || null;
const PROFILE = process.env.CHROME_PROFILE || 'Default';

(async () => {
  const useState = fs.existsSync(STATE);
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
    ctx = await browser.newContext(useState ? { storageState: STATE } : {});
  }
  // Prefer an existing chatgpt.com tab if one is already open (CDP attach).
  let page = ctx.pages().find(p => /chatgpt\.com|openai\.com/.test(p.url())) || ctx.pages()[0] || await ctx.newPage();
  if (!/chatgpt\.com/.test(page.url())) {
    await page.goto('https://chatgpt.com/', { waitUntil: 'domcontentloaded' });
  }

  console.log('Browser launched. Complete any login / CF challenges in the window.');

  let token = null;
  for (let i = 0; i < 180; i++) {
    const r = await page.evaluate(async () => {
      try {
        const s = await fetch('/api/auth/session', { credentials: 'include' });
        if (!s.ok) return { ok: false, status: s.status };
        const j = await s.json();
        return { ok: true, accessToken: j?.accessToken || null, user: j?.user?.email || null };
      } catch (e) { return { ok: false, err: String(e) }; }
    });
    if (r.ok && r.accessToken) {
      const probe = await page.evaluate(async (tok) => {
        const r = await fetch('/backend-api/conversations?offset=0&limit=1&order=updated', {
          credentials: 'include',
          headers: { 'Authorization': 'Bearer ' + tok }
        });
        return { ok: r.ok, status: r.status };
      }, r.accessToken);
      if (probe.ok) { token = r.accessToken; console.log('Logged in as:', r.user || '(unknown)'); break; }
    }
    await new Promise(r => setTimeout(r, 2000));
  }
  if (!token) {
    console.error('Timed out waiting for login.');
    if (!CDP_URL) { if (browser) await browser.close(); else await ctx.close(); }
    process.exit(1);
  }
  if (!USER_DATA_DIR && !CDP_URL) await ctx.storageState({ path: STATE });

  const cutoff = FETCH_ALL ? 0 : (Date.now() / 1000 - DAYS * 86400);
  const kept = [];
  let offset = 0;
  const pageSize = 100;
  let done = false;
  while (!done) {
    const res = await page.evaluate(async ({ offset, pageSize, token }) => {
      const r = await fetch(`/backend-api/conversations?offset=${offset}&limit=${pageSize}&order=updated`, {
        credentials: 'include',
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (!r.ok) return { ok: false, status: r.status };
      return { ok: true, body: await r.json() };
    }, { offset, pageSize, token });
    if (!res.ok) { console.error('fetch failed', res.status); break; }
    const items = res.body.items || [];
    if (items.length === 0) break;
    for (const c of items) {
      // Times are ISO strings on this endpoint; convert to epoch for comparison.
      const tsStr = c.update_time || c.create_time;
      const ts = tsStr ? (Date.parse(tsStr) / 1000) : 0;
      if (!FETCH_ALL && ts < cutoff) { done = true; break; }
      kept.push(c);
    }
    offset += items.length;
    process.stdout.write(`  scanned ${offset}, kept ${kept.length}\r`);
    if (items.length < pageSize) break;
    await new Promise(r => setTimeout(r, 100));
  }
  console.log();
  fs.writeFileSync(OUT, JSON.stringify(kept, null, 2));
  console.log(`Wrote ${kept.length} to ${OUT}`);
  console.log('Leave the browser open if you plan to run fetch_pages.js next.');
  if (CDP_URL) { process.exit(0); }
  // Do NOT close — next script reuses the same browser session.
  await new Promise(() => {});
})().catch(e => { console.error(e); process.exit(1); });
