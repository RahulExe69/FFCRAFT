# Block scripting field guide

## What block scripts can do

Garena describes block scripts as visual, event-driven logic that can control many game entities: player properties, backpack items, UI button behavior, weapon damage, and other custom effects. The usual pattern is: event/trigger → optional conditions → actions/API calls → feedback/state update.

Official reference: [Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101).

## Where to open the editor

Official documentation lists several entry points, depending on the editing surface: **More → Block Scripts**, **Basic Settings → Edit Scripts**, or selecting an object and choosing **Edit Blocks** beneath its property panel. Not every entry point appears in every version/context.

The editor includes a block search/category panel, script list, script-type toggle, and a context menu with undo/redo, templates, tutorial, log output, clear, and component management. Search can display results that are not available for the current script type; attempting to use them can produce an error. Search supports the current UI language and English.

## Block categories you should recognize

- Events/triggers: start a script when a documented event occurs.
- Flow control: sequencing, conditionals, loops, and early exit.
- Variables/properties: maintain local/script state and read/write entity properties.
- Data/logic operations: comparisons, boolean operations, math, conversion, and collection helpers.
- Entity/player/team APIs: query players/teams/entities and apply actions within the current runtime.
- UI/HUD: create or alter supported UI and bind player-facing actions.
- Debug/logging: print state, inspect execution, and narrow down where a graph stops.

Exact category names and membership can change. Use the live block search and the official [Block Classification and Flow Control](https://ffcraftland.garena.com/en/tutorial/cl/4-104) guide as the map.

## Recommended authoring pattern

1. Add one clearly named script in the correct scope (global/player/team/object/UI).
2. Pick one documented event, such as On Player Join or On Player Eliminate.
3. Confirm whether the script is server-side or client-side before adding blocks.
4. Add guards before mutating state: valid player/entity, correct phase, cooldown, team/role requirement, or not already processed.
5. Keep authoritative state mutation separate from UI/audio feedback.
6. Log key values before and after the mutation during testing.
7. Test repeated events and cleanup/reset paths.

## Script type is a correctness constraint

The official editor has distinct block and client-side script types. Some blocks exist only for one type; a search result alone does not prove availability. A client-only block in server logic (or vice versa) is not a small warning—it is a runtime/design error. Switch to the correct script context or use a supported event bridge.

## Event wiring and parameters

Treat event-provided parameters as typed values. For example, the official guide explains that an On Player Join event supplies a Player parameter, which can be connected to a player input slot in a HUD-creation action. A function/action that expects a Player should not be given an unrelated entity, UI element, or player index.

Before wiring an action, inspect the input slots/parameter types and select compatible outputs. Yellow/drag-compatible parameter slots and dropdown-selected properties are editor UI details that may vary by version.

## Reusable template resources

The official tutorial says a block template needs at least two blocks in the saved group. Use Save Template to package the selected block and the blocks beneath it, including contained parameter blocks. Downloaded block/HUD resources can be found through the resource manager and applied from the relevant editor.

Reference: [Publishing Blocks and HUD UIs](https://ffcraftland.garena.com/en/tutorial/cl/4-100).

## Common failure modes

- **Block appears in search, but errors on use:** likely unavailable in the selected script type/context or unsupported in that environment.
- **Logic runs twice:** multiple events or attached scripts may be responding; add logging and inspect all attachment points.
- **Wrong target player:** a player parameter may be confused with a player slot/index, local player, owner, or entity.
- **UI changes only for one player:** client-local presentation and server/shared state have been mixed. Identify which side owns the UI and whether state must be sent to clients.
- **Counter resets unexpectedly:** the script variable lifetime or reset event is not the lifetime intended by the design.
- **Action stops at a condition:** log condition inputs and test both branches explicitly.
- **Graph is hard to maintain:** split it into reusable templates, helper scripts, or code once complexity warrants it.

## Block-script checklist

- [ ] Scope and runtime side confirmed.
- [ ] Exact event and parameter types confirmed in current editor.
- [ ] Every called block is available in this context.
- [ ] State owner and reset lifetime documented.
- [ ] Null/invalid/disconnected targets handled where needed.
- [ ] Duplicate trigger path considered.
- [ ] Logs added for important transitions and removed/filtered before release.
- [ ] Tested in a real playtest, not only in the editor canvas.
