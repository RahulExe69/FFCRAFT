# Dropdown / enum reconstruction crosswalk

## Purpose

Rahul's original `Rough.txt` lists many dropdown/type labels but intentionally omits most dropdown entries to save time. This page and its JSON file map those labels to discoverable definitions without changing the original notes.

- Original notes: [`Rough.txt`](../Rough.txt) — preserved unchanged.
- Machine-readable crosswalk: [`research/enum-dropdown-crosswalk.json`](../research/enum-dropdown-crosswalk.json)
- Recovered library symbols: [`research/pc-library-symbol-catalog.json`](../research/pc-library-symbol-catalog.json)
- Official current additions: [`research/current-official-enum-supplement.json`](../research/current-official-enum-supplement.json)

## Current crosswalk result

The 65 dropdown/type labels recorded in `Rough.txt` have been assigned the following research states:

- 30 candidate mappings still based only on the public 1.5.0 extension-library mirror.
- 2 official enum/type labels discovered in the current Garena docs but absent from that mirror (`TypeEnum` and `RenderQualityType`).
- 23 labels now cross-checked against current official tables and the old mirror (including texture, loot, animation, AI, combat and HUD-related enums).
- 4 skin-type dropdowns confirmed by the official docs as dynamic ID types rather than fixed small enums.
- 3 legacy labels requiring obsolete/deprecation caution.
- 0 unresolved type-to-enum mappings remain in the manual-review bucket. `Loot Scorer Type` is now a likely spelling/transcription variation of the official `Loot Soccer Type` (`LootSoccerType`), with its three current documented options recorded below; only the exact visible label needs a current-editor screenshot if wording must be proven.
- 1 label clarified by current official docs as **not an enum**: `Phase And Round Enum` points toward the Workflow `Phase` and `Round` entity/component types, current phase/round indices, and their start/end events; no enum member list should be invented.

These categories describe the 65 labels, not the number of actual dropdown options. The JSON retains each candidate, member-count estimate, source file SHA, original Rough line and the next verification step.


### Loot Scorer / Loot Soccer Type: likely transcription correction

The current [official Enum reference](https://ffcraftland.garena.com/en/docs/enum/) lists **Loot Soccer Type**, identifier `LootSoccerType`, in the Football module. It provides these three entries:

| Numeric value | Display name | Script name | Description |
|---:|---|---|---|
| 1040 | Loot Soccer Random | `LootSoccerRandom` | Loot Soccer Random |
| 1038 | Loot Soccer Shield | `LootSoccerShield` | Loot Soccer Shield |
| 1039 | Loot Soccer Ice | `LootSoccerIce` | Freezing Grenade |

The older PC library mirror has the same identifier and three values. Since the raw note says `Loot Scorer Type` while official documentation says `Loot Soccer Type`, the crosswalk now records a **likely typo/transcription match**, not a silent edit to `Rough.txt`. A current editor screenshot is still the best evidence for the exact visible dropdown wording.

### Phase / Round label: classification now clarified

The [official Workflow manual](https://ffcraftland.garena.com/en/tutorial/fe/1-14/) describes phases and rounds as configurable game-flow entities. The official [Phase type](https://ffcraftland.garena.com/en/docs/type-25/), [Round type](https://ffcraftland.garena.com/en/docs/type-26/) and [Global entity properties](https://ffcraftland.garena.com/en/docs/type-11/) identify these as component/entity concepts; the Global entity exposes `CurrentPhaseIndex` and `CurrentRoundIndex`. Separate `On Phase Start/End` and `On Round Start/End` events have different parameter shapes (phase entity versus round index). The official [On Phase Start declaration](https://ffcraftland.garena.com/en/docs/event-18-5/) gives an explicit example.

This is enough to correct the **classification** of the Rough.txt label: do not build a fictitious `PhaseAndRoundEnum` or invent values. It does not settle whether the label in the author's original editor panel was a selector or a rough heading; that requires a screenshot of the current UI. Related Workflow API pages can be platform-marked Both Mobile and PC, but that still does not mean the Mobile editor has an identically named dropdown.

The [current official dropdown option cross-check](30-current-official-dropdown-option-crosschecks.md) now records 108 current published option rows across 24 rough labels, with official display names, script names, values and old-mirror alias notes. It is a cross-check subset, not a complete scrape; it deliberately keeps Mobile UI parity and runtime support unclaimed. The corresponding entries in the machine-readable crosswalk link to that dataset.

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
