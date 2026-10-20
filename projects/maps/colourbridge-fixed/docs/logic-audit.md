# ColourBridge source-graph audit

**Status:** Decoded static source audit; import/runtime test pending.

## Confirmed script groups

The main graph is `GR_617ac097-7cff-44c2-894e-51668b4233d9` inside `ProjectData_slot_1.bytes`.

| Group | Decoded flow |
|---|---|
| `GameLoop` | Selects `TargetColour`, waits 1 second, emits `NotifyShowTips("FIND THE COLOUR", ..., 5000 ms)`, prepares/colours tiles, updates `ColorHUD` background with the target colour, creates a five-second countdown HUD, then calls `Loser`. |
| `OnMatchStart` | Calls `Variables`, gathers objects tagged `Tile`, creates `PhaseCountDownHud`, sets `DurationTimeS=16`, waits 15 seconds, removes the start/spawn box, and enters `GameLoop`. |
| `Loser` | Resolves the tile phase, waits 5 seconds, then calls `GameLoop` again. |
| `OnPlayerAdd` | Performs camera/wait setup, shows creator-authored welcome dialogue, then creates the custom HUD. That authored dialogue is preserved. |

## HUD duplicate

The persistent custom HUD data already contains `FIND THE COLOUR`; the independent `NotifyShowTips` action in `GameLoop` emits the same string for five seconds. This aligns with the screenshot's main yellow banner plus dim offset text. Root-cause confidence: **high**.

## Timer lifecycle

The original phase timer is created once during `OnMatchStart`, with a 16-second duration, while the start handler waits 15 seconds before gameplay. It is not recreated during the repeated colour cycle. The repeated cycle is approximately 11 seconds: 1 second at the beginning of `GameLoop`, a 5-second decision HUD, and 5 seconds in `Loser`. Root-cause confidence: **high for an unsynchronized one-shot timer**, though the UI runtime itself has not been playtested here.

## Applied changes in working copy

- Disable only the duplicate `NotifyShowTips` writer.
- Disable the original one-time phase timer create/property nodes.
- Add graph state `RoundTimerHUD`.
- Create a phase countdown set to 11 seconds at each `GameLoop` entry and save the created entity.
- Remove that entity in `Loser` before the loop calls `GameLoop` again.

## Serialization and remaining uncertainty

A custom typed parser decodes the gzip-compressed custom graph format. A no-op re-encode/decode pass reproduced the uncompressed original graph bytes exactly before changes. Static validation of the patched graph passes. The patch changes `ProjectData_slot_1.bytes` only; `UserLevelData_1.bytes` and `ProjectData_slot_1.meta` are copied untouched. Craftland Mobile must import/open and save/re-export the working copy to determine whether those companion files are regenerated. Runtime success remains unknown until then.
