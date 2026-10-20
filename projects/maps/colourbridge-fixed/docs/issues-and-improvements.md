# ColourBridge issues and improvements

## CB-01 — Duplicate `FIND THE COLOUR`

- **Observed:** supplied screenshot shows a bright main title and a dim, offset duplicate beneath it.
- **Decoded evidence:** persistent custom HUD label plus a separate `NotifyShowTips("FIND THE COLOUR", ..., 5000 ms)` action in `GameLoop`.
- **Root-cause confidence:** high.
- **Source-graph change:** disable the redundant tip; preserve the persistent label and its colour update.
- **Regression risk:** a deliberate temporary help tip, if desired as a separate gameplay cue, is removed.
- **Manual test:** join the map and complete at least three colour cycles; there should be only one title.

## CB-02 — Top phase timer stays at `00:00`

- **Observed:** screenshot shows `00:00` while the player is already on the colour bridge.
- **Decoded evidence:** a one-time 16-second `PhaseCountDownHud` is created at match start, followed by a 15-second wait before `GameLoop`. The recurring loop itself is approximately 11 seconds.
- **Root-cause confidence:** high for a timer with the wrong lifecycle.
- **Source-graph change:** disable the one-shot timer setup; create an 11-second timer each loop, store the entity, and remove it at the loop transition.
- **Regression risk:** internal HUD creation and the `DurationTimeS` property have not been verified in the installed Mobile runtime. The patch preserves the original HUD/player scope assumptions.
- **Manual test:** save/re-export using Craftland Mobile, then watch at least three cycles. The timer should count down, reset, and not leave overlapping HUDs.

## Verification state

Static decode/encode/structural assertions passed. Import, editor save/re-export and in-game tests are still pending. Do not report the fixes as game-tested until observed in the editor/game.
