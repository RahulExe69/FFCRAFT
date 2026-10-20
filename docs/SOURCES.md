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


## Community asset/resource repositories

- [nexosstudio / CRAFTLAND_STUDIO_RESOURCES](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES) — community-curated asset IDs/names, sound lists, skybox names, UGC rigs, project-template folders, and tooling links. Last observed commit: 29 September 2025. Treat catalogues as discovery leads; some entries are explicitly sample data and the linked Studio installer is older than the current release snapshot. See [FFCRAFT audit](16-community-resource-audit.md).


## Community sample packages and curated assets

- [nexosstudio / FE_RESOURCES_BETA](https://github.com/nexosstudio/FE_RESOURCES_BETA) — community package samples for named/numbered skyboxes, dynamic weather, and a voting system. Latest observed commit: 7 March 2026. Packages are untested until imported into the matching editor. See [audit](18-fe-resources-beta-audit.md).
- [Curated skybox base types](17-curated-asset-reference.md) — six SkyboxType identifiers cross-checked against Garena's public enum reference, with untested community package links clearly separated from enum evidence.


## Recovered language-library and dropdown research

- [Official enum reference](https://ffcraftland.garena.com/en/docs/enum/) — current enum definitions, values, names, and deprecation labels; some selectors represent dynamic type/asset IDs rather than short fixed enums.
- [Official Type reference](https://ffcraftland.garena.com/en/docs/type) — current type system including skin IDs and asset/resource ID families.
- [Official Level Object module](https://ffcraftland.garena.com/en/docs/module-26) — exposes Level Object Type, Weapon Skin Type, Vehicle Skin Type, Outfit Skin Type, Backpack Skin Type, and Object Texture.
- [Official Get Render Quality API](https://ffcraftland.garena.com/en/docs/api-40-940) — current enum/API cross-check; page labels it Client Side and Both Mobile and PC.
- [Official Free Fire Craftland Code VS Code extension](https://marketplace.visualstudio.com/items?itemName=craftLandstudio.ffugclanguage) — official listing for the language tooling, IntelliSense/signature help and compiler workflow.
- [Public mirror of the extension's 1.5.0 library folder](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0/tree/main/library/release) — 42 text `.fcc` files used only as a discovery snapshot. It is older than Studio 1.19.0, and its `LICENSE.md` is empty; FFCRAFT stores a derivative symbol index and provenance hashes, not the raw libraries or executable binaries. See [PC catalog recovery](20-pc-library-catalog.md).
- [Machine-readable PC symbol catalog](../research/pc-library-symbol-catalog.json) — 144 parsed enum declarations, 2,274 member entries, and API/event/component candidates from the mirror; aliases and duplicate legacy definitions are included.
- [Dropdown/enum crosswalk](../research/enum-dropdown-crosswalk.json) — maps the 65 dropdown/type labels in `Rough.txt` to source candidates and flags gaps.
- [Current official enum/type supplement](../research/current-official-enum-supplement.json) — captures current official types/options spotted outside the old mirror.

The mirrored library is not treated as authoritative for current API support. A definition's presence there does not prove current availability or Mobile block parity; absence there does not prove that an enum/API is absent from the current official docs/editor.

- [Detailed PC API/event/component reference](../research/pc-library-api-reference.json) — extracted declarations and documentation fields from the full 42-file mirrored library set; includes parser caveats and 1.17+ compatibility warning in [doc 23](23-pc-api-reference-details.md).

- [Rough block-symbol crosswalk](../research/block-symbol-crosswalk.json) — line-level comparison of 443 extracted notes against functions, events, component names and candidate properties in the mirrored PC libraries.
- [Crosswalk methodology and results](24-block-symbol-crosswalk.md) — explains exact matches, fuzzy candidate status, and why editor-native blocks need separate verification.

- [Enum option-set analysis](../research/pc-enum-option-set-analysis.json) — identifies 42 identical ordered option sets shared by differently named enum types in the old mirror; preserves original type names and source context.
- [Enum option-set analysis notes](26-enum-option-set-analysis.md) — explains how to reduce duplicate browsing without declaring semantically different types interchangeable.


- [Current editor capture playbook](27-current-editor-capture-playbook.md) — current installed .fcc library path, project-generated EditorGenLib.fcc, Studio MCP server and Mobile screenshot evidence collection.
- [Editor metadata capture checklist](../research/editor-metadata-capture-checklist.json) — structured list of authoritative PC and Mobile sources that have not yet been captured.


## Current Mobile scripting and MCP metadata leads

- [Official Mobile Block Scripts guide](https://ffcraftland.garena.com/en/tutorial/cl/4-101) — documents the block editor, script context, search and typed connections; search can include blocks unavailable in the selected script.
- [Official Mobile scripting source map](29-official-mobile-scripting-source-map.md) and [machine-readable map](../research/mobile-official-scripting-source-map.json) — topic links for event/script types, classification/flow control, variables/properties, data/logic and server/client scripting.
- [Current official dropdown option cross-checks](30-current-official-dropdown-option-crosschecks.md) and [machine-readable option rows](../research/official-dropdown-option-crosschecks.json) — 109 published choices across 25 rough labels, comparing current official tables with old-mirror aliases.
- [Official Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87) and [Myconsole template](https://ffcraftland.garena.com/en/tutorial/cl/4-86) — source examples for trigger, player, object, HUD and helper-function patterns.
- [NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL) — recent community MCP-based KB-generation method. Its current public tree contains the README and generator/enrichment scripts but not the generated raw metadata or catalog pages; see [audit](28-live-mcp-repository-audit.md) and [machine-readable audit](../research/live-mcp-public-resource-audit.json). Advertised counts are not treated as verified data.


## Current MCP and Mobile scripting source audit

- [Live MCP repository audit](28-live-mcp-repository-audit.md) — audits the public NiteshCraftFF MCP-derived knowledge-base lead. Its README claims large block/API counts, but the inspected public commit contains only generator scripts and no raw export/catalog pages; counts remain unverified.
- [Official Mobile scripting source map](29-official-mobile-scripting-source-map.md) — official topic pages for Mobile block scripting, script types, flow control, variable/property assignment, data/logic, and server/client separation, plus two official template leads.
- [Machine-readable MCP lead audit](../research/live-mcp-public-resource-audit.json) and [Mobile source map](../research/mobile-official-scripting-source-map.json).
- [Public MCP-derived KB source](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL) — methodology lead only; inspect the pinned commit and published tree before treating any claimed export as accessible evidence.

- [Rough block review queue](31-rough-block-review-queue.md) and [machine-readable queue](../research/rough-block-review-queue.json) — prioritized follow-up for the 92 fuzzy old-mirror candidates, 18 mirror misses, and one likely editor-native block; misses are not claims of absence.
