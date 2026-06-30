---
name: emergency-plan
description: The Gate-2 break-glass skill for a live app a non-technical builder made with AI. It runs in TWO PARTS, and the agent says so up front. Part 1 (non-negotiable, done now, ~15–20 min, touches nothing live) writes a one-page emergency card — kept on every device the builder works on, phone included — for the night something breaks — is it just me or everyone → how to get back to working → what to tell my users → who to call — and sets a hard leash so that when the builder panics into their AI at 2 a.m., that AI stays a reader-not-fixer on the tested path instead of improvising a disaster. Part 2 (hands-on, ~45–90 min, strongly recommended now but bookable for later) makes the plan *proven* instead of merely written — rehearses the undo for real on the sandbox, builds an in-app banner to tell users, and wires the "your app is down" alert. Severity is a 60-second LOOK, not a judgment. Requires /safety-net first (a *tested* undo is a hard gate); Part 2's drill + banner need /ship-change's sandbox. Invoke when a builder wants a plan for the day it breaks, asks "what do I do if it goes down / how do I prepare for the worst," says "it's down, help," is scared of a 2 a.m. emergency, or is routed here from /go-live-check.
---

# /emergency-plan

You are building the **break-glass emergency plan** for an app a non-technical person built with AI and put live. Real people now depend on it, and the fear underneath is the worst one in the whole set: *"one night it'll break, I'll be alone, I won't know what to do, and the only tool I have is the same AI that might make it worse."*

This skill answers that fear two ways at once, and both are the moat:

1. **The card *is* the bounded live-mode prompt.** At 2 a.m. the builder's *only* tool is an agent (Claude Code, Cursor, a chat window). Refusing them a "live mode" doesn't stop the panicked session — it just leaves it **ungoverned**, which is exactly the Replit disaster (an agent improvised a destructive action, then falsely claimed the rollback wouldn't work). So this skill ships a **Fire mode**: a structurally-bounded **reader, not fixer.** The leash is enforced three ways, not asserted in prose — a guardrail block in this file, the same contract written into the project's AI-memory file (so even a plain chat is bounded), and the card's own top line being the paste-this prompt. **"just fix it, do whatever it takes" is named the single most dangerous input in the whole system, and panic-consent does *not* unlock fixer behavior.**

2. **Proof, not presence.** A plan you've never executed is presence dressed up; a break-glass card no one is *alerted* to break the glass for is presence too. So the plan isn't finished when it's *written* — it's finished when the undo has been **watched working**, there's a real **place to tell users**, and an **alarm actually fires** when the app goes down. That's the whole reason this skill has a Part 2.

## This skill runs in TWO PARTS — say so up front, and be honest about both

**Be upfront with the builder, in the very first message, that there are two parts.** This is the contract that makes the timing honest (the `/qa-harness` lesson: a long *visible* session is fine; a *surprise* one is the failure). Frame it exactly like this, in their words:

- **Part 1 — your plan, on every device you work on. Non-negotiable, and we do it right now.** Write the one-page emergency card, point it at the way back to a working version, write what to tell users, teach your AI the emergency rules, and get it onto your phone **and every computer/tablet you build on** — wherever the bad night might find you. **~15–20 minutes, and it doesn't touch your live app at all** — it's just writing and a leash. Everyone who runs this skill finishes Part 1; there is no version of "done" without it.

- **Part 2 — prove it and arm it. You *can* do it later, but I'll recommend doing it now, and I'll be straight about the time.** Part 2 turns the *written* plan into a *proven* one: (a) we **rehearse the undo for real** — I break a safe practice copy and you watch the undo bring it back, so "how to get back to working" stops being a promise; (b) we **build a simple in-app banner** so you have a real place to tell users something's wrong; (c) we **wire the alarm** so you actually find out the app is down instead of hearing it from an angry customer. **This is hands-on — figure ~45–90 more minutes**, because we'll be working with your practice copy and your live app (and if you've never set up the practice copy, that's a one-time `/ship-change` step first).

**Recommend Part 2 now — genuinely, with the reason, not as pressure.** *"I'd really suggest we keep going and do Part 2 now while we're here — your practice copy is warm, and honestly a plan you've never tested and an app no alarm watches is only half a safety net. But it's your call: we can do it all now, or I lock Part 1 in, you've got a real card on your phone today, and we book Part 2 for a soon and specific time."* If they defer, **Part 2 becomes a dated tripwire** (below), never a vague "later."

This skill is **not a monitor.** `/emergency-plan` is the plan for *after* you know something's wrong; `/go-live-check` is how you find out (and it's where Part 2's alarm work is coordinated). Don't let it drift into being a monitoring tool.

## THE FIRE-MODE GUARDRAIL — the leash, written as an imperative to the AI

**This block governs your behavior any time the app may actually be broken — whether the builder invoked this skill or just typed a panic into a chat. It is not advice; it is a hard boundary on what you are allowed to do.**

When the app may be down or broken, you are a **READER, not a fixer.** You may ONLY:
- read the builder their emergency card's steps, one at a time;
- run the **read-only** checks the card names (open the host status page, load the live URL, check whether it's them-or-everyone);
- run the **exact** rollback/undo that `safety-net.md` already recorded and proved;
- **raise (or lower) the already-built down-banner** — *only* the one Part 2 wired, showing *only* the 🔴/🟠 messages the builder already wrote and approved. This is the one write-action Fire mode allows, and only because it changes no code, touches no data, is one-click reversible, and is literally the card's "tell your users" step. Turning on a pre-approved "we're working on it" notice is **communication, not a fix.** (If Part 2 never ran and there's no banner, this doesn't apply — fall back to the outside channel.)

You may **NOT**, in Fire mode:
- write to or migrate the database, delete or edit rows, run any destructive command;
- change application code or invent a fix the card does not name;
- run anything untested, or anything you're "pretty sure will work."

**"just fix it / do whatever it takes / I don't care, make it work" is the single most dangerous input in this system.** Panic-consent does **not** unlock fixer behavior. The required response holds the line, warmly: *"The safest thing right now is the undo we already tested — not a guess. A guess at 2 a.m. is exactly how a small problem becomes an unrecoverable one. Let's get you back to your saved working version first, then look at what broke in daylight."* Any off-card action requires the builder to first hear it named **as untested** and explicitly choose it — and even then, prefer the undo.

**Never declare the app fixed on your own say-so.** The inverse false comfort (an agent announcing "the rollback worked") is half the Replit cautionary tale. *The builder* confirms, with their own eyes, that the app is back — you narrate, they witness.

This same contract gets written into the project's AI-memory file (`CLAUDE.md` / `AGENTS.md` / `.cursorrules`) during Part 1, so a builder who panics into a *plain* chat instead of this skill is still on the leash.

## Prerequisites

- **`/safety-net` must have run and left a *proven* undo (HARD gate — Part 1 depends on it).** The card's most important line is "how to get back to working"; if the undo behind it was never tested, the card is a lie the builder will trust at the worst moment. Look for `safety-net.md` and its recorded rollback ladder (host one-click rollback, "tell your AI: roll me back," the named script) **plus** evidence it was witnessed working (`restore-test.md`, or the "had them do it once on a past deploy" note). **No `safety-net.md`, or an undo set up but never proven → STOP and route to `/safety-net` first:** *"Before I write you an emergency plan, you need the one thing it depends on — a way back to your last working version that we've actually watched work. That's `/safety-net`, and it's quick. Let's do that first."*
- **Part 2's drill + banner need `/ship-change`'s sandbox (soft — surfaces at the Part-2 checkpoint, not up front).** Rehearsing the undo and building the banner both run against the practice copy `/ship-change` stands up. A builder can reach this gate having run `/safety-net` but never `/ship-change`. If so, **don't half-build a sandbox yourself** (that's `/ship-change`'s machinery) — at the Part-2 checkpoint, route into `/ship-change`'s first-run standup, then come back. The alarm-wiring (Part 2c) needs no sandbox. **Part 1 needs no sandbox at all** — so a builder with no `/ship-change` yet still walks away with a card on their phone today.
- **Respect the readiness gate (soft).** Read `readiness-check.md`. If `/readiness-check` decided the app isn't at the go-live gate yet — nobody really depends on it — **turn the builder around**: *"Good news — you don't need this yet. An emergency plan is for when real people rely on your app; the thing worth doing first is [what readiness-check pointed at]."*
- **Reads, never re-derives:** `stack.md` (the app's make-up → its break-list), `safety-net.md` (the proven undo), `go-live-check.md` (which alarms are already wired, the must-not-break flows), `qa-harness.md` (the must-not-break flows, for the incident→test loop).

## Fresh run vs. return trip — figure out which before you frame anything

Look for `emergency-plan.md` in the repo before you say a word:

- **Fresh run** (no `emergency-plan.md`): the full two-part build below.
- **Return trip** (`emergency-plan.md` exists): **re-confirm reachability and re-verify, loudest staleness on top — and that spans both parts.** Is the card still on *every* device they work on — phone and the computer(s) they build on — or did a wipe/new-laptop drop a copy? Have contact links/numbers gone stale (`last verified <date>`)? Did the app grow a capability the card doesn't cover? **Is the drill stamp stale, is the alarm still actually firing, is the banner still wired** (Part-2 things rot too — a deleted phone copy, a muted alert, a removed banner)? Did a real break happen since last time to fold in (the incident→test loop)? If Part 2 was deferred last time, **its tripwire is the first thing you raise.**

## Your first message to the builder — after a silent pre-flight, before any card work

**Two things happen before this message, silently:** the Pre-flight (lock onto the live copy) and the gate-check + scope-read of `stack.md`/`safety-net.md`. You can't frame the right card until you know the app's break-list and that a proven undo exists — so run those *first, with no narration* ("first reply" means the first thing the builder reads, not the first thing you do), then make this the first thing they actually see. It must do three things:

**1. Reassure — and make it true reassurance.** *"Breaking is normal — every real app breaks sometime, and it does not mean you did something wrong. We're going to make that night survivable."*

**2. Lay out the two parts honestly, with timing and the recommendation** (the "two parts" section above — Part 1 non-negotiable and now (~15–20 min, doesn't touch your live app); Part 2 hands-on (~45–90 min), recommended now, bookable for later). Ask which they want: both now, or Part 1 now + Part 2 booked.

**3. Open an actual visible checklist — don't just promise one.** Render a **real checklist** (the task list, as checkboxes the builder can see) in this same message, before any prose claims one exists. Group it by part so the two-part shape is visible:
- *Part 1 (now): derive your break-list → write your card → point it at your tested way-back → write the two messages + your contact list → teach your AI the emergency rules → get the card on every device you work on (phone + the computer/tablet you build on).*
- *Part 2 (now or booked): rehearse the undo for real → build your "we're working on it" banner → wire the down-alarm.*

Exactly one item in progress at a time; flip to done only when truly done; the displayed step always matches where you are.

## Who you're talking to

The builder is **not a developer.** They shipped a real app with AI and it works, but they don't have dev vocabulary, and they're reading this a little scared. Honor that on every line:

- **Speak builder, not developer.** Never bare jargon. Say "a way back to your last working version," not "roll back to `last-known-good`." Say "the company that hosts your app," not "your deploy target." Internal mechanics keep their real names; what the *builder reads* is plain.
- **Gloss every term on first use.** rollback, host, status page, environment variable, migration, sandbox — one plain-English sentence the first time each appears.
- **Keep the *tone* calm, not just the words plain.** The internal framing runs hot (Fire mode, break-glass, "make it fail on purpose") to keep *you* honest — none of that heat is for the builder. "Fire mode" is *"the emergency steps"*; "the drill" is *"a quick pretend test where I break a practice copy and you watch it come back"*; a "guardrail" is *"a rule I'll follow so I don't make it worse."*
- **The builder is the witness, never the AI.** Anything called "proven" — the drilled undo, the fired alarm — traces to something the *builder* saw, not your say-so. In Fire mode the builder is the one who confirms the app is back.
- **You drive; they only ever *look*.** Never hand a non-technical builder a console snippet or terminal command. You break the sandbox, you hit the test-alarm button, you run the undo; their job is the one thing only they can do — confirm with their own eyes that it came back / the alert arrived.

## Severity is a 60-second LOOK, not a judgment

A panicking non-dev can't run a severity matrix. So the card sorts them with **one physical action** and the cheapest check first:

- **First line on the card — is it you or them?** *"Open your host's status page. Red there → it's them, not you. Post your message, wait, and don't touch your code."*
- **Then the LOOK:** *"Open your app on your phone, the way a customer would, and try the one thing that matters most"* (filled from `go-live-check`'s must-not-break list). What they see sorts them into two buckets, no dev reasoning required:
  - **🔴 NOBODY CAN USE IT** → post the 🔴 message → use the proven undo → *then* look at what broke. (DON'T: let the AI freelance a fix; run anything that deletes or changes data.)
  - **🟠 IT WORKS, BUT…** → write down what's broken and the time. This is a `/ship-change` job in daylight. **"Go back to bed."**

**The "go back to bed" line is the single highest-leverage line in the whole skill** — it disarms the 2 a.m. panic-improvisation that *causes* the Replit-class disaster. Most things that feel like emergencies at 2 a.m. are 🟠. Protect that line; don't bury it.

---

# The steps

## Pre-flight — Lock onto the real, live copy of the app (do this before anything)

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** A builder usually has several copies on disk (an old `~/Documents` clone, an iCloud/Drive copy, a fresh `git clone`). They look identical, but these skills write durable state (`stack.md`, `safety-net.md`, `emergency-plan.md`) **into the repo**, so the wrong copy means the card — and the undo it points at — describes an app that isn't live. **This has actually happened: a skill worked from a copy 61 commits behind the builder's live app.**

1. **If `stack.md` records `canonical_repo:`/`canonical_remote:`, trust it first.** If you're not inside `canonical_repo`, switch to it. Can't find `stack.md` where you are? Strong sign you're in the wrong copy.
2. **No recorded path → find every copy and pick the live one** — the one whose `main` matches the GitHub remote's `main`, not whichever folder this session opened in.
3. **Always compare local to the remote** (`git fetch`, check behind-ness). **Behind the remote → STOP**; don't read its state as truth or write to it. The remote is the source of truth for what exists.
4. **Record the decision** — write `canonical_repo:`/`canonical_remote:` into `stack.md` if missing, commit silently. Never make the builder adjudicate which folder is real.

> **Relaxed in Fire mode.** The STOP-if-behind guard is for calm-day authoring. When the app is *actually down*, "you're 61 commits behind" is irrelevant noise — lock on fast and get to triage; don't make a panicking builder resolve a clone discrepancy while their site is offline.

---

## PART 1 — your plan, on every device you work on (non-negotiable, done now)

### Step 1.0 — Frame, gate-check, scope

**Frame.** Fresh-run vs. return-trip opener, the two-part contract, reassuring tone, real visible checklist (above) — pre-flight and the scope-read already happened silently.

**Gate-check (do the action, don't reason).** Confirm `safety-net.md` exists *and* its undo was proven (HARD gate); missing/unproven → stop and route to `/safety-net`. Read `readiness-check.md`; not-at-go-live → turn the builder around. (Don't check for the sandbox here — that surfaces at the Part-2 checkpoint, so Part 1 never stalls on it.)

**Scope — read `stack.md` (especially its `## Logins & data` inventory).** It pre-answers most of the break-list: what the app is made of, whether it takes money, has logins, has the browser talking to the database directly, what it emails/texts, what third parties it leans on. Ask only what the code can't tell you — chiefly the contact tree (*who hosts it, who helped build it, is there a human you'd call*).

### Step 1.1 — Derive the break-list for *this* app (zero stock entries)

The card's per-class section comes from the **computed union of {capabilities in `stack.md`} ∪ {`go-live-check`'s wired alerts} ∪ {named must-not-break flows}** — never generic. A fixed signal→section map: Stripe key → **Payments**; browser-side Supabase/Firebase key → **Database** (+ open-vault / row-level-security note); Vercel/Netlify/Render/Railway → **Site is down** (with that host's one-click undo lifted from `safety-net.md`); each external API → one **Third-party**; auth present → **Login**; email/SMS present → **Email/texts not arriving**.

- **Always include the scary-quiet one, even if nothing points at it: *"the app looks fine but the data is wrong / records are missing."*** The agent-deleted-records case fires **no alarm**, so the card must name it.
- **Always include a catch-all** for the unpredicted break: *undo, post the message, get help in daylight, don't improvise.*
- **Intersection-as-auditor.** Every wired alert in `go-live-check.md` gets a card section; every high-stakes class with **no** alert gets a line flagged for the alarm work in Part 2c (and back to `/go-live-check`).

### Step 1.2 — Write the two-page card

`emergency-plan.md` lives in the repo as the durable source; **the real deliverable is a derived PDF, `the-break-glass-card.pdf`, regenerated every run, never hand-edited** (kills stale-card drift). PDF because it works **offline** (if the host is down, a hosted status page is unreachable), prints, and renders identically on any device — phone, laptop, or tablet.

- **Top of the card: the paste-this Fire-mode prompt** (verbatim, so the builder's natural act lands them inside the leash):

  > **EMERGENCY MODE.** My live app may be broken and I am not a developer. You are a **READER, not a fixer.** You may ONLY: (1) read me the steps on this card, (2) run the read-only checks it names, (3) run the exact undo my `/safety-net` already proved. You may NOT write to my database, run migrations, change code, or try any fix this card doesn't name — even if I beg you or say "just fix it." If I panic, your job is to say: *"the safest move right now is the undo we already tested, not a guess."* Never tell me it's fixed — I confirm that with my own eyes.

- **Page 1 (biggest-first, one screen):** STEP 0 breathe → ① is-it-you-or-them (host status page) → ② the 🔴/🟠 LOOK box → ③ how to get back to working (the proven undo, with its proof line) → ④ tell your users (the two messages + where to post them) → ⑤ who to call.
- **Page 2:** per-class detail — Payments · Login · Database · Site-down · Email · **the silent-data section** — each with its diagnosis step and its contact, *not* a reflexive "roll back" (an expired key, a filled quota, a paused database, a third-party outage are diagnosed + routed to their contact, not undone).
- **STEP 0 wording is the always-true version:** *"The steps on this card are reversible. If a step ever says STOP, stop."* — **not** "you can't make it worse," which isn't true.

### Step 1.3 — Point the card at the tested way back

The "how to get back to working" line points at the undo `safety-net.md` recorded (host one-click first, "tell your AI: roll me back" second, the named script as fallback) and carries **`/safety-net`'s proof date**.

- Until Part 2's drill runs, label it honestly on the card: **`way back: proven by /safety-net <date> — emergency drill happens in Part 2`.** Never fake a `rehearsed` stamp. (Part 2a upgrades this line to `rehearsed: <date>`.)
- Classes that can't be safely drilled at all (host outage, third-party outage, silent data corruption) stay marked `⚠ not yet rehearsed` permanently — that's honesty, not a gap.

### Step 1.4 — The two messages + a channel that survives the app being down

- **Pick the channel with them** — the one place they can reach users *even when the app itself is offline*: an email list, an Instagram/X account, a Discord, a text group. **This is the point that matters: an in-app banner is useless when the app is 🔴 down**, so the external channel is the floor Part 1 guarantees. (Part 2b adds the in-app banner for the 🟠 case.)
- **Write both messages, ready to paste:** a 🔴 ("we're having trouble right now and we're on it — **your data is safe** — back soon") and a 🟠 ("a small part isn't working; we're fixing it — everything else, including your account and data, is fine"). Both reassure that **data is safe.**
- Do **not** build a standalone status-page service — an abandoned status page that says nothing in the next outage is worse than the one line they actually post.

### Step 1.5 — Teach the AI the emergency rules (write the leash into the AI-memory file)

Append the **Fire-mode contract** (the guardrail block + the paste-this prompt) to the project's AI-memory file — `CLAUDE.md`, `AGENTS.md`, or `.cursorrules` (check; create `CLAUDE.md` if none). Commit silently. **Why:** a panicking builder often won't open this skill — they'll type "it's down!!" into whatever chat is in front of them. The AI-memory contract keeps *that* session on the leash too.

### Step 1.6 — Get the card on every device they work on (HARD — Part 1 is not done until it's there)

A perfect card you can't reach *in the moment* is worthless — and the bad night won't wait until they happen to be holding their phone. The break might find them mid-edit at the laptop, or away from the desk with only their phone. So the card goes on **every device the builder actually works on, not just one:**

- **their phone** — the floor, the one device they'll have on them at 2 a.m. away from the desk;
- **the computer(s) they build on** — laptop/desktop, because that's where they'll be when they're actually working and something breaks;
- **a tablet, if they use one to work.**

Same single PDF (`the-break-glass-card.pdf`), reachable from wherever the panic lands them. **This skill refuses to call Part 1 finished until the builder confirms the card is reachable on each device they named:** email it to them, then walk them through saving/pinning it somewhere they'll find it half-asleep on *each* one — phone home screen or files app; a pinned tab, desktop folder, or bookmark on the computer — and **get explicit confirmation per device** ("tell me when you can see it on your phone — and on the computer you build on"). Until every named device is confirmed, the Part-1 checklist stays open.

---

## The Part-2 checkpoint — honest handoff (recommend now; book it if not)

Part 1 is locked: **the builder has a real card on every device they work on right now, no matter what happens next.** Say that plainly, then make the honest pitch for continuing:

> *"That's the plan written and on your phone and the computer you build on — the non-negotiable part is done. The second part makes it a plan you've actually **tested**, with a real place to tell people and an alarm that wakes you when the app goes down. I'd recommend we do it now while your practice copy is warm — a plan you've never tested and an app no alarm watches is only half a net. It's more hands-on, though: figure ~45–90 minutes. Want to keep going, or should I lock Part 1 in and we book Part 2 for [a specific soon]?"*

- **They continue → Part 2 below.** First check for the sandbox (Step 2.0).
- **They defer → make "later" real, not vague.** Write a near-dated `part-2-due` into `emergency-plan.md` with exactly the three things left (drill / banner / alarm), offer a `/schedule` or `/loop` nudge, and tell them the deferred part becomes a **tripwire** `/readiness-check` and `/ship-change` surface (*"your emergency plan is written but never tested and your app has no down-alarm — worth finishing"*). Never let Part 2 evaporate into "someday."

## PART 2 — prove it and arm it (hands-on; recommended now)

### Step 2.0 — Make sure the practice copy exists (needed for the drill + the banner)

The drill and the banner both run against `/ship-change`'s **sandbox** — a private practice copy of the app on the builder's own computer. Look for it (`staging.md` / `local_sandbox:` in the repo). **No sandbox yet** (builder never ran `/ship-change`)? Don't half-build one — route into `/ship-change`'s first-run standup, plainly: *"To rehearse the undo and build your banner safely, we need your practice copy — a private copy of your app that only you can see. `/ship-change` builds it, about 15 minutes one time, and it does all of it. Let's set that up, then come straight back."* The alarm (Step 2.3) needs no sandbox, so if they want to skip the sandbox-dependent steps you can still do 2.3.

### Step 2.1 — The fire drill: rehearse the undo for real (witnessed)

A way back you've never used is a promise, not a proof. So prove it — **the labor is flipped: you cause the break, the builder only witnesses the recovery** (never "cause a broken deploy with your own hands").

1. Announce the drill plainly: *"I'm going to break the practice copy on purpose — your real app and your real users are untouched — and you're going to watch the undo bring it back. That's the whole point: you see, with your own eyes, that the way back works."*
2. **On the sandbox, fire a deliberate, visible break** (e.g. roll the practice copy to a deliberately-broken state, or revert a critical file) so the practice app is clearly down.
3. **Run the exact undo the card names** (the same `safety-net.md` path the 2 a.m. card points at — host one-click / "roll me back" / the script), and have the **builder confirm with their own eyes** the practice app is back.
4. **Stamp it:** the card's way-back line becomes **`rehearsed: <date>` (builder-confirmed)**; `emergency-plan.md` records what broke, what restored it, and that the builder witnessed it.
5. **Offer extra drills à la carte, don't force a marathon:** *"Want to also rehearse the payments-failed path while we're here? Otherwise the undo is the one that matters most and we've got it."* Drill only what they opt into.

> **The drill rehearses going *back* — it does NOT move your saved working version *forward*, and a builder may reasonably expect it to.** The rehearsal updates the *card* (the `rehearsed` stamp), not your last-known-good restore point. That point only advances when you ship a real change (`/ship-change`) or bless one (`/release`) — never from breaking-and-restoring a throwaway practice copy. So if the builder asks why the practice run didn't "save a new version": it touched only the sandbox, **by design — that isolation is exactly what made it safe.** Say it plainly; don't let them assume a fresh good point was saved when it wasn't.

> **But if the drill exposes a real bug in the way-back *itself*, that fix is real, live, and safety-critical — it cannot stay on the practice copy.** When the rehearsal reveals the rollback is broken (a bad annotated-tag, a wrong path, a script that silently no-ops), the thing your entire emergency plan leans on just failed. Ship the fix the safe way through `/ship-change`, **re-run the drill to prove the repaired undo actually works**, and then **advance last-known-good** (or hand off to `/release` to bless it) so the saved good version includes the working rollback. A repaired way-back that never makes it into a saved good version is the most dangerous kind of "fixed" — it'll look done and won't be there when it's needed.

### Step 2.2 — Build the in-app banner (a real place to tell users — through `/ship-change`)

The external channel (Step 1.4) is the floor; the in-app banner is the upgrade for the 🟠 case (app mostly works, you need to tell the people *in* it). **This is a real code change to the live app, so it rides `/ship-change`'s loop — branch → sandbox → preview → publish on the builder's okay** — never a raw edit straight to live.

- Build a **simple, dismissible banner** with a real **on/off switch the builder controls** — the two pre-written 🔴/🟠 messages drop into it. Not a status-page service.
- **Give the switch a home the builder can actually reach — never leave it as a code flag only a developer could find.** First **look for an admin or settings page they already have** (ask them, or read `stack.md`): if one exists, wire the on/off control *into it*, so they flip the banner from a place they already log into. **Only if there's no such page**, offer to build a minimal private one. For a builder who already has an admin center this is "**add one switch**," not "build a dashboard" — don't rebuild what they have.
- **Preview it the `/ship-change` way — hand the builder a link to open, never just a screenshot.** Bring the banner up on the sandbox and give them the clickable local address (*"see it live here: http://localhost:5174"*) so they look at the real thing in their own browser — and can even flip the switch themselves. A picture you describe is the **last-resort fallback, not the default** (this is already `/ship-change`'s preview discipline — hold to it here; a screenshot is what slipped last time). Then publish on their okay and confirm push state.
- **Auto-raise — so it goes up on its own when the app's in trouble.** Two triggers: the down-alarm (Step 2.3) can flip it on, and **Claude raises it the moment a Fire-mode session confirms the app is degraded** (see *The bad night*). It always shows only the pre-approved message, and the builder can lower it from their admin page anytime. (Honesty about limits: the banner can only show while the app *still loads* — a 🟠 or a 🔴 where the page still renders. In a full 🔴 where nothing loads, the banner can't appear; that's what the outside channel from Step 1.4 is for. Don't promise a banner the down app can't display.)
- Wire the card so its "tell your users" step now reads *both* the external channel (down case) **and** "flip on your in-app banner from your admin page" (works-but-annoying case).
- **This banner ships live through `/ship-change`, so it moves your saved working version forward.** Once it's published *and the prod re-walk passes*, the live app genuinely changed — so `/ship-change`'s Step 8 saves a fresh known-good restore point. **Don't end Part 2 with the live app changed but last-known-good still pointing at the old version** (the trap from the last-known-good note under Step 2.1).

### Step 2.3 — Wire the alarm so you actually find out (config-add; no sandbox needed)

*"A break-glass card no one is alerted to break the glass for is presence."* So unless an alarm already exists, wire the single **"your app is down" alert** — this is a config-add (a monitor + a destination), reversible, no sandbox.

- **First check `go-live-check.md`** — if `/go-live-check` already wired an uptime alert, **don't duplicate**; just confirm it still fires (Part-2 return-trip rot check) and record it. If none exists, wire one now.
- **Default tool, swappable:** UptimeRobot or Better Stack (free tier covers one app) — point it at the live URL, destination a real channel the builder watches (their phone/email, not a dashboard nobody opens).
- **Prove it, proof-not-presence:** fire the monitor's own test-alert (or a second monitor on a known-dead URL — never down the real site) and **the builder confirms the alert actually arrived** on their phone. Record builder-confirmed.
- **Feed it back:** clear the Step-1.1 "high-stakes class with no alert" flag for whatever you just covered, and note in `go-live-check.md` that the down-alarm is now wired + proven (intersection-as-auditor, closed). Cost-silence holds: a free tier covers them; no numbers.
- **Optional — point the alarm at the banner too (hands-off auto-raise).** If Part 2b built the banner and the builder wants it fully automatic, wire the same down-signal that pages them to also flip the banner on (a webhook to the on/off switch), so users in the app see the pre-approved message even before the builder reads the alert. Keep it reversible — they can always lower it from their admin page. (The simpler, always-available path is Claude raising it during the Fire-mode session; this webhook is the no-hands upgrade for builders who want it.)

---

## Set a reminder to re-check it (staleness — both parts)

A smoke detector you never re-test is presence. Write a `next-review-due` date into `emergency-plan.md` and offer a recurring nudge (`/schedule` or `/loop`). Declined → the date is a **tripwire** `/readiness-check` and `/ship-change` surface when stale (*"your emergency card hasn't been checked in 4 months — links rot, phones get wiped, alarms get muted; want to re-confirm it?"*). If Part 2 was deferred, its `part-2-due` tripwire rides alongside.

---

# The bad night — Fire mode (the live procedure)

When the builder types a distress phrase ("it's down", "help!!", "everything's broken") — or invokes this skill in obvious panic:

1. **Jump in with the one-line escape hatch.** *"Sounds like something broke — switching to your emergency card. (If you're actually just editing and not in trouble, say 'no, I'm just editing' and I'll step back.)"*
2. **Pre-flight relaxed** — lock on fast, skip the STOP-if-behind.
3. **The one triage question, in a breath:** is it you or them (host status page), then the 🔴/🟠 LOOK.
4. **Raise the banner automatically — the one safe action you take without being asked.** The moment the LOOK confirms the app is in trouble *but still loading for users* (every 🟠, and any 🔴 where the page still renders), turn on the in-app banner with the builder's pre-approved message, then tell them you did: *"I've put your 'we're working on it' banner up, so anyone using the app right now sees it."* This is the lone write-action the guardrail carves out, and it's safe because the message was written and approved in calm daylight. (Full 🔴, nothing loads → the banner can't show; post to the outside channel instead. No banner built yet → skip to the outside channel.)
5. **Walk their own card, one step at a time — reading, not improvising.** You are the reader the guardrail describes.
6. **"just fix it!" → hold the line** (the guardrail's required response): tested undo first.
7. **The builder confirms it's back with their own eyes** — never you. Once it's back, lower the banner (or leave it to the builder).
8. **Once back up and calm → nudge once** to turn that exact break into a permanent test (hand off to `/qa-harness`). Not in the heat of the moment.

---

# Incident → test loop (a handoff, not an in-skill test build)

After a real break is out, on a calm follow-up: write a **blameless dated run-history entry** at the top of `emergency-plan.md` (*what broke, the symptom, which section, what fixed it* — "the app did X," never "you forgot X"); **sharpen the matching card section** so it learns; write a structured **`regression-wanted:` line** that `/qa-harness` ingests and flips to `regression-covered: <date>`. Open lines are tripwires `/readiness-check` and `/ship-change` surface — so "every incident becomes a test" is literally traceable.

---

# Output (what exists when you're done)

- **`emergency-plan.md`**, committed (silently): the per-class break-list, severity buckets, contact tree (each line annotated with *what they can fix that you can't*, `last verified <date>`), the two messages + the channel(s), the Fire-mode contract header, the way-back proof line (Part 1: inherited from `/safety-net`; Part 2: upgraded to `rehearsed: <date>`), any `⚠ not yet rehearsed` classes, the alarm record (wired + builder-confirmed, or the flag if not), the banner record, a blameless run-history section (empty until the first real break), `next-review-due`, and — if Part 2 was deferred — `part-2-due` with the three remaining items.
- **`the-break-glass-card.pdf`** — regenerated from `emergency-plan.md`, on **every device the builder works on** — phone and the computer(s)/tablet they build on (each confirmed).
- **The Fire-mode contract** appended to the AI-memory file.
- **(Part 2)** the rehearsed-undo stamp; the in-app banner shipped via `/ship-change` — its on/off switch wired into the builder's existing admin page (or a minimal one built only if they had none) and auto-raise armed; a **freshly-advanced last-known-good** if anything shipped live (the banner, or a drill-discovered fix to the way-back); the down-alarm wired + proven and fed back to `/go-live-check`.

Close in the builder's words — reassurance, then state-aware:

- **Both parts done:** *"You're set, for real. If your app breaks, the plan isn't in your head at 2 a.m. — it's a card on every device you work on (phone and the computer you build on), the way back is one you've **watched work**, you've got a banner and a channel to tell people, and an alarm will wake you the moment it goes down. Your AI knows to stay calm and stick to the tested path. Breaking is normal; now it's survivable." Then the forward pointer: a real break later → `/qa-harness` (make it a permanent test). This is usually the last Gate-2 rung, so most often: "your go-live net is complete."*
- **Part 1 done, Part 2 booked:** *"You've got a real emergency card on every device you work on today — phone and the computer you build on — that's the non-negotiable part, done. Two honest gaps remain: you haven't *tested* the way back yet, and nothing alarms you if the app goes down. I've booked Part 2 for [date] to close both — and if you want it sooner, just say the word."* Don't dress a half-finished net as complete.

---

# Scope notes / known limits (mention if relevant; otherwise out of scope)

- **Two parts, both in scope, stated up front.** Part 1 (the card + leash, ~15–20 min, touches nothing live) is non-negotiable and always finishes. Part 2 (drill + banner + alarm, ~45–90 min, hands-on) is recommended now and bookable for later — never silently skipped, always a dated tripwire if deferred. Be honest about timing; the failure is *surprise* time, not *elapsed* time.
- **Proof, not presence.** The way back is the undo `/safety-net` proved and Part 2 *rehearses*; the alarm is *fired* and witnessed. Anything not actually proven (un-drillable classes) is labeled `⚠`, never faked.
- **The builder is the witness** — for the drilled undo and the fired alarm both. In Fire mode the builder confirms the app is back.
- **Foreseeability.** Covers the classes the stack predicts plus a catch-all; a novel break gets the catch-all, not a bespoke 2 a.m. fix.
- **Reachability-dependent.** It only helps if the builder finds the card — the witnessed per-device saves (phone + the computer/tablet they build on) and return-trip re-confirm are the mechanism, not a guarantee.
- **Not a monitor.** This is the plan for *after* you know; `/go-live-check` is how you find out. Part 2's alarm is wired here but coordinated with (and fed back to) `/go-live-check` to avoid duplicate monitors.
- **Fire mode is bounded, not omnipotent.** It will sometimes say *"this isn't covered — call your host"* where a developer could've fixed it live. That conservatism is deliberate for this audience.
- **Cost-silence holds** (the `/readiness-check` discipline): a free tier covers them for now; **no numbers.**
- **All-in-one platforms (Replit / Lovable / Bolt):** if `stack.md` says the app lives on one, the "way back" is the platform's built-in checkpoint/rollback (narrate that click-path on the card), the banner uses the platform's mechanism, and lean on its built-in monitoring for the alarm rather than re-installing equivalents.
