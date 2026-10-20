# Current official dropdown option cross-checks

**Checked:** 21 October 2026  
**Machine-readable option rows:** [`research/official-dropdown-option-crosschecks.json`](../research/official-dropdown-option-crosschecks.json)  
**Official source:** [Garena Craftland Enum reference](https://ffcraftland.garena.com/en/docs/enum/)

## What this adds

This is a current official-doc cross-check for **39 labels found in or directly related to the ENUM section of `Rough.txt`**. The structured dataset contains **214 official-reference option rows** with each visible numeric value, display name, script name and description. It also records the older library mirror's member counts and known aliases.

It is intentionally a *subset*, not a complete scrape of the official reference. It also does not prove every listed enum is exposed as the same dropdown in Craftland Mobile.

## Labels covered

- Loot tables: Loot Ammo, Loot Consumable, Loot Armor, Loot Throwable, Loot Scope, Loot Weapon, and Loot Soccer (the likely canonical match for the Rough.txt label `Loot Scorer Type`).
- Workflow/animation and property behavior: Damage Type, Buff Type, Property Modify Type, Movable Platform Type, `LoopType`, Fill Type, Fill Direction Type, 3-Status Switch, and Money Type.
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

## Money Type

The current official table lists a single `MoneyType` value: `1 Basic` — described as the base currency type used for general shop-item pricing. The old mirror agrees. Do not infer additional enum values from the fact that the label says “Money Type.”

## Loot Scorer → Loot Soccer

The official Enum reference calls the value set **Loot Soccer Type**, identifier `LootSoccerType`, under Football:

| Value | Official display name | Script name |
|---:|---|---|
| 1040 | Loot Soccer Random | `LootSoccerRandom` |
| 1038 | Loot Soccer Shield | `LootSoccerShield` |
| 1039 | Loot Soccer Ice | `LootSoccerIce` |

This is a strong likely match for the original `Loot Scorer Type` spelling, but the raw notes are preserved. Capture a screenshot if the exact visible wording of that dropdown matters.

## Additional current official rows captured

The source data now also records visible current-official rows for fourteen more labels from the original notes (six labels added in the most recent pass). These rows are stored as the full visible row fields (value, display label, script name, description) in the JSON. Where the old v1.5.0 library has a substantially larger list, that discrepancy is deliberately left unresolved pending an installed-editor capture.

| Rough label | Current official rows captured | Old-mirror member count | Interpretation |
|---|---:|---:|---|
| VFX Type | 7 | 71 | Major mismatch; old-only names need current-editor verification. |
| Sound Effect Type | 10 | 102 | Major mismatch; do not assume either list is the live dropdown. |
| Special ID Type | 1 | 1 | Gloo Maker / IceWallMaker; source lists agree. |
| Monster Type | 4 | 13 | Old mirror includes a deprecated alias and additional types not visible in the current official table. |
| Object Texture | 15 | 35 | Old mirror includes multiple deprecated aliases and other older names. |
| Font Type | 6 | 7 | HindSiliguri appears in the old mirror but not the current official table. |
| SkyboxType | 6 | 8 | CityBuilding and Snow are old-mirror aliases marked deprecated. |
| Render Quality Type | 4 | 0 | Current official enum missing from the old mirror; Get Render Quality is documented as Client Side and Both Mobile and PC. |
| Equipment Type | 12 | 24 | Visible official rows are fewer than old-mirror members; installed editor verification remains open. |
| Switch Equip Slot | 11 | 17 | Visible official rows are fewer than old-mirror members; preserve non-contiguous IDs. |
| Coordinate System Type | 2 | 2 | Official table and old mirror agree on two rows. |
| Action Type | 3 | 3 | Official table and old mirror agree on three rows. |
| Status Code | 5 | 24 | Official page shows five rows; old-only codes need current editor verification. |
| Player UI Type | 19 | 63 | Non-contiguous current-page values; old mirror has many more members. |

For VFX, Sound Effect, Monster, Object Texture and Font Type, the option-row count above is the number of rows visible in the official reference snapshot, not an assertion that the installed editor must expose exactly that many entries. The old-mirror count difference is a reason to capture the current library/editor—not permission to call entries removed or supported by guesswork. Skybox options also cross-reference the curated asset dataset; package import/playtest status is separate.

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
