# Community resources and how to vet them

Official documentation is the source of truth for API support, but community resources can reveal useful templates, solved problems, editor workflows, and edge cases. This page records promising leads discovered during research and how to use them safely.

## Community GitHub repositories found

### FF-OGC / Craftland-Tutorial

Link: https://github.com/FF-OGC/Craftland-Tutorial

The repository organizes Craftland Studio PC material by topic and language; the code-script manual includes `.fcg`/`.fcc` explanation, server/client restrictions, library imports, script structure, and guidance for a Visual Studio Code extension called **Free Fire Craftland Code**. It is useful as a searchable/offline reading aid and cross-reference.

**Caution:** this is a community-maintained/mirrored documentation source, not a guarantee that every page tracks the newest Studio release. The inspected copy also contained detailed editor instructions that should be checked against the official site/current installed version.

### nexosstudio / CRAFTLAND_STUDIO_RESOURCES

Link: https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES

Its public README describes folders for assets, docs, scripts, templates, and tools. The README declares a CC0-1.0 license. It may be a useful source of discovery leads and reusable material.

**Caution:** verify the current repo license and individual asset/source provenance before reuse. Do not assume every external dependency or linked asset is cleared just because the repository-level README lists CC0. Inspect scripts for old APIs, hard-coded assumptions, unsupported languages, and Mobile-vs-PC constraints before running or copying them.

No arbitrary third-party code from either repository has been copied into FFCRAFT or treated as a verified implementation by this research pass.

## Official community sources

Garena's official portal links to the Craftland Global Discord and official creator resources. Official-hosted creator tutorials are particularly useful for practical systems such as:

- Custom triggers and game mechanics.
- Round count and objective changes.
- Revive buttons and per-player events.
- Character transformations, custom HUD/menu, and moving objects.
- Editor UI, publishing, assets, and troubleshooting.

Browse: [Craftland home](https://ffcraftland.garena.com/en/), [gameplay systems tutorials](https://ffcraftland.garena.com/en/community/creator-tutorials:-gameplay-systems/), [custom feature tutorials](https://ffcraftland.garena.com/en/community/creator-tutorials:-custom-features/), [creator basics](https://ffcraftland.garena.com/en/community/creator-tutorials:-creator-basics/).

## How to evaluate a community script/tutorial

Before trusting a downloaded block, `.fcg`, `.fcc`, asset, or video:

1. **Date/version:** when was it published and which Craftland/Free Fire version did the creator use?
2. **Platform:** Craftland Mobile, Studio PC, server script, client script, or offline template?
3. **API freshness:** are functions/events marked obsolete in current docs? Do names and parameters match installed `.fcc` definitions?
4. **Authority/security:** can a client change scores/currency/win conditions without validation? Are player identity values confused with slots or display names?
5. **Lifecycle:** what happens on leave/reconnect, death/respawn, round reset, scene switch, and game end?
6. **Performance:** are loops bounded? Are data writes throttled? Are spawned entities/timers cleaned up?
7. **Dependencies/license:** are asset IDs, prefabs, textures, scripts, fonts, audio, or other files required? Are they legally reusable?
8. **Reproducibility:** can a minimal example reproduce the claim in the current editor?

## How FFCRAFT should capture a discovery

For each new community finding, add an entry with the original URL, creator/author, date observed, claimed editor/client version, exact steps, relevant block/API names, expected and actual output, screenshots/logs if available, and an evidence label from `00-research-method.md`.

Never store passwords, account tokens, private Discord content, or other credentials in this repo. Do not commit a map/project dump that contains private player data or personally identifiable information.
