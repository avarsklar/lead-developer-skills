# PREFLIGHT.md — the canonical "lock onto the live copy" block

Every skill in this kit opens (after its calm first message, where that applies) with the **same pre-flight**: decide *which copy of the app you're looking at* and refuse to work from the wrong one. This is the most damaging failure in the whole system, and it's silent — a builder has several near-identical copies on disk (an old `~/Documents` clone, an iCloud/Drive-synced copy, a fresh `git clone`), and these skills write durable state **into the repo**, so the wrong copy makes a re-run "forget" prior work, makes one skill swear another never ran, and — worst — can overwrite weeks of real work or ship/bless/hand-off a stale app.

**These skills load as self-contained `SKILL.md` files (no runtime `include`s), so the pre-flight is physically copied into each one.** This file is the **canonical source** to copy from when you change it — and [`check_handshakes.py`](check_handshakes.py) enforces that every skill still carries the three load-bearing invariants below (so a copy can't silently weaken). When you edit the pre-flight, edit it here first, then propagate to all nine, then run the linter.

## The canonical block (customize only the closing stake)

> ## Pre-flight — Lock onto the real, live copy of the app (do this before anything else)
>
> **Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** A builder usually has several copies on disk (an old `~/Documents` clone, an iCloud/Drive copy, a fresh `git clone`) that look identical in a file browser. But these skills write durable state files (`stack.md`, `safety-net.md`, …) **into the repo**, so reading or writing the *wrong* copy makes a re-run forget prior work, makes one skill swear another never ran, and can overwrite real work. **This has actually happened: a skill worked from a copy that was 61 commits behind the builder's live app.**
>
> **Resolve the canonical copy, in this order:**
>
> 1. **If `stack.md` records `canonical_repo:` / `canonical_remote:`, trust it first.** If you're not inside `canonical_repo`, switch to it (run all reads and git with absolute paths under it — the harness resets the working directory between calls). Can't find `stack.md` where you are → strong sign you're in the wrong copy.
> 2. **No recorded path → find every copy and pick the live one** — the one whose `main` matches the GitHub remote's `main`, not whichever folder this session opened in. If the builder says which is real, honor it and verify.
> 3. **Always `git fetch` and compare local to the remote. If the copy you're in is behind the remote, STOP** — don't read its state as truth or write to it. Switch to a current copy, or (with the builder's okay) pull/clone fresh. The GitHub remote is the source of truth for what exists.
> 4. **Record the decision** — write `canonical_repo:` / `canonical_remote:` into `stack.md` if missing, commit silently. Never make the builder adjudicate which folder is real.
>
> **[CLOSING STAKE — customized per skill]** Each skill ends the pre-flight with why the wrong copy bites *it* specifically: safety-net builds a restore point over the wrong app; ship-change ships the wrong app; qa-harness tests a stale app; go-live-check renders a verdict on the wrong app; release blesses the wrong app; handoff hands someone a confident map of the wrong territory; emergency-plan's card points its undo at an app that isn't live. Keep that one customized sentence; everything above it stays verbatim.

## The three enforced invariants (the linter checks all nine skills)

1. The section header **"Lock onto the real, live copy"** is present.
2. **`canonical_repo`** is named (the recorded-path resolution).
3. The **behind-the-remote → STOP** rule is present.

The `61 commits` war-story is recommended flavor but not enforced (three skills legitimately phrase it as "dozens of commits behind"). Fire-mode skills (`/emergency-plan`) additionally note the STOP-if-behind guard is *relaxed* when the app is actually down — that's an intentional, documented exception, not a weakening.
