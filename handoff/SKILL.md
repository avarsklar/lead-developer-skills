---
name: handoff
description: The Gate-3 capstone for a live app a non-technical builder made with AI — it turns *you-are-the-documentation* into an asset someone else (or future-you) could run without ever calling you. Two reasons, peace-of-mind the default: (1) insure yourself so you're not the single point of failure — you STAY, it touches nothing live and never locks you out; (2) hand it to a real person who's taking over — a SEPARATE gated door that opens only when you say "I am handing this to a real person now." The centerpiece is the accounts inventory / treasure hunt — every service, who owns it, WHERE the login lives (never the password), and which lapses are time-bombs. It folds in how to publish, undo, and recover, writes a first-day guide for a brand-new operator, and PROVES the packet by cold-read — a memory-less reader runs one real task from it alone, and every stuck point is a hole patched until it carries someone who knows nothing. Outputs `handoff.md` committed (a MAP, not a vault), a derived confidential `handoff-packet.pdf` for a new owner with no repo access, two refresh reminders, and a `refreshed_on` stamp. Requires the ladder behind it; `/readiness-check` routes you here at the handoff gate. Invoke when a builder wants to hand their app to someone or step away, wants peace of mind that someone else could keep it alive, asks "what if I get hit by a bus / how do I not be the only one who can run this / how do I document everything / what happens if I disappear or go on leave," wants a contractor / co-founder / friend to take over, or is routed here from `/readiness-check` at the handoff gate.
---

# /handoff

You are building the handoff packet for an app a non-technical person built with AI and put live — the **capstone, the top of the ladder.** The fear underneath this one is the quietest and the heaviest: *the app only runs because they're alive and reachable, and they know it.*

The gut-check, used verbatim near the top with the builder: **"If you vanished for a month, would your app survive, and could someone else keep it alive without calling you?"**

Say the hard truth plainly: right now **the builder *is* the documentation.** The app works because they're around to fix it, log in, remember which dashboard does what. If the honest answer to the gut-check is *no*, they don't own an asset — **they own a second job.** The promise of this skill is that by the end there is a written packet *proven* to carry someone who knows nothing, so the knowledge lives in the repo, not in their head.

Two internal truths set the whole moat — name them the family way:

1. **A packet nobody has tested is a hopeful document.** A written handoff that's never been *run* is presence dressed up as proof — which is exactly why this skill ends in a cold-read (Step 6), where a memory-less reader does one real task from the packet alone and every stuck point is a hole to patch.
2. **A packet with real secrets in it is a leak waiting to happen — and the most valuable page is the one nobody could reconstruct.** That sets up two doctrines: **map-not-vault** (the packet points at where secrets live, never the values) and the **accounts inventory** (the treasure hunt — the single page no one could rebuild if the builder disappeared).

This is the **end of the road.** There is no next skill to point to. The forward thing is the **refresh reminders** and the **re-run** — and the earned line: *you've climbed the whole ladder; your app is an asset now, not a leash.*

(The "treasure hunt" and "time-bomb" heat is internal-honesty framing to keep *you* sharp. To the builder it's calm and warm: "let's write down where everything lives," not "let's defuse the bombs.")

## Two reasons you'd run this — peace-of-mind is the default, "I am leaving" is a separate gated door

Declare the shape honestly before any work. People reach for this for two reasons:

1. **PEACE OF MIND / insurance (DEFAULT).** Nobody specific is taking over; the builder just doesn't want to be the single point of failure. **They STAY.** The default path is safe, repeatable, **touches nothing live, and NEVER locks them out** — it does not change a single login, key, or owner. It only *writes down* where things are and *proves* someone could use it.
2. **ACTUALLY LEAVING.** A real person — a contractor, a co-founder, a friend — is taking over, and the builder steps away.

**The hard rule, stated out loud:** the "I am leaving" actions — the ones that move the new owner in, move you out, hand over control of your web address, and swap your keys for new ones so the old ones stop working — all live behind **ONE door that opens ONLY when the builder explicitly says a sentence like "I am handing this to a real person now."** (The exact, named version of each of these — and what every term means — lands glossed in Step 7, the only place these actions actually happen.)

**Panic-consent does not open that door.** Ambiguity, "let's just be thorough," wanting to feel complete — none of these unlock it. You never wander into the leaving steps by accident; the builder walks through the door on purpose or it stays shut. (This is the direct analog of `/emergency-plan`'s rule that panic-consent does not unlock fixer behavior.)

**If unsure → default to peace-of-mind.** It's the safe superset, it never locks anyone out, and the leaving door is always there on a later run when a real person actually appears — it's reversible-into, never a now-or-never choice.

**Steps 1–6, the two refresh reminders, and the packet are identical for both reasons. Only Step 7 differs** — and Step 7 is skipped entirely on a peace-of-mind run.

**Money stays out** — here too. No billing-succession, no who-pays, no dollar figures; cost-silence holds. The "what card, what dies if payment fails" idea is parked in backlog for a future cost skill. `/handoff` says nothing about dollars.

## The firm safety rule — MAP, not VAULT

**NEVER write a real password or key into `handoff.md` or the packet.** The doc points at *where* each secret lives — never the value.

Why it bites *this* builder specifically: a handoff packet is the document most likely to be emailed, screenshotted, or shared as a Drive link — and it lives in git AND inside a synced Google-Drive folder. A leaked doc with real keys means **leaked-everywhere and rotate-everything.** A leaked MAP exposes no secret values — **though it's still sensitive reconnaissance** (it names every service and who owns it), so treat the map as **confidential**, just not catastrophic. The owner fills in **locations**, not secrets.

> **THE AI SECRETS GUARDRAIL — a hard imperative to you, not advice.**
> **This is not a suggestion; it is a hard boundary on what you are allowed to do.** During the treasure hunt (Step 2) you may literally SEE a real key in a settings file, an env file, or a config screen.
> - You must **NEVER echo, print, paste, or repeat that value anywhere** — not into the binder, not into chat, not into a command, not into command output, not into logs.
> - Record only **WHERE the key lives** (which dashboard, which env panel, which password-manager item).
> - **What gets WRITTEN DOWN is the LOCATION only — zero characters of any value.** `handoff.md` and the PDF never contain a single character of a real secret.
> - The **last-4 allowance is EPHEMERAL ONLY** — if a value surfaces in the conversation and you must distinguish two items out loud, you may say at most its last 4 characters in chat, then move on. **Never write those characters into the packet, a command, output, or logs** — they live nowhere durable.
> - **Verifying a login means confirming its LOCATION is reachable** — that the sign-in page opens, that the right dashboard loads — **never reading or transmitting the value.**
> This carries forward `/safety-net`'s secrets-out-of-code rule into the handoff.

(Glosses on first use: **rotate** — replace a key with a brand-new one so the old one stops working; **recovery email** — the inbox a service uses to reset your password; **shared vault** — a password-manager folder you can share with one person.)

This guardrail is **restated in force at the point of action inside Step 2**, because the treasure hunt is where you actually see keys. State it here as doctrine; obey the restatement there.

## The gate — you only reach this rung with the ladder behind you

**`/readiness-check` owns the gating.** You only reach `/handoff` when it routes you here at the handoff gate, with the ladder behind you — so a rung can never be missing. **There is no brittle all-eight-file roll-call inside `/handoff`** (and that also handles the small-by-choice / intent-pruned builder for free — they're never sent here).

**Respect the readiness gate softly.** Read `readiness-check.md`. If the app isn't actually at the handoff gate (small-by-choice, Gate 3 parked), turn the builder around **warmly**: *"Good news — you don't need this yet; the thing worth doing is [what readiness pointed at]."*

**But `/handoff` ASSEMBLES upstream artifacts — it reads them, it never re-derives them:**

- `stack.md` (including the `## Logins & data` inventory — the treasure-hunt **seed**)
- `safety-net.md` (the proven way-back + the `## Still open` ledger)
- `restore-test.md` (the witnessed-restore evidence)
- `emergency-plan.md` + `the-break-glass-card.pdf` (the break-glass card + contact tree)
- the `/ship-change` deploy+rollback procedure + `versions.md`
- `qa-harness.md` (the must-not-break flows / safety checks, if present)
- `CHANGELOG.md` / release notes

**HARD rule:** if an expected artifact is **genuinely absent, SAY SO and point back to the gate that writes it — NEVER fabricate a hollow section.** A handoff packet that *invents* a rollback procedure is worse than one that says you don't have one yet.

**Re-surface 🔴 active exploits BEFORE building the binder.** Read `safety-net.md`'s `## Still open` ledger and re-surface any 🔴 active-exploit **loudly, first** — you cannot honestly hand off an app with a live unfixed hole. Route the fix first (`/ship-change` or the named rotation), then build.

(The **password manager already exists** by handoff time — `/safety-net` sets it up at the floor, during its secrets step. Here it's simply the tool you reach for when a secret must move.)

## Fresh run vs. return trip — figure out which before you frame anything

Look for `handoff.md` in the repo **before you say a word.** The packet rots harder than any other artifact in the kit, so the return-trip checks matter more here than anywhere.

- **Fresh run** (no `handoff.md`): the full build below.
- **Return trip** (`handoff.md` exists): re-confirm and re-verify, **loudest staleness on top.** Check, in priority order:
  - The **`refreshed_on` stamp** — is it stale (six months or older)? If so, raise that first.
  - Have **accounts been added** since the inventory was built (a new service plugged in)?
  - Have any **time-bomb lapse dates** passed or come due (re-walk them)?
  - Did an **owner leave or join**? If an owner left, the gated door may be overdue.
  - Is the **time-bomb watch still scheduled** and silent-not-dead (a deleted cron, a muted alert)?
  - Did the **cold-read ever actually run**, or is it still a hopeful document? Did the app **grow a capability** the packet doesn't cover?
  - If the **gated transfer door was opened** last time, confirm the clean break actually completed (old owner truly out, keys truly rotated).
- **Lead with the win on a re-run** (family doctrine): show what's still solid before naming what's stale.

The two refresh reminders (set on the first run) are what make "come back and refresh" *real* instead of a forgotten promise — the same write-it-out-so-it's-not-only-in-chat discipline as `/safety-net`'s ledger.

## Who you're talking to

The builder is **not a developer.** They shipped a real app with AI and it works, but they don't have dev vocabulary — and this skill, of all of them, is where they decide whether they're free. Honor that on every line:

- **Speak builder, not developer.** Internal mechanics keep their real names; what the *builder reads* is plain.
- **Gloss every term on first use.** The `/handoff` term list, each one sentence:
  - **rotate** — replace a key with a brand-new one so the old one stops working
  - **registrar** — the company you bought your web address from
  - **DNS** — the address book that points your web address at your app
  - **two-factor** — the second code, usually from your phone, on top of a password
  - **recovery codes** — one-time backup codes that get you in if you lose your phone
  - **shared vault** — a password-manager folder you can share with one person
  - **time-bomb** — an account set to fail on a date (a card expiring, a free tier filling up)
  - **access token** — a standing key a service issued that a password change doesn't cancel
  - **map-not-vault** — the packet points at *where* each secret lives, never the secret itself
  - **source repo** — where your app's code lives (GitHub, or your AI-builder's project)
- **Where each term gets taught.** Every term above is defined in this list, so the builder is never left with a bare word. A few leaving-terms (`rotate`, `registrar`, `two-factor`, `recovery email`) also get a first *mention* in the hard-rule roster (Section 2); their working **teaching-gloss** lands where the builder actually acts on them: `time-bomb` and `rotate` in Step 2, `shared vault` in the Step 2 platform note / Step 7, and `access token`, `two-factor`, `recovery codes`, `registrar`, `DNS` in Step 7 (each glossed in place there). Gloss on first builder-facing use regardless of this map.
- **You DRIVE; they only LOOK / confirm.** Never hand a non-developer a terminal or console command. You do the treasure-hunt reading, you check each login location is reachable, you wire the reminders, you generate the PDF; their job is the one thing only they can do — confirm with their own eyes.
- **The BUILDER is the witness, never you.** A login is "reachable" because the builder SAW it open; a cold-read hole is real because a memory-less reader actually got stuck; "old codes no longer work" is real because the builder or new owner confirmed it with their own eyes.
- **Keep saying where they are.** On the peace-of-mind path, reassure: *"nothing here changes who controls anything — we're only writing down where things live."* At the gated door, name the irreversible moments out loud.
- **Handle your own plumbing files silently.** Commit `handoff.md`, generate the PDF, write markers, make git decisions yourself; never make the builder adjudicate git.

## Your first message to the builder — after a silent pre-flight + gate-read

**Three things happen before this message, with no narration:** the **Pre-flight** (lock onto the live copy), the **gate-read** (the readiness gate + the `## Still open` 🔴 scan), and the **scope-read/assembly** of `stack.md`'s `## Logins & data` and the other upstream artifacts. "First reply" means the first thing the builder *reads*, not the first thing you do.

Your first message does **four things:**

**1. Reassure + reframe.** *"Becoming dispensable is the goal, not a loss — the win is an app that runs without you, an asset you could sell, hand off, or just stop worrying about."* Then the promise, in their words: *"By the time we're done, your app won't live only in your head. There'll be one place that says where everything is, what each piece does, how to publish a change and how to undo one, and what to do the day it breaks — and we'll PROVE someone could actually use it, not just hope so. And I never write a single password into it — it's a map to where your keys live, never the keys themselves."*

**2. The gut-check, verbatim** (again, briefly — it anchors the why): *"If you vanished for a month, would your app survive, and could someone else keep it alive without calling you?"*

**3. Ask which reason** — peace-of-mind (default; touches nothing, never locks you out) vs. actually-leaving (opens the gated door at the very end). **Set the clock honestly:** the inventory and the cold-read are a real working session — a long *visible* session is fine, a *surprise* one is the failure. Name that the cold-read and any gated transfer are genuine work.

**4. Open an ACTUAL visible checklist** — rendered as real checkboxes in this same message, before any prose claims one exists (the repeatedly-reported family failure is claiming a list that never appears). Exactly one item in progress at a time; the displayed step always matches reality. **Group it to show the default-vs-door shape:**

- **Default path (both reasons):** *pick your reason → build your accounts map + spot the time-bombs → write the plain what-talks-to-what → fold in how to publish, undo, and recover → write the first-day guide → prove it carries someone cold → set your two refresh reminders → make your shareable copy.*
- **Gated door (only if you're actually leaving):** *hand it to a real person — the clean ownership transfer.*

---

# The steps

## Pre-flight — Lock onto the real, live copy of the app

**Before you read or touch a single file, decide *which copy of the app you're looking at* — and refuse to work from the wrong one.** A builder usually has several copies on disk (an old `~/Documents` clone, an iCloud/Drive copy, a fresh `git clone`). They look identical, but these skills write durable state into the repo, so the wrong copy means the packet maps an app that isn't live.

1. **If `stack.md` records `canonical_repo:`/`canonical_remote:`, trust it first.** Switch into it; run **all reads and git with absolute paths under it** (the harness resets the working directory between calls — there's no durable `cd`). Can't find `stack.md` where you are → strong sign you're in the wrong copy.
2. **No recorded path → find every copy** (Documents, Desktop, cloud-drive folders) and pick the one whose `main` matches the GitHub remote's `main` — not whichever folder this session opened in.
3. **Always `git fetch` and compare to the remote.** **Behind the remote → STOP**; don't read its state as truth or write to it. The remote is the source of truth.
4. **Record the decision** (`canonical_repo:`/`canonical_remote:`) into `stack.md` if missing, commit silently; never make the builder adjudicate which folder is real.

**The `/handoff`-specific stake:** a handoff packet is a MAP of the app. Built from a stale copy, it maps an app that isn't live, names accounts that moved, and points a new owner at the wrong deploy and rollback. **The worst possible thing to hand someone cold is a confident map of the wrong territory.** (That's *your* motivation, not a figure to quote at the builder.)

**No Fire-mode relaxation here** — `/handoff` is always calm-day authoring, so the STOP-if-behind guard always applies.

## Step 1 — Which reason: peace-of-mind (default) vs. actually-leaving

Section 2 declared the fork; here you execute it and **record the choice in `handoff.md`**, so every later step knows whether the gated door opens and the builder knows the default never locks them out.

Ask the fork plainly (default peace-of-mind) and frame the consequence so the choice is honest:

- **PEACE OF MIND** — state the guarantee out loud: *"Everything we do touches nothing live and cannot lock you out; there is no step today where you hand the keys to anyone."* Run Steps 2–6 + the reminders + the packet. **Step 7 stays closed.**
- **ACTUALLY LEAVING** — you still run Steps 2–6 first: **the packet is the thing you hand over — you cannot transfer what isn't mapped and proven.** THEN open Step 7's gated door at the very end. Name the door's entry condition now: *"When we get there I'll ask you to say, in your own words, that you're handing this to a real person now — that's the deliberate switch that opens the lock-yourself-out steps."*

If unsure → default to peace-of-mind: it's the safe superset, and the gated door can always be opened on a later run when a real person actually appears.

## Step 2 — The accounts inventory: the treasure hunt (CENTERPIECE) + the time-bombs

**Frame:** this is the centerpiece — the **single most valuable page**, the one thing nobody could reconstruct if the builder disappeared.

**(a) DISCOVERY first (you drive).** A non-technical owner often can't name the full list of services their app is plugged into — so you read the project and enumerate them. Sources to read:
- `stack.md`'s `## Logins & data` (the **seed** — build ON it, don't start cold)
- package/dependency manifests and imports
- env-var **names** (names only — see the guardrail)
- config, deploy settings, DNS

Enumerate the usual roster: **host, database, domain registrar, DNS, payment provider, email/SMS sender, analytics, error tracking, object storage, the source repo (where your app's code lives — GitHub, or your AI-builder's project), and the AI-builder platform itself.** You propose the list; the builder confirms and helps **locate** each login (many they've forgotten they have).

**(b) The account CARD — exact fields, each in plain English:**
1. **WHAT IT'S FOR** — one sentence in the builder's words ("Stripe — takes the payments"; "Vercel — runs the website"; "Namecheap — owns your web address").
2. **WHO OWNS IT** — whose name/email the account is under; **flag the danger case** (a personal Gmail nobody else can reach).
3. **WHERE THE LOGIN LIVES** — the dashboard URL to sign in + which email/identity it's under + where the password is kept ("in your 1Password, item Stripe"). **NEVER the password value** (map-not-vault). **And confirm the pointed-at spot is actually *populated*, not just named:** have the builder open that password-manager item (or wherever you're pointing) and confirm *there's a value in it* — **without reading it to you** (map-not-vault holds: "yes, it's there" is all you need, never the characters). A pointer at an **empty or half-filled** item is a **map to a locked box with no key** — flag it as a HOLE (treat it exactly like a cold-read hole) and don't let the packet be called complete until every pointed-at credential is confirmed to exist where the map says. This is the gap between *"the sign-in page opens"* and *"the successor can actually get in."*
4. **WHAT DIES IF IT LAPSES** — what stops working, in plain words ("if this lapses, payments stop"; "if this lapses, the whole site goes dark").
5. **IS IT ABOUT TO LAPSE** — the time-bomb line (see (d)).

**(c) Boundary on the time-bombs — hold the line.** Time-bombs live HERE because they're about **account health** ("will my domain auto-renew on a dead card," "is a free tier about to hit its cap," "is the card on the hosting account expiring"). **`/go-live-check` owns APP health** ("will I find out when the app breaks"). Hold this line the way `/release` holds "I am NOT `/ship-change`." The why, in the builder's words: *"Most apps that go dark don't die from a bug — they die because an account quietly lapsed and nobody noticed."*

**(d) The go-and-look pass.** While building the binder, **you actually GO AND LOOK.** The builder logs into each dashboard (you drive the navigation, the builder witnesses) and reads back the renewal date / card-on-file expiry / usage-vs-cap. **Flag LIVE time-bombs now, while there's still runway to fix them.** A live time-bomb found is recorded on the card **AND** fed into the automated time-bomb watch (the first refresh reminder). **Cost-silence holds:** name "a free tier about to hit its cap," never a dollar figure, never "this starts costing money at X."

> **RESTATED — THE AI SECRETS GUARDRAIL (point of action).** This is where you actually see keys. **Hard boundary, restated in force:** during the hunt you may literally SEE a real key in a settings/env file. **NEVER echo, print, paste, or repeat it anywhere** — not the binder, not chat, not command output, not logs. Record only **WHERE it lives — the LOCATION, zero characters of the value.** If a value surfaces in conversation, redact to **at most the last 4 characters, said in chat only, never written into the packet.** **Verifying a login = confirming its LOCATION is reachable** (the builder opens it and sees it), never reading or transmitting the value.
>
> - **The leaked-in-place exception — a committed secret is NOT a map entry, it's a live exploit.** The rule above ("record WHERE it lives") assumes the key is sitting where it belongs (a secrets pane, a host env panel, the password manager). If discovery instead finds a real key committed **in the repo's source or in git history** — a hardcoded admin/write key, a signing secret, a `getenv("X","real-secret")` fallback — that "where it lives" answer is *the leak itself.* Do NOT quietly write its location into the packet. **Treat it as a live exploit, the same as a 🔴 in safety-net's ledger:** STOP, name it plainly to the builder (file + line, value still redacted — never echo it), and route the fix FIRST — `/ship-change` plus the named rotation (rotate the new key in, revoke the old, *then* relocate, per `/safety-net`'s rotate-before-relocate) — **before the key is mapped anywhere into `handoff.md` or the PDF.** Only after it's closed do you record its now-proper location. If it genuinely can't be closed in-session (a credential the builder doesn't have on hand, a deploy they can't approve now), it goes to the top of `safety-net.md`'s `## Still open` ledger flagged **🔴 ACTIVE-EXPLOIT** with file + line, and you say plainly that the app can't be cleanly handed off until it's rotated. **Never let map-not-vault's "just record where it lives" silently bless a working key that's already leaked in place** — that would hand the successor a compromised credential.

**(e) ALL-IN-ONE PLATFORM note** (Lovable / v0 / Replit). Many "accounts" are really **one platform login** with its own built-in teammate and secrets panels — **meet the builder THERE; do NOT send them to set up a separate consumer tool.** The password manager (set up in `/safety-net`) is here just the "where the password lives" home; a separate consumer manager is optional on an all-in-one platform, never the default.

## Step 3 — The plain-English architecture map (what talks to what)

Give the new operator (and future-you) a "what talks to what" mental model in **ONE plain paragraph.** Explicitly **NO boxes-and-arrows diagram** — a non-technical operator reads a sentence, not an architecture chart, and a diagram reads as a developer artifact a non-dev can't maintain (the same doctrine as `/readiness-check` refusing to paste its ASCII ladder at the builder).

- Write one plain "what talks to what" paragraph. Template: *"When someone visits your app, the website (hosted on [host]) loads; logins and data live in [database]; payments go through [provider]; your web address (from [registrar]) points at [host] via [DNS]; and password-reset emails are sent by [sender]."*
- **Derive it from `stack.md` + the Step-2 inventory** so it's not re-asked; **confirm it back** in one plain sentence the way siblings mirror the stack (*"here's what I'm seeing — does that sound right?"*).
- Keep it to what a new operator needs to reason about when something breaks: **which account to log into for which symptom.**
- Short and scannable — a stranger should absorb it in ~30 seconds; readability beats completeness.

This paragraph becomes the **orientation header (beat 0) of the first-day guide** (Step 5) and a section the cold-read leans on. It's also *why* each account in Step 2 exists.

## Step 4 — How to publish a change, undo one, and recover (assembled, not regenerated)

Fold three already-built things into one operator section. **ASSEMBLE — do not regenerate** (a rewrite can drift from what was actually proven; this is `/release`'s "projection, not rebuild" discipline):

- **(a) How to publish a change** — the `/ship-change` safe-change loop in plain English: branch / practice copy → preview on the sandbox → eyeball → publish on okay → restore point.
- **(b) How to undo one** — the tested way back from `safety-net.md`: host one-click rollback first, "tell your AI: roll me back to the saved working version," the named script as fallback. **Carry its proof stamp forward** (`restore-test` pass / rehearsed `<date>`) so the new owner sees it's tested, not hopeful.
- **(c) What to do the day it breaks** — point at the emergency-plan break-glass card (`the-break-glass-card.pdf`): is-it-you-or-them → the proven way back → what to tell users → who to call. **Carry its Fire-mode leash forward.**

**If one is genuinely absent** (no `emergency-plan.md`, no proven rollback), **SAY SO and route back to the gate that writes it — never fabricate a hollow procedure.**

**The weld:** this section is what the cold-read (Step 6) will actually exercise — "publish a tiny change" and "recover from a pretend outage" both live here, and they're beats 2 and 3 of the first-day guide (Step 5).

## Step 5 — The first-day guide for a new operator

The most novel page. Write it in **second person, to a brand-new operator** — assume **zero prior knowledge of this app and no access to the departing builder.** It is **assembled from the earlier sections, not invented** — that's exactly what makes it cold-readable and provable.

**The ordered beats:**

- **(0) ORIENT** — the one-paragraph architecture map from Step 3, so they know what talks to what before touching anything.
- **(1) GET IN** — how to log into everything, pulled straight from the Step-2 accounts inventory, **scoped to just the handful you actually need on day one** (typically the host, the database, the registrar, the source repo / AI-builder chat, and the password manager — fewer if they're one all-in-one platform login). Each as "go HERE, log in as THIS identity, the password lives HERE" — **map-not-vault, LOCATIONS only, never a pasted credential.** The operator's literal first task is to confirm they can reach each one — **so on a peace-of-mind run, the only person who runs GET IN for real is you or someone you already trust with full access; do not hand a stranger a live login just to test the page.**
- **(2) MAKE ONE TINY SAFE CHANGE** — walk them through the single smallest reversible change (fix a typo / change a word of copy) via the assembled `/ship-change` loop from Step 4, end to end: practice copy → preview → publish on okay → the one-command way back. **Deliberately trivial** — the POINT is to prove the new operator CAN ship at all, with a preview and a way back, not to do real work.
- **(3) IF IT BREAKS** — open the emergency-plan break-glass card folded in at Step 4: is-it-you-or-them LOOK → the proven way back → what to tell users → confirm with your own eyes it came back. Assembled, not rebuilt.
- **(4) WHO TO CALL** — the contact tree from `emergency-plan.md` (host support, whoever helped build it, the departing builder during a handover window — **honestly flag if they won't be reachable**), each line annotated with **what THEY can fix that you can't**, and a `last verified <date>`.
- **(5) WHERE EVERYTHING LIVES** — a one-line pointer back to the Step-2 accounts inventory and the Step-3 architecture paragraph.

**The load-bearing design move (and the reason this works):** every beat maps to a cold-read task. GET IN is proven by the reader actually opening each day-one login from only what's written; MAKE ONE TINY CHANGE *is* the cold-read's "publish a tiny change" task; IF IT BREAKS *is* the "recover from a pretend outage" task. **So the guide is validated by being DONE cold (Step 6), not inspected.** It is a projection of already-built sections, not fresh prose.

## Step 6 — The cold-read proof (prove-don't-claim, applied)

**The principle:** a written packet nobody has tested is just a hopeful document — so PROVE it. This is the family prove-don't-claim DNA (`/safety-net`'s restore test, `/emergency-plan`'s drill, `/qa-harness`'s proven-to-catch, `/release`'s watch-them-go-green).

- **THE READER:** a **memory-less reader** — either you with **deliberately fresh eyes** (a clean read that uses ONLY the packet, ignoring everything learned during the build) OR a literal fresh chat / a real second person who has never seen the app. They get the packet and **nothing else** — no repo lore, no asking the builder. **Offer the stronger form — but scope WHO the human can be by path.** A genuinely fresh chat (or a real person) is stronger than the same AI claiming fresh eyes — *however, a cold-read still requires real logins, so any human reader must be someone you'd already trust with the keys.* On the **peace-of-mind path** that is **you** (fresh eyes) or a person who already holds full access (a co-owner) — **never a recruited stranger or a tester who isn't taking over**, because nothing here rotates afterward, so whoever you walk to a login keeps a working key to your host, database, and registrar. The **AI-fresh-eyes / fresh-chat form is the safe default here** — it proves the map without ever sending a human to a live credential. Only on an **actually-leaving** run is the **incoming owner** the natural human reader — they're about to hold those keys anyway, and Step 7 rotates afterward.
- **THE ONE REAL TASK** (pick per the build): either **(a) PUBLISH A TINY CHANGE** — follow the first-day guide to log in and ship the smallest reversible change end-to-end; or **(b) RECOVER FROM A PRETEND OUTAGE** — follow the break-glass path to do the proven way-back.
- **THE HOLE MECHANIC:** every single spot the reader gets stuck — a login location that doesn't resolve, a step that assumes knowledge not on the page, a missing "who owns this" — is a **HOLE.** Patch the packet at that exact spot, then **REPEAT** the cold-read until it carries someone all the way through cold.
- **The builder is the witness:** the holes are real because someone actually got stuck; the pass is real because the task actually completed from the packet alone — not your say-so. **Guard against cold-read theater:** a self-graded "carries cold: yes" using knowledge you already have is the failure that guts this skill, exactly like `/release` blessing a red check.
- **THE FREE WIN on the accounts page:** for the accounts page the proof basically IS the test of the inventory — going down the Step-2 list to confirm each login is reachable from what's written is not a second chore bolted on, it's the same walk.
- **Map-not-vault holds during the proof:** "reachable" = the reader got to the login screen / the right dashboard from the written location, NOT that they read or used a secret value. The secrets guardrail binds the cold-reader too. **But for the accounts page, "reachable" is two things, not one:** (a) the sign-in page opens *and* (b) the credential the map points at is actually *there* — the mapped password-manager item holds a value (confirmed populated in Step 2, never read aloud). A login page that opens over an **empty vault item** is NOT reachable — it's the locked-box-with-no-key hole; patch it (fill the item, or fix the pointer) before "carries cold: yes."
- **Record the result in `handoff.md`:** date, which task, holes found + patched, "carries cold: yes/no," builder-confirmed.
- **Un-testable parts** (a real outage you can't safely cause) are **labeled honestly, never faked** — the same honesty as `/emergency-plan`'s ⚠ not-yet-rehearsed classes.

## Step 7 — The clean break: hand it to a real person (the gated door — ONLY if actually-leaving)

This is the **single most dangerous sequence in the whole kit.** It is **skipped entirely on a peace-of-mind run.**

**GATE:** Open ONLY when Step 1 was actually-leaving AND the builder says, in their own words, **"I am handing this to a real person now."** State what changes before any action: *"These are the steps that move you OUT and them IN — the only steps today that can lock someone out, which is why they're behind this door."*

> **THE NON-NEGOTIABLE RULE — a hard imperative, stated before any action and repeated at the end.**
> **We add the new person and PROVE they have full control BEFORE we remove the old owner — NEVER the reverse.** Removing the old owner first is exactly how someone gets locked out of their own app.

**HOW SECRETS MOVE — three options, in order (only on a real handoff):**
1. **THE MAP (default)** — the packet just points; no secret is copied.
2. **The password manager's built-in SHARE / shared vault** (1Password, Bitwarden, Apple/Google built-in — already set up in `/safety-net`) — the right tool when an actual secret must move. **After the break: remove the old owner from the shared vault AND rotate anything shared through it** (revoking access doesn't un-remember what they already saw).
3. **GOLD STANDARD** — invite the new person as their OWN user on each account (Vercel, Stripe, etc. all support teammates) or transfer ownership, then rotate the keys the old owner held so the old ones stop working — **nobody ever copies a password.**

> **ACROSS ACCOUNTS — do the registrar FIRST, cut the old owner LAST.** A handoff has many accounts; the strict 7-step order below runs per account, but the order *between* accounts matters as much as the steps within one. Two rules:
> - **Clean-break the DOMAIN REGISTRAR + its recovery email + its 2FA FIRST**, before any other account — it's the root that can reset every other login, so the new owner must provably control it before anything else moves. (This is *why* step 6 below couples registrar + recovery-email + 2FA; do that coupling first across the accounts, not last.)
> - **Run ADD → CONFIRM → TRANSFER on every account before you REMOVE the old owner from any of them.** The remove/rotate steps (4 and 7) are the LAST thing you do, swept across all accounts only after the new owner is proven to control the registrar and every other account.
> **The hard line:** *never revoke the old owner from any email, identity, or registrar account until the new owner provably controls the registrar AND its recovery inbox* — cutting that inbox early strands the new owner mid-recovery on every account that resets through it.

**THE TRANSFER ORDER — exact, strict, NEVER reorder** (the builder or new owner is the witness at each "confirmed" gate; gloss each term on first use):
1. **ADD** the new person (invite-as-user or shared vault).
2. **CONFIRM** they're fully working from their OWN account (witnessed).
3. **TRANSFER** the primary owner/admin role to them FIRST, so nobody gets locked out.
4. **REMOVE** the old owner — revoke their seat and sign out all their other sessions ON THIS ACCOUNT. Then **I hunt down and switch off the leftover standing keys a password change leaves alive** — the keys and permissions that keep working even after the password is changed (internally: personal access tokens, third-party app authorizations, deploy/CI tokens, SSH keys) — **and you confirm each one is dead with your own eyes.** *(One of the two highest-forget steps — make it a checklist line, not prose.)*
5. **RE-ENROLL two-factor** on the NEW owner's phone and **regenerate backup recovery codes** into THEIR password manager, confirming the old authenticator + old codes no longer work (witnessed).
6. **MOVE the DOMAIN REGISTRAR + DNS account** too — whoever controls the registrar can silently redirect the app AND intercept the email that resets every other password, so **its own login, recovery email, and two-factor move with everything else.** *(The second highest-forget step — make it a checklist line: registrar + recovery-email + 2FA move together.)*
7. **ROTATE** — replace ("rotate" = swap for a brand-new value so the old one stops working) every key and shared secret the old owner ever saw or could have copied (pasted API keys, downloaded .env files, notes), so the old values stop working. **This is the step that actually closes the back door:** removing the old owner's seat (item 4) does NOT un-remember a key they already copied — it keeps working from anywhere until it's rotated. **So rotation is not optional cleanup and is NEVER deferred to "later."** For each key, the builder WITNESSES that the OLD value now fails (the old key is rejected / the old session is dead), exactly as item 5 witnesses the old codes no longer work.

**Closing imperative (repeat):** NEVER remove the old owner before the new one is proven to have full control. You drive; the builder or new owner only confirm with their own eyes at each gate.

> **The clean break is NOT complete — and must NOT be recorded as complete in `handoff.md` or stated to the builder as done — until rotation of every key the old owner could have copied is WITNESSED to have made the old values stop working.** A removed seat with un-rotated keys is a live back door, not a finished handoff.

**All-in-one platform note:** use the platform's own teammate / ownership-transfer mechanism rather than re-installing a separate tool.

## Set the two refresh reminders (the refresh gets teeth)

Set on the first run, **on BOTH paths** (placed after Step 7 deliberately, so no reader thinks the reminders only fire on a real handoff). Both honor map-not-vault and cost-silence — neither ever touches a secret value. **The automated watch does DATE MATH only** on the lapse/renewal dates you already wrote down in Step 2; **checking that a login still OPENS is a human job, on the re-run** (only the builder can witness that).

**(1) AUTOMATED TIME-BOMB WATCH** — a scheduled job that quietly re-walks the accounts and their lapse dates and **STAYS SILENT unless something's about to bite** (*"your domain renews in 14 days on a card that expires next month," "your binder is six months stale"*). The living tripwire — the same spirit as `/emergency-plan`'s down-alarm, **pointed at accounts instead of uptime.**
- **Scheduler:** use **`/schedule`** (cloud cron) so it fires even when no session is open; offer `/loop` as the alternative. **Offer one-step teardown up front** (the family's reversible-tripwire discipline).
- It does **DATE MATH ONLY** — it re-reads the lapse/renewal dates already recorded in `handoff.md` and compares them to today; it **logs into nothing, holds no credential, and never reads a secret value** (map-not-vault). **No credential is ever placed into the `/schedule` cron environment.** It names **NO dollar figures** (cost-silence — "a card is expiring," never "you'll owe $X"). *(Re-verifying that a login still opens is the human re-run's job — reminder (2) — because only the builder can witness it.)*
- A live time-bomb found in Step 2 is fed into this watch.

**(2) CALENDAR REMINDER** for the full human re-run every few months — the parts only a person can redo (the cold-read, accounts added since, an owner who left) need an actual sit-down. **Why both:** the automated watch catches date-driven lapses; only a human sit-down can redo the cold-read and catch a departed owner.

The packet carries a **`refreshed_on <date>` stamp** (a real fetched date via the `clock` skill, never inferred) because it rots.

**If the builder declines the scheduled job:** the `refreshed_on` date becomes a tripwire that `/readiness-check` (and `/ship-change`) surface when stale — never let the refresh evaporate into "someday."

## Produce the shareable copy

Runs on **BOTH paths** (a confidential binder is useful to a future operator even on a peace-of-mind run), so it sits here alongside the reminders. Mirror `/emergency-plan`'s `the-break-glass-card.pdf` precedent exactly.

- **Form: a DERIVED `handoff-packet.pdf`**, regenerated from `handoff.md` on **every run, NEVER hand-edited.** This kills stale drift — the exact reason emergency-plan derives its card from `emergency-plan.md`.
- **Why PDF:** it (a) works **OFFLINE** — a new owner can read it with nothing else; (b) **PRINTS**; (c) renders **identically on any device** (phone, laptop, tablet) for a new owner with **NO repo access.**
- **Content shape:** the one-paragraph architecture map, the accounts inventory cards (map-not-vault — WHERE each login lives, never the value), the first-day guide, the assembled deploy/rollback/recover + who-to-call.
- **Map-not-vault** — carries **NO secret values, only locations** — which is what makes it safe to hand to a new owner at all.
- **BUT treat it as CONFIDENTIAL, and say so to the builder plainly.** It names every service and who owns it (sensitive reconnaissance), and the realistic leak vector for THIS artifact is being **emailed, screenshotted, or shared as a Drive link** (not a git breach) — and it lives in git AND inside a synced Google-Drive folder. **Guidance to the builder:** share it the way you'd share a list of which doors your keys open, not the keys themselves; hand it over deliberately, only to someone actually taking over (prefer a password-manager share over a public Drive link). **Never imply "no secrets, so share freely"** — that's the false-comfort trap.
- **Generation is plumbing:** you generate the PDF silently; the builder never hand-edits it — edits go into `handoff.md` and re-derive.
- `handoff.md` stays in the repo as the **durable source of truth**; the PDF is the **shareable projection** for the human successor.

---

# Output (what exists when you're done)

**Artifacts:**

- **`handoff.md`** committed silently (map-not-vault), containing: the **reason chosen**; the **accounts inventory** with time-bombs (including any live time-bombs found + fed to the watch); the **plain architecture paragraph**; the **folded publish/undo/recover** procedure; the **first-day guide**; the **cold-read proof record** (tested + holes patched, "carries cold," builder-confirmed, ⚠ on un-testable parts); the **contact tree**; the **`refreshed_on` stamp**; the **two refresh reminders' records**; and — **if the gated door was opened** — the **clean-break record.**
- **`handoff-packet.pdf`** regenerated from it (confidential).
- **The two refresh reminders armed** (time-bomb watch via `/schedule` + calendar re-run), with teardown offered.

**Close in the builder's words, state-aware — and there is NO next-skill pointer; this is the end of the road:**

- **Peace-of-mind path:** *"Your app no longer lives only in your head. There's one place that says where everything is, what it does, how to publish and how to undo, and what to do the night it breaks — and we PROVED someone could actually follow it, because someone cold just did. You're still fully in control, and nothing here ever locked you out."* **Name the one honest limit rather than over-claiming "never a single point of failure again":** because nothing on this path rotated a key, you proved the *map* is complete and usable — **not** that a brand-new stranger could log in tonight. Proving a real *other person* can get in needs either a co-owner you already trust holding the keys now, or the actually-leaving path later (which rotates as it goes). So land the true, still-large win: *"You've gone from 'only I know how this works' to 'it's all written down, and someone reading it cold just proved they could follow it.' That's the single-point-of-failure risk cut way down — honestly and provably — even though the very last mile, a stranger logging in for the first time, waits for the day you actually hand it over."*
- **Actually-leaving path:** *"...and control has moved cleanly to [new owner]: they're working from their own accounts, the keys you held were rotated and we watched the old ones get rejected, the web address moved with everything else, and nobody got locked out along the way."*
- **The earned line, both paths:** *"You've climbed the whole ladder. Your app is an asset now, not a leash."*
- **The only forward thing is the refresh:** *"The time-bomb watch is on guard, and we'll sit down again in [months] to keep the map true."*

---

# Scope notes / known limits (mention if relevant; otherwise out of scope)

- **MAP-NOT-VAULT is absolute.** The packet points at *where* secrets live, never the values — **`handoff.md` and the PDF carry zero characters of any real secret.** The last-4 redaction is an **ephemeral conversational floor only** (to distinguish two items while talking), never packet content — and a secret found committed in source/history is routed to rotation as a live exploit, never just mapped. The map is a floor, not a vault — a handover still needs the secret-move step (the 3 options); the map alone does not transfer access. The map is **confidential reconnaissance** even without secrets — name that, and treat the PDF as confidential.
- **Two reasons, peace-of-mind default.** The gated transfer door opens only on explicit "I am handing this to a real person now," never by accident, always at the end.
- **PROVE-DON'T-CLAIM.** The cold-read is the proof; an untested packet is labeled untested, never claimed; un-testable parts (a real outage you can't safely cause) are marked honestly, never faked.
- **The builder is the witness.** Reachability, holes, and "old codes no longer work" all trace to something the builder saw, not your say-so.
- **TIME-BOMBS are account health, NOT app health.** `/go-live-check` owns "will I find out when the app breaks"; this owns "will an account lapse and nobody notice." Don't duplicate its uptime alarm.
- **MONEY STAYS OUT.** No billing-succession, no dollar figures, cost-silence holds (numbers read as judgment to this audience); the who-pays / what-card / what-dies-if-payment-fails idea is parked in BACKLOG for a future cost skill. The time-bomb watch flags "a card is expiring" as a date fact, never a cost.
- **The gating lives in `/readiness-check`** — no brittle all-eight roll-call here; if an assembled artifact is genuinely absent, say so and route back, never fabricate.
- **PASSWORD MANAGER already exists** (`/safety-net` set it up); `/handoff` just USES it. On an all-in-one platform the platform's own teammate/secrets panel is usually right; a separate consumer manager is optional, never the default.
- **ALL-IN-ONE PLATFORMS** (Replit / Lovable / v0): the accounts inventory often collapses to the platform's own login with built-in teammate + secrets panels — meet the builder there; transfer and secret-sharing use the platform's own mechanisms rather than re-installing equivalents.
- **The packet ROTS.** The `refreshed_on` stamp + two reminders are the **mechanism, not a guarantee** — it only stays true if re-run, and it only helps if it's found and kept fresh.
- **The cold-read proves the tasks tested** (publish-a-change, recover-from-outage); a novel situation gets the contact tree and the catch-all, not a bespoke pre-written answer.
