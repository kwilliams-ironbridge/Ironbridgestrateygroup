# Session Cleanup Prompt

Paste this into any Claude Code session when the sidebar gets out of hand.
Run it every few weeks — sessions pile up fast.

---

Clean up my Claude Code sessions. The sidebar is out of control.

Use exactly these tags. Do not invent new ones:
  project:<name>   one per session, reuse existing names
  status:blocked   waiting on me
  status:ready     finished, nothing owed

Then:
1. Tag every untagged session.
2. Fix titles that are dates, machine names, duplicates,
   or no longer describe the work. Check the session's
   recent artifacts before renaming — old titles go stale.
3. Merge any duplicate or competing tags into the list above.
4. List archive candidates and ask me once before archiving.

Done = every active session has one project tag and one
status tag, and no two sessions share a title.

Report back with counts per tag and ONE thing to do next.
Not a list.

---

## Why each part is there

**Pinned tag vocabulary.** Without it the scheme drifts. It already
happened once: two sessions were writing `status:blocked` and
`needs:input` for the same thing, plus `project:jobs` and
`project:jobsearch` side by side.

**Check artifacts before renaming.** A session's title is set early
and the work moves on. One session still called "Google developer
documentation style" was actually about email routing; another kept
an August title while holding this month's booth prep.

**Ask once before archiving.** Otherwise you get a model that either
archives nothing useful or hides work you still need. Archiving is
reversible, but you should be the one deciding.

**One thing, not a list.** Lists stop me cold.

## Tag vocabulary in use

    project:ventures     business ideas, side projects, shops
    project:buildflow    the contractor app + its connectors
    project:ironbridge   Ironbridge Strategy Group
    project:va           VA claims, benefits, appeals
    project:jobs         applications, resumes, unemployment
    project:jarvis       assistant setup, morning briefs, infra
    project:notavault    NotaVault

Add a new `project:` only for a genuinely new area of life,
not for each new session.
