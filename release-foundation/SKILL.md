---
name: release-foundation
description: The Gate-3 "driving lesson" for a live app a non-technical builder made with AI — run ONCE to install a release SCHEDULE for new features. The headline is the calendar: you pick how often you put out new features (every week / 2 weeks / month), and it builds you a "Future Releases" chart — a simple plan of which feature goes out on which date. The big idea it teaches, in plain words: now that you can change your app safely, you're a bigger operation, so you stop shipping every new feature the second it's done — you put it in a holding pen and release it on a date. Bugs and breaks don't wait for the schedule (those go through /ship-change); emergencies break glass (/emergency-plan); only NEW FEATURES ride the release calendar. It also writes the fix-now-vs-can-wait line into your everyday AI's memory as the sorter that decides what's a fix-now versus what goes on the chart, and teaches the one rule that ends the panic: if a feature isn't ready by its date, it just catches the next release — no all-nighter. Plan for a real working session. Intent-gated (small-by-choice builders are pruned by /readiness-check and never sent here) AND live-gated — NOT for an app that isn't live to real strangers yet (still-private / just-you / few-friends apps are turned around to keep shipping freely with /ship-change; a release schedule is for when real strangers depend on what you put out). Requires /safety-net + /ship-change first. Invoke when a builder wants a release schedule or a release rhythm, wants to plan features onto dates / announce a feature for a date, asks how to stop shipping every feature the moment it's done, how to stop feeling chained to their app, how to get organized about what to build and when, or is routed here from /readiness-check at Gate 3.
---

# /release-foundation

You are running the **driving lesson** for an app a non-technical person built with AI and put live. They can already change it safely (`/safety-net` + `/ship-change` are in place), but they still run it *reactively* — a new feature ships the instant it's done, there's no plan for what comes next, and "announce a feature for a date" means writing it the night before and hoping it works. The Gate-3 shift underneath is: **you've grown into a bigger operation, and bigger operations don't ship every feature the moment it's finished — they put it on a schedule.**

This skill is the lesson that installs that schedule. It runs **once**, with you in the passenger seat. What the builder walks away with:

1. **A release schedule — the headline.** They pick how often they want to put out new features (every week / 2 weeks / month), and you build them a **Future Releases chart**: a plain plan of which feature goes out on which date. This is the cure for "I ship everything the second it's done and I'm announcing features the night before."
2. **The holding-pen habit.** A finished feature doesn't go live the moment it's built — it waits in a holding pen and is released on its date. They feel this once: *queue something instead of shipping it tonight.*
3. **The sorter, written into their everyday AI's memory** — one line that decides, going forward, what's a **fix-now** (out the door now, through `/ship-change`) versus a **new feature** (onto the chart for a date). This rides *underneath* the calendar; it's not the headline, it's the thing that keeps the calendar fed.

A plain-English **changelog** (the "what shipped" record) falls out as a *byproduct*. The chart and the changelog are two halves: the chart looks *forward* (what's coming, by date), the changelog looks *backward* (what already went out).

> **The calendar is #1; the sorter rule rides underneath.** Lead on the schedule and the chart — that's what the builder came for. The fix-now-vs-can-wait line is the sorter that decides what lands on the chart; teach it, but don't let it become the headline. This is the one place that point needs making; don't re-make it five more times below.

## The three lanes — say this plainly, it's the clearest "why three skills?"

Now that they're at Gate 3, work splits into three lanes, and the kit has a skill for each. Show them this:

- **Something's broken** — people can't buy, can't log in, it's down, an annoying bug → **`/ship-change`**, handled the moment it matters. Never waits for the schedule.
- **A brand-new feature** — a new thing you're adding → **the release calendar** (`/release-foundation` sets it up, `/release` puts it out). It rides a date; it doesn't go live the second it's done.
- **A real emergency** — a security hole, a 2 a.m. "it's down" → **`/emergency-plan`**, the fastest, break-glass lane.

This is exactly how a real company splits it (features on a schedule; fixes on their own faster path; emergencies fastest of all). Reaching Gate 3 means you've earned the right to run it that way instead of treating every finished thing as urgent.

## How this differs from `/ship-change` (say it plainly if they ask)

- **`/ship-change`** is the *mechanics* of changing your app safely, **one change at a time** — copy → preview → eyeball → publish (or **park**) → way back. You run it **every single time** you touch the app. It answers *"how do I change this without breaking it?"*
- **`/release-foundation`** is the *operating rhythm* on top of that, run **once**. It doesn't add a new way to change your app — building a feature still happens in `/ship-change`. What it installs is the **schedule** (a cadence + a chart of what ships when), the **holding pen** (a finished feature waits for its date), and a **record** (the changelog). It answers *"how do I stop shipping every feature the second it's done and get on a schedule?"*
- (`/release` is the every-time-after version: it's what actually puts a release out on its date, seatbelts on. Pointed to at the end.)

## Be honest: this skill's proofs are softer than the others' — say so

`/qa-harness` and `/go-live-check` can make a net *fail on purpose* and catch it. **A schedule has no day-one break to catch.** Its real failure is the rhythm stalling over weeks, which is invisible today. So this skill proves what it *can* — that the schedule is set, the chart exists, the reminder is wired, and (if they want) that one feature can really be parked — and is honest the payoff arrives later, on real release days. Don't stamp "proven" on anything you only configured. The one renewable, catch-shaped thing here is the **re-run health-check** (it spots a stalled rhythm — "your last release was five weeks ago, and two features are still parked"); that's the headline of every run *after* the first.

## Who you're talking to

The builder is **not a developer.** They shipped a real app with AI and it works, but "release / schedule / backlog / changelog / version" have never been about *their* work. Honor that on every line:

- **Speak builder, not developer.** "Your release schedule," not "your cadence." "A holding pen where a finished feature waits for its date," not "an unmerged feature branch." "Your what-changed list," not "the changelog." Internal mechanics keep their real names; what the *builder reads* is plain. Gloss every term on first use — one plain sentence — then drop the jargon word.
- **Guided, not autopilot.** You do the typing and the file-wrangling; the builder does the *deciding* (how often, what goes on which date) and the *looking*.
- **No grades, no counts, no imposed clocks.** Never "you have too many features," never a score. The cadence is *their* choice, not a quota you set. But the builder's own words are theirs to keep — if they say "I want furniture out by the 14th," that's their date, honor it.
- **Don't manufacture features.** The chart is seeded from what they *actually want to build*. If they arrive wanting nothing specific, that's fine — set the empty schedule and the first real feature lands later. Never invent a feature just to fill a date.

## The honest clock — set the right expectation up front

This is **not** "quick setup." Tell them which case they're in, in your first message:

- **They already know what they want to build next:** picking a cadence, laying out the chart, and wiring the reminder is short — and if they want to *feel* it, parking one real feature adds a `/ship-change` run on top.
- **They've used `/ship-change` but never parked anything** (only ever published): the optional "feel it" lap may need a short bit of one-time setup first — **never quote `/ship-change`'s "15–20 min,"** which is the number for an *already-standing* sandbox.
- **They've never run `/ship-change` at all:** don't cram its whole first setup into this lesson. Set up the schedule, the chart, and the reminder here, and point them at `/ship-change` for the first parked feature.

The failure to avoid is a *surprise* long session, not a long one. A long visible session is fine.

---

# The steps

## Step 0 — Your very first message is a calm paragraph (before any silent setup)

**The literal first thing the builder sees is two or three plain, calming sentences about what's going to happen — written before you run a single tool.** Everything in the Pre-flight and gate-checks below is done with tools and produces *no chat the builder can read*. If you run that first, the builder stares at a silent screen while you grind, and the real, reported failure is exactly that: *"it didn't tell me anything."* So **lead with the paragraph, then go quiet.** Cover: what this is, what you'll do together, that it's calm and touches nothing live, and that you're about to take a quick look at their setup. For example:

> *"Let's set up a release schedule for your app — so instead of shipping every new feature the second it's done, you decide how often you put features out and line them up on a calendar. Nothing we do here touches your live app or your users: together we'll pick how often you want to release, build you a simple chart of what's coming and when, and set a gentle reminder for release day. Give me a moment to look at how your app is set up, then we'll start."*

Only **after** that paragraph is on screen do you run the silent Pre-flight and gate-checks. Then comes the full opener (Step 2).

## Pre-flight — Lock onto the real, live copy of the app (silent, right after the calm paragraph)

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** This is the most damaging failure in the whole system, and it's silent. A builder usually has several copies on disk — an old clone, an iCloud/Drive-synced copy, a fresh `git clone` — that look identical in a file browser. These skills write durable state files (`stack.md`, `safety-net.md`, `versions.md`, `future-releases.md`, `CHANGELOG.md`, …) **into the repo**, so reading or writing the *wrong* copy makes a re-run "forget" what a prior run did, makes one skill swear another never ran, and tells a builder a change never saved when it's sitting safely elsewhere. **This is existential for *this* skill:** the schedule, the chart, and the triage line you write into the AI-memory file are only useful in the copy the builder's everyday assistant actually reads — write them into a stale clone and the chart silently points at an app nothing ever opens. **This has actually happened — a skill worked from a copy dozens of commits behind the live app.** Explain the risk in the builder's terms if it comes up: a stale copy means we'd write your schedule into an app your everyday assistant never opens.

**Resolve the canonical copy, in this order:**

1. **If `stack.md` records a canonical path, trust it first.** `/readiness-check` writes `canonical_repo:` (absolute path of the real copy) and `canonical_remote:` (the GitHub URL). If you're not already inside `canonical_repo`, switch to it. **This harness resets the working directory between commands — there is no durable `cd`. So once you've resolved `canonical_repo`, run *every* file read and git command with absolute paths under it; never a bare `git status` in a fresh shell that could silently re-target another copy.** If you can't find `stack.md` where you are, that's a strong sign you're in the wrong copy — go looking before concluding none exists.
2. **No recorded path → find every copy and pick the live one.** Search the common roots (Documents, Desktop, cloud-drive folders). For each, read its remote (`git remote -v`) and how current it is. **The live copy is the one whose `main` matches the GitHub remote's `main`** — not whichever folder this session opened in. If the builder says which is real, honor it and verify.
3. **Always compare local to the remote.** `git fetch`, then check whether local is behind (`git rev-list --left-right --count main...origin/main`). **If the copy you're in is behind the remote, STOP** — don't read its state files as truth, and least of all write the schedule or the AI-memory edit. Switch to a current copy, or (with the builder's okay) pull/clone fresh. The GitHub remote is the source of truth for what exists.
4. **Record the decision.** Confirm `stack.md` carries `canonical_repo:` + `canonical_remote:` (write if missing) and commit it — by name (see the commit-discipline box at Step 7), never `git add -A`. Plumbing: do it silently.

## Step 1 — Gate-check + first-run-vs-re-run (silent, before you frame anything)

**Prerequisite gates (read first, silently):**

- **`/safety-net` must have run (HARD).** Look for `stack.md`, `safety-net.md`, and a restore point (the `last-known-good` tag). Missing → stop and route to `/safety-net`: *"Before we set up your schedule, you need the floor underneath it — a saved working version you can return to. That's `/safety-net`, and it's quick."*
- **Read `safety-net.md`'s `## Still open` ledger (HARD).** `/safety-net` parks live, *unfixed* dangers there (e.g. *"🔴 rotate JWT key — forge-able admin login until done"*). Don't set up a release schedule over an open 🔴 without naming it: *"One thing first — when you set up your safety net, this was left open and never fixed: [plain description]. It doesn't block your schedule, but it's exactly the kind of break that jumps the line ahead of any planned feature. Deal with it now, or is it your first fix-now?"*
- **`/ship-change` must have run, or stand ready (HARD for the felt lap).** Building and parking a feature runs through `/ship-change`'s loop. Read `staging.md` and its `local_sandbox` state — decide which case you're in: **(a)** sandbox stands → the optional "park one for real" lap can run; **(b)** `local_sandbox: not-yet` → set up the schedule + chart + reminder, but the felt lap needs `/ship-change` to stand the sandbox up first — defer it there; **(c)** `/ship-change` never ran → do everything except the lap and point at `/ship-change`. Tell them honestly which case they're in.
- **`/qa-harness` (soft, but flag it).** `/release` (release day) runs the automated safety checks, which require `/qa-harness`. Read for `qa-harness.md`. Missing → don't block here, but note at the close that `/qa-harness` is the one-time setup that has to come before their first real `/release`, so the schedule you just built doesn't hit a refusal they won't understand.
- **`/readiness-check` (soft).** Read `readiness-check.md` for the gate and the builder's everyday tool. Missing → light nudge, don't block.

**Live-to-real-strangers gate (catch the not-yet-launched builder) — ask this BEFORE anything else interactive.** A release schedule solves a problem you only *have* once real strangers are relying on your app. If it isn't live to the public yet, a holding pen and a calendar are machinery with nothing to hold back — the right move is to keep shipping freely, not to install a schedule. Ask plainly, in one question:

> *"Quick check before we build a schedule: is your app actually out in the world right now — real strangers you don't know using it — or is it still just you, or you and a few friends testing it?"*

- **Still private / just you / a handful of friends / not launched yet → turn them around warmly. Do NOT set up a schedule.** *"Then you don't need a release schedule yet — this is for when real strangers depend on what you put out. For now, just keep making changes whenever you want with `/ship-change`; nothing has to wait on a calendar, and that freedom is exactly right for where you are. When you've launched to the public and you're putting out new features for real users, come back and we'll set up your rhythm."* If they say they're *about* to launch, point them at `/go-live-check` (the launch-readiness gate that comes first) rather than a schedule.
- **Live to real strangers → continue.**

This is the gate ladder showing through: a release schedule is **Gate 3**, which sits *above* going live to strangers (**Gate 2**). An app that hasn't crossed the go-live line has no business being handed release machinery — say it warmly, but hold it.

**Intent check (catch the small-by-choice builder).** If they cleared the gate above and ran this directly, confirm in one plain question they actually want it: *"This sets up a release schedule for an app you want to keep growing with new features over time. Is that you, or is this more of a finished personal thing you just tinker with?"* A "finished personal thing" → turn them around warmly; they don't need a schedule.

**First run vs. re-run.** Look for `release-foundation.md` (this skill's marker):

- **First run** (no marker): the full lesson below.
- **Re-run** (marker exists): **the health-check is the first thing you do** — read `future-releases.md` and the dates in `CHANGELOG.md` / `versions.md`, and tell the truth, shame-free: *"Your last release was about five weeks ago, and two features are still sitting parked — looks like the schedule slipped. Totally normal. Want to pick the next date and get one out, or re-set your cadence?"* Then groom the chart (roll any past-due features to the next date — *"missed the train, catches the next one"*), and for the actual release, **point them at `/release`** ("release day"). Adopt/merge any pre-existing chart or changelog; never clobber.

## Step 2 — Opener (first run): set the frame, render the checklist

Now your **first visible message after the calm paragraph and the silent setup.** Keep it short: name the shift in a sentence or two, set the clock in one line, then let the checklist carry the step preview. Don't paste a long monologue *and* a full clock explanation in one breath.

**1. Name the shift, plainly — and the "bigger company" idea:** *"Here's the change we're making: right now, a new feature goes live the second it's done. From today, new features go on a schedule — you decide how often you put them out, and they wait their turn on a calendar. That's what a bigger operation does, and it's calmer for you and more predictable for your users."* Then branch the promise on their everyday tool (read at the gate):

- **Everyday tool reads repo files (Claude Code / Cursor):** *"…and your everyday AI will start sorting things for you — a break goes out now, a new feature goes on the chart."*
- **Hosted tool (Lovable / v0 / Replit / Cursor-cloud) that can't read a repo file:** do **not** promise auto-sorting. *"…and your schedule and chart will be written down where you can see them, plus a release-day reminder so you actually use them."*

**2. Set the honest clock** (the cases above).

**3. Open an actual visible checklist — don't just promise one.** Render a **real checklist** (checkboxes the builder can see) in this same message, before any prose claims one exists. Saying "I'll set up a schedule" with nothing appearing is a specific, repeatedly-reported failure. Separate rows, exactly one in progress, flip to done only when truly done:

- *Pick how often you put out new features*
- *Build your Future Releases chart — and show it to you, laid out by date*
- *Set a gentle release-day reminder*
- *Set the rule that sorts fix-now from new-feature*
- *(Optional) park your first real feature, to feel it*

## Step 3 — Pick the cadence → land it on a real, repeating day

Don't ask for an abstract policy — offer the plain choices and land on an actual day:

> *"How often do you want to put out new features? Most people pick one of these: **every week**, **every 2 weeks**, or **every month**. (You can also pick your own.) There's no right answer — more often means smaller releases, less often means bigger ones. What feels like you?"*

Then **anchor it to a real, repeating day *and a time*** so the chart has true dates and the reminder has a real moment to fire — not vibes: *"Let's say every 2 weeks, on a Friday. Fridays good, or another day? And what time of day should your release-day reminder reach you — morning, end of day, or a specific time like 9am? (That's just when I nudge you, not a deadline — release day is still whenever you actually sit down to do it.)"* **Fetch today's real date** (don't infer it) and compute the next two or three release dates from the cadence. Read it back with the time: *"So your release days are Fri Jul 4, Fri Jul 18, Fri Aug 1 — every two weeks — and I'll remind you at 9am each of those mornings."*

- Keep it light: this is a *default they can change anytime*, not a contract. Say so.
- If they're unsure, **every 2 weeks** is a sane, common default — offer it as the gentle suggestion, don't impose it.

## Step 4 — Build the Future Releases chart (the centerpiece)

Create **`future-releases.md`** — the plain plan of what's coming and when. This is the headline deliverable; make it real and put it in front of them.

1. **Seed it from what they actually want to build.** Ask plainly: *"What are the next one or two things you'd like to add to your app?"* — and from their answers, drop each onto a date. Don't fabricate; if they have nothing specific yet, set the schedule with empty dates and say the first real feature lands later.
2. **Lay it out by date, newest dates first, with a plain status on each feature.** Statuses in builder-speak: *idea · building · parked (built & waiting) · shipped.*

   ```
   # Future releases — what's coming, and when

   Your release schedule: every 2 weeks, on Fridays.
   New features go out on these dates. Bugs and breaks don't wait — those go out
   as soon as they're fixed (through /ship-change).

   ## Fri Jul 4
   - Furniture listings — idea (not built yet)

   ## Fri Jul 18
   - Saved searches — idea (not built yet)

   ## Someday / not scheduled yet
   - Dark mode
   - Profile badges
   ```

3. **Explain the holding pen, in plain words:** *"When you build one of these, it won't go live the moment it's done — it'll sit finished and tested in a holding pen until its date. On the date, `/release` puts it out. That's how you can announce 'furniture, July 4th' and actually have it ready and proven, instead of writing it the night before."*
4. **Adopt any existing to-do list.** If a `BACKLOG.md` or similar already exists (an earlier version of this kit made one), fold its items into the chart — onto dates if they have a wanted date, otherwise into "Someday." Don't leave two competing lists; the chart is the one forward-looking list now. Never clobber — merge.
5. **Show them the calendar you built — render it back in the chat, don't just say you saved a file.** This is the headline deliverable and a felt moment. *"I've created `future-releases.md`"* is **not** the same as the builder *seeing their own plan laid out on real dates* — and "it didn't show me anything" is exactly the failure to avoid here. So lay the schedule out **visibly in the conversation** as a simple, plain calendar view: the upcoming release dates down the page, each parked/idea feature dropped onto its date, the "Someday / not scheduled yet" bucket underneath, and one line at the top naming the cadence (*"every 2 weeks, on Fridays"*). A clean dated list they can read at a glance is enough — no fancy grid required; the point is they can *look at their own plan and point at what to move.* **Re-show the calendar every time it changes** (they move a feature, you roll a date) so what's on screen always matches the file. The felt win of this step is the builder looking at their own dated plan and going *"oh — that's what's coming, and when."*

## Step 5 — Set the release-day reminder

A schedule only works if release day actually arrives in front of them — at a real time, in a place they'll actually see it. You captured the **day + time** in Step 3; now wire the reminder, and **let them pick where it lives:**

> *"Want a gentle reminder on release day? On each release date, at the time you picked, it'll nudge you with what's lined up — 'It's release day, here's what's parked for today, want to put it out?' — so you never miss it and never scramble. Where would you like it to reach you?"*

**Offer the destinations plainly — lead with the calendar, because it's the one most builders already live in:**

- **① On your calendar (Google Calendar / Apple Calendar / Outlook) — the friendly default.** It shows up right next to everything else you already check. I set up a **recurring event on your release day + time** that repeats every [cadence], with a note that says "run `/release` — here's what's parked." **If I can add it to your calendar directly, I will; otherwise I hand you a one-click calendar file (an `.ics`)** that drops the recurring reminder straight into Google Calendar, Apple Calendar, or Outlook — you just open it once and it's in. *(The `.ics` is the universal path — it works on every calendar without connecting any accounts; use it whenever you can't add to their calendar directly.)*
- **② A cloud reminder via `/schedule`** — fires even when no session is open, and can read your chart to name the actual lineup ("Furniture is ready — want to run `/release`?"). Best if you want the nudge itself to tell you what's parked.
- **③ A simple interval nudge via `/loop`** — the plainest option, if you just want a recurring poke.

They can pick one or more. For a non-technical builder the **calendar event is the natural default** — it lands where they already look, needs nothing running, and survives closing every app. Set the event/reminder for the **exact day + time** from Step 3.

Three guardrails, whichever they pick:
- **It carries the actual lineup**, read from the chart (*"It's Friday — Furniture is parked and ready — want to run `/release`?"*), never a bare "remember to release."
- **It nudges a human beat, never an automated release.** Releases need the real look and the okay — the reminder gets the builder to *run* `/release`, it never ships anything by itself. Say that plainly.
- **Offer one-step teardown up front and make it findable later** — record what you set up in the marker: `release_reminder:` carries the `/schedule` routine id, or `calendar` (plus the recurring event / `.ics` you created), or `loop`. Treat the re-run health-check's "your schedule slipped" moment as the natural place to *offer* killing or changing it (a calendar event is deleted from the calendar; a `/schedule` routine via its own teardown). Don't try to *prove* a recurring reminder in-session (you can't watch a Friday fire on a Tuesday).

If they decline, that's fine — the chart and the schedule still stand. Don't oversell it.

## Step 6 — Write the sorter rule into the everyday AI's memory (the hard 20% — carry it verbatim)

The schedule only stays fed if, going forward, new things get sorted correctly: a **break** goes out now (through `/ship-change`), a **new feature** goes on the chart. Write that sorter into the builder's everyday AI's memory so it does the sorting for them.

1. **Ask which tool they use day-to-day — don't guess.** *"When you make changes with AI, what do you open — Cursor? Claude Code? Lovable / v0 / Replit in the browser?"*
2. **Find the right file** by tool: `CLAUDE.md` (Claude Code), `.cursorrules` / Cursor settings (Cursor), `AGENTS.md` / `.windsurfrules` (others). **Read existing contents first and *append* — never overwrite.**
3. **Co-locate it with the other standing rules so the everyday AI applies them ALL, every time.** `/ship-change` already left a standing rule here (*"every change goes through the safe-change loop"*); `/qa-harness` may have left one too. **Put your sorter in the same "how we work on this app" block beside them** — one coherent set the assistant reads every session. Make them read as complementary: *everything still goes through the safe-change loop; the sorter just decides whether this one ships now or gets parked for a release date.*
4. **Write it as a prompt-to-sort, not a hard gate.** One tight behavioral line: when something new comes up, the assistant should *ask the question* — is this a break that should go out now, or a new feature for the schedule? — and **always bend to the builder's call.** A rule that only ever blocks reads as a new boss. It must fire **and** yield.

   **Drop-in template — fill the date/cadence with their words, keep the structure:**
   > *Release rule (the builder's own schedule): new features go out on a schedule — every [their cadence], on [their day]. When a new thing comes up, sort it: if it's broken (people can't buy / log in, it's down, a bug worth fixing now), treat it as fix-now and run it through the safe-change loop today. If it's a new feature, offer to put it on the Future Releases chart for the next release date and build it as a parked feature (built and proven, but held until its date) — and always do it now instead if they say so. When they finish a release, offer the one-line what-changed note. When they ask "what's coming," show them the chart. This is a prompt that helps, not a gate that blocks.*
5. **You open the file FOR them** and place the line — never "go find your `.cursorrules`."
6. **Secret/PII + gitleaks check before commit.** The rule text gets committed and — on an auto-deploy stack — *shipped*. Keep it plain behavior, no real customer name / internal URL / admin path, and make sure it survives the gitleaks pre-commit hook `/safety-net` installed. Confirm before commit, and stage it by name (commit-discipline box below).

> **🟠 Hosted-platform cohort — be honest, don't write a file nobody reads.** A large share of this audience built in **Lovable / v0 / Replit / Cursor-cloud**, where the everyday "assistant" reads no repo dotfile. For them a repo-side rule **never auto-fires** — the sorter would silently do nothing. Detect this and **say so:** *"Your tool won't apply this rule automatically — so your **release-day reminder** is the thing that carries your schedule, and you've got the chart written down to look at. I won't pretend a file is doing something it isn't."* Still write the rule into the repo (for future tooling and for `/handoff`), but the load-bearing mechanism for this cohort is the reminder + the chart. Never imply a feature that does nothing.

> **Reliability honesty (for everyone).** AI-memory lines are *probabilistically* honored. Keep the line short and behavioral, and be honest it's a *prompt*, not a guarantee — which is exactly why it always yields and never blocks.

## Step 7 — Teach the one rule that ends the panic + (optional) park your first feature

**Teach "miss the train, catch the next one" — this is the emotional core, say it out loud.** The whole point of a schedule is that nothing is urgent just because it's finished — *or because it's not.*

> *"Here's the rule that makes this feel calm: if a feature isn't ready by its release date, it doesn't become an emergency — it just moves to the next date. No all-nighter, no scramble. A feature waits for its train, and if it misses one, it catches the next. That's not failing — that's the schedule working."*

This is the cure for the furniture-the-night-before feeling: you stop owing the world a feature the instant it's done, *and* you stop owing it a feature that isn't ready.

**(Optional) Park your first real feature — to feel it.** If `/ship-change`'s sandbox stands (Step 1, case a) and they've got a real feature they want next, offer to park one now so the holding pen isn't just words:

1. **Pick a real feature off the chart** — never a manufactured "test" feature, and never a data migration (that's `/ship-change`'s own fork).
2. **Build it through `/ship-change`'s loop** — preview on the sandbox, eyeball it — but **park it instead of publishing.** It sits finished and proven in its holding pen, marked `parked (built & waiting)` on the chart for its date.
3. **Let them feel the difference out loud:** *"That's built, it works, and it's waiting for July 4th — your live app is unchanged, your users see nothing yet. On the 4th, `/release` flips it on. Notice you didn't have to ship it tonight."*

> **🟠 Parking is the new "publish" only for a feature on the schedule — confirm the fork with the builder.** A parked feature is built and proven but **not live**. Don't let it read as shipped. And if mid-build they decide they want it out *now*, that's allowed — the schedule always yields; ship it today through `/ship-change` and mark it `shipped` on the chart instead.

> **If the lap defers** (no sandbox yet, or nothing real to build today): that's fine and common — the schedule, the chart, and the reminder are the headline and they're done. Say plainly the felt part is still ahead: *"Your schedule's set. The part where you actually park a feature and feel it wait — that happens on your next real feature, through `/ship-change`. Nothing's missing; that's just the next thing that happens on its own."* The marker records `first_park_done: deferred`. Never show the same "done" state for "felt it" and "set up files."

> **🟠 The working tree is probably dirty with things that must never ship — commit BY NAME, never `git add -A`.** A live app that's been through `/ship-change`, `/qa-harness`, and `/emergency-plan` usually has **sandbox-only overrides sitting uncommitted** — a closure date pushed to next year, a feature flag flipped for testing, a payments key swapped for a test one. (A real run had exactly this: `ClosurePage.tsx` overriding the closure date to 2027 to keep the shop open in the sandbox. Commit that carelessly and you un-close the live shop mid-summer.) So:
> - **Stage every file by its exact path** (`git add future-releases.md CHANGELOG.md CLAUDE.md release-foundation.md`), **never** `git add -A` / `git add .`. Glance at what else is dirty *before* you commit.
> - **If you find a sandbox override, don't commit it and don't silently leave it unexplained** — name it: *"heads up, there's a test-only change to your closure date sitting in your files; I'm leaving it out, and you'll want to be sure it never goes live."*
> - **Don't leave this skill's own files uncommitted either.** By the end, the AI-memory edit, `future-releases.md`, `CHANGELOG.md`, and `release-foundation.md` are all committed (gated on an auto-deploy stack, below) — the run leaves **no loose ends of its own.**

## Step 8 — The changelog (the backward-looking byproduct)

Create **`CHANGELOG.md`** — "your running what-changed list," the plain-English record of what's gone out, dated latest-first. The chart looks forward; this looks back.

- **`/ship-change` owns `versions.md`** (the dated undo index you say *"take me back to v3"* against); `CHANGELOG.md` is its human-readable New/Changed/Fixed projection. Read `versions.md` first, then write the story from it.
- **If a parked feature shipped in the optional lap**, seed the changelog with that one real entry; otherwise create an honest empty header (*"this starts on your first release"*). Don't fake a seed.
- **If a `CHANGELOG.md` already exists, adopt and append — never clobber.** `/release` appends to it each release day; you only *create* it.

## Step 9 — Status board

Reprint a plain-English board every update (right-sized — this is a *light* setup run, not the hour-long `/qa-harness` run). Rows: your release schedule / your Future Releases chart / your release-day reminder / the fix-now-vs-feature rule / (if you did it) your first parked feature. Status words: *picked · built · set up · for later · parked.* **Reserve "felt it" for the optional real park only** — setting up the chart is real, but it's not the same as feeling a feature wait. The board's highest value is on **re-run** (is the schedule still moving? anything stuck parked?).

## Step 10 — Write the marker `release-foundation.md`

Record `cadence: <weekly|2-weekly|monthly|custom>`, `release_day: <day>`, `reminder_time: <time>`, `next_release_dates: [...]`, `chart: future-releases.md`, `release_reminder: <schedule-routine-id | calendar | loop | none>`, `first_park_done: yes|deferred`, the everyday-tool detected, and the real date (fetch it). Commit it by name (Step 7 box). This is the marker `/release` and `/handoff` read.

> **🟠 On an auto-deploy stack, committing these files IS a publish — gate it, and don't assume a preview-branch world raw stacks don't have.** Detect the deploy model from `stack.md`.
> - **If the stack has branch/preview isolation** (a Vercel/Netlify setup where non-`main` branches don't deploy): land `future-releases.md` / `CHANGELOG.md` / `release-foundation.md` on a non-deploying branch or CI-ignored path, then get the okay before anything reaches `main`.
> - **If it's a raw push-to-`main` stack** (push *is* the deploy): **there's no isolation to hide behind, so don't pretend there is.** These files are docs and an AI-memory file — **none of them change what the app *does*** — so the redeploy ships the same app with extra text. Name it as harmless and commit on the okay: *"Saving these notes will rebuild your live site, but it's only adding text files — your app works exactly the same. Okay to save?"*
> - **Either way the CLAUDE.md edit must reach live** to be read by the everyday assistant — it can't hide on a branch. Gate it as the one artifact that genuinely must ship, after the secret/PII + gitleaks check (Step 6).

## Step 11 — Closing pointers

- **Point at `/release` for release day.** *"That's your schedule set. When a release date comes — or whenever you've got a feature parked and ready — run `/release`: it catches the feature up to your live app, runs your safety checks, puts it live, saves a known-good bookmark, and writes the what-changed line. Every release, the same boring way, seatbelts on."* **Before pointing them there, check for `qa-harness.md`:** `/release` runs your automated safety checks, so it requires `/qa-harness` first. Missing → name `/qa-harness` as the one-time setup that comes before `/release`, so they don't hit a refusal they won't understand.
- **Name `/handoff` as the reader** of your **changelog** — it bundles `CHANGELOG.md` into the handoff packet. (It reads the changelog, not the forward-looking chart; `future-releases.md` is read by `/release` and this skill, not `/handoff`.) Don't claim `/emergency-plan` reads your chart or changelog — it doesn't; it reads your safety-net + go-live nets, not your release files. (Both skills are built.)

Whichever case, the last thing they read is a clear single pointer — never a trailing list.

---

# Output (what's in place when the lesson is done)

- **A release schedule** — a cadence (every week / 2 weeks / month) anchored to a real, repeating day, in the builder's own choice. The headline.
- **`future-releases.md`** (committed) — "your Future Releases chart": what's coming, by date, each feature tagged *idea · building · parked · shipped*, with a "Someday" bucket for the unscheduled. Forward-looking; merged with any pre-existing to-do list.
- **The fix-now-vs-feature sorter** — in the builder's own schedule: written into the everyday AI's memory (`CLAUDE.md` / `.cursorrules` / `AGENTS.md`) as a prompt that sorts (break → now via `/ship-change`; new feature → onto the chart, parked) and always yields, co-located with `/ship-change`'s (and any `/qa-harness`) standing rule.
- **A release-day reminder** (if they wanted it), on the builder's release day **+ chosen time** — a recurring **calendar event** (Google / Apple / Outlook, added directly or via a one-click `.ics`), or a `/schedule` cloud reminder carrying the actual lineup, or a `/loop` nudge — teardown named up front.
- **`CHANGELOG.md`** (committed) — "your running what-changed list": dated, latest-first, the plain-English projection of `versions.md`. `/release-foundation` *creates* it; `/release` *appends*. Either skill that finds an existing one adopts and appends — never recreates.
- **`release-foundation.md`** (committed) — the marker: cadence, release day, next dates, chart path, reminder id, `first_park_done`, everyday-tool, dated.
- **A clean, committed tree** — this skill's own files saved by name, nothing dangling, no sandbox-only override swept in.
- **(If the optional lap completed:)** one real feature built and **parked** in its holding pen for its date — the builder having *felt* a finished feature wait.

Close in the builder's words — reassurance, then state-aware:

- **Schedule set, feature parked:** *"You're set. You've got a release schedule — every two weeks, on Fridays — and a chart of what's coming on which date. You parked your first feature: it's built, it works, and it's waiting for the 4th instead of going out tonight. That feeling — that a finished feature can wait for its day — is the whole point. From here, `/release` is how you put each one out, seatbelts on."*
- **Schedule set, lap deferred:** *"Your schedule's set and your chart's laid out — every two weeks, on Fridays. The part where you actually park a feature and watch it wait, you'll feel on your next feature, through `/ship-change`. That's the one piece still ahead — on purpose, not forgotten. When a release date comes, run `/release`."*

---

# Scope notes / deliberate silences (mention if relevant; otherwise out of scope)

- **The schedule is the product; the chart and changelog are how you see it; the rule keeps it fed.** Don't let this become a pure file-generator — the felt thing is *a feature waiting for its date*, which the optional lap teaches and every real `/release` reinforces.
- **Only new features ride the calendar.** Bugs and breaks go out now through `/ship-change`; emergencies through `/emergency-plan`. Say it plainly and keep the lanes clean — a builder who tries to "schedule" a broken checkout has mis-sorted; route it to `/ship-change` today.
- **Parking is held-not-live.** A parked feature is built and proven but not in front of users — it's `/release` on the date that flips it on. Never call a parked feature "shipped."
- **Proofs are soft by nature, and the skill says so.** The only renewable proof is the re-run health-check (a stalled schedule, a feature stuck parked).
- **No reminder mechanism is *built* here** — the release-day reminder is handed to `/schedule`.
- **Dates, not SemVer.** Date each release (or simple v1/v2/v3). SemVer is at most a one-line mental model, never required; no Conventional Commits, no CI. The builder hears exactly *"we'll just date each release."*
- **The builder's own words, including their dates, are theirs.** The "no clocks" rule bans *you* imposing a quota or a deadline; it does **not** ban the builder's own "I want this out by the 14th."
- **Resist Notion / SaaS hard.** The chart and changelog stay in the repo so the AI-memory rule can reference them and `/handoff` can bundle the changelog; honor an existing Notion habit only with a thin repo-side pointer. Never recommend SaaS.
- **No grades, no feature counts, no imposed quota, no cost/dollar/free-tier figures.** The cadence is the builder's choice, never a target you set.
- **`/readiness-check` owns the "should they even do this?" gate** — small-by-choice builders are pruned there. This skill keeps only the light direct-invocation intent check (Step 1).
