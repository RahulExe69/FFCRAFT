# Map1 logic audit tracker

## Status

**Partial / static inspection only.** This is not yet a line-by-line reconstruction of the serialized block graph.

## Known anchors

| Name | Initial interpretation | Confidence |
|---|---|---|
| `GameLoop` | Likely central gameplay controller/logic group | Inferred from name |
| `TilesList` | Likely collection of tile objects | Inferred from name |
| `ColourList` | Likely collection of colours or tile colour values | Inferred from name |
| `TargetColour` | Likely current target colour state | Inferred from name and HUD |
| `PickedColour` | Likely selected colour state | Inferred from name |
| `ColorHUD` | Likely UI object or UI-related logic | Inferred from name |
| `CurrentTile` | Likely currently selected/processed tile | Inferred from name |
| `LuckyTile` | Likely safe/winning tile or related state | Inferred from name |
| `Loser` | Likely failure/elimination handling | Inferred from name |
| `CheckedObject` | Unknown without graph connections | Unknown |

## Flow to reconstruct

1. Initialization: identify the actual event and all list/object setup.
2. Target selection: trace colour choice, randomness/rules, and state assignment.
3. HUD update: trace every writer of the target text and any duplicate UI references.
4. Player selection: trace input/trigger and the assignment to `PickedColour` or `CurrentTile`.
5. Resolution: trace comparison conditions, safe/losing outcome, tile visibility/destruction, and player consequence.
6. Round lifecycle: trace wait/timer logic, next round, reset and end conditions.
7. Intro: trace its start event and cadence, while preserving the creator's intended dialogue.
8. Multiplayer/state: determine which logic is authoritative, shared, or player-local where applicable.

## Required audit format

For each decoded script/block group, record:
- Script/object name and owning scope
- Entry event(s)
- Ordered blocks/nodes and their connections
- Inputs, output/state changes, and object references
- Branch conditions and loops
- Wait/timer behaviour
- Cross-script/event dependencies
- Evidence source and confidence
- Edge cases and proposed tests

## Not yet established

No exact block sequence, event wiring, branch condition, or round-reset implementation has been proven from the current static inspection. Do not generate a replacement logic graph or edit the export based only on the names above.

## Next action

Identify and decode the binary serialization and block graph. If no reliable decoder/schema is available, document experiments with copies and seek an editor-supported export/inspection method rather than guessing the format.
