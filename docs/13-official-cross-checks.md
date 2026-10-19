# First official cross-check pass

**Checked:** 20 October 2026  
**Scope:** small, source-backed comparison against official Garena docs; not a complete validation of the 441 candidate lines.

## What is confirmed by the official documentation

### 1. Block scripts are context-sensitive and use typed slots

Garena's [Block Scripts guide](https://ffcraftland.garena.com/en/tutorial/cl/4-101) describes default global, party, and player scripts, plus scripts attached to individual objects and UI elements. It also distinguishes block scripts from client-side scripts and warns that some blocks are inactive in an incompatible script type. Block parameter slots show what type of value is expected.

**Implication for FFCRAFT:** preserve each signature's slot labels and script context. The `GLOBAL / TEAM / PLAYER` wording in `Rough.txt` needs a nomenclature check because the current guide uses **party** in this context. We should not silently equate TEAM with party until we confirm the editor version and semantics.

### 2. Official API, event, type, and enum references are separate

The [official API reference index](https://ffcraftland.garena.com/en/docs/api) has distinct reference areas for **API**, **Event**, **Type**, and **Enum**. Its modules include standard library, list, map, math, strings, conversion, scene, items, combat, HUD, level objects, playable, animation, behavior tree, player, team, workflow, physics, camera, minimap, collection, economy, data storage, football, morph, and more.

This means the seven-category layout recorded in `Rough.txt` is valuable as the author's observed block-panel structure, but it is not necessarily a one-to-one copy of Garena's API taxonomy. FFCRAFT should retain both labels and attach cross-references only where verified.

### 3. Three enum-like entries in the rough list are explicitly obsolete

The current [official enum reference](https://ffcraftland.garena.com/en/docs/enum/) marks the following as obsolete:

| Rough.txt entry | Official reference label | Current handling |
|---|---|---|
| `Character skill` | `PlayerSkillType` | Obsolete; don't recommend for new logic |
| `Score Type` | `ScoreType` | Obsolete; don't recommend for new logic |
| `Effect Texture Type` | `PresentEffectTextureType_Deprecated` | Obsolete; don't recommend for new logic |

This does **not** mean your transcription was wrong. It means those names really are useful to keep for understanding existing maps, but they must be flagged before new code is generated.

### 4. Types are first-class catalogue entries, not just dropdowns

The [official type reference](https://ffcraftland.garena.com/en/docs/type) lists types such as `Entity`, `Property`, `Event ID`, `Bool`, `Int`, `Float`, `Int64`, `Number`, `String`, `Color`, asset IDs, `List`, `Map`, `Vector2`, `Vector3`, `Quaternion`, and many others. The type pages themselves can carry obsolete labels.

**Implication for FFCRAFT:** create separate indexed records for block labels, parameter types, outputs, enum types, enum values, and assets. The seven variable types in the rough note should not be treated as the whole underlying type system.

### 5. Some standard-library names overlap with official references

The official [STD Library module index](https://ffcraftland.garena.com/en/docs/module-1) lists names including `Get All Players`, `Get All Teams`, `Set All Players Move Status`, `Wait For Next Frame`, `Break loop`, `Continue to next`, and related helpers.

These are **name-level cross-checks only**. For code generation, each block still needs the exact declaration, argument and return types, async rules, script-side support, Mobile/PC availability, and deprecation status.

## Unresolved and potentially confusing areas

- **`DATA - DICTIONARY`** currently contains `Create Random Seed` and `Next` in the rough notes. These look like random-seed helpers, so the heading may be misplaced or the editor's grouping may need a closer look.
- **Cylinder test blocks:** two entries are recorded as `Is Inside Cylinder` but have different parameter shapes. Keep both raw signatures until verified.
- **Spelling/label variants:** entries such as `Gey Owner`, `Parnt`, `LIAT`, and `Knok-down` remain untouched in the original file; the cleaned layer should store canonical names separately instead of rewriting the source.
- **Platform split:** the mobile tutorial and Studio PC documentation are separate. Do not assume every observed visual block corresponds to a PC code API, or that every documented PC API is available in Mobile.
- **Scope visibility:** the variable/function sharing rules in `Rough.txt` are firsthand observations and still need confirmation in the target version.

## Next verification sequence

1. Confirm the current editor version and whether the inventory was taken from Craftland Mobile, Craftland Studio PC, or a particular version of both.
2. Crosswalk each rough entry to an official API/event/type/enum page and record the canonical identifier, declaration, required types, outputs, side/platform support, and obsolete status.
3. Enumerate the **values inside** every enum dropdown. The existing list contains 65 enum-like type names; it does not yet contain every option within them.
4. Fill gaps using screenshots or exported editor/library files when the official pages don't expose the visual-block shape.
5. Mark each record `documented`, `editor-observed`, `compiled`, or `playtested` as those separate levels of evidence are achieved.

Machine-readable cross-checks are stored in [`research/user-observed-block-inventory.json`](../research/user-observed-block-inventory.json).
