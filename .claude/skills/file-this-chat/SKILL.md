---
name: file-this-chat
description: Files the current chat under its subject the moment the subject is known, by renaming the session with a topic prefix. Use at the very START of any session, and any time the user names a project - Twenty & Out, T&O, BuildFlow, NotaVault, Creator Brain, Foursquare, VA, a job application, Ironbridge, IBSG - or says "file this", "where am I", "what is this chat", "where did we leave off", or starts describing work without saying which project it belongs to. Also use when a session's title no longer matches what the chat became.
---

# File this chat

Your job is to make the sidebar readable at a glance, at the moment work
starts, not in a cleanup pass later.

The sidebar shows **titles only**. Tags are invisible to the user. So the
title is the filing system. Everything else is bookkeeping.

## The naming convention

    PREFIX — what this chat is actually about

Uppercase prefix, space, em dash, space, then a short specific phrase.
Prefixes sort together alphabetically, so the sidebar groups itself.

## The registry

Use ONLY these prefixes. Never invent a new one without asking first.

| Prefix | Covers |
|---|---|
| `T&O` | Twenty & Out — veteran apparel, Shopify, Printful, booth, social |
| `BUILDFLOW` | BuildFlow Pro app, its connectors, App Store work |
| `NOTAVAULT` | NotaVault, remote notary business |
| `CREATORBRAIN` | Creator Brain |
| `FOURSQUARE` | Foursquare |
| `VA` | VA claims, benefits, appeals, medical equipment |
| `JOBS` | applications, resumes, cover letters, unemployment |
| `IBSG` | Ironbridge Strategy Group, outreach, landing page |
| `JARVIS` | assistant setup, skills, session hygiene, morning brief |
| `IDEA` | a new venture with no home yet — revisit within two weeks |

## What to do

**1. Work out the subject.**
Read what the user just said. If they named a project, use it. If the
repo or artifacts make it obvious, use that. Do not interrogate them.

**2. If you genuinely cannot tell, ask once — and only this:**
"Which one is this: T&O, BuildFlow, NotaVault, VA, Jobs, IBSG, or new?"
One line. Never a paragraph. Never a list of follow-ups.

**3. Rename the session immediately.**
- `mcp__Claude_Code_Remote__get_session` with no `session_id` returns THIS session.
- Take its `id`, then `mcp__Claude_Code_Remote__set_session_title`.
- Do this BEFORE the substantive work, not after. Sessions that get
  renamed "later" never do.

**4. Tag it too, for the record.**
`project:<lowercase>` plus `status:blocked` or `status:ready`.
Tags are invisible in the UI but keep the API queryable. One project
tag per session. Never more.

**5. Log it.**
Append one line to `LOG.md` in the repo root:

    2026-09-21 | T&O | booth inventory tracker | blocked: need shirt counts

Create the file if missing. One line per session, newest at the bottom.
This is the file that answers "where did we leave off" — not the chat
history, which is exactly what keeps failing her.

## When the user asks where they left off

Read `LOG.md`. Give them the last three lines for the subject they
asked about. Then give **one** next action.

Never tell them to scroll back through a chat. That is the thing that
made them lose an afternoon.

## Rules

- **Rename before working.** Always.
- **One prefix per session.** A chat that drifts into a second subject
  means: finish the thought, then tell them plainly that the rest belongs
  in a new chat, and name it for them.
- **Never invent a prefix.** Ask first, then add it to this table.
- **Never report the filing as an accomplishment.** Rename, log, and get
  straight to the actual work. She does not want a status update about
  her filing system, she wants her afternoon back.
