#!/usr/bin/env python3
"""Build self-contained Claude Cowork skill ZIPs from skills/.

Claude Cowork loads skills as individual ZIP uploads (Customize -> Skills): each ZIP
is one skill folder as its root, containing a SKILL.md. Cowork does NOT read
.claude-plugin/plugin.json. And unlike Claude Code's single-plugin layout — where all
four skills sit side by side and can reach each other with ../ paths — each Cowork
skill folder is isolated and must be fully self-contained.

This script makes them so, without duplicating anything in the repo (the single source
of truth stays in skills/):
  - bundles the shared references/ into every skill folder, and
  - rewrites the daily skill's ../job-application/... cross-skill paths.
Then it zips each folder (spec-compliant forward-slash entries, folder-as-root).

Output goes to cowork-build/, which is gitignored — it's generated, not source. Attach
the four zips to a GitHub Release so users download them without cloning.

Usage:  python build-cowork.py
"""
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(ROOT, "skills")
OUT = os.path.join(ROOT, "cowork-build")
SHARED_REFS = os.path.join(SKILLS, "job-application", "references")
SKILL_NAMES = [
    "job-application",
    "job-application-init",
    "job-application-profile",
    "job-application-daily",
]

# The daily skill delegates to the job-application skill through ../ sibling paths that
# resolve in Claude Code's plugin layout but break in Cowork's isolated folders. Point
# file reads at the now-bundled local references/, and turn skill-to-skill references
# into "keep both skills enabled" guidance (Cowork loads every enabled skill's SKILL.md
# into context, so the job-application rules are available without a path).
DAILY_REWRITES = [
    (
        "Read `../job-application/SKILL.md` and `../job-application/references/career-profile.md`\n"
        "(in the user's cwd) before doing anything. The fit filter, anti-slop rules, and writing\n"
        "style all live there. Don't restate them — apply them.",
        "Keep the **job-application** skill enabled alongside this one — its fit filter, anti-slop\n"
        "rules, and writing style are the source of truth, and this skill applies them (when both are\n"
        "enabled, Cowork loads both into context). Read `career-profile.md` from the working directory\n"
        "before doing anything. Don't restate the job-application rules — apply them.",
    ),
    (
        "Run every listing through the fit filter from `../job-application/SKILL.md`. For each:",
        "Run every listing through the fit filter from the **job-application** skill. For each:",
    ),
    (
        "- Draft resume bullets and a cover letter per `../job-application/SKILL.md` (lead with",
        "- Draft resume bullets and a cover letter per the **job-application** skill (lead with",
    ),
    (
        "`../job-application/references/daily-review-template.html` as the structural template.",
        "`references/daily-review-template.html` as the structural template.",
    ),
    (
        "gigs, using the **freelance gig pipeline** in `../job-application/SKILL.md` (SPEND/SKIP +\n"
        "Proposal Spine) and `../job-application/references/platform-economics.md`.",
        "gigs, using the **freelance gig pipeline** in the **job-application** skill (SPEND/SKIP +\n"
        "Proposal Spine) and `references/platform-economics.md`.",
    ),
    (
        "mapping** in `../job-application/SKILL.md` (the 12-column positional layout: `opportunity_type=gig`,",
        "mapping** in the **job-application** skill (the 12-column positional layout: `opportunity_type=gig`,",
    ),
]


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    for name in SKILL_NAMES:
        src = os.path.join(SKILLS, name)
        dst = os.path.join(OUT, name)
        os.makedirs(dst)

        with open(os.path.join(src, "SKILL.md"), encoding="utf-8") as f:
            text = f.read()

        if name == "job-application-daily":
            for old, new in DAILY_REWRITES:
                if old not in text:
                    sys.exit(
                        f"ERROR: rewrite pattern not found in {name}/SKILL.md — the source "
                        f"text changed. Update DAILY_REWRITES.\n--- expected ---\n{old}\n"
                    )
                text = text.replace(old, new)

        with open(os.path.join(dst, "SKILL.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

        # Self-containment: every Cowork skill carries its own copy of the references.
        shutil.copytree(SHARED_REFS, os.path.join(dst, "references"))

        zip_path = os.path.join(OUT, name + ".zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for walk_root, _, files in os.walk(dst):
                for fn in files:
                    full = os.path.join(walk_root, fn)
                    arc = os.path.relpath(full, OUT).replace(os.sep, "/")
                    z.write(full, arc)

        count = len(zipfile.ZipFile(zip_path).namelist())
        print(f"  built {name}.zip ({count} entries)")

    print(f"\nDone. Upload the 4 zips in cowork-build/ via Cowork -> Customize -> Skills.")
    print("Enable job-application alongside job-application-daily (daily applies its rules).")


if __name__ == "__main__":
    print("Building Cowork skill packages from skills/ ...")
    build()
