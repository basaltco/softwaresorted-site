# AGENTS.md — read this before writing anything into this repository

**This repo is output, not source of truth.** The standards governing every page here live in the
sibling **`../venture-os`** repo. Applies to every tool and session equally — Claude Code,
Antigravity, Gemini, Cursor, Copilot, any other agent, or a human. "I was only asked to write one
page" is not an exemption.

## Before creating or editing any page

1. `../venture-os/AGENTS.md`, in full — the canonical framework (`CLAUDE.md` and `GEMINI.md`
   there are thin pointers to it, not separate rulesets)
2. `../venture-os/principles.md` — 7 non-negotiable principles
3. `../venture-os/ventures/softwaresorted/` — `config.json`, `context.md`, `voice-guide.md`,
   `visual-standards.md`, `learnings.md` (whichever exist)
4. The relevant cluster research file in `../venture-os/ventures/softwaresorted/`

If you cannot access those files, **stop and say so.** Do not infer the standards by copying a
neighbouring page — cloning the template is the easy half and proves nothing about the content.

## Hard requirement for any NEW page

No new `src/**/*.html` may be committed unless the venture's research file already contains, for
that page: the target keyword and a real demand signal plus a SERP note; a source for every
factual claim (vendor docs, help centre, regulator, named review platform — recollection is not a
source); and a verification date. Missing or partial → **stop and flag it, do not commit.**

## Site-specific basics (full set in venture-os)

- British English (UK), GBP pricing
- Mobile-first at the 680px breakpoint, JSON-LD schema, footer disclosure where affiliate links exist
- Design tokens are fixed in `visual-standards.md` — do not improvise colours, fonts, or components

## Why this file exists

On 2026-08-13 a page was generated into a sibling site repo by a tool that had read none of the
above. It cloned the template near-perfectly and read fluently — and was factually inverted on
every vendor it covered, with invented figures and no research trail. The polish is what made it
dangerous.
