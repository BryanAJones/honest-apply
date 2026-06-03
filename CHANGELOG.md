# What's New — honest-apply

Plain-English notes on what changed in each version, newest first. No jargon — this is for
the people using the kit, not just the people building it.

> Versioning starts with this file. Everything the kit shipped before today is treated as the
> **0.1.0** baseline; the changes below are **0.2.0**.

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

**Also in progress (designed, not yet built):**
A **freelance track** — applying to gig work (Upwork, Contra, Wellfound, fractional boards), not
just full-time jobs. It adds a short-proposal writer, a "is this gig even worth the cost to
apply?" filter, a recommender that tells a new freelancer *which platform* to start on, and a
profile builder. The full design is written up in `DESIGN-freelance-track.md`. None of it is in
the skills yet — it's the next thing to build.

---

## 0.1.0 — baseline

The kit as it shipped before this changelog existed: the setup interview
(`job-application-init`), the per-listing apply pipeline (fit-filter → tailor → anti-slop → log),
the daily batch mode, and the supporting reference files.
