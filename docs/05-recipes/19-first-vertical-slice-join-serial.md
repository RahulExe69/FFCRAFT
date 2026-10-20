# First vertical slice: sequential player join serial

**Status:** design and source checks completed; not compiled or playtested.  
**Chosen because:** this mechanic already has a documented recipe in FFCRAFT, a clear acceptance test, and an official event reference shared by Mobile and PC. It lets us test the workflow without inventing an entirely new system.

## Natural-language request

“When a player joins the match, assign them the next number in join order: 1, 2, 3, and so on. A later player must not inherit that number just because they reuse a player slot.”

## Acceptance criteria

- One authoritative sequence is assigned in the chosen scope.
- The first join receives 1; each subsequent join event increments once.
- Reusing a runtime slot never reuses an earlier serial.
- Reconnect behavior is explicit. This first version uses **join-attempt serials**: a reconnect receives a new serial.
- The counter resets once at the intended match/session boundary, not automatically at every round.
- The number is stored on the correct player and displayed only through a supported player/UI mechanism.
- Invalid references and lifecycle transitions do not crash the script.

## Evidence already confirmed

1. Garena's **On Player Join** event page says it triggers when a player joins, is owned by the Game entity, and is documented for both Server and Client and both Mobile and PC. Source: https://ffcraftland.garena.com/en/docs/event-11-14
2. Garena's PC API page for **Set property** says the target attribute must already be defined, and labels this API **Only PC**. Source: https://ffcraftland.garena.com/en/docs/api-1-871/
3. Garena's Mobile block tutorial demonstrates wiring the Player output from On Player Join into a Player-accepting action and demonstrates Set Property for a created HUD entity. This confirms a visual-block wiring pattern, but does **not** establish that the PC-only Set property API is a Mobile player-property setter. Source: https://ffcraftland.garena.com/en/tutorial/cl/4-101

## Craftland Mobile: visual-block plan

**Status: conceptually specified; exact player storage block/property is unresolved. Do not substitute a PC-only API.**

1. In the game/global script context, create an integer counter with match/session lifetime.
2. Initialize it to zero at the documented/current game initialization event.
3. Use the Game entity's On Player Join event.
4. Increment the shared counter once per event, then copy the resulting integer into a player-scoped field using a setter explicitly available in the current Mobile editor.
5. If the serial should appear on screen, use a player-specific UI path. Do not assume a shared HUD or a global property is private to one player.
6. Test two sequential joins, slot reuse after leave, reconnect, and match reset.

**Blocking evidence needed:** a version-stamped screenshot or export from the current Mobile editor showing the exact block that stores an integer on a Player entity (including its input slots and scope). Until then, the exact block graph is not claimed complete.

## Craftland Studio PC: code-script plan

**Status: design-level; exact compile-ready source still requires the current installed .fcc declarations.**

1. Create a server-side global script that owns the match counter.
2. Initialize the counter at the selected session start event.
3. Handle On Player Join on the server side.
4. Increment the counter once and assign the result to a property defined on the intended Player/entity type.
5. Use only the current PC API signature confirmed in the installed libraries/extension. The public Set property reference says the target property must already exist and is PC-only; it does not by itself confirm the name/type of a player property that is appropriate for this serial.
6. If client UI needs the number, use a documented server-to-client replication mechanism and verify that the target UI is player-specific.

**Blocking evidence needed:** the installed PC version's declaration for the selected property setter and the defined player property, plus a successful compile. Do not invent an FCC function signature from the conceptual pseudocode in the related recipe.

## Test matrix

| Test | Expected result |
|---|---|
| First player joins | Serial = 1 |
| Second player joins | Serial = 2 |
| First player leaves; a new player joins | New player receives 3, even if a slot is reused |
| Player reconnects | New serial is assigned in join-attempt mode |
| A new round begins | Counter stays unchanged if the serial is match-scoped |
| A new match/session begins | Counter resets to zero before the first join is processed |
| Two players join close together | Unique serials; no duplicate assignment |
| Player-specific display | Each player sees their own serial, not another player's |
| Missing/invalid player reference | Handler fails safely and logs useful context |

## Completion gate

Do not mark this mechanic **editor-verified**, **compiled**, or **playtested** until those steps have actually happened in the intended environment. Current state: **official event documented; Mobile setter unresolved; PC property setter/platform limit documented; implementation not compiled/tested**.

## Related docs

- [Player roster and sequential join serials](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/04-gameplay-systems/05-player-roster-join-serials.md)
- [AI Craftland coding workflow](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/05-recipes/14-ai-craftland-coding-workflow.md)
- [Craftland Mobile block tutorial](https://ffcraftland.garena.com/en/tutorial/cl/4-101)
- [Craftland PC Set property API](https://ffcraftland.garena.com/en/docs/api-1-871/)
