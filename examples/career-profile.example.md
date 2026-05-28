# Career Profile — Maya Chen (FICTIONAL EXAMPLE)

> **This is a fictional example.** Maya doesn't exist — she's the candidate the kit's
> dry-run interview produced, included here so you can see what a finished profile
> looks like. Do not copy this verbatim. Your `career-profile.md` will look different
> because the interview pushes on YOUR resume and YOUR situation.

---

## 0. TARGETING SPEC

- **Role type:** Senior Software Engineer — Backend
- **Seniority to target:** Senior SWE (no jump to Staff yet)
- **Seniority to auto-SKIP (too senior):** Staff, Principal, Engineering Manager
- **Tenure-in-posting cap:** Auto-SKIP if listing requires more than 6 years.
- **Industries with a credible story:**
  - Developer tools / infrastructure (primary — explicit move target)
  - B2B SaaS broadly (transferable, but not the goal)
  - **Industry as hard filter?** Yes — dev-tools / infra companies only.
- **Geography:** Remote-first only; NY metro hybrid OK if 1-2 days max.
- **Salary floor:** $190,000 base (HARD floor — auto-SKIP below this)
- **Job boards to search (priority order):**
  1. Y Combinator Work at a Startup
  2. Wellfound
  3. Hacker News "Who's Hiring" monthly thread
  4. Console.dev jobs
  5. LinkedIn (last resort)
- **Additional hard blocks:** No agency/contract. No Java-heavy stacks.
- **Tension flags to watch:** Salary floor + non-Staff seniority is achievable in
  dev-tools but the band is tight — many Sr SWE listings at this seniority cap
  out around $180k. Watch for listings that don't post bands.

---

## 1. ASSET INVENTORY

### HEADLINE ASSET 1 — Internal dev-env CLI (off-resume, promoted up)
- **What got built:** A Go-based CLI for spinning up dev environments for new
  carrier-integration partners. Wraps Terraform and internal API calls with
  opinionated config; distributed via internal Homebrew tap.
- **Maya's specific role:** Built it solo, unprompted. Nobody assigned it; she
  got tired of the manual 2-day onboarding process.
- **Framing for dev-tools Senior SWE:** This is engineer-as-end-user work — the
  exact instinct dev-tools companies hire for. Recognized friction, built tooling,
  measured adoption.
- **Hard numbers:** Onboarding 2 days -> 20 minutes. ~15 active weekly users out
  of ~40 engineers.
- **Do NOT claim:** It's open source (it's internal). She did NOT design the
  partner-onboarding flow itself, just the tooling that automated the existing one.

### HEADLINE ASSET 2 — FHIR data pipeline (Acme Health)
- **What got built:** FHIR-compliant data pipeline processing 10M+ patient records
  daily.
- **Maya's specific role:** Solo ownership end to end.
- **Framing for dev-tools Senior SWE:** Proves she can ship and operate a real
  high-throughput data system, not just write services. Healthcare data is regulated
  and unforgiving — survivability matters.
- **Hard numbers:** 10M+ records/day. Solo build.
- **Do NOT claim:** Don't overstate the regulatory scope — she implemented
  FHIR-compliance, didn't architect the broader HIPAA posture.

### HEADLINE ASSET 3 — Rate-quoting engine: sync -> event-driven
- **What got built:** Architecture call to move the rate-quoting engine from
  synchronous to event-driven, then led the implementation.
- **Maya's specific role:** Made the call, ran the rewrite.
- **Framing for dev-tools Senior SWE:** Proves she can make and defend a real
  architecture decision — the kind of judgment dev-tools companies want at Senior.
- **Hard numbers:** [no metric available — qualitative claim]
- **Do NOT claim:** Don't conflate this with the broader microservices migration;
  that was her staff engineer's call.

### SUPPORTING ASSETS
- **Carrier integrations framework (FreightFlow):** Built the integration framework
  + ~30 of the connectors directly; platform now runs 200+. Do NOT claim she built
  all 200 — she built the framework that lets others add them.

---

## 1.5 CLAIMS LEDGER

- **Current role:** Senior Software Engineer, FreightFlow (B2B logistics SaaS),
  started Jun 2022, full-time
- **Prior roles:**
  - Software Engineer, Acme Health (healthtech SaaS), Aug 2020 – May 2022, full-time
  - Junior Software Engineer, StartupCo (consumer marketplace), Jul 2019 – Jul 2020,
    full-time
- **Total professional tenure:** ~5 years (post-CMU)
- **Location:** Brooklyn, NY
- **Education:**
  - BS Computer Science, Carnegie Mellon University, 2019
- **Education anti-claims:** Do not list bootcamps (none); do not claim grad work
  (none).
- **Certifications:** None worth listing.
- **Tools / stack (defensible):** Go, Ruby (Rails), PostgreSQL, Kafka, gRPC,
  Terraform (basic), AWS (EKS, RDS, SQS).
- **Tool exposure (NOT claim as expertise):** Rust — shipped one internal tool;
  do not claim "Rust engineer."
- **Hard numbers:**
  - Internal CLI: 2 days -> 20 minutes onboarding, ~15 weekly users (solo build)
  - FHIR pipeline: 10M+ records/day (solo build)
  - Rate-quoting rewrite: sync -> event-driven (Maya's call, no quantified metric)
  - 200+ integrated carrier APIs at FreightFlow (framework built by Maya, ~30
    connectors built directly; rest added by others)
  - 40% latency reduction at Acme (with 2 others, not solo)
  - 60% deploy time reduction during microservices migration (team-wide, not
    Maya's solo claim — do not overclaim)

---

## 2. WRITING STYLE GUIDE

### Personal voice patterns — do these
- Open with a specific failure mode (an actual pager incident, a real bug) rather
  than a thesis statement.
- Use small code snippets inline as evidence rather than abstract description.
- Close by naming what she'd do differently — no triumphalism.

### Personal phrases to avoid
- "best practices"
- "battle-tested"
- "at scale" (when used as filler)

---

## 3. THE COVER LETTER SPINE

**Situation:** lateral

**What's changing:** The work at FreightFlow is too CRUD-heavy — same shape of code
repeatedly, and there's no engineer-as-end-user component. Wants to build for an
audience that reads the code.

**What's specifically interesting about the target company category:** Linear's
"How We Built Linear" sync-engine blog post — the kind of engineering writing
that can only exist when the product audience reads code. Vercel's work on Turborepo
and the accountability loop of shipping to developers who will immediately notice
sloppiness.

**Honest reason for leaving** (context, not letter content): Got passed over for
staff promo last cycle; that's clarifying, not the load-bearing reason. Avoid
bitterness in the Spine.

**The Spine (4-6 sentences):**

> Companies like Linear and Vercel ship to engineers who notice. The "How We Built
> Linear" sync-engine post is the kind of writing you can only do when the product
> audience reads the code, and that accountability loop is what I want next. After
> five years building backend services against logistics APIs, the work I'm proudest
> of isn't on the assigned roadmap — it's a CLI I built because spinning up dev
> environments for new partners took two days and I got tired of it. Fifteen
> engineers use it weekly now; onboarding takes twenty minutes. That instinct — see
> a developer-friction problem, build the tool, watch other engineers actually use
> it — is what I want my whole job to be.
