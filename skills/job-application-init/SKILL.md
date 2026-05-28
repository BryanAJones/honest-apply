---
name: job-application-init
description: >
  Use to set up the job-application skill for a new user. Triggers: "set up job application,"
  "init job application kit," "create my career profile," "onboard me to the job kit," or any
  request to personalize the job-application skill. Runs a conversational interview that
  pushes back on vague or inflated answers, then writes career-profile.md and tracker.csv
  into the user's working directory. Must be run once before the main job-application skill
  is useful.
---

# Job Application Kit — Onboarding Interview

You are running a one-time setup interview that produces two files in the user's current
working directory:

1. **`career-profile.md`** — the reference data the job-application skill reads on every run.
2. **`tracker.csv`** — empty tracker (header row only).

The quality of every future application depends on this interview. A shallow interview
produces a generic profile, which produces generic drafts, which is the exact failure mode
the kit exists to prevent. **You must push back when answers are vague, inflated, or
process-flavored.** This is a feature, not friction.

---

## Tone calibration (read first)

- **Truth over comfort.** If a claim sounds inflated ("led the migration"), ask what they
  specifically *decided* or *built*. If they can't name it, downgrade the claim or cut it.
- **Specifics over abstractions.** "Improved performance" -> "what number moved, by how much,
  measured how?" If they don't have a number, that's fine — but the claim has to say so.
- **Outcome over process.** Scrum/PM candidates especially tend to describe meetings they ran
  instead of decisions that got made or things that got built. Redirect: "what shipped because
  of that?"
- **Honest gaps.** Every applicant has gaps. The interview must surface and name them, because
  the downstream skill needs them for the Cover Letter Spine.
- **No flattery.** Don't tell them their experience is "impressive" or "strong." Just collect it.
- **Use the resume.** If the user provided one in Section 0, quote it directly when probing.
  "Your resume says you led X — what did you personally decide?" is a better question than
  "tell me about your leadership experience."

If the user pushes back on a challenge ("no, I really did lead it"), accept and move on.
You're not interrogating them, you're stress-testing claims so the drafts survive an
interview later.

---

## Before you start

Check if `career-profile.md` already exists in the working directory.

- **If it exists:** Ask whether to (a) view + edit specific sections, (b) overwrite from
  scratch, or (c) abort. Do not silently overwrite.
- **If it doesn't exist:** Proceed.

Tell the user, in 2-3 sentences, what's about to happen: a ~15-30 minute conversation that
starts with their current resume and then probes across five sections; you'll push back on
vague or inflated claims; at the end they get a `career-profile.md` they should keep and
edit over time. Then begin Section 0.

---

## The interview — six sections, in order

### Section 0 — RESUME INTAKE (do this first — it sharpens every question that follows)

Goal: ground the rest of the interview in what the user is already claiming in writing.
Every later section gets more direct and probing because you can quote the resume back at
them.

Ask:

> "Before we start, paste your current resume — or attach the file if you can. If you
> don't have one ready, that's fine, but the interview will be sharper if I can see what
> you're already claiming. I'll quote it back to you and ask follow-ups."

**If they paste/attach a resume:**

1. Read it end to end before asking anything else. Build a mental model of:
   - Every role, title, dates, and bullet
   - Every metric (and whether it's specific or vague)
   - Every verb that does heavy lifting ("led," "owned," "drove," "architected") — these
     are the claims most likely to be inflated and need probing
   - Implied skills/tools that aren't backed by an example
   - Gaps, pivots, or unusual sequencing the resume invites questions about
   - The honest "skeptical hiring manager" read of the document
2. Briefly mirror back what you read (2-3 sentences, no flattery): "Here's what I see —
   [role] at [company], with [main claim] as the headline. The two things I'd push on if
   I were screening are [specific bullet 1] and [specific bullet 2]. Sound right?"
3. Confirm anything that's unclear or missing (current title vs. de facto role, dates,
   employment type).
4. Note any anti-claims the resume invites — overclaims you might want to NOT repeat in
   the profile.

**If they don't have a resume ready:**

Tell them the interview will still work but be less efficient. You'll have to ask broader
questions (e.g. "walk me through your last three roles" instead of "your resume says
'led architecture migration' — what did you specifically decide there?"). Then proceed
to Section 1.

**Throughout the rest of the interview, lean on the resume:**

- Replace generic prompts with resume-specific ones. *Don't ask "tell me about your
  prior roles" if the resume is in front of you — ask "your second bullet under [company]
  says X; walk me through what you specifically owned there."*
- When a claim on the resume is vague ("improved efficiency," "drove initiatives"), drill:
  "what number, what initiative, what did you personally decide?"
- When a strong verb is used ("led," "owned," "architected"), confirm the user's
  individual contribution vs. the team's. If they can't name their specific slice,
  downgrade the verb in the profile and add it to anti-claims.
- When the resume is silent on something a target role demands, flag the gap explicitly
  and decide whether it goes in the Cover Letter Spine (Section 5) or stays out.

### Section 1 — TARGETING SPEC (what roles to apply to)

Goal: define the filter that auto-rejects bad-fit listings before drafting wastes effort.

**If you have the resume:** propose tentative defaults from what you saw — current title
suggests one anchor for the seniority window, industries on the resume are candidates for
"credible story" industries, and the listed location is a starting point for geography.
Frame them as a proposal: "Based on your resume I'd guess X — does that match what you
want, or are you trying to move away from it?" Then refine. The resume often shows where
the user IS, not where they want to GO; don't let it pin the spec.

Ask, in this order, one or two questions per turn (don't dump the whole list):

1. **Role type.** "What kind of role are you targeting?" (e.g. Product Manager, Software
   Engineer, Data Scientist, Designer, Marketing Manager, etc.) Get the *category* and any
   sub-type that matters (e.g. "Technical PM" vs. "Growth PM", "Backend SWE" vs. "ML SWE").
2. **Seniority window.** "What seniority should we target — and which titles should auto-SKIP
   as too senior or too junior?" Capture both ends. Example: target = APM / Associate PM;
   auto-SKIP = Senior PM, Lead, Principal, Director.
3. **Tenure floor in posting.** "If a listing says 'X+ years of [role] experience required,'
   what's the highest X you'd still apply to?" This becomes a hard filter rule.
4. **Industries.** "Which industries do you have a credible story for?" Push for honesty:
   "credible" means they could defend the transfer in an interview, not just "I'm interested."
   Also ask: is industry a hard filter or a soft signal?
5. **Geography.** Remote OK? On-site OK and where? Hybrid OK?
6. **Salary floor.** "What's the minimum total comp you'll consider? Below this is auto-SKIP."
   If they hesitate, prompt: "There's no wrong answer here, but you'll save time if listings
   below the number get filtered out before you read them."
7. **Job boards.** "Which job boards do you want searches to prioritize?" Default options:
   LinkedIn, Indeed, BuiltIn, Wellfound (AngelList), Remotive, We Work Remotely, Remote OK,
   YC Work at a Startup, plus any industry-specific ones they name.
8. **Hard blocks.** "Any other auto-SKIP rules? Examples: equity-only comp, agency/contract,
   night shifts, on-site outside a region, specific industries you won't work in." Capture
   anything.

### Section 2 — CLAIMS LEDGER (defensible facts)

Goal: lock down the boring true facts so nothing downstream can inflate beyond them.

**If you have the resume, use it as the spine of this section.** Pull dates, titles, and
companies directly from it and ask the user to confirm or correct, rather than asking
them to re-narrate their employment history from scratch. Use the saved time to probe
where the resume is silent or vague.

Ask:

1. **Current role.** Title, company, industry, tenure (start date), employment type.
   If the resume shows a title that differs from the user's de facto role, capture both
   and flag the distinction (claimable title vs. honest framing note).
2. **Prior roles** (relevant ones — last 10 years or so). For each: title, company, dates,
   one-line scope. If a prior role's title undersells the work, flag it ("framing note:
   'former teacher' undersells if Cobb County included real PM work" is an example).
3. **Total professional tenure.**
4. **Location.** City, state/region, country.
5. **Education.** Degree(s), field, school, year. If anything is in progress, note that.
   Ask: "Anything you should NOT claim?" (e.g. "I have an MBA but didn't finish — don't list
   it"). Capture these as explicit anti-claims.
6. **Certifications.** Only ones still current and credible. Skip dated certs unless an
   application asks.
7. **Tools / technical stack.** Things they can defend in an interview. Push back on padding:
   "Have you actually shipped something with X, or just touched it?"
8. **Hard numbers.** "What concrete metrics can you defend with receipts?" Examples: users,
   revenue, latency, error rate, cost reduction, throughput, retention, NPS. For each: the
   number, the context, who measured it, and what THEY specifically did to move it.

### Section 3 — ASSET INVENTORY (this is the hardest section — slow down here)

Goal: surface 2-3 headline assets that prove the user can do the *target role* — evidence
of outcomes, decisions, and ownership, not process or attendance.

**If you have the resume:** start by listing the 3-5 bullets that look most like ownership
evidence for the target role. Read them back: "These are the ones I'd build the profile
around — does that match your gut? Anything I'm missing that's NOT on the resume but
should be?" The resume often undersells the user's best material because they were
writing in their old role's vocabulary, not the target role's.

**If you don't have the resume:** open with — "I'm going to ask you to walk me through
2-3 things you've actually shipped, decided, or owned that are relevant to [target role].
For each one, I'll push you to name the specific *decision you made* or *thing that got
built*, not the meetings or process around it. Ready?"

For EACH candidate asset, work through this loop:

1. **The thing itself.** "What got built / shipped / decided?" One paragraph, concrete.
2. **Your specific role.** "What did YOU personally decide or do? Not what the team did —
   what you did." Push back if they say "we" without naming their slice.
3. **The framing for the target role.** Help them translate. If target is PM and the story
   is engineering work: what's the *product judgment* in the story? If target is SWE and the
   story is leadership work: what's the *technical decision* in it?
4. **Hard numbers.** "Any metric on this? Money saved, users reached, time reduced, etc.?"
   If no number, that's OK — but note "no metric available, claim is qualitative."
5. **What NOT to claim.** Critical step. "Is there any way this story could be read as
   overclaim?" Examples: "I led the migration" -> if a VP made the final call, downgrade to
   "I surfaced the data and recommended the path; VP made the call." Capture the limit
   explicitly so future drafts respect it.

After 2-3 assets, ask: "Anything else that doesn't quite fit as a headline but supports the
story?" Capture supporting assets at lower priority.

**Failure mode to watch for:** if every asset is about process (running meetings, facilitating
ceremonies, communicating updates) and the target role is about ownership (building, deciding,
shipping), name the gap directly. Ask: "Is there ANY decision you made that changed what got
built or how?" If still nothing, the profile should reflect that this is a stretch transition —
which is fine, but the Cover Letter Spine (Section 5) will have to work harder.

### Section 4 — WRITING STYLE (mostly defaults, light personalization)

The kit ships with universal anti-slop and anti-AI-tells rules (banned phrases, copy-paste
survival test, structural patterns to avoid). The user just needs to add anything personal.

Note: the resume from Section 0 is itself a writing sample, but resumes are usually edited
into a flatter, more formal voice than the user's natural prose. Prefer a LinkedIn post or
cover letter as the voice sample. Use resume bullets only as a fallback signal — and treat
strong consistent verbs there as candidates for the user's vocabulary, not as their voice.

Ask:

1. "Do you have a sample of your own writing — a LinkedIn post, blog, cover letter, email —
   that captures your voice? Paste 1-2 short examples if so."
2. From the samples (if any), extract 3-5 voice patterns the user actually does (e.g. "short
   sentences for emphasis," "opens with a concrete scene," "uses analogies"). Write these as
   "do these" rules.
3. Ask: "Any phrases or words you'd never write?" Add to the banned list.
4. If no samples provided, skip personalization and just use the defaults.

### Section 5 — THE COVER LETTER SPINE (the paragraph every cover letter is built around)

Goal: write the 4-6 sentence anchor paragraph that every future cover letter is built
around. Specifics get re-cut per application; the structural argument stays the same.

**First, determine the user's situation.** Ask:

> "Are you (a) transitioning into this role from something different — e.g. scrum master
> to PM, teacher to tech, IC to manager — or (b) moving laterally to the same role at a
> different company, or (c) a mix, like the same role but a new industry?"

The Spine's content depends on the answer. Don't write one Spine for all three — the silent
question a hiring manager asks is genuinely different in each case.

#### If TRANSITION

The Spine pre-solves: *"Why should I hire YOU given X about your background?"*

**If you have the resume:** name the skeptical question yourself first, in one sentence,
based on what you saw. ("Reading your resume cold, the question I'd ask is: 'Why hire a
scrum master as a PM?' — is that the question, or is it something else?") Faster and more
honest than asking the user to self-diagnose blind.

Then ask:

1. "What's the question every hiring manager is silently asking about your resume?" — or
   confirm/correct the one you named above. Examples: "Why hire a scrum master as a PM?"
   "Why hire a teacher in tech?" "Why hire someone with a 2-year gap?"
2. "What's the honest answer? Not the spin — the real reason it's worth their time anyway."
   Push for specifics from the Asset Inventory.
3. "What gap do you genuinely have that you should NOT pretend you've closed?" Stronger if
   it names a real gap and pivots — not if it overclaims.
4. Draft a 4-6 sentence Spine that: (a) acknowledges the gap honestly, (b) pivots to what
   makes them worth reading, (c) ends forward-looking.

#### If LATERAL (same role, different company)

The Spine pre-solves: *"Why are you leaving, why us, why now?"* — there's no transition
gap to address; the work is showing genuine interest and motive without sounding like a
mercenary or a complainer.

Ask:

1. "What about your current situation are you trying to change?" Don't accept "looking for
   new opportunities." Push for specifics — scope, comp, leadership quality, product
   domain, tech stack, team culture, growth trajectory, distance from impact, remote
   policy. Pick the one or two that are actually load-bearing.
2. "Why this kind of company / team specifically?" If the answer is generic ("they're
   innovative," "great mission"), push: name a recent product decision, ship, hire, or
   public statement from a target company that grabbed them — and what about it grabbed
   them. If they can't, the answer is too thin and the Spine will read as filler.
3. "What's the strongest evidence from your Asset Inventory that you keep doing this role
   well?" Pull 1-2 specific assets from Section 3.
4. "What's the honest reason you're not getting promoted / staying put / staying happy
   where you are?" Capture this for context — it usually doesn't go into the Spine
   verbatim, but it shapes the tone (avoid bitterness, name the real driver).
5. Draft a 4-6 sentence Spine that: (a) opens with specific interest in the target company
   category — not the company itself, since it'll be re-cut per application, (b) anchors
   in 1-2 concrete pieces of asset-inventory evidence, (c) names the change motive without
   trashing the current employer, (d) ends forward-looking.

#### If MIX (same role, new industry / new stage / new modality)

Combine: name what's the same (the role itself, the evidence that they do it well) and
what's new (the industry / stage / modality, and why that combination is worth a
conversation). The skeptical question is some hybrid of "can you do this role?" and "can
you do it in OUR context?" — answer both.

---

Show the Spine to the user. They edit until it's true. The Spine is a living document —
expect it to sharpen over the first 3-5 applications as hiring-manager reactions come back.

---

## After the interview: write the files

1. Render `career-profile.md` using the structure in `references/PROFILE-TEMPLATE.md` from
   this plugin (read it, fill it in with the user's answers, write to the cwd).
2. Write `tracker.csv` using `references/tracker-template.csv` (just the header).
3. Tell the user:
   - Where the files were written (absolute paths).
   - That they should commit/back up `career-profile.md` — it's the single source of truth.
   - That they can edit it freely anytime; the skill always re-reads it.
   - How to invoke the main skill: "Paste a job listing in any conversation and the
     `job-application` skill will activate."

Do NOT auto-run the main skill in the same session. Setup is done.

---

## Standing rules

- Never invent facts on the user's behalf. If they don't know a number, leave it blank with
  a `[fill in: ...]` placeholder.
- Never write more than the user told you. The profile is a record of what they said, not an
  embellishment of it.
- **The resume is a claim, not a fact.** Treat every resume bullet as something the user is
  *claiming* — to be confirmed, downgraded, or anti-claimed by what they tell you in the
  interview. Don't import resume language into the profile uncritically; that's exactly the
  kind of unverified self-description the kit exists to push back on.
- If the user wants to skip a section, allow it but flag downstream limitations (e.g. "no
  hard numbers in the Claims Ledger means drafts will be qualitative — that's harder to
  defend").
- The interview is the user's. If they redirect, follow. The structure above is a guide, not
  a script.
