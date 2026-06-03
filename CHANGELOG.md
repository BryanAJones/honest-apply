# What's New — honest-apply

Plain-English notes on what changed in each version, newest first. No jargon — this is for
the people using the kit, not just the people building it.

> Versioning starts with this file. Everything the kit shipped before today is treated as the
> **0.1.0** baseline; the changes below are **0.2.0** and **0.3.0**.

---

## 0.3.0 — June 3, 2026 · "Freelance track"

The kit now does **freelance gig work**, not just full-time jobs.

**You pick a track at setup.**
The interview asks whether you're after **employment, freelance, or both**. For freelance, it
collects your services and rates, the platforms you're targeting, and a **proof ledger** of your
work — and for each piece it pins down the honest stuff: was it solo or a team effort (and what
*you* did), how finished it really is, what you can actually show a stranger, and whether it's
even OK to make public.

**A "where do I start?" step.**
A new step (`job-application-profile`) tells you **which platform to start on**, based on your
real profile — a designer gets pointed at Contra/Dribbble, a fractional PM at fractional boards,
a new builder at Wellfound + small trial gigs — instead of everyone defaulting to Upwork and
burning money bidding blind. Then it writes your profile into each platform's exact fields
(Upwork's short title + two specialized profiles, Contra's portfolio-forward layout, etc.).

**A gig flow that respects your money.**
Paste an Upwork/Contra gig and, instead of "should I apply," you get **"is this even worth the
cost to bid?"** (SPEND/SKIP) plus a short, specific proposal. On Upwork — where every bid costs
real money — talking you out of the bad ones is the whole point.

**Built for starting from zero.**
Cold-start mode for brand-new freelancers (bid a little lower to earn your first reviews, always
labeled), a **paid-trial** default when you have no reviews to show yet, and platform-fee facts
that carry a "checked on" date and get re-verified instead of trusted forever.

*This is the track that was "designed, not yet built" in 0.2.0 — now built.*

---

## 0.2.0 — June 3, 2026 · "The honesty hardening"

This release closes a whole category of accidental over-claiming that the kit used to miss.
The short version: it's now much harder to say something flattering that isn't quite true.

**Your drafts can't quietly oversell anymore.**
The most common accidental lie isn't a big one — it's *rounding up*. Calling a project "live"
or "in users' hands" when it's really just deployed with nobody using it yet. Or writing "I
built it" for something a team built. The kit now catches both:
- The writing rules flag "live / shipped / launched / users love / customers" unless there's a
  real number to back it up.
- The setup interview now asks, for every project, two new questions: **was it solo or a team
  effort** (and if a team, what *specific* part was yours), and **how far along is it really**
  (just a prototype? deployed but no users? live with real users? shipped at scale?). Your
  drafts can never claim more than that.

**It won't let you link something embarrassing.**
New rule: never point a hiring manager or client at a link, demo, or product name without first
confirming it actually loads well for a stranger — not a login wall, an empty page, or an old
name you've since changed. A link to a broken or hollow page is worse than no link.

**Facts about the outside world now come with a "checked on" date.**
Things like which job boards block automated checking change over time. The kit used to state
them as permanent truth. Now they carry a "verified on" date, and a live check always beats an
old hardcoded note — so the kit won't act on stale information about the world.

*Files touched: the writing-style rules, the profile template, the setup interview, the main
skill, and the job-scan spec.*

**Also designed here, shipped in 0.3.0:** the **freelance track** (gig work on Upwork, Contra,
Wellfound, fractional boards) was designed during this release and built out in 0.3.0 above.

---

## 0.1.0 — baseline

The kit as it shipped before this changelog existed: the setup interview
(`job-application-init`), the per-listing apply pipeline (fit-filter → tailor → anti-slop → log),
the daily batch mode, and the supporting reference files.
