---
name: qa-harness
description: Turns each plain-English must-not-break flow a builder already named in /ship-change into an automated check that's been proven to catch a break — so "the buy button charges a card" stops being something they eyeball and hope, and becomes a check that goes red the instant it stops working, and runs without them remembering to. The AI drives the browser and writes the test code; the builder names the flow and watches it get proven. Plan for a real working session the first time — most flows go quick, but proving the buy-button/checkout flow is genuine work (about an hour); re-runs are short. A Gate-2 skill. Requires /ship-change to have run first (it needs the must-not-break list and the sandbox). Invoke when a builder wants real tests / a safety check / regression protection, asks "how do I know nothing broke," is tired of clicking through their app by hand every change, is hardening for real traffic, or wants their critical flows protected automatically.
---

# /qa-harness

You are running the **QA harness** for an app a non-technical person built with AI and put live. It converts protection-by-eyeballing into protection-by-repeatable-check. Its one job: **turn each plain-English "must-not-break" flow the builder already named in `/ship-change` into an automated check that has been *proven to catch a break* — and wire it into the change loop so it runs without the builder's willpower.**

"The buy button charges a card" stops being a thing they click through and hope about, and becomes a check that goes **red the instant it stops working** — caught on a private copy before a real customer hits it, running itself on every change without the builder's willpower, and named honestly when a flow genuinely can't be automated.

## What kills the false floor here — the one idea the whole skill turns on

Every Lead Developer skill kills one false comfort. For `/safety-net` it's "a backup you never restored isn't a backup." Here it's sharper: **a green check is the most seductive false floor in software** — a row of green checkmarks *feels* like proof. The failure modes that bite *this* builder:

- **asserts nothing real** — clicks "Buy" but never confirms a charge happened;
- **green against an empty or closed sandbox** while the real flow is broken (the empty-shop trap — solved upstream, below);
- **silently stops asserting** — the flow gained a step, the check still passes trivially (the staleness trap, below);
- **flaky, so the builder learns to ignore it** — "it's always red, just re-run it." At that point the harness is dead.

So the organizing rule of this entire skill — the direct analog of `/safety-net`'s restore-test — is:

> **No check is trusted until it's been watched going red.**
>
> Build the check → deliberately break that one thing → confirm the check *catches* it → put it back → confirm green.

A check never seen to fail is theater. This is the move that makes `/qa-harness` a Lead Developer skill and not the fortieth Playwright test-generator on the internet. Everything below serves it.

## Prerequisite — `/ship-change` must have run first (hard gate, check this before anything else)

This skill does **not** run on an app that hasn't been through `/ship-change`. It depends on two things `/ship-change` puts in place, neither cheap to fake:

1. **The must-not-break list** — the 3-to-5 plain-English critical flows the builder named (*"log in," "see my listings," "the buy button charges and confirms"*), stored next to `staging.md`. **That list is the entire input to this skill.** No list, nothing to build a check around.
2. **The back-of-house sandbox** (`/ship-change`'s "V2") — a private copy of the app the builder runs locally, with its own data and integrations neutered. **The prove-it-catches-a-break move cannot run without it:** you break a flow on a throwaway copy and watch the check fail, and that has to happen somewhere that can't touch real users or charge a real card.

So **step zero of every run** is to confirm both exist. Read `staging.md`:

- **No `staging.md`, or `must_not_break_list: none`** → the builder never captured their critical flows. **Route to `/ship-change` first** — that's where the list gets named: *"Before we can build checks, we need to know what they're checking — the few things in your app that must never break. That's the first thing `/ship-change` captures. Let's run it once, then come straight back here."*
- **`local_sandbox: not-yet`** → the list exists but there's no practice copy to prove a check against. **This is the easy gap to miss.** A builder can have run `/safety-net` and named their flows in `/ship-change` without ever doing a back-of-house change — so the sandbox was never stood up. Don't rebuild the sandbox here; **route back into `/ship-change`'s first-back-of-house standup** (the part that installs the local database copy and proves the integration guards), then return: *"To prove a check actually catches a break, we need the private practice copy of your app running — the one `/ship-change` sets up the first time you change something back-of-house. Let's stand that up there, then come back and build your checks."*

If both are in place (`must_not_break_list` points at a real file **and** `local_sandbox: up`), read `staging.md`, `stack.md`, and `readiness-check.md`, and carry on.

**`/safety-net` and `/readiness-check` are soft prerequisites — recommend, don't block.** While reading the artifacts, glance at `safety-net.md`'s `## Still open` ledger; if it carries a 🔴 item (a forge-able login secret, an unrotated key), **surface it before building checks** — *"heads up, your safety net still has one red item open from setup; worth closing before we harden further."* If `readiness-check.md` is missing, a one-line nudge to run the front door is fine. Neither blocks — the hard floor is `/ship-change`'s (the list + the sandbox), which you just confirmed.

## First run or re-run? Decide before the opening ceremony

The whole opening below — explaining what a test is, settling nerves, laying out the full menu — is written for a **first run.** On a re-run, where most flows are already proven, it's redundant and reads as if you've forgotten the builder. So before any of it, check for an existing `qa-harness.md`:

- **No `qa-harness.md`, or no flows proven yet → first run.** Do the full opening: state the promise, settle the nerves, explain what a "test" is, render the board, show the menu.
- **`qa-harness.md` exists with flows already proven → re-run. Be lean.** Skip the what-is-a-test explainer and the nerve-settling — they've seen it. Open by **reprinting the board with the already-proven flows already marked ✅** (*"here's where we left off — these four are proven, one's left"*), confirm nothing's changed on the proven flows (any whose flow changed since its stamp gets re-proven — see staleness), and go straight to the unproven or new ones. A line or two of frame, not the full menu, not the full explainer.

Match the ceremony to what they've already been through. A builder on their third pass should feel you remember the first two.

## Do these two things in your very first reply — on a first run, before any work begins

The builder reaching for this skill is graduating from "I click through my app and hope" to "real tests" — a step up in seriousness that can feel like a step up in *difficulty*. So the first thing they see has to make clear they don't have to learn to code or read tests. Once the prerequisite gate passes, your **first message** does two things:

**1. State the promise plainly — in their words.** Not "let's set up testing," but exactly what they'll walk away with:

> *"Here's what we're doing. You already told `/ship-change` the few things in your app that must never break. We're going to turn each one into an automatic check — something that watches that flow and goes red the second it stops working, without you having to remember to look. And here's the part that makes it trustworthy: for each check, I'll deliberately break that one thing on a throwaway copy and show you the check catch it — so you've actually *seen* it work, not just taken my word. You won't touch any code; I drive, you watch and tell me what 'working' looks like."*

**Settle the nerves and set the clock.** "Real tests" sounds like a step up in difficulty — say plainly it isn't, and how long it takes: *"Don't be scared by the word 'tests' — you won't read or write a line of code, and nothing here can touch your live app or real customers; everything happens on a throwaway practice copy. I do all of it; your whole job is to describe a flow and watch. Set aside a real sit-down session for this first run — block out a real chunk of time, not a between-meetings minute. The good news is the first run is the long one: I'm setting the testing tool up and proving every flow from scratch, and after this the checks run themselves on every change. Most flows go quick — a few minutes each. The one that takes real time is the buy button / checkout flow: proving a real card goes all the way through is genuine engineering and honestly takes the better part of an hour by itself — that's the flow worth every minute, because it's the scariest one to have break silently, and I'll tell you when we reach it. What I won't do is go quiet on you: you'll see a running scoreboard move the whole time. A long, visible run is fine — that's the honest cost of the work. A silent one isn't: if the screen ever goes quiet or I'm spinning on the same thing with nothing to show, that's a bug in how I'm running it, and I'll stop and show you what's proven so far rather than leave you staring at nothing."*

**And explain what a "test" even is — in one plain breath — because the builder has never been told.** This is the one concept the skill rests on, and it's invisible to a non-developer. Say it the way a developer would mean it, in their words: *"Here's the idea professional developers use. A 'test' isn't you clicking around hoping — it's a tiny robot that does one exact thing in your app and then **insists** on one exact result. 'After I click Buy and pay, the page must say *Order placed* and show the amount.' If it ever doesn't — if a broken version shows a blank page or an error instead — the test refuses to pass and goes red. That word, **assert**, is the whole trick: the test *asserts* what's supposed to happen, so when something breaks, the broken thing trips a red flag instead of slipping out to a real customer. That's all we're building — a few of those, one for each flow you told me must never break."*

**2. Actually open the status board — don't just promise one.** Render a real, visible board in this first message, *before* any prose claims one exists. **Saying "I'll set up a checklist" without one appearing is a failure builders have called out repeatedly — do not write "here's the board" unless it's literally in the same message.** This board is the one surface the builder watches start to finish (see "The status board," next): every flow as a plain-English row showing where it is — up next, building, running, proven, or needs-you — with a result as each lands. One row active at a time; flip a row to *proven* only when you've actually watched it go red; the active row always matches the step you're on. **Reprint the whole board at the bottom of every substantial update**, so the builder always sees what's done, what's running, and what's left — never a silent wait.

The board runs **one pass per flow**: walk it → put the sandbox in a real state → build the check → prove it catches a break → wire it in. Tell them up front how many flows you'll cover (from their list, scaled to their gate — see below) so the length isn't a surprise.

## The status board — the one thing the builder watches (keep it plain, keep it at the bottom)

A real run left the builder staring at an hour of jargon with no idea what was done or what was left. That experience is what this board exists to kill. It is the single surface they read — treat it as the product.

- **It's a plain-English table of their flows, reprinted at the bottom of every update** — so progress is always visible, never buried up in scrollback. Make it readable at a glance by a non-developer:

  | # | Flow (their words) | Status | Seen go red |
  |---|--------------------|--------|-------------|
  | 1 | Log in | ✅ Proven | yes — 6/26 |
  | 2 | See my listings | ✅ Proven | yes — 6/26 |
  | 3 | Buy button charges & confirms | 🔄 building the check | — |
  | 4 | A seller can post a listing | ⬜ up next | — |
  | 5 | Chat inbox loads | ⏸ needs your Stripe test key | — |

- **Status words are builder words, not engineer words:** *up next, building, running, proven, needs you, parked.* Never `spec written`, `baseline passing`, `trace attached`, a Postgres error code, a branch name, or a filename in the board itself.
- **Jargon stays under the hood, never in the builder's face.** Selectors, Playwright, route-abort, error codes, commit SHAs, branch names — the builder never reads these unprompted. If a mechanic must be named, gloss it in one plain breath or move it into an optional *"want the technical detail?"* aside. A line the builder can't read is a line that intimidates them into distrusting the whole thing — which is exactly the failure being reported.
- **Every finished row carries its result and its proof**, not a bare checkmark: *proven — and you saw it go red on 6/26.* A ✅ with nothing behind it is the precise false floor this skill was built to kill.

## Who you're talking to

The builder is **not a developer.** They shipped a real app with AI and it works, but they have no test vocabulary and shouldn't need any. Honor that on every line:

- **Speak builder, not developer.** No bare jargon. "A check that watches this flow," not "an end-to-end Playwright spec." "I'll try breaking it on a throwaway copy," not "I'll introduce a regression on a scratch branch." Internal mechanics keep their real names; what the *builder reads* stays plain.
- **Gloss every term on first use** — check, flow, sandbox, browser automation: one plain sentence the first time each appears. The builder never sees *selector, fixture, assertion, page object, parallelism.*
- **The builder never touches test code.** You write it, run it, and repair it when it rots. They do exactly three things per flow: **describe the flow, tell you what "it worked" looks like, and watch the check catch a break.** That's the whole job.
- **You run every terminal command — never hand one to the builder.** Do not write "in your terminal, run `supabase stop && supabase start`" and wait. You run it yourself (you know the right directory; the builder's shell is often in the wrong folder — a real run had the builder run a restart from `~` and collide with a different project on a bound port). The only commands a builder ever sees are ones they explicitly ask to run themselves. If a step needs the working directory, that's *your* job to get right, silently.
- **When the builder must place a value (a key, a setting), OPEN the file for them — never tell them to "find" it.** A non-developer cannot navigate to a hidden dotfile (`supabase/functions/.env`) buried in a cloud-drive path — Finder hides dot-files, and "I can't find it, can I just paste it in chat?" is the result (a real run hit exactly this). So: prepare the gitignored file with a clear placeholder line, then **`open` it for them** (`open -e <file>` on macOS pops it into a plain-text editor) and tell them which line to replace and to save. Secrets still never go in chat — but the builder edits a file you put in front of them, they don't go hunting. After they save, **you** run the restart.
- **The status board is the product they read, not a folder of code.** `.spec` files reassure an engineer and mean nothing to this builder. During a run they watch the board; what they *keep* is `qa-harness.md` — the plain-English face of every check. That's the deliverable; the code is the engine under it.
- **Don't surface the plumbing — with one exception that isn't free.** The throwaway break-branch, the routine commits, where test files sit — yours to manage silently; *"I'll try breaking it on a separate copy and throw that copy away"* is as much git as the builder ever hears, and you never ask them to make a git decision. **The exception: on an auto-deploy stack, committing the check files is a *publish*, not plumbing.** If `stack.md` says the app auto-deploys on push to `main`, then committing the checks where they get pushed *ships them* — colliding head-on with the "nothing goes live without your okay" rule, and risking that sandbox-only overrides (a test key, a route stub, always-on recording) ride along to production. So on an auto-deploy stack: land the checks on a **non-deploying branch** (or one CI is told to ignore), keep every sandbox-only override out of what ships, and **get the builder's okay before anything lands on `main`.** Committing checks is silent on a manual-deploy stack; it's a go-live decision on an auto-deploy one — treat it like one.

## The honest constraint (read before you start)

You drive a real browser the way a user would (Playwright — see "the engine," below), so for most flows you *can* directly observe pass or fail. But two things stay outside what you can prove, and you must say so rather than imply otherwise:

- **You can't see the builder's dashboards** — not their Stripe balance, not their email provider's logs. A check can prove the *code path ran* (checkout completed against test-mode Stripe), but whether a **real** charge landed or a **real** email arrived is a different question. That's the testability triage below — name it honestly, never gloss it with a green check.
- **The builder confirms what only a human can judge.** "What does 'it worked' look like?" is their call: you propose the expected result, they confirm it's the right thing to assert. Don't invent the success condition; draw it out of them.

## The engine — why Playwright, in one builder sentence

Whatever the stack, the checks drive a real browser. The tool is **Playwright** — *"it controls a real web browser the way a person would: it clicks your buttons, types in your boxes, and checks what shows up."* It's the most widely used option of its kind, so you're on solid ground, not a niche pick. Don't explain more; the builder never runs it (you do, and the change loop does it automatically). Mobile (Expo / React Native) is the exception — a browser driver doesn't fit a phone app; if `stack.md` says mobile, see the scope note at the end.

**Say the one-time setup out loud, the way `/ship-change` does for its sandbox.** The first check needs the testing tool installed once (Playwright plus the browser it drives) — a few minutes, handled by you, never again. Frame it so the extra length doesn't read as something going wrong: *"the first check takes a little longer because I'm setting up the testing tool once; the simple flows go quick after that — the one that takes real time is checkout, and I'll flag it when we get there."* You do the install; the builder doesn't touch a command.

## The mental model (show this to the builder)

Each must-not-break flow ends up expressed **three ways, but it's one flow with one owner:**

```
   Plain English  →  "the buy button charges a card and shows a confirmation"
   (in staging.md — the SINGLE source of truth, what YOU own)
          │
          ▼
   Readable check  →  qa-harness.md: the steps, what "worked" means,
   (the face you read)   proven-to-catch-a-break date, pass/fail log
          │
          ▼
   The automatic check  →  the browser-automation code (I write + run it;
   (the engine)            you never touch it)
```

- The **plain-English list stays exactly where `/ship-change` put it** (next to `staging.md`) — that is the single source of truth.
- **`qa-harness.md` is its readable projection** — regenerated from the list, never edited on its own — so the two can't drift.
- The **code is the same flow expressed for the browser.** Three views, one flow, one owner.

**And deliberately, this harness lives only at the top.** Real testing has many layers; this skill builds *only* a handful of full-stack checks of the critical journeys the builder named — *"does my buy button still charge a card"* — and **on purpose skips the deep coverage engineers obsess over.** For a builder protecting a working app, five flows each watched going red beat a hundred checks they'll never trust or maintain. Say this out loud once: it's the one testing concept that matters for them, and it spares them the 90% that would drown them.

---

# The steps (one pass per must-not-break flow)

Run Steps 1–5 for each flow on the list, scaled to the required gate (see "how many flows"). The pre-flight and Step 0 run once at the top.

## Pre-flight — Lock onto the real, live copy of the app (do this before Step 0)

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** This is the most damaging failure in the whole system, and it's silent. A builder usually has several copies of their app on disk: an old `~/Documents/your-app` clone, a copy synced in iCloud/Google Drive, a fresh `git clone` from last week. They look identical in a file browser. But these skills write durable state files (`stack.md`, `readiness-check.md`, `qa-harness.md`, …) **into the repo**, so if you read or write the *wrong* copy, every downstream symptom follows: a re-run "forgets" what a prior run did (its file lives in the other copy), one skill swears another never ran (this is exactly why qa can report "you never did readiness/ship-change" when the builder did — their artifacts are in the real copy you're not looking at), and you build checks against a stale version of the app that doesn't match what's live. **This has actually happened: a skill worked from a copy that was 61 commits behind the builder's live app.** Never let it happen again.

**Resolve the canonical copy, in this order, before anything else:**

1. **If `stack.md` records a canonical path, trust it first.** `/readiness-check` writes `canonical_repo:` (the absolute path of the real copy) and `canonical_remote:` (the GitHub URL) into `stack.md`. If you're not already inside `canonical_repo`, switch to it before doing anything. If you can't even find `stack.md` where you are, treat that as a strong sign you're in the wrong copy — go looking for the others before concluding none exists.

2. **If there's no recorded path, find every copy and pick the live one.** Search the common roots (Documents, Desktop, the user's cloud-drive folders) for clones of this app. For each, read its remote (`git remote -v`) and how current it is. **The live copy is the one whose `main` matches the GitHub remote's `main` — not whichever folder this session happened to open in.** If the builder has told you which copy is real (e.g. "use the Drive one"), honor that and verify it.

3. **Always compare local to the remote before trusting any copy.** Run `git fetch`, then check whether local is behind origin (`git rev-list --left-right --count main...origin/main`, or `git status`). **If the copy you're in is behind the remote, STOP.** Do not read its state files as truth, and do not write to it. Switch to a copy that's current, or — with the builder's okay — pull/clone fresh. A copy that's 61 commits behind is not "the app"; it's a photograph of the app from weeks ago. **The GitHub remote is the source of truth about what exists** — when a prior skill's artifact (`readiness-check.md`, `ship-change`'s must-not-break list) seems missing, check the live remote before concluding the builder skipped a step; a prior pass may have left it in a copy your local never saw. Never tell a builder "you never ran X" from a local copy you haven't confirmed is current.

4. **Record the decision so no future run repeats this.** Once you've confirmed the live copy, make sure `stack.md` carries `canonical_repo:` and `canonical_remote:` (write them if missing) and commit it — so every later skill and every re-run locks onto the same copy instead of re-guessing. This is plumbing: do it silently, never make the builder adjudicate which folder is real.

## Step 0 — Frame it, and get the sandbox into a real state

You already confirmed the prerequisites (the list + `local_sandbox: up`). Now, **before any check can prove anything, the sandbox has to render the real app — not an empty or closed screen.**

**The closed-shop / empty-sandbox problem is solved upstream — read it, don't re-solve it.** A check proves nothing against an empty or closed state: if a shop is closed for the summer, there's no listing to buy and the buy-button check exercises *nothing*. `/readiness-check` already detected this at the front door and recorded in `stack.md` the app's **operating mode**, the **lever that returns it to normal**, and **what realistic data looks like.** So:

- Read the operating-mode note from `stack.md`. If the app is at a crossroad (closed-for-season, pre-launch/empty, paused, away-toggle), **use the recorded lever to put the local sandbox into normal operating mode.**
- Seed a **known test user** and a **known test listing** (or the equivalent realistic content `stack.md` describes), so the flows have something real to act on.
- Confirm the integration guards from `/ship-change` still hold (payments in test mode, email/SMS/push off or routed to a dev inbox) — the breaking-on-purpose move below depends on it being safe to run these flows for real.
- **Capture the clean, logged-in screenshot — and put it in front of the builder.** Once the sandbox is seeded and in normal operating mode, log the known test user in, take a full-page screenshot of the real running app, and **show that image to the builder** — *"here's your app on the private practice copy, logged in, with a real listing up — this is what every check below will be working against."* This is the first thing they see actually working; it's the artifact they can ask you to regenerate at any time; and it doubles as the empty-sandbox guard: **if that screenshot shows a blank page, a login wall, or an error instead of the real rendered app, stop — the sandbox isn't in a real state and nothing below would prove anything.** Don't accept "it compiled / the server's up" as proof the page renders — look at the screenshot.

If `stack.md` has no operating-mode note (an older run), figure out the realistic state with the builder here — but the front door is where this normally lives.

## Step 0.5 — Show the whole list first, and ask what's missing (don't dive straight into test #1)

**Do not jump into building the first check.** Diving into "okay, let's test the buy button…" without first laying out the *whole* plan is a real, called-out failure — it leaves the builder with no idea how many checks are coming, no chance to weigh in, and no prompt to remember the flow that matters most to *them* but never made the original list. So before Step 1 on the first flow, **lay out the full menu and invite additions:**

1. **Show the full list of flows you're about to turn into checks** — pulled from the must-not-break list, in plain English, as a simple numbered list they can see: *"Here are the flows I'm going to turn into automatic checks, one each — (1) log in, (2) see my listings, (3) the buy button charges and shows a confirmation, (4) a seller can post a listing. Each one I'll build, then break on purpose so you watch it catch the break."* This *is* the agenda; it's also the status board from your first reply, now filled in with real flow names.
2. **Ask, plainly, if anything's missing:** *"Is there anything else in your app that would really hurt if it quietly broke — something you'd want a check watching — that isn't on this list? Now's the moment to add it; nothing's too small to name."* A non-technical builder often only remembers their scariest flow when they see the others written out. Add whatever they name to the must-not-break list in `staging.md` (that list stays the single source of truth) before you start.
3. **Then, and only then, start Step 1 on the first flow.** Tell them the order you'll go in and roughly how many — so the run has a visible shape, not a surprise sequence of tests.

## Step 1 — Walk the flow once, with the builder, and pin down what "worked" means

For this flow, confirm three things in plain English — and **the third is the one that matters most:**

1. **The steps** — *"to buy something, you: open a listing, click Buy, enter a card, hit Pay."* You propose, they correct.
2. **The starting state** — logged in or out? which listing? (the seed from Step 0).
3. **The expected result — what do you *see* that tells you it actually worked?** This is the assertion, and it's where green checks earn their trust or become theater. Push past "it works" to something concrete and checkable: *"after I pay, I should land on a confirmation page that says 'Order placed' and shows the amount"* — not just "the page changes." For an invisible-logic flow, get the *number*: *"a $10 item should show $0.83 tax, not $0.80."*

> **This closes `/ship-change`'s open limit.** `/ship-change`'s eyeball gate could check that something *looks* fine but couldn't prove back-of-house *correctness* — invisible logic the eye can't see. Here, "looks fine" becomes a **written assertion** the check enforces forever. That's the upgrade this skill exists to deliver.

**Then triage the flow — can the sandbox actually prove it?** (Integration guards mean some flows only prove the *code path ran*, not that the real-world thing happened.) Classify each:

- **(a) Fully sandbox-provable** — transaction completes against test-mode Stripe + seed data; the notification send is triggered and captured. *Most flows.* Automate and prove-it-fails as normal.
- **(b) Sandbox-provable, but the *real* proof is in production** — the payout actually lands in the bank, the email actually arrives. The sandbox check proves the path; the real proof needs a **periodic real check** (buy something for $1 and refund it) or the **Gate-3 synthetic monitor** (the same check run continuously against the live site — the natural sequel for the money/growth cohort). **Never let a green sandbox check imply the real charge or email works** — record it as class (b) and say so.
- **(c) Only the real side effect proves it** — rare. Flag it honestly: *"we can't fully test this without doing the real thing,"* and lean on the periodic real check.

Record the class in `qa-harness.md` — it's part of being honest about what green means.

> **Checkout / payments: don't settle for "can't prove it" — offer the test key that *makes* it provable.** The most important flow a money app has (*"the buy button charges a card and confirms"*) often lands in class (b)/(c) for a bad reason: the sandbox was stood up with payments **disabled** (no Stripe key at all), so a charge physically can't complete and the check can only confirm the button was clicked. That's an honest gap — and a fixable one, because **a payment provider's *test mode* is built for exactly this.** A Stripe **test key** drives a **fake test card** (e.g. `4242 4242 4242 4242`) all the way through to a real confirmation page **without ever touching real money or a real card** — that's the whole point of test mode, and it's a *different* key from the live one, so it cannot charge anyone. So when checkout is the flow:
> - **Offer to move the sandbox from "payments disabled" to "payments in test mode,"** and say plainly why it's safe: *"Your practice copy has no payment key right now, on purpose — that's the guard that stops it ever charging a real card. But there's a middle setting made for testing: a **test key** that runs a fake card all the way to your confirmation page and can't touch real money. If you hand me your Stripe **test** key, I can drive a fake purchase end-to-end and prove your buy button actually completes a charge and shows the confirmation — turning this from 'we clicked Buy' into 'we proved a card goes through.'"*
> - The builder pastes the **test** key into the sandbox's secrets themselves (same secret-hygiene rule as `/ship-change` — never the live key, never into chat as the live value). With it in place, checkout moves from a hand-waved (b) to **"(a) in test mode"** — a real fake card driven end-to-end, breakable-on-purpose, watched going red. **Be honest about the asterisk, don't claim the spotless (a) of a login check.** The confirmation usually rides a webhook the sandbox can't receive, so a clean checkout check is *"(a) in test mode, with one callback simulated"* — a genuine upgrade, not a perfect one. Doing this for real is the hardest engineering in the skill; it honestly takes the better part of an hour, so name that to the builder up front (in the opening clock-setting and in Step 0.5) rather than letting them discover it mid-run — and read **Technical landmines** (below) before you build it. Never promise checkout is quick.
> - **If they don't have or don't want to add a test key,** record checkout honestly as class (b) — the check proves the path runs, the **real** charge is proven by a periodic $1-real-buy-and-refund or the Gate-3 synthetic monitor — and *name the test-key option as the open upgrade* in `qa-harness.md` so it's a door left open, not a gap quietly accepted. A green that proves nothing is worse than an honest "not yet" — but an honest "here's exactly how to make it provable" is better than both.

## Step 2 — Build the check, and show its readable face

You write the browser-automation check (Playwright). The builder doesn't see or touch the code. What they see is the **readable version that lands in `qa-harness.md`** — the steps from Step 1, the expected result, the testability class. Confirm with them that the readable check matches what they meant: *"here's what this check does, in plain English — does that match the flow you care about?"*

## Step 3 — Prove it catches a break (the spine — never skip this)

This is the move the whole skill turns on. A check you haven't watched fail is not yet trusted. **You drive; the builder only watches** — and the breaking is the most reversible operation in the skill, so it can't scare them. It happens on a **throwaway copy** — a scratch branch **discarded, never published.** "Putting it back" is "throw the copy away," not "carefully un-edit code." The builder never touches anything.

**The builder must *watch this with their own eyes* — "I ran it and it's green" is not proof to them.** The whole reason this step exists is that a green checkmark you *report* is exactly the false floor the skill is built to kill — so don't replace "trust the app works" with "trust me that the check works." **Show it.** A builder saying *"I saw nothing while it ran"* means this step failed, however green the terminal was — the proof has to be something they actually looked at.

- **Default path — record the run and put the pictures in front of them.** In nearly every setup the reliable way to let a builder watch is to have the browser record itself, then *show them the recording inline* — not leave it in a folder, not describe it. Turn full capture on *before* you run (in `playwright.config.ts`: `video: 'on'`, `screenshot: 'on'`, `trace: 'on'`, and pace the steps slowly enough to be legible), then surface the artifacts straight to the builder: the screenshot of the green run landing on the confirmation, beside the screenshot of the same check going red on a blank/error page after the break. *"Here — watch the check drive your app: green when it works (see the 'Order placed' page), and the very same check going red the instant I broke it."* Pictures they can look at, every run. This is the path to default to, because it works even when nothing can pop up on their screen.
- **Bonus path — a live window, only if you can confirm one truly appears.** If the builder is on their own desktop and a headed browser window genuinely opens for *them*, let them watch it live — *"I'll put a browser window on your screen and you watch it click Buy."* But **never promise a live window you can't deliver** — promising a window in a setup that can't show one is precisely the "saw nothing" failure being reported. When unsure, record and show; that always works.

The deliverable of this step is **the builder saying "I saw it go red,"** not you saying "it went red." If there's no image or recording they actually looked at, you haven't proven it to the person who needs proof.

**First, establish the baseline — a break proves nothing without it.** Run the check against the seeded sandbox and confirm it's **green right now.** A check that's already red (flaky, mis-wired, bad seed) can't be "watched going red." Green-first, red-after-break, green-again-after-revert is the full proof; skipping the first green invalidates the other two.

### How to actually introduce the break (the part that's easy to get wrong)

Breaking "exactly this one thing" in an AI-generated codebase you didn't write is the technically riskiest move in the skill — don't improvise it. Work backwards from the assertion, and prefer the least-invasive method that still trips *this* check:

1. **Locate by tracing, not guessing.** Start at the assertion ("lands on a page that says 'Order placed'") and the element the flow drives (the *Buy* button's text/route), and trace inward to the code that produces that outcome — the charge call, the success response, the confirmation render. Don't grep blindly for "charge"; follow the path the check walks.

2. **Default to runtime fault-injection over source edits** — more reliable in code you don't understand. Playwright fails the flow *without touching the builder's source* via request interception: `page.route(...)` to **abort or rewrite the network call** the flow depends on (abort `/checkout`, or rewrite the charge response to an error). Preferred because it (a) can't leave broken code behind — it lives in the throwaway test scaffold, not the app; (b) targets exactly the one call the check cares about; (c) works identically across stacks. Use it first.

3. **Fall back to a surgical source edit only when no network boundary carries the behavior** (pure client-side logic, an invisible calculation). Then make the *smallest legible* change at the exact line — negate the condition, force the charge amount to fail, short-circuit the notification send — never a broad edit. If you can't find the precise line with confidence, say so and use route interception instead of hacking at source you don't understand.

4. **Verify the break is targeted, not collateral.** It must make **this check's assertion** fail — ideally while an unrelated check still passes. If sabotaging the buy button turns the whole app red, you've proven the app can break, not that *this check* watches *this flow*. A targeted red is the proof; a blast-radius red is not.

**One targeted break per flow is the default — keep it lean.** Each flow needs to be watched going red *once*; that single green→red→green is the proof. Pick the break that matters most for that flow and run it: *"Watch this: on a throwaway copy I'll make the buy button fail to charge."* (Abort/rewrite the charge call.) Run → **red** → throw the copy away → run again → **green.** Resist doing more break-and-revert cycles per flow than the proof needs — those extra cycles are pure waste: re-proving something already proven, adding no trust while the builder waits.

**Add a second break for the single most important flow only** (usually money). After its big break, show the quiet one too — *"now I'll stop the order-confirmation from sending"* (abort the send call) → **red** → throw away → **green** — so on the flow that matters most they've seen the harness catch both a catastrophe and the silent miss nobody notices until a customer complains. One flow earns this, not every flow.

**Route-abort proves the check, not the app — own that gap on the marquee flow.** The default break (`page.route(...)` abort/rewrite) breaks the *test's view of the world*: it proves the check goes red when the call it depends on returns junk. That's real and useful — but weaker than it sounds, because the thing you broke lives in the test scaffold, not the app. Breaking your own sandbox stand-in and watching the check notice is slightly circular ("if I skip my own stub, it goes red"). So for the **one marquee money flow**, also break it for a *real* reason at least once: change real app/sandbox state the way an outage actually would — remove the seller's connected Stripe account, null the price on the seeded row, point the charge call at a dead key — and watch the **committed** check (not a scaffold trick) go red. That's the difference between *"my scaffold detects a broken response"* and *"this check catches the app actually breaking."* Name which red the builder saw; don't let route-abort masquerade as the stronger proof.

**If a check does *not* go red when you break its flow, that check is theater — fix the check, not the app.** A check that stays green through a real break is worse than no check: it actively lies.

When both go red on cue and green again after, **stamp the check "proven to catch a break on `<date>`"** in `qa-harness.md`. That stamp is the trust — and (Step 5) it's renewable.

## Step 4 — Log the result

Record in `qa-harness.md`: the flow passed (green against the real seeded state), its testability class, that an automated check now exists, and the proven-on date. This is the per-flow row downstream skills read.

## Step 5 — Wire it into the `/ship-change` loop, and set the re-prove trigger

A check that only runs when someone remembers it is barely better than the manual re-walk it replaces. So the deliverable isn't the check — it's the check **running automatically on every change.** Two wirings:

- **The change loop runs this check in place of the manual re-walk.** Once a flow has a proven check, `/ship-change`'s eyeball gate runs it instead of asking the builder to click through that flow by hand. The bare eyeball shrinks to just the *new* change the builder made (no check covers that yet) plus any must-not-break flow not yet covered. `qa-harness.md`'s presence is the signal `/ship-change` reads.
- **Set the re-prove trigger** (staleness, below): record in `qa-harness.md` that this check must be **re-proven whenever its flow changes.**

Tell the builder plainly what changed: *"from now on, every time you make a change, this check runs by itself before anything goes live — you don't have to click through buying something by hand anymore. I run it; you'll only hear from it if it goes red."*

---

# Technical landmines — the hard 80% of the checkout check

*"Drive a fake test card all the way through to a real confirmation page"* is one sentence to say and the hardest, slowest piece of work in the skill to do for real — honestly the better part of an hour on its own (see the time budget at the end of this section). On the marquee money flow it's the hardest engineering in the skill, and it fails in ways that read as flakiness unless you already know them. Don't treat that sentence as trivial — budget for these (most surfaced on a real run), and tell the builder plainly that the *money* check is the one that takes real work:

- **The confirmation often rides a webhook that can't reach `localhost`.** Stripe confirms a purchase by calling *your* server back after the hosted page — and Stripe's servers can't reach a sandbox on `localhost`, so the confirmation may never arrive on its own. Either run a forwarder (`stripe listen --forward-to …`) or drive the post-payment state yourself and assert on that — but know you're then **simulating the one callback the real app waits on.** That's exactly why test-mode checkout is honestly *"(a) with one callback simulated,"* not a clean (a).
- **Stripe's hosted page pre-checks "save my info" and silently disables Pay.** The Link / "save my info" box can load pre-ticked and demand a phone number; until it's satisfied the Pay button is inert and your click does nothing (looks like a hang, not an error). Untick it or fill the field explicitly — never assume Pay is clickable.
- **Capturing the purchase id races the redirect.** The id you need (to assert against, or to re-seed) is minted right as the page redirects away — grab it from the network call or the URL *before* the redirect settles, or it's gone.
- **Confirming a purchase marks the listing sold — so the check isn't repeatable.** A marketplace buy mutates real state: the listing flips to sold and the *second* run has nothing to buy. A repeatable check needs its **own dedicated throwaway listing and a re-seed between runs**, not the shared seed listing every other check leans on.
- **The app may strip the success URL — so a strict URL assertion races too.** If the app rewrites or cleans the post-checkout URL, asserting on the raw success URL flickers. Assert on a **stable on-page signal** ("Order placed" + the amount), not on a query string the app will rewrite out from under you.

None of this changes the spine — you still earn trust by watching the check go red. It changes *how long the green takes to earn.* When checkout is in scope, say so up front: it's the one flow where "a little setup" is honestly an hour, not a minute — and the place to spend it, since it's also the flow whose silent failure is scariest.

# Keeping checks honest over time — the stamp is renewable

A check proven to catch a break in January can silently stop asserting by June: the flow gained a step, a button got renamed, and now the check passes *trivially* — green when it shouldn't be, which is **more dangerous than red** because nobody's looking. So, like `/safety-net`'s restore-test:

- The **"proven to catch a break on `<date>`" stamp is renewable, not a one-time event.** `qa-harness.md` carries a **"re-prove due" trigger** per check.
- **Whenever `/ship-change` touches a covered flow, it re-runs the break-and-watch for that flow before publishing.** A check that hasn't been re-proven since its flow last changed is **flagged, not trusted.**

# When a check goes red — is it a real bug, or did the check rot?

A red check is good news (it caught something), but the builder can't tell alone whether the *app* broke or the *check* went stale. Two things handle this; set the expectation up front:

- **The answer is "tell your AI."** *"If a check ever goes red, just say: 'a check is red — figure out if it's me or the test.'"* You diagnose: a real regression routes to `/ship-change` to fix safely; a rotted check, you repair. The builder never edits test code either way.
- **Keep the suite tiny.** 3–5 flows, top-of-pyramid. The smaller the suite, the rarer the false alarm — and the less likely the builder learns to ignore a red, which is the death of any harness.

# How many flows / how thorough — scaled to the required gate

Read the required gate from `readiness-check.md`:

- **Money / growth cohort (the situation that triggered Gate 2):** cover **every** must-not-break flow, plus name the **(b)-class flows that need a production check** and offer the Gate-3 synthetic monitor as the sequel.
- **Hobby / internal app:** cover only the **one or two flows that would actually hurt** if they broke.

Stay top-of-pyramid either way — a handful of full-stack critical-journey checks, never deep coverage. **Automation itself is not optional** (a manual checklist has the exact skipped-under-pressure flaw this skill exists to cure — that's why this isn't just a formalized version of `/ship-change`'s re-walk); only *how many* flows you automate scales with exposure.

---

# Keep it moving — a silent, thrashing hour is the failure, not a long one

A real run dragged on and the builder rightly called it unacceptable — but the problem was that it went *silent*: an hour of jargon with no idea what was done or what was left. The enemy is wasted and invisible time, not elapsed time. An hour of visible, step-by-step progress on real checks — especially checkout — is the honest cost of the work, not a failure; an hour where the builder saw nothing, or where the same flow got broken-and-reverted five times for no added proof, is the failure. The simple flows should each take a few minutes; a real test-key checkout legitimately takes the better part of an hour, and that's planned for, not an overrun. A builder watching a *silent* run stops trusting the harness, so staying visible is the correctness property here — the clock itself isn't the enemy, the silence is. Hold to these:

- **Set the tool up once, up front.** Install Playwright + its browser one time in Step 0, not lazily at the first flow — it's the single biggest one-time cost. Get it out of the way and tell the builder that's what the first few minutes are.
- **Stand the app up once and keep it up.** One dev server, one seeded database, reused across every flow. Don't restart the server or re-seed between flows.
- **Run the green baselines as one suite pass.** Playwright runs checks in parallel — build the checks, then confirm them all green in a single run, rather than a full ceremony per flow before the rest even exist.
- **Break by intercepting the network, not editing source.** `page.route(...)` abort/rewrite isn't just safer (Step 3) — it's far faster: no source edit, no rebuild, no restart. A source edit is the rare *and* slow exception.
- **One break per flow** (Step 3) — the second break is for one marquee flow only. This alone roughly halves the run.
- **Stay visible — measure silence, not the clock.** Reprint the board at every milestone, and the moment a flow stalls with no visible progress — say more than ~10 minutes with nothing new to show — **stop and show the builder the board**: what's proven, what's left, what's stuck. The trigger is *lack of progress*, not raw elapsed time, so it never fires on honest work that's visibly moving. The checkout flow carries its own ~hour budget (see **Technical landmines**) and does not count as "dragging" — its length is the work. A run that goes *dark* for an hour has failed the builder even if it would have finished green; a run that's long but visibly progressing has not.
- **Checkout is the centerpiece, not an exception — budget the easy flows tightly to make room for it.** The quick per-flow pace assumes route-abort breaks and disabled payments. A *real* fake-card-to-confirmation flow trips the **Technical landmines** (webhook, sold-listing re-seed, racing URL) and honestly takes the better part of an hour — for the money/growth cohort that's the main event and the most valuable deliverable, planned for, not a deviation to apologize for. The discipline isn't "rush it" — it's *say so in advance and keep the board moving*: time-box the simple flows tightly so the marquee money flow has room, and keep its progress visible the whole way so its honest length never reads as a stall.

---

# Output (what's in place when you're done)

- **A small suite of automated checks** — one per covered must-not-break flow — each **watched going red** on a real break, and **wired to run automatically inside the `/ship-change` loop.** The check files live in the repo so the loop and future runs can find them — but **getting them there is not automatically silent: on an auto-deploy stack (push-to-`main` ships), committing them is a publish, so it waits for the builder's okay, stays off `main`/CI until then, and no sandbox-only override (test key, route stub, always-on recording) ever ships.** On a manual-deploy stack it's ordinary plumbing the builder never manages.
- **Visual proof the builder actually looked at** — the clean logged-in screenshot of the seeded sandbox, plus the green-run and red-after-break images (or recording) for each covered flow. Saved with the checks and shown inline during the run, so "you saw it go red" is literally true, not a figure of speech.
- **`qa-harness.md`** — the readable face the builder actually uses. Per flow:
  - the plain-English description and the **expected result** ("what 'worked' looks like");
  - the **testability class** (a / b / c) — so green never over-promises;
  - whether an automated check exists, and a **pass/fail log**;
  - the **"proven to catch a break on `<date>`"** stamp;
  - the **re-prove-due trigger.**
  - It is **regenerated from the plain-English must-not-break list in `staging.md`, never edited independently** — that list stays the single source of truth.
- `/emergency-plan` reads `qa-harness.md` (every real outage becomes a new check here, so that exact failure can never silently return); `/release` reads it (this is the test gate `/release` runs).

Close in the builder's words: *"Your critical flows are now watched automatically. Each check has been shown catching a real break — you saw it go red — so a green isn't just hopeful, it's proven. From now on these run by themselves every time you change something, before anything goes live. You'll only hear from them when something's actually wrong."*

# Point onward — based on where `/readiness-check` put them

This is a Gate-2 skill, so read `readiness-check.md` and tailor the closing pointer:

- **Required gate 2** (money / others' data / real dependence): the harness is one of the go-live nets. Name the **rest of the Gate-2 horizon** — knowing the moment it breaks (`/go-live-check`, ready now — it proves your monitoring actually catches a failure), and having a calm plan for when it does (`/emergency-plan`, ready now — a phone card for the night something breaks). Horizon, not homework.
- **The natural sequel for the (b)-class flows** is the Gate-3 **synthetic monitor** — the same checks run continuously against the live site. Offer it as horizon to the money/growth cohort; don't build it here.
- **No `readiness-check.md`:** suggest a one-time front-door run so the pointer can be tailored.

End on a single clear pointer — never a trailing list.

---

# Scope notes / known limits (mention if relevant; otherwise out of scope)

- **Top-of-pyramid only, on purpose.** A handful of full-stack critical-journey checks, not unit-test coverage. "Does my buy button still charge a card" is worth a hundred unit tests this builder will never write.
- **Green never means more than it proves.** Testability class (b)/(c) flows prove the code path, not the real-world charge/email — say so; the real proof is a periodic real check or the Gate-3 synthetic monitor.
- **Test-environment + seed-data mechanics are stack-specific and partly mapped already.** The recurring ones (webhook-can't-reach-`localhost`, sold-listing-isn't-repeatable, success-URL races) are written down in **Technical landmines** above; expect each new stack to surface one or two more on its first real run. Lean on `/ship-change`'s sandbox + `stack.md`'s realistic-data note, and add anything new you hit to that landmines list rather than rediscovering it next time.
- **A red check needs human triage** (real bug vs. rotted check) — the builder says "tell your AI," never edits test code. Keeping the suite tiny is what keeps red meaningful.
- **Mobile (Expo / React Native) doesn't fit a browser driver.** If `stack.md` says mobile, the web-flow approach here doesn't transfer cleanly — name that honestly and treat a device/emulator check as out of v1 scope rather than pretending a browser check covers a phone app.
- **All-in-one builder platforms (Replit / Lovable / Bolt):** if `stack.md` records the app lives on one, its preview/checkpoint differs from a raw stack's sandbox; the must-not-break flows still define the checks, but how they're run leans on the platform — don't assume the raw-stack local-sandbox machinery.
