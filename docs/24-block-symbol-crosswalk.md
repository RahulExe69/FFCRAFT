# Block-symbol crosswalk for Rough.txt

## Purpose

The original `Rough.txt` remains untouched. This crosswalk compares each extracted line in `research/user-observed-block-inventory.json` against the detailed PC function, event, component and property declarations parsed from the public extension-library mirror.

Machine-readable result: [`research/block-symbol-crosswalk.json`](../research/block-symbol-crosswalk.json).

## Comparison result

For 443 lines extracted from `Rough.txt`:

- **306** lines have an exact normalized match to a mirrored symbol name or API documentation title.
- **113** lines have one or more approximate candidates, retained only as search leads.
- **21** lines have no match in the older mirrored libraries.
- **3** entries look like explanatory prose or section notes rather than standalone blocks.

The 113 approximate entries are **not confirmed mappings**. There are repeated labels and overloaded functions, and the mirror can include stale/deprecated declarations. Use source line numbers and the candidates in the JSON to review each case.

## Examples of confirmed label-level matches

| Rough label | Candidate recovered from mirror | Why it is useful |
|---|---|---|
| `On Game Start` | `StdLibrary.fcc: OnGameStart()` | Event signature is available |
| `On Round Start (Round Index)` | `Workflow.fcc: OnRoundStart(roundIndex int)` | Confirms the callback argument name/type in this snapshot |
| `Create Level Object` | `LevelObject.fcc: CreateLevelObject(...)` | Output entity and parameters are captured |
| `Add Item` | `Items.fcc: AddItem(...)` | Captures target, item ID, count and output list; snapshot marks it server-side |
| `Create Built in UI` | `Hud.fcc: CreateBuiltInUIClient(...)` or `CreateBuiltInUI(...)` | Shows that related names can have different client/server signatures |
| `Set SkyBox Type` | `Scene.fcc: SetSkyboxType(...)` | Snapshot marks this declaration deprecated, so a current official equivalent must be checked |

These are candidate source mappings, not proof that the same node exists in the current visual-block editor or on both platforms.

## Why some blocks do not match

A visual editor can have native data-flow/control blocks, property getter/setter blocks, generic type-cast nodes, and special nodes that do not appear as ordinary named `func` declarations in `.fcc`. The crosswalk intentionally does not force those names into unrelated APIs.

Current Garena documentation is also ahead of the mirror:
- [Studio 1.17.0 patch notes](https://ffcraftland.garena.com/en/patch-notes/) say TYPE-related APIs changed to ID-based APIs.
- [Studio 1.17.1 patch notes](https://ffcraftland.garena.com/en/patch-notes/) describe block recommendations when an empty block slot is selected.
- [Studio 1.19.0 patch notes](https://ffcraftland.garena.com/en/patch-notes/) describe an integrated MCP server that supports Blocks, Scripts, Scenes, UI, Animation Controllers, and more; the MCP URL is available inside the editor.

That makes the current editor itself the most promising authority for unresolved/current block IDs and available choices. This research pass has not connected to the user's local editor MCP endpoint, and has not inspected a current local `EditorGenLib.fcc` export.

## What the data file contains

Each entry preserves the category, subcategory, original line number, observed label/signature, exact candidates, approximate candidates and source blob SHAs. It marks fuzzy matches as leads only and flags likely narrative notes. The index draws from the 42-file version-1.5.0 public mirror; it is not a full current-version inventory.

## Next verification pass

Review every no-match and approximate entry against the live official docs/current editor. Then record separately:
1. current PC script/API symbol,
2. current PC visual-block label and socket types,
3. current Mobile visual-block label and dropdown values,
4. platform/side restrictions,
5. current/deprecated status,
6. source and test status.

Until then, the crosswalk is a gap map, not a compatibility guarantee.
