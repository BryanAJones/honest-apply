# Automated Job Scan — Spec

Optional spec for scheduling a recurring scan that surfaces filtered, drafted application
material on a daily cadence. Read this before scheduling; not every job board is fetchable
unattended.

---

## What this delivers

- **Output:** Filtered short list + drafts. Only APPLY / STRETCH roles. For each: fit
  verdict, most-likely-rejection-reason, direct link, and tailored materials pre-drafted.
- **Cadence:** Daily (early AM is a reasonable default).
- **Boundary:** Surfaces and pre-stages. The user applies live themselves. Never
  auto-submits.

## Design principle (non-negotiable)

Breadth WITHOUT the fit-filter is just noise. Aggregate wide -> run every listing through
the fit filter -> surface ONLY the short list. Volume in, ruthless cut, a few items out.

---

## Step 0 — Reconnaissance (do this first)

Test which sources actually return real listing content to an unattended fetch (not a
login wall or a JS-only blank shell). Keep only the passing sources.

**Candidate sources (likely fetchable):**
- Remote-first boards with feeds: We Work Remotely, Remotive, Remote OK (often expose
  RSS/JSON)
- ATS aggregators that index company career pages
- Industry-specific job boards relevant to the user's Targeting Spec

**Candidate sources (often hostile to unattended fetch):**
- LinkedIn (login wall, anti-bot)
- Indeed (anti-bot)
- Most Workday / Greenhouse-rendered listing pages (JS-rendered)

Record pass/fail per source. The scan runs ONLY over the passers. For hostile sources, fall
back to the user opening them in a browser they control.

## Step 1 — Fetch

Pull current postings from verified-fetchable sources only.

## Step 2 — Filter (the gate)

Run each listing through the Fit Filter from SKILL.md. Apply every hard block from the
user's Targeting Spec. Carry forward ONLY APPLY / STRETCH. If the day's pass list is long,
the filter is too loose.

## Step 3 — Draft

For each passing role, draft tailored materials per SKILL.md (lead with ownership
evidence; relevant headline asset re-cut; Cover Letter Spine as cover-letter anchor). Run
the anti-slop check before including anything.

## Step 4 — Deliver + Log

- Present as a compact ranked short list: role + company, verdict, rejection reason,
  direct link, draft, anti-slop status.
- Mark roles on hostile sites as "open yourself — filter verdict provided."
- Log each to tracker.csv (status=Drafted, followup +7d).

---

## Honest limits

- A scheduled task's reach = what web_fetch / web search can pull unattended.
  JS-rendered and login-walled boards will NOT work this way.
- It surfaces and drafts; it cannot pre-stage a LIVE application without the user present.
- Wider / hostile-source coverage requires the user supervising with a real browser — a
  separate, in-the-loop mode, not this scheduled scan.
