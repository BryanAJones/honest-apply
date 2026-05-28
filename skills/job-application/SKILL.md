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

## The pipeline — always in this order

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

Append a row to `tracker.csv` in the user's working directory:

```
company, role, fit_verdict, predicted_rejection_reason, status, date_applied, followup_date, notes
```

Defaults:
- `status`: "Drafted" (the user will update to "Submitted" when they actually apply)
- `date_applied`: today
- `followup_date`: today + 7 days
- `notes`: which asset mapped, any flags worth remembering

---

## Tone calibration

The user wants truth over comfort. If a role is a bad fit, say so plainly. If the materials
came out weak, fix them and say what was weak — don't pad with encouragement. The kit's
value is the friction it adds against shipping mediocre applications, not the volume of
applications it produces.

---

## Additional workflows (optional)

- **Daily batch mode** (find listings, filter many at once, queue for review): see
  `references/daily-batch-workflow.md`.
- **Automated job scan** (scheduled morning pass over fetchable boards): see
  `references/job-scan-spec.md`.
- **Browser form-fill** (auto-fill applications in Chrome, stop at submit): see
  `references/browser-fill-workflow.md`.
