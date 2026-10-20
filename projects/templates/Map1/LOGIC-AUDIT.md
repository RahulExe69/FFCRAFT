# ColourBridge — Map Logic Audit (Mobile Export)

> Status: first-pass static inspection. This document records what is supported by the exported files and screenshots; it does not claim the serialized block graph has been fully decoded. Keep the original Map1 export unchanged.

## Source files inspected

- `projects/templates/Map1/ProjectData_slot_1.bytes` — 107,913 bytes
- `projects/templates/Map1/ProjectData_slot_1.meta` — 38,853 bytes
- `projects/templates/Map1/UserLevelData_1.bytes` — 132,083 bytes
- `projects/templates/Map1/UserLevelData_C_1.bytes` — 74,723 bytes
- `projects/templates/Map1/SceneReview_1.bytes` — 211,296 bytes
- `projects/templates/Map1/DataStorageFile_Server_Slot1.json`
- `projects/templates/Map1/ProjectEditRecord_slot_1.meta` and its JSON sidecar

The two UserLevelData files contain repeated object labels and serialized references. They are binary editor data, not plain-text source code. Text extraction can reveal labels and likely variable names, but cannot by itself establish the exact control-flow graph or event wiring.

## Confirmed from exported names and the supplied gameplay screenshots

- Project/map label: `ColourBridge`.
- The editor metadata contains many repeated `Tile` entries and `CheckedObject`.
- User-level data includes labels/names `TilesList`, `ColourList`, `TargetColour`, `PickedColour`, `ColorHUD`, `GameLoop`, `CurrentTile`, `LuckyTile`, and `Loser`.
- UI/scene names include `FIND THE COLOUR`, `HudID-1`, `Spawn Point1`, and `Custom trigger1`.
- A serialized dialogue/text entry contains `Welcome To Colour Bridge`.
- Screenshots show a long bridge with coloured sections; another screenshot shows the coloured floor largely absent while separated coloured platforms remain.

## Interpretation — plausible, not yet proven

The names suggest a colour-selection gameplay loop that tracks tiles, stores a target and a picked colour, updates a colour HUD, and may use a lucky/safe tile and a loser state. The disappearing-floor screenshot is consistent with some tile-removal or reveal mechanic. We cannot yet prove which event starts the loop, how the target is selected, whether incorrect tiles are removed, or whether falling is the intended failure condition.

The welcome dialogue is creator-authored content and must be treated as intentional unless the owner asks to change it. Do not recommend removing it as a default cleanup.

## Initial review priorities (do not edit until block graph is decoded)

1. **Round/state lifecycle:** trace initialization, round start, target selection, player choice, resolution, reset, and end conditions. Ensure state is reset at the intended boundary and not accidentally repeated.
2. **Tile lists and references:** determine how `TilesList` and `ColourList` are built, whether their indices stay aligned, and whether `CurrentTile`/object references can become stale.
3. **HUD updates:** trace all writes to `ColorHUD` and the `FIND THE COLOUR` UI. The screenshot appears to show overlapping/repeated text, but this could be a duplicated UI object, repeated update, or render/layout issue; do not assume which without checking object/script references.
4. **Tile removal/reveal:** identify the exact action and trigger responsible for the missing floor. Verify timing and whether the removal is expected after selection, timeout, or round progression.
5. **Player failure and recovery:** trace `Loser`, fall/kill-zone triggers, spawn point, and reset path.
6. **Intro dialogue:** preserve the welcome message; inspect text clipping/sequence only if the creator wants it improved.

## Current findings are not yet enough to safely propose a specific block-by-block edit

The key remaining step is to decode the Craftland serialized block/script representation and map its IDs, event nodes, block types, links, and parameters. The repository's scripting references can help identify supported blocks, but generic documentation is not a substitute for the actual graph stored in this export.

Until that is decoded, avoid editing the binary exports by hand. Make changes in Craftland Mobile and export a fresh copy, or use a verified editor-supported import/edit path. Keep a pristine backup of this Map1 template.
