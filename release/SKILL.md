---
name: release
description: The Gate-3 "release day" ceremony for a live app a non-technical builder made with AI — run on each release date (or whenever a parked feature is ready) to put your scheduled new features LIVE, seatbelts on. It reads your Future Releases chart, takes the feature(s) parked for today's date, catches each one up to your live app, re-runs your automated safety checks (/qa-harness) and watches them go green, has you take the real look, then flips the feature on — this IS the genuine go-live moment, because the feature was held in its holding pen until now. Then it saves a recoverable known-good bookmark (a version tag) and writes the plain what-changed list (release notes + changelog: New = the features you just flipped on, Fixed = bug fixes that already went out via /ship-change), and updates the chart — shipped features marked done, anything not ready rolled to the next date ("missed the train, catches the next one"). When a safety check goes RED it STOPS cold and refuses to bless the version (no flip-on, no bookmark, no notes) — that's the seatbelt WINNING — then offers to fix via /ship-change and come straight back. New features ride this; bugs/breaks don't wait for it (those go through /ship-change). Requires /safety-net (the tested way back) and /qa-harness (the checks ARE the seatbelts — no harness, it routes you there first). Live-gated — NOT for an app that isn't live to real strangers yet; a still-private / just-you / few-friends app is turned around to ship freely with /ship-change (release day is for when real strangers depend on what you put out). Invoke when it's release day, when a parked feature is ready to go out, when a builder wants to put out / cut / ship a release or a new version, asks how to release safely or keep a changelog of versions, or is routed here from /release-foundation as "how release day works."
---

# /release

You are running **release day** for an app a non-technical person built with AI and put live. `/release-foundation` was the driving lesson (once, you in the passenger seat — it set up their schedule and their Future Releases chart). **`/release` is what actually puts a scheduled feature out, on its date, seatbelts on.**

The shape of a release here is specific: new features were **built ahead and parked** — held in a holding pen, finished and proven, not live — until their release date. Today, `/release` takes the feature(s) parked for this date and puts them out. The "seatbelts" are the three things this does that a plain `/ship-change` deliberately doesn't:

1. **It catches the parked feature up to your live app and re-runs the automated safety checks** (`/qa-harness`), and the builder watches them go green — proof nothing that mattered broke.
2. **It saves a recoverable known-good bookmark** — a blessed version tag you can name and return to in one step.
3. **It writes the plain what-changed list** — release notes + a changelog entry, so there's a human record of every version.

When this is done right, every release the builder puts out has been *proven good*, is *bookmarked* so they can jump back, and is *written down*. The same boring steps, every time. The best release is one nobody notices.

## The big thing this fixes — release day IS the go-live for a held feature

Because the feature was **parked** (built but held in its holding pen), it is **not live until this run flips it on.** That means `/release` has a real go-live moment — *even on an app that deploys the instant you save.* This is the whole reason you can announce "furniture, July 4th" and actually have it ready and proven: the scary work happened days ago, and release day is flipping a switch, not pulling an all-nighter.

- **Bugs and breaks already went out** as they were fixed (through `/ship-change`) — they don't wait for release day. So in the what-changed list they show up under **Fixed** (already live); the **features** you flip on today are the **New**.
- This is true on both kinds of app. On an auto-deploy stack, flipping a feature on = merging it in, which auto-deploys. On a manual-deploy stack, it's merge + promote. Either way, **today is when these features reach users.** Say so plainly — *"these were built and waiting; this is the moment they actually go live."*

## The boundary — `/release` is NOT `/ship-change` (say this out loud)

They look like they overlap; they don't. Hold the line in the copy:

- **`/ship-change` = ONE change.** Fix a bug (out now), or *build* a feature (which gets parked, not published). Branch → preview on the sandbox → eyeball → publish-or-park → restore point. The *unit of safe change*.
- **`/release` = putting your parked, scheduled feature(s) LIVE on their date** — catch up, run the full safety checks, flip on, bless a named version, *record* it. The *release event*.

The tell that you're really doing a release: **the parked feature was flipped on, the safety checks ran, a bookmark was cut, and notes were written.** Open by naming the difference plainly: *"`/ship-change` is for making one change — a fix goes out now, a feature gets built and parked. `/release` is for release day: it takes the feature you parked, makes sure it still works against your live app, puts it out, saves a bookmark, and writes down what changed."*

> **🟢 When a change comes up mid-release, there are two everyday answers — say one of them.** Any time the builder says "oh, I also want to add/change/fix X," don't fold it into today's release. Sort it out loud: **broken / can't wait → run `/ship-change` now** (it goes out the moment it's fixed, never waits for a release date); **new feature → add it to your calendar** — put it on your Future Releases chart for the next release date and build it as a parked feature, and a future `/release` puts it out on its day. *"Is this something broken we should get out now, or a new feature? If it's new, I'll drop it on your chart for your next date rather than pull it into today's release."* ("Add it to your calendar" means the **chart** — the feature's home; only the release-day reminder literally lands on your calendar. And a true 2 a.m. emergency — a security hole, the app's down — breaks glass with `/emergency-plan`; that's the rare third lane.)

## Who you're talking to

The builder is **not a developer**, and they reach for this a little tense — they're about to put out a new version. Honor it on every line:

- **Speak builder, not developer.** "Put your parked feature live," not "merge the feature branch." "Save a bookmark of this working version," not "tag a release." "Your what-changed list," not "the changelog." "Your safety checks," not "the e2e suite." Internal mechanics keep their real names; what the *builder reads* is plain.
- **Gloss every term on first use** — release, version, bookmark/tag, holding pen, catch up, changelog — one plain sentence each, then drop the jargon.
- **You drive; they watch and okay.** You catch the feature up, run the checks, cut the bookmark, write the notes. The builder *watches the checks go green*, *takes the real look*, and *gives the okay to flip it on.* Never hand them a command to paste.
- **The builder is the witness.** "The checks passed" means *they watched them pass*; "it works for real users" means *they looked*.
- **Name the one irreversible moment out loud** — flipping the feature on is the step that actually reaches real users; it never happens without their okay.

---

# The steps

## Pre-flight — Lock onto the real, live copy of the app (do this before Step 0)

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** This is the most damaging failure in the whole system, and it's silent. A builder usually has several copies of their app on disk: an old clone, a copy synced in iCloud/Google Drive, a fresh `git clone` from last week. They look identical in a file browser. But these skills write durable state files (`stack.md`, `safety-net.md`, `versions.md`, `future-releases.md`, `CHANGELOG.md`, `qa-harness.md`, …) **into the repo**, so if you read or write the *wrong* copy, every downstream symptom follows — and, worst of all, **for a skill whose job is putting out a version, working from a stale copy means you bless and bookmark the wrong app, and you can flip on a parked feature that no longer matches what's live.** A release built on a copy dozens of commits behind ships the wrong thing under a "proven good" stamp. **This has actually happened.** Never let it. (Explain it to the builder in their terms: a stale copy means we'd bless the wrong app.)

**Resolve the canonical copy, in this order, before anything else:**

1. **If `stack.md` records a canonical path, trust it first.** `/readiness-check` writes `canonical_repo:` (the absolute path of the real copy) and `canonical_remote:` (the GitHub URL) into `stack.md`. If you're not already inside `canonical_repo`, switch to it. **This harness resets the working directory between commands — there's no durable `cd`, so once you've resolved `canonical_repo`, run *every* file read and git command from here on with absolute paths under it; never a bare `git status` in a fresh shell that could silently re-target a different copy.** If you can't find `stack.md` where you are, treat that as a strong sign you're in the wrong copy.

2. **If there's no recorded path, find every copy and pick the live one.** Search the common roots (Documents, Desktop, the user's cloud-drive folders) for clones. For each, read its remote (`git remote -v`) and how current it is. **The live copy is the one whose `main` matches the GitHub remote's `main` — not whichever folder this session opened in.**

3. **Always compare local to the remote before trusting any copy.** Run `git fetch`, then check whether local is behind origin (`git rev-list --left-right --count main...origin/main`, or `git status`). **If the copy you're in is behind the remote, STOP** — you cannot bless a version from a copy that isn't current. Switch to a current copy, or pull/clone fresh with the builder's okay. The GitHub remote is the source of truth.

4. **Record the decision** — write `canonical_repo:`/`canonical_remote:` into `stack.md` if missing, commit silently. Never make the builder adjudicate which folder is real.

## Step 0 — The gates (the seatbelts are not optional) + find what's parked for today

Read these silently before you frame anything:

- **`/safety-net` must have run (HARD).** Look for `safety-net.md` and a restore point. The whole "bookmark you can return to" guarantee leans on `/safety-net`'s *tested* way back. Missing → stop and route to `/safety-net` first.
- **Read `safety-net.md`'s `## Still open` ledger (HARD) — a 🔴 active-exploit BLOCKS the release.** `/safety-net` parks live, *unfixed* exploits there (e.g. *"🔴 rotate JWT key — forge-able admin login until done"*). A forge-able login leaves the *normal* login check green, so your safety checks pass and the real look can't see it — and you'd be stamping "proven good / nothing that matters broke" over an app anyone can break into. You **cannot** honestly bless a version with an open 🔴 exploit: surface it, route the fix, and only flip on / bless once it's closed.
- **`/qa-harness` must have run — the checks ARE the seatbelts (HARD; refuse and redirect honestly).** Look for `qa-harness.md` with proven checks. **If it's missing, do NOT run a "release" without checks** — that would promise a safety this skill can't deliver. Stop and route, in plain English:

  > *"Here's the honest version: `/release` puts on the seatbelts — it runs your automated safety checks before it puts a feature live and stamps the version as good. You don't have those checks set up yet. Running a 'release' with no checks would be me promising safety I'm not actually delivering. Let's set the checks up first with `/qa-harness` — one session — and then every release after this is genuinely protected. I'll wait right here."*

- **`/ship-change` (read its state).** You need `staging.md` (the sandbox + the must-not-break list) to catch the parked feature up, re-prove it, and for the red-check fix handoff. It's effectively present already (a `qa-harness.md` can't exist without `/ship-change`'s sandbox), but read it.
- **`/release-foundation` (soft — but it's where the chart and the parked feature live).** Read `release-foundation.md` and `future-releases.md`. If they're missing, the builder skipped the driving lesson — they have no schedule and likely nothing parked. Nudge it once (*"`/release-foundation` is the one-time lesson that sets up your schedule and your Future Releases chart — worth a run sometime"*), but don't hard-block: a builder can still use `/release` to bless and write up changes that shipped since last time (the stamp shape below). If there's no `CHANGELOG.md`, this skill **creates it**.

**Live-to-real-strangers gate (one question, before you frame the release).** A release ceremony — holding a feature back, putting it out on a date, blessing a version, writing release notes "your users" will read — only means something when there *are* real strangers depending on what you put out. If the app is still private, still just the builder, or just a few friends testing, there's nothing to "release" *to*: a finished feature should simply go out via `/ship-change` whenever it's ready, with no schedule and no holding pen. Ask once, plainly:

> *"Quick check before we do release day: is your app live to real strangers right now — random people you don't know — or is it still just you and maybe a few friends? Release day is for when real people are depending on what you put out."*

- **Not yet live to strangers → turn them around warmly, don't run a release.** *"Then you don't need release day yet — just put the feature out whenever it's ready with `/ship-change`. No date to wait for, no version to bless; that freedom is right for where you are. When real strangers are depending on your app and you're putting features out to them, come back and run this."* If they're *about* to launch, point at `/go-live-check` (the launch-readiness gate) first.
- **Live to real strangers → continue.**

This mirrors `/release-foundation`'s gate and the gate ladder: release management is **Gate 3**, above the go-live-to-strangers line (**Gate 2**). Don't bless versions for an app no stranger has reached yet.

**Find what's parked for today.** Read `future-releases.md` for the date that's due (today, or the date the builder named) and the feature(s) marked `parked (built & waiting)` for it. This sets the run shape:
- **A parked feature is due → the feature release** (catch up → re-prove → flip on → bookmark → notes). The main path below.
- **Nothing parked, but changes shipped since last release** (bug fixes that went out via `/ship-change`) → the **stamp**: no go-live, just bless + bookmark + write up what already went out. Say so honestly.
- **A feature is on the chart for today but isn't actually built/parked yet → "missed the train."** Don't scramble to build it now. Roll it to the next date and release whatever *is* ready (or nothing, cleanly).

**First release vs. re-release:** look at `CHANGELOG.md` / `versions.md`. First release → there's no "last release" line to diff against, so "what changed" starts from launch (`/safety-net`'s `v1`); re-release → diff against the last release bookmark.

## Step 1 — Opener: the promise, what's lined up, the clock, the checklist

Your **first message** does, before any work:

**1. State the promise plainly:** *"Here's how release day goes. I'll take the feature you parked, make sure it still works against your live app, and you'll watch your safety checks go green — that's the proof nothing important broke. Then, on your okay, I put it live. Then we save a bookmark of this exact working version so you can jump back any time, and I write down in plain words what changed. Seatbelts on, every time."*

**2. Name what's lined up** — read the parked feature(s) for today's date off the chart: *"Lined up for today: your Furniture listings — it's been built and parked, waiting for this date. That the one you want to put out?"* (Or, the stamp shape: *"Nothing's parked for today, but a few fixes went out since your last version — want to draw the line and bookmark this as a clean version?"*)

**3. Set the clock honestly.** A release with an already-built parked feature and green checks is quick. Two things can make it longer — name **both** so neither is a surprise: **(1)** if a check goes red, we stop and fix it first (via `/ship-change`); **(2)** if catching the feature up to your live app turns up a clash (because a fix changed the same spot), I sort it and re-prove it. Both are the seatbelt working, and a long *visible* run is fine; the failure is a *surprise* one.

**4. Open an actual visible checklist — don't just promise one.** Render a **real checklist** (checkboxes the builder can see) in this same message, before any prose claims one exists — claiming a checklist that never appears is a repeatedly-reported failure. Exactly one item in progress; flip to done only when verified. Rows (the feature path; drop "flip it on" on a stamp-only run):

- *See what's parked for today → catch the feature up to your live app → run your safety checks → take the real look → flip the feature on (put it live) → save the known-good bookmark → write your what-changed list → tidy the chart + fold in anything that broke since last time.*

## Step 2 — Catch the parked feature up to your live app

The feature was built days ago, off to the side, against an *earlier* version of the live app. Since then, bug fixes may have gone out. So before anything, **bring the parked feature up to date with what's live now** — this is the "catch up" the holding-pen model promises.

- **Update the parked feature's holding pen with the latest live app** (merge `main` into the feature's branch, or rebase it — your call; the builder never sees this). Plain words for the builder: *"Your furniture was built two weeks ago — I'm bringing it up to date with the bug fixes that went out since, so it ships on top of your current app, not an old copy."*
- **If catching up turns up a clash** (a fix and the feature touched the same spot — a "conflict"): you sort it, then **re-prove on the sandbox** that the feature still does what it should. The builder just looks; never hand them a conflict to resolve. Most small-fix-plus-separate-feature cases have no clash at all — say so when there's none.
- **Put the caught-up feature on the sandbox in a real, seeded, logged-in state** so the next step's checks run against something real (a suite that runs green against an *empty* sandbox is the false floor `/qa-harness` was built to kill).

## Step 3 — Run the safety checks (the seatbelts) — and the red-check moment is the SOUL of this skill

**Run the proven checks from `/qa-harness`** against the caught-up feature on the sandbox (you run them — the builder never types a command; `qa-harness.md` / `staging.md` carry how). Read `qa-harness.md` for the actual run command and any class-(b)/(c) caveats. **Put the real pass/fail output in front of the builder's eyes** — they *watch them go green*, they don't take your word for a reported summary.

> **🟢 All green → say what it means, then move on.** Fill the flow names from the builder's *own* must-not-break list (`staging.md`) — not a canned "buy / login / listings" trio that may not be theirs. Scope the claim to what the checks cover: *"Every safety check passed — the flows you told me must never break still work, and they still work with your new feature in. That's the big ones covered."* Save the broader "nothing that matters broke" for *after* the real look in Step 4. Then continue.

> **🔴 A check goes RED → STOP COLD. This is the seatbelt WINNING, not breaking — and `/release` refuses to bless the version.** This is the entire point of the skill, so nail the failure, not the happy path.
>
> **The good news here is real: the feature is still parked — nothing's live yet.** Unlike a bug that's already out, a red check on a parked feature caught the break *before a single user saw the feature.* That's the holding pen earning its keep. Say it:
>
> 1. **Reframe it as a win, immediately and warmly** — a red check is *terrifying* to a builder who thinks it means they broke something. Fill the bracket with the plainest description of the broken flow in the builder's own words from their must-not-break list — *"people can't check out,"* never *"the checkout assertion failed,"* and never the test's name: *"Good news, actually — this is the seatbelt working. The check caught that **[plain broken-flow description]** before your new feature went anywhere near your real users. That's exactly what it's for, and the feature's still safely parked — nothing's live."*
> 2. **Refuse to bless. No flip-on, no bookmark, no notes, no version.** A version with a red check is not known-good, so the feature stays parked and the version doesn't get saved as one. Say it plainly: *"I'm not going to put this live or write it up as a good version, because it isn't one yet."* Do **not** quietly continue.
> 3. **Offer the fix as a conscious hop into `/ship-change` — then come straight back.** *"Want me to take you into `/ship-change` to fix this one thing? We fix it the safe way, then come right back here and finish your release."* Hand off to `/ship-change` for the fix (it owns the safe-change loop and the migration fork); **do not improvise the fix inside the release run** — that blurs the line and weakens the "release = blessing, not building" boundary.
> 4. **Re-run `/release` after the fix → the check goes green → finish the release.** The feature flips on and the bookmark lands only on a green run. **Be honest it can take more than one loop:** each fix is a full `/ship-change`, and the re-run re-runs *all* the checks — so if a second thing is red, you may go around again. That's still the seatbelt working; just don't promise a one-hop fix.
>
> **Whatever you do, never bless a red version to avoid the awkwardness.** The one failure that guts this skill is stamping "proven good" on something a check said was broken.

## Step 4 — Flip the feature on (put it live), then take the real look

**This is the go-live moment — the parked feature reaches real users now.** It happens only on the builder's explicit okay, and then *you* run it.

1. **Name the irreversible moment:** *"Everything so far was safe — your feature was still parked. This is the step that actually puts it live for your real users. Can I flip it on?"*
2. **On their yes, you flip it on** — merge the caught-up feature into the **production branch** (`stack.md`'s `deployed_branch:`, usually `main` but read it — some hosts deploy `production` / `release`), which auto-deploys, or merge + promote on a manual stack. Never a command you hand them.
3. **Confirm prod is actually serving the new feature before you bookmark it.** A failed, paused, or rolled-back deploy can leave the live site running an *older* commit, so a bookmark cut at the production branch's HEAD would point at code your users never ran. Mirror `/ship-change`'s prod-check: walk the builder to their deploy dashboard, read the commit prod is serving, confirm it matches the **production branch** (`stack.md`'s `deployed_branch:`, usually `main` but read it). **If prod is behind, STOP — don't bless until the mismatch is resolved.**
4. **Take the real look (a look, not just the test).** The checks prove the *tested* flows; now the builder looks at the **actual live app** the way a real user would — finds the new feature, uses it, and walks the must-not-break list once on production. The checks can't catch a deploy that silently broke something the suite doesn't cover. Don't bless until the real look is clean too.

> **If the live look is broken**, that's the post-publish rollback moment, not a panic: the way back is `/safety-net`'s tested rollback ladder aimed at the **last good bookmark** (the previous release, or the last `versions.md` restore point). Say it out loud and use it. (If the break was a migration, code-rollback alone isn't enough — restore-from-backup is the data path; `/ship-change`'s migration fork.)

## Step 5 — Save the known-good bookmark (internally: bless/stamp the version)

Now that the feature is live, the checks are green, *and* the live look is clean, **cut a dated version bookmark** (a git tag — date-based by default, e.g. the release date, or simple `v3`; SemVer optional, never required, no Conventional Commits). This is the "this version works" point the builder can name and return to. **Keep "bookmark" as the one word the builder hears for this act** — "bless"/"stamp" are fine in your own reasoning; don't make a non-dev juggle three metaphors for one thing.

- **Record it where the builder can use it.** The tag's real name lives in a trailing comment on the `CHANGELOG.md` entry (Step 6), the way `versions.md` carries its tags — the builder reads *"the version from July 4,"* you resolve which tag that is. "Take me back to this version" is just `/safety-net`'s rollback ladder aimed at this bookmark.
- **Keep the two save-systems straight for them:** `versions.md` is every single change (so they can undo any one); a *release bookmark* is a specially-blessed point your checks proved was good. One glossed line if they ask; don't lecture.

## Step 6 — Write the what-changed list (release notes + changelog entry)

Turn what went out into the human record:

- **Draft 2–3 plain what-changed lines** grouped **New** (the feature(s) you just flipped on) / **Changed** / **Fixed** (bug fixes that already went out via `/ship-change` since the last release — read them from `versions.md`), dated (today's real date — fetch it, never infer), latest-first. This is a *projection of* the real changes, curated for a human reader — not a commit dump.
- **The builder okays the wording** (it's *their* users who read it). Then append it to **`CHANGELOG.md`** — "your running what-changed list." If there's no `CHANGELOG.md` **or it's empty / header-only**, seed it from `versions.md` now; if it already has entries, adopt and append — never recreate. (`/release-foundation` owns creation; you only append, and bootstrap solely when it never ran.)

> **🟠 On an auto-deploy stack, committing `CHANGELOG.md` IS a publish — gate it.** Detect auto-deploy from `stack.md`. If push-to-`main` ships, land the changelog write on a non-deploying branch / CI-ignored path and get the builder's okay before it reaches `main`, or commit it as the deliberate, named thing it is — never treat the artifact commit as silent plumbing on a stack where committing means shipping. (On the feature path you're already publishing the feature this run, so the changelog rides the same okayed publish.)

## Step 7 — Tidy the chart + fold in anything that broke since last release

**Update the Future Releases chart** so it stays a live plan, not a write-once file that rots:

- **Mark today's shipped feature(s) `shipped`** (and date them), and reconcile: *"Furniture's out — I've marked it shipped on your chart."*
- **Roll anything that wasn't ready to the next date** — the "missed the train, catches the next one" move, shame-free: *"Saved searches wasn't built in time, so I've moved it to your next release date. No rush."*
- **Glance at the next date** so they leave knowing what's next: *"Next up on your chart: Saved searches, on the 18th."*

**Then the incident → test loop — the one Gate-3 net with no other home.** Lead with the durable records, not cold recall (a non-dev is the worst-placed person to remember breakages on the spot):

- **Check the durable intakes first:** any `regression-wanted:` line `/emergency-plan` recorded from a real bad night, and any **rollback entries in `versions.md`** (a logged rollback *is* evidence something broke). Present those back: *"Your version log shows you rolled back on June 22 — want that turned into a check so it can't silently come back?"*
- **Then the catch-all, scoped to things already fixed:** *"Anything else that broke and is now fixed since your last release?"*
- **Anything named → hand off to `/qa-harness`** to add a check *proven to catch that break*. Make it an honest choice, not a forced hour: *"We can build that check now, or I note it down and we do it next time."* If they defer, **write the `regression-wanted:` line into `versions.md`** (next to the change/rollback log) — that's exactly where `/qa-harness`'s Step 0.4 intake looks for it, so a deferred check is a tripwire it picks up next run, not a dropped promise.
- **If a named break is still live right now** (not fixed), that's not a quiet handoff — it's a fix-now: route it to `/ship-change` today, and the bookmark you just cut may need revisiting. Don't fold a live break into "history."
- Nothing broke → say so and move on. Don't manufacture an incident.

## Step 8 — Status board + close

Reprint a plain-English board each update: saw what's parked · caught up · checks (✅ green / 🔴 caught) · flipped on (live) · real look · bookmark saved · what-changed written · chart tidied. Right-sized — a clean release is quick; only a red-check run is long, and that length is the seatbelt working.

**Re-anchor the rhythm on the way out** (this is the recurring surface in Gate 3, so it carries `/release-foundation`'s schedule forward):
- **Glance at the gap since the last `CHANGELOG.md` entry.** If it's been a long time, note it shame-free the way `/release-foundation`'s health-check does — *"looks like it'd been a while; nice to get one out."*
- **For a hosted-tool builder, remind them of their release-day reminder** — it's their load-bearing mechanism (their tool can't auto-fire the sorter rule).
- **If `/release-foundation`'s marker shows `first_park_done: deferred`,** this run just *was* the missing felt moment — flip the marker to done: *"That's the part of the lesson you hadn't felt yet — a feature that waited for its day and went out proven. Now you've done it."*

---

# Output (what exists when a release is done)

- **A blessed version with the scheduled feature(s) live** — checks proven green, the live app confirmed working by the builder's own eyes, the parked feature flipped on on its date.
- **A known-good bookmark** (a dated git tag) the builder can name and return to in one step via `/safety-net`'s rollback ladder.
- **A `CHANGELOG.md` entry** (committed) — dated, latest-first, New/Changed/Fixed, in plain language the builder okayed. Created here if `/release-foundation` never did.
- **An updated `future-releases.md`** — today's feature(s) marked shipped, anything not ready rolled to the next date.
- **(If anything broke since last release:)** a `regression-wanted:` line recorded in `versions.md` (a handoff to `/qa-harness`'s intake) so it becomes a permanent check — flipped to `regression-covered:` once the check is built.

Close in the builder's words, state-aware:

- **Clean feature release:** *"That's your new feature out, the safe way. It was built and waiting, I made sure it still worked with your live app, your checks all passed and you watched them, you looked at the real thing and it's good, there's a bookmark you can jump back to any time, and what changed is written down. Same boring steps next release — that's the whole idea."*
- **Caught a red check:** *"Your seatbelt did its job today — it caught a break while your feature was still parked, before a single user saw it. We fixed it, the checks went green, and *then* we put it out. That's exactly how this is supposed to feel."*

Then one forward pointer: **`/release` again** on your next release date; **`/handoff`** reads these notes and bookmarks. Never a trailing list.

---

# Scope notes / known limits (mention if relevant; otherwise out of scope)

- **The seatbelts are the point.** No `/qa-harness` → this skill routes there first rather than running a checkless "release" that lies about safety. A red check stops the release cold and refuses the bookmark — that's the skill winning.
- **New features ride this; bugs don't wait for it.** A broken checkout doesn't get "scheduled" — it's a fix-now through `/ship-change`, and it appears here only as an already-shipped **Fixed** line. If a builder brings a live break to release day, route it to `/ship-change` today.
- **Release day is a real go-live, because the feature was held.** Even on an auto-deploy stack, the parked feature isn't live until this run flips it on. Don't call it "just a stamp" when a feature ships — it genuinely goes live here. (The stamp-only shape is the no-feature case: bless + bookmark + write up fixes that already went out.)
- **Fixing happens in `/ship-change`, not here.** A red check hands off to `/ship-change`, then you re-run `/release`. Don't improvise fixes inside a release run — release = blessing, not building.
- **`/release` ≠ `/ship-change`.** One change vs. putting scheduled features live. The tell is the release-only things: feature flipped on, checks ran, a bookmark was cut, notes were written.
- **Dates, not SemVer.** Date-based bookmarks/versions by default; SemVer optional, never required; no Conventional Commits, no CI assumed. Only git.
- **Rollback is `/safety-net`'s tested ladder aimed at a bookmark** — not a fresh mechanism. "Take me back to the July 4 version" resolves to that version's tag.
- **Scaled-down deploy strategy, honestly.** No blue-green / canary infra promised — the *intent* (hold a feature safely, prove it, verify after, one-command way back), not the machinery. A "hidden on/off switch" (feature flag) is the sturdier way to hold a feature than an unmerged branch, but it's an opt-in upgrade `/ship-change` can set up — not assumed here.
- **All-in-one platforms (Replit / Lovable / Bolt):** lean on the platform's built-in preview, checkpoints, and one-click rollback for the bookmark and the go-live; hold a parked feature on the platform's own branch/preview rather than re-building one. The changelog and chart still live as repo markdown for `/handoff`.
