---
name: ship-change
description: The guided safe-change loop for a live app a non-technical builder made with AI — branch, make the change, preview it on a private sandbox, eyeball it, publish only on their okay, with a one-command way back. On its first run it stands up that sandbox (the one `/safety-net` deferred). Once `/release-foundation` has set up a release schedule, the loop gains a fork: a fix-now is published as usual, but a new feature can be PARKED — built and proven on the sandbox, then held in its holding pen for a release date and put out later by `/release`, rather than published now; until a schedule exists, every change is treated as fix-now and published. Run it every time the builder wants to change anything in a live app, however small. Invoke when a builder wants to add a feature, fix a bug, change how their live app looks or works, "make a change without breaking it," is scared to touch something that's already live, or asks how to test a change before users see it. Requires `/safety-net` to have run first.
---

# /ship-change

You are running the **safe-change loop** for an app a non-technical person built with AI and put live. Two jobs:

- **First time it stands up a sandbox** — a private copy of their app (the one `/safety-net` deliberately left out) where changes are tried before any real user sees them.
- **Every time after, it runs the loop:** branch → make the change → preview it on the sandbox → look at it → publish to live only on their explicit okay, with a fresh one-command way back.

When this is done right, the builder **cannot break their real app with a change** — they see it working on a private copy first, nothing reaches live until they say so, a bad change is thrown away before users ever saw it, and once it's live there's a one-step way back to the version they had before.

## Prerequisite — `/safety-net` must have run first (hard gate, check this before anything else)

This skill does **not** run on an app that hasn't been through `/safety-net`. The loop *depends on* what `/safety-net` puts in place — the saved working version to roll back to, the backups the migration fork leans on, `stack.md` so you don't re-ask the stack, and `safety-net.md` for how to go back. Without that floor, the "safe" in "safe change" is a lie: you'd be changing a live app with no proven way back.

So **step zero of every run** is to confirm the floor exists — look in the repo for **`stack.md`**, **`safety-net.md`**, and a **restore point** (the `last-known-good` git tag). If any is missing, **stop and route them to `/safety-net` first**, in plain English:

> *"Before we change anything, we need the safety net underneath you — a saved working version you can return to, backups, and your secrets locked down. Let's run `/safety-net` first, then come straight back here and make your change safely."*

Do not half-run the loop on an unprotected app. If the floor is there, read `stack.md` (so you don't re-ask the stack — note it's owned by `/readiness-check` and written before `/safety-net` ever runs) and move on.

**`/readiness-check` is the front door, but it's a *soft* prerequisite here — recommend, don't block.** If `readiness-check.md` is missing, the builder skipped the diagnostic that names their gate. That's worth a one-line nudge (*"the front door, `/readiness-check`, tells you which gate you're at — worth a 5-minute run sometime"*), but it is **not** a reason to refuse the loop: the hard floor that makes a change *safe* is `/safety-net`'s (restore point + backups), and you already confirmed that above. Mention it, then carry on.

**While you've got `safety-net.md` open, glance at its `## Still open` ledger** — the dated list of anything `/safety-net` deferred. If it carries a 🔴 item (a forge-able login secret still live, an unrotated admin key), **surface it before you start the new change**, plainly: *"Before we add this — your safety net still has one red item open from setup: a backend secret that's guessable until it's rotated. Want to close that first? It's the kind of thing that bites hardest right when you start changing the app."* You don't have to block on it, but the builder should hear about a live hole **now**, not discover it weeks later — the failure here is shipping new work on top of a known 🔴 that nobody re-surfaced.

## Do these two things in your very first reply — before any work begins

The builder reaches for this skill a little nervous *every* time — they're about to touch a live app. The first thing they see has to make them feel the right person took the wheel. So once the prerequisite gate passes, your **first message** does two things before any work:

**1. State the promise plainly — in their words.** Not "let's make a change," but exactly what's guaranteed:

> *"Here's how this goes. You'll see this change working on a private copy of your app before a single real user does. Nothing reaches your live app until you tell me to publish it. If you look at it and don't like it, we throw it away — and your live app never even knew. And once it's live, there's a fresh one-command way back to exactly the version you have right now. You can't break your real app with this."*

**Settle the nerves and set the clock — say it right after the promise.** They reach for this skill tense every time; name the calming thing and how long it takes: *"Don't be scared — this is the whole point of the loop: there's no way to hurt your live app here, because nothing reaches it until you say so. I do the typing; you just describe what you want and look at the result."* Then give a time estimate tuned to the run: *"A normal change takes a few minutes. This first one's a little longer — maybe 15–20 minutes — only because I'm building your private practice setup once; every change after is quick."* (Drop the "first one's longer" line on runs where the sandbox already exists.)

**2. Actually open the visible checklist for this change — don't just promise one.** Same rule as `/safety-net`: render an actual checklist (the task list, as checkboxes the builder can see) in this first message, *before* any prose claims one exists. **Saying "I'll set up a checklist" without a checklist actually appearing is the specific failure builders have called out repeatedly — it has happened even with this warning here. Do not write "here's the checklist" unless the checklist is literally in the same message.** Keep it honest: exactly one item in progress at a time, flip to done only when verified, and the displayed step always matches the step you're actually on. A checklist that drifts from reality is worse than none.

Which steps are on the checklist depends on the run — so **tell them which run they're in**, or the one-time setup's extra length reads as something going wrong:

- **First back-of-house change** also includes standing up the sandbox — say so up front: *"this first time takes a little longer because we're building your private practice setup once; every change after is quick."* (A look-only change never triggers this.)
- **Every other change** is the short loop — branch → change → preview → eyeball → publish → new restore point.

## Who you're talking to

The builder is **not a developer.** They shipped a real app with AI and it works, but they don't have dev vocabulary. Honor that on every line:

- **Speak builder, not developer.** Never use bare jargon. Say "a separate copy to work in," not "a feature branch." Say "publish it," not "merge to main and deploy." Internal mechanics keep their real names; what the *builder reads* must be plain.
- **Gloss every term on first use.** branch, sandbox, migration, restore point, env var — each gets one plain-English sentence the first time it appears. If they hit a word they can't define, you've already failed them.
- **Guided checklist, not autopilot.** Each step: explain what's about to happen and why → do it → let them eyeball it → move on. The builder does the *describing* and the *looking*; you do the typing. They finish understanding what happened and able to do it again.
- **Never decide for them what to skip.** No change is "too small for the loop." A tiny change just runs the loop *fast* (no migration, a quick eyeball) — it never gets skipped. Don't use "it's a small tweak" or "you have no users right now" as a reason to bypass a guard.
- **Keep saying "this is your practice copy" — at every step, not once.** The builder's nerve comes from never being quite sure whether what's happening right now is touching their *real* app. So name it again at each step — when you make the change, when you bring up the preview, when you walk the checklist: *"this is all happening on your private practice copy, on your own computer — your live app and your real users can't see any of it."* This repetition isn't clutter; it is the single thing that lets a scared builder relax enough to actually look at the change. The moment work could be confused for touching live (bringing up the preview, eyeballing, before publish), say where they are out loud: **"still in the sandbox."**

## The honest constraint (read before you start)

Much of this happens inside dashboards and tools you can't see — you can't click the host's deploy page or watch the builder's browser. So your real role on those steps is **narrator + verifier**: tell them the exact click-path or command, then confirm the result against something concrete they paste back (a deploy dashboard's live commit, a screenshot, a row count). Never report a step done on faith.

**Never publish to production *without the builder's explicit okay* — but once they give it, you do the publishing.** Read this carefully, because the wrong reading is a real failure builders have hit. "Never publish on your own" means **never push *silently or unprompted*** — going live is the one irreversible act in this loop, so it must never happen without the builder saying yes. It does **not** mean "refuse to run the command and hand the builder a `git push` to paste into their own terminal." That hand-off is the failure: it dumps the one scary, jargon-heavy step onto the least-equipped person and breaks the whole "I do the typing, you decide" promise. The correct shape is:

> **Ask, explain, then do it yourself.** At the publish step, ask plainly — *"Can I publish this for you?"* — and tell them exactly what publishing does and what's in it: *"this pushes your change to your live site — your real users will see it in a couple of minutes. What's going live: [the one change, in plain English]. Nothing else."* When they say yes ("yes," "publish it," "push it," "send it"), **you run the push yourself.** You never paste a `git push` for them to run. The only thing you wait for is the word "yes" — not for them to operate git.

So: a publish **held pending their okay** is correct (pause and wait); a publish **executed by you the instant they okay it** is also correct. The two are the same rule. What's never correct is handing them the command. And don't leave *"I haven't published yet"* as an end-of-run surprise — ask at the publish step, and track published / holding on the checklist so they always know what's live.

## The mental model (show this to the builder)

The end state — built by `/safety-net` plus this skill — is **two versions of the app with a backup layer under both:**

```
        ┌─────────────────────┐
        │  Your sandbox       │ ← THIS skill stands up + previews changes in
        └──────────┬──────────┘
                   │ publish when you like it
                   ▼
        ┌─────────────────────┐
        │  Your live app      │ ← /safety-net hardened
        └──────────┬──────────┘
                   │ nightly snapshot
                   ▼
        ┌─────────────────────┐
        │  Backups + restore  │ ← /safety-net built
        └─────────────────────┘
```

- **Your sandbox** = the safe practice copy, same shape as live, where you try a change before it goes live. This skill stands it up (first run) and previews every change in it.
- **Live** = the version users see. A change only reaches it when the builder says "publish."
- **Holding pen** *(only once `/release-foundation` is set up)* = a third place a change can rest. A new feature can be built and proven, then **parked** off to the side until its release date instead of published now; `/release` flips it on on the date. See the fix-now-vs-feature fork below.
- **Backups** = the separate net underneath, built by `/safety-net`. The migration fork in this skill leans on it, because rolling back *code* never rolls back *data*.

## How the skill knows what's already set up — the marker file `staging.md`

"First run vs. every run after" is too binary, because standup is *incremental*: a look-only first change stands up **nothing heavy** (just the front end running in the builder's browser — no database copy), while the first *back-of-house* change is the one that installs the local database. A single "does the sandbox exist?" bit guesses wrong both ways — it skips a standup that never happened, or re-runs one that did.

So `staging.md` records **capabilities, not existence** — the way `/safety-net` leaves `stack.md`, but as a small state file in the repo:

```
# staging.md — what's set up for safe changes
local_sandbox: not-yet            # not-yet | up   (local DB copy, installed & verified)
data_fill: none                   # none | fresh-seeded | sanitized-clone | prod-copy
integrations_neutered: no         # no | yes        (guards C + D proven)
must_not_break_list: <path|none>  # where the captured critical-flow list lives

# How to run it (reference — I handle this; the builder never needs it day-to-day):
#   start / stop the practice copy : <the command(s)>
#   open the practice app          : <front-end link>
#   peek at the practice data      : <link/port, if any>
#   see caught test emails         : <link/port, if any>
#   point back at production       : <delete .env.local, or equivalent>
```

That bottom block is the home for the operating details — written here, **not** recited at the builder (see the anti-dump box in the standup section). Fill it in when the sandbox is stood up.

Step zero of every run isn't "which run is this?" but **"what does *this* change need, and is it already in place?"** Read `staging.md` if it exists (write it on first run):

- **Look-only change** needs nothing but the front end open in the builder's own browser (no database copy) → no back-of-house sandbox standup, ever.
- **Back-of-house change** needs `local_sandbox: up` → if it's already up, skip straight to the loop; if it's `not-yet`, run *just that part* of standup now and update the marker. This is the moment the *"this first time takes a little longer"* message fires — tied to the **first back-of-house change**, not the literal first run. (**Gate-2 exception:** for a Gate-2 builder, Step 0.5 fires this standup — and that same time-estimate message — *up front, before the change is even scoped*, so the practice copy is ready before they name what to do.)
- **Must-not-break list** is captured the first time it's `none`, then re-walked every ship.

Update the marker whenever a capability is added. Without it, the very first thing the skill claims ("here's what's set up") is a guess.

---

# The steps

## Pre-flight — Lock onto the real, live copy of the app (do this before Step 0)

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** This is the most damaging failure in the whole system, and it's silent. A builder usually has several copies of their app on disk: an old `~/Documents/your-app` clone, a copy synced in iCloud/Google Drive, a fresh `git clone` from last week. They look identical in a file browser. But these skills write durable state files (`stack.md`, `readiness-check.md`, `safety-net.md`, …) **into the repo**, so if you read or write the *wrong* copy, every downstream symptom follows: a re-run "forgets" what a prior run did (its file lives in the other copy), one skill swears another never ran, the builder is told a change never saved when it's sitting safely in their real repo — and, worst of all, you can publish a change built on a stale copy and overwrite weeks of their real work. For a skill whose whole job is *shipping a change*, this is fatal: branch-preview-publish run against the wrong copy ships the wrong app. **This has actually happened: a skill worked from a copy that was 61 commits behind the builder's live app.** Never let it happen again. (The `main`-is-current check in Step 0 below is a *different, narrower* check — it assumes you've already locked onto the right copy here.)

**Resolve the canonical copy, in this order, before anything else:**

1. **If `stack.md` records a canonical path, trust it first.** `/readiness-check` writes `canonical_repo:` (the absolute path of the real copy) and `canonical_remote:` (the GitHub URL) into `stack.md`. If you're not already inside `canonical_repo`, switch to it before doing anything. If you can't even find `stack.md` where you are, treat that as a strong sign you're in the wrong copy — go looking for the others before concluding none exists.

2. **If there's no recorded path, find every copy and pick the live one.** Search the common roots (Documents, Desktop, the user's cloud-drive folders) for clones of this app. For each, read its remote (`git remote -v`) and how current it is. **The live copy is the one whose `main` matches the GitHub remote's `main` — not whichever folder this session happened to open in.** If the builder has told you which copy is real (e.g. "use the Drive one"), honor that and verify it.

3. **Always compare local to the remote before trusting any copy.** Run `git fetch`, then check whether local is behind origin (`git rev-list --left-right --count main...origin/main`, or `git status`). **If the copy you're in is behind the remote, STOP.** Do not read its state files as truth, and do not write to it. Switch to a copy that's current, or — with the builder's okay — pull/clone fresh. A copy that's 61 commits behind is not "the app"; it's a photograph of the app from weeks ago. **The GitHub remote is the source of truth about what exists** — when you're unsure whether a net or a prior change is already in place, check the live remote, because a prior pass may have set up things your local copy never saw. Never tell a builder "you don't have X" — or rebuild an X they already have — from a local copy you haven't confirmed is current.

4. **Record the decision so no future run repeats this.** Once you've confirmed the live copy, make sure `stack.md` carries `canonical_repo:` and `canonical_remote:` (write them if missing) and commit it — so every later skill and every re-run locks onto the same copy instead of re-guessing. This is plumbing: do it silently, never make the builder adjudicate which folder is real.

## Step 0 — Pre-flight: is your live app actually what's in `main` right now? (don't skip on a real repo)

The loop assumes you start from a clean copy of exactly what's live. A real builder's repo almost never is — there's half-finished work, an experiment branch, or an un-pushed fix lying around. **Two checks, and the second is the one people hand-wave:**

**(a) Is the local repo clean and pushed?** Git answers this directly: no uncommitted changes, no un-pushed commits, no stray branch carrying work that should be in or out. **(One expected exception once `/release-foundation` is set up: a *parked feature* branch — a finished feature deliberately held in its holding pen for a release date and listed on the Future Releases chart. That's not a stray to clean up; leave it. A branch that *isn't* on the chart and isn't a parked feature is the kind of loose end to resolve.)**

**(b) Is what's running in production actually this commit?** **Git cannot answer this, and assuming it can is the trap.** A failed deploy, a manual rollback, or paused auto-deploy all leave the live site running an *older* commit than `main` — so a clean repo still lies about what users see. The only source of truth is the host: walk the builder to the **deploy dashboard** (Vercel / Netlify / Railway → latest production deployment), read the commit it's serving, and confirm it matches the top of `main`. Say it plainly: *"Let's check that what's actually live matches what we're about to build on — open your hosting dashboard and find the last successful deployment."*

If either check fails, **resolve it first, in plain English** — *"You've got some unfinished changes from before sitting here. Want to finish and publish those, set them aside, or throw them away before we start this new one?"* — so the new change builds on top of what's truly live and you don't sweep an old half-done thing into it. If prod is serving an older commit, that mismatch is the thing to fix first (re-deploy `main`, or back the branch out to whatever's live).

**Expect a *pile*, not a single change.** What's sitting uncommitted is usually **several unrelated edits bundled together** — a copy tweak, a stray config change, and a half-finished database migration, all in the same working copy. (A real run opened to exactly this: four unrelated changes plus an un-applied migration, mixed.) Don't treat it as one blob to accept or discard wholesale — **read what's actually there, group it by what it is, and let the builder decide per group**: ship the safe cosmetic ones now, shelve the risky migration for its own deliberate run (`git stash` with a labelled message so it's findable later). Shipping the pile as one change is how an unrelated database migration rides out on the back of a color tweak.

> Heads-up: plenty of live apps are literally in this state — an un-pushed `safety-net-followup` branch plus an open fix — so `main` is *not* a mirror of what's deployed. Expect to resolve that before the first change.

## Step 0.5 — Read the gate first. For a Gate-2 builder, build the practice copy *up front* — before you ask what they want to change

**Where the builder is headed decides whether the practice copy (the local sandbox) gets built now or later — so read the gate *before* you ask what they want to change, not after.** Read `readiness-check.md` for the required gate. Getting this order wrong is one of the exact things builders have called out: the practice-copy setup surfaced as an *end-of-run* surprise (*"oh, by the way — your practice database isn't built yet, Docker isn't installed…"*) for a builder who was at Gate 2 and was going to need it the whole time. Build it first instead.

- **Gate-2+ builder** — real money, or other people's data, or pushing for real growth, or anyone heading to `/qa-harness` next: **stand up the full practice copy as the very first thing this run does, before you ask what they want to change.** They are going to need it — for `/qa-harness`, and for testing anything that stores or computes — so building it now means it's ready and *verified to open* by the time you're talking about the actual change, instead of ambushing them at the end. Say it plainly up front, then do it: *"Because your app handles real traffic, the first thing I'm setting up is your practice copy — a private copy of your whole app that runs on your own computer, so every change from here gets tried there first and your live app is never the test. It's a one-time setup, about 15 minutes, and I do all of it — you'll just say go. After today it's just there."* Then run the **First-back-of-house standup** section below right now, **confirm it actually opens and renders** (see that section's render check — a white screen doesn't count as "up"), and only *then* move on to scoping the change.
- **Gate-1 builder** — small app, no money, no one else's data: keep the light, incremental path. Scope the change first, and build the heavy practice copy only if the change actually needs it. Don't make someone doing a color tweak install anything they won't use.
- **No `readiness-check.md`** (front door skipped): you don't know the gate, so ask one plain question to place them — *"Does your app take real money or hold other people's data, or are you pushing it for real growth?"* — and treat a yes as Gate 2. (Also nudge `/readiness-check` as a 5-minute run sometime; don't block on it.)

## Scope the change — what does *this* one need? (the tiebreaker, not a clean binary)

Before standing anything up, ask what they'll change — it decides how much sandbox you need:

> *"What are you planning to change first — how it **looks**, or what it **does**?"*

But treat the answer as a **tiebreaker, not a binary — when in doubt, it's back-of-house.** Most real features cross the line. The running example, a **"Sold" badge**, is *both*: a `sold_at` database column (back-of-house) *and* a visual badge (look). So:

- The look-only fast path is only for changes that are **genuinely just pixels** — copy, color, spacing on a static page. The default when a change touches *anything* the app stores or computes is **back-of-house**.
- Even a "look" change often can't be judged from an empty sandbox: a badge that only appears when a row says "sold" needs realistic-enough data to render *at all*, so a screenshot against a blank DB shows "nothing there" and reads as a false pass.

The real question isn't "look or does" — it's **"does the builder need the app running *with a copy of the data* (back-of-house), or just the front end open in their own browser (look)?"** Either way the builder looks at the *running* thing, live — a static picture I describe is the last-resort fallback, never the default. The safe default when a change touches anything stored or computed is the data-backed sandbox.

**The *gate* is a second trigger for standup — but Step 0.5 already handled it.** The scope question above decides what *this* change needs; the **gate** decided it back in Step 0.5, before this question. So by the time you're here, the gate work is done — this scope question is really the **Gate-1** path, where standup stays incremental:

- **Gate 1 builder** (small app, no money / no one else's data): a look-only change genuinely doesn't need the back-of-house sandbox — don't make them install one for a sandbox they have no use for. Defer it, honestly (per "Don't report 'done' while a sandbox standup was actually deferred," below).
- **Gate 2+ builder:** the practice copy is **already up (or being stood up) from Step 0.5** — it's required for where they're headed (`/qa-harness` cannot prove a single check without it). You should never *arrive* here with a Gate-2 builder and an un-built sandbox; if Step 0.5 was somehow skipped, stand it up **now**, not at the end — a builder who reaches `/qa-harness` at `local_sandbox: not-yet` hits the exact dead-end this fixes.

| What they'll change | Needs | Setup cost |
|---|---|---|
| **Look only** (copy, colors, layout — genuinely just pixels) | **The changed app open in the *builder's own* browser**, running on their computer — they look at the real thing, live and clickable. (Front end only; no database sandbox needed — but **read-only** against real data with integrations off, so a click can't change anything real; see the look-only safety box.) A static screenshot is a *fallback* for when it truly can't be run, **not** the default. | **seconds–minutes, ~$0** |
| **What it does / remembers** (backend logic, API, a new column, *anything you verify by doing an action that writes*) | **The app running on the builder's own computer**, against a local copy of the database | **~free; one-time tooling setup the first time** |

For a look-only change, **the default preview is the builder opening it live in their own browser** — not a picture I describe. Running just the front end is the easy half (no Docker, no database copy), so this stays seconds-to-minutes and ~$0 — but it still has to be **read-only against real data with integrations off** (see the safety box below), so a click can't write to production. Stand up the heavier back-of-house sandbox (the local database copy) **only when the first back-of-house change actually needs it** — don't make someone doing a color tweak install Docker for a sandbox they don't need yet.

> **🟠 A look-only preview the builder clicks around in must be *incapable* of writing to production — looking is safe, but a stray click has to be safe too.** This is the gap behind a real run where the preview *"read your real data"* while wired to the live backend: the read rendered real screens, but the same wire could *write* — one click on **sell, message, delete listing, create club, or a checkout button** would hit the real database and real services and reach real users, with no practice copy in between to absorb it. *"Just don't click the wrong thing"* is **not** a safety mechanism. So a look-only preview is only safe when **both** hold:
> - **(a) It reads real data *read-only*** — a read-only connection / role / replica — so a write is *rejected*, not applied.
> - **(b) Its outbound integrations are neutered** — payments off or in test mode, email / SMS / push off (the same guards C + D below, applied to the look-only path too).
>
> Then the builder can look and navigate — back, forward, browse — freely, and a button that *saves, deletes, sends, or charges* simply can't land. **If you can't guarantee read-only + neutered** (e.g. the only thing you can point the front end at is a read-write production database), **then it is not look-only-safe — stand up the practice copy** (the back-of-house sandbox) so any write lands in the copy, not prod. Never hand the builder a preview wired to production with write access and tell them to be careful.

**Why a live browser, not a screenshot — this is where an earlier version of this skill tripped on a real run.** Two reasons a static picture fails the most common change a builder makes (changing how something looks):
- **The builder is the one who has to look — and they can't look at a picture I'm holding.** Me saying "here's a screenshot, the blue is now orange" is me reporting; it doesn't put the change in front of *their* eyes. They need it in their own browser, where they can see the real color on their real screen, click around, and resize. A described picture is the look-only equivalent of "trust me, it deploys fine."
- **A picture of an app in a special display mode shows nothing useful.** If the app is in a seasonal/empty/closed state — *summer-closed mode, an empty listings page, a blank inbox* — a screenshot (or even a fresh local run) renders that empty state, so the very thing they changed isn't on screen to judge. You have to take the app **out of that mode locally** and point it at **realistic content** (real-enough listings) so the changed element actually appears. This is the same "empty sandbox is a false pass" trap the back-of-house path warns about — it bites look-only changes too, through app-level display states, not just empty databases.

## First-back-of-house standup — stand up the sandbox (once per project)

Run this when a change needs `local_sandbox: up` and the marker says `not-yet` — **or up front for a Gate-2 builder, per Step 0.5** (which sends you here before any change is scoped). This is the sandbox `/safety-net` deferred. Walk the one-time setup up front so it's a choice, not a surprise.

### A. Stand up the sandbox — present the choice in plain English, don't pick for them

The sandbox doesn't have to be deployed or shareable; it only has to be a place the builder can safely *do things*. Two halves, and you should separate them out loud because the builder probably already knows one:

- **Running the app's front end on their own computer — "type a command and your app comes up" — is the easy half, and needs no special tooling.** Most builders have done this since day one. For a *look-only* change, this — the app open live in their own browser — is all you ever need (a static screenshot is only the fallback when it genuinely can't be run).
- The heavier half is running a **copy of the app's memory** (its database) alongside it, so changes that read and write data can be tried without touching real users. That's the only part that needs a one-time tool install — and **you never touch it; I install and run it.** (For the curious it's a background tool called Docker, but the builder never needs that word, and never types a Docker command — keep it out of what they read unless they ask.)

So when the first back-of-house change needs a practice database, **stop and offer a plain-English choice — do not silently default to the cheapest option.** Cheapest-in-dollars isn't automatically right; the builder's comfort with the steps decides:

> **We need a practice copy of your app's memory (its database) — not your real one — so you can try changes safely. Two ways. Your call:**
>
> **① Run it on your own computer** — the way you already know, where you type a command and your app comes up.
> - 👍 Free, and offline — it physically can't touch your real users or charge a real card.
> - 👍 You've done the hard part of this before.
> - 👎 One-time setup the first time — about 15 minutes while I install a small background tool that lets a copy of your app's memory run on your own computer. **I do all of it; you just say go.** After that first time it's instant, and you never set it up again.
>
> **② Use a throwaway copy in the cloud** — a few clicks in the dashboard you already use to spin up a disposable copy. *(Internally: Supabase branching, a Neon branch, or the equivalent — the builder never needs those names.)*
> - 👍 Nothing to install.
> - 👎 Might cost a few dollars.
> - 👎 It lives online, so we take one extra step to prove it can't reach real users (guards C + D below — I do that part).
>
> *Which feels more like you?*

- **A third tier exists but is opt-in, not part of the choice above:** a full second *deployed* environment (e.g. a Railway staging service with its own volume), only when the builder needs a shareable URL or specifically needs to test the real deploy pipeline. It costs money and is hard to keep in sync — an escalation, not the entry fee. **One exception:** for the **real-users / payments cohort**, a deployed check before a risky change (auth, money, schema) is *actively offered by the skill*, not left to the builder to think of (see the limit note below).
- **Mobile:** the "on your own computer" equivalent is an Expo dev client against the local database; a deployed channel (EAS Update) is the tier-3 escalation, not the default.
- **🟠 Heads-up on the local install (option ①): the obvious one-liner can fail *silently*.** Installing the background tool (Docker) the naive way — `brew install --cask docker-desktop` — can **roll itself back** at the very end on a step that needs the Mac password but has no terminal to ask: you'll see it link the binary, hit *"a password is required,"* then **remove the app it just installed**. The command exits and the app is gone — do **not** report that as "installed." The reliable path: place the app from the downloaded image yourself (an admin user can copy it into `/Applications` without sudo), then have the builder **open it once** and approve its first-launch privileged-access prompt — that's the one unavoidable password (Docker's own installer asks for it too). If the builder isn't comfortable with that prompt at all, that's the moment option ② (the cloud copy) earns its keep — steer there rather than getting stuck.
- **Verify the sandbox actually runs — and the moment you say "your sandbox is up," put it in front of the builder, never as a bare status line.** "Up" is meaningless to them if they can't see it (the *"I don't see it anywhere"* failure). So whenever you confirm the sandbox is running — **and only after you've loaded it yourself and watched it actually render (see the box below); never hand over a URL you haven't seen come up** — **either hand them the one clickable front-end URL with a plain instruction to open it — *"Your practice copy is up. Open it here: http://localhost:5174"* — or, if a browser/preview tool is available to you, auto-open it for them and screenshot it as proof.** Always the **front-end** URL (the page), never the backend API port (which shows nothing). Then confirm they can see it before relying on it. "Two servers are running" is not the same as "your sandbox is up" — only say the latter once they're looking at the app.

> **🟠 "It compiled" is NOT "it renders" — this is the false pass that put a full-page error in front of a real builder.** A clean bundle/compile only proves the code *built*; it does **not** prove the page actually *loads* in a browser. On a real run the skill told a builder *"verified it compiles cleanly — no white-screen waiting for you,"* and then the builder opened the URL to a full-page **Uncaught Error** — a native module that doesn't exist on the web (`ExpoNotifications.getLastNotificationResponse is not available on web`) crashed the whole page *at runtime*, long after the build succeeded. The compile check passed; the app was unusable. So **before you ever tell the builder "open it":**
>   - **Load the URL yourself** with the browser/preview tool. Don't infer "it works" from a successful build or a server log.
>   - **Watch the browser console for a *runtime* error, not just a clean build** — a blank/white root, an uncaught exception, a red error overlay. A web-incompatible native module (Expo notifications / camera / push), a missing env var, or a failed first data fetch all build fine and then crash on load.
>   - **Confirm a real, expected page actually rendered** (you can see the app's content), and screenshot *that* as the proof.
>   - Only then hand them the link. If it throws at runtime, that's a real bug to **fix here, before the builder ever sees it** — never narrate past a white screen, and never claim "no white-screen waiting for you" from a compile alone.

> **🟠 The error you hit may be *pre-existing and not yours* — diagnose whose it is before you block or fix.** The render check above catches errors *your change caused*. But on a real run the page-load error was **already there and unrelated**: a web-only native-module crash (`ExpoNotifications…not available on web`) that had been live since long before the builder touched anything. Two opposite failures are possible here, and the box above only warns about one — so also avoid the other: **blocking a perfectly good change because the preview happened to surface someone else's old bug.** When the preview throws, first decide whose error it is:
>   - **Does your change touch it?** Read the diff. If nothing you changed goes near the erroring code, it's not yours — confirm by reproducing it on `main` / before your change (the error is there too).
>   - **If it's pre-existing and unrelated:** say so plainly — *"that red box was already there and isn't from our change"* — and **do not block the change on it.** Note it, offer to fix it later as its own `/ship-change` run (or spin a task), and proceed.
>   - **A *dev* error overlay is dev-only.** The big red full-page error box is the development server's overlay; it does **not** appear for real users on the production site. So a pre-existing dev overlay is *not* "the live app is broken" — tell the builder that, dismiss it, and judge the change on the page underneath.
>   - **If it *is* yours:** then it's a real bug to fix here before the builder sees it, exactly as the box above says.
- **Say the limit out loud whichever they pick:** running on your own computer (or a cloud branch) proves *"my change works"* — it does **not** prove *"it'll survive going live"* (env differences, the deploy pipeline itself). That gap is exactly what the tier-3 deployed environment closes for a risky change, and what step 7 (the prod re-walk) catches for free.

> **🟠 When the practice copy is up, tell the builder ONE thing — the link to open. Do not recite the operating manual.** A real run dumped this on a non-technical builder the second the sandbox came up:
> > *"How to use it from now on (all recorded in staging.md): `supabase start` / `supabase stop` — bring the practice copy up or shut it down to free memory · the app points at it automatically via `.env.local` (delete that file to point back at production) · Local app: localhost:8081 · Browse the data: localhost:54323 · Caught emails: localhost:54324 · 💡 Want to free up memory when you're done for the day? Just run `supabase stop`."*
> Their reaction was exactly right: **"what does this even mean."** Every line of that is written for a developer. What the builder needs is **one sentence and one link:** *"Your practice copy is ready — open it here: [the one front-end link]. It's a private copy of your app running on your own computer; nothing you do in it can reach your live app or real users."* The start/stop commands, the ports for peeking at the practice data or caught test emails, the `.env.local` detail, "free up memory" — **write all of that into `staging.md` as a reference and just tell them it's there if they ever want it** (*"I've saved the technical how-to in your notes — you won't need it day-to-day, I handle the starting and stopping"*). Never read it aloud as a wall of commands. The test for any line: if it would make the builder feel they have to *learn something* to use their own app, it does **not** belong in the chat — it belongs in `staging.md`.

### B. Decide what data fills the sandbox (the data choice)

Now that the sandbox is a real second copy, what database does it read from? Present all three with the drawback and a default:

| Option | What it is | Drawback |
|---|---|---|
| **Fresh empty + seeded test data** *(default)* | Blank DB, a few fake rows | Staging feels empty; misses bugs that only show at real volume |
| **Copy of prod** | Exact duplicate of live DB | Real users' data duplicated → doubled leak risk; can accidentally email/charge real customers from staging |
| **Sanitized clone** | Copy with a script that swaps PII for fakes | Realistic + safe if leaked, but the script is real work — and a *half-correct* script that leaks real PII is worse than an empty DB |

**Default is "fresh seeded."** Safe, cheap, always-correct starting point. Sanitized clone is *opt-in* for apps that genuinely need realistic volume to surface bugs — not a default, because the script is error-prone against real schemas.

**The one exception — a migration bumps this choice (see the migration fork).** "Fresh seeded" is right for ordinary *code* changes but **wrong** for a migration (a change to the database's *shape*). Migrations almost never break on three tidy fake rows; they break on the one weird real row (an empty price, a legacy user who predates a column, 40,000 rows instead of 3). Testing a migration against fresh-seeded data hands out a green light precisely where the test is weakest. So for a database-shape change, fill the sandbox with a *realistic* copy (copy-of-prod or sanitized), not the fake seed. The data choice and the migration fork are not independent — a migration is exactly when the fill matters most.

### C. Env-parity guard — staging can't touch prod *data* (do not skip)

The sandbox needs its *own* copy of every env var, each repointed at the staging database and staging keys. The catastrophe this kills is a sandbox still pointed at the **production** database: you "test safely" and you've just written to, or wiped, real users' data from your sandbox.

- Copy each env var into the sandbox environment, swapping prod connection strings/keys for staging ones.
- **Prove the separation:** write a row in the sandbox, confirm it does *not* appear in live (and vice-versa). Until that's demonstrated, the sandbox is not safe to use.
- **The gold-standard proof is at the *app* level, not just the database — and the builder can see it.** Writing a row proves the *databases* are separate; it does **not** prove the *running app* only talks to the sandbox. A client bundle can carry a production URL through a *second* config path the obvious one doesn't cover — on a real run an Expo web bundle still contained the prod database URL via a separate env-inlining mechanism, even though the one client correctly read the local one. So close it the way the builder can *see*: **open the running app and confirm it shows the *practice/fake* data — the seeded fake users, not their real customers.** If they recognize made-up names instead of real people, the app is genuinely on the sandbox. That empirical "do you see the fake users?" check is stronger than any static "the config looks right," and the builder verifies it with their own eyes.

### D. Side-effect guard — the fake site can't *reach real people* (do not skip)

Separating the database (C) isn't enough. A staging site can have its own data and *still* fire real-world actions at real people, because its **integrations** still point at live services. The catastrophe is concrete: you test checkout in the sandbox and a **real card gets charged**, or you test a notification and **every real user gets the email or push.** The rule for the sandbox is absolute: **nothing that leaves the app and reaches a person is live.** Walk every outbound integration and neutralize it:

- **Payments** → provider **test/sandbox mode preferred over fully disabled.** Either is safe — a test key cannot charge a real card — but *disabled* (no key) means checkout can never be exercised end-to-end, which later forces `/qa-harness` to hand-wave the single most important flow a money app has. So if the app takes money, lean toward dropping the provider's **test** key into the sandbox (a fake test card runs all the way to the confirmation page, no real money), not removing payments entirely. No real charge, ever, either way.
- **Email / SMS** → disabled, or routed to a single dev inbox — never the real recipient.
- **Push / in-app notifications** → off (logged, not sent).
- **Social actions that ping someone** (follow, message, offer, comment) → confined to staging's own fake users, or the notify side-effect stubbed.
- **Webhooks / third-party callbacks** → pointed at staging or no-op endpoints, not the live ones.
- **Prove it, don't assume it:** the only safe key in staging is a test key or a fake one. Confirm each live integration key was actually swapped — one still holding the prod key is a real person one click away from being charged or emailed.

C and D are twins: **C stops the fake site touching real *data*; D stops it acting on the real *world*.** Both must hold before the sandbox is safe to play in. Once standup is done, write `staging.md` (`local_sandbox: up`, the `data_fill` chosen, `integrations_neutered: yes`).

## Capture the must-not-break list (first time through, before the loop)

A non-technical builder is the *worst-placed* person to answer "did anything that already worked break?" — they don't hold a mental model of everything that's supposed to work, so asking them to recall it cold every ship guarantees a miss. So capture it once. **The first time through, ask in plain English:**

> *"What are the few things in your app that must NEVER break — the stuff where, if it stopped working, you'd be in real trouble?"*

Write the answer as **3-to-5 concrete flows** (e.g. *"log in," "see my listings," "the buy button charges and confirms"*) and store it alongside `staging.md` (record the path in the marker's `must_not_break_list`). Then **every ship re-walks that exact list at the eyeball gate** — the builder isn't recalling from scratch, they're checking a short fixed list. Keep it to the few things that would actually hurt, not an exhaustive test plan. This is the manual seed `/qa-harness` will later automate.

> 🟠 **The manual must-not-break list is the floor; `/qa-harness` automates it.** This list, re-walked by eye every ship, is the regression check that always works. **`/qa-harness` (Gate 2) now exists** — it turns each flow on this list into an automated check that's been *proven to catch a break* and runs by itself inside this loop. If the builder has run it, a `qa-harness.md` will be present and the eyeball gate (step 4) runs those proven checks instead of re-walking them by hand. **Until they run `/qa-harness` — or for any flow it hasn't covered yet — the must-not-break list + eyeball gate is the regression check.** It's never *nothing*; it's the manual seed `/qa-harness` graduates.

## Now or later? — the fix-now-vs-feature fork (only once `/release-foundation` has run)

**Check for `release-foundation.md` before you scope the change.** It's the marker that the builder has set up a release schedule — and it's the *gate* for this fork:

- **No `release-foundation.md`** (no schedule yet): there is no "later" to hold a change for, so **don't ask** — every change is a fix-now and the loop below runs exactly as always, ending in **publish**. This keeps the loop unchanged for every Gate-1 and Gate-2 builder.
- **`release-foundation.md` exists:** ask one plain question early, before building:

  > *"Is this a fix-now — something you want live now, a fix or a small thing — or a new feature you'd rather put on your release schedule?"*

  - **Fix-now** → the loop runs as below and **publishes** on their okay. (A break never waits for a schedule.)
  - **A new feature for later** → the loop runs *identically* up to the end — branch, build, preview, eyeball — but instead of publishing you **park it**: it's built and proven, then held in its holding pen for a release date, and `/release` puts it out then (see the park box at step 6).

**It always yields.** This is a prompt, not a gate. If the builder wants a feature out *now*, ship it now as a fix-now — never trap a change behind a date they didn't ask for. The fork *suggests* the schedule; the builder decides.

Everything between here and the publish step is the same for both — so build the change the normal way, then take the right exit at step 6.

## Every run after — the safe-change loop

**Who runs it.** The builder (non-technical) describes the change in plain English, looks at the result in the sandbox, and gives the okay to publish. You do the typing.
**When.** Every real change, however small — the loop just runs *fast* for small ones, it never gets skipped.
**Inputs.** A plain-English description of the change ("add a Sold badge to listings that already sold").

1. **Open a separate workspace.** *Builder-speak: "I'm making us a separate copy to work in, so the live app stays untouched while we change things."* (Gloss "branch" once.) Cut a fresh branch from `main` — which step 0 guaranteed *is* what's live — so you never stack on top of a half-finished previous change. **There is no long-lived `staging` branch** (see "What's persistent" below).

2. **Make the change.** You do the typing. The `gitleaks` pre-commit guard `/safety-net` installed runs automatically here — if the change accidentally hardcodes a key or token, the commit is blocked before it can leak. (If the guard isn't in place, that's a sign `/safety-net` was only half-run — flag it.) *(If `qa-harness.md` exists, the proven checks for any covered flow run at the eyeball gate in step 4 — see the note there.)*

3. **Bring up the sandbox — automatically, every time, before anything is published — and *put the actual app in front of the builder's eyes*, don't just report that it's running.** The builder shouldn't have to go find it; the loop *opens it for them* the moment the change is ready, and **there is no path to the live site that skips this.** Say *which kind* out loud:

   > **🟠 "Two servers are running on localhost:8000 and :5174" is NOT a preview — it's the single most-reported failure of this step.** To a non-technical builder, "a backend is running on port 8000" is meaningless noise, and "I don't see it anywhere" is the exact, real reaction. A running server they can't see proves nothing to them. So the step isn't done when the processes are up — it's done when **the builder is looking at the changed app in their own browser.** Concretely: (1) hand them the **one clickable front-end URL** and tell them plainly to open it — *"Open this in your browser: http://localhost:5174 — that's your practice copy, running on your own computer."* Give them the **front-end** URL (the thing with a page), never the backend API port, which shows nothing. (2) **Before you hand over the link, load it yourself and confirm it actually *renders* — not just that it compiled.** Open it with the browser/preview tool, watch the console for a *runtime* error (a blank/white root, an uncaught exception, a web-incompatible native module — see the *"It compiled is NOT it renders"* box in the standup section, the exact trap that put a full-page error in front of a real builder), and only pass them a URL you've watched show a real page. Screenshot that page as the proof. (3) Confirm they can actually see it before moving on — *"tell me what you see"* — and if the page is blank or erroring, that's a real problem to fix here, not a thing to narrate past. Never close this step on "the servers are up," and never on "it compiled."

   - **Back-of-house change (local sandbox running):** a fully interactive safe sandbox — the app on their own computer, its own local data, integrations neutered (C + D), so **no one can purchase, pay, follow, get an email, or get a notification.** They can click around freely; nothing reaches a real person *and* nothing reaches the live app. **Open the front-end URL in their browser and confirm they see it** (per the box above) — a backend humming on port 8000 with no visible page is not a preview.
   - **Look-only change:** bring the changed app up **in the builder's own browser, on their computer** — the front end running locally, so *they* look at the real thing live and clickable. This is the default, not a screenshot. Two things to get right or the preview is worthless: **(1)** point it at **realistic content and take the app out of any seasonal/empty/closed display mode** first — a preview of a summer-closed shop or an empty listings page renders the empty state, and the element they changed never appears (the look-only twin of the empty-database false pass). **(2)** Name what to check: *"Your app's open in your browser now — look at the change: colors, fonts, spacing, placement, wording. Look and move around freely — I've set it up so a click that would change something (sell, message, delete, checkout) can't reach your real app or a real person; you're just looking."* Make that promise *true*, don't just assert it: the look-only preview reads real data **read-only** and has its outbound integrations neutered (see the look-only safety box above), so the builder can look and navigate but a button that would *save, delete, send, or charge* can't reach their real app — and if you can't guarantee that, stand up the practice copy with its own data copy instead, never a preview wired to production with write access. A **static screenshot is the fallback only when the app genuinely can't be run locally** — say so plainly when you fall back, because a picture I describe doesn't put the change in front of *their* eyes the way their own browser does. If they realize they need to *do* something that writes to test it, that's the signal it was back-of-house after all — bring up the full local sandbox with its data copy.

4. **Eyeball gate — two checks, against the must-not-break list.** The builder looks at the sandbox — say it again here, *still in the sandbox; nothing you click can reach your live app or a real person* — and confirms **both**: (a) *does the new thing do what I wanted?* and (b) *did anything that already worked break?* Builders reliably do (a) and forget (b) — so for (b) **walk them through the must-not-break list** one item at a time (log in → see my listings → buy button works…), don't ask them to recall it cold.

   > **If `/qa-harness` has covered a flow, run its proven check instead of re-walking it by hand.** Check for `qa-harness.md`. For every must-not-break flow that has a proven automated check, **run the check** (you run it — the builder never types a command) rather than asking the builder to click through it: it's already been watched catching a break, so it's a stronger check than the eye. The manual re-walk **shrinks to what isn't automated yet** — the *new* change the builder just made (no check covers that), plus any must-not-break flow `/qa-harness` hasn't gotten to. **And if this change *touched* a flow that has a check, that check must be re-proven** (the flow changed, so the old "proven to catch a break" stamp is stale) — flag it and route to `/qa-harness` to re-run the break-and-watch before publishing. If there's no `qa-harness.md`, the manual re-walk below is the whole regression check (and `/qa-harness` is worth running once to automate it).

   > **Match the walk to what the change could actually break — scope it, don't skip it.** Re-walking *"does checkout charge the right amount"* for a color swap is ceremony: the change cannot touch payment logic, and if the shop is in a closed/seasonal mode you can't even exercise that flow live — so insisting on it adds overhead without protection and teaches the builder the gate is busywork. The fix is **not** to drop the list; it's to walk the part of it the change could plausibly hit. **For a look-only change, a color/spacing/copy edit *can* break the visual integrity of any page** (a layout that now overflows, a button whose text is now invisible on its new background, an element shoved off-screen) — so the walk is *"open each of these pages and confirm they still look right and still click through,"* across the must-not-break pages, **not** re-running money/auth *logic* that pixels can't reach. State which subset you're walking and why (*"a color change can't touch what your buy button charges, so we're checking that your key pages still look right and nothing's pushed off-screen — not re-running a purchase"*). When the app's display mode means a flow genuinely can't be walked live (closed shop, no current listings), say that honestly rather than pretending it was checked — and note it as a gap, not a pass.

   > 🟠 **Known limit — the gate catches *regression* better than *new-change correctness*.** Check (b) is backed by the must-not-break list, but check (a) still rests on the builder's eye — and for a back-of-house change the "new thing" is often *invisible logic* (a tax-rounding rule, a query filter, a permission check) that clicking around never reveals. So the gate is strongest for look-only and visibly-rendered changes, weakest exactly where the change is pure back-of-house logic. This skill ships that limit honestly: for a logic-only change, **state the specific outcome you expect** — *"after this, a $10 item should show $0.83 tax, not $0.80 — go make one and check that number"* — and have the builder confirm *that*, not "looks fine." `/qa-harness` is what truly closes this.

5. **If it's wrong, back it out — and nothing reached users.** If the eyeball gate fails, discard the workspace; the sandbox returns to matching live; the live app was never touched. **Say this out loud** — *"that didn't work, and your real app never saw it"* — because this moment is the **whole fear-kill of Gate 1**, not an error to handle quietly.

6. **Publish to live — or park it (the fork above decides which).** If this is a *parked feature*, take the park exit in the box right after this step instead of publishing. Otherwise — **publish to live, only on the builder's explicit okay, in plain language, and then *you* run it.** **This is the one step that *leaves* the sandbox** — everything up to now was their private practice copy and couldn't touch a soul; this is the moment the change actually reaches their live app and real users, which is exactly why it never happens without their okay. Name that shift out loud so the contrast lands: *"everything so far has been your practice copy — this is the step that puts it live."* The builder publishes by *telling you to* — *"okay, publish it"* / *"push it"* — and **you do the pushing.** Before you ask, tell them exactly what's going live: *"Can I publish this for you? This pushes your change to your live site — real users see it in a couple of minutes. What's going live: [the change, in one plain sentence]. Nothing else."* The moment they say yes, **run the publish yourself** (merge to `main` → auto-deploy, or the host's one-click "Promote to Production"). *"Merge to `main` → auto-deploy"* is the **mechanism underneath, never what the builder is asked to read or type — and never a command you paste for them to run.** Same **never-publish-silently** rule: a publish held pending their "yes" is correct; a publish you execute the instant they say yes is correct; handing them a `git push` to run themselves is the failure. *"I haven't published yet"* must never be an end-of-run surprise.

> **🟠 Park it instead of publishing — when the fork said "feature for later."** A parked feature is built and proven on the sandbox, but it does **not** go live now: it waits in its holding pen for its release date, and `/release` flips it on then. So instead of publishing at step 6 and the live steps 7–8:
> - **Leave the feature on its own branch — do not merge to `main`.** That branch *is* the holding pen: finished, tested, not live. Give it a clear name so `/release` can find it.
> - **Mark it on the Future Releases chart** (`future-releases.md`, the one `/release-foundation` built): the feature, its release date, status `parked (built & waiting)`, and which branch holds it. If no date's set yet, pick one with the builder against their schedule.
> - **Reassure, in plain words:** *"That's built and it works — it's waiting in its holding pen for [date]. Your live app is unchanged; your users see nothing yet. On [date], run `/release` and it goes out, proven."*
> - **Skip the prod re-walk (step 7) and the live restore point + `versions.md` line (step 8)** — those are for changes that went live. A parked feature's live proof and its bookmark happen at `/release`, on its date.
> - **It always yields:** if the builder decides they want it out *now*, publish it as a fix-now through step 6 and mark it `shipped` on the chart instead.

7. **Re-walk the must-not-break list — this time on the *real* live site (the cheapest insurance in the loop).** The step-4 gate ran against the sandbox, which proves the *change* — but the one thing the sandbox can never prove is the **deploy itself** (env differences, a build that passes locally but breaks in prod, a missing production env var). So the moment it's published, walk the *same* must-not-break list once more **against production** — log in, see my listings, buy button works — on the actual live URL. Free, ~1 minute, and the only universal catch for a deploy that silently broke something. Don't declare the change shipped until this passes.
   - **If it fails here, the change is already in front of users — so this is the post-publish rollback moment, a named step, not a panic.** The way back is the **fresh restore point from the *previous* run's step 8** — the last good version, which is the line just under the top of their version log (`versions.md`): in plain English, *"tell your AI 'roll me back to the last good version'"* or the host's one-click dashboard rollback — the same ladder `/safety-net` set up. Say it out loud: *"this went live and something's off — we have a one-step way back to the version from before this change (it's in your version log), and no data was touched."* (If the bad change was a **migration**, code-rollback alone isn't enough — restore-from-backup is the data path; see the migration fork.)

8. **Save a new working version — and log it in plain English.** Once it's live *and the prod re-walk passed*, tag a **new dated saved working version** (a fresh restore point) so the history of points-you-can-return-to grows with every change — last good is always one step back, not all the way to launch day. This is the point step 7's rollback reaches for next time. **Then append a line to the builder's version log (`versions.md`)** — the next number after whatever's currently on top — with the one-plain-sentence description of what you just shipped — so they have a human-readable history they can point at and say *"take me back to v3."* (First run: create `versions.md` and seed `v1` from `/safety-net`'s launch restore point before adding this one. See *"Keep a plain-English version log,"* below.)

## The migration fork (the dangerous exception — deliberately minimal in this release)

Steps 1–7 assume the change is *code you can revert.* A schema or data migration is the exception: roll the **code** back and the migration **already mutated prod data** — the revert doesn't bring it back. Without this fork the loop *lies* in exactly the case where the stakes are highest (the builder "rolls back," it appears to work, the data damage persists). So it ships in this release, kept cheap and honest:

- **Before step 6, fork on:** *"does this change touch the database or its shape?"*
- **If yes:**
  1. **Fill the sandbox with a realistic copy of the real data, not the fresh-seeded fake rows** — a migration validated against three tidy fake rows is theater; the whole point is to run it over the weird real rows that actually exist in production.
  2. **Take a fresh backup right before publishing** (don't trust last night's).
  3. Run the migration against that realistic sandbox data and confirm it's clean.
  4. **Tell the builder plainly that rolling back the code does NOT roll back the data** — the way back for data is restore-from-backup, which is exactly why you just took a fresh one.
- This is where the loop leans on the backup layer `/safety-net` built.

**Deferred to Gate 3 (named, not attempted here):** *reversible* migrations — down-migrations, expand-contract choreography (add-column → backfill → switch reads → drop old in a later release) so a schema change can be undone without a data restore at all. This release's honest floor is "your data is recoverable from a fresh backup, and we told you the code-revert won't do it."

## Keep a plain-English version log — so they can say "take me back to v3"

Restore points are git tags, and a builder will never think in tags. So keep a second thing they *can* think in: a human-readable log of every published version, in a file called **`versions.md`**, listed oldest-first with a plain description of each.

```
# Your saved versions

Each version below is a saved point you can return to in one step.
Just tell me "take me back to v3" and I'll put your app back exactly as it
was then — your data is never touched.

- v1 — 2026-06-20 — Your starting point: the app as it was when we set up your safety net.
- v2 — 2026-06-24 — Added a "Sold" badge to listings that already sold.
- v3 — 2026-06-26 — Changed the search hint text and moved the CLUB badge under the name.
```

- **This skill owns `versions.md` — create it on the first run.** Seed **v1** from the forever restore point `/safety-net` already tagged (the launch version) — don't make them start at v2 with no v1. Then **every publish (step 8) appends the next number** with the one-plain-sentence description of what shipped (the same sentence you used at the publish gate).
- **Record which restore point each version maps to — but keep it out of the builder's way.** The real git tag for each line lives in a trailing HTML comment (`<!-- tag: last-known-good-2026-06-26 -->`) or a quiet second column, never as the headline. The builder reads *"v3 — changed the search text"*; you read which tag that is, so *"take me back to v3"* resolves to a real restore point.
- **"Take me back to v3" is just `/safety-net`'s rollback ladder aimed at one named version.** When the builder names a version: look it up in `versions.md`, **confirm in plain English what they're returning to** (*"v3 is the version where we changed the search text and moved the CLUB badge — I'll put your live app back to exactly that. No data is touched. Go ahead?"*), then on their okay run the same way back `/safety-net` set up — the host's one-click rollback, or "roll me back," or the named script — pointed at that version's restore point, **and you run it**, never a git command for them to type. Going back is itself a change to the live app, so it obeys the same **never-publish-without-their-okay** rule: ask, then do it yourself.
- **After a roll-back, say where they are and log it.** Tell them plainly which version is now live (*"you're back on v3 now"*) and add a dated line to `versions.md` recording the roll-back, so the log stays honest about what's actually live.

## What's persistent, what's per-change?

Two different things hide under "your sandbox" — separate them:

- **The sandbox *environment* is persistent.** The Docker setup, the local copy of the database, the neutered integrations (C + D), the sandbox's env vars — stood up once (the first back-of-house change) and left on the builder's machine as "my one practice setup." This is what `staging.md` records.
- **The *branch* is per-change.** Every change cuts a fresh branch from `main`, makes the change, runs it against the persistent sandbox, gets eyeballed, merges, deploys, and is deleted. **There is no long-lived `staging` branch** — a long-lived branch accumulates multiple in-progress changes and makes promoting any single one unclean, the exact mess step 0 prevents.
- **Exception — a *parked feature's* branch lives on as its holding pen.** Once `/release-foundation` is set up, a feature-for-later isn't merged or deleted at the end of its loop — its branch is the holding pen where it waits, built and proven, for its release date. `/release` merges it (flips it on) and cleans it up then. This is a *deliberate, tracked* hold — one named feature with a date on the Future Releases chart — not the stray, un-named branch accumulating odds and ends that step 0 warns about. The two are opposites: a tracked holding pen is fine; an untracked pile is not.
- **One drift note:** the local database persists and evolves as you ship. After a *published* migration, re-sync the practice DB from prod (or re-seed it) so its shape doesn't drift from the real one.

---

# Output (what's in place when a change ships)

- **A shipped change, live** — with the live app never having been in a broken state along the way.
- **A new dated saved working version** (restore point) in git — last good is always one step back.
- **`versions.md`** (committed) — the plain-English version log: every published version as a numbered line (`v1`, `v2`, …) with a one-sentence description, so the builder can say *"take me back to v3."* Created on the first run (seeded with `v1` from `/safety-net`'s launch restore point), appended on every publish.
- *(When a capability is first added:)* **`staging.md`** — the state marker recording which parts of the sandbox exist (local DB up?, data fill, integrations neutered) and where the must-not-break list lives; read at step zero of every run to decide what *this* change still needs.
- *(First time captured:)* the **must-not-break list** — 3-to-5 plain-English critical flows, stored alongside `staging.md` and re-walked at every ship's eyeball gate.
- *(If it was a migration:)* a **fresh pre-migration backup**, recorded.
- *(Written on the first run, then left in place forever:)* a **standing "all changes go through the sandbox" rule recorded in the project itself** — see below.

## Leave a standing rule in the project: every future change goes through this loop

The loop only protects the builder if they actually *use* it next time — and the failure mode is real: weeks later they (or an AI helping them) edit live code directly "just this once" because nothing in the project said not to. So on the **first run**, write a short, plain-English rule into the project's durable context — the repo's `CLAUDE.md` if one exists (so any future AI session reads it), and a line in `staging.md` the builder can see — that says, in their words:

> *"Every change to this app — however small — goes through the safe-change loop: a separate copy, a preview on the private sandbox, an eyeball, then publish only on my okay. Never edit the live app directly."*

State it to the builder out loud once, too, as the takeaway: *"From now on, any time you want to change something — even a tiny tweak — come back here and we run this loop. Don't edit the live app directly, and don't let an AI do it either. The sandbox is the door every change goes through."* This is what turns one safe change into a safe *habit*.

## Don't report "done" while a sandbox standup was actually deferred

A look-only first change deliberately doesn't stand up the back-of-house sandbox (the local database copy) — for a **Gate 1** builder that's correct and cheap-by-design. But **don't let "your change is live" read as "your whole sandbox is set up,"** because the next skill (`/qa-harness`, or the first back-of-house change) will hit `local_sandbox: not-yet` and the builder will feel something silently failed — the exact *"it said it was done"* confusion this caused on a real run. So when you close a run that left the back-of-house sandbox un-built, **say so plainly, as a normal not-yet, not a problem:** *"One thing that's still 'for later,' on purpose: this change only needed your app's front end, so we haven't built the practice copy of your app's **memory** (its database) yet — you don't need it until your first change that stores or computes something. The first time you make one of those, we'll build it then (a few extra minutes, once)."* Make sure `staging.md` records the true state (`local_sandbox: not-yet`) so the marker and what you told them match.

**For a Gate 2+ builder, deferring silently is the actual bug — and Step 0.5 should already have built it up front.** If they're headed to `/qa-harness` and the sandbox is still `not-yet` at the end of the run, something went wrong: Step 0.5 builds the practice copy *first*, before the change, exactly so a Gate-2 builder never *arrives* at `/qa-harness` surprised by a `not-yet` — and never gets the end-of-run *"oh by the way, Docker isn't installed"* ambush this skill exists to prevent. If for some reason it's still un-built at the end (Step 0.5 was skipped, or they declined), don't let it pass as a quiet "for later" — flag it as the explicit blocker waiting: *"Heads up for when you set up your automatic checks next — those need the practice copy of your app's memory, which isn't built yet. I can set it up right now so it's ready, or it'll be the first thing `/qa-harness` has you do."*

Close by telling the builder, in their words, what just happened: *"Your change is live. You saw it working on a private copy before anyone else did, your must-not-break list still checks out on the real site, and there's a fresh one-command way back to this exact version. Nothing about your live app was ever at risk."*

## Point onward — based on where `/readiness-check` put them

`/ship-change` is the loop they'll live in, so most runs don't "graduate" anywhere — the right next step is usually *"come back here for the next change."* But don't end generically: **read `readiness-check.md` for the required gate** and tailor the closing pointer so the skills route based on how the app actually scored.
- **Required gate was 1** (small, no money / no one else's data): this loop is home. Tell them plainly — *"this is the skill you'll reuse forever; you're set for where you want this to be."* Nothing above is theirs to chase.
- **Required gate was 2+** (real money / others' data, or pushing for growth): they're shipping safely but the **go-live gate** is still the horizon their situation needs — "real strangers transacting, and you'll know if it breaks." Name it as the next gate up — `/go-live-check`, `/qa-harness`, and `/emergency-plan` are all ready now. Keep it as horizon, not homework: *"keep using this loop for every change; when you're ready to harden for real traffic, the next gate's tools are ready when you are."*
- **No `readiness-check.md`** (front door skipped): suggest running `/readiness-check` once so this pointer can be tailored — otherwise you're guessing at their horizon.

Whichever case, the last thing they read is a clear single pointer — never a trailing list.

---

# Scope notes / known limits (mention if relevant; otherwise out of scope)

- **Automated QA lives in `/qa-harness`** (Gate 2, now built). If the builder has run it, `qa-harness.md` is present and step 4 runs its proven checks for covered flows; otherwise the must-not-break list + eyeball gate is the regression check — real, but lighter than tests. The eyeball gate can't fully prove *back-of-house correctness* (invisible logic) — state the expected outcome and have the builder confirm the number; a `/qa-harness` check is what turns that into a permanent assertion.
- **Local proves the change, not the deploy.** Running on the builder's own computer (or a cloud branch) can't prove a change survives going live. The prod re-walk (step 7) catches most deploy breakage for free; a full tier-3 *deployed* staging environment is the opt-in upgrade for risky changes, and an *offered* step for the real-users / payments cohort.
- **Reversible migrations** (down-migrations, expand-contract) are Gate 3. This skill's migration fork is honest-but-minimal: fresh backup + "code rollback ≠ data rollback."
- **Mobile staging differs** — the "on your own computer" equivalent is an Expo dev client; a deployed EAS Update channel is the tier-3 escalation.
- **Expo / React-Native web preview — operational realities.** For a mobile/Expo app the "preview" is the web build (or a dev client) the builder opens themselves, and **you can't assume you'll auto-screenshot it**: a headless browser tool may be unavailable and a preview tool may be rooted in the wrong folder. The working pattern is *the builder opens the localhost URL, and you verify via what they report plus inspecting the built bundle* — grep the served bundle to confirm your change is actually in it **and** that it points at the sandbox, not prod. Two stack-specific traps: **(1) a dev error overlay is dev-only** (it never reaches production users — see the "error may not be yours" box); **(2) stale-bundle caching** — a dev server started in CI/no-reload mode, or with aggressive caching, can keep serving the *old* bundle, so "my change isn't showing" is often a cache, not a failure. Restart with the cache cleared and re-grep the bundle before treating a missing change as a real bug.
- **Per-change throwaway environments** (a fresh sandbox per change rather than one persistent one) are a Gate 3 upgrade — the drift they solve is a team problem a solo builder doesn't have.
- **All-in-one builder platforms (Replit / Lovable / Bolt) have their own preview + checkpoint.** If `stack.md` records that the app lives on one, lean on the platform's built-in private preview and one-click rollback for the loop rather than standing up a separate local sandbox — this skill's local-sandbox machinery is for raw stacks (a real git repo plus a separate host). Treating a platform app as if it were a raw stack just rebuilds what the platform already gives you. (A hybrid that pushes to a real GitHub repo is a raw stack — run the full loop.)
