# FFCRAFT — Free Fire Craftland Research & Coding Field Manual

A source-backed knowledge base for **Free Fire Craftland**, with a focus on visual block logic, Craftland Studio PC code scripts, events, player systems, persistent storage, UI, gameplay mechanics, debugging, and version changes.

> Research snapshot: **20 October 2026**. This repository is an independent creator reference, not an official Garena product. Official documentation and the installed editor take precedence over anything written here.

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
11. [Source catalogue](docs/SOURCES.md)

## Current verified baseline

- Garena's official portal separates **Craftland Mobile** learning content from the more expansive **Craftland Studio PC** manual. They should not be treated as identical authoring environments.
- Craftland supports both visual block scripts and code scripts. The official PC code-scripting guide identifies `.fcg` script files and `.fcc` library files; server and client runtimes have different supported events/APIs and communicate through events rather than calling each other directly.
- Block scripts are event-driven visual logic. Common script scopes include global, party/team, player, object, and UI-related scripts. The available blocks depend on the script type/context.
- The latest official patch-note entry found during this review is **Craftland Studio 1.19.0, September 2026**. It includes editor AI/MCP workflow integration and scripting/debugger improvements.
- Official reference pages visibly mark some APIs/events/types obsolete. Do not copy legacy blocks blindly; inspect the installed editor's current library and deprecation labels.
- The official Data Storage guide documents limits and caveats. Those limits are recorded in the storage guide with a warning to re-check them against the live editor before publishing.

## Research rules

- Every factual claim should have a source link or be explicitly labelled as a design pattern, hypothesis, or test-needed note.
- Never invent API names. For exact names, parameter types, platform availability, and deprecation status, confirm in the version of Craftland Studio being used.
- Distinguish **documented behavior** from **recommended implementation** and **locally verified behavior**. This repo has not claimed that the example recipes have been tested in a live Free Fire match.
- Treat player IDs/slots, display names, account UUIDs, custom properties, and persistent records as different concepts; do not use them interchangeably.
- Prefer server-side authority for match state, scoring, roster order, and win-condition decisions; keep client-side code for local UI/input/presentation unless the relevant API documentation says otherwise.

## Scope

This first research pass establishes a documented baseline and reliable routes into the official references. The Craftland API is large and version-sensitive; the API index is a discovery map, not a promise that every listed entry is current, supported on mobile, or available in every script context.

## Main official links

- [Official Craftland portal](https://ffcraftland.garena.com/en/)
- [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/)
- [Craftland Studio PC user manual](https://ffcraftland.garena.com/en/tutorial/fe/1)
- [Craftland beginner tutorial and wiki index](https://ffcraftland.garena.com/en/tutorial/cl/3)
- [Official API/event/type reference index](https://ffcraftland.garena.com/en/docs/api-1-26)
