# Scared to Touch It — the Lead Developer skills

A kit of nine plain-English skills that turn the AI you already use into a **careful lead developer** for an app you built with AI and put live — so you can change it without breaking it, launch it to real strangers safely, and never be the only person who can run it.

You don't become a developer. You become the person who approves each step. The AI does the typing; a way back stays ready the whole time.

**New here? Read the guide first:** *Scared to Touch It — A Builder's Field Guide.* It explains the whole idea in plain words, with pictures and a short video for each skill.

## The nine skills, in order

| Gate | Skill | What it's for |
|---|---|---|
| Front door | `/readiness-check` | Tells you which gate you're at and the one next move. **Run this first.** |
| Gate 1 | `/safety-net` | A floor you can't fall through: a restore point, secrets cleaned up, backups that really restore. Run once. |
| Gate 1 | `/ship-change` | The everyday safe-change loop: try it on a private copy, publish only on your okay. Run every time you change anything. |
| Gate 2 | `/qa-harness` | Turns a must-not-break flow into a check that's proven to go red when it breaks. |
| Gate 2 | `/go-live-check` | Proves your safety nets actually catch real failures before strangers and money arrive. |
| Gate 2 | `/emergency-plan` | A one-page break-glass card, a proven way back, and an alarm — for the night it breaks. |
| Gate 3 | `/release-foundation` | Put new features on a calendar instead of shipping each one the second it's done. Run once. |
| Gate 3 | `/release` | Release day, seatbelts on: put a parked feature live, proven and bookmarked. |
| Gate 3 | `/handoff` | Prove someone else could keep it running without you. |

You climb the gates **in order** — each skill needs the ground the one before it laid. Most builders need Gate 1 and stop there; you climb higher only when a higher gate's fear becomes actually yours.

## Install (Claude Code)

These are [Claude Code](https://claude.com/claude-code) skills. Each lives in its own folder with a `SKILL.md`.

1. **Get the files** — clone or download this repo.
2. **Make them available to Claude Code** — copy (or symlink) each skill folder into your skills directory:

   ```bash
   # from inside this repo
   for d in readiness-check safety-net ship-change qa-harness go-live-check \
            emergency-plan release-foundation release handoff; do
     ln -s "$PWD/$d" "$HOME/.claude/skills/$d"
   done
   ```

   (Use `cp -R` instead of `ln -s` if you'd rather copy them.)
3. **Open your project in Claude Code and run:**

   ```
   /readiness-check
   ```

   It will tell you exactly where to start.

## What you'll need

- Your app in a git repository (the skills offer to set this up if it isn't).
- The skills are validated on common web stacks (Next.js / Supabase / Vercel-style apps); other stacks are best-effort, and the skills say so plainly when they hit a limit. The automated-checks skill drives a web browser, so it fits web apps — phone apps aren't covered yet.

## How it works, in one breath

Every fear you have about your live app has a name, and every named fear has a smallest possible fix. You add **one safety net at a time**, only when you actually feel the fear it removes — never a forty-item checklist. Whenever a skill says a net is "proven," it means one thing: a safe, on-purpose failure was made to happen and **you watched the net catch it.**

---

*Not legal, financial, or security advice. These skills help you work carefully; you remain the person who approves what goes live.*
