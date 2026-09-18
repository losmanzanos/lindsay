"""Re-sync the 5 pre-existing source files' header/footer/script to the new
shared chrome.py canonical versions, leaving each file's own <title>, schema,
and main content completely untouched."""
import re
import chrome

FILES = ["index.html", "faq.html", "privacy.html", "terms.html", "texas.html"]

HEADER_RE = re.compile(r'<header id="siteHeader">.*?</header>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer class="on-ink">.*?</footer>', re.DOTALL)
SCRIPT_RE = re.compile(r'<script>\n\(function\(\)\{\n  var STATES.*?</script>', re.DOTALL)
STYLE_RE = re.compile(r'<style>.*?</style>', re.DOTALL)

for fname in FILES:
    raw = open(fname).read()
    n_header = len(HEADER_RE.findall(raw))
    n_footer = len(FOOTER_RE.findall(raw))
    n_script = len(SCRIPT_RE.findall(raw))
    n_style = len(STYLE_RE.findall(raw))
    assert n_header == 1, f"{fname}: expected 1 header, found {n_header}"
    assert n_footer >= 1, f"{fname}: expected >=1 footer, found {n_footer}"
    assert n_script == 1, f"{fname}: expected 1 script block, found {n_script}"
    assert n_style == 1, f"{fname}: expected 1 style block, found {n_style}"

    # Keep every file's own <style> block (colors, layout, new component CSS)
    # in sync with index.html's, which is the single source of truth.
    raw = STYLE_RE.sub(lambda m: chrome.STYLE_BLOCK, raw, count=1)
    raw = HEADER_RE.sub(lambda m: chrome.HEADER, raw, count=1)
    # texas.html has a stray duplicate footer left over from an earlier edit;
    # replace ALL footer occurrences with the single canonical one, then we'll
    # dedupe duplicates below.
    footers_found = FOOTER_RE.findall(raw)
    raw = FOOTER_RE.sub(lambda m: "@@FOOTER@@", raw)
    # collapse consecutive duplicate footer markers into one
    raw = re.sub(r'(@@FOOTER@@\s*){2,}', '@@FOOTER@@', raw)
    raw = raw.replace("@@FOOTER@@", chrome.FOOTER)
    raw = SCRIPT_RE.sub(lambda m: chrome.SCRIPT, raw, count=1)

    with open(fname, "w") as f:
        f.write(raw)
    print(fname, "-> header/footer/script synced", f"(collapsed {len(footers_found)} footer block(s))")
