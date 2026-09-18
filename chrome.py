"""
Shared "chrome" (font link, style block, header/nav, footer, script) used by
every page on the site. Extracted once from index.html and updated here so
every page (old and new) is generated from the SAME strings — this is the fix
for the earlier bug where shared CSS/nav updates only reached the homepage.
"""
import re

_idx = open('index.html').read()

FONT_LINK = re.search(r'<link rel="stylesheet".*?>\n', _idx).group(0)
STYLE_BLOCK = re.search(r'<style>.*?</style>', _idx, re.DOTALL).group(0)

CLIENT_PORTAL_URL = "https://rosenpsychology.sessionshealth.com"

# Services sub-pages, reused by both the desktop dropdown and the mobile
# nested list below "Services".
SERVICE_LINKS = [
    ("__ADOLESCENT__", "Adolescent Therapy"),
    ("__INDIVIDUAL__", "Individual Adult Therapy"),
    ("__MOTHERHOOD__", "Motherhood"),
    ("__FATHERHOOD__", "Fatherhood"),
    ("__CONSULTATION__", "Consultation"),
    ("__ASSESSMENT__", "Psychological Assessment"),
]
_SERVICE_PANEL_ITEMS = "\n".join(
    f'            <a href="{href}">{label}</a>' for href, label in SERVICE_LINKS
)
_SERVICE_MOBILE_ITEMS = "\n".join(
    f'      <a href="{href}" class="mobile-nav-sub">{label}</a>' for href, label in SERVICE_LINKS
)

NAV_LINKS_DESKTOP = f'''    <nav class="links">
      <a href="__ABOUT__">About</a>
      <span class="nav-dropdown">
        <a href="__SERVICES__">Services</a>
        <div class="nav-dropdown-panel">
          <div class="nav-dropdown-panel-inner">
{_SERVICE_PANEL_ITEMS}
          </div>
        </div>
      </span>
      <a href="__APPROACH__">Approach</a>
      <a href="__START__">Getting Started</a>
      <a href="__CONTACT__">Contact</a>
      <a href="{CLIENT_PORTAL_URL}" target="_blank" rel="noopener">Client Portal</a>
    </nav>'''

NAV_LINKS_MOBILE = f'''    <nav class="wrap mobile-nav-list">
      <a href="__ABOUT__">About</a>
      <a href="__SERVICES__">Services</a>
{_SERVICE_MOBILE_ITEMS}
      <a href="__APPROACH__">Approach</a>
      <a href="__START__">Getting Started</a>
      <a href="__CONTACT__">Contact</a>
      <a href="{CLIENT_PORTAL_URL}" target="_blank" rel="noopener">Client Portal</a>
    </nav>'''

HEADER = f'''<header id="siteHeader">
  <div class="wrap nav">
    <a class="brand" href="__HOME__#top">
      <svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true">
        <circle cx="16" cy="20" r="11" fill="none" stroke="#86813F" stroke-width="1.6"/>
        <circle cx="25" cy="20" r="11" fill="none" stroke="#272F32" stroke-width="1.6"/>
      </svg>
      <span class="brand-text">
        <span class="brand-name">Rosen Psychology</span>
        <span class="brand-sub">Denver, Colorado</span>
      </span>
    </a>
{NAV_LINKS_DESKTOP}
    <div class="nav-cta">
      <a class="btn btn-primary" href="__CONTACT__">Schedule a consultation</a>
      <button type="button" class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mobileNav" aria-label="Open menu">
        <span class="nav-toggle-bars"><span></span><span></span><span></span></span>
      </button>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
{NAV_LINKS_MOBILE}
  </div>
</header>'''

FOOTER = f'''<footer class="on-ink">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <svg width="34" height="34" viewBox="0 0 40 40" aria-hidden="true">
            <circle cx="16" cy="20" r="11" fill="none" stroke="#A9A462" stroke-width="1.6"/>
            <circle cx="25" cy="20" r="11" fill="none" stroke="#F6EFDF" stroke-width="1.6"/>
          </svg>
          <span class="brand-name" style="display:block;margin-top:0.7rem;">Rosen Psychology</span>
          <span class="brand-sub" style="display:block;margin-top:0.2rem;">Dr. Lindsay Rosen, PSY.D</span>
          <p>Psychotherapy for adolescents and adults, and psychological assessment, in Denver, Colorado
            and by telehealth across the country.</p>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <a href="mailto:lindsay@rosenpsych.com" class="mono">lindsay@rosenpsych.com</a>
          <a href="tel:+17202579204" class="mono">+1 720-257-9204</a>
          <address class="mono">1557 N Ogden Street, Suite 11<br>Denver, CO 80218</address>
          <a href="{CLIENT_PORTAL_URL}" target="_blank" rel="noopener" style="margin-top:0.3rem;">Client Portal &rarr;</a>
        </div>
        <div class="footer-col">
          <h4>Site</h4>
          <a href="__ABOUT__">About Dr. Rosen</a>
          <a href="__SERVICES__">Services</a>
          <a href="__ADOLESCENT__">Adolescent Therapy</a>
          <a href="__INDIVIDUAL__">Individual Adult Therapy</a>
          <a href="__CONSULTATION__">Consultation</a>
          <a href="__ASSESSMENT__">Psychological Assessment</a>
          <a href="__APPROACH__">Approach</a>
          <a href="__START__">Getting Started</a>
          <a href="__CONTACT__">Contact</a>
          <a href="__FAQ__">FAQ</a>
        </div>
        <div class="footer-col">
          <h4>Coverage</h4>
          <a href="__HOME__#top">Check telehealth in your state</a>
        </div>
      </div>
      <div class="footer-legal">
        <p class="crisis"><b>Rosen Psychology does not provide emergency or crisis services.</b> If you are
          experiencing a mental health crisis, call or text 988, or visit 988colorado.com. If this is an
          emergency, call 911. You have the right to a Good Faith Estimate of expected charges. Ask any
          provider before scheduling. Learn more at cms.gov/nosurprises.</p>
        <div class="footer-bottom">
          <p class="rights">© 2026 Rosen Psychology · Licensed Clinical Psychologist, Colorado</p>
          <p class="footer-legal-links"><a href="__PRIVACY__">Privacy Policy</a> · <a href="__TERMS__">Terms &amp; Conditions</a></p>
        </div>
      </div>
    </div>
  </footer>'''

SCRIPT = '''<script>
(function(){
  var STATES = [
    ["AL","Alabama"],["AZ","Arizona"],["AR","Arkansas"],["MP","N. Mariana Islands"],
    ["CO","Colorado"],["CT","Connecticut"],["DE","Delaware"],["DC","District of Columbia"],
    ["FL","Florida"],["GA","Georgia"],["ID","Idaho"],["IL","Illinois"],["IN","Indiana"],
    ["KS","Kansas"],["KY","Kentucky"],["ME","Maine"],["MD","Maryland"],["MI","Michigan"],
    ["MN","Minnesota"],["MS","Mississippi"],["MO","Missouri"],["MT","Montana"],["NE","Nebraska"],
    ["NV","Nevada"],["NH","New Hampshire"],["NJ","New Jersey"],["NC","North Carolina"],
    ["ND","North Dakota"],["OH","Ohio"],["OK","Oklahoma"],["PA","Pennsylvania"],["RI","Rhode Island"],
    ["SC","South Carolina"],["SD","South Dakota"],["TN","Tennessee"],["TX","Texas"],["UT","Utah"],
    ["VT","Vermont"],["VA","Virginia"],["WA","Washington"],["WV","West Virginia"],["WI","Wisconsin"],
    ["WY","Wyoming"]
  ];
  var input = document.getElementById('stateInput');
  var box = document.getElementById('stateDropdown');
  if(!input || !box) return;

  var STATE_PAGES = {
    "TX": "__TEXAS_URL__", "AZ": "__STATE_AZ__", "FL": "__STATE_FL__",
    "NC": "__STATE_NC__", "VA": "__STATE_VA__", "WA": "__STATE_WA__"
  };

  function render(raw){
    var q = raw.trim().toLowerCase();
    if(!q){ box.hidden = true; box.innerHTML = ''; return; }
    var matches = STATES.filter(function(s){
      return s[1].toLowerCase().indexOf(q) === 0 || s[0].toLowerCase() === q;
    }).slice(0, 6);
    if(matches.length){
      box.innerHTML = matches.map(function(s){
        var page = STATE_PAGES[s[0]];
        var right = page
          ? '<a class="yes" href="'+page+'">Available ✓</a>'
          : '<span class="yes">Available ✓</span>';
        return '<div><span>'+s[1]+'</span>'+right+'</div>';
      }).join('');
    } else {
      box.innerHTML = '<div class="empty">Not licensed there yet.<br>Denver in-person is always an option.</div>';
    }
    box.hidden = false;
  }

  input.addEventListener('input', function(){ render(input.value); });
  input.addEventListener('focus', function(){ if(input.value) render(input.value); });
  input.addEventListener('blur', function(){ setTimeout(function(){ box.hidden = true; }, 150); });
})();

(function(){
  var header = document.getElementById('siteHeader');
  var toggle = document.getElementById('navToggle');
  var panel = document.getElementById('mobileNav');
  if(!header || !toggle || !panel) return;
  function close(){
    header.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
  }
  function open(){
    header.classList.add('nav-open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close menu');
  }
  toggle.addEventListener('click', function(){
    header.classList.contains('nav-open') ? close() : open();
  });
  panel.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', close);
  });
  window.addEventListener('resize', function(){
    if(window.innerWidth > 880) close();
  });
})();

(function(){
  var form = document.getElementById('contactForm');
  var status = document.getElementById('cfStatus');
  if(!form || !status) return;
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var name = form.name.value.trim();
    var email = form.email.value.trim();
    var phone = form.phone.value.trim();
    var message = form.message.value.trim();
    if(!name || !email || !message){
      status.textContent = 'Please fill in your name, email, and a short message.';
      return;
    }
    var subject = 'New consultation request from ' + name;
    var bodyLines = [
      'Name: ' + name,
      'Email: ' + email,
      'Phone: ' + (phone || 'n/a'),
      '',
      message
    ];
    // PREVIEW BUILD: routed to Chad for review, not Lindsay. Change this address
    // to lindsay@rosenpsych.com before this site actually goes live.
    var mailto = 'mailto:dahc.reverse@gmail.com'
      + '?subject=' + encodeURIComponent(subject)
      + '&body=' + encodeURIComponent(bodyLines.join('\\n'));
    window.location.href = mailto;
    status.textContent = 'Opening your email app to send this message…';
  });
})();
</script>'''


def assemble(title, schema_json, main_html):
    """Build a full source-file string (no doctype/head/body — build.py's
    wrap() adds those) for a brand-new page from shared chrome + page content."""
    parts = [
        f"<title>{title}</title>",
        FONT_LINK.rstrip("\n"),
        STYLE_BLOCK,
        f'<script type="application/ld+json">\n{schema_json.strip()}\n</script>',
        HEADER,
        main_html.strip(),
        FOOTER,
        SCRIPT,
    ]
    return "\n".join(parts) + "\n"
