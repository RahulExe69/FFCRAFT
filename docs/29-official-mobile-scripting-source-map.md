# Current official Craftland Mobile scripting source map

**Checked:** 20 October 2026  
**Scope:** official Mobile-oriented block scripting pages that can guide the next pass over the original block inventory. This is a source-navigation map, **not** a complete export of current blocks or dropdown contents.

## Official scripting sequence

Garena's current Mobile learning pages break block scripting into the following focused topics. Read the relevant page before deciding what a Rough.txt line means; do not assume the old hand-written categories map one-to-one with Studio PC API modules.

| Topic | Official source | What it is useful for | What it does not provide in this research pass |
|---|---|---|---|
| Main Block Scripts guide | [Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101) | Editor layout, block panel/search, script list/context, script-type toggle, templates and typed connections. It says category panel entries are context-sensitive; search can return blocks unavailable in the selected script context. | A complete machine-readable catalog of every block and dropdown option. |
| Purpose, operation and debugging | [The Purpose, Operation Rules, and Debugging Methods of Blocks](https://ffcraftland.garena.com/en/tutorial/cl/4-102/) | How to interpret block operation and debug feedback. | A full node/socket schema export. |
| Event/script types | [Event and Script Types](https://ffcraftland.garena.com/en/tutorial/cl/4-103/) | Event-start logic and script-type distinctions. | Proof that a block works in every script scope. |
| Classification and flow control | [Block Classification and Flow Control](https://ffcraftland.garena.com/en/tutorial/cl/4-104/) | How blocks are grouped and how flow-control constructs behave. | A full live list of category members. |
| Variables, properties and assignment | [Variables and Properties, Assignment](https://ffcraftland.garena.com/en/tutorial/cl/4-105/) | Separating variables from entity properties and assignment operations. | Every possible property key or dynamic asset option. |
| Data and logic | [Data and Logic Operations](https://ffcraftland.garena.com/en/tutorial/cl/4-106/) | Data/value operations and logical expression concepts. | An exact enumeration of every operator block in the current editor. |
| Server/client scripts | [Server-side and client-side scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-107/) | Runtime-side separation and context constraints. | An exhaustive API compatibility matrix by itself. |

## Mechanism examples that are worth mining

Two official re-editable templates contain worked examples rather than only abstract explanations:

- [Game Mechanics](https://ffcraftland.garena.com/en/tutorial/cl/4-87) — examples include custom triggers, health adjustment, zombie spawning, object movement, player teleportation, custom text, outfit changes and HUD UI interaction.
- [Myconsole](https://ffcraftland.garena.com/en/tutorial/cl/4-86) — examples include HUD interaction, player body proportions, random terrain generation, player join/leave lists and custom helper functions.

The public translated tutorial corpus already summarizes 13 Game Mechanics recipes in [research/mobile-block-recipe-index.json](../research/mobile-block-recipe-index.json). This new map links those recipe examples back to current official topic pages and clarifies what can and cannot be inferred from documentation alone.

## Inventory rules that follow from these pages

1. **Record script context for every block.** A result in the block search field does not prove the block is valid in the currently selected script.
2. **Record both the block and its sockets.** Store display name, category, event/action/value role where known, inputs, output type, and typed slot constraints. A label-only match is insufficient for code generation.
3. **Treat scope and runtime side as separate dimensions.** Global/player/team/object/UI placement and server/client availability should not be collapsed into one boolean.
4. **Keep Mobile and PC inventories distinct.** A similarly named PC function or .fcc declaration is a cross-reference candidate, not a substitute for Mobile evidence.
5. **Keep enum type and its options separate.** Record each option's visible label and canonical/internal value if the editor reveals both; capture every scrolled segment of long dynamic lists.
6. **Preserve unknowns instead of filling gaps by intuition.** If the official page explains a concept but doesn't expose the exact current dropdown list, mark that list as `not-captured`.

## Current coverage status

This research pass has navigable, official documentation for the seven topic areas above and summary leads for 13 mechanisms. It still does **not** have a complete current screenshot/export set for the Mobile block panel or all of its expanded dropdowns. The highest-priority remaining Mobile evidence is the unknown/fuzzy subset from [the Rough crosswalk](24-block-symbol-crosswalk.md), plus dynamic skin/asset selectors and context-sensitive blocks.

## Sources

- [Official Craftland Mobile Block Scripts guide](https://ffcraftland.garena.com/en/tutorial/cl/4-101)
- [Official Craftland Mobile scripting topic pages 4-102 through 4-107](https://ffcraftland.garena.com/en/tutorial/cl/4-102/)
- [Official Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87)
- [Official Myconsole template](https://ffcraftland.garena.com/en/tutorial/cl/4-86)
- [Public tutorial corpus audit](25-public-tutorial-corpus-audit.md)
- [Current editor capture playbook](27-current-editor-capture-playbook.md)
