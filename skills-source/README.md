# Skill source

`file-this-chat.SKILL.md` is the source of truth for the filing skill.

The **live** copy is installed account-level at
claude.ai → Settings → Capabilities → Skills, where it fires in every
session on every surface.

This folder is the backup and the place to edit. It is deliberately
NOT under `.claude/skills/` — a second live copy would load alongside
the account one, and two copies of the same rules drift apart. That is
how the tag scheme broke the first time.

## To change the filing rules

1. Edit `file-this-chat.SKILL.md` here.
2. Zip it as a folder named `file-this-chat` containing `SKILL.md`.
3. Re-upload at claude.ai → Settings → Capabilities → Skills.
