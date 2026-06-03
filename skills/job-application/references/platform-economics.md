# Platform Economics & Recommender Rules

Single source of platform facts for the freelance track. Read by:
- the **SPEND/SKIP filter** (the gig branch of `job-application`) — for cost-to-apply per platform
- the **Platform Recommender** (`job-application-profile`) — to rank starting platforms per profile

> **Fact freshness** (per the kit-wide convention in `../SKILL.md`): platform fees, connect
> prices, and application models drift constantly. Every fact below carries a status:
> **✅ verified 2026-06-03** or **⚠️ unverified** (confirm on the platform's own pricing page
> before relying). When you use a fact in a live recommendation: re-verify ✅ facts older than
> ~3 months, and resolve ⚠️ facts first. Never present a stale fee as current.

---

## The key abstraction: "cost to apply" has three models

Connects are just one way a platform charges you to compete. Generalize to:

- **pay-per-bid** — each application costs money/credits. The SPEND/SKIP filter asks
  *"is this worth my bid budget?"* → bid only where you can plausibly win.
- **free** — $0 to apply; the real cost is your time + lower deal volume. The filter asks
  *"is this worth my time?"* → fit + effort matter, dollars-per-bid doesn't.
- **vetting-gate** — no per-bid cost, but a one-time screening/application wall. The "cost"
  is passing the gate once; after that, applying is cheap.

The filter must read each platform's model from the table below, not assume connects.

---

## Platform table

| Platform | Cost to apply | Take rate (from freelancer) | Model | Shape | Best-fit profile | Status |
|---|---|---|---|---|---|---|
| **Upwork** | Connects ~$0.15 ea; 4–16/bid, **dynamically repriced to 16–40+** on hot gigs ($2.40–$6+); ~$50–150/mo typical | ~10% | pay-per-bid | Crowded bid pool, huge volume | Established freelancers with a JSS; commodity-to-mid services; deliver-to-prove cold-start gigs | ✅ |
| **Contra** | $0 | **0%** (you absorb Stripe ~2.9% + $0.30) | free | Portfolio-forward; no real job board, you promote your profile | Strong *showable* portfolio (designers, devs with public work); lower volume | ✅ |
| **Wellfound** (ex-AngelList) | $0 | **0%** | free | Startup job board; one-click private apps; salary/equity upfront | Devs / PMs / designers who want startup clients; judged on a call + trial, not a portfolio | ✅ |
| **Go Fractional** | $0 to apply, **vetting-gate** (discovery call, curated) | **20% of ongoing comp** | vetting-gate | Full-service: matches, contracts, invoices for you | High-end fractional execs/PMs/engineers | ✅ |
| **Fiverr** | $0 to list | ~20% | **inbound** (you publish gigs, buyers come — NOT outbound apply) | Productized gig listings | Packaged, repeatable services; SEO-able niches | ⚠️ confirm rate/model |
| **Freelancer.com** | Bid credits (limited free/mo, buy more) | ~10% or $5 min | pay-per-bid | Bid pool, high volume, lower-end | Price-competitive commodity work | ⚠️ confirm |
| **Toptal** | $0, **hard vetting-gate** (multi-stage screening) | Markup on client side | vetting-gate | Curated elite network | Senior devs/designers/finance who pass screening | ⚠️ confirm |
| **Braintrust** | $0 | **0% to talent** (client pays the fee) | free / curated | Decentralized talent network | Mid-to-senior tech talent | ⚠️ confirm |
| **A.Team** | $0, **vetting-gate** (application) | Platform fee | vetting-gate | Curated product/eng/design "teams" | Senior product/eng/design building in small teams | ⚠️ confirm |
| **Fractional Jobs** (fractionaljobs.io) | $0 | n/a (job board) | free | Job board for fractional roles | Fractional execs/PMs/marketers | ⚠️ confirm |
| **Dribbble / Behance** | $0 | n/a (portfolio + inbound) | free / inbound | Design portfolio → inbound leads | Designers with strong visual portfolios | ⚠️ confirm |

> Adding a platform = add a row here (with a status tag) and a render map in
> `platform-render-maps.md`. Keep the two files in sync.

---

## Recommender rules

Map the user's profile to a **ranked starting set per wedge**: `start here / add next / skip`.
Inputs come from the profile: discipline/wedge, **portfolio strength**, **track record**,
**rate tier / seniority**.

**Critical: "showable" ≠ "exists."** Portfolio strength means *polished and demonstrable* —
not "I have deployed-but-rough/pre-alpha work." A builder with real code but no demos/traction
is NOT "strong portfolio."

| Profile signal | Start here | Add next | Skip / later |
|---|---|---|---|
| **Showable portfolio + new** (designer w/ Dribbble; dev w/ shipped public work) | Contra, Dribbble/Behance (designers) | Wellfound | Upwork until you have reviews |
| **Build-capable but thin proof + new** (real code, no demos/traction, no reviews) | Wellfound (call + paid trial), small Upwork cold-start (deliver-to-prove) | Contra as a *home* (code + design) | Portfolio-forward platforms as a spearhead |
| **High-end strategic / fractional** (PM, exec, architect) | Go Fractional, Fractional Jobs, A.Team | Wellfound | Upwork (its buyers want cheap task-doers) |
| **Commodity / high-volume, price-competitive** | Upwork, Fiverr | Freelancer.com | Curated networks (overkill) |
| **Established (real reviews / JSS)** | Upwork as a *primary* channel (volume) | keep portfolio platforms for inbound | — |

**The honest move for any "new + thin proof" profile:** default the Proposal Spine to a
**small paid trial** ("let me build/do a slice for $X first"). Proving by doing beats
overselling a thin portfolio. (See `writing-style-defaults.md` → maturity/traction honesty.)

### Discipline quick-notes
- **Designers** → portfolio-forward platforms win (Contra, Dribbble, Behance); visual proof
  is the whole game.
- **Developers / AI builders** → Wellfound + deliver-to-prove gigs; public code/GitHub is
  proof even without finished products.
- **Writers** → Contra + niche job boards; samples are cheap to show, so lead with them.
- **PMs / fractional execs** → fractional-specific boards; skip generalist bid pools.

---

## Output contract (what the recommender returns)

Per wedge, a short list:
```
START HERE → <platform> — <one-line why> (cost to apply: <model>)
ADD NEXT  → <platform> — <why>
SKIP/LATER → <platform> — <why not yet>
```
Always state cost-to-apply so the user sees the money/time tradeoff, and stamp the advice with
the verification date of the facts it used.
