# FFCRAFT — Free Fire Craftland Research & Coding Field Manual

A source-backed knowledge base for **Free Fire Craftland**, with a focus on visual block logic, Craftland Studio PC code scripts, events, player systems, persistent storage, UI, gameplay mechanics, debugging, and version changes.

> Research snapshot: **21 October 2026**. This repository is an independent creator reference, not an official Garena product. Official documentation and the installed editor take precedence over anything written here.

## Start here

1. [Research method and confidence labels](docs/00-research-method.md)
2. [Platform map and core concepts](docs/01-platform-and-fundamentals.md)
3. [Block scripting](docs/02-block-scripting.md)
4. [Code scripting: .fcg and .fcc](docs/03-code-scripting.md)
5. [Events, entities, and server/client runtime](docs/04-events-and-runtime.md)
6. [Player roster and sequential join serials](docs/05-player-roster-join-serials.md)
7. [Data storage, persistence, and rankings](docs/06-data-storage.md)
8. [Gameplay patterns, UI, assets, and audio](docs/07-gameplay-ui-audio.md)
9. [Debugging, performance, and version watch](docs/08-debugging-performance-versions.md)
10. [Reusable logic recipes](docs/09-recipes.md)
11. [API/module discovery map](docs/10-api-reference-map.md)
12. [Community resources and how to vet them](docs/11-community-resources.md)
13. [User-observed block inventory](docs/12-user-observed-block-inventory.md) — searchable draft extracted from Rahul's original `Rough.txt`; unverified entries are explicitly labelled.
14. [Source catalogue](docs/SOURCES.md)
15. [Machine-readable block inventory](research/user-observed-block-inventory.json)
16. [Machine-readable research index](research/research-index.json) — structured source map, confirmed findings, platform constraints, and open verification items.
17. [AI Craftland coding workflow](docs/14-ai-craftland-coding-workflow.md) — the repeatable process for translating game ideas into verified block/code implementations.
18. [Viability decision and effort budget](docs/15-viability-decision.md) — what is supported, where FFCRAFT adds value, when an install is needed, and the proof-first next step.
19. [Community resource repository audit](docs/16-community-resource-audit.md) — what is useful in Nexos Studio Resources, what appears stale/sample-based, and how to verify it safely.
20. [Curated asset reference](docs/17-curated-asset-reference.md) — six officially documented skybox base types linked to community package leads, with evidence kept separate.
21. [FE_RESOURCES_BETA audit](docs/18-fe-resources-beta-audit.md) — review of its 68 sample packages for skyboxes, weather, and voting.
22. [First vertical slice: join serial](docs/19-first-vertical-slice-join-serial.md) — separate Mobile/PC implementation plans and explicit unresolved blockers.
23. [PC language-library catalog recovery](docs/20-pc-library-catalog.md) — parsed symbol inventory from 42 public-mirror .fcc libraries, with version/licensing caveats.
24. [Dropdown/enum crosswalk](docs/21-enum-dropdown-reconstruction.md) — maps the 65 labels in Rough.txt to likely library or official definitions and flags the unresolved set.
25. [Current official enum/type supplement](docs/22-current-official-enum-supplement.md) — newer official dropdown types missing from the older mirror, plus dynamic skin/texture ID notes.
26. [Detailed PC API reference](docs/23-pc-api-reference-details.md) — function/event metadata, parameters, deprecations, server/client annotations, and component-property declarations extracted from all 42 mirrored libraries.
27. [Rough block-symbol crosswalk](docs/24-block-symbol-crosswalk.md) — compares all 443 extracted lines against the recovered PC API/event/component/property catalog, separating exact matches from fuzzy leads and gaps.
28. [Public tutorial corpus audit](docs/25-public-tutorial-corpus-audit.md) — indexes translated Mobile Block Script and PC code/element-script manuals, official-linked screenshots, and 13 reusable mechanism recipes.
29. [Enum option-set analysis](docs/26-enum-option-set-analysis.md) — identifies 42 repeated option lists across differently named PC enums, while preserving each original type identity.
30. [Current editor capture playbook](docs/27-current-editor-capture-playbook.md) — exact local .fcc path, EditorGenLib and MCP data sources, plus what Mobile screenshots are needed to close the remaining gaps.
31. [Live MCP repository audit](docs/28-live-mcp-repository-audit.md) — audits a new community MCP-export workflow and separates its useful method clues from its unpublished raw catalog.
32. [Official Mobile scripting source map](docs/29-official-mobile-scripting-source-map.md) — maps Garena's current block-scripting topics and worked templates without claiming they form a complete block dump.
33. [Current official dropdown option cross-checks](docs/30-current-official-dropdown-option-crosschecks.md) — 109 official option rows across 25 labels, with old-mirror deprecated-alias discrepancies and exact script names.
34. [Unresolved block review queue](docs/31-rough-block-review-queue.md) — prioritizes 111 approximate/no-match entries from the 443-line rough inventory, with exact source lines and review actions.

## Author-contributed inventory
- [First official cross-check pass](docs/13-official-cross-checks.md) — early verified findings and known conflicts from comparing the rough list with Garena's references.

- [Original `Rough.txt`](Rough.txt) — Rahul's raw, hand-typed editor observations. Preserved as authored; not official or independently verified.
- [Normalized block inventory](docs/12-user-observed-block-inventory.md) — searchable draft grouped by category and subcategory.
- [Machine-readable block inventory](research/user-observed-block-inventory.json) — extracted candidates with source-line references and verification labels.
- [PC library symbol catalog](research/pc-library-symbol-catalog.json) — machine-readable enum/member/function/event/component candidates from the extension mirror.
- [Dropdown/enum crosswalk](research/enum-dropdown-crosswalk.json) — maps Rough.txt labels to recovered library definitions and records verification status.
- [Current official enum/type supplement](research/current-official-enum-supplement.json) — official additions and dynamic ID-type findings missing from the older mirror.
- [Detailed PC API reference](research/pc-library-api-reference.json) — parsed function/event documentation and component properties from all 42 mirrored library files.
- [Block-symbol crosswalk](research/block-symbol-crosswalk.json) — line-by-line comparison of Rough.txt against recovered PC symbols, with exact/fuzzy/unmatched statuses and targeted official matches.
- [Rough block review queue](research/rough-block-review-queue.json) — 111 prioritised lines needing current-editor review or exact candidate verification.
- [Public tutorial manifest](research/public-tutorial-corpus-index.json) — indexes 160 public manual files and key script references.
- [Mobile block recipe index](research/mobile-block-recipe-index.json) — 13 summarized mechanism examples from a re-editable gameplay template.
- [Enum option-set analysis](research/pc-enum-option-set-analysis.json) — groups identical dropdown-like option sequences for efficient browsing without merging API types.
- [Live MCP public-resource audit](research/live-mcp-public-resource-audit.json) — machine-readable audit of a community PC MCP exporter; catalog counts are self-reported and raw records are absent.
- [Official Mobile scripting source map](research/mobile-official-scripting-source-map.json) — structured links to seven official scripting topics and two mechanism templates.
- [Official dropdown option cross-checks](research/official-dropdown-option-crosschecks.json) — 109 current official option rows across 25 rough labels, with old-mirror alias notes.

## Current verified baseline

- Garena's official portal separates **Craftland Mobile** learning content from the more expansive **Craftland Studio PC** manual. They should not be treated as identical authoring environments.
- Craftland supports visual block scripts and code scripts. The official PC guide identifies `.fcg` script files and `.fcc` library files; server and client runtimes have different supported events/APIs and communicate through events rather than calling each other directly.
- Block scripts are event-driven visual logic. Common script scopes include global, party/team, player, object, and UI-related scripts. Available blocks depend on script type/context.
- The latest official patch-note entry found during this review is **Craftland Studio 1.19.0, September 2026**. It includes AI/MCP integration, scripting/debugger improvements, chat and UI capabilities, and additional APIs.
- Official reference pages visibly mark some APIs/events/types obsolete. Do not copy legacy blocks blindly; inspect the installed editor's current library and deprecation labels.
- Storage documentation and individual Data Store API pages describe distinct functionality and may have different platform constraints. Confirm the path actually available in the current editor before relying on storage behavior or quotas.

## Research rules

- Every factual claim should have a source link or be explicitly labelled as a design pattern, hypothesis, or test-needed note.
- Never invent API names. For exact names, parameter types, platform availability, and deprecation status, confirm in the version of Craftland Studio being used.
- Distinguish **documented behavior** from **recommended implementation** and **locally verified behavior**. This repo does not claim the example recipes have been tested in a live Free Fire match.
- Treat player IDs/slots, display names, account UUIDs, custom properties, and persistent records as different concepts; do not use them interchangeably.
- Prefer server-side authority for match state, scoring, roster order, and win-condition decisions; keep client-side code for local UI/input/presentation unless the relevant API documentation says otherwise.

## Scope

This research pass establishes a structured, source-backed baseline and a workflow for deeper API testing. Craftland's API surface is large and version-sensitive; the API index is a discovery map, not a promise that every entry is current, supported on mobile, or available in every script context.

## Main official links

- [Official Craftland portal](https://ffcraftland.garena.com/en/)
- [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/)
- [Craftland Studio PC user manual](https://ffcraftland.garena.com/en/tutorial/fe/1)
- [Craftland beginner tutorial and wiki index](https://ffcraftland.garena.com/en/tutorial/cl/3)
- [Official API/event/type reference index](https://ffcraftland.garena.com/en/docs/api-1-26)


