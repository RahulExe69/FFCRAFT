# Public tutorial corpus audit: manuals, block editor, code and recipes

## What this source adds

A public multilingual repository, [`FF-OGC/Craftland-Tutorial`](https://github.com/FF-OGC/Craftland-Tutorial), contains **3,796 Git tree entries and 160 Markdown manuals** across English, Vietnamese and Chinese. GitHub metadata reports the latest commit as **2025-11-12** (commit `e4cf9dc7a8ee9cb7189478abb2f80a8b11d64b44`). The repository metadata page showed an update date of 2026-09-30, but its latest commit is older; for freshness, use the commit date rather than the metadata edit field.

The repository has no explicit license surfaced in GitHub metadata. The English manuals include images hosted on official Garena content-delivery hosts. We therefore record links, file hashes, headings and our own concise summaries rather than copying the full manuals or image library into FFCRAFT. Treat it as a secondary translated/manual corpus—not the current official API source.

Machine-readable indexes:
- [Full Markdown manifest](https://github.com/RahulExe69/FFCRAFT/blob/main/research/audits/public-tutorial-corpus-index.json) — 160 Markdown paths, hashes/sizes, script-related tags, important page outlines and source links.
- [Mobile block recipe index](https://github.com/RahulExe69/FFCRAFT/blob/main/research/mobile/mobile-block-recipe-index.json) — 13 summaries from the re-editable Game Mechanics template.
- [Existing PC API/function catalog](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/pc-library-api-reference.json) — separate from visual block documentation.
- [Rough-to-PC symbol crosswalk](https://github.com/RahulExe69/FFCRAFT/blob/main/research/crosswalks/block-symbol-crosswalk.json) — marks matches and gaps from your original notes.

## Most valuable manuals

### Craftland Mobile: Block Script

Source: [Block Script tutorial](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20Mobile/English/Features/Block%20Script.md), blob `709422e3eacbb47790ac2307d737f0d22305eae0`.

The tutorial explicitly says the editor’s red blocks are event entries and most actions appear in green/blue categories. Colored ports and plus signs indicate required/provided typed data. The example shows how to:
1. Connect `On Player Join`.
2. Feed the joining Player into `Get Property`.
3. Read the player's rig, then the rig's head.
4. Use the head as the target of `Set Property`, select `Skeleton Scale`, and feed a Vector3 assignment with X/Y/Z all set to 3.
5. Keep script attachment scope in mind: global, player, team and object/consumable scripts do not have the same behavior.

The key wide screenshot is [the documented connected-block example](https://dl.dir.freefiremobile.com/common/OB46/CSH/OfficialWeb/CLtutorial/009_BlockScript_New/image-20250402192733907.png). That image shows actual selected UI values and wiring; it is evidence for this example, **not a complete dump of all dropdown options**.

### Craftland PC: Code Script manual

Source: [Code Script - User Manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/4.%20Scripting%20and%20Logic/Code%20Script%20-%20User%20Manual.md), blob `18a3fcfb17de1e08878eac2dcf9975e2fe741db7`.

This is one of the best public explanations of the code environment:
- `.fcg` files are script files; `.fcc` files are libraries.
- Standard libraries are automatically added to new code scripts.
- It describes server/client code, functions/events, parameters/returns, async waits, user-defined events/components/enums, imports, asset registration and compile workflow.
- Editor-generated `EditorGenLib.fcc` records game/editor data and block-script graphs that can be imported from PC code.
- When a block script is non-static, the script must be associated with the correct entity when called.
- The editor tooling provides API/event autocomplete, parameter hints, and navigation into library definitions.

That generated `EditorGenLib.fcc` is a high-value route for mapping **a particular project’s block-script graphs and registered asset dropdowns**. A stock public library cannot include every project’s generated asset/type list.

### Craftland PC: Block/Element Script manual

Source: [Element Script - User Manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/4.%20Scripting%20and%20Logic/Element%20Script%20-%20User%20Manual.md), blob `65688f0b3fc9783c945cd9f26fc7c5b5efece524`.

This documents the PC graph editor: block/port shapes, data typing, flow control, global/entity variables, script/local variables, custom functions and custom events. It is directly useful for converting a block concept into matching PC code structure, but it is not a complete live dump of all current blocks.

### Craftland PC: Script and language references

- [Script - User Manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/4.%20Scripting%20and%20Logic/Script%20-%20User%20Manual.md) distinguishes block vs code, server/client, static scripts and mounting/usage.
- [Script Additional Notes](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/4.%20Scripting%20and%20Logic/Script%20Additional%20Notes%20-%20User%20Manual.md) covers syntax, enum and collection types, `entity<T>`, component access, operators, loops and conditionals.
- [Formula Property](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/4.%20Scripting%20and%20Logic/Formula%20Property.md) describes property-formula logic and weapon-damage calculation examples.
- [Global manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/6.%20Global/Global%20-%20User%20Manual.md) covers custom room parameters, global scope and timed pause/resume examples.
- [Player manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/7.%20Player/Player%20-%20User%20Manual.md) explains player-module configuration and the consequences of per-player vs global event scope.
- [Level Object manual](https://github.com/FF-OGC/Craftland-Tutorial/blob/main/Craftland%20PC/English/12.%20Level%20Objects/Level%20Objects%20-%20User%20Manual.md) covers object families, triggers, generators, safe-zone objects and zombies.

## Reusable Mobile recipe examples indexed

The source's re-editable Game Mechanics template explains 13 recipe areas:
1. Healing zone — periodic health restoration and effects.
2. Damage zone — periodic player damage.
3. Monster spawn zone — relative positioning, zombie configuration and sound.
4. Trap area — trap movement/activation and a timed reset.
5. Transfer area — delayed teleport, countdown UI/effects and cancellation cleanup.
6. Text display area — create/show/hide a text entity on trigger enter/exit.
7. Outfit change area — choose and apply outfit based on player gender.
8. Elevator — track occupants and step a moving object with timed loops.
9. Automatic door — enter/exit events and state-dependent movement.
10. Global script — initialize a shared marker/state variable.
11. Player script — initialize player state and respawn after a delay.
12. HUD button — branch on entity/global state and invoke a corresponding action.
13. Respawn-point script — activate on round start, then deactivate after a short wait.

See the JSON for line ranges and explicit source-version/testing caveats. These are recipe descriptions, not copied runnable scripts and not a guarantee that old screenshot socket labels still exactly match the current editor.

## Current editor vs public manuals

The official [Craftland Studio patch notes](https://ffcraftland.garena.com/en/patch-notes/) describe a current integrated MCP server that can expose Blocks, Scripts, Scenes, UI, Animation Controllers and other editor concepts; the MCP endpoint is available inside the running editor. That is likely the strongest source for *current* block IDs, names, sockets and project-generated definitions if its endpoint/data can be accessed. We have not connected to a running Studio instance in this work.

Until current editor exports/screenshots are available, use this source hierarchy:
1. Current official API/event/type reference and current installed editor libraries.
2. Current editor-generated `EditorGenLib.fcc` or editor/MCP metadata for project-specific assets/blocks.
3. Public 1.5.0 extension mirror for symbol discovery.
4. Public tutorial translations and screenshots for conceptual wiring and example mechanics.
5. `Rough.txt` as the raw record of what you personally saw.

Never treat a PC API signature as proof that Mobile has the same visual block, socket names, dropdowns or platform scope. Record these as separate observations.
