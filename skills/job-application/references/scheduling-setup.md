# Scheduling the Daily Batch

The daily skill (`job-application-daily`) is designed to run from your job-search
folder, where `career-profile.md` and `tracker.csv` live. To get a daily queue
waiting each morning without triggering it manually, set up a recurring task in
one of the environments below.

## Pick your path

| Environment | Persistent? | Setup difficulty | Notes |
|---|---|---|---|
| Windows Task Scheduler | Yes | Low | Best for Windows users. Runs in your account so it can read your local profile. |
| macOS / Linux cron | Yes | Low | One crontab line. Same model as Task Scheduler. |
| Cowork recurring task | Yes | Low (UI) | Needs `career-profile.md` accessible in the Cowork workspace. |
| `/loop` in a session | No — session-bound | Lowest | Good for trying it for a day; doesn't survive session close. |
| Claude Code `/schedule` | Yes, but | N/A | **Not recommended.** `/schedule` creates remote agents that can't read your local files. Skip unless you've staged your profile somewhere a remote agent can reach. |

## Honest limits (read first)

- **Unattended runs only reach what your search tools can fetch without a login.**
  Remotive, We Work Remotely, YC, HN's "Who's Hiring," static company career
  pages — those work. LinkedIn, Indeed, and most ATS pages (Workday, Greenhouse)
  need a supervised session with you watching, not a cron.
- **The scheduled task runs in YOUR account.** It can read every file in your
  job-search folder, including `career-profile.md`. Keep that folder out of
  shared drives.
- **The output is `daily-review.html` in your job-search folder.** Open it in a
  browser to act on the queue. Nothing is submitted automatically.
- **If `claude` isn't on your PATH, use the full path** in the scheduled command.
  Check with `where claude` (Windows) or `which claude` (macOS/Linux).

---

## Windows Task Scheduler

The simplest setup uses a small batch wrapper so the task knows the working directory.

### Step 1 — Write `daily-batch.bat` in your job-search folder

```bat
@echo off
cd /d "C:\Users\<you>\job-search"
claude -p "Run my daily honest-apply batch"
```

Replace the path with your actual job-search folder.

### Step 2 — Register the task

Open PowerShell and run:

```powershell
schtasks /create /tn "HonestApply Daily" `
  /tr "C:\Users\<you>\job-search\daily-batch.bat" `
  /sc daily /st 06:30 /f
```

That schedules a daily 6:30 AM run. Adjust `/st` for a different time.

### To remove later

```powershell
schtasks /delete /tn "HonestApply Daily" /f
```

### GUI alternative

If you'd rather use the Task Scheduler app: New Basic Task → Daily → set time →
Action: Start a program → Program: `C:\Users\<you>\job-search\daily-batch.bat`.
Optional but recommended: in the task's Properties → General, check "Run whether
user is logged on or not" only if you need it; otherwise leave default so it
runs in your user context.

---

## macOS / Linux cron

One crontab line. Run `crontab -e` and add:

```
30 6 * * * cd ~/job-search && claude -p "Run my daily honest-apply batch"
```

That's 6:30 AM daily. Tweak the cron expression for a different time.

If `claude` isn't in cron's PATH (common — cron has a minimal environment), use
the full path:

```
30 6 * * * cd ~/job-search && /usr/local/bin/claude -p "Run my daily honest-apply batch"
```

Find the full path with `which claude`.

---

## Cowork recurring task

In Cowork:

1. Make sure your `career-profile.md` is in a workspace folder the scheduled
   agent can access (upload it if needed, or create the profile inside a Cowork
   session in the first place).
2. Create a new recurring task.
3. Set the working directory to that folder.
4. Set the prompt to: `Run my daily honest-apply batch.`
5. Set the schedule (daily, ~6-7 AM is common).
6. Save.

Cowork's exact UI changes over time — if a field above doesn't exist by that
name, the equivalent should be obvious. The two things that matter are: the
prompt and the working directory.

---

## `/loop` (temporary, for testing)

If you want to try the daily flow without a persistent schedule:

1. Open a Claude Code session in your job-search folder.
2. Run: `/loop 24h Run my daily honest-apply batch`
3. The batch runs every 24 hours as long as the session is open.

This is the lowest-friction way to verify the flow works before committing to a
scheduled task. It does NOT persist across session close.

---

## Verifying the schedule works

After setting up:

1. Trigger the task manually once (Task Scheduler: right-click → Run; cron: run
   the command from a shell directly; Cowork: trigger the recurring task once).
2. Confirm `daily-review.html` appears in your job-search folder.
3. Open it in a browser, check that listings are filtered and drafts are present.
4. If it failed silently, check the task's last-run status (Windows: Task
   Scheduler History; macOS/Linux: `grep CRON /var/log/syslog`; Cowork: task
   logs in the UI).
