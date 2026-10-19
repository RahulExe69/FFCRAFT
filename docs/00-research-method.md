# Research method, scope, and evidence labels

**Checked:** 20 October 2026. **Purpose:** provide a durable starting point for future Craftland coding work without silently turning guesses into facts.

## Evidence hierarchy

1. **Tier A — official live editor and current installed `.fcc` libraries.** Best authority for whether a block/API exists in the build being used, its exact signature, target platform, and deprecation status. The local library can be opened from code references in Craftland Studio PC; official documentation explains Ctrl-click navigation to the library.
2. **Tier B — official Craftland website documentation and patch notes.** Primary source for conceptual behavior, supported workflows, event descriptions, limits, and version changes. Some pages are old or explicitly marked obsolete, so check their dates/context.
3. **Tier C — official Garena-hosted creator tutorials and reusable templates.** Strong practical examples, especially for custom triggers, HUDs, combat rules, and common modes, but they may describe a previous editor build.
4. **Tier D — community posts, videos, Discord discussions, and third-party projects.** Useful for discovering techniques and bugs; treat as hypotheses until a current editor test or an official reference confirms them.
5. **Tier E — this repository's recipes.** They are implementation designs and checklists, not proof that an exact block name/signature is valid.

## What was searched

- Official Craftland landing page, mobile beginner tutorial/wiki, Craftland Studio PC manual, block-script tutorials, code-script manual, API/event/type index, data-storage guide, audio/entity guides, creator tutorials, preset gameplay-template guides, and patch notes.
- Current official patch notes were checked for the latest published Craftland Studio version and recent scripting changes.
- The user's FFCRAFT repository was inspected before writing; it initially contained only a minimal README, so a documentation-first structure was appropriate.

## Key distinction: two authoring surfaces

**Craftland Mobile** is the in-game creation experience for making and playing custom maps. **Craftland Studio PC** documents a broader toolchain including visual logic, flexible code scripts, custom libraries, scene/UI/resource workflows, data storage, and debugging. A feature found in a PC-only API reference must not be presented as guaranteed to work in the mobile editor/client.

## Confidence labels used in this repository

- **Documented:** explicitly supported by an official source linked in the same section.
- **Version-sensitive:** documentation exists, but the exact build or current editor availability must be checked.
- **Recommended pattern:** a robust design inferred from documented primitives; still needs a live test.
- **Test needed:** ordering, concurrency, API signatures, persistence, replication, or cross-platform behavior has not been verified here.
- **Obsolete:** official reference marks it deprecated/obsolete; avoid unless needed for maintaining old content and no replacement is available.

## Research caveats

- The site contains legacy/obsolete reference pages and APIs. The API index is intentionally not copied wholesale as a current API catalogue.
- Official Data Storage limitations may have evolved. Use the limits in `06-data-storage.md` as the published-documentation baseline and confirm against the installed version.
- No live Craftland Studio session or game match was run in this research pass. The recipes in this repository are carefully specified designs, not claimed successful builds.
- There is no reliable guarantee that every public third-party tutorial matches the current region/build/editor version. Capture the game/editor version when reporting an issue.

## Research follow-ups

1. Export or inspect the installed release's current standard `.fcc` files and create a version-stamped API/event catalogue.
2. Implement the recipes in a throwaway test map, record exact blocks/API signatures and expected vs observed results.
3. Test server/client replication, reconnect behavior, match reset behavior, simultaneous joins, and mobile-vs-PC differences separately.
4. Add community discoveries only with the original source, date, version, reproducible steps, and an evidence label.
