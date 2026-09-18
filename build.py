import re, os, shutil

# Flip to False once Lindsay has approved + the site is actually going live at
# rosenpsych.com. While True: every page keeps <meta robots noindex,nofollow>,
# robots.txt disallows everything, and no sitemap is written into site/.
PREVIEW_MODE = True

# ---------------------------------------------------------------------------
# PAGES: every page on the site, as (id, src file, out path relative to a
# build root, <title>, meta description, canonical path from the domain root).
# id is what "__TOKEN__" placeholders in source files resolve through — see
# TOKEN_FOR_ID below.
# ---------------------------------------------------------------------------
PAGES = [
    ("home",         "index.html",                  "index.html",                            "Rosen Psychology | Licensed Clinical Psychologist, Denver, CO",
     "Dr. Lindsay Rosen, PsyD, is a licensed clinical psychologist in Denver, CO providing evidence-based therapy for adolescents and adults, in person and by telehealth in 40+ states.",
     "/"),
    ("about",        "about.html",                  "about/index.html",                      "About Dr. Rosen | Rosen Psychology",
     "Meet Dr. Lindsay Rosen, PsyD: a licensed clinical psychologist in Denver, CO with doctoral training from the University of Denver and a caseload spanning teenagers to executives.",
     "/about/"),
    ("services",     "services.html",               "services/index.html",                   "Services | Rosen Psychology",
     "Adolescent therapy, individual adult therapy, motherhood and fatherhood support, consultation, and psychological assessment with Dr. Lindsay Rosen in Denver, CO.",
     "/services/"),
    ("approach",     "approach.html",                "approach/index.html",                   "Approach | Rosen Psychology",
     "How Dr. Lindsay Rosen works with clients: a relationship-first, evidence-based approach to therapy in Denver, CO.",
     "/approach/"),
    ("adolescent",   "services-adolescent.html",    "services/adolescent-therapy/index.html","Adolescent Therapy in Denver, CO | Rosen Psychology",
     "Therapy for teens ages 13-17 with Dr. Lindsay Rosen, a licensed clinical psychologist in Denver, CO, in person and by telehealth.",
     "/services/adolescent-therapy/"),
    ("individual",   "services-individual.html",    "services/individual-therapy/index.html","Individual Adult Therapy in Denver, CO | Rosen Psychology",
     "Evidence-based individual therapy for adults 18+ with Dr. Lindsay Rosen, a licensed clinical psychologist in Denver, CO.",
     "/services/individual-therapy/"),
    ("motherhood",   "services-motherhood.html",    "services/motherhood/index.html",        "Therapy for New & Expecting Mothers | Rosen Psychology",
     "Support for pregnancy, postpartum, and the transition to motherhood with Dr. Lindsay Rosen, a licensed clinical psychologist in Denver, CO.",
     "/services/motherhood/"),
    ("fatherhood",   "services-fatherhood.html",    "services/fatherhood/index.html",        "Therapy for New Fathers | Rosen Psychology",
     "Support for new and expecting fathers navigating identity, relationships, and the transition to fatherhood with Dr. Lindsay Rosen in Denver, CO.",
     "/services/fatherhood/"),
    ("consultation", "services-consultation.html", "services/consultation/index.html",       "Psychological Consultation | Rosen Psychology",
     "Consultation for individuals, parents, and organizations from Dr. Lindsay Rosen, PsyD, a licensed clinical psychologist in Denver, CO.",
     "/services/consultation/"),
    ("assessment",   "services-assessment.html",    "services/psychological-assessment/index.html","Psychological Assessment | Rosen Psychology",
     "Psychological assessment services from Dr. Lindsay Rosen, PsyD, launching January 2027 in Denver, CO.",
     "/services/psychological-assessment/"),
    ("start",        "getting-started.html",        "getting-started/index.html",            "Getting Started | Rosen Psychology",
     "What to expect from your first consultation call through your first session with Dr. Lindsay Rosen in Denver, CO.",
     "/getting-started/"),
    ("contact",      "contact.html",                "contact/index.html",                    "Contact | Rosen Psychology",
     "Reach Dr. Lindsay Rosen's Denver, CO practice by phone, email, or the contact form to schedule a free consultation.",
     "/contact/"),
    ("faq",          "faq.html",                    "faq/index.html",                        "FAQ | Rosen Psychology",
     "Fees, insurance, telehealth availability, and what to expect from your first sessions with Dr. Lindsay Rosen.",
     "/faq/"),
    ("privacy",      "privacy.html",                "privacy/index.html",                    "Privacy Policy | Rosen Psychology",
     "Rosen Psychology's website privacy practices.",
     "/privacy/"),
    ("terms",        "terms.html",                  "terms/index.html",                      "Terms & Conditions | Rosen Psychology",
     "Rosen Psychology's website terms and conditions.",
     "/terms/"),
    ("state-tx",     "texas.html",                  "telehealth/texas/index.html",           "Telehealth in Texas | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout Texas.",
     "/telehealth/texas/"),
    ("state-az",     "state-arizona.html",          "telehealth/arizona/index.html",         "Telehealth in Arizona | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout Arizona.",
     "/telehealth/arizona/"),
    ("state-fl",     "state-florida.html",          "telehealth/florida/index.html",         "Telehealth in Florida | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout Florida.",
     "/telehealth/florida/"),
    ("state-nc",     "state-north-carolina.html",   "telehealth/north-carolina/index.html",  "Telehealth in North Carolina | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout North Carolina.",
     "/telehealth/north-carolina/"),
    ("state-va",     "state-virginia.html",         "telehealth/virginia/index.html",        "Telehealth in Virginia | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout Virginia.",
     "/telehealth/virginia/"),
    ("state-wa",     "state-washington.html",       "telehealth/washington/index.html",      "Telehealth in Washington | Rosen Psychology",
     "Dr. Lindsay Rosen offers licensed telehealth psychotherapy to adults and adolescents throughout Washington State.",
     "/telehealth/washington/"),
]

# Legacy flat tokens used throughout the existing source files, still supported.
LEGACY_TOKEN_TO_ID = {
    "__HOME__": "home", "__FAQ__": "faq", "__PRIVACY__": "privacy",
    "__TERMS__": "terms", "__TEXAS_URL__": "state-tx",
}
# New tokens for the pages added in this round.
NEW_TOKEN_TO_ID = {
    "__ABOUT__": "about", "__SERVICES__": "services", "__APPROACH__": "approach",
    "__ADOLESCENT__": "adolescent", "__INDIVIDUAL__": "individual",
    "__MOTHERHOOD__": "motherhood", "__FATHERHOOD__": "fatherhood", "__CONSULTATION__": "consultation",
    "__ASSESSMENT__": "assessment", "__START__": "start", "__CONTACT__": "contact",
    "__STATE_AZ__": "state-az", "__STATE_FL__": "state-fl", "__STATE_NC__": "state-nc",
    "__STATE_VA__": "state-va", "__STATE_WA__": "state-wa",
}
ALL_TOKENS = {**LEGACY_TOKEN_TO_ID, **NEW_TOKEN_TO_ID}

ID_TO_CANONICAL = {p[0]: p[5] for p in PAGES}
ID_TO_TITLE = {p[0]: p[3] for p in PAGES}
ID_TO_DESC = {p[0]: p[4] for p in PAGES}


def wrap(content, canonical, description, img_root=""):
    robots = "noindex, nofollow" if PREVIEW_MODE else "index, follow"
    head = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="robots" content="{robots}">\n'
        f'<meta name="description" content="{description}">\n'
        f'<link rel="canonical" href="{canonical}">\n'
        f'<link rel="icon" type="image/svg+xml" href="{img_root}/images/favicon.svg">\n'
        f'<link rel="icon" type="image/png" sizes="32x32" href="{img_root}/images/favicon-32.png">\n'
        f'<link rel="icon" type="image/png" sizes="16x16" href="{img_root}/images/favicon-16.png">\n'
        f'<link rel="apple-touch-icon" href="{img_root}/images/apple-touch-icon.png">\n'
    )
    content = re.sub(r'(</style>)', r'\1\n</head>\n<body>', content, count=1)
    return head + content + '\n</body>\n</html>\n'


def resolve_tokens(raw, current_id, url_for, img_root=""):
    """url_for(id) -> resolved href for this build target. Home gets '' when
    current_id == 'home' so in-page anchors like '#contact' keep working.
    img_root prefixes root-relative "/images/..." asset paths so they still
    resolve correctly on a subpath target like GitHub Pages' /lindsay/."""
    for token, pid in ALL_TOKENS.items():
        val = "" if (pid == "home" and current_id == "home") else url_for(pid)
        raw = raw.replace(token, val)
    raw = raw.replace('src="/images/', f'src="{img_root}/images/')
    return raw


def build_target(out_dir, url_for, extra_files=None, write_sitemap=False, domain="", img_root=""):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    for pid, src, out_rel, title, desc, canonical_path in PAGES:
        with open(src) as f:
            raw = f.read()
        raw = resolve_tokens(raw, pid, url_for, img_root=img_root)
        canonical_full = domain + canonical_path if domain else url_for(pid)
        out_full = os.path.join(out_dir, out_rel)
        os.makedirs(os.path.dirname(out_full), exist_ok=True)
        with open(out_full, "w") as f:
            f.write(wrap(raw, canonical_full, desc, img_root=img_root))
    if extra_files:
        for name, content in extra_files.items():
            with open(os.path.join(out_dir, name), "w") as f:
                f.write(content)
    if os.path.isdir("images"):
        shutil.copytree("images", os.path.join(out_dir, "images"), dirs_exist_ok=True)
    if write_sitemap:
        urls = "\n".join(
            f"  <url><loc>{domain}{canonical_path}</loc></url>"
            for _, _, _, _, _, canonical_path in PAGES
        )
        sitemap = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )
        with open(os.path.join(out_dir, "sitemap.xml"), "w") as f:
            f.write(sitemap)
        robots_txt = (
            "User-agent: *\nDisallow: /\n" if PREVIEW_MODE else
            f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml\n"
        )
        with open(os.path.join(out_dir, "robots.txt"), "w") as f:
            f.write(robots_txt)


# ---- real domain root (site/) ----
def site_url_for(pid):
    return ID_TO_CANONICAL[pid]
build_target(
    "site", site_url_for,
    extra_files={"CNAME": "rosenpsych.com\n", ".nojekyll": ""},
    write_sitemap=True, domain="https://rosenpsych.com",
)

# ---- GitHub Pages /lindsay/ subpath (site-ghpages/) ----
def ghpages_url_for(pid):
    return "/lindsay" + ID_TO_CANONICAL[pid]
build_target("site-ghpages", ghpages_url_for, extra_files={".nojekyll": ""}, img_root="/lindsay")

print("site/ and site-ghpages/ rebuilt:", len(PAGES), "pages")

# ---- standalone review files (only the original 5, for quick email/download review) ----
STANDALONE = {
    "index.html":  "rosen-psychology-homepage.html",
    "faq.html":    "rosen-psychology-faq.html",
    "privacy.html":"rosen-psychology-privacy-policy.html",
    "terms.html":  "rosen-psychology-terms.html",
    "texas.html":  "rosen-psychology-telehealth-texas-sample.html",
}
SRC_TO_ID = {p[1]: p[0] for p in PAGES}
def standalone_url_for(pid):
    for src, out_name in STANDALONE.items():
        if SRC_TO_ID[src] == pid:
            return out_name
    # Pages not in the standalone set (about/services/etc.) fall back to the
    # real site path, since these review files aren't the primary delivery
    # mechanism anymore.
    return ID_TO_CANONICAL[pid]

for src, out_name in STANDALONE.items():
    pid = SRC_TO_ID[src]
    with open(src) as f:
        raw = f.read()
    raw = resolve_tokens(raw, pid, standalone_url_for)
    with open(out_name, "w") as f:
        f.write(wrap(raw, ID_TO_CANONICAL[pid], ID_TO_DESC[pid]))

print("standalone files rebuilt:", len(STANDALONE))
