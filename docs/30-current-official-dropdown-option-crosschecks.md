# Current official dropdown option cross-checks

**Checked:** 20 October 2026  
**Machine-readable option rows:** [`research/official-dropdown-option-crosschecks.json`](../research/official-dropdown-option-crosschecks.json)  
**Official source:** [Garena Craftland Enum reference](https://ffcraftland.garena.com/en/docs/enum/)

## What this adds

This is a current official-doc cross-check for **24 labels found in or directly related to the ENUM section of `Rough.txt`**. The structured dataset contains **108 option rows** with each visible numeric value, display name, script name and description. It also records the older library mirror's member counts and known aliases.

It is intentionally a *subset*, not a complete scrape of the official reference. It also does not prove every listed enum is exposed as the same dropdown in Craftland Mobile.

## Labels covered

- Loot tables: Loot Ammo, Loot Consumable, Loot Armor, Loot Throwable, Loot Scope, Loot Weapon, and Loot Soccer (the likely canonical match for the Rough.txt label `Loot Scorer Type`).
- Workflow/animation and property behavior: Damage Type, Buff Type, Property Modify Type, Movable Platform Type, `LoopType`, Fill Type, Fill Direction Type, and 3-Status Switch.
- Gameplay and AI: Player Revival Source Type, Patrol Type, Patrol Style Type, Aim Assist Type, Gender Type, Knock-down Type, Fire Type, Camera Viewing Angle Restriction Type, and Layout Sort Type.

## Why comparing the source versions matters

The 1.5.0 mirror includes several deprecated aliases that share the same numeric value as a current documented option. The current official table shows the canonical option rows without those aliases for the following examples:

| Label | Current official options visible | Extra old-mirror rows to treat cautiously |
|---|---:|---|
| Loot Ammo Type | 7 | `LootAmmoRandom` = 1014 |
| Loot Consumable Type | 6 | `LootConsumableItemRandom` = 1024, `Cardiotonic` = 1021, `Glooshield` = 1023 |
| Loot Armor Type | 4 | `LootArmorRandom` = 1018 |
| Loot Throwable Type | 5 | `LootThrowableRandom` = 1029, `Flash` = 1026, `FrozenGrenade` = 1028 |
| Loot Scope Type | 4 | `LootSightRandom` = 1036, `Sight2` = 1032, `Sight4` = 1033, `HeatSight` = 1035 |
| Loot Weapon Type | 9 | `FootGun` = 1041 |
| Property Modify Type | 2 | `Mul` = 2 |
| Movable Platform Type | 3 | `Translate` = 0 |
| `LoopType` | 3 | `NotChange` = 0 |
| Knock-down Type | 3 | `MustKnockDown` = 2 |
| Layout Sort Type | 3 | `SortByHierarchy` = 0 |

These are **source-list differences**, not a claim that the editor compiler will reject every alias. Use the current installed editor/library to settle compilation support and the actual choices visible in a particular UI.

Other comparison notes: current official Damage Type has a `Finishing Move` row (`ExecuteSkill = -40`) not present in the old mirror, while several aliases in the old mirror are marked deprecated and omitted from the current table. Buff Type similarly omits the mirror's deprecated `AmmoBuff` alias. The official Fill Type values skip numeric value 4, so the list must not be renumbered. The 3-Status Switch official identifier is `ThreeStatusSwitch` while the mirror uses `CommonUISwitchValue` and `CommonHudSwitchValue` for matching option sets; keep type identity separate. The official Camera Viewing Angle Restriction Type leaves script-name cells blank.

One notable spelling discrepancy remains visible in the docs: Patrol Type displays `Cylic` while its script name is `Cyclic`; the older mirror labels `Cylic` as a deprecated alias. Preserve both exact fields and verify the installed editor rather than normalizing this silently.

## Loot Scorer → Loot Soccer

The official Enum reference calls the value set **Loot Soccer Type**, identifier `LootSoccerType`, under Football:

| Value | Official display name | Script name |
|---:|---|---|
| 1040 | Loot Soccer Random | `LootSoccerRandom` |
| 1038 | Loot Soccer Shield | `LootSoccerShield` |
| 1039 | Loot Soccer Ice | `LootSoccerIce` |

This is a strong likely match for the original `Loot Scorer Type` spelling, but the raw notes are preserved. Capture a screenshot if the exact visible wording of that dropdown matters.

## How to consume the JSON

Each entry records the rough label, canonical identifier, module, value type, official URL, ordered option rows, old mirrored member count, known deprecated aliases/spelling conflicts and interpretation notes. Keep display labels separate from script identifiers and numerical values. Do not reorder or renumber values based on assumptions.

## Coverage limits and next steps

- No runtime compilation or gameplay test is claimed.
- Mobile parity is **not** inferred from the PC language-library snapshot.
- Some dropdowns are dynamic ID/type selectors, not fixed enums.
- The old mirror has 42 files but represents v1.5.0; compare against the installed current library for exact current declarations.
- Next, expand the official cross-check to the remaining labels and separately gather current Mobile dropdown screenshots/exports.

## Sources

- [Official Enum reference](https://ffcraftland.garena.com/en/docs/enum/)
- [Older 1.5.0 library symbol catalog](20-pc-library-catalog.md)
- [Dropdown / enum reconstruction crosswalk](21-enum-dropdown-reconstruction.md)
- [Current editor capture playbook](27-current-editor-capture-playbook.md)
