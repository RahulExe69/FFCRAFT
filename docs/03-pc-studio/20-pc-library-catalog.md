# PC library catalog recovered from a public extension mirror

## Why this exists

`Rough.txt` remains the untouched, user-authored handwritten inventory. The new catalog is a separate discovery aid for the parts that were hard to transcribe by hand: enum-like dropdown choices and the exact API/event/component identifiers used by Craftland Studio PC.

## Discovery result

A publicly accessible repository mirror of the Free Fire Craftland Code VS Code extension contains 42 text `.fcc` library files under `library/release/`. A lightweight parser extracted this snapshot:

- 42 library files
- 144 enum declarations
- 2,274 enum member entries
- 681 function declaration candidates
- 259 event declaration candidates
- 419 component names
- 20 aliases and 50 declared type names

These are parser counts from the mirrored snapshot, not guaranteed counts of distinct, current, supported blocks. Aliases/repeated compatibility definitions are included. A function declaration is not necessarily a visual block; a `.fcc` enum is not proof the Mobile editor exposes the same dropdown.

## Start here

- Machine-readable symbol catalog: [`research/pc-library-symbol-catalog.json`](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/pc-library-symbol-catalog.json)
- User-observed enum/block inventory: [`research/user-observed-block-inventory.json`](https://github.com/RahulExe69/FFCRAFT/blob/main/research/mobile/user-observed-block-inventory.json)
- Untouched original notes: [`Rough.txt`](https://github.com/RahulExe69/FFCRAFT/blob/main/notes/raw/Rough.txt)
- Public mirror: https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0/tree/main/library/release
- Official extension listing: https://marketplace.visualstudio.com/items?itemName=craftLandstudio.ffugclanguage
- Official API docs: https://ffcraftland.garena.com/en/docs/api
- Official events: https://ffcraftland.garena.com/en/docs/event/
- Official types/components: https://ffcraftland.garena.com/en/docs/type
- Official enums: https://ffcraftland.garena.com/en/docs/enum/
- Official PC code-script manual: https://ffcraftland.garena.com/en/tutorial/fe/1-9

## Important source/version warning

The mirrored extension's `package.json` identifies version **1.5.0** and the mirror's `LICENSE.md` is empty. The current official Craftland patch notes have reached Studio **1.19.0 (September 2026)** and include newer script/API and editor capabilities. Therefore:

1. Use this catalog to discover names, enum values, and promising references.
2. Cross-check each entry against the current official docs and the libraries installed with the target Studio build.
3. Prefer current official documentation and current installed libraries when they disagree.
4. Keep old/deprecated/preview declarations visibly flagged; do not recommend obsolete items for new maps.
5. Do not copy or redistribute the mirror's executable binaries or raw `.fcc` library files into FFCRAFT.
6. Do not assume PC code/API definitions map 1:1 to Craftland Mobile visual blocks. Validate Mobile block slots and dropdowns independently.

## What this unlocks

The largest extracted enums include 211 item-ID entries, 155 dynamic-create level-object entries, 102 sound-effect entries, 96 icon entries, 75 level-object entries, 71 VFX/effect entries, 63 player UI switch entries, and 61 built-in HUD entries. Some of these are aliases or duplicate legacy types, so they should be deduplicated only after the relationship is documented.

The next research pass is to map each enum label mentioned in `Rough.txt` to the best source definition, flag mismatches/missing entries, and then build a separate current-version crosswalk for visual-block dropdowns. For missing dropdowns, likely routes include current official enum/API pages, the latest official extension package, generated project-level `EditorGenLib.fcc` files, and screenshots/exported blocks from the target editor.

## Supplementary legacy symbol index

A companion `BuiltinSymbol.json` exists in the same public extension mirror. It indexes symbols by library path and records numeric IDs for components, APIs and component properties. A separate [audit](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/07-research-audits/32-legacy-builtin-symbol-index-audit.md) counted 590 component records, 3,315 component-property records, 150 enum records, 739 API records and 259 event records across 42 file spaces.

These counts are not directly interchangeable with the parser counts above: repeated library-scoped names, aliases and extraction rules differ. The index is version 1.5.0, its upstream license is not affirmatively declared, and the raw JSON has not been copied into FFCRAFT. Use it only as a version-labelled discovery/cross-check source until the current installed editor confirms the IDs and declarations.

## Reproducibility and limits

The JSON includes source file paths and blob SHAs to identify precisely which snapshot was inspected. The catalog records identifiers/signatures and does not claim a successful import, compile, or in-game test. A downloaded mirror may be incomplete or stale, and the local editor's generated asset library may contain project-specific symbols not found in the public standard libraries.
