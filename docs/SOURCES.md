# Source catalogue

This index prioritizes official Garena sources. They are grouped by what they are good for. A source can be authoritative and still be version-sensitive or explicitly obsolete; check its current labels and the installed editor.

## Official home and current releases

- [Craftland portal](https://ffcraftland.garena.com/en/) — entry points to mobile and PC tools, tutorials, Asset Store, Creator Center, official community links.
- [Patch notes](https://ffcraftland.garena.com/en/patch-notes/) — release-by-release changes. The latest entry found for this repository snapshot (20 October 2026) is Craftland Studio 1.19.0 from September 2026.
- [Craftland Studio PC User Manual index](https://ffcraftland.garena.com/en/tutorial/fe/1) — recommended sections for overview, scripts, global/player, scene editor, and templates.
- [Mobile Beginner Tutorial index](https://ffcraftland.garena.com/en/tutorial/cl/3) — map creation/publishing, scene editing, game parameters, common objects, economy, monster/spawn setup, block scripts, custom UI.
- [Craftland Wiki index](https://ffcraftland.garena.com/en/tutorial/cl/4) — block, script, mode, and template reference.

## Script authoring and runtime

- [Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101) — editor UI, scopes, script-type toggle, block search, templates, event-to-action logic.
- [Publishing Blocks and HUD UIs](https://ffcraftland.garena.com/en/tutorial/cl/4-100) — packaging/sharing block and HUD templates.
- [Block Classification and Flow Control](https://ffcraftland.garena.com/en/tutorial/cl/4-104) — block types and flow control concepts.
- [Variables and Properties, Assignment](https://ffcraftland.garena.com/en/tutorial/cl/4-105) — variable/property/assignment concepts.
- [Data and Logic Operations](https://ffcraftland.garena.com/en/tutorial/cl/4-106) — data operations and logic blocks.
- [Server-side and client-side scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-107/) — visual scripting side constraints.
- [PC Scripts manual](https://ffcraftland-pre.garena.com/en/tutorial/fe/1-7/) — block vs code scripts, server/client, static scripts.
- [PC Code Scripts](https://ffcraftland.garena.com/en/tutorial/fe/1-9) — `.fcg` scripts, `.fcc` libraries, imports, graph/function/event structure, custom libraries/events, platform labels, and VS Code tooling.
- [API index / standard library](https://ffcraftland.garena.com/en/docs/api-1-26) — API discovery and categories. The page indicates legacy/obsolete entries, so use it as an index and verify individual declarations.
- [Event index](https://ffcraftland.garena.com/en/docs/type-11/) — event name/description table, including lifecycle and combat events and deprecated entries.
- [On Player Join event](https://ffcraftland.garena.com/en/docs/event-11-14) — event meaning, owner, and platform/runtime labels.

## Selected current PC Data Store API references

- [Write To Data Store V2](https://ffcraftland.garena.com/en/docs/api-31-1017) — page labels it Server Side and Only PC.
- [Steady Read From Data Store](https://ffcraftland.garena.com/en/docs/api-31-1006) — page labels it Server Side and Only PC.
- [Read From Data Store By Column](https://ffcraftland.garena.com/en/docs/api-31-953) — page labels it Server Side and Only PC.
- [Legacy Write To Data Store](https://ffcraftland.garena.com/en/docs/api-31-802) — marked obsolete.

## Storage and other systems

- [Data Storage manual](https://ffcraftland.garena.com/en/tutorial/fe/1-35) — general/player storage, ranking data, statistics, constraints, batch operations, Data Center inspection, archives.
- [Playable system](https://ffcraftland.garena.com/en/tutorial/fe/1-24) — runtime sound/FX entities and scripting notes.
- [Audio Tracks](https://ffcraftland.garena.com/en/tutorial/cl/4-89) — timeline sound resources/keyframes/volume/speed and overlap note.
- [Sound entity/object guide](https://ffcraftland.garena.com/en/tutorial/cl/3-44) — Auto play and 3D sound settings.
- [Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87) — healing/damage zones, teleport/traps, monster spawners, text, costume changes, doors/elevators, custom HUD.
- [Myconsole template](https://ffcraftland.garena.com/en/tutorial/cl/4-86) — HUD and interaction patterns.
- [Big Head Mode template](https://ffcraftland.garena.com/en/tutorial/cl/4-85) — model-scale and equipment patterns.
- [Game-rule win-condition example](https://ffcraftland-pre.garena.com/en/tutorial/fe/1-51/) — elimination objective and custom event/global check pattern.

## Official creator/community tutorials

- [Creator basics](https://ffcraftland.garena.com/en/community/creator-tutorials:-creator-basics/) — script editor basics, assets, interface/publishing, known editor issues, and feature updates.
- [Gameplay systems](https://ffcraftland.garena.com/en/community/creator-tutorials:-gameplay-systems/) — rounds, triggers, revive buttons, player transformation, mic-related scripts, headshot-only maps.
- [Custom features](https://ffcraftland.garena.com/en/community/creator-tutorials:-custom-features/) — custom menus, cinematic scenes, two-player puzzle map, HUD, object movement, banner scripts.
- [Official Discord entry point](https://ffcraftland.garena.com/en/) — the official homepage recommends the Craftland Global Discord for connection with creators and the Craftland team. Use that for discoveries, then preserve the original post/date/version and verify claims.

## Community-maintained GitHub resources (secondary evidence)

- [FF-OGC/Craftland-Tutorial](https://github.com/FF-OGC/Craftland-Tutorial) — a browsable Markdown mirror/organization of Craftland manuals, including the code-script user manual. Handy for offline reading/search; verify content against the official current site/editor.
- [nexosstudio/CRAFTLAND_STUDIO_RESOURCES](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES) — community resource repository describing a directory of assets, docs, scripts, templates, and tools. Its README declares CC0-1.0; still inspect each item's provenance and the repo's current license/files before reusing assets or code.

These GitHub sources were discovered and inspected as leads. No arbitrary third-party code from them has been copied into FFCRAFT or treated as tested official behavior.

## How to cite/record a future discovery

When adding a new technique, record:

- Original URL and author/source type.
- Publication or observation date.
- Craftland Studio/client/editor version and region if known.
- Mobile vs PC; server vs client; script scope.
- Exact block/API/type/event names, copied from the current editor reference.
- Minimal reproduction and expected/observed result.
- Whether the finding is official, community-reported, locally reproduced, or still unverified.

## Link and version notes

Some links point to the official pre-release host because that host exposes a more detailed PC-manual page for a specific topic. It is still a Garena-hosted source, but any pre-release/live discrepancy must be resolved against the installed release. Official API pages may retain old entries and explicitly label obsolete elements. Do not conclude an API is current merely because its page still exists.
