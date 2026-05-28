# job-application-kit

A plug-and-play job application skill for [Claude Code](https://claude.com/claude-code). One
interview personalizes it to you; from then on it filters listings for fit, drafts tailored
materials only when the role passes, runs an anti-slop check before showing you anything,
and logs every application to a tracker.

The kit's job is **not** to maximize applications. It's to apply to the right roles with
materials that survive a skeptical hiring manager. A `SKIP` verdict — talking you out of a
bad-fit application — is a success, not a failure.

---

## What's in the box

Three skills:

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
  Code's `/schedule` or a Cowork recurring task.

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

This repo is structured as a Claude Code plugin. Install it however you usually install
plugins (e.g. via `/plugin` in Claude Code, or by cloning into your plugins directory):

```bash
git clone https://github.com/BryanAJones/honest-apply.git
```

If you're not using the plugin system, you can also just drop the three `skills/*`
directories into `~/.claude/skills/` and they'll work.

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
| GitHub Copilot Chat | Workable, awkward | Paste the relevant SKILL content into `.github/copilot-instructions.md` for workspace-level always-on instructions. Lose the multi-skill structure (init / per-listing / daily); collapses to one big instruction blob. |
| Windsurf, Continue, others | Workable | Same pattern as Cursor — wherever the harness loads persistent instructions, point it at the SKILL content. |

**The hard dependency on Claude is the install, not the brain.** If you'd rather
use a different harness, the pipeline still works — you'll just lose the
trigger-phrase auto-activation and the scheduled-task walkthrough. Everything
else (resume intake, fit filter, anti-slop, HTML output) is harness-agnostic
because it's all prompt-level instruction.

## First-time setup (run once)

**Have your current resume ready** — paste-able or as a file. The interview starts by
reading it and uses it to ask sharper, more direct follow-ups instead of generic intake
questions. You can skip the resume, but the resulting profile will be noticeably shallower.

In a Claude Code session, from the directory where you want your career profile and tracker
to live (e.g. `~/job-search/`), say:

> "Set up the job application kit."

That triggers the `job-application-init` skill. It will walk you through the interview and,
at the end, write two files into your current directory:

- `career-profile.md` — your single source of truth. Edit it freely; the runtime always
  re-reads it.
- `tracker.csv` — empty (header row only). The runtime will append to it.

**Back up `career-profile.md`.** It's the artifact the entire kit depends on. Commit it to
a private repo, drop it in a password manager attachment field, whatever — just don't lose it.

## Daily use

From the same directory (so the skill can find `career-profile.md` and `tracker.csv`),
paste a job listing into Claude Code:

> Here's a role: [paste]
> Should I apply?

The `job-application` skill will activate, run the pipeline, and either:
- Tell you SKIP and why (and stop), or
- Tell you APPLY/STRETCH, draft tailored materials, run anti-slop, and log the row.

You can also ask for just one piece ("just the cover letter," "just bullets," "filter only,
no draft").

## See an example

`examples/career-profile.example.md` — a fictional finished profile (Maya Chen, a
backend engineer doing a lateral move into dev-tools). Shows what a completed
profile looks like and how the lateral-move branch of the Cover Letter Spine plays
out. Don't copy it verbatim — your interview will produce something different
because it pushes on YOUR resume and YOUR situation.

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
