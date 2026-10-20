# Current editor metadata capture playbook

## Goal

Use the **currently installed Craftland Studio build** to close gaps that old public mirrors and tutorials cannot settle: exact current PC APIs, visual-block names/sockets, platform restrictions, generated graph scripts, and project-specific asset dropdown IDs.

The original `Rough.txt` remains untouched. Record new discoveries in the derived catalog and crosswalk, with a source file/screenshot/API response and editor version for every claim.

## Why local editor data is the stronger source

The public PC Code Script manual describes this official library location under the installation directory:

```text
Craftland Studio\\resources\\LocalData\\Utilities\\UGCLanguage\\release
```

Files in that directory are the libraries used by the installed editor/compiler, not arbitrary community examples. The manual describes:
- `.fcg` as code-script files.
- `.fcc` as library files containing types, components, events, APIs and other declarations.
- `EditorGenLib.fcc` as a generated/project library containing registered assets and references to graph-based block scripts.
- Asset/resource keys from `EditorGenLib.fcc` as a way to inspect registered assets and look up project-specific values.

Official PC manual: https://ffcraftland.garena.com/en/tutorial/fe/1-9

The current Studio 1.19.0 patch notes also state that Studio now integrates an MCP server that supports Blocks, Scripts, Scenes, UI, Animation Controllers, and more, and that its URL is available from inside the running editor:
https://ffcraftland.garena.com/en/patch-notes/

An editor-local MCP server or installed libraries are **not reachable from this chat by default**. Do not make the local endpoint public or disable authentication just to share it; export the metadata or share only the required files/screenshots instead.

## Capture A — current installed standard libraries

1. Open the installed Craftland Studio folder.
2. Navigate to `resources/LocalData/Utilities/UGCLanguage/release`.
3. Copy the current text `.fcc` library files into a zip or upload the relevant files. Do not include game binaries or credentials.
4. Include the Studio version/build number and the date the files were collected.
5. If any files are very large, start with `StdLibrary.fcc`, `Player.fcc`, `LevelObject.fcc`, `Items.fcc`, `Hud.fcc`, `Scene.fcc`, `Workflow.fcc`, `AI.fcc`, `BehaviourTree.fcc`, `Collection.fcc`, `Combat.fcc`, `Physics.fcc`, and any library identified in the unresolved-block crosswalk.

For current PC API recovery we can compare the current `.fcc` set against [the old-mirror catalog](../research/pc-library-symbol-catalog.json) and flag:
- new APIs/types/events,
- removed or renamed declarations,
- parameter/signature changes,
- deprecated/obsolete declarations,
- changed server/client and Mobile/PC annotations,
- enum value additions/removals,
- renamed or newly split type IDs.

## Capture B — project-specific generated data

If the project was opened in Studio, locate the project's generated `EditorGenLib.fcc` (the manual says it stores registered assets/graph-based block script references). Share that text file if the project permits it. It can supply data that cannot be reconstructed from a generic installed library, such as:
- the names and import paths of visual block-graph scripts,
- the key names chosen for registered assets,
- scene/UI/object/widget references,
- generated asset-ID maps/enums exposed to code.

This file varies by project; its contents should not be copied blindly into a general global catalog. Store a source-specific extract and keep sensitive or private project data out of public FFCRAFT.

## Capture C — live editor MCP inventory

In current Studio 1.19.0, locate the built-in MCP server URL from the editor's settings/integration UI. Prefer saving structured responses to JSON or text for:
- block catalog/search results,
- node definitions (display name, internal ID, category),
- inputs/outputs/port types,
- dropdown/enum values,
- context rules (which script/entity/module the block is valid in),
- platform/server-client restrictions if exposed,
- API/function/event descriptions,
- scene/UI/animation-controller definitions.

Do not post the endpoint publicly or share API tokens. An MCP URL that points to `localhost`/a private LAN is not automatically accessible outside the PC. The safe route is to export response data or screenshots here. If it exposes an authenticated/permissioned remote endpoint, use only the official intended integration and permissions.

A public community repo now provides a useful methodology lead: [the MCP repository audit](28-live-mcp-repository-audit.md) records a PowerShell generator/enrichment workflow and reported operations such as `eca-block-config-list` and `eca-get-action`. However, its inspected public commit contains only five files; the generated `blocks/`, `events/`, `actions/`, `valuations/`, `types/`, `indexes/` and `raw/` data are absent. Use it to guide a fresh capture, **not** as a substitute for collecting current responses or as proof of its self-reported counts.

## Capture D — Craftland Mobile block inventory

Mobile blocks are a separate inventory. PC `.fcc` APIs alone do not prove that Mobile exposes the same visual block or options.

For each dropdown or block that isn't fully captured in `Rough.txt`, obtain:
- one screenshot with the whole block and neighboring connections visible,
- one screenshot with its dropdown expanded and all options visible (scroll the dropdown and capture every segment),
- the block category and script context (Global, Player, Team, HUD, Object/Consumable),
- the exact Mobile/editor version and language,
- a screenshot/export of the connected inputs if relevant.

Most valuable first: the 21 lines that have no exact match in the old PC mirror, the 113 fuzzy-match leads, every label with a dynamic skin/asset ID list, and the ambiguous labels identified in [doc 24](24-block-symbol-crosswalk.md). The old-mirror crosswalk status is a search hint, not proof of current support or lack of support.

## Safe source/evidence labels

Use one status per observation:
- `official-current-installed-library` — extracted from the user's current installed build, version captured.
- `official-current-editor-mcp` — returned by the current editor MCP inventory, editor version and field names captured.
- `official-current-doc` — official online documentation.
- `user-observed-current-ui` — screenshot/export from the target Mobile/PC editor.
- `community-snapshot` — third-party repo/file with commit SHA and license/provenance notes.
- `derived-candidate` — text parser or approximate match, not yet confirmed.
- `runtime-tested` — only after a real build/test has been performed and the test environment is recorded.

Do not mark a declaration compiled or runtime-tested merely because it exists in a library.

## Priority order, by the question being answered

- **Exact PC code API signatures and enum declarations:** current installed `.fcc` libraries first; then current official online references.
- **PC visual node IDs, sockets, block-config dropdowns and context metadata:** current Studio MCP responses first, with raw JSON retained. Community extraction scripts are only a methodology lead until their output is reproduced.
- **Project-specific registered assets and graph scripts:** that project's generated `EditorGenLib.fcc`.
- **Craftland Mobile visual blocks and dropdowns:** current Mobile editor screenshots/exports first; the [official Mobile source map](29-official-mobile-scripting-source-map.md) is the topic guide, not the full inventory.
- **Semantics, platform and deprecation checks:** current official docs and patch notes, cross-checked against the matching installed build.
- **Public tutorials, old mirrors and other community repos:** discovery leads and examples only; retain commit, license/provenance and version caveats.

## Limitations

The [official Mobile scripting source map](29-official-mobile-scripting-source-map.md) now indexes the seven main scripting topic pages and two mechanism templates; it is not a node-by-node export. The public MCP-methodology audit likewise found no current raw catalog to import. This is a collection workflow, not evidence that the capture has already happened. No current installed library zip, current MCP response, project-specific `EditorGenLib.fcc`, or full Mobile dropdown screenshot set has been inspected in this pass. The public/research-derived files remain candidate references until the matching current data is supplied and compared.
