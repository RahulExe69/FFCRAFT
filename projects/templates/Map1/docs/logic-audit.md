# Map1 logic audit

**Status:** Serialized graph decoded and statically audited. Craftland import/runtime verification remains pending. The original export in this directory is reference-only and has not been modified.

## Confirmed graph structure

The main graph is `GR_617ac097-7cff-44c2-894e-51668b4233d9` in `ProjectData_slot_1.bytes`.

| Script group | Confirmed behaviour from decoded node graph |
|---|---|
| `GameLoop` | Selects a random `TargetColour`, waits 1 second, contains `NotifyShowTips("FIND THE COLOUR", ..., 5000 ms)`, prepares/colours tiles, updates the persistent `ColorHUD` background from `TargetColour`, creates a five-second decision countdown, and calls `Loser`. |
| `OnMatchStart` | Calls `Variables`, gathers objects tagged `Tile`, creates `PhaseCountDownHud`, sets `DurationTimeS = 16`, waits 15 seconds, removes the start/spawn box and enters `GameLoop`. |
| `Loser` | Resolves the tile phase, waits 5 seconds and calls `GameLoop` again. |
| `OnPlayerAdd` | Performs camera/wait setup, triggers the authored welcome plot/dialogue, waits, and creates the custom HUD. Preserve the creator-authored dialogue. |

## HUD duplicate

The persistent custom HUD contains `FIND THE COLOUR`. Separately, `GameLoop` sends the same text through `NotifyShowTips` for 5,000 ms (`FC_eceaa884-6d9c-4126-8635-c8102e65b6f1`). This matches the screenshot's bright banner plus dim, slightly offset duplicate.

**Root-cause confidence: high.** Proposed source-graph fix: disable the redundant tip node and keep the persistent `ColorHUD` label and its colour-setting logic.

## Timer stuck at 00:00

The one-shot `PhaseCountDownHud` is started in `OnMatchStart` with a 16-second duration, while that handler waits 15 seconds before the first gameplay loop. The repeating colour loop is approximately 11 seconds: 1-second pre-round wait + 5-second choice period + 5-second resolution wait. The original phase HUD is not recreated/reset by that recurring path.

**Root-cause confidence: high for the one-shot/misaligned lifecycle.** Actual behaviour of a newly created phase HUD and its duration property still needs testing in the installed Mobile editor.

## Working-copy patch

A separate reproducible patch is documented in [ColourBridge HUD/timer fix](../../../maps/colourbridge-fixed/README.md). It disables the duplicate tip and original startup timer nodes, creates an 11-second phase timer per loop, stores its entity, and removes it before the next loop. It preserves the original template and welcome dialogue.

## Serialization/export caveat

A typed decoder for the custom compressed graph container now exists in the working-copy folder, and its no-op round trip matched the original decompressed graph byte-for-byte. The patch modifies `ProjectData_slot_1.bytes` only. `UserLevelData_1.bytes` and `ProjectData_slot_1.meta` remain copied from the original; their regeneration process is not yet established. The patch is therefore a **source-graph patch**, not a fully editor-generated or runtime-verified export.

Rebuild the working export from the repo root with `python projects/maps/colourbridge-fixed/build_fixed_export.py`. Then import/open and save/re-export through Craftland Mobile and test several cycles. Do not edit this pristine template or claim a successful in-game fix until that test is completed.

## Test status

- [x] Decode complete source graph.
- [x] Verify no-op graph round-trip against the original decoded bytes.
- [x] Build and statically validate a separate patched graph.
- [ ] Import/save/re-export in Craftland Mobile.
- [ ] Confirm one target label is visible.
- [ ] Confirm the timer counts down and resets for at least three cycles.
