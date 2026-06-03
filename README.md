# job-application-kit

A plug-and-play job application skill for [Claude Code](https://claude.com/claude-code). One
interview personalizes it to you; from then on it filters listings for fit, drafts tailored
materials only when the role passes, runs an anti-slop check before showing you anything,
and logs every application to a tracker.

The kit's job is **not** to maximize applications. It's to apply to the right roles with
materials that survive a skeptical hiring manager. A `SKIP` verdict — talking you out of a
bad-fit application — is a success, not a failure.

> **New to Claude Code?** It's Anthropic's AI assistant that runs in your terminal (also a
> desktop app and IDE extensions). You need it installed first —
> [claude.com/claude-code](https://claude.com/claude-code). After that, everything in this kit
> happens by **typing plain-English requests** to it. There's no code for you to write, and a
> "skill" is just a set of instructions Claude Code follows when you ask for it by name.

---

## What's in the box

Four skills. The kit covers **both full-time jobs and freelance gig work** (Upwork, Contra,
Wellfound, fractional boards) — the setup interview asks which track(s) you want:

- **`job-application-init`** — one-time onboarding interview. Starts by reading your
  resume, then asks ~30 minutes of questions across five sections (targeting spec,
  claims ledger, asset inventory, writing style, cover letter spine). Writes
  `career-profile.md` into your working directory. It pushes back on vague or inflated
  answers — that's the feature.
- **`job-application`** — the per-listing runtime. Paste a job listing in any
  conversation, it runs the pipeline:
  1. **Fit filter** — scores APPLY / SKIP / STRETCH, names the single most likely reason
     this posting's screener would pass on you.
  2. **Tailor** — only if the role passes, drafts resume bullets and/or cover letter
     pulling from the asset inventory and cover letter spine.
  3. **Anti-slop check** — copy-paste survival test, banned phrases scan, anti-AI
     structural tells. Runs before you ever see the draft.
  4. **Log** — appends a row to `tracker.csv`.
- **`job-application-daily`** — the batched daily flow. Searches the job boards in
  your targeting spec, filters every listing, drafts materials for the passes,
  renders an HTML review document (`daily-review.html`) in your cwd, and logs
  each role. Designed to run manually each morning or on a schedule via Claude
  Code's `/schedule` or a Cowork recurring task. Has a **gig mode** for freelance batches.
- **`job-application-profile`** — *(freelance track)* turns your profile into **publishable
  platform profiles** + a **starting-platform plan**. It runs a recommender (tells a new
  freelancer *which* platform to start on, per wedge, with the cost-to-apply tradeoff —
  not just "default to Upwork"), then renders your profile into each platform's fields
  (Upwork's 70-char title + Specialized Profiles, Contra's portfolio-forward shape, etc.).
  Re-run it anytime your work changes.

For freelance, the per-listing skill paste-a-gig flow swaps the fit-filter for a
**SPEND/SKIP** filter (because each bid has a real cost — Upwork connects are money) and the
cover letter for a short **proposal**. Same honesty discipline throughout: it won't let you
claim a project is more finished than it is, claim solo credit on team work, or link a hollow
page.

It never auto-submits. You review everything.

## Workflow modes

There are two ways to use the kit. Pick whichever fits your job-search rhythm:

### Mode A — Per-listing (the simplest)

You're browsing jobs yourself. When you find one that looks worth it, paste it into
Claude Code:

> *Here's a role: [paste]. Should I apply?*

The `job-application` skill runs the pipeline and either talks you out of it (SKIP)
or drafts materials and logs a tracker row. Closest to a normal Claude conversation.
Good when you're already in the habit of browsing and just want a smarter filter +
draft helper.

### Mode B — Daily batch (the volume mode)

You want filtered listings *found for you* and pre-drafted. Open a session in your
job-search folder and say:

> *Run my daily honest-apply batch.*

The `job-application-daily` skill searches your target boards using whatever search
tools the host environment provides (`WebSearch`, `WebFetch`, Firecrawl, Chrome
DevTools / Playwright MCP, etc.), filters every listing through the fit filter,
drafts the passes, and renders `daily-review.html` — a visual review page with
verdict cards, copy-to-clipboard cover letters, and a "skipped today" list with
reasons.

You open the HTML, decide what to act on, and apply live yourself.

**Scheduling Mode B:**

The init skill ends by offering to set up a schedule for you — Windows Task
Scheduler, macOS/Linux cron, a Cowork recurring task, or a temporary `/loop`
for testing. Pick "schedule it" at the end of the interview and it walks you
through the right one for your setup, generates the wrapper script, and offers
to register the task with one confirmation. You can also do this later — see
`skills/job-application/references/scheduling-setup.md` for the same
instructions in reference form.

**Not** Claude Code's `/schedule` — that creates remote agents that can't read
your local `career-profile.md`. The kit explicitly avoids it.

**Honest limit:** scheduled unattended runs reach only what fetch tools can
pull without a login — RSS/JSON feeds and static pages work, LinkedIn / Indeed /
most ATS pages don't. For hostile boards, open a supervised session.

**Search tools the kit needs (not bundled):**

The kit uses whatever's in the host environment. It does NOT ship its own. You
need at least one of: `WebSearch`/`WebFetch` (built into Claude Code), Firecrawl
skills (resilient extraction), or a browser MCP (Chrome DevTools, Playwright)
for supervised sessions on hostile boards. If nothing is available, the daily
skill stops cleanly and tells you instead of fabricating listings.

## Install

You only do this once. Pick whichever path you're comfortable with.

**Option 1 — as a plugin (recommended):**

1. Download the kit to your machine. In a terminal:
   ```bash
   git clone https://github.com/BryanAJones/honest-apply.git
   ```
2. Open Claude Code and run the `/plugin` command, pointing it at the `honest-apply` folder you
   just downloaded.

**Option 2 — drop-in (if you don't use the plugin system):**

Copy the four folders inside `skills/` into your Claude Code skills folder:
```bash
git clone https://github.com/BryanAJones/honest-apply.git
cp -r honest-apply/skills/* ~/.claude/skills/
```
On Windows, that destination folder is `%USERPROFILE%\.claude\skills\`.

**Check it worked:** start Claude Code and type *"set up the job application kit."* If it begins
asking you interview questions, you're set. If nothing happens, the skills aren't being found —
re-check the folder location above.

## Compatibility

**Primary target: Claude Code** (CLI, desktop app, IDE extensions, Cowork). The
plugin format, auto-discovered skills, and trigger-phrase activation all assume
Anthropic's Skills system.

**Other harnesses — partial:** the *content* is portable (the SKILL files,
templates, and reference docs are just markdown + HTML), but the *packaging*
isn't. Other agentic tools don't have an equivalent of Claude's Skill
auto-trigger, so the user has to point the agent at the files manually.

| Harness | Status | How to use |
|---|---|---|
| Claude Code | First-class | Install as a plugin; skills auto-activate on trigger phrases. |
| Cowork | First-class | Same as Claude Code — uses the same Skills system. |
| Cursor | Workable | Copy `skills/job-application/SKILL.md` and the relevant references into `.cursor/rules/honest-apply.mdc` or `AGENTS.md` so they're always in context. Trigger by saying "use the honest-apply pipeline on this listing." No auto-activation. |
| Codex CLI (OpenAI) | Workable | Point the agent at the SKILL files manually each session: `codex -p "Read skills/job-application/SKILL.md and skills/job-application/references/career-profile.md, then process this listing: <paste>"`. No persistent install. |
| GitHub Copilot Chat | Workable, awkward | Paste the relevant SKILL content into `.github/copilot-instructions.md` for workspace-level always-on instructions. Lose the multi-skill structure (init / per-listing / daily / profile); collapses to one big instruction blob. |
| Windsurf, Continue, others | Workable | Same pattern as Cursor — wherever the harness loads persistent instructions, point it at the SKILL content. |

**The hard dependency on Claude is the install, not the brain.** If you'd rather
use a different harness, the pipeline still works — you'll just lose the
trigger-phrase auto-activation and the scheduled-task walkthrough. Everything
else (resume intake, fit filter, anti-slop, HTML output) is harness-agnostic
because it's all prompt-level instruction.

## First-time setup (run once)

**1. Have your resume ready** — as a file or copy-pasteable text. The interview reads it to ask
sharper questions. You can skip it, but the profile comes out shallower.

**2. Make a folder for your job search.** The kit saves your profile and tracker into whatever
folder Claude Code is running in (this is called your "working directory"). Make or pick one:
```bash
mkdir ~/job-search
cd ~/job-search
```

**3. Start Claude Code in that folder** and type:

> Set up the job application kit.

This starts the `job-application-init` interview. It will first ask whether you're targeting
**full-time jobs, freelance gig work, or both**, then walk you through ~15-30 minutes of
questions. It pushes back on vague or inflated answers — that's the point.

**4. When it finishes, two files appear in your folder:**

- `career-profile.md` — your single source of truth. Edit it anytime; the kit always re-reads it.
- `tracker.csv` — empty for now (just column headers); the kit adds a row per application.

**5. Back up `career-profile.md`.** It's the one file the whole kit depends on. A private repo,
a cloud drive, a password-manager note — anything, just don't lose it.

## Daily use

Always start Claude Code **in the same folder** you set up in, so it can find your
`career-profile.md` and `tracker.csv`.

### Full-time jobs

Paste a listing and ask:

> Here's a role: [paste]
> Should I apply?

The `job-application` skill runs the pipeline and either:
- tells you **SKIP** and why (and stops), or
- tells you **APPLY / STRETCH**, drafts tailored materials, runs the anti-slop check, and logs
  the row.

You can also ask for just one piece — *"just the cover letter," "just bullets," "filter only,
no draft."*

### Freelance gigs

First, build your platform profiles + a starting plan (do this once, then re-run whenever your
work changes):

> Build my freelance profile.

That runs `job-application-profile`: it recommends **which platform to start on** for your
situation, and writes ready-to-paste profiles into `freelance-profiles.md`. Then, for any gig:

> Here's a gig: [paste]. Worth bidding?

You'll get a **SPEND / SKIP** verdict — is it worth the cost to apply (on Upwork, every bid
costs money) — and, if it's worth it, a short tailored proposal.

## See an example

- `examples/career-profile.example.md` — a fictional finished **employment** profile (Maya
  Chen, a backend engineer doing a lateral move into dev-tools). Shows what a completed profile
  looks like and how the lateral-move branch of the Cover Letter Spine plays out.
- `examples/freelance-profile.example.md` — a fictional **freelance** profile (a product/brand
  designer). Shows the freelance sections — the Proof Ledger, rates, and platform plan — filled
  in for a non-developer.

Don't copy either verbatim — your interview produces something different because it pushes on
YOUR resume and YOUR situation.

## Reference docs (for the curious)

Inside `skills/job-application/references/`:

- **`daily-batch-workflow.md`** — the per-phase logic the daily skill executes.
- **`job-scan-spec.md`** — reconnaissance (which boards are fetchable), search-tool
  selection, honest limits.
- **`scheduling-setup.md`** — Task Scheduler, cron, Cowork, and `/loop` setup
  instructions for the daily batch. The init skill walks through these
  interactively; this is the same content in reference form.
- **`daily-review-template.html`** — the structural template for the HTML review.
- **`browser-fill-workflow.md`** — drive a real Chrome to fill application forms,
  stop before submit, never enter sensitive data.
- **`writing-style-defaults.md`** — universal anti-slop and anti-AI-tells rules.
- **`PROFILE-TEMPLATE.md`** — the skeleton the init skill fills in.

## Honest limits

- **The interview is the bottleneck.** A vague profile makes vague drafts. The init skill
  pushes back, but if you breeze through it, the output is on you.
- **Not all job boards are fetchable.** Scheduled scans work on remote-first boards with
  feeds. LinkedIn and Indeed require you to open them yourself.
- **Sensitive data is never autofilled.** SSN, salary expectations, demographic questions,
  work authorization — flagged and left blank for you.
- **You always click submit.** Always.

## Updating your profile

`career-profile.md` is a living document. Edit it directly when:
- You ship something new that should be in the Asset Inventory.
- Your salary floor changes.
- Hiring managers keep asking the same question — sharpen the Cover Letter Spine.
- A claim got pushback in an interview — adjust the anti-claim list.

Re-running `job-application-init` is also fine if you want to redo a section. It will
ask before overwriting.

## License

MIT. See `LICENSE`.

## Acknowledgments

Originally built as a personal skill for a PM job search, generalized into a kit so anyone
can fork it. The pipeline structure (fit-filter -> tailor -> anti-slop -> log) and the
anti-AI-tells list are the core ideas — everything else is connective tissue.
