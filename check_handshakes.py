#!/usr/bin/env python3
"""
check_handshakes.py — the handshake linter for the Lead Developer skills.

Reads state-files.json (the authoritative cross-skill token manifest) and asserts,
against the ACTUAL SKILL.md files, that every declared handshake is real:

  1. Every token has at least one writer.
  2. Every token has at least one reader, UNLESS it's on the intentional
     write-no-read allowlist (with a stated reason).
  3. Every declared writer AND reader actually mentions the token (its `grep`
     string) in its SKILL.md — catches drift the instant a skill is edited to
     drop a token another skill still depends on. THIS is what would have caught
     the H2 dead-loop and the H3 orphan tripwires automatically.
  4. Every dual-owner seam names a first_owner, and that owner is one of the owners.

Run:  python3 check_handshakes.py         (from the skills/ directory)
Exit: 0 = clean, 1 = one or more violations.

This is the "handshake linter" from the 2026-07-01 adversarial review's structural
fixes. Wire it as a pre-commit hook or a build step. Keep state-files.json and
STATE-FILES.md in sync when you add or change a cross-skill token.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "state-files.json")


def skill_path(name):
    return os.path.join(HERE, name, "SKILL.md")


def load_skill_text(name, cache):
    if name not in cache:
        p = skill_path(name)
        if not os.path.exists(p):
            cache[name] = None
        else:
            with open(p, "r", encoding="utf-8") as f:
                cache[name] = f.read()
    return cache[name]


def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        m = json.load(f)

    errors = []
    warnings = []
    cache = {}

    known_skills = set(m.get("skills", []))
    allowlist_ids = {e["id"] for e in m.get("intentional_write_no_read", [])}

    # Sanity: every declared skill file exists.
    for s in known_skills:
        if load_skill_text(s, cache) is None:
            errors.append(f"[missing-file] declared skill '{s}' has no SKILL.md at {skill_path(s)}")

    # ---- tokens ----
    for tok in m.get("tokens", []):
        tid = tok["id"]
        grep = tok["grep"]
        writers = tok.get("writers", [])
        readers = tok.get("readers", [])

        if not writers:
            errors.append(f"[no-writer] token '{tid}' has no writer.")
        if not readers and tid not in allowlist_ids:
            errors.append(
                f"[no-reader] token '{tid}' is written but never read, "
                f"and is not on the intentional write-no-read allowlist."
            )

        # Drift check: every declared writer/reader must actually mention the token.
        for role, skills in (("writer", writers), ("reader", readers)):
            for s in skills:
                if s not in known_skills:
                    errors.append(f"[unknown-skill] token '{tid}' names {role} '{s}' which is not a known skill.")
                    continue
                text = load_skill_text(s, cache)
                if text is None:
                    continue
                if grep not in text:
                    errors.append(
                        f"[drift] token '{tid}': declared {role} '{s}' does not mention "
                        f"'{grep}' in its SKILL.md — the handshake is broken or the manifest is stale."
                    )

    # ---- pre-flight invariants (PREFLIGHT.md) ----
    # Every skill must carry the load-bearing "lock onto the live copy" guard; a copy
    # can't silently weaken. See PREFLIGHT.md for the canonical block.
    preflight_invariants = [
        ("lock-header", "Lock onto the real"),
        ("canonical_repo", "canonical_repo"),
        ("behind-remote-STOP", "behind the remote"),
    ]
    for s in known_skills:
        text = load_skill_text(s, cache)
        if text is None:
            continue
        for label, needle in preflight_invariants:
            if needle.lower() not in text.lower():
                errors.append(
                    f"[preflight] skill '{s}' is missing the pre-flight invariant "
                    f"'{label}' (expected phrase: \"{needle}\") — see PREFLIGHT.md."
                )

    # ---- seams ----
    for seam in m.get("seams", []):
        concept = seam["concept"]
        owners = seam.get("owners", [])
        first = seam.get("first_owner")
        if not first:
            errors.append(f"[no-first-owner] seam '{concept}' (owners {owners}) has no first_owner.")
        elif first not in owners:
            errors.append(f"[bad-first-owner] seam '{concept}': first_owner '{first}' is not in owners {owners}.")

    # ---- report ----
    print("Lead Developer handshake linter")
    print(f"  manifest: {MANIFEST}")
    print(f"  tokens checked: {len(m.get('tokens', []))}   seams: {len(m.get('seams', []))}   "
          f"allowlisted write-no-read: {len(allowlist_ids)}   preflight-guarded skills: {len(known_skills)}")
    print()

    for w in warnings:
        print("  WARN  " + w)
    for e in errors:
        print("  FAIL  " + e)

    if errors:
        print(f"\n{len(errors)} violation(s). Handshake graph is NOT clean.")
        return 1
    print("All handshakes symmetric and drift-free. ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
