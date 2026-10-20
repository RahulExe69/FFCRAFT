# ColourBridge — HUD and timer fix (working copy)

**Status: source-graph patch built; Craftland import and in-game validation still pending.** This is a separate working copy of the user-provided ColourBridge export. The pristine original is `projects/templates/Map1/`; do not edit it.

## What was found

### Duplicate `FIND THE COLOUR`

The decoded source graph contains both (1) a persistent custom HUD label, whose background image is coloured from `TargetColour`, and (2) a `NotifyShowTips` action in `GameLoop` that sends the same text for 5,000 ms. The screenshot shows the two texts layered together. This is a duplicate output source, not evidence that the label itself needs redesigning.

### Timer stuck at `00:00`

`OnMatchStart` creates a `PhaseCountDownHud`, sets its `DurationTimeS` to 16 seconds, then waits 15,000 ms before calling `GameLoop`. The timer is not restarted by the original repeated colour-loop path. The recurring script cadence is approximately 11 seconds: 1,000 ms pre-round wait + 5,000 ms visible decision period + 5,000 ms resolution wait.

## Source graph changes

The builder modifies only a separate copy of `ProjectData_slot_1.bytes`:

1. Disables the redundant `NotifyShowTips` action but keeps the persistent yellow custom HUD label.
2. Disables the one-shot `PhaseCountDownHud` creation/property writes in `OnMatchStart`.
3. Adds a graph variable `RoundTimerHUD`; the start of each `GameLoop` creates a phase countdown, sets it to 11 seconds and stores the created entity.
4. Adds timer removal to `Loser` immediately before the next recursive `GameLoop` call, to prevent old countdown overlays accumulating.
5. Preserves the authored welcome dialogue, existing `ColorHUD` colour-setting logic, tile setup, five-second gameplay HUD and original template assets.

## Important export caveat

The graph in `ProjectData_slot_1.bytes` is patched and statically validated. `UserLevelData_1.bytes` and `ProjectData_slot_1.meta` remain copied from the original because their regeneration process and relationship to runtime serialization have not been established. **This is not yet an editor-generated full export or a proven in-game fix.** Open/import the separate working export in Craftland Mobile, save/re-export it so the editor can update its companion data, then run the tests in [testing.md](docs/testing.md).

## Rebuild the working export

From the repository root:

```bash
python projects/maps/colourbridge-fixed/build_fixed_export.py
```

The script reads the pristine template and writes generated files to `build/colourbridge-fixed-export/` and `build/colourbridge-fixed-export.zip`. It does not write to `projects/templates/Map1/`.

## Static validation performed

- The gzip-wrapped inner graph was decoded with the typed graph parser.
- A no-op serialize/decode round trip reproduced the original inner graph byte-for-byte before modification.
- The patched graph re-parses to its exact new length and retains untouched outer fields.
- Static assertions confirm the duplicate tip is disabled, old startup timer nodes are disabled, the per-cycle 11-second timer create/property/store sequence is enabled, and timer removal precedes the recursive loop call.
- A deterministic rebuild was executed successfully from a test repository with a copy of the template.
- Craftland import, editor save/re-export, and in-game behavior are **not yet tested**.

## Official references

- [UI Widget Label](https://ffcraftland.garena.com/en/docs/type-40)
- [UI Phase Timer](https://ffcraftland.garena.com/en/docs/type-1021/)
- [Official custom HUD and timer scripting tutorial](https://ffcraftland.garena.com/en/tutorial/cl/4-87)
