# Map1 — creator intent and observations

## Creator intent

- The project is named **ColourBridge**.
- The welcome dialogue `Welcome To Colour Bridge` was authored by the creator. Treat it as intentional, not a defect to remove.
- The current task is to understand the existing map first, then make evidence-based suggestions. Do not create or modify a sequel until the creator agrees on changes.
- Keep the original export untouched.

## Direct observations from supplied screenshots

- The editor screenshot shows a long, straight white bridge, bordered by low side rails, connected to a wooden starting platform with concrete-like railings.
- The gameplay screenshot shows a HUD label reading `FIND THE COLOUR` and a bridge surface made of coloured sections.
- Another screenshot shows most of the coloured surface absent while a few separated coloured platforms remain.
- The introduction screen displays a narrator panel with `Welcome To Colour Bridge` and a second visible line that appears truncated in the screenshot.
- The HUD appears to show duplicated/overlapping `FIND THE COLOUR` text in one screenshot.

## Interpretations that need verification

- The missing floor may be a tile-removal, safe-tile reveal, or round-resolution effect.
- The repeated HUD text may be duplicate UI elements, repeated script updates, layout/rendering, or capture timing.
- The narrator line may be clipped, still typing, or cut off by the dialogue UI. The screenshot alone cannot establish the cause.
- The player model appearance may be a game asset/rendering state; do not assume a map script caused it.

## Questions for a future logic audit

1. Which event starts the gameplay loop?
2. How are `TilesList` and `ColourList` initialized and kept aligned?
3. How is `TargetColour` selected and displayed?
4. What updates `PickedColour` and `CurrentTile`?
5. What makes a tile safe, lucky, or losing?
6. What action removes/hides the other tiles, and when?
7. How are player failure, respawn, round reset, and end conditions handled?
8. Which UI object/script writes the `FIND THE COLOUR` text?
9. At what lifecycle event does the welcome dialogue run, and is that cadence intentional?

Do not answer these questions from variable names alone. Trace decoded graph connections and verify uncertain runtime behaviour.
