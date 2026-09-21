---
name: file-this-chat
description: Files the current work under its subject the moment the subject is known, using a topic prefix on whatever gets a name - session title, artifact, doc, or file. Use at the very START of any session, and any time the user names a project - Twenty & Out, T&O, BuildFlow, NotaVault, Creator Brain, FourCount, Foursquare, BreathWorks, VA, a job application, Ironbridge, IBSG - or says "file this", "where am I", "what is this", "where did we leave off", "what was I working on", or starts describing work without saying which project it belongs to. Also use when a title no longer matches what the work became. Works in Claude Code, Claude chat, Cowork/Dispatch, and Claude Design.
---

# File this

Make the sidebar readable at a glance, at the moment work starts, not
in a cleanup pass three days later.

**The title is the filing system.** Tags are invisible to her. Folders
do not exist. The only thing she sees in a list is the name. So the
subject goes in the name, every time, on every surface.

## The convention

    PREFIX — what this is actually about

Uppercase prefix, space, em dash, space, then a short specific phrase.
Prefixes sort together, so any alphabetical list groups itself.

Put the prefix on **anything that gets a name**: session titles,
artifact titles, doc titles, canvas names, file names, Notion pages.

## The registry

Use ONLY these. Never invent one without asking.

| Prefix | Covers |
|---|---|
| `T&O` | Twenty & Out — veteran apparel, Shopify, Printful, booth, social |
| `BUILDFLOW` | BuildFlow Pro app, its connectors, App Store work |
| `NOTAVAULT` | NotaVault, remote notary business |
| `FOURCOUNT` | FourCount breathing app, formerly "BreathWorks" (she also says "Foursquare" — same thing) |
| `CREATORBRAIN` | Creator Brain |
| `VA` | VA claims, benefits, appeals, medical equipment |
| `JOBS` | applications, resumes, cover letters, unemployment |
| `IBSG` | Ironbridge Strategy Group, outreach, landing page |
| `JARVIS` | assistant setup, skills, session hygiene, morning brief |
| `IDEA` | a venture with no home yet — revisit within two weeks |

## What to do, by surface

Do the most you can on whatever surface you are on. Never skip the
naming because the automation is unavailable.

**Claude Code (web, CLI, or teleported)**
1. `mcp__Claude_Code_Remote__get_session` with no `session_id` returns
   THIS session. Take its `id`.
2. `mcp__Claude_Code_Remote__set_session_title` with the prefixed name.
3. `mcp__Claude_Code_Remote__set_session_tags`: one `project:<lowercase>`
   plus `status:blocked` or `status:ready`.
4. Do this BEFORE the substantive work.

**Claude chat (claude.ai)**
You cannot rename the conversation. So:
1. Say the name in ONE line at the top of your first reply:
   `Filed as: T&O — booth inventory`
2. Prefix every artifact and doc you create in that conversation.

**Cowork / Dispatch**
Prefix every file and output you produce. If a session title is
settable, set it. If not, name the folder or file with the prefix.

**Claude Design**
Prefix the canvas and artboard names.

## The log

Append one line to `LOG.md` in the ai-memory-vault repo, or the repo
in play, or tell her the line to paste if you have no file access:

    2026-09-21 | T&O | booth inventory tracker | blocked: need shirt counts

One line per session, newest at the bottom.

## When she asks where she left off

Read `LOG.md`. Give her the last few lines for the subject she asked
about, then **one** next action.

Never tell her to scroll back through a conversation. That is the
exact thing that cost her an afternoon and made her furious, with
cause.

## Rules

- **Name it before working.** Always. Work renamed "later" never is.
- **One subject per session.** If it drifts, finish the thought, then
  tell her the rest belongs in a new chat and name it for her.
- **Never invent a prefix.** Ask in one line, then add it to the table.
- **Never report the filing as an accomplishment.** File it and get on
  with the real work. She wants her afternoon back, not a status
  update about her filing system.
