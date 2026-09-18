import threading, http.server, time, sys
from playwright.sync_api import sync_playwright

ROOT = "/tmp/pw-preview-root"
PORT = 8123

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=srv.serve_forever, daemon=True)
t.start()
time.sleep(0.3)

PAGES = [
    "/lindsay/", "/lindsay/about/", "/lindsay/services/", "/lindsay/approach/",
    "/lindsay/services/adolescent-therapy/",
    "/lindsay/services/individual-therapy/", "/lindsay/services/motherhood/",
    "/lindsay/services/fatherhood/", "/lindsay/services/consultation/",
    "/lindsay/services/psychological-assessment/", "/lindsay/getting-started/",
    "/lindsay/contact/", "/lindsay/faq/", "/lindsay/privacy/", "/lindsay/terms/",
    "/lindsay/telehealth/texas/", "/lindsay/telehealth/arizona/",
    "/lindsay/telehealth/florida/", "/lindsay/telehealth/north-carolina/",
    "/lindsay/telehealth/virginia/", "/lindsay/telehealth/washington/",
]
SIZES = [(1440, 900), (390, 844), (320, 568)]

errors = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    context = browser.new_context()
    context.route("**/fonts.googleapis.com/**", lambda route: route.abort())
    context.route("**/fonts.gstatic.com/**", lambda route: route.abort())
    page = context.new_page()

    for path in PAGES:
        for w, h in SIZES:
            page.set_viewport_size({"width": w, "height": h})
            resp = page.goto(f"http://127.0.0.1:{PORT}{path}", wait_until="domcontentloaded", timeout=15000)
            if resp is None or resp.status >= 400:
                errors.append(f"{path} @ {w}x{h}: HTTP {resp.status if resp else 'no response'}")
                continue
            page.wait_for_timeout(150)
            overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if overflow > 0:
                # find offenders
                offenders = page.evaluate("""
                    () => {
                      const vw = document.documentElement.clientWidth;
                      const out = [];
                      document.querySelectorAll('*').forEach(el => {
                        const r = el.getBoundingClientRect();
                        if (r.right > vw + 1) out.push(el.tagName + '.' + (el.className+'').split(' ').join('.'));
                      });
                      return out.slice(0,5);
                    }
                """)
                errors.append(f"{path} @ {w}x{h}: overflow {overflow}px, offenders: {offenders}")
            # check broken internal images
            broken_imgs = page.evaluate("""
                () => Array.from(document.querySelectorAll('img')).filter(i => i.complete && i.naturalWidth === 0).map(i => i.src)
            """)
            if broken_imgs:
                errors.append(f"{path} @ {w}x{h}: broken images {broken_imgs}")

    browser.close()

srv.shutdown()

print(f"Checked {len(PAGES)} pages x {len(SIZES)} sizes = {len(PAGES)*len(SIZES)} checks")
if errors:
    print(f"\n{len(errors)} ISSUE(S):")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("All clear: no HTTP errors, no horizontal overflow, no broken images.")
