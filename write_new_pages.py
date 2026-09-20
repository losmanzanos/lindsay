# -*- coding: utf-8 -*-
import chrome

PSYCHOLOGIST_BASE = {
    "@context": "https://schema.org",
    "@type": "Psychologist",
    "name": "Dr. Lindsay Rosen, PsyD",
    "telephone": "+1-720-257-9204",
    "email": "lindsay@rosenpsych.com",
    "medicalSpecialty": "Psychiatric",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "1557 N Ogden Street, Suite 11",
        "addressLocality": "Denver",
        "addressRegion": "CO",
        "postalCode": "80218",
        "addressCountry": "US"
    },
}

import json

def schema(url, available_service, area_served=None):
    d = dict(PSYCHOLOGIST_BASE)
    d["url"] = url
    d["availableService"] = available_service
    if area_served:
        d["areaServed"] = area_served
    return json.dumps(d, indent=2)

ADOLESCENT_SVC = [{"@type": "MedicalTherapy", "name": "Adolescent Therapy"}]
INDIVIDUAL_SVC = [{"@type": "MedicalTherapy", "name": "Individual Therapy"}]
ASSESSMENT_SVC = [{"@type": "MedicalTherapy", "name": "Psychological Assessment"}]
BOTH_THERAPY_SVC = [{"@type": "MedicalTherapy", "name": "Adolescent Therapy"},
                     {"@type": "MedicalTherapy", "name": "Individual Therapy"}]
ALL_SVC = [{"@type": "MedicalTherapy", "name": "Adolescent Therapy"},
           {"@type": "MedicalTherapy", "name": "Individual Therapy"},
           {"@type": "MedicalTherapy", "name": "Psychological Assessment"}]

PAGES_TO_WRITE = []

# =====================================================================
# ABOUT
# =====================================================================
about_main = '''<main id="top">
  <section class="on-paper band-tight">
    <div class="wrap about-grid">
      <div>
        <div class="headshot-wrap">
          <img src="/images/lindsay-headshot.jpg" alt="Dr. Lindsay Rosen, licensed clinical psychologist, in her Denver office" loading="lazy">
        </div>
        <p class="eyebrow">About Dr. Rosen</p>
        <h2 style="margin-top:1rem;">Training that runs deep.<br>A bedside manner that doesn't feel like one.</h2>
      </div>
      <div class="about-body">
        <p>Dr. Lindsay Rosen is a licensed clinical psychologist who provides psychotherapy to adolescents
          and adults and comprehensive psychological assessment across the lifespan. Her training spans
          schools, hospitals, community mental health centers, and private practice. That range gives her a
          nuanced read on the many factors that shape how a person thinks, feels, relates, and moves through
          the world.</p>
        <p>She has particular expertise in the periods when people are figuring out who they are and how
          they want to live: adolescents and young adults navigating identity and independence, and adults
          adapting to changes in relationships, roles, or sense of self.</p>
        <p>Her caseload runs a wide spectrum by design: high school students working through identity,
          confidence, and complicated peer relationships; and high-functioning professionals and executives
          who look fine on paper but are quietly stretched thin. What connects them is the same approach:
          evidence-based, relational, and responsive to how each person actually thinks, copes, and relates.</p>
        <p>In session, Dr. Rosen helps clients explore the emotional and relational patterns underneath
          their day-to-day struggles, deepen self-awareness, and build practical, evidence-based skills
          alongside a genuine, trusting relationship. Her approach is warm, straightforward, and grounded,
          making room to work on both present-day challenges and their deeper roots, aimed at real clarity
          rather than quick fixes.</p>

        <div class="cred-groups">
          <details open>
            <summary>Education</summary>
            <div class="cred-list">
              <div>PsyD, Clinical Psychology (APA-Accredited) &middot; University of Denver, Denver, CO</div>
              <div>M.A., Applied Child Development and Human Study &middot; Tufts University, Medford, MA</div>
              <div>B.A., Psychology, Phi Beta Kappa, Magna Cum Laude &middot; University of Miami, Coral Gables, FL</div>
            </div>
          </details>
          <details>
            <summary>Internship &amp; Postdoctoral Training</summary>
            <div class="cred-list">
              <div>Postdoctoral Fellowship &middot; Birch Psychology, Denver, CO</div>
              <div>Clinical Psychology Internship &middot; Community Reach Center (CRC), Denver, CO</div>
            </div>
          </details>
          <details>
            <summary>Additional Training</summary>
            <div class="cred-list">
              <div>Mental Health Center of Denver &middot; Adult Psychological Assessment, Denver, CO</div>
              <div>Caring for You and Baby Clinic (CUB Clinic) &middot; University of Denver Graduate School of Professional Psychology, Denver, CO</div>
              <div>National Jewish Health &middot; Pediatric Behavioral Health Neuropsychology, Denver, CO</div>
              <div>CRC In-Home Resiliency and Support Services Team, Denver, CO</div>
              <div>CRC School-Based Therapy Program, Denver, CO</div>
              <div>NeuroWorks Neuropsychological Assessment Private Practice, Boulder, CO</div>
              <div>Growing Minds Psychological Assessment Practice, Lexington, MA</div>
              <div>Boston Medical Center &middot; Developmental and Behavioral Pediatrics, Boston, MA</div>
              <div>Harvard University &middot; Social Neuroscience and Psychopathology Lab</div>
            </div>
          </details>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap">
      <p class="eyebrow">The office</p>
      <h2 style="margin-top:1rem;font-size:clamp(1.5rem,2.4vw,2rem);max-width:24ch;">In person, at 1557 N Ogden Street, Denver.</h2>
      <div class="photo-grid">
        <div class="wide"><img src="/images/office-wide.jpg" alt="Living-room style therapy office with couch, reading chair, and antique fireplace" loading="lazy"></div>
        <div><img src="/images/office-mantel.jpg" alt="Antique fireplace mantel with plants" loading="lazy"></div>
        <div><img src="/images/office-couch.jpg" alt="Couch with pillows and reading lamp in the therapy office" loading="lazy"></div>
        <div><img src="/images/office-bookshelf.jpg" alt="Antique painted bookshelf with books and decor" loading="lazy"></div>
        <div><img src="/images/office-diplomas.jpg" alt="Desk with framed diplomas from University of Denver, Tufts, and University of Miami" loading="lazy"></div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">See how she works with clients.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Read about her approach, or explore
          adolescent and individual therapy directly.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "about.html", "About Dr. Rosen | Rosen Psychology",
    schema("https://rosenpsych.com/about/", ALL_SVC), about_main
))

# =====================================================================
# SERVICES: ADOLESCENT THERAPY
# =====================================================================
adolescent_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__SERVICES__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; All services</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Adolescent Therapy &middot; Ages 13&ndash;17</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:19ch;margin-top:1rem;">A space that's <em>theirs</em>,<br>not a parent's, teacher's, or peer's.</h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:60ch;">Adolescence is a period of enormous growth and change, unfolding in an especially demanding
        world of constant connection, comparison, and pressure. Teens benefit from having a trusted,
        approachable adult who is not a parent, teacher, coach, or friend: someone who can help them put
        words to the good, the bad, the confusing, and the overwhelming parts of what they are experiencing,
        without judgment or pressure to have it all figured out.</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Schedule a free consultation</a>
        <a class="btn btn-ghost" href="__START__">How sessions work</a>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">Who this is for</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:15ch;">Teens figuring out who they are, for the first time.</h2>
      </div>
      <div class="about-body">
        <p>Adolescence is often the first time a person has to actively construct an identity rather than
          just have one handed to them. Dr. Rosen creates a space where teens can feel understood, make
          sense of what is happening beneath the surface, and build the insight and practical skills to
          navigate difficult emotions, relationships, and everyday challenges with greater confidence and
          flexibility.</p>
        <p>Dr. Rosen may be a good fit for teens struggling with:</p>
        <ul class="check-list">
          <li>School stress, perfectionism, and procrastination</li>
          <li>Friendship changes, social pressure, and feeling left out</li>
          <li>Overthinking texts, relationships, and what others think</li>
          <li>Social media, dating, crushes, and first relationships</li>
          <li>Self-esteem, body image, and comparison</li>
          <li>Big emotions, irritability, and feeling overwhelmed</li>
          <li>Family conflict, boundaries, and growing independence</li>
          <li>Feeling unmotivated, checked out, or unlike themselves</li>
          <li>Major changes, loss, and difficult transitions</li>
          <li>Stress about college, the future, and what comes next</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">What therapy looks like</h2>
        <p>The practical shape of the work, so nothing feels like a surprise.</p>
      </div>
      <div class="about-body" style="max-width:74ch;">
        <p>Therapy gives teens a place to slow things down and get curious about what is happening beneath
          the surface. Thoughts and feelings that are difficult to understand or put into words often show
          up in other ways: shutting down, avoiding, arguing, overthinking, procrastinating, or reacting
          more intensely than intended. Dr. Rosen helps teens make connections between what they are
          feeling, how they are thinking, and what they do next.</p>
        <p>The goal is not to eliminate difficult emotions or expect teens to always respond perfectly. It
          is to help them better understand themselves, tolerate discomfort, recognize patterns, and have
          more flexibility and choice in how they respond.</p>
        <p>Dr. Rosen prioritizes building a genuine relationship with each teen and getting to know them as
          a whole person, approaching their experiences with curiosity rather than judgment. She integrates
          relational and insight-oriented therapy with evidence-based strategies from cognitive behavioral
          therapy (CBT), mindfulness, and other skills-based approaches, so teens leave not only knowing
          themselves better, but feeling more capable of navigating what happens outside the therapy room.</p>
      </div>
      <div class="service-list" style="margin-top:2.4rem;">
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Format &amp; length</h3>
          <span class="service-tag">LOGISTICS</span>
          <p>50-minute sessions, typically weekly, in person at the Denver office or by telehealth
            anywhere Dr. Rosen is licensed. Consistency matters most in the early stages of building trust.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Privacy, in age-appropriate terms</h3>
          <span class="service-tag">CONFIDENTIALITY</span>
          <p>Teens need a space that feels genuinely private. What stays between the two of them and what's
            shared with a parent or guardian is discussed openly at intake, calibrated to the teen's age and
            the family's situation, not a blanket policy applied the same way to a 13-year-old and a 17-year-old.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">Where parents fit</h2>
      </div>
      <div class="about-body" style="max-width:74ch;">
        <p>Parents remain an important part of adolescence, even as teens naturally begin to rely on them
          differently. Developing independence, identity, and self-trust often means creating more space
          from parents and turning increasingly toward peers and the world outside the family.</p>
        <p>Therapy gives teens another trusted adult relationship where they can develop their own voice,
          think through decisions, and practice understanding and trusting themselves. At the same time,
          healthy independence does not develop in isolation. When appropriate, Dr. Rosen collaborates with
          parents to better understand what may be happening beneath a teen's behavior, strengthen
          communication, reduce unproductive cycles of conflict, and find a balance between staying
          connected and making room for independence.</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">Let's see if it's a good fit.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">A free 15-minute call, for you or
          your teen, before committing to anything.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-adolescent.html", "Adolescent Therapy in Denver, CO | Rosen Psychology",
    schema("https://rosenpsych.com/services/adolescent-therapy/", ADOLESCENT_SVC), adolescent_main
))

# =====================================================================
# SERVICES: INDIVIDUAL THERAPY
# =====================================================================
individual_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__SERVICES__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; All services</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Individual Adult Therapy &middot; Ages 18+</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:20ch;margin-top:1rem;">For the parts of life<br><em>that don't fit a checklist.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;">Many of the people Dr. Rosen works with are high-functioning on the outside but feel
        overwhelmed, stuck, or disconnected internally. Individual therapy for adults, grounded in
        understanding your history, not just your symptoms.</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Schedule a free consultation</a>
        <a class="btn btn-ghost" href="__START__">How sessions work</a>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">Areas of focus</h2>
        <p>Different presentations, same underlying approach.</p>
      </div>
      <div class="service-list">
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Anxiety, depression &amp; burnout</h3>
          <span class="service-tag">EVERYDAY</span>
          <p>Anxiety, professional stress and burnout, depression and low mood, and trauma or posttraumatic
            stress, for people who often look composed from the outside and are quietly running on empty.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Life transitions &amp; uncertainty</h3>
          <span class="service-tag">CHANGE</span>
          <p>Support through the demands and self-reflection that come with major change: graduating
            college, moving to a new place, the end or start of a relationship, being between jobs, or
            getting engaged.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Relationship patterns</h3>
          <span class="service-tag">CONNECTION</span>
          <p>Feeling disconnected, or caught in patterns that keep you from being happy: chronic people
            pleasing, difficulty asserting yourself, or needs that consistently go unmet.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;"><a href="__MOTHERHOOD__" style="text-decoration:none;color:inherit;">New &amp; expecting mothers</a></h3>
          <span class="service-tag">MOTHERHOOD</span>
          <p>Support through pregnancy, postpartum, and the transition to motherhood, including the
            feelings that don't match what it was "supposed" to feel like. <a href="__MOTHERHOOD__">Read more &rarr;</a></p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;"><a href="__FATHERHOOD__" style="text-decoration:none;color:inherit;">New &amp; expecting fathers</a></h3>
          <span class="service-tag">FATHERHOOD</span>
          <p>Support for new fathers navigating competing demands, identity change, and what it means to
            show up as the partner and parent they want to be. <a href="__FATHERHOOD__">Read more &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">What sessions look like</h2>
        <p>The practical shape of the work, so nothing feels like a surprise.</p>
      </div>
      <div class="service-list">
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Format &amp; cadence</h3>
          <span class="service-tag">LOGISTICS</span>
          <p>50-minute sessions, weekly or biweekly depending on what you're working through, in person at
            the Denver office or by telehealth anywhere Dr. Rosen is licensed.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Approach</h3>
          <span class="service-tag">METHOD</span>
          <p>Psychodynamic, CBT, ACT, mindfulness, and attachment/family-systems approaches, drawn on as the
            work calls for it rather than applied as a single fixed protocol, explained in plain language.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Insurance</h3>
          <span class="service-tag">BILLING</span>
          <p>In-network with Lyra Health. For other plans, sessions are $205 for 50 minutes, with a
            superbill available to submit for possible out-of-network reimbursement.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">The first step is one phone call.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Fifteen minutes, no obligation, just
          a conversation about what's bringing you in.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-individual.html", "Individual Adult Therapy in Denver, CO | Rosen Psychology",
    schema("https://rosenpsych.com/services/individual-therapy/", INDIVIDUAL_SVC), individual_main
))

# =====================================================================
# SERVICES: MOTHERHOOD
# =====================================================================
motherhood_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__INDIVIDUAL__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; Individual Adult Therapy</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Pregnancy, Postpartum &amp; Motherhood</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:20ch;margin-top:1rem;">Deeply wanted<br><em>and deeply difficult, at once.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:60ch;">The transition to motherhood can be deeply wanted and deeply difficult at the same time.
        Pregnancy, fertility struggles, and the postpartum period can bring joy and gratitude alongside
        discomfort, anxiety, vulnerability, grief, and a changing relationship with your body and sense of
        self. It can be especially hard to make room for those feelings when you believe you should simply
        feel grateful or happy.</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Schedule a free consultation</a>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">What it's actually like</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:16ch;">Preparing for it and living it are different things.</h2>
      </div>
      <div class="about-body">
        <p>There is also a difference between preparing for motherhood and actually living it. You can read
          the books, make the plans, and imagine the kind of mother you want to be, and still be unprepared
          for the visceral reality of caring for a baby, the intensity of the responsibility, and how little
          control you sometimes have. Meanwhile, there is no shortage of advice about how to do it "right":
          breastfeed, but protect your mental health; sleep train, but respond to every need; go back to
          work, stay home, find the right daycare, cherish every minute.</p>
        <p>Therapy offers a place to quiet some of that noise and make room for your own experience of
          motherhood, including the parts that do not match what you expected it to feel like. Dr. Rosen
          helps women make sense of complicated and sometimes conflicting emotions, navigate changes in
          identity and relationships, and feel more grounded, organized, and cared for during a period when
          so much of their attention is devoted to caring for someone else.</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">You don't have to sort this out alone.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">A free 15-minute call to talk
          through what you're navigating and see if it's a fit.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-motherhood.html", "Therapy for New & Expecting Mothers | Rosen Psychology",
    schema("https://rosenpsych.com/services/motherhood/", INDIVIDUAL_SVC), motherhood_main
))

# =====================================================================
# SERVICES: FATHERHOOD
# =====================================================================
fatherhood_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__INDIVIDUAL__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; Individual Adult Therapy</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">New Fatherhood</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:20ch;margin-top:1rem;">Meaning and joy,<br><em>messier than expected.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:60ch;">Becoming a father can bring tremendous meaning and joy while also being much harder,
        messier, and more complicated than expected. Many new fathers find themselves caught between
        competing demands: to provide and to be present, to support their family and care for themselves,
        to be patient while feeling frustrated or depleted, and to somehow know what they are doing while
        figuring it out as they go.</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Schedule a free consultation</a>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">What it's actually like</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:16ch;">A quieter sense of loss, alongside the joy.</h2>
      </div>
      <div class="about-body">
        <p>Alongside the joy of becoming a parent, there can also be a quieter sense of loss. Parts of life
          and identity that once felt familiar or easily accessible may suddenly feel far away. Becoming a
          parent can also bring your own childhood into sharper focus, stirring up memories, questions, or
          feelings about how you were parented and the relationships you have with your own parents.
          Experiences that once felt settled may look or feel different when viewed from the other side of
          the parent-child relationship.</p>
        <p>Therapy offers a place to talk honestly about these tensions, including the parts of fatherhood
          that may feel difficult to admit, make sense of changes in identity and relationships, and find a
          way of being a father that feels sustainable, connected, and true to who you are.</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">Talk it through before you commit to anything.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">A free 15-minute call, no pressure,
          just a conversation about what's going on.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-fatherhood.html", "Therapy for New Fathers | Rosen Psychology",
    schema("https://rosenpsych.com/services/fatherhood/", INDIVIDUAL_SVC), fatherhood_main
))

# =====================================================================
# SERVICES: CONSULTATION
# =====================================================================
consultation_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__SERVICES__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; All services</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Consultation &middot; Individuals, Parents &amp; Organizations</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:20ch;margin-top:1rem;">Not every question<br><em>requires therapy.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:58ch;">Sometimes, you simply need an expert to help you make sense of something complicated.
        Dr. Rosen offers consultation for individuals, parents, and organizations who would benefit from a
        psychologist's expertise applied to a specific question, concern, or goal.</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Ask about consultation</a>
      </div>
    </div>
  </section>

  <section class="on-ink quote-band">
    <div class="wrap">
      <svg class="quote-mark" viewBox="0 0 34 24" aria-hidden="true"><path d="M0 24V13.5C0 5.6 4.6 0.7 13.7 0L14.8 4C9.4 5.3 6.6 8.2 6.4 12.6H14V24H0ZM19.2 24V13.5C19.2 5.6 23.8 0.7 32.9 0L34 4C28.6 5.3 25.8 8.2 25.6 12.6H33.2V24H19.2Z"/></svg>
      <blockquote>The goal of consultation is to make psychological expertise more accessible and useful: helping people understand complex information, ask better questions, and determine what comes next.</blockquote>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">What consultation is</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:17ch;">Making psychological expertise useful.</h2>
      </div>
      <div class="about-body">
        <p>Consultation can be a single meeting or a series of conversations focused on understanding the
          issue at hand and translating psychological knowledge into useful, practical next steps.</p>
        <p>With extensive training in psychological and neuropsychological assessment, Dr. Rosen can help
          individuals and families understand the results of an evaluation they have already completed.
          Psychological reports can contain an overwhelming amount of data, diagnostic terminology, and
          clinical jargon; consultation is a chance to slow down, review the findings together, and think
          through recommendations and next steps.</p>
        <p>Dr. Rosen also brings expertise in child and adolescent development. Parents may seek consultation
          to better understand what is typical at a particular developmental stage, make sense of a child or
          teen's behavior, or think through how best to support them socially, emotionally, or academically.
          She also works with schools, businesses, and other organizations to translate psychological
          research and mental health concepts into education, training, or guidance relevant to a specific
          community, team, or setting.</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">Consultation may be helpful for</h2>
      </div>
      <ul class="check-list" style="max-width:74ch;">
        <li>Making sense of a recent psychological, neuropsychological, or psychoeducational evaluation</li>
        <li>Understanding test scores, diagnoses, recommendations, or clinical terminology</li>
        <li>Translating assessment findings into concrete next steps at home, school, college, or work</li>
        <li>Understanding a child or teen's behavior within the context of their developmental stage</li>
        <li>Learning developmentally appropriate ways to communicate with or support a child or adolescent</li>
        <li>Providing mental health education, training, or consultation to schools, businesses, and organizations</li>
        <li>Applying psychological research and expertise to a specific question, population, or setting</li>
      </ul>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">Have a question in mind?</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Reach out to see whether
          consultation is the right fit for what you're working through.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Get in touch</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-consultation.html", "Psychological Consultation | Rosen Psychology",
    schema("https://rosenpsych.com/services/consultation/", ALL_SVC), consultation_main
))

# =====================================================================
# SERVICES: PSYCHOLOGICAL ASSESSMENT (placeholder, still substantive)
# =====================================================================
assessment_main = '''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__SERVICES__" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">&larr; All services</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Psychological Assessment &middot; Launching January 2027</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:19ch;margin-top:1rem;">Grounded in the same<br><em>doctoral training.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;">Psychological assessment draws on the same doctoral training as Dr. Rosen's clinical work,
        and a fuller assessment practice is planned to launch in January 2027. This page will be updated
        with real offerings once it's ready; for now, here's what to expect, and how to get on the waitlist.</p>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">Why assessment</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:15ch;">Answers, not just impressions.</h2>
      </div>
      <div class="about-body">
        <p>Therapy is often about process, working through something over time. Assessment is different:
          it's a structured way of answering a specific question about how someone thinks, learns, or
          functions, with more rigor than a conversation alone can provide.</p>
        <p>As the practice grows, a formal assessment offering is planned for January 2027, and it will be
          announced here first. In the meantime, Dr. Rosen offers <a href="__CONSULTATION__" style="color:var(--ink);border-bottom:1px solid var(--gold);text-decoration:none;">consultation</a>
          for anyone who wants help making sense of an evaluation they've already completed.</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Want to be notified?</p>
        <h2 style="margin-top:1rem;">Get on the waitlist.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Send a note and you'll hear first
          when assessment services are ready to book in January 2027.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Join the waitlist</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services-assessment.html", "Psychological Assessment | Rosen Psychology",
    schema("https://rosenpsych.com/services/psychological-assessment/", ASSESSMENT_SVC), assessment_main
))

# =====================================================================
# GETTING STARTED
# =====================================================================
start_main = '''<main id="top">
  <section class="on-paper" style="padding:2.6rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Getting Started</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:18ch;margin-top:1rem;">Three steps.<br><em>No pressure.</em></h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;">You don't need it all figured out before reaching out. Here's exactly what happens
        from first contact through your first session.</p>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap">
      <div class="steps">
        <div class="step">
          <span class="step-index mono">01 / REACH OUT</span>
          <h3>Free 15-minute call</h3>
          <p>A no-pressure conversation about what brings you in, whether it feels like a good fit, and any
            questions you have. Nothing to prepare beforehand.</p>
        </div>
        <div class="step">
          <span class="step-index mono">02 / GET SET UP</span>
          <h3>A few short forms</h3>
          <p>Secure client-portal paperwork and a brief background form. Share as much or as little as feels
            right; there's time to fill in the rest as the work progresses.</p>
        </div>
        <div class="step">
          <span class="step-index mono">03 / FIRST SESSION</span>
          <h3>50 minutes, together</h3>
          <p>A guided conversation to start getting to know each other, beyond whatever brought you in.
            Sessions after that are typically weekly or biweekly, whichever fits.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">The practical details</h2>
        <p>Cost, insurance, and coverage, in one place.</p>
      </div>
      <div class="service-list">
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Cost</h3>
          <span class="service-tag">FEES</span>
          <p>$205 for a 50-minute session, the same rate whether it's in person or by telehealth. You have
            the right to a Good Faith Estimate of expected charges before beginning care; you can ask for
            one at any time.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Insurance</h3>
          <span class="service-tag">BILLING</span>
          <p>In-network with Lyra Health. For other plans, a superbill is available to submit for possible
            out-of-network reimbursement, though that depends on your specific plan.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;">Where sessions happen</h3>
          <span class="service-tag">LOCATION</span>
          <p>In person at 1557 N Ogden Street, Suite 11, Denver, CO, or by telehealth anywhere Dr. Rosen is
            licensed. <a href="__HOME__#top" style="color:var(--ink);border-bottom:1px solid var(--gold);text-decoration:none;">Check your state</a> to confirm coverage.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">Start with a phone call, not a form.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Fifteen minutes, free, to see if
          working together makes sense.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "getting-started.html", "Getting Started | Rosen Psychology",
    schema("https://rosenpsych.com/getting-started/", ALL_SVC), start_main
))

# =====================================================================
# CONTACT
# =====================================================================
contact_main = '''<main id="top">
  <section class="on-paper band-tight final-cta" id="contact" style="padding-top:2.6rem;">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;font-size:clamp(2.1rem,4.2vw,3.2rem);">How to reach her.</h2>
        <p>Send a note below and we'll set up a complimentary 15-minute call: no pressure, just a
          conversation about what brings you to therapy.</p>
        <p class="final-cta-note">Prefer to reach out directly? <a href="mailto:lindsay@rosenpsych.com">lindsay@rosenpsych.com</a>
          or <a href="tel:+17202579204">720-257-9204</a>.</p>
        <p class="final-cta-note" style="margin-top:0.8rem;">In person at 1557 N Ogden Street, Suite 11,
          Denver, CO 80218, or by telehealth anywhere Dr. Rosen is licensed:
          <a href="__HOME__#top">check your state</a>.</p>
      </div>
      <form class="contact-form" id="contactForm" novalidate>
        <div class="form-row">
          <div class="form-field">
            <label for="cf-name">Name</label>
            <input id="cf-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="form-field">
            <label for="cf-email">Email</label>
            <input id="cf-email" name="email" type="email" autocomplete="email" required>
          </div>
        </div>
        <div class="form-field">
          <label for="cf-phone">Phone <span style="text-transform:none;letter-spacing:0;">(optional)</span></label>
          <input id="cf-phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="form-field">
          <label for="cf-message">What brings you here?</label>
          <textarea id="cf-message" name="message" required></textarea>
        </div>
        <p class="form-note">This form isn't a secure or HIPAA-compliant channel, so please don't include
          health information, diagnoses, or other confidential details here. We'll set up a secure way to
          share anything clinical once we're in touch. If this is a mental health emergency, call or text
          988, or call 911.</p>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Send message</button>
          <p class="form-status" id="cfStatus" aria-live="polite"></p>
        </div>
      </form>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "contact.html", "Contact | Rosen Psychology",
    schema("https://rosenpsych.com/contact/", ALL_SVC), contact_main
))

# =====================================================================
# SERVICES (overview)
# =====================================================================
services_main = '''<main id="top">
  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Services</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:18ch;margin-top:1rem;">Ways to work together.</h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;">Every path below draws on the same doctoral-level
        training and the same relationship-first approach, just applied to where you are right now.</p>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap">
      <div class="service-list">
        <div class="service-row">
          <h3><a href="__ADOLESCENT__" style="text-decoration:none;color:inherit;">Adolescent Therapy</a></h3>
          <span class="service-tag">AGES 13&ndash;17</span>
          <p>A private, nonjudgmental space for teens to slow down, get curious about what's underneath,
            and build a relationship that isn't like the other relationships in their life.</p>
        </div>
        <div class="service-row">
          <h3><a href="__INDIVIDUAL__" style="text-decoration:none;color:inherit;">Individual Adult Therapy</a></h3>
          <span class="service-tag">AGES 18+</span>
          <p>For anxiety, self-esteem, relationship patterns, career burnout, and life transitions, grounded
            in understanding your history, not just your symptoms.</p>
        </div>
        <div class="service-row">
          <h3><a href="__MOTHERHOOD__" style="text-decoration:none;color:inherit;">Motherhood</a></h3>
          <span class="service-tag">PREGNANCY &amp; POSTPARTUM</span>
          <p>Support through pregnancy, postpartum, and the identity shift of becoming, or becoming again, a
            mother, including the parts that don't match what you expected it to feel like.</p>
        </div>
        <div class="service-row">
          <h3><a href="__FATHERHOOD__" style="text-decoration:none;color:inherit;">Fatherhood</a></h3>
          <span class="service-tag">NEW &amp; EXPECTING FATHERS</span>
          <p>A place to talk honestly about the tensions of new fatherhood: providing and being present,
            supporting a family while caring for yourself.</p>
        </div>
        <div class="service-row">
          <h3><a href="__CONSULTATION__" style="text-decoration:none;color:inherit;">Consultation</a></h3>
          <span class="service-tag">INDIVIDUALS, PARENTS &amp; ORGANIZATIONS</span>
          <p>Not every question requires therapy. For understanding an evaluation's results, making sense of
            a child's development, or bringing psychological expertise to a specific question or setting.</p>
        </div>
        <div class="service-row soon">
          <h3><a href="__ASSESSMENT__" style="text-decoration:none;color:inherit;">Psychological Assessment</a></h3>
          <span class="service-tag">LAUNCHING JANUARY 2027</span>
          <p>A fuller assessment practice, drawing on the same doctoral training as her clinical work, is in
            development for 2027. Reach out to get on the waitlist.</p>
        </div>
      </div>

      <div class="tag-cloud">
        <span>Anxiety</span><span>Depression</span><span>Life transitions</span>
        <span>Relationship patterns</span><span>New &amp; expecting parents</span>
        <span>Career burnout</span><span>Self-esteem</span><span>College &amp; collegiate athletes</span>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">Not sure which fits? Start with a call.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">Fifteen minutes is usually enough
          to sort out where to begin.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "services.html", "Services | Rosen Psychology",
    schema("https://rosenpsych.com/services/", ALL_SVC), services_main
))

# =====================================================================
# APPROACH
# =====================================================================
approach_main = '''<main id="top">
  <section class="on-ink" style="padding:3rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">How she works</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:16ch;margin-top:1rem;color:var(--paper);">The foundation of the work.</h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;color:var(--ink-soft-inv);">Five principles that shape every
        session, whatever brought you in.</p>
    </div>
  </section>

  <section class="on-ink band" style="padding-top:0;">
    <div class="wrap">
      <div class="approach-list">
        <div class="approach-row">
          <span class="approach-num mono">01</span>
          <div>
            <h3>The relationship comes first</h3>
            <p>Research consistently shows the therapeutic relationship is one of the strongest predictors
              of successful therapy, so sessions are built to feel human, not clinical.</p>
          </div>
        </div>
        <div class="approach-row">
          <span class="approach-num mono">02</span>
          <div>
            <h3>Education &amp; evidence</h3>
            <p>Work is grounded in psychodynamic, CBT, ACT, mindfulness, and attachment/family-systems
              approaches, explained in plain language, not jargon.</p>
          </div>
        </div>
        <div class="approach-row">
          <span class="approach-num mono">03</span>
          <div>
            <h3>Humor has a place here</h3>
            <p>There's room for depth and lightness in the same session. Well-timed humor builds connection
              and shifts perspective on even the hardest material.</p>
          </div>
        </div>
        <div class="approach-row">
          <span class="approach-num mono">04</span>
          <div>
            <h3>Every client makes sense</h3>
            <p>Even the most frustrating patterns make sense in the context of a person's lived experience.
              Understanding the "why" is the first step toward lasting change.</p>
          </div>
        </div>
        <div class="approach-row">
          <span class="approach-num mono">05</span>
          <div>
            <h3>Cultural humility</h3>
            <p>Conversations about identity, culture, and context are approached with humility and openness:
              how culture, race, ethnicity, religion, gender, sexual orientation, and migration history shape
              the way a person understands themselves and the world.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="practical">
      <div class="wrap">
        <span><b>In-person</b> &middot; 1557 N Ogden St, Suite 11, Denver, CO</span>
        <span><b>Telehealth</b> &middot; 40+ states &amp; D.C.</span>
        <span><b>Insurance</b> &middot; In-network with Lyra Health; superbills available</span>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" style="border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;">See if it's the right fit.</h2>
        <p style="color:var(--ink-soft);max-width:36ch;margin-top:1rem;">A free 15-minute call, no forms,
          no pressure.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

PAGES_TO_WRITE.append((
    "approach.html", "Approach | Rosen Psychology",
    schema("https://rosenpsych.com/approach/", ALL_SVC), approach_main
))

# =====================================================================
# STATE PAGES
# =====================================================================
def state_page(state_name, url_path, timezone_html, color_note, area_url_token,
                headline_html, hook_html, good_to_know_h2, closing_h2):
    breadcrumb_label = "&larr; Telehealth coverage, all 43 states"
    return f'''<main id="top">
  <div class="wrap" style="padding-top:1.6rem;">
    <a href="__HOME__#top" class="mono" style="font-size:0.76rem;color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px;">{breadcrumb_label}</a>
  </div>

  <section class="on-paper" style="padding:2rem 0 3.5rem;">
    <div class="wrap" style="max-width:760px;">
      <p class="eyebrow">Telehealth in {state_name} &middot; Licensed Clinical Psychologist</p>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);max-width:18ch;margin-top:1rem;">{headline_html}</h1>
      <p class="hero-sub" style="margin-top:1.1rem;max-width:56ch;">{hook_html}</p>
      <div class="hero-actions" style="margin-top:1.6rem;">
        <a class="btn btn-primary" href="__CONTACT__">Schedule a free consultation</a>
        <a class="btn btn-ghost" href="__ABOUT__">Meet Dr. Rosen</a>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight" style="background:var(--paper-2);">
    <div class="wrap about-grid">
      <div>
        <p class="eyebrow">Good to know</p>
        <h2 style="margin-top:1rem;font-size:clamp(1.7rem,2.8vw,2.3rem);max-width:15ch;">{good_to_know_h2}</h2>
      </div>
      <div class="about-body">
        <p>Sessions happen over secure video, the same 50 minutes as an in-person session in her Denver
          office. A few things worth knowing if you're calling in from {state_name} specifically:</p>
        <div class="transcript">
          <div class="transcript-row"><span class="school">Time zone</span><span class="credential">{timezone_html}</span></div>
          <div class="transcript-row"><span class="school">Session length</span><span class="credential">50 minutes, weekly or biweekly</span></div>
          <div class="transcript-row"><span class="school">Insurance</span><span class="credential">In-network with Lyra Health; superbills available</span></div>
          <div class="transcript-row"><span class="school">Getting started</span><span class="credential">Free 15-minute consultation call</span></div>
        </div>
        <p style="margin-top:1.4rem;">{color_note}</p>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight">
    <div class="wrap">
      <div class="section-head">
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.3rem);">What we'd work on</h2>
        <p><a href="__SERVICES__" style="color:inherit;">See all services</a></p>
      </div>
      <div class="service-list">
        <div class="service-row">
          <h3 style="font-size:1.35rem;"><a href="__ADOLESCENT__" style="text-decoration:none;color:inherit;">Adolescent Therapy</a></h3>
          <span class="service-tag">AGES 13&ndash;17</span>
          <p>A private, nonjudgmental space for {state_name} teens to slow down and get curious about what's
            underneath, not a parent, teacher, or peer.</p>
        </div>
        <div class="service-row">
          <h3 style="font-size:1.35rem;"><a href="__INDIVIDUAL__" style="text-decoration:none;color:inherit;">Individual Adult Therapy</a></h3>
          <span class="service-tag">AGES 18+</span>
          <p>For anxiety, self-esteem, relationship patterns, career burnout, and life transitions, grounded
            in understanding your history, not just your symptoms.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-paper band-tight final-cta" id="contact" style="background:var(--paper-2);border-top:1px solid var(--line);">
    <div class="wrap final-cta-simple">
      <div>
        <p class="eyebrow">Let's talk</p>
        <h2 style="margin-top:1rem;font-size:clamp(2rem,3.6vw,2.8rem);">{closing_h2}</h2>
        <p>Book a complimentary 15-minute consultation: no forms, no pressure, just a conversation
          about what brings you to therapy.</p>
      </div>
      <a class="btn btn-primary" href="__CONTACT__" style="padding:1.05em 1.9em;font-size:0.9rem;">Schedule a consultation</a>
    </div>
  </section>
</main>'''

STATE_DATA = [
    ("state-arizona.html", "Arizona", "AZ",
     "Same as Denver most of the year (no daylight saving in AZ)",
     "Arizona doesn't observe daylight saving. That means sessions run on the same clock time as Denver "
     "for most of the year, but during daylight saving months (roughly March&ndash;November) they'll show "
     "as one hour earlier on your local Arizona clock than on Dr. Rosen's Denver schedule. Arizona is also "
     "a popular relocation spot for retirees, remote workers, and families drawn to warmer winters, "
     "a common reason existing Denver clients ask about continuing care after a move.",
     "Denver-trained care,<br><em>now available across Arizona.</em>",
     "Arizona has become a common landing spot for Dr. Rosen's existing Denver clients, whether they're "
     "retiring, working remotely, or simply chasing warmer winters. Telehealth means the move doesn't have "
     "to mean starting over with someone new.",
     "One clock, almost year-round.",
     "Let's talk before the move."),
    ("state-florida.html", "Florida", "FL",
     "Eastern Time, two hours ahead of Denver year-round.",
     "Florida has no state income tax and is a frequent relocation destination for families, retirees, and "
     "remote workers alike.",
     "Licensed telehealth therapy,<br><em>anywhere in Florida.</em>",
     "From Miami to the Panhandle, Dr. Rosen is licensed to see clients throughout Florida by video, a "
     "state that draws a steady stream of relocating families, retirees, and remote workers.",
     "A few Florida specifics.",
     "One call, wherever in Florida you are."),
    ("state-north-carolina.html", "North Carolina", "NC",
     "Eastern Time, two hours ahead of Denver year-round.",
     "Home to the Research Triangle's fast-growing tech, biotech, and finance sectors, which has made it a "
     "common landing spot for people relocating for work.",
     "Support for the move to<br><em>North Carolina, and beyond.</em>",
     "The Research Triangle's tech, biotech, and finance boom has brought a lot of new residents to North "
     "Carolina, and Dr. Rosen is licensed to work with clients anywhere in the state by telehealth.",
     "A few things specific to North Carolina.",
     "Let's find a time that works."),
    ("state-virginia.html", "Virginia", "VA",
     "Eastern Time, two hours ahead of Denver year-round.",
     "Home to a large federal, government-contracting, and military community, particularly in Northern "
     "Virginia near Washington, D.C.",
     "Therapy that keeps up<br><em>with life in Virginia.</em>",
     "Virginia's federal, government-contracting, and military community often means demanding schedules "
     "and frequent moves. Telehealth sessions from Dr. Rosen fit around both.",
     "Logistics for Virginia clients.",
     "Book a call around your schedule."),
    ("state-washington.html", "Washington", "WA",
     "Pacific Time, one hour behind Denver year-round.",
     "One of the country's biggest tech hubs, anchored by Seattle, and a common destination for people "
     "relocating for work in that industry.",
     "Licensed care for<br><em>Washington's fast pace.</em>",
     "Washington's tech industry, centered around Seattle, draws people from all over, often into demanding "
     "jobs with little room to spare. Dr. Rosen is licensed to see clients throughout the state by telehealth.",
     "A few Washington specifics.",
     "Let's find fifteen minutes."),
]

for fname, state_name, abbr, tz_html, color_note, headline_html, hook_html, good_to_know_h2, closing_h2 in STATE_DATA:
    url = f"https://rosenpsych.com/telehealth/{fname.replace('state-','').replace('.html','')}/"
    main_html = state_page(state_name, url, tz_html, color_note, abbr, headline_html, hook_html, good_to_know_h2, closing_h2)
    PAGES_TO_WRITE.append((
        fname, f"Telehealth in {state_name} | Rosen Psychology",
        schema(url, BOTH_THERAPY_SVC, area_served={"@type": "State", "name": state_name}),
        main_html
    ))

# =====================================================================
# WRITE ALL FILES
# =====================================================================
for fname, title, schema_json, main_html in PAGES_TO_WRITE:
    out = chrome.assemble(title, schema_json, main_html)
    with open(fname, "w") as f:
        f.write(out)
    print("wrote", fname, f"({len(out)} bytes)")
