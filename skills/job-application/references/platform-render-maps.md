# Platform Render Maps

How the **platform-neutral Profile Pack** (authored once, in `career-profile.md`) gets cut into
each platform's actual fields and limits. Read by the **Profile Pack step**
(`job-application-profile`).

**The pattern:** author the identity ONCE (positioning, overview, rate card, portfolio
projects-as-case-studies, skills). Then render per platform. Adding a site = adding a map here,
never re-authoring the content.

> **Fact freshness:** field names and character limits change. Status tags below: **✅ verified
> 2026-06-03** / **⚠️ unverified** (confirm in the platform's profile editor). Re-check ✅ items
> older than ~3 months.

---

## Neutral source fields (the Profile Pack)

Every render map maps FROM these:
- `positioning` — one-line "what I do for whom"
- `overview` — the longer narrative (with a strong first ~2 lines)
- `services[]` — each: name, rate model (hourly / fixed / project-min), rate
- `portfolio[]` — each: title, problem, what-I-did, outcome, link-or-media, **honesty fields**
  (solo/team + slice, maturity/traction, demonstrable-level, IP public/private)
- `skills[]`
- `rate_card` — published / floor / min, per wedge

---

## Upwork ✅

Outbound bid platform. Supports up to **2 Specialized Profiles** — use them for distinct wedges.

| Upwork field | Map from | Limit / note |
|---|---|---|
| Title | `positioning` (per wedge) | **≤ ~70 chars.** Lead with the concrete service. |
| Overview | `overview` | ~5000 chars, but the **first ~2 lines show before a "more" fold** — put the hook + strongest proof there. |
| Skills | `skills[]` | up to ~15 tags; match Upwork's tag vocabulary |
| Hourly rate | `rate_card.published` | bid lower (toward `floor`) per-gig in cold-start |
| Portfolio items | `portfolio[]` (2–4 best) | **Image/video upload — a public link is NOT required.** Use media for login-gated/private work. |
| Specialized Profiles | one per wedge | only when wedges attract different buyers/search terms |

**Honesty enforcement on render:** never imply a portfolio item is more mature than its tag
(no "live"/"users" for a `deployed-no-users` item); never link a URL that's login-walled/empty.

## Contra ✅

Portfolio-forward, $0 to apply, **no 70-char title cap**, projects do the selling.

| Contra field | Map from | Note |
|---|---|---|
| Headline | `positioning` | fuller line OK |
| About / Bio | `overview` | portfolio-first audience; keep it tight, let projects carry |
| Services | `services[]` | listed as offerings with rates (hourly or fixed) |
| Projects | `portfolio[]` | **the core** — lead with these; rich media |
| Skills | `skills[]` | — |

## Wellfound ✅

Startup job board; you apply to roles + keep a profile. Judged on the profile + a conversation.

| Wellfound field | Map from | Note |
|---|---|---|
| Headline / role | `positioning` | frame as the role you want (e.g. "Fractional PM", "Full-stack + AI") |
| About | `overview` | startup audience — emphasize shipping + range |
| Experience | `portfolio[]` + roles | real roles; portfolio projects as evidence |
| Skills | `skills[]` | — |
| Salary/equity expectation | `rate_card` | translate hourly → expected comp range |

> Wellfound is more "apply to posted roles" than "publish a bid profile" — the Profile Pack
> populates the standing profile; the gig/SPEND-SKIP branch handles individual applications.

## Fiverr ⚠️ (different shape — inbound)

You publish **gig listings** (productized services), buyers come to you. NOT outbound apply.
- Map `services[]` → gig listings (title, packages/tiers, price).
- Map `portfolio[]` → gig gallery media.
- This is a **listing-optimizer** mode, deferred in the design — not the same engine as
  outbound platforms. Confirm Fiverr's current gig structure before building.

## Freelancer.com ⚠️
Similar to Upwork (bid + profile). Map Title→`positioning`, Summary→`overview`,
Skills→`skills[]`, Portfolio→`portfolio[]`. Confirm field limits.

## Dribbble / Behance ⚠️ (portfolio gallery — link + gallery, not a fielded profile)

Not a bid platform and not a fielded profile in the same sense — these are **visual portfolio
galleries** that generate *inbound* leads. There's little to "render": you publish work and a
short bio.
- `portfolio[]` → gallery posts (image/video + a short caption per piece). This is the product.
- `positioning` + a trimmed `overview` → the profile bio.
- `services[]` / rates → optionally in the bio or a pinned post.
- **No proposal/bid flow.** The recommender lists these as a START-HERE *home* for designers;
  leads arrive inbound and are handled outside the gig (SPEND/SKIP) pipeline. So for these
  platforms the Profile Pack step outputs the bio + which pieces to post, not a fielded render.

Confirm current profile fields before relying.

---

## Adding a new platform
1. Add a row to the table in `platform-economics.md` (with cost-to-apply + status).
2. Add a render map section here (fields ← neutral source, with limits + status tag).
3. That's it — no content re-authoring. The Profile Pack step picks up the new map.
