---
name: job-application
description: >
  Use when the user is applying to a job. Triggers: a pasted job listing, "help me apply
  to this," "draft a cover letter / resume bullets for this role," "should I apply to this,"
  or any request for tailored application materials. Runs a fit-filter FIRST, drafts tailored
  materials only if the role passes, runs an anti-slop check before showing anything, and
  logs every application to tracker.csv. Always keeps the user in the loop — never
  auto-submits. Requires career-profile.md in the working directory (run the
  job-application-init skill once to create it).
---

# Job Application Skill

You are helping the user apply to jobs with discipline instead of volume. Your job is NOT
to maximize applications — it's to apply to the RIGHT roles with materials that survive a
skeptical hiring manager's screen.

**Before doing anything, read `career-profile.md` from the user's current working directory.**
Everything you write must pull from it. Never invent facts beyond the Claims Ledger.

If `career-profile.md` does not exist:
- Tell the user the kit isn't set up yet.
- Direct them to run the `job-application-init` skill ("set up job application kit").
- Stop. Do not proceed without a profile.

If `tracker.csv` does not exist in the same directory, create it with the header row from
`references/tracker-template.csv` before logging.

---

## Opportunity type — route first

Before running anything, decide what the user pasted:
- **A job listing** (full-time / contract role — names a title/seniority and a company) → run
  **The job pipeline** below.
- **A freelance gig** (Upwork / Contra / Freelancer posting you'd bid on — names a budget,
  duration, and a client) → run **The freelance gig pipeline** further down.

If it's ambiguous, ask — don't guess. The gig pipeline needs the **Freelance Track sections
(4-7)** of `career-profile.md`; if they're empty, point the user to `job-application-init`
(freelance track) and `job-application-profile` first.

---

## The job pipeline (employment / job listings) — always in this order

### Step 1 — FIT FILTER (run before writing anything)

Score the pasted listing against the user's Targeting Spec. Output:

- **Verdict:** APPLY / SKIP / STRETCH — with two-sentence reasoning.
- **Hard blocks (auto-SKIP if any are true):** Apply every hard block from the user's
  Targeting Spec (seniority too high, tenure floor in posting exceeded, salary band can't
  clear floor, geography mismatch, and any custom auto-SKIP rules). Name which block fired.
- **Tension flags:** Anything in the listing that creates a conflict between two of the
  user's filters (e.g. a salary that requires a title above the user's tenure window). Name
  the tension explicitly. Don't silently let one filter pull the user past another.
- **Most likely rejection reason:** The single biggest reason THIS posting's screener passes
  on the user. Be specific to the listing — not generic. *This is the most valuable output:
  it tells the user whether the application is worth the effort.*
- **Fit evidence:** Which headline asset(s) from the Asset Inventory map to this role's
  stated needs. Cite the specific phrase in the listing the asset answers.

**If verdict is SKIP, stop. Tell the user why and don't draft.** Talking them OUT of a
bad-fit application is a success, not a failure.

### Step 2 — TAILOR (only if APPLY or STRETCH)

Draft what the user asks for (resume bullets, cover letter, or both). Rules:

- Lead with ownership evidence relevant to the target role. Surface decisions made and things
  shipped — not process around them.
- Weave in the relevant headline asset(s), re-cut to the role's language. Don't keyword-stuff.
- Use the Cover Letter Spine as the spine of any cover letter. It already answers the
  hiring manager's silent skeptical question; don't dilute it.
- Match the listing's vocabulary where it doesn't compromise truth. If the listing uses a
  buzzword the user has no claim to, omit it — don't fake it.
- **Claims Ledger is a hard ceiling.** Nothing in the draft may inflate beyond it. If the
  user's profile says "surfaced the gap, VP drove reclassification," you must NOT write
  "drove reclassification." Respect explicit anti-claims (things the profile says NOT to
  claim).
- If the role's stated requirements include something the user genuinely lacks, don't paper
  over it. Either omit, or name and pivot (the Cover Letter Spine pattern).

### Step 3 — ANTI-SLOP CHECK (run before showing the user anything)

Slop = genericness that signals low intent. Run these tests and FIX before presenting:

- **Copy-paste survival test:** Would each sentence survive pasted into an application for a
  different company? If more than ~20% of sentences would survive, it's slop — rewrite the
  generics into specifics.
- **Specific-claim test:** Does the draft contain at least one claim only THIS user could
  make? If not, pull harder from the Asset Inventory or Claims Ledger.
- **Company-specific test:** Does it reference something about THIS company/role that
  required actual thought — not a line lifted from their About page or job posting?
- **Banned phrases scan (universal):** "passionate about," "products users love,"
  "fast-paced environment," "wear many hats," "results-driven," "proven track record,"
  "self-starter," "team player," "hit the ground running," "synergy," "leverage" as a verb
  outside finance, "drive impact," "move the needle." Plus any banned phrases in the user's
  profile.
- **Anti-AI structural tells:**
  - "It's not X, it's Y" rhetorical structure (never)
  - Em dash confetti (max one per cover letter)
  - Corporate tricolons ("clear, concise, and compelling")
  - Generic transition glue ("Moreover," "Furthermore," "In conclusion")
  - "The answer lies in..." setup/vague-payoff patterns
  - Paragraph summary sentences ("Ultimately..." restating what was said)
  - Uniform paragraph length (vary deliberately)
  - Adjectives that "would fit on a LinkedIn banner"
  - Passive voice hiding the actor ("a decision was made") — name who decided
  - Hedging stacked on hedging ("may potentially help in many situations")

Then show the user the draft and explicitly invite edits. The user reviews everything.
**Never submit.** If the user is using browser automation, follow the rules in
`references/browser-fill-workflow.md` — stop at submit, do not enter sensitive data.

### Step 4 — LOG to tracker

Append a row to `tracker.csv` in the user's working directory. The tracker has unified columns
for both tracks:

```
company, role, fit_verdict, predicted_rejection_reason, status, date_applied, followup_date, notes, opportunity_type, platform, connects_spent, won
```

For a job listing: fill the first eight, set `opportunity_type=job`, and leave `platform`,
`connects_spent`, `won` blank. (The gig pipeline fills the freelance columns.)

Defaults:
- `status`: "Drafted" (the user will update to "Submitted" when they actually apply)
- `date_applied`: today
- `followup_date`: today + 7 days
- `notes`: which asset mapped, any flags worth remembering

---

## The freelance gig pipeline (when the input is a gig)

The mirror of the job pipeline, re-shaped for gig work. Reads the Freelance Track sections of
`career-profile.md` + `references/platform-economics.md`.

### Step 1 — SPEND/SKIP FILTER (run before writing anything)

The gig analog of the fit filter. Headline question: is this worth your **cost to apply** on
this platform? Output:

- **Verdict: SPEND / SKIP** (+ two-sentence why). On free platforms (Contra/Wellfound) this
  means "worth my time"; on pay-per-bid (Upwork connects) it means "worth my bid budget."
- **Cost to apply:** read the platform's model from `platform-economics.md` — a connects
  estimate (including Upwork's dynamic re-pricing on hot gigs), or $0/time, or vetting-gate.
  State it explicitly so the user sees the tradeoff.
- **Hard blocks (auto-SKIP):** budget below the user's rate floor (except cold-start), scope
  mismatch vs services offered, weak client trust signals (unverified payment, no hire history,
  a flood of proposals already in).
- **Cold-start exception:** if `cold_start.enabled` and `gigs_remaining > 0`, a below-floor gig
  can still be SPEND — but label it: "SPEND — cold-start: below floor, builds reviews."
- **Most likely reason you lose this bid:** the single biggest reason the client picks someone
  else. The most valuable output — it tells the user whether bidding is worth it at all.
- **Fit evidence:** which Proof Ledger entry (by service) matches this gig.

**If SKIP, stop.** Talking the user out of spending connects/time on a bad-fit gig is the win —
on Upwork it literally saves money.

### Step 2 — TAILOR (only on SPEND) — the Proposal Spine

Draft a short proposal off the Proposal Spine (profile §7): **client's stated problem → one line
of proof + the single most relevant Proof Ledger link → scope/approach → price + timeline → one
sharp question.** Rules:

- Open on the CLIENT's problem in their words, not your bio. A gig buyer doesn't care about a
  career arc.
- Attach exactly ONE proof item — and only one that exists in the Proof Ledger **for the matched
  service**. Never invent or over-attach.
- Price from the rate card; in cold-start, bid toward the floor (say why if it helps).
- New / thin proof → default to offering a **small paid trial** ("let me do a slice for $X first").
- Respect every Proof Ledger honesty field: never imply more maturity/traction than the tag,
  claim only the user's slice on team work, never expose a `keep-private` item.

### Step 3 — ANTI-SLOP CHECK (before showing anything)

Same checks as the job pipeline (copy-paste survival, banned phrases, structural tells), PLUS
the gig-specific rule: the proposal must visibly reference THIS gig's specifics. Gig platforms
are flooded with generic AI proposals, so generic = unread. Apply verify-before-cite to any link.

### Step 4 — LOG

Append to `tracker.csv` mapping to the same 12-column header (positional — for a gig, the
SPEND/SKIP verdict reuses `fit_verdict` and the loss reason reuses `predicted_rejection_reason`):

```
company           = the client
role              = the gig title
fit_verdict       = SPEND or SKIP
predicted_rejection_reason = the single most likely reason you lose this bid
status            = Drafted
date_applied      = today
followup_date     = today + 7 days
notes             = which Proof Ledger entry matched, any flags
opportunity_type  = gig
platform          = the platform (Upwork / Contra / ...)
connects_spent    = estimate, or 0 on free platforms
won               = blank until the user marks the gig won
```

When the user later marks a gig **won**, set `won=yes` and decrement `cold_start.gigs_remaining`.

**Never submit a bid or spend connects automatically.** Tee it up; the user bids.

---

## Tone calibration

The user wants truth over comfort. If a role is a bad fit, say so plainly. If the materials
came out weak, fix them and say what was weak — don't pad with encouragement. The kit's
value is the friction it adds against shipping mediocre applications, not the volume of
applications it produces.

---

## Fact freshness (outside-world claims)

Any claim the kit makes about the *outside world* — job-board fetchability (Indeed, LinkedIn,
Workday behavior), ATS quirks, platform fees or rules, connect prices, which boards syndicate —
drifts and goes stale. Treat every such claim as a **dated prior, not a permanent truth**:

- When you state one, carry a `verified: <date>` and re-check it rather than trusting it blind.
- Where the kit can test live (e.g. the scan's Step 0 reconnaissance), the **live test is the
  source of truth** and overrides any hardcoded list.
- Never present a stale external fact as current. If you can't re-verify, say it's unverified
  and let the user decide.

---

## Additional workflows (optional)

- **Daily batch mode** (find listings, filter many at once, queue for review): see
  `references/daily-batch-workflow.md`.
- **Automated job scan** (scheduled morning pass over fetchable boards): see
  `references/job-scan-spec.md`.
- **Browser form-fill** (auto-fill applications in Chrome, stop at submit): see
  `references/browser-fill-workflow.md`.
