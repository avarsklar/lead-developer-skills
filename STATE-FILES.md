# STATE-FILES.md — the cross-skill contract

The nine Lead Developer skills talk to each other **only** through durable state files they write into the repo (`stack.md`, `safety-net.md`, `staging.md`, `versions.md`, `qa-harness.md`, `go-live-check.md`, `emergency-plan.md`, `future-releases.md`, `release-foundation.md`, `CHANGELOG.md`, `handoff.md`, plus the derived PDFs). Every one of those handshakes is a promise: *skill A writes token X, skill B reads it.* When a promise is one-sided — A writes X but nobody reads it, or B claims to read X but A never writes it — a non-technical builder who was told "this happens automatically" gets a silent broken promise. That is the single most common defect class in this kit (it's what the 2026-07-01 adversarial review found again and again).

**This file + [`state-files.json`](state-files.json) + [`check_handshakes.py`](check_handshakes.py) turn that contract from prose into something enforced.** `state-files.json` is the machine-readable manifest (the source of truth for the linter); this file is the human explanation; the linter fails the build if any handshake is broken or has drifted.

## How to run the check

```bash
cd skills/
python3 check_handshakes.py     # exit 0 = clean, 1 = a broken handshake
```

Wire it as a pre-commit hook or a build step. Run it after editing any skill that reads or writes a state file. A green run means: every token has a writer and a reader (or is a declared, reasoned exception), every declared writer/reader actually mentions the token, and every dual-owner seam has a named first-owner. A grep of a token against its declared consumers is exactly what would have caught the `regression-wanted` dead loop and the orphan tripwires the instant they were introduced.

## What the linter enforces

1. **Every token has ≥1 writer.** A read with no writer is a phantom input.
2. **Every token has ≥1 reader** — unless it's on the **intentional write-no-read allowlist** (below), each with a stated reason.
3. **No drift:** every declared writer *and* reader must literally mention the token in its `SKILL.md`. Edit a skill to drop a token another skill still depends on, and the linter goes red.
4. **Every dual-owner seam names a `first_owner`** that is one of its owners.

## State-file catalog (who owns each)

| File | First owner | Written by | Read by |
|---|---|---|---|
| `stack.md` | `/readiness-check` | readiness-check (+ safety-net fallback) | everyone |
| `readiness-check.md` | `/readiness-check` | readiness-check | most skills (gate + tailoring) |
| `safety-net.md` (+ `## Still open`) | `/safety-net` | safety-net | everyone downstream |
| `restore-test.md` | `/safety-net` | safety-net | readiness-check, go-live-check, emergency-plan, handoff |
| `staging.md` (`local_sandbox`, `must_not_break_list`, …) | `/ship-change` | ship-change (+ qa-harness appends the list) | qa-harness, go-live-check, emergency-plan, release, release-foundation |
| `versions.md` | `/ship-change` | ship-change (+ release notes regressions) | qa-harness, release-foundation, release, handoff |
| `qa-harness.md` | `/qa-harness` | qa-harness | ship-change, go-live-check, emergency-plan, release, release-foundation, handoff |
| `go-live-check.md` | `/go-live-check` | go-live-check (+ emergency-plan writes back the alarm) | emergency-plan, qa-harness |
| `emergency-plan.md` (+ `the-break-glass-card.pdf`) | `/emergency-plan` | emergency-plan | qa-harness (regression intake), handoff |
| `future-releases.md` | `/release-foundation` | release-foundation, ship-change (parked rows), release | readiness-check, release, release-foundation |
| `release-foundation.md` | `/release-foundation` | release-foundation | release, release-foundation |
| `CHANGELOG.md` | `/release-foundation` | release-foundation (creates), release (appends) | handoff |
| `handoff.md` (+ `handoff-packet.pdf`) | `/handoff` | handoff | (terminal — capstone) |

## Cross-skill tokens (the enforced handshakes)

The full list with exact spellings, writers, and readers is in [`state-files.json`](state-files.json). The load-bearing ones:

- **`canonical_repo` / `canonical_remote`** — the stale-clone guard. Every skill locks onto the live copy first. First owner: readiness-check; all carry a write-if-missing fallback.
- **`deployed_branch`** *(added 2026-07-02, M2)* — which branch is production (not assumed `main`). readiness-check writes; ship-change + release publish to it.
- **`regression-wanted` → `regression-covered`** *(fixed 2026-07-02, H2 + B16)* — the incident→test loop. emergency-plan, release, and go-live-check write `regression-wanted:` lines; qa-harness's Step 0.4 intake reads them, builds the check, and flips them to `regression-covered:`. This was the dead loop the review found.
- **`part-2-due` / `next-review-due` / `next check due`** *(fixed 2026-07-02, H3)* — the rot tripwires. emergency-plan and go-live-check write them; readiness-check (warm re-run) and ship-change (step zero) surface them when stale.
- **`password manager`** *(added 2026-07-02, H1)* — safety-net sets it up; handoff assembles against it.
- **`## Still open` ledger** — safety-net's dated deferral list; re-surfaced by every downstream skill.
- **`local_sandbox` / `must-not-break` list / `restore-test.md` / `qa-harness.md` / `the-break-glass-card.pdf`** — the proof artifacts each gate leaves for the next.

## Dual-owner seams — the first-owner table

Some concepts are legitimately touched by more than one skill. Each needs a single **first owner** so ownership is never ambiguous:

| Concept | Owners | **First owner** | Rule |
|---|---|---|---|
| `CHANGELOG.md` creation | release-foundation, release | **release-foundation** | foundation creates; release appends; either adopts-not-clobbers an existing one. |
| `must_not_break_list` | ship-change, qa-harness, go-live-check | **ship-change** | single source of truth; qa-harness appends; go-live-check's fallback-capture must write back, not diverge (B12). |
| the down-alarm / uptime alert | go-live-check, emergency-plan | **go-live-check** | go-live-check owns/wires it; emergency-plan Part-2c checks `go-live-check.md` first and never duplicates. |
| the in-app banner | emergency-plan, ship-change | **emergency-plan** | emergency-plan authors it; it ships via ship-change's loop (which advances the restore point). |
| the checkout / money-path proof | go-live-check, qa-harness | **go-live-check** | go-live-check proves it once, now; qa-harness makes it permanent; a FAIL seeds a qa-harness test (B16). |
| `future-releases.md` chart | release-foundation, ship-change, release | **release-foundation** | foundation creates; ship-change adds parked rows; release marks shipped / rolls dates. |
| `stack.md` ownership | readiness-check, safety-net | **readiness-check** | readiness-check owns it; safety-net writes only as a front-door-skipped fallback. |

## Intentional write-no-read (allowlisted, with reasons)

These are written with no *sibling-skill* reader — on purpose. They are **not** broken handshakes:

- **The `CLAUDE.md` standing rules** (never-hardcode-secrets from safety-net; the release sorter from release-foundation; the Fire-mode leash from emergency-plan; the every-change-through-the-loop rule from ship-change) — their reader is the builder's **ambient AI, every session**, not another skill.
- **`handoff.md` clean-break record** and **`handoff-packet.pdf`** — terminal capstone deliverables (end of the road).
- **`safety-net.md` size trip-wire** and **`qa-harness.md` test-key option** — builder-facing future-task notes.
- **`staging.md` `data_fill`** — a human-facing record; qa-harness re-derives realistic state from `stack.md`'s operating mode (B4).

If you add a token, add it to `state-files.json` (and here). If it's deliberately reader-less, add it to `intentional_write_no_read` with a reason — that keeps the allowlist honest instead of a dumping ground.
