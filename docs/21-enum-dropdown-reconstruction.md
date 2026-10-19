# Dropdown / enum reconstruction crosswalk

## Purpose

Rahul's original `Rough.txt` lists many dropdown/type labels but intentionally omits most dropdown entries to save time. This page and its JSON file map those labels to discoverable definitions without changing the original notes.

- Original notes: [`Rough.txt`](../Rough.txt) — preserved unchanged.
- Machine-readable crosswalk: [`research/enum-dropdown-crosswalk.json`](../research/enum-dropdown-crosswalk.json)
- Recovered library symbols: [`research/pc-library-symbol-catalog.json`](../research/pc-library-symbol-catalog.json)
- Official current additions: [`research/current-official-enum-supplement.json`](../research/current-official-enum-supplement.json)

## Current crosswalk result

The 65 dropdown/type labels recorded in `Rough.txt` have been assigned the following research states:

- 53 candidate mappings to enum definitions in the public 1.5.0 extension-library mirror.
- 2 official enum/type labels discovered in the current Garena docs but absent from that mirror (`TypeEnum` and `RenderQualityType`).
- 1 texture label confirmed by both the official reference and mirror.
- 4 skin-type dropdowns confirmed by the official docs as dynamic ID types rather than fixed small enums.
- 3 legacy labels requiring obsolete/deprecation caution.
- 2 still needing manual review (`Loot Scorer Type` and `Phase And Round Enum`).

These categories describe the 65 labels, not the number of actual dropdown options. The JSON retains each candidate, member-count estimate, source file SHA, original Rough line and the next verification step.

## Important distinctions

**A type name is not necessarily an enum with a fixed member list.** The current official enum reference documents `TypeEnum` as the list of available types. It also identifies `WeaponSkinType`, `VehicleSkinType`, `ClothType`, and `BagSkinType` as values typed by Weapon Skin ID, Vehicle Skin ID, Outfit ID, and Backpack Skin ID. Those asset IDs are potentially much larger/dynamic lists; they are not accurately reconstructed by copying a 1.5-era enum.

**The old mirror is a discovery snapshot.** It provides useful member and identifier lists for labels such as Item ID, sound effects, icons, dynamic level objects, weapons, loot, and HUD widget types, but its version and empty license file mean we retain only a derivative identifier/signature index and links. It does not establish that every entry is still present in the latest editor.

**PC and Mobile must be cross-checked separately.** PC `.fcc` declarations help discover an API or enum but do not prove it appears as a Craftland Mobile visual block, nor that the same options exist in both editors.

## Current official references worth mining further

- [Enum reference](https://ffcraftland.garena.com/en/docs/enum/)
- [Type reference](https://ffcraftland.garena.com/en/docs/type)
- [Level Object module](https://ffcraftland.garena.com/en/docs/module-26) — explicitly lists Level Object Type, Weapon Skin Type, Vehicle Skin Type, Outfit Skin Type, Backpack Skin Type, and Object Texture.
- [API reference](https://ffcraftland.garena.com/en/docs/api)
- [Official Mobile block scripting guide](https://ffcraftland.garena.com/en/tutorial/cl/4-101)
- [Official PC code scripting guide](https://ffcraftland.garena.com/en/tutorial/fe/1-9)

## Remaining work

1. Inspect all 2,274 extracted enum-member entries against the live official pages, and preserve the official display label, script name, numerical/string value, description, and deprecation status wherever available.
2. Extract newer APIs and types from the latest official reference—not only the 1.5.0 mirror.
3. Build a separate visual-block crosswalk from current Mobile/PC editor screenshots or templates, including exact slots, drop-down labels, input/output types, and scope.
4. For dynamic asset selectors, seek current official catalogs or project-generated `EditorGenLib.fcc` rather than guessing IDs.
5. Mark every entry as official-current, official-obsolete, mirror-only, user-observed, or runtime-tested. None is runtime-tested by this document.

## What is still not claimed

This crosswalk is not a complete current dropdown dump, not an official API compatibility matrix, and not evidence of a compiled or live-tested map. It is a structured gap map so subsequent research can close those gaps systematically.
