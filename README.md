# FFCRAFT — Craftland Mobile Map-Making & Scripting Knowledge Base

FFCRAFT is a creator-first, source-backed knowledge base for **building maps and gameplay in Free Fire Craftland Mobile**, with supporting research for visual-block logic and Craftland Studio PC code.

The long-term goal is practical: describe a map or mechanic in ordinary language, then use documented editor workflows, exact blocks, verified APIs, asset references, and repeatable tests to turn the idea into a buildable plan. This is not an official Garena product.

> **Research snapshot:** 21 October 2026. The installed editor and current official documentation take precedence over old mirrors or unverified notes.

## Start here

- **[Project vision & Mobile map-making roadmap](docs/00-project-vision-and-map-making-roadmap.md)** — what FFCRAFT is meant to achieve, how the assistant should learn from editor evidence, and the next milestone.
- **[Research method & confidence labels](docs/00-research-method.md)** — how findings are sourced and what “verified” means.
- **[Platform map & fundamentals](docs/01-platform-and-fundamentals.md)** — Mobile vs. Studio PC and core concepts.
- **[AI implementation workflow](docs/14-ai-craftland-coding-workflow.md)** — turn a natural-language idea into an implementation with setup and tests.
- **[Viability decision & effort budget](docs/15-viability-decision.md)** — project scope, what is already proven, and where to spend effort next.

## Find information by task

### I want to build a map

The Mobile map-making playbooks are the next major content milestone. Until they are captured from the real editor, use the vision document as the workflow plan and the guides below as supporting references.

- **Custom environment:** layout, terrain, buildings, props, landmarks, routes, and visual composition.
- **Combat/arena map:** spawns, cover, sightlines, rounds, boundaries, and scoring.
- **Minigame:** parkour, race, puzzle, checkpoints, timers, and reset flows.
- **Interactive map:** triggers, object interactions, buttons, UI feedback, and event-driven mechanics.
- **Advanced mechanics:** state, player/team tracking, and complex win conditions.

These are map-design categories, not promises that every tool is available in every editor version.

### I want to build gameplay logic

- [Block scripting](docs/02-block-scripting.md)
- [Events, entities & runtime](docs/04-events-and-runtime.md)
- [Gameplay patterns, UI & audio](docs/07-gameplay-ui-audio.md)
- [Reusable logic recipes](docs/09-recipes.md)
- [Player roster & join serials](docs/05-player-roster-join-serials.md)
- [Data storage, persistence & rankings](docs/06-data-storage.md)
- [Debugging, performance & version checks](docs/08-debugging-performance-versions.md)

### I want to write or verify Studio PC code

- [Code scripting: .fcg and .fcc](docs/03-code-scripting.md)
- [API/module discovery map](docs/10-api-reference-map.md)
- [PC library catalog](docs/20-pc-library-catalog.md)
- [Detailed PC API reference](docs/23-pc-api-reference-details.md)
- [Current editor metadata capture playbook](docs/27-current-editor-capture-playbook.md)

**Important:** PC code declarations do not automatically prove that an equivalent Mobile visual block or dropdown exists.

### I need exact block names, dropdowns, or unresolved candidates

- [Human-readable user-observed block inventory](docs/12-user-observed-block-inventory.md)
- [Official cross-checks](docs/13-official-cross-checks.md)
- [Rough block-symbol crosswalk](docs/24-block-symbol-crosswalk.md)
- [Dropdown/enum reconstruction](docs/21-enum-dropdown-reconstruction.md)
- [Current official enum/type supplement](docs/22-current-official-enum-supplement.md)
- [Current official dropdown option cross-checks](docs/30-current-official-dropdown-option-crosschecks.md)
- [Unresolved block review queue](docs/31-rough-block-review-queue.md)
- [Official Mobile scripting source map](docs/29-official-mobile-scripting-source-map.md)

## Research reports

- [Community resources and vetting](docs/11-community-resources.md)
- [Community resource repository audit](docs/16-community-resource-audit.md)
- [Curated asset reference](docs/17-curated-asset-reference.md)
- [FE_RESOURCES_BETA audit](docs/18-fe-resources-beta-audit.md)
- [First vertical slice: join serial](docs/19-first-vertical-slice-join-serial.md)
- [Public tutorial corpus audit](docs/25-public-tutorial-corpus-audit.md)
- [Enum option-set analysis](docs/26-enum-option-set-analysis.md)
- [Live MCP repository audit](docs/28-live-mcp-repository-audit.md)
- [Legacy BuiltinSymbol index audit](docs/32-legacy-builtin-symbol-index-audit.md)
- [Public script repository audit](docs/33-public-script-repository-audit.md)
- [Source catalogue](docs/SOURCES.md)

## Machine-readable research

JSON datasets are useful for searching, cross-referencing, and future automation, but are not intended to replace the human-readable guides.

Start with the **[research data directory guide](research/README.md)** for a table explaining which JSON file to use for each question. The main datasets include:

- [Research index](research/research-index.json)
- [User-observed block inventory](research/user-observed-block-inventory.json)
- [Block-symbol crosswalk](research/block-symbol-crosswalk.json)
- [PC library symbol catalog](research/pc-library-symbol-catalog.json)
- [PC API reference](research/pc-library-api-reference.json)
- [Enum/dropdown crosswalk](research/enum-dropdown-crosswalk.json)
- [Official dropdown option cross-checks](research/official-dropdown-option-crosschecks.json)
- [Unresolved block review queue](research/rough-block-review-queue.json)
- [Mobile block recipe index](research/mobile-block-recipe-index.json)
- [Mobile official scripting source map](research/mobile-official-scripting-source-map.json)

The complete file-by-file index is in [research/README.md](research/README.md).

## Original notes and preservation rule

- **[Original `Rough.txt`](Rough.txt)** is the creator's raw, hand-typed editor inventory. It is preserved unchanged.
- Derived inventories, corrected spellings, official mappings, candidate matches, and verification notes belong in separate files.
- Do not remove an obscure, duplicated, old, ambiguous, or unverified entry just to make the catalogue look cleaner. Keep the entry and make its evidence status clear.

## Research and implementation rules

1. **Never invent identifiers.** Exact names, parameters, dropdown values, asset IDs, and editor controls need evidence.
2. **Keep Mobile and PC distinct.** Similar labels do not establish identical behavior or availability.
3. **Separate evidence levels.** A candidate match is not editor-verified; a documented API is not compiled; compiled code is not playtested.
4. **Keep sources attached.** Record official URLs, community provenance, checked date, and editor version where available.
5. **Explain the whole implementation.** Include script context, block wiring or code, dependencies, setup, reset/edge cases, and validation.
6. **Make docs creator-friendly.** Lead with the task and steps, then link deeper reference data for people who need it.

## Official starting points

- [Official Craftland portal](https://ffcraftland.garena.com/en/)
- [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/)
- [Craftland Studio PC manual](https://ffcraftland.garena.com/en/tutorial/fe/1)
- [Craftland beginner tutorial and wiki index](https://ffcraftland.garena.com/en/tutorial/cl/3)
- [Official API/event/type reference](https://ffcraftland.garena.com/en/docs/api-1-26)

## Current research baseline

The repository contains a substantial PC API/library and enum research base, a derived inventory from `Rough.txt`, official Mobile tutorial mappings, recipe indexes, resource audits, and an unresolved editor-review queue. It is **not yet a complete current Mobile editor manual**. Exact Mobile controls, block sockets, dropdown values, and map-building workflows should be captured from the editor and documented before being treated as confirmed.

The next milestone is creator-first: capture real Mobile editor workflows, write map-building playbooks, and verify one complete map mechanic end to end.
